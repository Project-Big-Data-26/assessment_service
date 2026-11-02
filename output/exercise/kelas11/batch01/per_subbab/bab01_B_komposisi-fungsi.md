# Lembar koreksi — kelas11 SMA11U-B1 subbab B: Komposisi Fungsi

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11-b01-b-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: evaluasi nilai komposisi*

Diketahui beberapa nilai fungsi sebagai berikut:
$f(4) = 9$, $g(4) = 8$, $f(8) = 15$, dan $g(8) = 14$.
Nilai dari $(f \circ g)(4)$ adalah ....

- A. $14$  
  <sub>Salah: Siswa tertukar urutan komposisi menjadi $(g \circ f)(4)$ lalu salah membaca $g(8)$.</sub>
- B. $9$  
  <sub>Salah: Siswa langsung mengambil nilai $f(4)$ tanpa mengevaluasi $g(4)$ terlebih dahulu.</sub>
- C. $72$  
  <sub>Salah: Siswa mengalikan nilai $f(4)$ dengan $g(4)$, yaitu $9 \times 8 = 72$.</sub>
- **D. $15$** ✅  
  <sub>Benar: $(f \circ g)(4) = f(g(4)) = f(8) = 15$.</sub>

**Pembahasan:** Berdasarkan definisi komposisi fungsi:
$$(f \circ g)(4) = f(g(4))$$
Dari data yang diketahui, nilai $g(4) = 8$. Substitusikan ke dalam $f$:
$$f(g(4)) = f(8) = 15$$
Jadi, nilai dari $(f \circ g)(4)$ adalah $15$.
**Acuan:** pretest — kelas11-b01-p0047-latihan-14-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11-b01-b-easy-bt01-002
*variasi (angka) | C2 | 1 langkah | jenis: aljabar komposisi fungsi*

Diketahui fungsi $f(x) = x + 7$ dan $g(x) = \sqrt{x}$. Rumus fungsi $h(x) = (g \circ f)(x)$ adalah ....

- A. $\sqrt{x - 7}$  
  <sub>Salah: Siswa keliru menggunakan tanda pengurangan saat mensubstitusikan $f(x)$.</sub>
- B. $\sqrt{x} + 7$  
  <sub>Salah: Siswa menjumlahkan $g(x) + 7$ alih-alih memasukkan $x + 7$ ke dalam tanda akar.</sub>
- **C. $\sqrt{x + 7}$** ✅  
  <sub>Benar: $h(x) = g(f(x)) = g(x + 7) = \sqrt{x + 7}$.</sub>
- D. $\sqrt{x} - 7$  
  <sub>Salah: Siswa salah memasukkan fungsi dan salah menulis tanda operasi.</sub>

**Pembahasan:** Komposisi fungsi didefinisikan sebagai:
$$h(x) = (g \circ f)(x) = g(f(x))$$
Substitusikan $f(x) = x + 7$ ke dalam rumus fungsi $g(x) = \sqrt{x}$:
$$g(f(x)) = g(x + 7) = \sqrt{x + 7}$$
Jadi, rumus fungsi $h(x)$ adalah $\sqrt{x + 7}$.
**Acuan:** siswa — siswa hal.43 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11-b01-b-easy-bt01-003
*orisinal | C1 | 1 langkah | jenis: konsep syarat komposisi*

Dua fungsi $f$ dan $g$ dapat dikomposisikan menjadi $(f \circ g)(x)$ apabila ....

- A. daerah asal (domain) $f$ harus sama persis dengan daerah asal (domain) $g$  
  <sub>Salah: Siswa mengira domain kedua fungsi harus identik seperti pada operasi penjumlahan.</sub>
- B. daerah asal (domain) dari $g$ merupakan himpunan bagian dari daerah hasil (range) $f$  
  <sub>Salah: Siswa tertukar antara daerah asal dan daerah hasil.</sub>
- C. daerah hasil (range) dari $f$ merupakan himpunan bagian dari daerah asal (domain) $g$  
  <sub>Salah: Siswa tertukar urutan fungsi yang diproses duluan ($f$ dan $g$ terbalik).</sub>
- **D. daerah hasil (range) dari $g$ merupakan himpunan bagian dari daerah asal (domain) $f$** ✅  
  <sub>Benar: Syarat eksistensi $(f \circ g)$ adalah $R_g \subseteq D_f$.</sub>

**Pembahasan:** Berdasarkan buku siswa halaman 44, syarat agar dua fungsi $f$ dan $g$ dapat dikomposisikan sebagai $f \circ g$ adalah range (daerah hasil) dari $g$ merupakan himpunan bagian dari domain (daerah asal) $f$ (dituliskan $R_g \subseteq D_f$).
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11-b01-b-easy-bt01-004
*orisinal | C2 | 1 langkah | jenis: operasi aljabar fungsi*

Diketahui fungsi $f(x) = 6x + 5$ dan $g(x) = 2x - 8$. Rumus fungsi $(f + g)(x)$ adalah ....

- A. $8x + 3$  
  <sub>Salah: Siswa salah tanda saat menjumlahkan $5 + (-8)$ menjadi $+3$.</sub>
- **B. $8x - 3$** ✅  
  <sub>Benar: $(f + g)(x) = (6x + 5) + (2x - 8) = 8x - 3$.</sub>
- C. $4x + 13$  
  <sub>Salah: Siswa melakukan pengurangan koefisien $6 - 2 = 4$ dan salah tanda konstanta.</sub>
- D. $8x + 13$  
  <sub>Salah: Siswa salah menghitung konstanta: $5 - (-8) = 13$ alih-alih $5 + (-8) = -3$.</sub>

**Pembahasan:** Berdasarkan rumus penjumlahan dua fungsi:
$$(f + g)(x) = f(x) + g(x)$$
Substitusikan masing-masing fungsi:
$$(f + g)(x) = (6x + 5) + (2x - 8)$$
Jumlahkan suku-suku yang sejenis:
$$(6x + 2x) + (5 - 8) = 8x - 3$$
Jadi, rumus fungsi $(f + g)(x)$ adalah $8x - 3$.
**Acuan:** siswa — siswa hal.37

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11-b01-b-easy-bt01-005
*variasi (angka) | C2 | 1 langkah | jenis: perkalian fungsi*

Diketahui beberapa nilai fungsi sebagai berikut: $f(5) = 8$, $g(5) = 4$, $f(4) = 11$, dan $g(4) = 10$. Nilai dari $(f \cdot g)(5)$ adalah ....

- **A. $32$** ✅  
  <sub>Benar: $(f \cdot g)(5) = f(5) \times g(5) = 8 \times 4 = 32$.</sub>
- B. $12$  
  <sub>Salah: Siswa menjumlahkan $f(5) + g(5) = 8 + 4$ alih-alih mengalikan.</sub>
- C. $88$  
  <sub>Salah: Siswa mengalikan nilai $f(5) \times f(4) = 8 \times 11 = 88$.</sub>
- D. $110$  
  <sub>Salah: Siswa salah menggunakan nilai pada $x = 4$, yaitu $f(4) \times g(4) = 11 \times 10 = 110$.</sub>

**Pembahasan:** Berdasarkan definisi operasi perkalian fungsi, $(f \cdot g)(x) = f(x) \cdot g(x)$.
Untuk $x = 5$:
$(f \cdot g)(5) = f(5) \cdot g(5) = 8 \times 4 = 32$.
Jadi, nilai dari $(f \cdot g)(5)$ adalah $32$.
**Acuan:** pretest — kelas11-b01-p0040-latihan-13-6c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11-b01-b-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: evaluasi nilai komposisi*

Jika diketahui $f(2) = 5$, $g(2) = 7$, $f(7) = 16$, dan $g(7) = 9$, maka nilai dari $(f \circ g)(2)$ adalah ....

- **A. $16$** ✅  
  <sub>Benar: $(f \circ g)(2) = f(g(2)) = f(7) = 16$.</sub>
- B. $35$  
  <sub>Salah: Siswa mengalikan nilai $f(2) \times g(2) = 5 \times 7 = 35$ alih-alih mengomposisikannya.</sub>
- C. $5$  
  <sub>Salah: Siswa langsung mengambil nilai $f(2) = 5$ tanpa mengevaluasi fungsi dalam $g(2)$ terlebih dahulu.</sub>
- D. $9$  
  <sub>Salah: Siswa menghitung $(g \circ g)(2) = g(g(2)) = g(7) = 9$.</sub>

**Pembahasan:** Berdasarkan definisi komposisi fungsi:
$(f \circ g)(2) = f(g(2))
Diketahui $g(2) = 7$, sehingga:
$f(g(2)) = f(7) = 16$.
Jadi, nilai dari $(f \circ g)(2)$ adalah $16$.
**Acuan:** pretest — kelas11-b01-p0047-latihan-14-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11-b01-b-easy-bt01-007
*variasi (angka) | C2 | 1 langkah | jenis: pengurangan fungsi*

Jika $f(4) = 15$, $g(4) = 9$, $f(9) = 20$, dan $g(9) = 18$, maka nilai dari $(f - g)(4)$ adalah ....

- **A. $6$** ✅  
  <sub>Benar: $(f - g)(4) = f(4) - g(4) = 15 - 9 = 6$.</sub>
- B. $24$  
  <sub>Salah: Siswa menjumlahkan $f(4) + g(4) = 15 + 9 = 24$ alih-alih mengurangkan.</sub>
- C. $-6$  
  <sub>Salah: Siswa mengurangkan secara terbalik, yaitu $g(4) - f(4) = 9 - 15 = -6$.</sub>
- D. $2$  
  <sub>Salah: Siswa salah menggunakan titik $x = 9$, yaitu $f(9) - g(9) = 20 - 18 = 2$.</sub>

**Pembahasan:** Berdasarkan definisi operasi pengurangan dua fungsi:
$(f - g)(x) = f(x) - g(x)$
Untuk $x = 4$:
$(f - g)(4) = f(4) - g(4) = 15 - 9 = 6$.
Jadi, nilai dari $(f - g)(4)$ adalah $6$.
**Acuan:** siswa — siswa hal.40 Latihan 1.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11-b01-b-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: sifat komutatif komposisi*

Pernyataan yang tepat mengenai sifat komutatif pada operasi komposisi fungsi adalah ....

- A. selalu menghasilkan $(f \circ g)(x) = 0$  
  <sub>Salah: Siswa salah menafsirkan arti tidak berlakunya sifat komutatif.</sub>
- **B. secara umum tidak berlaku, sehingga $(f \circ g)(x) \neq (g \circ f)(x)$** ✅  
  <sub>Benar: Komposisi fungsi secara umum tidak memenuhi sifat komutatif.</sub>
- C. hanya berlaku jika kedua fungsi berupa fungsi kuadrat  
  <sub>Salah: Siswa berspekulasi secara keliru tentang jenis fungsi tertentu tanpa dasar konsep.</sub>
- D. selalu berlaku untuk semua jenis pasangan fungsi $f(x)$ dan $g(x)$  
  <sub>Salah: Siswa keliru menganggap sifat komutatif pada penjumlahan/perkalian bilangan juga selalu berlaku pada komposisi fungsi.</sub>

**Pembahasan:** Berdasarkan konsep materi komposisi fungsi, operasi komposisi secara umum tidak memenuhi sifat komutatif, yang berarti secara umum $(f \circ g)(x) \neq (g \circ f)(x)$.
**Acuan:** siswa — siswa hal.45

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11-b01-b-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: domain dan kodomain komposisi*

Jika diketahui fungsi $g: A \to B$ dan $f: B \to C$, maka fungsi komposisi $(f \circ g)$ merupakan fungsi dari domain .... ke kodomain ....

- A. $B$ ke $C$  
  <sub>Salah: Siswa menyebut domain dan kodomain dari fungsi $f$ saja.</sub>
- **B. $A$ ke $C$** ✅  
  <sub>Benar: Komposisi $(f \circ g)(x) = f(g(x))$ memetakan masukan dari himpunan $A$ langsung ke himpunan hasil $C$.</sub>
- C. $C$ ke $A$  
  <sub>Salah: Siswa membalik arah pemetaan fungsi komposisi.</sub>
- D. $B$ ke $A$  
  <sub>Salah: Siswa mengira domainnya adalah himpunan perantara $B$.</sub>

**Pembahasan:** Berdasarkan definisi komposisi fungsi, jika $g: A \to B$ dan $f: B \to C$, maka fungsi komposisi $(f \circ g)$ memiliki domain asal dari himpunan masukan pertama yaitu $A$, dan kodomain hasil akhir yaitu $C$ (ditulis $(f \circ g): A \to C$).
**Acuan:** siswa — siswa hal.42

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11-b01-b-easy-bt01-010
*variasi (angka) | C2 | 1 langkah | jenis: penjumlahan nilai fungsi*

Jika diketahui $f(5) = 14$, $g(5) = 11$, $f(11) = 25$, dan $g(11) = 22$, maka nilai dari $(f + g)(5)$ adalah ....

- A. $3$  
  <sub>Salah: Melakukan operasi pengurangan alih-alih penjumlahan, $14 - 11 = 3$.</sub>
- B. $47$  
  <sub>Salah: Menjumlahkan nilai fungsi pada masukan $11$, yaitu $f(11) + g(11) = 25 + 22 = 47$.</sub>
- **C. $25$** ✅  
  <sub>Benar: $(f + g)(5) = f(5) + g(5) = 14 + 11 = 25$.</sub>
- D. $36$  
  <sub>Salah: Menjumlahkan nilai fungsi pada masukan yang salah, yaitu $f(11) + g(5) = 25 + 11 = 36$.</sub>

**Pembahasan:** Berdasarkan definisi penjumlahan fungsi:
$$(f + g)(5) = f(5) + g(5)$$
Substitusikan nilai yang diketahui:
$$(f + g)(5) = 14 + 11 = 25$$
Jadi, nilai dari $(f + g)(5)$ adalah $25$.
**Acuan:** siswa — siswa hal.40 Latihan 1.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11-b01-b-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: sifat asosiatif komposisi*

Pada operasi komposisi fungsi, manakah bentuk kesamaan berikut yang menunjukkan berlakunya sifat asosiatif untuk sebarang fungsi $f$, $g$, dan $h$?

- A. $((f \circ g) \circ h)(x) = (f \cdot g \cdot h)(x)$  
  <sub>Salah: Mengacaukan operasi komposisi fungsi dengan operasi perkalian aljabar fungsi.</sub>
- **B. $((f \circ g) \circ h)(x) = (f \circ (g \circ h))(x)$** ✅  
  <sub>Benar: Sifat asosiatif pada komposisi menyatakan bahwa pengelompokan operasi tidak mengubah hasil komposisi, yaitu $((f \circ g) \circ h) = (f \circ (g \circ h))$.</sub>
- C. $((f \circ g) \circ h)(x) = ((g \circ f) \circ h)(x)$  
  <sub>Salah: Menukar urutan fungsi di dalam tanda kurung yang melanggar urutan komposisi.</sub>
- D. $(f \circ g)(x) = (g \circ f)(x)$  
  <sub>Salah: Merupakan representasi sifat komutatif (yang secara umum tidak berlaku pada komposisi fungsi).</sub>

**Pembahasan:** Sifat asosiatif menyatakan bahwa urutan pengelompokan pengerjaan operasi tiga objek tidak memengaruhi hasil akhirnya. Untuk tiga buah fungsi $f$, $g$, dan $h$, sifat asosiatif komposisi fungsi dinyatakan sebagai:
$$((f \circ g) \circ h)(x) = (f \circ (g \circ h))(x)$$
Jadi, pernyataan yang tepat adalah $((f \circ g) \circ h)(x) = (f \circ (g \circ h))(x)$.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11-b01-b-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: domain operasi penjumlahan fungsi*

Jika fungsi $f(x)$ memiliki domain $D_f$ dan fungsi $g(x)$ memiliki domain $D_g$, maka domain dari fungsi hasil penjumlahan $(f + g)(x)$ adalah ....

- A. $D_f \times D_g$  
  <sub>Salah: Mengira domain merupakan perkalian Cartesius dari kedua domain.</sub>
- B. $D_f \cup D_g$  
  <sub>Salah: Mengira domain penjumlahan adalah gabungan (union) dari kedua domain.</sub>
- **C. $D_f \cap D_g$** ✅  
  <sub>Benar: Domain hasil operasi penjumlahan dua fungsi adalah irisan dari domain kedua fungsi asalnya, yaitu $D_f \cap D_g$.</sub>
- D. $D_f - D_g$  
  <sub>Salah: Menganggap operasi domain menggunakan operasi selisih himpunan.</sub>

**Pembahasan:** Agar fungsi $(f + g)(x) = f(x) + g(x)$ terdefinisi, nilai $x$ harus terdefinisi pada fungsi $f$ sekaligus terdefinisi pada fungsi $g$. Oleh karena itu, domain dari fungsi $(f + g)(x)$ adalah irisan dari domain $f$ dan domain $g$, yang dituliskan sebagai $D_f \cap D_g$.
**Acuan:** siswa — siswa hal.37

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11-b01-b-easy-bt01-013
*variasi (angka) | C2 | 1 langkah | jenis: perkalian nilai fungsi*

Jika diketahui nilai fungsi $f(7) = 9$, $g(7) = 5$, $f(5) = 8$, dan $g(5) = 4$, maka nilai dari $(f \cdot g)(7)$ adalah ....

- **A. $45$** ✅  
  <sub>Benar: Sesuai definisi perkalian fungsi, $(f \cdot g)(7) = f(7) \cdot g(7) = 9 \cdot 5 = 45$.</sub>
- B. $14$  
  <sub>Salah: Melakukan penjumlahan $f(7) + g(7) = 9 + 5 = 14$, bukan perkalian.</sub>
- C. $36$  
  <sub>Salah: Mengalikan $f(7)$ dengan $g(5)$, yaitu $9 \cdot 4 = 36$.</sub>
- D. $32$  
  <sub>Salah: Mengalikan $f(5)$ dengan $g(5)$, yaitu $8 \cdot 4 = 32$.</sub>

**Pembahasan:** Berdasarkan definisi operasi perkalian fungsi:
$$(f \cdot g)(x) = f(x) \cdot g(x)$$
Untuk $x = 7$:
$$(f \cdot g)(7) = f(7) \cdot g(7) = 9 \cdot 5 = 45$$
**Acuan:** pretest — kelas11-b01-p0040-latihan-13-6c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11-b01-b-easy-bt01-014
*variasi (angka) | C2 | 1 langkah | jenis: pembagian nilai fungsi*

Jika diketahui $f(4) = 28$, $g(4) = 7$, $f(7) = 15$, dan $g(7) = 5$, maka nilai dari $(f \div g)(4)$ adalah ....

- A. $3$  
  <sub>Salah: Menghitung $(f \div g)(7) = \frac{15}{5} = 3$ bukannya untuk $x = 4$.</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: Menghitung posisi terbalik $(g \div f)(4) = \frac{7}{28} = \frac{1}{4}$.</sub>
- C. $21$  
  <sub>Salah: Menghitung operasi pengurangan $f(4) - g(4) = 28 - 7 = 21$.</sub>
- **D. $4$** ✅  
  <sub>Benar: Operasi pembagian fungsi $(f \div g)(4) = \frac{f(4)}{g(4)} = \frac{28}{7} = 4$.</sub>

**Pembahasan:** Definisi pembagian dua fungsi:
$$(f \div g)(x) = \frac{f(x)}{g(x)}$$
Untuk $x = 4$:
$$(f \div g)(4) = \frac{f(4)}{g(4)} = \frac{28}{7} = 4$$
**Acuan:** siswa — siswa hal.40 Latihan 1.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11-b01-b-easy-bt01-015
*variasi (konteks) | C1 | 1 langkah | jenis: konsep operasi fungsi*

Sebuah koperasi sekolah ingin menentukan fungsi sisa hasil usaha (keuntungan) $U(x)$ dari penjualan alat tulis, di mana $P(x)$ menyatakan fungsi penerimaan total dan $B(x)$ menyatakan fungsi beban operasional. Operasi aljabar fungsi yang tepat untuk menentukan fungsi $U(x)$ adalah ....

- A. penjumlahan, yaitu $U(x) = (P + B)(x)$  
  <sub>Salah: Keliru mengira keuntungan diperoleh dengan menggabungkan/menjumlahkan penerimaan dan beban.</sub>
- B. perkalian, yaitu $U(x) = (P \cdot B)(x)$  
  <sub>Salah: Keliru menerapkan operasi perkalian antar-fungsi.</sub>
- **C. pengurangan, yaitu $U(x) = (P - B)(x)$** ✅  
  <sub>Benar: Keuntungan diperoleh dari selisih penerimaan total dikurangi beban operasional, sehingga $U(x) = P(x) - B(x) = (P - B)(x)$.</sub>
- D. pembagian, yaitu $U(x) = (P \div B)(x)$  
  <sub>Salah: Keliru menganggap rasio penerimaan terhadap beban sebagai keuntungan mutlak.</sub>

**Pembahasan:** Keuntungan diperoleh dari total penerimaan dikurangi total beban biaya:
$$U(x) = P(x) - B(x) = (P - B)(x)$$
Jadi, operasi yang tepat adalah pengurangan fungsi.
**Acuan:** siswa — siswa hal.37 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11-b01-b-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: sifat komutatif diskon komposisi*

Sebuah toko pakaian memberikan promo diskon bertingkat. Suatu barang dikenai diskon 40% kemudian dilanjutkan diskon 10%. Jika urutan diskon ditukar menjadi diskon 10% kemudian dilanjutkan diskon 40%, hubungan harga akhir barang pada kedua urutan tersebut adalah ....

- **A. sama besar, karena perkalian faktor pengali diskon bersifat komutatif** ✅  
  <sub>Benar: Diskon 40% lalu 10% menghasilkan faktor $(1 - 0,10)(1 - 0,40) = 0,9 \times 0,6 = 0,54$. Urutan sebaliknya menghasilkan $(1 - 0,40)(1 - 0,10) = 0,6 \times 0,9 = 0,54$, sehingga harganya sama.</sub>
- B. berbeda, karena komposisi dua fungsi secara umum tidak komutatif  
  <sub>Salah: Menerapkan fakta umum ketidakkonmutatifan komposisi tanpa melihat bahwa fungsi diskon ini berbentuk perkalian skalar yang saling komutatif.</sub>
- C. lebih murah jika diskon 40% diberikan terlebih dahulu  
  <sub>Salah: Keliru menduga diskon persentase lebih besar di awal membuat harga akhir lebih rendah.</sub>
- D. lebih murah jika diskon 10% diberikan terlebih dahulu  
  <sub>Salah: Keliru menduga persentase lebih kecil di awal menguntungkan pembeli.</sub>

**Pembahasan:** Misalkan harga awal adalah $x$.
Urutan 1 (diskon 40% lalu 10%):
$$f(x) = (1 - 0,40)x = 0,60x$$
$$g(f(x)) = (1 - 0,10)(0,60x) = 0,90 \times 0,60x = 0,54x$$

Urutan 2 (diskon 10% lalu 40%):
$$g(x) = (1 - 0,10)x = 0,90x$$
$$f(g(x)) = (1 - 0,40)(0,90x) = 0,60 \times 0,90x = 0,54x$$

Karena $0,54x = 0,54x$, kedua urutan menghasilkan harga akhir yang sama besar.
**Acuan:** siswa — siswa hal.45 Eksplorasi 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11-b01-b-easy-bt01-017
*orisinal | C1 | 1 langkah | jenis: domain operasi perkalian fungsi*  **[warning validator]**

Jika fungsi $f(x)$ memiliki daerah asal (domain) $D_f$ dan fungsi $g(x)$ memiliki daerah asal $D_g$, maka daerah asal dari fungsi hasil perkalian $(f \cdot g)(x)$ adalah ....

- A. $D_f \cup D_g$  
  <sub>Salah: Keliru menggunakan operasi gabungan himpunan.</sub>
- **B. $D_f \cap D_g$** ✅  
  <sub>Benar: Daerah asal dari perkalian dua fungsi adalah irisan dari domain kedua fungsi asalnya, yaitu $D_f \cap D_g$.</sub>
- C. $D_f - D_g$  
  <sub>Salah: Keliru menggunakan operasi selisih himpunan.</sub>
- D. $D_f \times D_g$  
  <sub>Salah: Keliru menganggap perkalian fungsi menghasilkan perkalian Cartesius domain.</sub>

**Pembahasan:** Berdasarkan materi Buku Siswa kelas XI, jika $f(x)$ dan $g(x)$ memiliki domain masing-masing $D_f$ dan $D_g$, maka perkalian $(f \cdot g)(x) = f(x) \cdot g(x)$ menghasilkan fungsi baru dengan domain irisan kedua domain tersebut, yaitu $D_f \cap D_g$.
**Acuan:** siswa — siswa hal.38
**Warning:** kelas11-b01-b-easy-bt01-017 sangat mirip dengan kelas11-b01-b-easy-bt01-019 (0.96) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11-b01-b-easy-bt01-018
*variasi (angka) | C2 | 1 langkah | jenis: komposisi bentuk akar*

Jika diketahui fungsi $f(x) = x - 5$ dan $g(x) = \sqrt{x}$, maka rumus fungsi $h(x) = g(f(x))$ adalah ....

- A. $\sqrt{x - 2}$  
  <sub>Salah: Siswa menggunakan konstanta dari soal acuan di buku tanpa mengubah angka.</sub>
- B. $\sqrt{x} - 5$  
  <sub>Salah: Siswa tertukar urutan komposisi menjadi $(f \circ g)(x) = f(g(x)) = \sqrt{x} - 5$.</sub>
- **C. $\sqrt{x - 5}$** ✅  
  <sub>Benar: Berdasarkan definisi komposisi, $h(x) = g(f(x)) = g(x - 5) = \sqrt{x - 5}$.</sub>
- D. $\sqrt{5 - x}$  
  <sub>Salah: Siswa salah menuliskan urutan pengurangan di dalam akar.</sub>

**Pembahasan:** Komposisi fungsi $h(x) = g(f(x))$ diperoleh dengan menyubstitusikan $f(x)$ ke dalam rumus $g(x)$:
$$h(x) = g(f(x)) = g(x - 5) = \sqrt{x - 5}$$
Jadi, rumus fungsi $h(x)$ adalah $\sqrt{x - 5}$.
**Acuan:** siswa — siswa hal.43 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11-b01-b-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: domain operasi pengurangan fungsi*  **[warning validator]**

Jika fungsi $f(x)$ memiliki daerah asal (domain) $D_f$ dan fungsi $g(x)$ memiliki daerah asal $D_g$, maka daerah asal dari fungsi hasil pengurangan $(f - g)(x)$ adalah ....

- A. $D_f - D_g$  
  <sub>Salah: Siswa menyamakan operasi pengurangan fungsi dengan pengurangan himpunan pada domain.</sub>
- B. $D_f \cup D_g$  
  <sub>Salah: Siswa mengira operasi fungsi menggabungkan seluruh anggota domain (operasi gabungan/union).</sub>
- C. $D_f \times D_g$  
  <sub>Salah: Siswa mengira domain dihasilkan dari perkalian Cartesius antarhimpunan domain.</sub>
- **D. $D_f \cap D_g$** ✅  
  <sub>Benar: Sesuai definisi pada materi operasi aljabar fungsi, daerah asal dari $(f - g)(x)$ adalah irisan dari kedua daerah asalnya, yaitu $D_f \cap D_g$.</sub>

**Pembahasan:** Berdasarkan sifat operasi aljabar fungsi, operasi pengurangan $(f - g)(x) = f(x) - g(x)$ hanya terdefinisi pada nilai-nilai $x$ yang sekaligus menjadi anggota domain $f$ dan domain $g$. Oleh karena itu, daerah asalnya adalah irisan dari kedua daerah asal tersebut, yaitu $D_{(f - g)} = D_f \cap D_g$.
**Acuan:** siswa — siswa hal.37
**Warning:** kelas11-b01-b-easy-bt01-017 sangat mirip dengan kelas11-b01-b-easy-bt01-019 (0.96) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11-b01-b-easy-bt01-020
*variasi (angka) | C2 | 1 langkah | jenis: menentukan komponen fungsi komposisi*

Diketahui hasil dari $(f \circ g)(x) = (7x + 6)^5$ dan $f(x) = x^5$. Rumus fungsi $g(x)$ yang memenuhi adalah ....

- A. $7x - 6$  
  <sub>Salah: Kesalahan tanda operasi pada konstanta fungsi dalam.</sub>
- B. $(7x + 6)^5$  
  <sub>Salah: Siswa menganggap hasil komposisi $(f \circ g)(x)$ sama dengan $g(x)$ secara langsung tanpa menguraikan fungsi luar $f$.</sub>
- C. $\frac{7x + 6}{5}$  
  <sub>Salah: Siswa salah menerapkan inversi operasi pangkat menjadi pembagian dengan pangkatnya.</sub>
- **D. $7x + 6$** ✅  
  <sub>Benar: Berdasarkan definisi $(f \circ g)(x) = f(g(x)) = (g(x))^5$. Karena $(g(x))^5 = (7x + 6)^5$, maka $g(x) = 7x + 6$.</sub>

**Pembahasan:** Berdasarkan definisi komposisi fungsi:
$$(f \circ g)(x) = f(g(x))$$

Diketahui $f(x) = x^5$, sehingga:
$$f(g(x)) = (g(x))^5$$

Dari soal diketahui bahwa $(f \circ g)(x) = (7x + 6)^5$. Dengan menyamakan kedua bentuk tersebut, diperoleh:
$$(g(x))^5 = (7x + 6)^5$$
$$g(x) = 7x + 6$$

Jadi, rumus fungsi $g(x)$ adalah $7x + 6$.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11-b01-b-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: nilai parameter komposisi*

Diketahui fungsi $f(x) = \frac{1}{x + 3}$ dan $g(x) = 4x - 1$. Jika $(f \circ g)(a) = \frac{1}{7}$, maka nilai dari $g(a)$ adalah ....

- A. $2$  
  <sub>Salah: Siswa salah saat menyelesaikan persamaan $4a + 2 = 7$ menjadi $4a = 3$, sehingga $a = \frac{3}{4}$ dan $g(a) = 3 - 1 = 2$.</sub>
- B. $\frac{5}{4}$  
  <sub>Salah: Siswa berhenti pada nilai $a$ dan lupa menyubstitusikannya kembali ke $g(a)$.</sub>
- **C. $4$** ✅  
  <sub>Benar: $(f \circ g)(a) = f(g(a)) = \frac{1}{(4a - 1) + 3} = \frac{1}{4a + 2} = \frac{1}{7}$, sehingga $4a + 2 = 7 \Rightarrow 4a = 5 \Rightarrow a = \frac{5}{4}$. Maka $g(a) = 4\left(\frac{5}{4}\right) - 1 = 4$.</sub>
- D. $7$  
  <sub>Salah: Siswa langsung menganggap $g(a)$ sama dengan penyebut dari hasil komposisi tanpa memperhitungkan konstanta $+3$ pada fungsi $f$.</sub>

**Pembahasan:** Berdasarkan definisi fungsi komposisi:
$$(f \circ g)(a) = f(g(a)) = \frac{1}{g(a) + 3}$$
Diketahui $(f \circ g)(a) = \frac{1}{7}$, maka:
$$\frac{1}{g(a) + 3} = \frac{1}{7}$$
$$g(a) + 3 = 7$$
$$g(a) = 7 - 3 = 4$$

Jadi, nilai $g(a)$ adalah $4$.
**Acuan:** siswa — siswa hal.46 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11-b01-b-medium-bt01-002
*variasi (angka) | C4 | 3 langkah | jenis: komutatif komposisi*

Diketahui fungsi $f(x) = 5x - 4$ dan $g(x) = ax + 8$. Agar berlaku sifat komutatif $(f \circ g)(x) = (g \circ f)(x)$ untuk setiap $x \in \mathbb{R}$, maka nilai konstanta $a$ adalah ....

- A. $7$  
  <sub>Salah: Siswa salah tanda saat memindahkan ruas konstanta: $-4a = -28$ sehingga $a = 7$.</sub>
- **B. $-7$** ✅  
  <sub>Benar: $(f \circ g)(x) = 5(ax + 8) - 4 = 5ax + 36$. $(g \circ f)(x) = a(5x - 4) + 8 = 5ax - 4a + 8$. Menyamakan konstanta: $36 = -4a + 8 \Rightarrow -4a = 28 \Rightarrow a = -7$.</sub>
- C. $1$  
  <sub>Salah: Siswa berasumsi sifat komutatif hanya terpenuhi jika $a = 1$.</sub>
- D. $-11$  
  <sub>Salah: Siswa menjumlahkan konstanta $36 + 8 = 44$ lalu membaginya dengan $-4$.</sub>

**Pembahasan:** Tentukan masing-masing fungsi komposisi:
1. $(f \circ g)(x) = f(g(x)) = 5(ax + 8) - 4 = 5ax + 40 - 4 = 5ax + 36$
2. $(g \circ f)(x) = g(f(x)) = a(5x - 4) + 8 = 5ax - 4a + 8$

Agar $(f \circ g)(x) = (g \circ f)(x)$ identik untuk setiap $x$, konstanta kedua ruas harus bernilai sama:
$$36 = -4a + 8$$
$$4a = 8 - 36$$
$$4a = -28$$
$$a = -7$$

Jadi, nilai $a$ yang memenuhi adalah $-7$.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11-b01-b-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: akar persamaan komposisi*

Diketahui fungsi $f(x) = x^2 - 4x + 3$ dan $g(x) = 2x + 1$. Jumlah semua nilai $x$ yang memenuhi persamaan $(f \circ g)(x) = 0$ adalah ....

- **A. $1$** ✅  
  <sub>Benar: $(f \circ g)(x) = f(2x + 1) = (2x+1)^2 - 4(2x+1) + 3 = 4x^2 + 4x + 1 - 8x - 4 + 3 = 4x^2 - 4x = 0$. Akar-akarnya $x_1 = 0$ dan $x_2 = 1$, sehingga $x_1 + x_2 = 1$.</sub>
- B. $4$  
  <sub>Salah: Siswa mencari jumlah akar dari persamaan $f(x) = 0$, bukan $(f \circ g)(x) = 0$.</sub>
- C. $-1$  
  <sub>Salah: Siswa melakukan kesalahan tanda pada rumus jumlah akar $-(-4)/4$ menjadi $-4/4 = -1$.</sub>
- D. $2$  
  <sub>Salah: Siswa menggunakan rumus $-b/a$ langsung dari fungsi awal $f(x)$ yaitu $-(-4)/1 = 4$ lalu membaginya 2.</sub>

**Pembahasan:** Langkah 1: Tentukan rumus $(f \circ g)(x)$:
$$(f \circ g)(x) = f(g(x)) = (2x + 1)^2 - 4(2x + 1) + 3$$
$$(f \circ g)(x) = (4x^2 + 4x + 1) - (8x + 4) + 3 = 4x^2 - 4x$$

Langkah 2: Selesaikan persamaan $(f \circ g)(x) = 0$:
$$4x^2 - 4x = 0$$
$$4x(x - 1) = 0$$
Diperoleh akar-akar $x_1 = 0$ dan $x_2 = 1$.

Langkah 3: Hitung jumlah akar-akarnya:
$$x_1 + x_2 = 0 + 1 = 1$$

Jadi, jumlah semua nilai $x$ yang memenuhi adalah $1$.
**Acuan:** siswa — siswa hal.42

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11-b01-b-medium-bt01-004
*orisinal | C4 | 3 langkah | jenis: domain fungsi komposisi*

Diketahui fungsi $f(x) = \sqrt{x - 5}$ dan $g(x) = x^2 - 4$. Daerah asal (domain) dari fungsi komposisi $(f \circ g)(x)$ untuk $x \in \mathbb{R}$ adalah ....

- A. $\{x \mid x \ge 5,\, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa hanya melihat domain dari fungsi luar $f(x)$ yaitu $x \ge 5$ tanpa mengomposisikannya dengan $g(x)$.</sub>
- B. $\{x \mid -3 \le x \le 3,\, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa terbalik menentukan interval tanda pertidaksamaan kuadrat $\ge$ dengan interval tertutup di dalam akar.</sub>
- **C. $\{x \mid x \le -3 \text{ atau } x \ge 3,\, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: $(f \circ g)(x) = \sqrt{(x^2 - 4) - 5} = \sqrt{x^2 - 9}$. Syarat domain nilai di bawah akar tidak negatif: $x^2 - 9 \ge 0 \Rightarrow (x - 3)(x + 3) \ge 0 \Rightarrow x \le -3$ atau $x \ge 3$.</sub>
- D. $\{x \mid x \ge 3,\, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa hanya mengambil solusi positif dari pertidaksamaan kuadrat dan mengabaikan bagian $x \le -3$.</sub>

**Pembahasan:** Langkah 1: Susun bentuk fungsi komposisi $(f \circ g)(x)$:
$$(f \circ g)(x) = f(g(x)) = \sqrt{(x^2 - 4) - 5} = \sqrt{x^2 - 9}$$

Langkah 2: Tentukan syarat agar bentuk akar terdefinisi pada bilangan real:
$$x^2 - 9 \ge 0$$
$$(x - 3)(x + 3) \ge 0$$

Langkah 3: Pembuat nol adalah $x = 3$ dan $x = -3$. Menggunakan garis bilangan, daerah yang memenuhi tanda positif adalah:
$$x \le -3 \text{ atau } x \ge 3$$

Jadi, domain dari $(f \circ g)(x)$ adalah $\{x \mid x \le -3 \text{ atau } x \ge 3,\, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11-b01-b-medium-bt01-005
*orisinal | C3 | 3 langkah | jenis: pemodelan komposisi diskon*

Sebuah butik memberikan promo akhir pekan berupa diskon sebesar 15% kemudian dilanjutkan dengan potongan kupon belanja senilai Rp30.000,00 pada saat pembayaran di kasir. Jika seorang pelanggan membayar sebesar Rp140.000,00 untuk sepotong pakaian, harga awal pakaian tersebut sebelum dikenakan promo adalah ....

- A. Rp220.000,00  
  <sub>Salah: Siswa salah menghitung persentase diskon dengan mengalikan $170.000 \times 1{,}15$ ditambah pembulatan.</sub>
- B. Rp195.500,00  
  <sub>Salah: Siswa menerapkan potongan kupon Rp30.000 terlebih dahulu sebelum diskon 15%, sehingga $0{,}85(x - 30.000) = 140.000$.</sub>
- C. Rp170.000,00  
  <sub>Salah: Siswa hanya menambahkan potongan kupon Rp30.000 ke harga akhir tanpa memperhitungkan diskon 15%.</sub>
- **D. Rp200.000,00** ✅  
  <sub>Benar: Fungsi diskon $d(x) = 0{,}85x$, fungsi kupon $k(y) = y - 30.000$. Komposisinya $(k \circ d)(x) = 0{,}85x - 30.000$. Persamaan: $0{,}85x - 30.000 = 140.000 \Rightarrow 0{,}85x = 170.000 \Rightarrow x = 200.000$.</sub>

**Pembahasan:** Misalkan harga awal pakaian adalah $x$.
1. Tahap pertama (diskon 15%):
Harga menjadi $d(x) = (1 - 0{,}15)x = 0{,}85x$.
2. Tahap kedua (potongan kupon Rp30.000,00):
Harga akhir menjadi $(k \circ d)(x) = 0{,}85x - 30.000$.

Diketahui harga akhir yang dibayar adalah Rp140.000,00:
$$0{,}85x - 30.000 = 140.000$$
$$0{,}85x = 170.000$$
$$x = \frac{170.000}{0{,}85} = 200.000$$

Jadi, harga awal pakaian tersebut adalah Rp200.000,00.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11-b01-b-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: komposisi biaya produksi*

Jumlah kertas yang diperlukan untuk mencetak $x$ eksemplar buku panduan dinyatakan dengan fungsi $k(x) = 120(x + 5)$ lembar. Biaya cetak untuk $k$ lembar kertas memenuhi fungsi $b(k) = 500k + 50.000$ (dalam rupiah). Jika total biaya yang dikeluarkan percetakan sebesar Rp15.350.000,00, maka banyak eksemplar buku panduan yang dicetak adalah ....

- A. 255  
  <sub>Salah: Lupa mengurangkan konstanta 5 di akhir perhitungan ($x + 5 = 255$ dianggap sebagai $x$).</sub>
- **B. 250** ✅  
  <sub>Benar: Fungsi total biaya terhadap banyak eksemplar adalah $(b \circ k)(x) = 500(120(x + 5)) + 50.000 = 60.000(x + 5) + 50.000$. Menyamakan dengan Rp15.350.000,00 menghasilkan $60.000(x + 5) = 15.300.000 \iff x + 5 = 255 \iff x = 250$.</sub>
- C. 260  
  <sub>Salah: Salah operasi tanda pada langkah terakhir, menjumlahkan $255 + 5$ bukannya mengurangkan.</sub>
- D. 245  
  <sub>Salah: Salah menjumlahkan konstanta 5 dua kali sehingga mengurangkan 10 dari 255.</sub>

**Pembahasan:** Langkah 1: Susun fungsi komposisi total biaya terhadap $x$:
$$(b \circ k)(x) = b(k(x)) = 500(120(x + 5)) + 50.000 = 60.000(x + 5) + 50.000$$

Langkah 2: Substitusikan total biaya yang diketahui:
$$60.000(x + 5) + 50.000 = 15.350.000$$
$$60.000(x + 5) = 15.300.000$$

Langkah 3: Tentukan nilai $x$:
$$x + 5 = \frac{15.300.000}{60.000} = 255$$
$$x = 255 - 5 = 250$$

Jadi, banyak eksemplar buku panduan yang dicetak adalah 250 eksemplar.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11-b01-b-medium-bt01-007
*variasi (angka) | C3 | 2 langkah | jenis: komposisi bertingkat produksi*

Sebuah pabrik perakitan elektronik mengatur kapasitas produksinya. Produksi telepon genggam Android dirumuskan oleh $A(x) = 3x + 50$, dengan $x$ adalah banyak telepon genggam non-Android. Sementara itu, produksi unit laptop dirumuskan oleh $L(A) = 4A - 100$, dengan $A$ adalah banyak telepon genggam Android yang dirakit. Jika pabrik tersebut merakit 1.500 unit telepon genggam non-Android, banyak unit laptop yang dihasilkan adalah ....

- A. 18.200  
  <sub>Salah: Lupa mengurangkan konstanta 100 pada fungsi laptop $L(A)$.</sub>
- B. 17.900  
  <sub>Salah: Lupa menambahkan konstanta 50 pada fungsi pertama sehingga $L(4(1.500)) - 100 = 17.900$.</sub>
- **C. 18.100** ✅  
  <sub>Benar: Nilai $A(1.500) = 3(1.500) + 50 = 4.550$. Kemudian $L(4.550) = 4(4.550) - 100 = 18.200 - 100 = 18.100$.</sub>
- D. 18.300  
  <sub>Salah: Salah tanda pada konstanta laptop menjadi $4A + 100$.</sub>

**Pembahasan:** Langkah 1: Hitung banyak telepon genggam Android ($A$) untuk $x = 1.500$:
$$A(1.500) = 3(1.500) + 50 = 4.500 + 50 = 4.550$$

Langkah 2: Hitung banyak laptop yang diproduksi dengan memasukkan $A = 4.550$ ke fungsi $L(A)$:
$$L(4.550) = 4(4.550) - 100 = 18.200 - 100 = 18.100$$

Jadi, banyak unit laptop yang dihasilkan adalah 18.100 unit.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11-b01-b-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: komutatif fungsi linear*

Diketahui fungsi $f(x) = 4x - 6$ dan $g(x) = 3x + b$. Agar berlaku kesamaan $(f \circ g)(x) = (g \circ f)(x)$ untuk setiap bilangan real $x$, maka nilai konstanta $b$ adalah ....

- A. -2  
  <sub>Salah: Lupa mengalikan konstanta $b$ dengan koefisien luar $4$ pada saat ekspansi $(f \circ g)(x)$.</sub>
- B. -8  
  <sub>Salah: Salah menjumlahkan konstanta di ruas kanan menjadi $4b - b = -18 - 6 = -24$ sehingga $b = -8$.</sub>
- C. 4  
  <sub>Salah: Kesalahan tanda minus saat membagi $-12$ dengan $3$.</sub>
- **D. -4** ✅  
  <sub>Benar: Hasil $(f \circ g)(x) = 4(3x + b) - 6 = 12x + 4b - 6$ dan $(g \circ f)(x) = 3(4x - 6) + b = 12x - 18 + b$. Menyamakan kedua konstanta menghasilkan $4b - 6 = -18 + b \iff 3b = -12 \iff b = -4$.</sub>

**Pembahasan:** Langkah 1: Tentukan rumus fungsi $(f \circ g)(x)$:
$$(f \circ g)(x) = f(g(x)) = 4(3x + b) - 6 = 12x + 4b - 6$$

Langkah 2: Tentukan rumus fungsi $(g \circ f)(x)$:
$$(g \circ f)(x) = g(f(x)) = 3(4x - 6) + b = 12x - 18 + b$$

Langkah 3: Samakan kedua fungsi karena $(f \circ g)(x) = (g \circ f)(x)$:
$$12x + 4b - 6 = 12x - 18 + b$$
$$4b - b = -18 + 6$$
$$3b = -12$$
$$b = -4$$

Jadi, nilai $b$ yang memenuhi adalah $-4$.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11-b01-b-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: domain operasi aljabar fungsi*

Diketahui dua fungsi real $f(x) = \sqrt{2x + 8}$ dan $g(x) = \frac{5}{x - 3}$. Daerah asal (domain) dari fungsi hasil pengurangan $(f - g)(x)$ adalah ....

- **A. $\{x \in \mathbb{R} \mid x \ge -4 \text{ dan } x \ne 3\}$** ✅  
  <sub>Benar: Domain $f(x)$ adalah $2x + 8 \ge 0 \implies x \ge -4$. Domain $g(x)$ adalah $x - 3 \ne 0 \implies x \ne 3$. Maka daerah asal $(f - g)(x)$ adalah irisan $D_f \cap D_g = \{x \in \mathbb{R} \mid x \ge -4 \text{ dan } x \ne 3\}$.</sub>
- B. $\{x \in \mathbb{R} \mid x > -4 \text{ dan } x \ne 3\}$  
  <sub>Salah: Mengira tanda pertidaksamaan fungsi bentuk akar tidak boleh nol (menggunakan $>$ bukannya $\ge$).</sub>
- C. $\{x \in \mathbb{R} \mid x \ge 4 \text{ dan } x \ne 3\}$  
  <sub>Salah: Salah menghitung pertidaksamaan $2x + 8 \ge 0$ menjadi $x \ge 4$.</sub>
- D. $\{x \in \mathbb{R} \mid x \ge -4\}$  
  <sub>Salah: Lupa memperhitungkan syarat pembuat nol pada penyebut fungsi rasional $g(x)$.</sub>

**Pembahasan:** Langkah 1: Menentukan domain fungsi $f(x)$ ($D_f$).
Bentuk akar terdefinisi di bilangan real jika radikan tak negatif:
$$2x + 8 \ge 0 \iff 2x \ge -8 \iff x \ge -4$$
Jadi, $D_f = \{x \in \mathbb{R} \mid x \ge -4\}$.

Langkah 2: Menentukan domain fungsi $g(x)$ ($D_g$).
Fungsi pecahan terdefinisi jika penyebut tidak sama dengan nol:
$$x - 3 \ne 0 \iff x \ne 3$$
Jadi, $D_g = \{x \in \mathbb{R} \mid x \ne 3\}$.

Langkah 3: Menentukan domain $(f - g)(x)$ melalui irisan domain:
$$D_{f - g} = D_f \cap D_g = \{x \in \mathbb{R} \mid x \ge -4 \text{ dan } x \ne 3\}$$
**Acuan:** siswa — siswa hal.37

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11-b01-b-medium-bt01-010
*variasi (angka) | C3 | 3 langkah | jenis: komposisi biaya pencetakan*

Jumlah kertas yang diperlukan untuk mencetak $x$ eksemplar modul ajar dinyatakan dalam fungsi $k(x) = 150(x + 2)$ lembar. Biaya pencetakan yang diperlukan untuk $k$ lembar kertas adalah $b(k) = 300k + 10.000$ (dalam rupiah). Jika total biaya yang dikeluarkan percetakan sebesar Rp4.060.000,00, banyak eksemplar modul ajar yang dicetak adalah ....

- A. 92  
  <sub>Salah: Siswa salah mengoperasikan tanda pada langkah terakhir, menjumlahkan 90 + 2 bukannya mengurangkan.</sub>
- B. 86  
  <sub>Salah: Siswa keliru mengurangkan konstanta 4 alih-alih 2 pada persamaan linear akhir.</sub>
- **C. 88** ✅  
  <sub>Benar: Menyelesaikan $300k + 10.000 = 4.060.000$ menghasilkan $k = 13.500$, lalu $150(x + 2) = 13.500$ menghasilkan $x + 2 = 90$, sehingga $x = 88$.</sub>
- D. 90  
  <sub>Salah: Siswa lupa mengurangkan nilai 2 dari hasil pembagian 13.500 / 150.</sub>

**Pembahasan:** Fungsi total biaya dinyatakan dengan komposisi $(b \circ k)(x) = b(k(x))$. Diketahui total biaya $b(k) = 4.060.000$:
$$300k + 10.000 = 4.060.000$$
$$300k = 4.050.000$$
$$k = 13.500$$
Substitusikan nilai $k$ ke dalam fungsi $k(x)$:
$$150(x + 2) = 13.500$$
$$x + 2 = \frac{13.500}{150}$$
$$x + 2 = 90$$
$$x = 90 - 2 = 88$$
Jadi, banyak eksemplar modul yang dicetak adalah 88.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11-b01-b-medium-bt01-011
*variasi (angka) | C3 | 2 langkah | jenis: komposisi rasio bertingkat*

Suatu pabrik elektronik menetapkan target harian sebagai berikut: jumlah produksi ponsel Android adalah 4 kali jumlah produksi ponsel non-Android, sedangkan jumlah produksi laptop adalah 5 kali jumlah produksi ponsel Android. Jika pada suatu hari pabrik memproduksi 600 unit ponsel non-Android, maka banyak laptop yang dihasilkan pada hari tersebut adalah ....

- A. 5.400 unit  
  <sub>Salah: Menjumlahkan pengali $(4 + 5) \times 600 = 9 \times 600 = 5.400$ alih-alih mengomposisikannya.</sub>
- B. 15.000 unit  
  <sub>Salah: Salah menghitung ponsel Android menjadi $5 \times 600 = 3.000$, lalu dikalikan 5 lagi.</sub>
- **C. 12.000 unit** ✅  
  <sub>Benar: Komposisi fungsi menghasilkan $L(x) = 5 \times (4x) = 20x$. Untuk $x = 600$, diperoleh $20 \times 600 = 12.000$ unit.</sub>
- D. 2.400 unit  
  <sub>Salah: Hanya menghitung ponsel Android ($4 \times 600$) tanpa mengalikan rasio laptop.</sub>

**Pembahasan:** Misalkan $x$ adalah banyak ponsel non-Android, $A(x) = 4x$ adalah banyak ponsel Android, dan $L(A) = 5A$ adalah banyak laptop.
Komposisi fungsinya adalah:
$$(L \circ A)(x) = L(A(x)) = 5(4x) = 20x$$
Untuk $x = 600$ unit:
$$(L \circ A)(600) = 20 \times 600 = 12.000\text{ unit}$$
Jadi, banyak laptop yang dihasilkan adalah 12.000 unit.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11-b01-b-medium-bt01-012
*orisinal | C4 | 3 langkah | jenis: syarat domain komposisi*

Diketahui fungsi $f(x) = \frac{1}{\sqrt{x - 2}}$ dan $g(x) = x^2 - 7$. Daerah asal (domain) dari fungsi komposisi $(f \circ g)(x)$ untuk $x$ bilangan real adalah ....

- A. $\{x \in \mathbb{R} \mid x > 3\}$  
  <sub>Salah: Siswa melupakan penyelesaian pertidaksamaan kuadrat untuk nilai variabel yang negatif.</sub>
- **B. $\{x \in \mathbb{R} \mid x < -3 \text{ atau } x > 3\}$** ✅  
  <sub>Benar: Syarat fungsi terdefinisi adalah $g(x) > 2 \iff x^2 - 7 > 2 \iff x^2 > 9$, sehingga $x < -3$ atau $x > 3$.</sub>
- C. $\{x \in \mathbb{R} \mid x \le -3 \text{ atau } x \ge 3\}$  
  <sub>Salah: Siswa menyertakan tanda sama dengan, padahal penyebut dalam pecahan tidak boleh bernilai nol.</sub>
- D. $\{x \in \mathbb{R} \mid -3 < x < 3\}$  
  <sub>Salah: Siswa salah menentukan daerah pertidaksamaan kuadrat $x^2 > 9$ menjadi rentang interval dalam.</sub>

**Pembahasan:** Agar $(f \circ g)(x) = f(g(x))$ terdefinisi, nilai $g(x)$ harus berada dalam domain $f$.
Fungsi $f(u) = \frac{1}{\sqrt{u - 2}}$ terdefinisi pada bilangan real jika bagian di bawah tanda akar bernilai positif murni (karena penyebut tidak boleh nol):
$$u - 2 > 0 \implies u > 2$$
Karena $u = g(x) = x^2 - 7$, maka:
$$x^2 - 7 > 2$$
$$x^2 - 9 > 0$$
$$(x - 3)(x + 3) > 0$$
Dari garis bilangan diperoleh pembuat nol $x = -3$ dan $x = 3$. Daerah yang memenuhi pertidaksamaan bertanda positif adalah $x < -3$ atau $x > 3$.
Jadi, daerah asalnya adalah $\{x \in \mathbb{R} \mid x < -3 \text{ atau } x > 3\}$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11-b01-b-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: evaluasi asosiatif komposisi*

Diketahui tiga buah fungsi $f(x) = 2x - 3$, $g(x) = x^2 + 1$, dan $h(x) = 3x - 2$. Nilai dari $((f \circ g) \circ h)(2)$ adalah ....

- A. 35  
  <sub>Salah: Siswa melakukan kesalahan tanda pada fungsi $f$, menghitung $2(17) + 3 = 37$ atau salah hitung aritmetika menjadi 35.</sub>
- **B. 31** ✅  
  <sub>Benar: $h(2) = 4$, lalu $g(4) = 17$, dan $f(17) = 2(17) - 3 = 31$.</sub>
- C. 27  
  <sub>Salah: Siswa salah saat menghitung nilai $g(4) = 4^2 - 1 = 15$, sehingga $f(15) = 27$.</sub>
- D. 15  
  <sub>Salah: Siswa salah membalik urutan pengerjaan menjadi $(h \circ g \circ f)(2)$.</sub>

**Pembahasan:** Berdasarkan sifat asosiatif komposisi fungsi, $((f \circ g) \circ h)(2) = f(g(h(2)))$.
Langkah 1: Hitung nilai $h(2)$:
$$h(2) = 3(2) - 2 = 6 - 2 = 4$$
Langkah 2: Hitung nilai $g(h(2)) = g(4)$:
$$g(4) = 4^2 + 1 = 16 + 1 = 17$$
Langkah 3: Hitung nilai $f(g(4)) = f(17)$:
$$f(17) = 2(17) - 3 = 34 - 3 = 31$$
Jadi, nilai dari $((f \circ g) \circ h)(2)$ adalah 31.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11-b01-b-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: analisis perbandingan komposisi*

Sebuah pusat perbelanjaan menawarkan dua pilihan skema promo untuk barang seharga $x$:
- Skema 1: Diskon 20% terlebih dahulu, kemudian dilanjutkan potongan harga langsung sebesar Rp15.000,00.
- Skema 2: Potongan harga langsung sebesar Rp15.000,00 terlebih dahulu, kemudian dilanjutkan diskon 20%.

Jika seorang pembeli membeli pakaian dengan label harga Rp200.000,00, selisih harga akhir yang dibayar antara Skema 1 dan Skema 2 adalah ....

- **A. Rp3.000,00** ✅  
  <sub>Benar: Harga Skema 1 = $0{,}8(200.000) - 15.000 = 145.000$. Harga Skema 2 = $0{,}8(200.000 - 15.000) = 148.000$. Selisih = $148.000 - 145.000 = 3.000$.</sub>
- B. Rp2.500,00  
  <sub>Salah: Salah mengalikan persentase diskon terhadap potongan harga.</sub>
- C. Rp5.000,00  
  <sub>Salah: Salah menghitung harga akhir Skema 2 menjadi Rp150.000,00 sehingga selisihnya Rp5.000,00.</sub>
- D. Rp0,00  
  <sub>Salah: Mengira komposisi fungsi diskon dan potongan harga bersifat komutatif sehingga menghasilkan nilai yang persis sama.</sub>

**Pembahasan:** Misalkan $x = 200.000$.
Fungsi diskon 20%: $d(x) = x - 0{,}2x = 0{,}8x$.
Fungsi potongan harga Rp15.000,00: $p(x) = x - 15.000$.

1. Skema 1 (diskon lalu potongan harga):
$$(p \circ d)(x) = p(d(x)) = 0{,}8x - 15.000$$
$$(p \circ d)(200.000) = 0{,}8(200.000) - 15.000 = 160.000 - 15.000 = 145.000$$

2. Skema 2 (potongan harga lalu diskon):
$$(d \circ p)(x) = d(p(x)) = 0{,}8(x - 15.000)$$
$$(d \circ p)(200.000) = 0{,}8(200.000 - 15.000) = 0{,}8(185.000) = 148.000$$

Selisih harga kedua skema:
$$|148.000 - 145.000| = 3.000$$
Jadi, selisih harga akhir yang dibayar adalah Rp3.000,00.
**Acuan:** siswa — siswa hal.42

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11-b01-b-medium-bt01-015
*variasi (konteks) | C3 | 3 langkah | jenis: pemodelan biaya fungsi*

Seorang pemilik konveksi memesan gulungan kain secara daring. Toko memberlakukan biaya tambahan penanganan sebesar 5% dari harga kain, serta ongkos kirim kargo tetap senilai Rp45.000,00. Jika pengusaha tersebut membayar total sebesar Rp885.000,00, maka harga asli gulungan kain sebelum dikenai biaya tambahan dan ongkos kirim adalah ....

- A. Rp795.000,00  
  <sub>Salah: Siswa menghitung dengan cara salah: mengurangkan 5% langsung dari 840.000 ($840.000 - 42.000$).</sub>
- **B. Rp800.000,00** ✅  
  <sub>Benar: Total biaya dimodelkan dengan $B(x) = 1,05x + 45.000$. Persamaan $1,05x + 45.000 = 885.000$ memberikan $1,05x = 840.000$, sehingga $x = 840.000 / 1,05 = 800.000$.</sub>
- C. Rp840.000,00  
  <sub>Salah: Siswa hanya mengurangkan ongkos kirim ($885.000 - 45.000$) tanpa membagi dengan faktor pengali persentase 1,05.</sub>
- D. Rp825.000,00  
  <sub>Salah: Siswa salah menghitung pembagian atau mengurangkan biaya penanganan secara acak.</sub>

**Pembahasan:** Misalkan harga asli kain adalah $x$.
Biaya penanganan 5% membuat total harga kain menjadi $1,05x$.
Dengan ongkos kirim tetap Rp45.000,00, model total pengeluaran adalah:
$B(x) = 1,05x + 45.000$

Diketahui $B(x) = 885.000$, maka:
$1,05x + 45.000 = 885.000$
$1,05x = 885.000 - 45.000$
$1,05x = 840.000$
$x = \frac{840.000}{1,05} = 800.000$

Jadi, harga asli gulungan kain tersebut adalah Rp800.000,00.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11-b01-b-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: optimasi selisih fungsi*

Fungsi penerimaan total dari penjualan $x$ unit kue dinyatakan oleh $R(x) = 800x - 2x^2$, sedangkan fungsi biaya total produksi dinyatakan oleh $C(x) = 200x + 10.000$ (keduanya dalam ribuan rupiah). Keuntungan maksimum yang dapat diraih dari penjualan kue tersebut adalah ....

- A. Rp25.000.000,00  
  <sub>Salah: Siswa melakukan kesalahan perhitungan pada suku kuadrat saat menghitung nilai puncak.</sub>
- B. Rp45.000.000,00  
  <sub>Salah: Siswa lupa mengurangkan biaya tetap 10.000 dari fungsi biaya.</sub>
- C. Rp70.000.000,00  
  <sub>Salah: Siswa hanya memaksimalkan fungsi pendapatan $R(x)$ tanpa mengurangkan biaya produksi $C(x)$.</sub>
- **D. Rp35.000.000,00** ✅  
  <sub>Benar: Fungsi keuntungan $U(x) = R(x) - C(x) = -2x^2 + 600x - 10.000$. Nilai maksimum tercapai saat $x = -\frac{600}{2(-2)} = 150$. Substitusi $x = 150$ menghasilkan $U(150) = -2(22.500) + 600(150) - 10.000 = 35.000$ ribu rupiah, atau Rp35.000.000,00.</sub>

**Pembahasan:** Fungsi keuntungan $U(x)$ adalah selisih fungsi pendapatan dan biaya produksi:
$U(x) = (R - C)(x) = R(x) - C(x)$
$U(x) = (800x - 2x^2) - (200x + 10.000)$
$U(x) = -2x^2 + 600x - 10.000$

Titik puncak fungsi kuadrat terjadi pada:
$x = -\frac{b}{2a} = -\frac{600}{2(-2)} = 150$

Keuntungan maksimum:
$U(150) = -2(150)^2 + 600(150) - 10.000$
$U(150) = -2(22.500) + 90.000 - 10.000$
$U(150) = -45.000 + 90.000 - 10.000 = 35.000$ (ribu rupiah)

Dalam rupiah, keuntungan maksimum adalah $35.000 \times \text{Rp}1.000,00 = \text{Rp}35.000.000,00$.
**Acuan:** siswa — siswa hal.37

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11-b01-b-medium-bt01-017
*orisinal | C3 | 2 langkah | jenis: rekonstruksi fungsi dalam*

Diketahui fungsi $g(x) = 3x - 2$ dan rumus komposisinya $(f \circ g)(x) = 9x^2 - 3x + 1$. Nilai dari $f(4)$ adalah ....

- A. 25  
  <sub>Salah: Siswa salah hitung aljabar pada perpangkatan atau perkalian koefisien.</sub>
- B. 133  
  <sub>Salah: Siswa langsung menyubstitusikan angka 4 ke rumus $(f \circ g)(x)$ tanpa menyesuaikan domain bagian dalam.</sub>
- C. 10  
  <sub>Salah: Siswa hanya menghitung nilai $g(4) = 3(4) - 2 = 10$.</sub>
- **D. 31** ✅  
  <sub>Benar: Untuk menghitung $f(4)$, dicari nilai $x$ pembuat $g(x) = 4$, yaitu $3x - 2 = 4 \implies x = 2$. Kemudian nilai $x = 2$ disubstitusikan ke $(f \circ g)(x)$: $f(g(2)) = 9(2)^2 - 3(2) + 1 = 36 - 6 + 1 = 31$.</sub>

**Pembahasan:** Diketahui $(f \circ g)(x) = f(g(x)) = 9x^2 - 3x + 1$ dan $g(x) = 3x - 2$.

Untuk mencari nilai $f(4)$, cari nilai $x$ sehingga $g(x) = 4$:
$3x - 2 = 4$
$3x = 6$
$x = 2$

Substitusikan $x = 2$ ke dalam $(f \circ g)(x)$:
$f(g(2)) = 9(2)^2 - 3(2) + 1$
$f(4) = 9(4) - 6 + 1$
$f(4) = 36 - 6 + 1 = 31$
**Acuan:** siswa — siswa hal.42

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11-b01-b-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: persamaan komposisi bertingkat*

Diketahui fungsi-fungsi real $f(x) = 3x - 1$, $g(x) = x + 2$, dan $h(x) = x^2 - 1$. Jika $((f \circ g) \circ h)(a) = 50$ dengan $a > 0$, maka nilai $a$ adalah ....

- **A. 4** ✅  
  <sub>Benar: Komposisi $(f \circ g)(x) = 3(x + 2) - 1 = 3x + 5$. Lalu $((f \circ g) \circ h)(a) = 3(a^2 - 1) + 5 = 3a^2 + 2$. Persamaan $3a^2 + 2 = 50$ menghasilkan $3a^2 = 48 \implies a^2 = 16$. Karena $a > 0$, maka $a = 4$.</sub>
- B. 2  
  <sub>Salah: Siswa salah membagi nilai $48 / 3$ atau melakukan kesalahan penarikan akar.</sub>
- C. 5  
  <sub>Salah: Siswa salah menyederhanakan konstanta pada saat komposisi awal.</sub>
- D. 16  
  <sub>Salah: Siswa berhenti pada nilai $a^2$ dan lupa menarik akar kuadrat.</sub>

**Pembahasan:** Langkah 1: Tentukan fungsi $(f \circ g)(x)$:
$(f \circ g)(x) = f(g(x)) = 3(x + 2) - 1 = 3x + 6 - 1 = 3x + 5$

Langkah 2: Komposisikan dengan fungsi $h(x)$:
$((f \circ g) \circ h)(a) = (f \circ g)(h(a))$
$= 3(a^2 - 1) + 5
= 3a^2 - 3 + 5
= 3a^2 + 2$

Langkah 3: Selesaikan persamaan untuk $a > 0$:
$3a^2 + 2 = 50$
$3a^2 = 48$
$a^2 = 16$
$a = 4$ (karena syarat $a > 0$).
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11-b01-b-medium-bt01-019
*variasi (konteks) | C3 | 3 langkah | jenis: pemodelan tarif total*

Rani memesan satu set lemari pakaian secara daring. Toko mebel menetapkan biaya asuransi pengiriman sebesar 4% dari harga lemari dan biaya ongkos kirim kargo tetap sebesar Rp40.000,00. Jika total pembayaran yang dikeluarkan Rani adalah Rp1.860.000,00, maka harga lemari pakaian tersebut sebelum dikenai asuransi dan ongkos kirim adalah ....

- A. Rp1.820.000,00  
  <sub>Salah: Siswa hanya mengurangkan ongkos kirim tetap tetapi lupa memperhitungkan persentase biaya asuransi.</sub>
- B. Rp1.700.000,00  
  <sub>Salah: Siswa salah menghitung pembagian atau mengurangkan nilai persentase secara kasar tanpa rumus fungsi yang tepat.</sub>
- C. Rp1.747.200,00  
  <sub>Salah: Siswa mengurangkan ongkos kirim lalu langsung mengalikan dengan $(1 - 0,04) = 0,96$ alih-alih membagi dengan 1,04.</sub>
- **D. Rp1.750.000,00** ✅  
  <sub>Benar: Total biaya dimodelkan oleh fungsi $B(x) = x + 0,04x + 40.000 = 1,04x + 40.000$. Diketahui $B(x) = 1.860.000$, sehingga $1,04x = 1.860.000 - 40.000 = 1.820.000$. Diperoleh $x = \frac{1.820.000}{1,04} = 1.750.000$.</sub>

**Pembahasan:** Misalkan harga lemari pakaian adalah $x$.
1. Fungsi biaya mencakup harga barang dan asuransi 4%: $f(x) = x + 0,04x = 1,04x$.
2. Fungsi total setelah ditambah ongkos kirim kargo Rp40.000,00: $B(x) = 1,04x + 40.000$.
3. Rani membayar total Rp1.860.000,00, maka:
$$1,04x + 40.000 = 1.860.000$$
$$1,04x = 1.820.000$$
$$x = \frac{1.820.000}{1,04} = 1.750.000$$
Jadi, harga lemari pakaian sebelum dikenai asuransi dan ongkos kirim adalah Rp1.750.000,00.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11-b01-b-medium-bt01-020
*variasi (angka) | C3 | 3 langkah | jenis: inversi model diskon*

Harga awal suatu barang adalah $x$ rupiah. Sebuah toko memberikan penawaran khusus berupa diskon 25% dilanjutkan dengan potongan voucer belanja sebesar Rp35.000,00 dari harga setelah diskon. Jika seorang pembeli membayar sebesar Rp145.000,00 di kasir untuk barang tersebut, harga awal barang sebelum diskon dan potongan voucer adalah ....

- **A. Rp240.000,00** ✅  
  <sub>Benar: Harga setelah diskon 25% adalah $f(x) = (1 - 0,25)x = 0,75x$. Setelah potongan voucer, total yang dibayar adalah $g(f(x)) = 0,75x - 35.000$. Karena $0,75x - 35.000 = 145.000$, diperoleh $0,75x = 180.000$, sehingga $x = \frac{180.000}{0,75} = 240.000$.</sub>
- B. Rp225.000,00  
  <sub>Salah: Siswa menambahkan voucer menjadi Rp180.000,00 lalu mengalikannya dengan 1,25 (menambah 25%) alih-alih membaginya dengan 0,75.</sub>
- C. Rp180.000,00  
  <sub>Salah: Siswa hanya menambahkan potongan voucer ke harga bayar dan lupa memperhitungkan diskon 25%.</sub>
- D. Rp720.000,00  
  <sub>Salah: Siswa keliru memodelkan persentase yang harus dibayar sebagai $0,25x$ bukan $0,75x$, sehingga membagi $180.000$ dengan $0,25$.</sub>

**Pembahasan:** Misalkan harga awal barang adalah $x$.
1. Setelah diskon 25%, harga menjadi:
$$f(x) = (1 - 0,25)x = 0,75x$$
2. Setelah dipotong voucer sebesar Rp35.000,00, harga akhir menjadi:
$$y = (g \circ f)(x) = 0,75x - 35.000$$
3. Karena pembeli membayar Rp145.000,00:
$$0,75x - 35.000 = 145.000$$
$$0,75x = 180.000$$
$$x = \frac{180.000}{0,75} = 240.000$$
Jadi, harga awal barang tersebut adalah Rp240.000,00.
**Acuan:** siswa — siswa hal.42 Masalah Pertama

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11-b01-b-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: analisis_kebijakan_diskon*

Sebuah pusat perbelanjaan memberikan dua pilihan promo akhir pekan untuk pembelian barang dengan harga awal di atas Rp60.000,00:
- **Pilihan A**: Diskon 30% terlebih dahulu, kemudian dilanjutkan dengan potongan voucer sebesar Rp60.000,00.
- **Pilihan B**: Potongan voucer sebesar Rp60.000,00 terlebih dahulu, kemudian dilanjutkan dengan diskon 30%.

Berdasarkan konsep komposisi fungsi, manakah pernyataan berikut yang paling tepat mengenai perbandingan kedua promo tersebut?

- **A. Pilihan A selalu lebih murah Rp18.000,00 dibandingkan Pilihan B untuk setiap harga barang.** ✅  
  <sub>Benar: Harga akhir Pilihan A dirumuskan $(g \circ f)(x) = 0{,}7x - 60.000$, sedangkan Pilihan B dirumuskan $(f \circ g)(x) = 0{,}7(x - 60.000) = 0{,}7x - 42.000$. Selisihnya adalah $(0{,}7x - 42.000) - (0{,}7x - 60.000) = 18.000$, sehingga Pilihan A selalu lebih hemat Rp18.000,00.</sub>
- B. Pilihan B selalu lebih murah Rp18.000,00 dibandingkan Pilihan A untuk setiap harga barang.  
  <sub>Salah: Tertukar dalam membandingkan hasil akhir kedua fungsi komposisi.</sub>
- C. Pilihan A selalu lebih murah Rp42.000,00 dibandingkan Pilihan B untuk setiap harga barang.  
  <sub>Salah: Mengira selisih diperoleh dari nilai potongan $0{,}7 \times 60.000 = 42.000$ secara langsung.</sub>
- D. Kedua pilihan promo selalu menghasilkan harga akhir yang sama karena urutan operasi tidak memengaruhi hasil.  
  <sub>Salah: Menganggap keliru bahwa komposisi fungsi perkalian dan pengurangan selalu bersifat komutatif.</sub>

**Pembahasan:** Misalkan $x$ adalah harga awal barang dalam rupiah, fungsi diskon $30\%$ adalah $f(x) = (1 - 0{,}30)x = 0{,}7x$, dan fungsi potongan voucer adalah $g(x) = x - 60.000$.

1. Menentukan model fungsi Pilihan A (diskon dilanjutkan potongan harga):
$$H_A(x) = (g \circ f)(x) = g(f(x)) = g(0{,}7x) = 0{,}7x - 60.000$$

2. Menentukan model fungsi Pilihan B (potongan harga dilanjutkan diskon):
$$H_B(x) = (f \circ g)(x) = f(g(x)) = f(x - 60.000) = 0{,}7(x - 60.000) = 0{,}7x - 42.000$$

3. Membandingkan harga akhir kedua opsi:
$$H_B(x) - H_A(x) = (0{,}7x - 42.000) - (0{,}7x - 60.000) = -42.000 + 60.000 = 18.000$$

Karena nilai $H_B(x) - H_A(x) = 18.000 > 0$, maka harga pada Pilihan A selalu Rp18.000,00 lebih murah (lebih hemat) daripada Pilihan B.
**Acuan:** siswa — siswa hal.41 3. Komposisi Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11-b01-b-hard-bt01-002
*orisinal | C5 | 5 langkah | jenis: interval_parameter_domain*

Diketahui fungsi $f(x) = \sqrt{16 - x^2}$ dan $g(x) = 2x + c$. Agar fungsi komposisi $(f \circ g)(x)$ dapat terdefinisi untuk seluruh bilangan real $x$ pada interval tertutup $[-1, 3]$, maka nilai konstanta $c$ yang memenuhi adalah ....

- A. $c = 2$  
  <sub>Salah: Kesalahan tanda saat menyelesaikan pertidaksamaan batas atas dan bawah.</sub>
- B. $c = -4$  
  <sub>Salah: Hanya menyamakan langsung nilai $c$ dengan batas bawah daerah asal fungsi $f$.</sub>
- **C. $c = -2$** ✅  
  <sub>Benar: Domain $f$ adalah $[-4, 4]$. Agar $(f \circ g)(x)$ terdefinisi pada $[-1, 3]$, daerah hasil $g([-1, 3]) = [c - 2, c + 6]$ harus merupakan himpunan bagian dari $[-4, 4]$, sehingga diperoleh $c - 2 \ge -4 \implies c \ge -2$ dan $c + 6 \le 4 \implies c \le -2$, yang memberikan nilai unik $c = -2$.</sub>
- D. $-2 \le c \le 2$  
  <sub>Salah: Mengira solusi berupa interval rentang tanpa menyadari irisan kedua syarat menghasilkan nilai tunggal.</sub>

**Pembahasan:** Langkah 1: Tentukan domain dari fungsi $f(x)$:
Syarat di dalam akar kuadrat tidak boleh negatif:
$$16 - x^2 \ge 0 \iff x^2 \le 16 \iff -4 \le x \le 4$$
Jadi, daerah asal $D_f = [-4, 4]$.

Langkah 2: Tentukan range dari $g(x) = 2x + c$ untuk $x \in [-1, 3]$:
Karena $g(x)$ merupakan fungsi linear yang monoton naik:
- Nilai minimum tercapai pada $x = -1$, yaitu $g(-1) = 2(-1) + c = c - 2$.
- Nilai maksimum tercapai pada $x = 3$, yaitu $g(3) = 2(3) + c = c + 6$.
Jadi, $R_g = [c - 2, c + 6]$.

Langkah 3: Terapkan syarat komposisi fungsi:
Agar $(f \circ g)(x)$ terdefinisi untuk seluruh $x \in [-1, 3]$, maka $R_g \subseteq D_f$, yang berarti:
$$[c - 2, c + 6] \subseteq [-4, 4]$$

Langkah 4: Tentukan pertidaksamaan untuk parameter $c$:
1) $c - 2 \ge -4 \implies c \ge -2$
2) $c + 6 \le 4 \implies c \le -2$

Langkah 5: Tentukan irisan nilai $c$:
Irisan dari $c \ge -2$ dan $c \le -2$ adalah tepat satu nilai, yaitu $c = -2$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11-b01-b-hard-bt01-003
*orisinal | C6 | 4 langkah | jenis: analisis_komutatif_linear*

Meskipun secara umum komposisi fungsi tidak bersifat komutatif, dua fungsi tertentu dapat memenuhi sifat komutatif $(f \circ g)(x) = (g \circ f)(x)$ untuk seluruh $x \in \mathbb{R}$. Diketahui fungsi linear $f(x) = 3x - 8$ dan $g(x) = -3x + n$. Nilai konstanta $n$ agar kedua fungsi tersebut saling komutatif adalah ....

- A. $32$  
  <sub>Salah: Lupa membagi dengan koefisien $2$ dari variabel $n$ pada langkah akhir.</sub>
- B. $8$  
  <sub>Salah: Kesalahan perhitungan tanda $2n = 24 - 8 = 16$ sehingga $n = 8$.</sub>
- **C. $16$** ✅  
  <sub>Benar: $(f \circ g)(x) = 3(-3x + n) - 8 = -9x + 3n - 8$, sedangkan $(g \circ f)(x) = -3(3x - 8) + n = -9x + 24 + n$. Menyamakan konstanta menghasilkan $3n - 8 = 24 + n \iff 2n = 32 \iff n = 16$.</sub>
- D. $-16$  
  <sub>Salah: Kesalahan aljabar saat memindahkan ruas konstanta sehingga bertanda negatif.</sub>

**Pembahasan:** Langkah 1: Menentukan fungsi komposisi $(f \circ g)(x)$:
$$(f \circ g)(x) = f(g(x)) = f(-3x + n) = 3(-3x + n) - 8 = -9x + 3n - 8$$

Langkah 2: Menentukan fungsi komposisi $(g \circ f)(x)$:
$$(g \circ f)(x) = g(f(x)) = g(3x - 8) = -3(3x - 8) + n = -9x + 24 + n$$

Langkah 3: Menyamakan kedua hasil komposisi fungsi:
Agar $(f \circ g)(x) = (g \circ f)(x)$ berlaku untuk setiap $x \in \mathbb{R}$, koefisien $x$ dan suku konstanta pada kedua ruas harus bernilai sama:
$$-9x + 3n - 8 = -9x + 24 + n$$

Langkah 4: Menyelesaikan nilai $n$:
$$3n - 8 = 24 + n$$
$$3n - n = 24 + 8$$
$$2n = 32$$
$$n = 16$$
**Acuan:** siswa — siswa hal.45

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11-b01-b-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: domain_pembagian_fungsi*

Diketahui dua fungsi real $f(x) = \sqrt{25 - x^2}$ dan $g(x) = \sqrt{x^2 - 9}$. Daerah asal (domain) dari fungsi pembagian $h(x) = \left(\frac{f}{g}\right)(x)$ adalah ....

- A. $\{x \in \mathbb{R} \mid -5 < x < -3 \text{ atau } 3 < x < 5\}$  
  <sub>Salah: Keliru menganggap batas pembilang juga tidak boleh bernilai sama dengan nol.</sub>
- **B. $\{x \in \mathbb{R} \mid -5 \le x < -3 \text{ atau } 3 < x \le 5\}$** ✅  
  <sub>Benar: $D_f = [-5, 5]$ dan $D_g = (-\infty, -3] \cup [3, \infty)$ sehingga $D_f \cap D_g = [-5, -3] \cup [3, 5]$. Karena $g(x) \neq 0$, titik pembuat nol $x = \pm 3$ dikeluarkan dari domain sehingga menjadi $[-5, -3) \cup (3, 5]$.</sub>
- C. $\{x \in \mathbb{R} \mid -5 \le x \le -3 \text{ atau } 3 \le x \le 5\}$  
  <sub>Salah: Lupa mengecualikan pembuat nol pada penyebut $g(x) = 0$.</sub>
- D. $\{x \in \mathbb{R} \mid -3 < x < 3\}$  
  <sub>Salah: Salah menentukan arah pertidaksamaan kuadrat $x^2 - 9 \ge 0$ sebagai rentang dalam.</sub>

**Pembahasan:** Langkah 1: Menentukan daerah asal fungsi pembilang $f(x) = \sqrt{25 - x^2}$:
$$25 - x^2 \ge 0 \iff x^2 \le 25 \iff -5 \le x \le 5$$
Jadi, $D_f = [-5, 5]$.

Langkah 2: Menentukan daerah asal fungsi penyebut $g(x) = \sqrt{x^2 - 9}$:
$$x^2 - 9 \ge 0 \iff x^2 \ge 9 \iff x \le -3 \text{ atau } x \ge 3$$
Jadi, $D_g = (-\infty, -3] \cup [3, \infty)$.

Langkah 3: Menentukan irisan kedua domain $D_f \cap D_g$:
$$[-5, 5] \cap ((-\infty, -3] \cup [3, \infty)) = [-5, -3] \cup [3, 5]$$

Langkah 4: Menentukan syarat pembagi tidak boleh bernilai nol ($g(x) \neq 0$):
$$\sqrt{x^2 - 9} \neq 0 \iff x^2 - 9 \neq 0 \iff x \neq -3 \text{ dan } x \neq 3$$

Langkah 5: Mengeluarkan pembuat nol penyebut dari irisan daerah asal:
$$D_{f/g} = (D_f \cap D_g) \setminus \{-3, 3\} = [-5, -3) \cup (3, 5]$$
Dalam notasi himpunan: $\{x \in \mathbb{R} \mid -5 \le x < -3 \text{ atau } 3 < x \le 5\}$.
**Acuan:** siswa — siswa hal.39

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11-b01-b-hard-bt01-005
*variasi (angka) | C5 | 4 langkah | jenis: evaluasi_anggaran_komposisi*

Kebutuhan kertas untuk mencetak $x$ eksemplar majalah sekolah dinyatakan oleh fungsi $k(x) = 160(x + 5)$ lembar. Biaya total untuk pengadaan $k$ lembar kertas mengikuti fungsi $B(k) = 450k + 50.000$ (dalam rupiah). Jika pihak sekolah mengalokasikan anggaran sebesar Rp11.570.000,00 untuk mencetak 155 eksemplar majalah, pernyataan evaluasi anggaran yang paling tepat adalah ....

- A. Anggaran kurang sebesar Rp50.000,00  
  <sub>Salah: Menghitung pengeluaran menjadi $11.620.000$ karena keliru menambahkan biaya tetap dua kali.</sub>
- B. Anggaran mencukupi dengan sisa dana Rp50.000,00  
  <sub>Salah: Lupa menjumlahkan konstanta biaya tetap Rp50.000,00 pada fungsi $B(k)$.</sub>
- C. Anggaran kurang sebesar Rp360.000,00  
  <sub>Salah: Menghitung $k(155) = 160(155) + 5 = 24.805$ lembar lalu salah mengalikan koefisien.</sub>
- **D. Anggaran mencukupi dan tersisa Rp0,00 (tepat habis)** ✅  
  <sub>Benar: $k(155) = 160(160) = 25.600$ lembar; $B(25.600) = 450(25.600) + 50.000 = 11.520.000 + 50.000 = 11.570.000$, tepat sama dengan alokasi dana.</sub>

**Pembahasan:** Langkah 1: Menghitung kebutuhan lembar kertas untuk $x = 155$:
$k(155) = 160(155 + 5) = 160 	imes 160 = 25.600$ lembar.

Langkah 2: Menghitung biaya total menggunakan fungsi komposisi $(B \circ k)(155)$:
$B(25.600) = 450(25.600) + 50.000 = 11.520.000 + 50.000 = 11.570.000$.

Langkah 3: Membandingkan dengan alokasi anggaran:
Biaya yang dibutuhkan adalah Rp11.570.000,00, sehingga anggaran tepat habis tanpa sisa.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11-b01-b-hard-bt01-006
*variasi (angka) | C5 | 4 langkah | jenis: evaluasi_range_komposisi*

Diketahui dua fungsi real $f(x) = \frac{1}{3x + 4}$ dan $g(x) = 3x^2 + 2$. Daerah hasil (range) dari fungsi komposisi $(f \circ g)(x)$ untuk seluruh $x \in \mathbb{R}$ adalah ....

- A. $\left\{y \in \mathbb{R} \mid 0 < y \le \frac{1}{6}\right\}$  
  <sub>Salah: Keliru mengalikan $3(3x^2 + 2) + 4$ menjadi $9x^2 + 6$ karena lupa menambahkan konstanta $4$.</sub>
- **B. $\left\{y \in \mathbb{R} \mid 0 < y \le \frac{1}{10}\right\}$** ✅  
  <sub>Benar: $(f \circ g)(x) = \frac{1}{9x^2 + 10}$. Karena $x^2 \ge 0$, penyebut bernilai minimum $10$ saat $x = 0$, sehingga nilai maksimum pecahan adalah $\frac{1}{10}$ dan selalu positif mendekati $0$.</sub>
- C. $\left\{y \in \mathbb{R} \mid y \ge \frac{1}{10}\right\}$  
  <sub>Salah: Terbalik menafsirkan bahwa penyebut minimum menghasilkan nilai pecahan minimum.</sub>
- D. $\left\{y \in \mathbb{R} \mid 0 \le y \le \frac{1}{10}\right\}$  
  <sub>Salah: Mengira nilai pecahan pembilang satu dapat mencapai angka nol.</sub>

**Pembahasan:** Langkah 1: Menentukan rumus komposisi:
$(f \circ g)(x) = f(g(x)) = \frac{1}{3(3x^2 + 2) + 4} = \frac{1}{9x^2 + 10}$.

Langkah 2: Menentukan batas nilai penyebut:
Untuk sebarang bilangan real $x$, berlaku $x^2 \ge 0$, sehingga $9x^2 \ge 0$.
Akibatnya, penyebut memenuhi $9x^2 + 10 \ge 10$.

Langkah 3: Menentukan batas nilai pecahan:
Karena penyebut bernilai paling kecil $10$, maka nilai terbesar dari $\frac{1}{9x^2 + 10}$ adalah $\frac{1}{10}$ (tercapai saat $x = 0$).
Karena pembilang bertanda positif dan penyebut selalu positif untuk seluruh $x \in \mathbb{R}$, pecahan tidak pernah bernilai nol atau negatif.
Jadi, daerah hasil adalah $\left\{y \in \mathbb{R} \mid 0 < y \le \frac{1}{10}\right\}$.
**Acuan:** siswa — siswa hal.46 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11-b01-b-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: analisis_eksistensi_komposisi*

Diketahui fungsi $f(x) = \sqrt{x - k}$ dan $g(x) = 8 - x^2$. Agar fungsi komposisi $(f \circ g)(x)$ terdefinisi untuk setiap nilai $x$ pada interval $-2 \le x \le 2$, nilai bilangan bulat terbesar dari $k$ yang memenuhi adalah ....

- **A. 4** ✅  
  <sub>Benar: Pada interval $[-2, 2]$, range $g(x)$ adalah $[4, 8]$. Syarat komposisi terdefinisi menuntut $[4, 8] \subseteq [k, \infty)$, sehingga $k \le 4$. Nilai bulat terbesar adalah 4.</sub>
- B. -4  
  <sub>Salah: Salah tanda dalam menyelesaikan pertidaksamaan nilai minimum $8 - 2^2 \ge k$.</sub>
- C. 0  
  <sub>Salah: Menganggap batas bawah domain harus nol tanpa memperhitungkan pergeseran nilai parameter $k$.</sub>
- D. 8  
  <sub>Salah: Menggunakan nilai maksimum $g(x)$ alih-alih nilai minimumnya sebagai batas bawah domain $f$.</sub>

**Pembahasan:** Langkah 1: Menentukan daerah asal fungsi $f(x)$:
Agar $f(x) = \sqrt{x - k}$ terdefinisi pada bilangan real, disyaratkan $x - k \ge 0 \iff x \ge k$. Jadi, $D_f = [k, \infty)$.

Langkah 2: Menentukan daerah hasil $g(x)$ pada domain $[-2, 2]$:
Fungsi kuadrat $g(x) = 8 - x^2$ terbuka ke bawah dengan puncak di $x = 0$.
Nilai maksimum: $g(0) = 8$.
Nilai minimum di ujung interval: $g(-2) = g(2) = 8 - 4 = 4$.
Jadi, $R_g = [4, 8]$.

Langkah 3: Menerapkan syarat komposisi fungsi:
Agar $(f \circ g)(x)$ terdefinisi pada interval tersebut, maka seluruh nilai $g(x)$ harus berada di dalam domain $f$, yaitu $R_g \subseteq D_f$:
$[4, 8] \subseteq [k, \infty) \iff k \le 4$.

Langkah 4: Nilai bulat terbesar dari $k$ yang memenuhi $k \le 4$ adalah 4.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11-b01-b-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: evaluasi_parameter_asosiatif*

Diketahui tiga buah fungsi real $f(x) = 2x - 1$, $g(x) = x^2 + 1$, dan $h(x) = ax + 2$ dengan parameter $a > 0$. Berdasarkan sifat asosiatif komposisi fungsi, diketahui bahwa $((f \circ g) \circ h)(1) = 33$. Nilai dari $3a^2 - 2a$ adalah ....

- **A. 8** ✅  
  <sub>Benar: $h(1) = a+2$; $g(a+2) = (a+2)^2 + 1$; $f(g(h(1))) = 2((a+2)^2 + 1) - 1 = 2(a+2)^2 + 1 = 33 \Rightarrow (a+2)^2 = 16 \Rightarrow a = 2$. Maka $3(2)^2 - 2(2) = 12 - 4 = 8$.</sub>
- B. 16  
  <sub>Salah: Langsung menggunakan nilai $(a + 2)^2 = 16$ sebagai jawaban akhir tanpa menghitung nilai ekspresi.</sub>
- C. 5  
  <sub>Salah: Keliru memperoleh $a = 1$ akibat salah mengalikan koefisien 2 ke seluruh kurung.</sub>
- D. 33  
  <sub>Salah: Tertukar antara hasil akhir yang diminta dengan nilai fungsi komposisi pada soal.</sub>

**Pembahasan:** Langkah 1: Menerapkan sifat asosiatif:
$((f \circ g) \circ h)(1) = (f \circ (g \circ h))(1) = f(g(h(1)))$.

Langkah 2: Menghitung nilai fungsi terdalam:
$h(1) = a(1) + 2 = a + 2$.

Langkah 3: Mengomposisikan ke dalam fungsi $g$:
$g(h(1)) = g(a + 2) = (a + 2)^2 + 1$.

Langkah 4: Mengomposisikan ke dalam fungsi $f$:
$f(g(h(1))) = 2\left[(a + 2)^2 + 1\right] - 1 = 2(a + 2)^2 + 2 - 1 = 2(a + 2)^2 + 1$.

Langkah 5: Menyelesaikan nilai $a$ dan menghitung ekspresi akhir:
$2(a + 2)^2 + 1 = 33$
$2(a + 2)^2 = 32 \iff (a + 2)^2 = 16$.
Karena disyaratkan $a > 0$, maka $a + 2 = 4 \iff a = 2$.
Nilai dari $3a^2 - 2a = 3(2^2) - 2(2) = 12 - 4 = 8$.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11-b01-b-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: dekomposisi_dan_akar_fungsi*

Diketahui rumus komposisi dua fungsi adalah $(f \circ g)(x) = 4x^2 - 20x + 21$ dan fungsi dalam $g(x) = 2x - 3$. Jika $x_1$ dan $x_2$ merupakan akar-akar persamaan $f(x) = 5$ dengan $x_1 > x_2$, maka nilai dari $2x_1 + 3x_2$ adalah ....

- A. 13  
  <sub>Salah: Tertukar menetapkan nilai $x_1$ dan $x_2$ sehingga menghitung $2(-1) + 3(5) = 13$.</sub>
- B. -7  
  <sub>Salah: Lupa membalik tanda saat memindahkan suku konstanta ke ruas kiri menjadi $x^2 - 4x + 5 = 0$.</sub>
- **C. 7** ✅  
  <sub>Benar: Misal $u = 2x - 3 \Rightarrow 2x = u + 3$, diperoleh $f(u) = u^2 - 4u$. Persamaan $x^2 - 4x - 5 = 0$ menghasilkan akar $x_1 = 5$ dan $x_2 = -1$. Nilai $2(5) + 3(-1) = 7$.</sub>
- D. 9  
  <sub>Salah: Salah menentukan tanda pemfaktoran menjadi $(x + 5)(x - 1) = 0$ sehingga akarnya $1$ dan $-5$.</sub>

**Pembahasan:** Langkah 1: Melakukan dekomposisi fungsi dengan pemisalan:
Misalkan $u = g(x) = 2x - 3$, maka $2x = u + 3$.

Langkah 2: Menentukan rumus fungsi $f(u)$:
$(f \circ g)(x) = (2x)^2 - 10(2x) + 21$
$f(u) = (u + 3)^2 - 10(u + 3) + 21$
$f(u) = u^2 + 6u + 9 - 10u - 30 + 21 = u^2 - 4u$.
Sehingga rumus fungsi adalah $f(x) = x^2 - 4x$.

Langkah 3: Menyusun persamaan $f(x) = 5$:
$x^2 - 4x = 5 \iff x^2 - 4x - 5 = 0$.

Langkah 4: Menentukan akar-akar persamaan:
$(x - 5)(x + 1) = 0 \iff x = 5$ atau $x = -1$.
Karena $x_1 > x_2$, maka $x_1 = 5$ dan $x_2 = -1$.

Langkah 5: Menghitung nilai yang diminta:
$2x_1 + 3x_2 = 2(5) + 3(-1) = 10 - 3 = 7$.
**Acuan:** siswa — siswa hal.42

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11-b01-b-hard-bt01-010
*variasi (angka) | C5 | 5 langkah | jenis: kesamaan_fungsi_komposisi*

Diketahui fungsi $f(x) = 9x - 8$ dan $g(x) = mx + n$. Jika kesamaan $(f \circ g)(x) = (g \circ f)(x)$ berlaku untuk setiap bilangan real $x$, dan diketahui pula bahwa $g(2) = 10$, maka hasil kali $m \cdot n$ adalah ....

- A. -9  
  <sub>Salah: Siswa salah mengoperasikan nilai parameter menjadi m + n = 1 atau keliru mengeliminasi sistem persamaan linear.</sub>
- **B. -72** ✅  
  <sub>Benar: Dari $(f \circ g)(x) = (g \circ f)(x)$ diperoleh $9(mx + n) - 8 = m(9x - 8) + n$, sehingga $9n - 8 = -8m + n \iff m + n = 1$. Dari $g(2) = 10$ diperoleh $2m + n = 10$. Penyelesaian SPLDV menghasilkan $m = 9$ dan $n = -8$, sehingga $m \cdot n = -72$.</sub>
- C. 72  
  <sub>Salah: Kesalahan tanda aljabar saat menyelesaikan eliminasi sehingga diperoleh n = 8.</sub>
- D. 10  
  <sub>Salah: Siswa keliru menganggap hasil kali parameter sama dengan nilai masukan g(2).</sub>

**Pembahasan:** Langkah 1: Menentukan rumus $(f \circ g)(x)$:
$$(f \circ g)(x) = f(g(x)) = 9(mx + n) - 8 = 9mx + 9n - 8$$

Langkah 2: Menentukan rumus $(g \circ f)(x)$:
$$(g \circ f)(x) = g(f(x)) = m(9x - 8) + n = 9mx - 8m + n$$

Langkah 3: Menyamakan kedua komposisi:
$$9mx + 9n - 8 = 9mx - 8m + n$$
$$9n - 8 = -8m + n$$
$$8m + 8n = 8 \implies m + n = 1 \quad \text{...(Persamaan 1)}$$

Langkah 4: Menggunakan nilai $g(2) = 10$:
$$g(2) = 2m + n = 10 \quad \text{...(Persamaan 2)}$$

Langkah 5: Menyelesaikan sistem persamaan linear:
Kurangkan Persamaan 2 dengan Persamaan 1:
$$(2m + n) - (m + n) = 10 - 1 \implies m = 9$$
Substitusikan $m = 9$ ke Persamaan 1:
$$9 + n = 1 \implies n = -8$$

Maka hasil kali $m \cdot n = 9 \times (-8) = -72$.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11-b01-b-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: analisis_domain_komposisi*

Diketahui fungsi $f(x) = \frac{1}{x - 5}$ dan $g(x) = x^2 - 4x + k$. Agar fungsi komposisi $(f \circ g)(x)$ terdefinisi untuk seluruh bilangan real $x$, maka batasan nilai konstanta $k$ yang memenuhi adalah ....

- A. $k \ge 9$  
  <sub>Salah: Menggunakan tanda pertidaksamaan non-ketat sehingga saat k = 9 penyebut bernilai nol di x = 2.</sub>
- B. $k < 9$  
  <sub>Salah: Kesalahan membalik tanda ketaksamaan saat membagi kedua ruas dengan koefisien negatif.</sub>
- **C. $k > 9$** ✅  
  <sub>Benar: Agar terdefinisi pada R, penyebut g(x) - 5 tidak boleh memiliki pembuat nol real, sehingga diskriminan x^2 - 4x + k - 5 = 0 harus bernilai negatif (D < 0), menghasilkan k > 9.</sub>
- D. $k > 1$  
  <sub>Salah: Siswa lupa mengurangkan nilai 5 pada konstanta saat membentuk persamaan kuadrat penyebut.</sub>

**Pembahasan:** Langkah 1: Menentukan bentuk fungsi komposisi $(f \circ g)(x)$:
$$(f \circ g)(x) = f(g(x)) = \frac{1}{g(x) - 5} = \frac{1}{x^2 - 4x + k - 5}$$

Langkah 2: Menentukan syarat keterdefinisian fungsi rasional:
Fungsi $(f \circ g)(x)$ terdefinisi untuk seluruh $x \in \mathbb{R}$ jika dan hanya jika penyebut tidak pernah bernilai nol:
$$x^2 - 4x + (k - 5) \neq 0 \quad \text{untuk setiap } x \in \mathbb{R}$$

Langkah 3: Menerapkan syarat diskriminan persamaan kuadrat tidak memiliki akar real:
Persamaan $x^2 - 4x + (k - 5) = 0$ tidak boleh memiliki solusi real, sehingga diskriminannya harus negatif ($D < 0$):
$$D = b^2 - 4ac < 0$$
$$(-4)^2 - 4(1)(k - 5) < 0$$
$$16 - 4k + 20 < 0$$
$$36 - 4k < 0$$

Langkah 4: Menyelesaikan pertidaksamaan:
$$-4k < -36$$
$$k > 9$$

Jadi, batasan nilai yang memenuhi adalah $k > 9$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11-b01-b-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: evaluasi_kebijakan_diskon*

Sebuah toko swalayan menawarkan dua skema promosi untuk barang dengan harga awal $x$ rupiah:
- **Skema A**: Diskon 20% terlebih dahulu, kemudian dilanjutkan dengan potongan kupon sebesar Rp50.000,00.
- **Skema B**: Potongan kupon sebesar Rp30.000,00 terlebih dahulu, kemudian dilanjutkan dengan diskon 25%.

Dengan asumsi kedua kupon dapat digunakan tanpa menghasilkan harga akhir negatif, interval harga awal barang $x$ agar Skema A memberikan harga akhir yang **lebih murah** daripada Skema B adalah ....

- A. $\text{Rp}30.000,00 \le x < \text{Rp}550.000,00$  
  <sub>Salah: Siswa salah menetapkan batas bawah keberlakuan kupon Skema A menggunakan potongan Skema B.</sub>
- **B. $\text{Rp}62.500,00 \le x < \text{Rp}550.000,00$** ✅  
  <sub>Benar: Fungsi harga akhir A(x) = 0,8x - 50.000 dan B(x) = 0,75x - 22.500. Pertidaksamaan A(x) < B(x) menghasilkan x < 550.000, dengan batas bawah x >= 62.500 agar 0,8x >= 50.000.</sub>
- C. $x > \text{Rp}550.000,00$  
  <sub>Salah: Siswa terbalik dalam menginterpretasikan tanda pertidaksamaan lebih murah.</sub>
- D. $x < \text{Rp}450.000,00$  
  <sub>Salah: Siswa lupa mengalikan faktor diskon 25% ke nominal kupon pada Skema B.</sub>

**Pembahasan:** Langkah 1: Memodelkan fungsi harga akhir Skema A sebagai fungsi komposisi:
$$A(x) = (1 - 0{,}20)x - 50.000 = 0{,}8x - 50.000$$
Syarat harga setelah diskon mencukupi potongan kupon Rp50.000,00:
$$0{,}8x \ge 50.000 \iff x \ge 62.500$$

Langkah 2: Memodelkan fungsi harga akhir Skema B sebagai fungsi komposisi:
$$B(x) = (1 - 0{,}25)(x - 30.000) = 0{,}75(x - 30.000) = 0{,}75x - 22.500$$

Langkah 3: Menyusun pertidaksamaan agar Skema A lebih murah dari Skema B:
$$A(x) < B(x)$$
$$0{,}8x - 50.000 < 0{,}75x - 22.500$$

Langkah 4: Menyelesaikan pertidaksamaan:
$$0{,}8x - 0{,}75x < 50.000 - 22.500$$
$$0{,}05x < 27.500$$
$$x < \frac{27.500}{0{,}05} = 550.000$$

Langkah 5: Menggabungkan dengan syarat batas nilai $x$:
$$\text{Rp}62.500,00 \le x < \text{Rp}550.000,00$$
**Acuan:** siswa — siswa hal.42

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11-b01-b-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: ekstremum_komposisi_fungsi*

Diketahui tiga buah fungsi real $f(x) = 2x + 3$, $g(x) = 3x - 1$, dan $h(x) = x^2 - 4x + 5$. Nilai minimum dari fungsi komposisi $k(x) = (f \circ (g \circ h))(x)$ untuk seluruh $x \in \mathbb{R}$ adalah ....

- A. 2  
  <sub>Salah: Siswa hanya menghitung sampai nilai minimum komposisi dua fungsi g(h(x)) tanpa mengomposisikannya dengan f.</sub>
- B. 5  
  <sub>Salah: Siswa hanya mengambil nilai konstanta fungsi terdalam h(x).</sub>
- C. 11  
  <sub>Salah: Kesalahan perhitungan saat mengevaluasi nilai balik kuadratik hasil komposisi.</sub>
- **D. 7** ✅  
  <sub>Benar: Fungsi h(x) memiliki nilai minimum 1 pada x = 2. Karena g dan f merupakan fungsi linear monoton naik, k(x) mencapai nilai minimum pada f(g(1)) = f(2) = 2(2) + 3 = 7.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai minimum fungsi terdalam $h(x)$:
$$h(x) = x^2 - 4x + 5 = (x - 2)^2 + 1$$
Karena $(x - 2)^2 \ge 0$, maka nilai minimum dari $h(x)$ adalah $h_{\min} = 1$ saat $x = 2$.

Langkah 2: Menentukan komposisi $(g \circ h)(x)$:
Karena $g(u) = 3u - 1$ adalah fungsi linear monoton naik (gradien $3 > 0$), maka nilai minimum $(g \circ h)(x)$ terjadi saat $h(x)$ minimum:
$$(g \circ h)_{\min} = g(1) = 3(1) - 1 = 2$$

Langkah 3: Menentukan nilai minimum fungsi komposisi $k(x) = f((g \circ h)(x))$:
Karena $f(v) = 2v + 3$ juga monoton naik (gradien $2 > 0$), maka nilai minimum $k(x)$ terjadi saat $(g \circ h)(x)$ minimum:
$$k_{\min} = f(2) = 2(2) + 3 = 7$$

(Dapat pula dibuktikan dengan menyusun rumus lengkap $k(x) = 2(3(x^2 - 4x + 5) - 1) + 3 = 6x^2 - 24x + 31$, dengan titik puncak di $x = -\frac{-24}{2(6)} = 2$, sehingga $k(2) = 6(4) - 48 + 31 = 7$).
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11-b01-b-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: dekomposisi_nilai_fungsi*

Diketahui rumus komposisi dua fungsi $(f \circ g)(x) = \frac{4x - 1}{2x + 3}$ dan fungsi luar $f(x) = \frac{x + 1}{x - 2}$ untuk $x \neq 2$. Nilai dari $g(5)$ adalah ....

- **A. $\frac{17}{2}$** ✅  
  <sub>Benar: Substitusi x = 5 menghasilkan (f o g)(5) = 19/13. Persamaan f(g(5)) = 19/13 diselesaikan dengan mengalikan silang sehingga diperoleh g(5) = 17/2.</sub>
- B. $\frac{13}{6}$  
  <sub>Salah: Siswa melakukan kesalahan aritmetika dalam menyelesaikan persamaan pecahan.</sub>
- C. $\frac{19}{13}$  
  <sub>Salah: Siswa mengira nilai (f o g)(5) adalah nilai dari g(5).</sub>
- D. $-\frac{17}{2}$  
  <sub>Salah: Kesalahan tanda aljabar saat memindahkan suku sejenis pada persamaan linear.</sub>

**Pembahasan:** Langkah 1: Menghitung nilai dari $(f \circ g)(5)$ secara langsung dari rumus komposisinya:
$$(f \circ g)(5) = \frac{4(5) - 1}{2(5) + 3} = \frac{20 - 1}{10 + 3} = \frac{19}{13}$$

Langkah 2: Menghubungkan definisi komposisi fungsi dengan fungsi luar:
Berdasarkan definisi komposisi fungsi:
$$(f \circ g)(5) = f(g(5)) = \frac{19}{13}$$

Langkah 3: Membentuk persamaan aljabar dengan memisalkan $g(5) = k$:
$$f(k) = \frac{k + 1}{k - 2} = \frac{19}{13}$$

Langkah 4: Menyelesaikan persamaan pecahan linear:
$$13(k + 1) = 19(k - 2)$$
$$13k + 13 = 19k - 38$$
$$13 + 38 = 19k - 13k$$
$$51 = 6k$$
$$k = \frac{51}{6} = \frac{17}{2}$$

Jadi, nilai dari $g(5) = \frac{17}{2}$.
**Acuan:** siswa — siswa hal.42

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas11-b01-b-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: analisis_syarat_eksistensi_komposisi*

Diketahui fungsi $f(x) = \sqrt{18 - x}$ dan $g(x) = x^2 - 4x + c$ dengan daerah asal $D_g = \{x \in \mathbb{R} \mid 1 \le x \le 5\}$. Berdasarkan syarat komposisi bahwa daerah hasil $R_g \subseteq D_f$, batas nilai maksimum dari konstanta $c$ agar fungsi komposisi $(f \circ g)(x)$ terdefinisi untuk seluruh $x \in D_g$ adalah ....

- A. 22  
  <sub>Salah: Menggunakan titik minimum $x = 2$ di mana $g(2) = c - 4$, lalu mensyaratkan $c - 4 \le 18 \implies c \le 22$ (salah memilih ekstremum maksimum).</sub>
- B. 15  
  <sub>Salah: Mengevaluasi $g(x)$ pada ujung kiri interval $x = 1$ di mana $g(1) = c - 3$, sehingga $c - 3 \le 18 \implies c \le 21$, lalu salah hitung menjadi 15.</sub>
- **C. 13** ✅  
  <sub>Benar: Nilai maksimum $g(x)$ pada $[1, 5]$ terjadi di $x = 5$, bernilai $5^2 - 4(5) + c = 5 + c$. Agar $R_g \subseteq D_f = (-\infty, 18]$, maka $\max(g(x)) \le 18 \implies 5 + c \le 18 \implies c \le 13$. Jadi batas nilai maksimum dari $c$ adalah 13.</sub>
- D. 18  
  <sub>Salah: Hanya menyamakan nilai batas fungsi luar $c = 18$ tanpa memperhitungkan nilai fungsi dalam $g(x)$.</sub>

**Pembahasan:** Langkah 1: Tentukan domain dari $f(x)$. Agar $f(x) = \sqrt{18 - x}$ terdefinisi, disyaratkan $18 - x \ge 0 \implies x \le 18$. Jadi $D_f = (-\infty, 18]$.
Langkah 2: Tentukan sifat fungsi $g(x) = (x - 2)^2 + c - 4$ pada interval tertutup $[1, 5]$. Titik puncak parabola berada pada $x = 2 \in [1, 5]$.
Langkah 3: Evaluasi nilai $g(x)$ pada titik puncak dan batas interval:
- $g(2) = (2 - 2)^2 + c - 4 = c - 4$ (nilai minimum)
- $g(1) = (1 - 2)^2 + c - 4 = c - 3$
- $g(5) = (5 - 2)^2 + c - 4 = 9 + c - 4 = c + 5$ (nilai maksimum)
Daerah hasil $g$ adalah $R_g = [c - 4, c + 5]$.
Langkah 4: Agar $(f \circ g)(x)$ terdefinisi untuk setiap $x \in D_g$, disyaratkan $R_g \subseteq D_f$. Artinya, seluruh nilai dalam $R_g$ harus $\le 18$, yang berarti nilai maksimumnya harus memenuhi:
$\max(g(x)) \le 18 \implies c + 5 \le 18 \implies c \le 13$.
Langkah 5: Jadi, nilai maksimum dari konstanta $c$ adalah 13.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas11-b01-b-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: analisis_parameter_asosiatif*

Diketahui tiga fungsi real $f(x) = 2x - 5$, $g(x) = 4x + 1$, dan $h(x) = px - 3$ dengan $p$ konstanta positif. Jika fungsi komposisi $((f \circ g) \circ h)(x) = 48x - 27$, maka nilai dari $((g \circ h) \circ f)(3)$ adalah ....

- A. 9  
  <sub>Salah: Lupa menambahkan konstanta $+1$ pada perhitungan akhir fungsi $g(x)$.</sub>
- **B. 13** ✅  
  <sub>Benar: $f(g(x)) = 2(4x+1) - 5 = 8x - 3$. Komposisi dengan $h(x)$: $8(px - 3) - 3 = 8px - 27$. Karena $8px - 27 = 48x - 27$, diperoleh $8p = 48 \implies p = 6$. Untuk $((g \circ h) \circ f)(3)$, hitung $f(3) = 2(3) - 5 = 1$. Lalu $h(1) = 6(1) - 3 = 3$. Akhirnya $g(3) = 4(3) + 1 = 13$.</sub>
- C. 49  
  <sub>Salah: Langsung mensubstitusikan $x = 3$ ke rumus persamaan pertama $48(3) - 27$ kemudian salah operasi.</sub>
- D. 21  
  <sub>Salah: Tertukar menghitung $g(f(h(3)))$ atau salah mensubstitusikan $f(3) = 1$ menjadi $f(3) = 2$.</sub>

**Pembahasan:** Langkah 1: Tentukan $(f \circ g)(x) = f(g(x)) = 2(4x + 1) - 5 = 8x + 2 - 5 = 8x - 3$.
Langkah 2: Komposisikan dengan $h(x)$:
$((f \circ g) \circ h)(x) = 8(h(x)) - 3 = 8(px - 3) - 3 = 8px - 24 - 3 = 8px - 27$.
Langkah 3: Samakan dengan persamaan yang diketahui: $8px - 27 = 48x - 27 \implies 8p = 48 \implies p = 6$.
Jadi fungsi $h(x) = 6x - 3$.
Langkah 4: Hitung nilai $((g \circ h) \circ f)(3)$ secara bertahap memanfaatkan kesetaraan asosiatif $g(h(f(3)))$:
- $f(3) = 2(3) - 5 = 1$.
- $h(f(3)) = h(1) = 6(1) - 3 = 3$.
- $g(h(f(3))) = g(3) = 4(3) + 1 = 13$.
Langkah 5: Diperoleh hasil akhir 13.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas11-b01-b-hard-bt01-017
*orisinal | C6 | 5 langkah | jenis: evaluasi_optimasi_skema_diskon*

Sebuah pusat perbelanjaan menyediakan dua kupon promo belanja untuk pembelian barang dengan harga awal minimal Rp100.000,00:
- **Kupon Merah**: Diskon 15% dari total belanja, kemudian dilanjutkan potongan harga langsung sebesar Rp30.000,00.
- **Kupon Biru**: Potongan harga langsung sebesar Rp10.000,00, kemudian dilanjutkan diskon 25% dari sisa belanja.

Seorang pembeli ingin membeli sebuah barang dengan harga $x$ rupiah. Agar penggunaan **Kupon Biru** menghasilkan harga bayar akhir yang lebih murah daripada **Kupon Merah**, batas nilai harga awal $x$ yang memenuhi adalah ....

- A. $x > \text{Rp}375.000,00$  
  <sub>Salah: Salah melakukan pengurangan $30.000 + 7.500 = 37.500$ pada ruas pertidaksamaan.</sub>
- B. $x < \text{Rp}225.000,00$  
  <sub>Salah: Terbalik dalam menyusun pertidaksamaan Kupon Biru lebih murah.</sub>
- C. $x > \text{Rp}200.000,00$  
  <sub>Salah: Lupa mendiskon potongan langsung Rp10.000 pada Kupon Biru (hanya menghitung selisih potongan Rp30.000 - Rp10.000 = Rp20.000 dibagi 0,10).</sub>
- **D. $x > \text{Rp}225.000,00$** ✅  
  <sub>Benar: Model Kupon Merah: $M(x) = 0{,}85x - 30.000$. Model Kupon Biru: $B(x) = 0{,}75(x - 10.000) = 0{,}75x - 7.500$. Syarat Kupon Biru lebih murah: $B(x) < M(x) \implies 0{,}75x - 7.500 < 0{,}85x - 30.000 \implies 22.500 < 0{,}10x \implies x > 225.000$.</sub>

**Pembahasan:** Langkah 1: Definisikan fungsi untuk masing-masing skema kupon:
- Misal $x$ adalah harga awal barang dalam rupiah ($x \ge 100.000$).
- Kupon Merah terdiri dari fungsi diskon $d_1(x) = 0{,}85x$ dan potongan langsung $p_1(y) = y - 30.000$. Fungsi akhirnya: $M(x) = (p_1 \circ d_1)(x) = 0{,}85x - 30.000$.
- Kupon Biru terdiri dari fungsi potongan langsung $p_2(x) = x - 10.000$ dan fungsi diskon $d_2(y) = 0{,}75y$. Fungsi akhirnya: $B(x) = (d_2 \circ p_2)(x) = 0{,}75(x - 10.000) = 0{,}75x - 7.500$.
Langkah 2: Susun pertidaksamaan agar Kupon Biru lebih murah daripada Kupon Merah:
$B(x) < M(x)$.
Langkah 3: Substitusikan model fungsi:
$0{,}75x - 7.500 < 0{,}85x - 30.000$.
Langkah 4: Selesaikan pertidaksamaan linear:
$30.000 - 7.500 < 0{,}85x - 0{,}75x$
$22.500 < 0{,}10x$
$x > \frac{22.500}{0{,}10} \implies x > 225.000$.
Langkah 5: Jadi, Kupon Biru lebih murah apabila harga awal barang $x > \text{Rp}225.000,00$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas11-b01-b-hard-bt01-018
*variasi (angka) | C5 | 4 langkah | jenis: optimasi_anggaran_komposisi*

Jumlah kertas yang diperlukan untuk mencetak $x$ eksemplar buletin bulanan dinyatakan oleh fungsi $k(x) = 300(x + 2)$ lembar. Biaya percetakan untuk $k$ lembar kertas memenuhi rumus $b(k) = 150k + 50.000$ (dalam rupiah). Selain biaya percetakan, panitia mengalokasikan biaya konsumsi dan distribusi sebesar Rp5.000,00 untuk setiap eksemplar buletin yang berhasil dicetak. Jika total anggaran yang tersedia adalah Rp10.400.000,00, banyak eksemplar buletin maksimum yang dapat dicetak adalah ....

- **A. 205** ✅  
  <sub>Benar: Fungsi biaya percetakan adalah $(b \circ k)(x) = 150(300(x + 2)) + 50.000 = 45.000x + 140.000$. Biaya total mencakup distribusi: $T(x) = 45.000x + 140.000 + 5.000x = 50.000x + 140.000$. Agar $T(x) \le 10.400.000$, maka $50.000x \le 10.260.000 \iff x \le 205,2$. Karena $x$ bilangan bulat, nilai maksimumnya adalah 205 eksemplar.</sub>
- B. 208  
  <sub>Salah: Siswa lupa memperhitungkan konstanta pergeseran lembar kertas $(x + 2)$, sehingga memakai $45.000x + 50.000$.</sub>
- C. 226  
  <sub>Salah: Siswa lupa memperhitungkan biaya distribusi Rp5.000,00 per eksemplar, sehingga menghitung $45.000x + 140.000 \le 10.400.000 \iff x \le 228$ atau membagi langsung tanpa biaya tetap.</sub>
- D. 206  
  <sub>Salah: Siswa melakukan pembulatan ke atas dari 205,2 menjadi 206, yang mengakibatkan pengeluaran melampaui anggaran.</sub>

**Pembahasan:** Langkah 1: Menentukan rumus biaya percetakan melalui komposisi fungsi.
$(b \circ k)(x) = b(k(x)) = 150(300(x + 2)) + 50.000$
$(b \circ k)(x) = 45.000(x + 2) + 50.000 = 45.000x + 90.000 + 50.000 = 45.000x + 140.000$.

Langkah 2: Menyusun fungsi total pengeluaran $T(x)$.
Total pengeluaran mencakup biaya cetak ditambah biaya distribusi sebesar Rp5.000,00 per eksemplar:
$T(x) = (45.000x + 140.000) + 5.000x = 50.000x + 140.000$.

Langkah 3: Menerapkan syarat anggaran.
Total pengeluaran tidak boleh melebihi anggaran yang tersedia:
$50.000x + 140.000 \le 10.400.000$
$50.000x \le 10.400.000 - 140.000$
$50.000x \le 10.260.000$
$x \le \frac{10.260.000}{50.000} = 205,2$.

Langkah 4: Menentukan jumlah eksemplar maksimum.
Karena banyak eksemplar buletin harus berupa bilangan bulat, nilai bulat terbesar yang memenuhi $x \le 205,2$ adalah $x = 205$.

Jadi, banyak eksemplar buletin maksimum yang dapat dicetak adalah 205.
**Acuan:** siswa — siswa hal.47 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas11-b01-b-hard-bt01-019
*orisinal | C5 | 4 langkah | jenis: syarat_eksistensi_komposisi_interval*

Diketahui dua fungsi real $f(x) = \sqrt{x - 3}$ dan $g(x) = x^2 - 6x + c$ dengan daerah asal fungsi $g$ dibatasi pada interval $D_g = \{x \in \mathbb{R} \mid 2 \le x \le 5\}$. Berdasarkan syarat komposisi fungsi, agar fungsi komposisi $(f \circ g)(x)$ terdefinisi untuk setiap $x \in D_g$, nilai minimum dari konstanta $c$ adalah ....

- A. 3  
  <sub>Salah: Siswa langsung menyamakan konstanta $c$ dengan batas syarat akar tanpa menganalisis nilai ekstrem dari fungsi kuadrat $g(x)$.</sub>
- B. 8  
  <sub>Salah: Siswa menghitung nilai fungsi pada batas interval ujung $x = 5$ yaitu $g(5) = c - 5 \ge 3 \implies c \ge 8$, padahal titik puncak $x = 3$ memberikan nilai yang lebih kecil.</sub>
- C. 11  
  <sub>Salah: Siswa menghitung nilai fungsi pada ujung interval $x = 2$ yaitu $g(2) = c - 8 \ge 3 \implies c \ge 11$, bukan di titik puncak parabola.</sub>
- **D. 12** ✅  
  <sub>Benar: Agar terdefinisi pada bilangan real, daerah asal fungsi $f$ adalah $D_f = [3, \infty)$. Syarat $(f \circ g)(x)$ terdefinisi pada seluruh $x \in [2, 5]$ adalah daerah hasil $g$ pada interval tersebut termuat dalam $D_f$, yang berarti nilai minimum $g(x)$ pada interval $[2, 5]$ harus $\ge 3$. Fungsi kuadrat $g(x) = (x - 3)^2 + c - 9$ memiliki titik puncak di $x = 3 \in [2, 5]$, sehingga nilai minimumnya adalah $g(3) = c - 9$. Syarat $c - 9 \ge 3 \iff c \ge 12$. Jadi nilai minimum $c$ adalah 12.</sub>

**Pembahasan:** Langkah 1: Menentukan daerah asal (domain) fungsi luar $f(x)$.
Fungsi $f(x) = \sqrt{x - 3}$ terdefinisi pada bilangan real jika radikan tak negatif:
$x - 3 \ge 0 \iff x \ge 3$.
Jadi, $D_f = [3, \infty)$.

Langkah 2: Menerapkan syarat komposisi fungsi.
Fungsi komposisi $(f \circ g)(x)$ terdefinisi untuk seluruh $x \in D_g$ jika dan hanya jika seluruh nilai keluaran $g(x)$ untuk $x \in [2, 5]$ termuat di dalam $D_f$, yaitu:
$g(x) \ge 3$ untuk setiap $x \in [2, 5]$.
Hal ini setara dengan mensyaratkan nilai minimum dari $g(x)$ pada interval $[2, 5]$ bernilai $\ge 3$.

Langkah 3: Menentukan nilai minimum fungsi $g(x)$ pada interval $[2, 5]$.
Bentuk kuadrat sempurna dari $g(x)$ adalah:
$g(x) = x^2 - 6x + c = (x - 3)^2 + c - 9$.
Titik puncak parabola berada pada absis $x = 3$.
Karena $x = 3$ berada di dalam interval tertutup $[2, 5]$, maka nilai minimum $g(x)$ pada interval tersebut terjadi di $x = 3$:
$g_{\text{min}} = g(3) = (3 - 3)^2 + c - 9 = c - 9$.

Langkah 4: Menyelesaikan pertidaksamaan parameter $c$.
Agar $g(x) \ge 3$, maka nilai minimumnya harus memenuhi:
$c - 9 \ge 3 \iff c \ge 12$.

Dengan demikian, nilai minimum dari konstanta $c$ adalah 12.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas11-b01-b-hard-bt01-020
*variasi (angka) | C5 | 5 langkah | jenis: evaluasi_range_komposisi_kuadrat*

Diketahui dua fungsi real $f(x) = \frac{1}{5x - 4}$ dan $g(x) = 6x^2 + 8$. Daerah hasil (range) dari fungsi komposisi $(g \circ f)(x)$ untuk seluruh daerah asalnya adalah ....

- A. $\{y \in \mathbb{R} \mid y \ge 8\}$  
  <sub>Salah: Siswa menganggap $(f(x))^2 \ge 0$ tanpa menyadari bahwa nilai pecahan pembilang satu tidak pernah menghasilkan nilai nol.</sub>
- B. $\{y \in \mathbb{R} \mid y > 0\}$  
  <sub>Salah: Siswa hanya meninjau sifat positif dari bentuk kuadrat tanpa memperhitungkan pergeseran konstanta positif delapan pada fungsi g.</sub>
- C. $\{y \in \mathbb{R} \mid y \neq 8\}$  
  <sub>Salah: Siswa keliru menganggap delapan sebagai asimtot biasa yang nilainya boleh di bawah delapan, mengabaikan ketidaksamaan kuadratik.</sub>
- **D. $\{y \in \mathbb{R} \mid y > 8\}$** ✅  
  <sub>Benar: Karena $f(x) \neq 0$ untuk setiap $x \neq \frac{4}{5}$, maka $(f(x))^2 > 0$, yang menghasilkan $(g \circ f)(x) = 6(f(x))^2 + 8 > 8$.</sub>

**Pembahasan:** Langkah penyelesaian:
1. Tentukan domain dari $f(x)$: $D_f = \{x \in \mathbb{R} \mid 5x - 4 \neq 0\} = \{x \in \mathbb{R} \mid x \neq \frac{4}{5}\}$.
2. Tentukan range dari $f(x)$: karena pembilang bernilai 1 (konstan tak nol), maka tidak ada nilai $x$ yang membuat $f(x) = 0$. Jadi, $R_f = \{u \in \mathbb{R} \mid u \neq 0\}$.
3. Bentuk rumus fungsi komposisi:
$$(g \circ f)(x) = g(f(x)) = 6(f(x))^2 + 8 = 6\left(\frac{1}{5x - 4}\right)^2 + 8$$
4. Analisis nilai untuk $u = f(x) \neq 0$:
Karena $u \neq 0$, maka $u^2 > 0$ untuk setiap $x \in D_f$.
5. Tentukan range dari $(g \circ f)(x)$:
$$u^2 > 0 \implies 6u^2 > 0 \implies 6u^2 + 8 > 8$$
Ketika $|x| \to \infty$, nilai $u \to 0$ sehingga $6u^2 + 8 \to 8^+$. Ketika $x \to \frac{4}{5}$, nilai $u^2 \to \infty$ sehingga $6u^2 + 8 \to \infty$.
Dengan demikian, daerah hasilnya adalah $R_{g \circ f} = \{y \in \mathbb{R} \mid y > 8\}$.
**Acuan:** siswa — siswa hal.46 Latihan 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
