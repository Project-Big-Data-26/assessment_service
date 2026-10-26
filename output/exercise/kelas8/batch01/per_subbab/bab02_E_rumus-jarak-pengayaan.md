# Lembar koreksi — kelas8 SMP8-B2 subbab E: Rumus Jarak (Pengayaan)

45 soal | easy 15, medium 15, hard 15 | variasi 21, orisinal 24

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas8-b02-e-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: perhitungan jarak*

Diketahui titik $K(1, 2)$ dan titik $L(7, 10)$ pada bidang Kartesius. Jarak antara titik $K$ dan $L$ adalah ....

- A. $14$  
  <sub>Salah: Menjumlahkan selisih absis dan selisih ordinat langsung tanpa rumus Pythagoras ($(7-1)+(10-2) = 6+8 = 14$).</sub>
- B. $100$  
  <sub>Salah: Lupa menarik akar kuadrat dari hasil penjumlahan kuadrat ($6^2 + 8^2 = 100$).</sub>
- C. $\sqrt{28}$  
  <sub>Salah: Mengurangkan kuadrat selisih ordinat dengan kuadrat selisih absis ($8^2 - 6^2 = 28$).</sub>
- **D. $10$** ✅  
  <sub>Benar: $KL = \sqrt{(7-1)^2 + (10-2)^2} = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$.</sub>

**Pembahasan:** Gunakan rumus jarak antara dua titik:
$$KL = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
Substitusikan koordinat titik $K(1, 2)$ dan $L(7, 10)$:
$$KL = \sqrt{(7 - 1)^2 + (10 - 2)^2}$$
$$KL = \sqrt{6^2 + 8^2}$$
$$KL = \sqrt{36 + 64} = \sqrt{100} = 10$$
Jadi, jarak antara titik $K$ dan $L$ adalah $10$.
**Acuan:** pretest — kelas8-b02-p0110-rumus-jarak-b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas8-b02-e-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: perhitungan jarak*

Panjang ruas garis yang menghubungkan titik $P(5, 1)$ dan $Q(9, 4)$ adalah ....

- A. $7$  
  <sub>Salah: Menjumlahkan selisih absis dan ordinat secara langsung ($(9-5)+(4-1) = 4+3 = 7$).</sub>
- B. $25$  
  <sub>Salah: Lupa menarik akar kuadrat dari $4^2 + 3^2 = 25$.</sub>
- **C. $5$** ✅  
  <sub>Benar: $PQ = \sqrt{(9-5)^2 + (4-1)^2} = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5$.</sub>
- D. $\sqrt{7}$  
  <sub>Salah: Mengurangkan kuadrat selisih komponen ($4^2 - 3^2 = 7$) lalu menarik akar.</sub>

**Pembahasan:** Gunakan rumus jarak dua titik:
$$PQ = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
Substitusikan titik $P(5, 1)$ dan $Q(9, 4)$:
$$PQ = \sqrt{(9 - 5)^2 + (4 - 1)^2}$$
$$PQ = \sqrt{4^2 + 3^2}$$
$$PQ = \sqrt{16 + 9} = \sqrt{25} = 5$$
Jadi, panjang ruas garis $PQ$ adalah $5$.
**Acuan:** pretest — kelas8-b02-p0110-rumus-jarak-b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas8-b02-e-easy-bt01-003
*variasi (konteks) | C2 | 1 langkah | jenis: sifat rumus jarak*

Budi menghitung jarak antara titik $M(2, 5)$ dan $N(8, 13)$ menggunakan rumus $\sqrt{(x_N - x_M)^2 + (y_N - y_M)^2}$, sedangkan Siti menghitungnya dengan rumus $\sqrt{(x_M - x_N)^2 + (y_M - y_N)^2}$. Kesimpulan yang tepat mengenai hasil perhitungan keduanya adalah ....

- A. hasil Siti lebih kecil karena koordinat titik awal dikurangkan dengan koordinat titik yang lebih besar  
  <sub>Salah: Mengabaikan efek operasi pengkuadratan pada bilangan negatif.</sub>
- B. hasilnya berbeda tanda karena urutan pengurangan koordinat dibalik  
  <sub>Salah: Mengira tanda negatif tetap bertahan di luar hasil pengkuadratan.</sub>
- C. jarak tidak dapat ditentukan karena urutan titik harus selalu dari kiri ke kanan  
  <sub>Salah: Mengira arah penentuan titik berpengaruh pada nilai jarak geometris.</sub>
- **D. hasilnya sama karena bilangan negatif jika dikuadratkan menghasilkan bilangan positif yang sama** ✅  
  <sub>Benar: Pengkuadratan selisih $(x_1 - x_2)^2 = (x_2 - x_1)^2$ selalu menghasilkan nilai yang identik.</sub>

**Pembahasan:** Dalam rumus jarak dua titik, komponen yang dihitung adalah $(x_2 - x_1)^2$ dan $(y_2 - y_1)^2$.
Karena sifat aljabar $(a - b)^2 = (b - a)^2$, pertukaran titik awal dan titik akhir menghasilkan bilangan berlawanan tanda yang nilai kuadratnya tetap sama.
Oleh karena itu, hasil perhitungan Budi dan Siti pasti sama.
**Acuan:** siswa — siswa hal.111 Soal Laihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas8-b02-e-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: identifikasi rumus*

Berdasarkan Teorema Pythagoras, rumus yang benar untuk menentukan jarak $d$ antara dua titik $A(x_1, y_1)$ dan $B(x_2, y_2)$ pada bidang koordinat adalah ....

- A. $d = \sqrt{(x_2 - x_1)^2 - (y_2 - y_1)^2}$  
  <sub>Salah: Salah menggunakan tanda pengurangan antarkomponen kuadrat.</sub>
- B. $d = (x_2 - x_1)^2 + (y_2 - y_1)^2$  
  <sub>Salah: Lupa menarik akar kuadrat pada sisi miring.</sub>
- **C. $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$** ✅  
  <sub>Benar: Rumus jarak diturunkan dari $AB^2 = AC^2 + BC^2$ sehingga $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.</sub>
- D. $d = \sqrt{(x_2 + x_1)^2 + (y_2 + y_1)^2}$  
  <sub>Salah: Menjumlahkan koordinat alih-alih mencari selisih jarak antartitik.</sub>

**Pembahasan:** Segitiga yang terbentuk dari dua titik sembarang pada bidang Kartesius adalah segitiga siku-siku dengan panjang sisi mendatar $|x_2 - x_1|$ dan sisi tegak $|y_2 - y_1|$.
Berdasarkan Teorema Pythagoras:
$$d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$$
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
Jadi, rumus yang benar adalah $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas8-b02-e-easy-bt01-005
*orisinal | C1 | 1 langkah | jenis: panjang ruas garis horizontal*

Diketahui titik $A(3, 4)$ dan titik $C(9, 4)$ terletak pada bidang koordinat. Panjang ruas garis horizontal $AC$ adalah ....

- **A. $6$** ✅  
  <sub>Benar: Karena nilai ordinat sama ($y = 4$), panjang ruas horizontal adalah $x_2 - x_1 = 9 - 3 = 6$.</sub>
- B. $12$  
  <sub>Salah: Menjumlahkan kedua nilai absis ($9 + 3 = 12$).</sub>
- C. $8$  
  <sub>Salah: Menjumlahkan kedua nilai ordinat ($4 + 4 = 8$).</sub>
- D. $5$  
  <sub>Salah: Salah menghitung selisih $9 - 4 = 5$.</sub>

**Pembahasan:** Ruas garis yang menghubungkan dua titik dengan nilai ordinat sama ($y_1 = y_2 = 4$) adalah ruas garis horizontal.
Panjangnya dihitung langsung dari selisih absisnya:
$$AC = x_2 - x_1 = 9 - 3 = 6$$
Jadi, panjang ruas garis $AC$ adalah $6$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas8-b02-e-easy-bt01-006
*variasi (konteks) | C2 | 1 langkah | jenis: jarak titik pada koordinat negatif*

Jarak antara titik $P(-4, -6)$ dan titik $Q(-4, 2)$ pada bidang Kartesius adalah ....

- A. $4$ satuan  
  <sub>Salah: Siswa salah menghitung operasi bilangan negatif: $2 - 6 = -4$ lalu dimutlakkan menjadi $4$.</sub>
- **B. $8$ satuan** ✅  
  <sub>Benar: Kedua titik memiliki absis yang sama ($x = -4$), sehingga jaraknya adalah $|y_2 - y_1| = |2 - (-6)| = 8$.</sub>
- C. $10$ satuan  
  <sub>Salah: Siswa salah menjumlahkan nilai mutlak koordinat $x$ dan $y$: $4 + 6 = 10$.</sub>
- D. $-8$ satuan  
  <sub>Salah: Siswa menghitung $-6 - 2 = -8$ dan lupa bahwa jarak selalu bernilai non-negatif.</sub>

**Pembahasan:** Karena absis kedua titik bernilai sama yaitu $x = -4$, ruas garis $PQ$ sejajar dengan sumbu $Y$.
Jarak antara titik $P$ dan $Q$ adalah:
$d = |y_2 - y_1| = |2 - (-6)| = |2 + 6| = 8$ satuan.
**Acuan:** siswa — siswa hal.110 Pengayaan

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas8-b02-e-easy-bt01-007
*variasi (konteks) | C1 | 1 langkah | jenis: dasar penurunan rumus jarak*

Rumus jarak antara dua titik $A(x_1, y_1)$ dan $B(x_2, y_2)$ diturunkan dari Teorema Pythagoras karena ....

- A. panjang ruas garis $AB$ selalu sama dengan jumlah kuadrat dari absis dan ordinat titik awal  
  <sub>Salah: Siswa salah memahami konsep dengan mengira koordinat langsung dikuadratkan tanpa mencari selisihnya terlebih dahulu.</sub>
- B. titik asal $(0, 0)$ selalu menjadi salah satu sudut siku-siku pada bidang Kartesius  
  <sub>Salah: Siswa salah mengira segitiga siku-siku yang terbentuk harus selalu berpangkal di titik pusat $(0, 0)$.</sub>
- **C. ruas garis horizontal $(x_2 - x_1)$ dan ruas garis vertikal $(y_2 - y_1)$ saling tegak lurus sehingga ruas garis $AB$ merupakan hipotenusa** ✅  
  <sub>Benar: Sumbu X dan sumbu Y saling tegak lurus, membuat segitiga pembantu yang dibentuk selisih absis dan selisih ordinat menjadi segitiga siku-siku dengan sisi miring $AB$.</sub>
- D. setiap garis lurus pada bidang Kartesius selalu memotong sumbu koordinat dengan sudut $90^\circ$  
  <sub>Salah: Siswa keliru menganggap semua garis lurus tegak lurus terhadap sumbu koordinat.</sub>

**Pembahasan:** Pada bidang Kartesius, sumbu koordinat $X$ dan $Y$ saling tegak lurus. Selisih absis $(x_2 - x_1)$ membentuk sisi horizontal dan selisih ordinat $(y_2 - y_1)$ membentuk sisi vertikal. Kedua sisi ini saling tegak lurus membentuk segitiga siku-siku, sehingga jarak $AB$ adalah panjang hipotenusa yang dihitung menggunakan Teorema Pythagoras: $AB = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.
**Acuan:** siswa — siswa hal.110 Pengayaan

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas8-b02-e-easy-bt01-008
*orisinal | C2 | 1 langkah | jenis: panjang ruas garis vertikal*

Diketahui titik $B(5, 9)$ dan $C(5, 2)$ terletak pada bidang koordinat Cartesius. Panjang ruas garis vertikal $BC$ adalah ....

- A. $\sqrt{7}$ satuan  
  <sub>Salah: Siswa menarik akar dari hasil selisih ordinat karena terbiasa dengan tanda akar pada rumus jarak.</sub>
- **B. $7$ satuan** ✅  
  <sub>Benar: Panjang sisi vertikal adalah $y_2 - y_1 = 9 - 2 = 7$.</sub>
- C. $5$ satuan  
  <sub>Salah: Siswa terkecoh menggunakan nilai absis $x = 5$ sebagai panjang ruas garis.</sub>
- D. $11$ satuan  
  <sub>Salah: Siswa menjumlahkan ordinat: $9 + 2 = 11$.</sub>

**Pembahasan:** Berdasarkan materi Buku Siswa, panjang sisi vertikal $BC$ pada segitiga siku-siku dengan absis sama dirumuskan dengan selisih ordinatnya:
$BC = y_2 - y_1 = 9 - 2 = 7$ satuan.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas8-b02-e-easy-bt01-009
*orisinal | C2 | 1 langkah | jenis: koordinat titik sudut siku-siku*

Titik $A(2, 3)$ dan $B(8, 11)$ membentuk hipotenusa dari segitiga siku-siku $ABC$ yang sisi-sisinya sejajar sumbu koordinat. Jika titik sudut siku-siku $C$ memiliki absis yang sama dengan titik $B$ dan ordinat yang sama dengan titik $A$, maka koordinat titik $C$ adalah ....

- A. $(6, 8)$  
  <sub>Salah: Siswa menghitung selisih koordinat $8 - 2 = 6$ dan $11 - 3 = 8$ lalu menjadikannya titik koordinat.</sub>
- B. $(5, 7)$  
  <sub>Salah: Siswa menghitung titik tengah antara titik $A$ dan titik $B$.</sub>
- C. $(2, 11)$  
  <sub>Salah: Siswa menukar posisi koordinat menjadi $(x_1, y_2)$.</sub>
- **D. $(8, 3)$** ✅  
  <sub>Benar: Sesuai rumus pembentukan segitiga siku-siku pembantu, koordinat $C$ adalah $(x_2, y_1) = (8, 3)$.</sub>

**Pembahasan:** Dalam penurunan rumus jarak pada Buku Siswa, segitiga siku-siku pembantu $ABC$ memiliki titik sudut siku-siku $C(x_2, y_1)$.
Dengan $A(x_1, y_1) = A(2, 3)$ dan $B(x_2, y_2) = B(8, 11)$, maka:
$x_C = x_B = 8$
$y_C = y_A = 3$
Sehingga koordinat titik $C$ adalah $(8, 3)$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas8-b02-e-easy-bt01-010
*variasi (angka) | C2 | 1 langkah | jenis: sifat urutan titik rumus jarak*

Dina menghitung jarak antara titik $(1, 3)$ dan $(9, 15)$ dengan menetapkan $(1, 3)$ sebagai $(x_1, y_1)$. Fajar menghitung jarak kedua titik tersebut dengan menetapkan $(9, 15)$ sebagai $(x_1, y_1)$. Kesimpulan yang benar mengenai hasil perhitungan keduanya adalah ....

- **A. hasilnya sama karena $(x_2 - x_1)^2 = (x_1 - x_2)^2$** ✅  
  <sub>Benar: Pengkuadratan bilangan yang berlawanan tanda menghasilkan bilangan yang sama besar.</sub>
- B. hasil perhitungan Dina lebih kecil dari hasil Fajar  
  <sub>Salah: Siswa mengira titik dengan koordinat lebih kecil selalu menghasilkan jarak yang lebih kecil.</sub>
- C. hasil perhitungan Fajar bernilai negatif dari hasil Dina  
  <sub>Salah: Siswa mengira tanda minus di dalam kurung tidak hilang setelah dikuadratkan.</sub>
- D. kedua hasil berbeda karena urutan absis tidak boleh ditukar  
  <sub>Salah: Siswa mengira urutan titik dalam rumus jarak tidak bersifat komutatif terhadap hasil akhir.</sub>

**Pembahasan:** Pada rumus jarak $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$, nilai $(x_2 - x_1)^2 = (x_1 - x_2)^2$ dan $(y_2 - y_1)^2 = (y_1 - y_2)^2$. Karena pengkuadratan bilangan negatif maupun positif menghasilkan nilai positif yang sama, pemilihan urutan titik tidak mengubah hasil akhir jarak.
**Acuan:** siswa — siswa hal.111 Soal Laihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas8-b02-e-easy-bt01-011
*variasi (konteks) | C2 | 1 langkah | jenis: keberlakuan koordinat bertanda*

Apakah rumus jarak dua titik $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ tetap berlaku jika kedua titik berada di kuadran III (semua koordinat bernilai negatif)?

- **A. Ya, rumus tetap berlaku karena hasil pengkuadratan selisih koordinat selalu menghasilkan bilangan tak-negatif.** ✅  
  <sub>Benar: Kuadrat bilangan riil selalu $\ge 0$ sehingga teorema Pythagoras selalu menghasilkan jarak bernilai positif yang valid.</sub>
- B. Tidak, karena panjang sisi segitiga tidak boleh dihitung dari koordinat bernilai negatif.  
  <sub>Salah: Siswa salah memahami bahwa koordinat negatif dianggap menghasilkan panjang sisi bernilai negatif.</sub>
- C. Ya, tetapi tanda penjumlahan di dalam akar harus diubah menjadi tanda pengurangan.  
  <sub>Salah: Siswa mengira tanda koordinat negatif mengubah operasi penjumlahan kuadrat sisi.</sub>
- D. Tidak, tanda akar pada rumus harus diganti dengan nilai mutlak tanpa pengkuadratan.  
  <sub>Salah: Siswa mengira konsep nilai mutlak menggantikan Teorema Pythagoras untuk koordinat negatif.</sub>

**Pembahasan:** Rumus jarak diturunkan dari Teorema Pythagoras. Walaupun koordinat bernilai negatif, selisih koordinat merepresentasikan panjang sisi segitiga siku-siku pada bidang Cartesius. Saat dikuadratkan, nilainya selalu positif atau nol, sehingga rumus tetap berlaku penuh pada kuadran mana pun.
**Acuan:** siswa — siswa hal.110 Pertanyaan Pemantik Subbab E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas8-b02-e-easy-bt01-012
*variasi (konteks) | C1 | 1 langkah | jenis: representasi geometri rumus jarak*

Dalam penurunan rumus jarak pada bidang koordinat Cartesius, ruas garis yang menghubungkan titik $A(x_1, y_1)$ dan $B(x_2, y_2)$ berperan sebagai ....

- A. garis tinggi ke sisi miring  
  <sub>Salah: Siswa salah mengenali unsur garis pada segitiga siku-siku.</sub>
- B. sisi siku-siku horizontal  
  <sub>Salah: Siswa tertukar dengan ruas garis selisih absis $(x_2 - x_1)$.</sub>
- C. sisi siku-siku vertikal  
  <sub>Salah: Siswa tertukar dengan ruas garis selisih ordinat $(y_2 - y_1)$.</sub>
- **D. hipotenusa segitiga siku-siku** ✅  
  <sub>Benar: Ruas garis miring $AB$ merupakan sisi terpanjang di hadapan sudut siku-siku segitiga bantu $ABC$.</sub>

**Pembahasan:** Pada bidang Cartesius, jarak antara $A(x_1, y_1)$ dan $B(x_2, y_2)$ dibentuk dengan membuat titik bantu $C(x_2, y_1)$ sehingga terbentuk segitiga siku-siku $ABC$. Ruas garis $AB$ adalah sisi di depan sudut siku-siku $C$, sehingga berperan sebagai hipotenusa.
**Acuan:** siswa — siswa hal.110 Pertanyaan Pemantik Subbab E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas8-b02-e-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: jarak ke pangkal koordinat*

Jarak antara titik pangkal koordinat $O(0, 0)$ dan titik $P(6, 8)$ pada bidang Cartesius adalah ....

- A. $7$  
  <sub>Salah: Siswa menghitung rata-rata dari kedua koordinat $(6 + 8) / 2$.</sub>
- **B. $10$** ✅  
  <sub>Benar: $\sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$.</sub>
- C. $14$  
  <sub>Salah: Siswa langsung menjumlahkan koordinat $6 + 8$ tanpa menguadratkan dan menarik akar.</sub>
- D. $48$  
  <sub>Salah: Siswa mengalikan nilai absis dan ordinat $6 \times 8$.</sub>

**Pembahasan:** Jarak titik $P(x, y)$ ke titik asal $O(0, 0)$ dihitung dengan Teorema Pythagoras:
$OP = \sqrt{(6 - 0)^2 + (8 - 0)^2} = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas8-b02-e-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: panjang sisi penyiku segitiga jarak*

Segitiga siku-siku $ABC$ dibentuk untuk menghitung jarak antara titik $A(3, 2)$ dan $B(11, 8)$, dengan titik siku-siku $C(11, 2)$. Panjang sisi mendatar $AC$ adalah ....

- A. $14$ satuan  
  <sub>Salah: Siswa menjumlahkan koordinat absis $3 + 11$.</sub>
- **B. $8$ satuan** ✅  
  <sub>Benar: Panjang sisi horizontal $AC = |x_2 - x_1| = |11 - 3| = 8$.</sub>
- C. $10$ satuan  
  <sub>Salah: Siswa menghitung panjang hipotenusa $AB$ bukan sisi $AC$.</sub>
- D. $6$ satuan  
  <sub>Salah: Siswa menghitung panjang sisi vertikal $BC = 8 - 2$ bukan sisi horizontal $AC$.</sub>

**Pembahasan:** Sisi mendatar $AC$ menghubungkan titik $A(3, 2)$ dan $C(11, 2)$. Karena memiliki ordinat yang sama, panjangnya adalah selisih absisnya:
$AC = 11 - 3 = 8$ satuan.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas8-b02-e-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: jarak dua titik*

Diketahui titik $A(4, 7)$ dan $B(16, 12)$ pada bidang koordinat Cartesius. Panjang ruas garis $AB$ adalah ....

- A. $17$ satuan  
  <sub>Salah: Menjumlahkan langsung selisih koordinat $12 + 5$ tanpa menguadratkan dan menarik akar.</sub>
- B. $\sqrt{119}$ satuan  
  <sub>Salah: Salah menggunakan operasi pengurangan kuadrat di dalam akar: $12^2 - 5^2 = 144 - 25 = 119$.</sub>
- **C. $13$ satuan** ✅  
  <sub>Benar: Menggunakan rumus jarak: $AB = \sqrt{(16 - 4)^2 + (12 - 7)^2} = \sqrt{12^2 + 5^2} = \sqrt{144 + 25} = \sqrt{169} = 13$ satuan.</sub>
- D. $7$ satuan  
  <sub>Salah: Mengurangkan selisih kedua sumbu: $12 - 5 = 7$.</sub>

**Pembahasan:** Berdasarkan Teorema Pythagoras, jarak antara dua titik $A(x_1, y_1)$ dan $B(x_2, y_2)$ dirumuskan sebagai:
$$AB = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
Substitusikan koordinat titik $A(4, 7)$ dan $B(16, 12)$:
$$AB = \sqrt{(16 - 4)^2 + (12 - 7)^2}$$
$$AB = \sqrt{12^2 + 5^2}$$
$$AB = \sqrt{144 + 25}$$
$$AB = \sqrt{169} = 13$$

Jadi, panjang ruas garis $AB$ adalah $13$ satuan.
**Acuan:** siswa — siswa hal.110 E. Rumus Jarak

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [medium] kelas8-b02-e-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: jarak dua objek bergerak*

Doni dan Reno berdiri saling membelakangi di titik asal $(0, 0)$. Doni berjalan $9$ langkah ke utara kemudian $12$ langkah ke timur. Pada saat bersamaan, Reno berjalan $12$ langkah ke selatan kemudian $16$ langkah ke barat. Berapakah jarak lurus antara posisi Doni dan Reno pada titik pemberhentian mereka?

- A. $28$ langkah  
  <sub>Salah: Salah menghitung nilai kuadrat selisih absis dan ordinat.</sub>
- B. $25$ langkah  
  <sub>Salah: Mengurangkan nilai mutlak koordinat kedua anak alih-alih mengurangkan koordinat bertanda.</sub>
- **C. $35$ langkah** ✅  
  <sub>Benar: Posisi Doni berada pada koordinat $(12, 9)$ dan posisi Reno berada pada koordinat $(-16, -12)$. Jarak lurus keduanya adalah $\sqrt{(12 - (-16))^2 + (9 - (-12))^2} = \sqrt{28^2 + 21^2} = \sqrt{784 + 441} = \sqrt{1225} = 35$ langkah.</sub>
- D. $49$ langkah  
  <sub>Salah: Hanya menjumlahkan semua langkah perjalanan tanpa menggunakan Teorema Pythagoras.</sub>

**Pembahasan:** Misalkan titik mula-mula adalah $(0, 0)$:
- Doni bergerak ke utara ($+y$) sejauh $9$ dan ke timur ($+x$) sejauh $12$, sehingga posisinya adalah $(12, 9)$.
- Reno bergerak ke selatan ($-y$) sejauh $12$ dan ke barat ($-x$) sejauh $16$, sehingga posisinya adalah $(-16, -12)$.

Jarak lurus kedua anak:
$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
$d = \sqrt{(12 - (-16))^2 + (9 - (-12))^2}$
$d = \sqrt{28^2 + 21^2} = \sqrt{784 + 441} = \sqrt{1225} = 35$ langkah.
**Acuan:** siswa — siswa hal.111 Soal Laihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [medium] kelas8-b02-e-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: total jarak perjalanan*

Sebuah drone pengantar bergerak dari titik pengisian daya $A(-3, -2)$ menuju ke titik penerima pertama $B(5, 4)$, kemudian melanjutkan rute ke titik penerima kedua $C(5, -1)$ pada bidang koordinat. Total jarak tempuh lintasan lurus yang dilalui drone dari $A$ ke $B$ lalu ke $C$ adalah ....

- **A. $15$ satuan** ✅  
  <sub>Benar: Jarak $AB = \sqrt{(5 - (-3))^2 + (4 - (-2))^2} = \sqrt{8^2 + 6^2} = 10$. Jarak $BC = \sqrt{(5 - 5)^2 + (-1 - 4)^2} = \sqrt{0 + (-5)^2} = 5$. Total jarak tempuh adalah $10 + 5 = 15$ satuan.</sub>
- B. $19$ satuan  
  <sub>Salah: Menjumlahkan langsung seluruh selisih koordinat mendatar dan vertikal tanpa menarik akar kuadrat.</sub>
- C. $10$ satuan  
  <sub>Salah: Hanya menghitung jarak segmen pertama dari titik $A$ ke $B$.</sub>
- D. $13$ satuan  
  <sub>Salah: Keliru menggunakan nilai acuan tripel Pythagoras tanpa menghitung selisih koordinat sebenarnya.</sub>

**Pembahasan:** Hitung panjang masing-masing lintasan:
1. Jarak $A(-3, -2)$ ke $B(5, 4)$:
   $AB = \sqrt{(5 - (-3))^2 + (4 - (-2))^2} = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10$ satuan.
2. Jarak $B(5, 4)$ ke $C(5, -1)$:
   $BC = \sqrt{(5 - 5)^2 + (-1 - 4)^2} = \sqrt{0^2 + (-5)^2} = \sqrt{25} = 5$ satuan.

Total jarak yang ditempuh drone:
$\text{Total} = AB + BC = 10 + 5 = 15$ satuan.
**Acuan:** pretest — kelas8-b02-p0110-rumus-jarak-b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [medium] kelas8-b02-e-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: menentukan koordinat titik*

Diketahui jarak antara titik $A(2, -1)$ dan titik $B(x, 7)$ pada bidang koordinat Cartesius adalah $10$ satuan panjang. Jika $x$ merupakan bilangan bulat positif, berapakah nilai $x$?

- A. $6$  
  <sub>Salah: Menganggap nilai $x$ sama dengan hasil akar dari $36$ tanpa menambahkan absis titik $A$.</sub>
- B. $4$  
  <sub>Salah: Memilih penyelesaian $x - 2 = -6$ sehingga didapat $x = -4$ lalu mengabaikan tanda negatifnya.</sub>
- C. $10$  
  <sub>Salah: Salah menjumlahkan konstanta pada langkah aljabar terakhir.</sub>
- **D. $8$** ✅  
  <sub>Benar: Menggunakan rumus jarak: $(x - 2)^2 + (7 - (-1))^2 = 10^2 \iff (x - 2)^2 + 64 = 100 \iff (x - 2)^2 = 36$. Karena $x > 0$, maka $x - 2 = 6 \iff x = 8$.</sub>

**Pembahasan:** Gunakan rumus jarak antara dua titik:
$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
$10 = \sqrt{(x - 2)^2 + (7 - (-1))^2}$

Kuadratkan kedua ruas:
$100 = (x - 2)^2 + 8^2$
$100 = (x - 2)^2 + 64$
$(x - 2)^2 = 36$

Maka:
$x - 2 = 6$ atau $x - 2 = -6$
$x = 8$ atau $x = -4$

Karena disyaratkan $x$ merupakan bilangan bulat positif, maka nilai $x = 8$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [medium] kelas8-b02-e-medium-bt01-004
*orisinal | C3 | 3 langkah | jenis: keliling bangun datar*

Titik-titik sudut segitiga $PQR$ pada bidang Cartesius adalah $P(-2, 1)$, $Q(6, 1)$, dan $R(2, 4)$. Keliling segitiga $PQR$ tersebut adalah ....

- A. $16$ satuan  
  <sub>Salah: Salah menghitung panjang sisi alas mendatar menjadi $6$ satuan.</sub>
- **B. $18$ satuan** ✅  
  <sub>Benar: Sisi $PQ = |6 - (-2)| = 8$ satuan. Sisi $PR = \sqrt{(2 - (-2))^2 + (4 - 1)^2} = \sqrt{4^2 + 3^2} = 5$ satuan. Sisi $QR = \sqrt{(2 - 6)^2 + (4 - 1)^2} = \sqrt{(-4)^2 + 3^2} = 5$ satuan. Keliling $= 8 + 5 + 5 = 18$ satuan.</sub>
- C. $24$ satuan  
  <sub>Salah: Tertukar dengan perhitungan dua kali luas segitiga.</sub>
- D. $13$ satuan  
  <sub>Salah: Hanya menjumlahkan dua sisi segitiga ($PQ + QR$).</sub>

**Pembahasan:** Hitung panjang setiap sisi segitiga $PQR$:
1. Panjang $PQ$ (sisi horizontal):
   $PQ = \sqrt{(6 - (-2))^2 + (1 - 1)^2} = \sqrt{8^2 + 0} = 8$ satuan.
2. Panjang $PR$:
   $PR = \sqrt{(2 - (-2))^2 + (4 - 1)^2} = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5$ satuan.
3. Panjang $QR$:
   $QR = \sqrt{(2 - 6)^2 + (4 - 1)^2} = \sqrt{(-4)^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5$ satuan.

Keliling segitiga $PQR$:
$\text{Keliling} = PQ + PR + QR = 8 + 5 + 5 = 18$ satuan.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [medium] kelas8-b02-e-medium-bt01-005
*variasi (angka) | C4 | 3 langkah | jenis: identifikasi jenis segitiga*

Diketahui sebuah segitiga $PQR$ memiliki koordinat titik-titik sudut $P(-3, 6)$, $Q(5, 10)$, dan $R(7, 6)$. Jenis segitiga $PQR$ yang terbentuk adalah ....

- A. segitiga siku-siku di $R$  
  <sub>Salah: Siswa salah menjumlahkan kuadrat sisi sehingga mengira $PR^2 + QR^2 = PQ^2$.</sub>
- **B. segitiga siku-siku di $Q$** ✅  
  <sub>Benar: $PQ^2 = (5 - (-3))^2 + (10 - 6)^2 = 80$, $QR^2 = (7 - 5)^2 + (6 - 10)^2 = 20$, dan $PR^2 = (7 - (-3))^2 + (6 - 6)^2 = 100$. Karena $PQ^2 + QR^2 = 80 + 20 = 100 = PR^2$, segitiga tersebut siku-siku di $Q$.</sub>
- C. segitiga lancip sembarang  
  <sub>Salah: Siswa salah menghitung selisih koordinat dengan tanda negatif sehingga kuadrat sisi tidak memenuhi Teorema Pythagoras.</sub>
- D. segitiga siku-siku di $P$  
  <sub>Salah: Siswa salah menentukan sisi miring dan menduga titik sudut siku-siku berada di depan sisi $QR$.</sub>

**Pembahasan:** Hitung kuadrat panjang setiap sisi menggunakan rumus jarak:
1. $PQ^2 = (5 - (-3))^2 + (10 - 6)^2 = 8^2 + 4^2 = 64 + 16 = 80$
2. $QR^2 = (7 - 5)^2 + (6 - 10)^2 = 2^2 + (-4)^2 = 4 + 16 = 20$
3. $PR^2 = (7 - (-3))^2 + (6 - 6)^2 = 10^2 + 0^2 = 100$

Periksa Teorema Pythagoras:
$PQ^2 + QR^2 = 80 + 20 = 100 = PR^2$
Karena kuadrat sisi terpanjang sama dengan jumlah kuadrat dua sisi lainnya, maka segitiga $PQR$ adalah segitiga siku-siku dengan hipotenusa $PR$, sehingga sudut siku-siku berada di titik $Q$.
**Acuan:** pretest — kelas8-b02-p0111-soal-laihan-2-4-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas8-b02-e-medium-bt01-006
*variasi (angka) | C3 | 2 langkah | jenis: jarak dua titik*

Panjang ruas garis yang menghubungkan titik $K(-4, -7)$ dan titik $L(4, 8)$ pada bidang Cartesius adalah ....

- **A. $17$ satuan** ✅  
  <sub>Benar: $d = \sqrt{(4 - (-4))^2 + (8 - (-7))^2} = \sqrt{8^2 + 15^2} = \sqrt{64 + 225} = \sqrt{289} = 17$.</sub>
- B. $23$ satuan  
  <sub>Salah: Siswa menjumlahkan langsung selisih mendatar dan tegak $(8 + 15 = 23)$ tanpa mengakar kuadratkan.</sub>
- C. $13$ satuan  
  <sub>Salah: Siswa salah menghitung selisih koordinat negatif: $4 - (-4) = 0$ atau salah menggunakan tripel Pythagoras $5, 12, 13$.</sub>
- D. $15$ satuan  
  <sub>Salah: Siswa hanya mengambil nilai selisih koordinat $y$ tanpa melibatkan koordinat $x$.</sub>

**Pembahasan:** Gunakan rumus jarak antara dua titik:
$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
$d = \sqrt{(4 - (-4))^2 + (8 - (-7))^2}$
$d = \sqrt{(4 + 4)^2 + (8 + 7)^2}$
$d = \sqrt{8^2 + 15^2} = \sqrt{64 + 225} = \sqrt{289} = 17$
Jadi, panjang ruas garis $KL$ adalah $17$ satuan.
**Acuan:** pretest — kelas8-b02-p0110-rumus-jarak-b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas8-b02-e-medium-bt01-007
*variasi (angka) | C4 | 3 langkah | jenis: jarak perpindahan posisi*

Dika dan Fani berdiri saling membelakangi di titik asal $(0, 0)$. Dika berjalan $7\text{ meter}$ ke depan kemudian $9\text{ meter}$ ke kanan. Pada saat yang sama, Fani berjalan $5\text{ meter}$ ke depan kemudian $7\text{ meter}$ ke kanan (relatif terhadap arah hadapnya masing-masing). Jarak lurus antara Dika dan Fani pada posisi akhir adalah ....

- **A. $20\text{ meter}$** ✅  
  <sub>Benar: Posisi Dika $(9, 7)$ dan Fani $(-7, -5)$. Jarak $= \sqrt{(9 - (-7))^2 + (7 - (-5))^2} = \sqrt{16^2 + 12^2} = \sqrt{256 + 144} = \sqrt{400} = 20\text{ meter}$.</sub>
- B. $28\text{ meter}$  
  <sub>Salah: Siswa menjumlahkan total perpindahan secara skalar $(16 + 12 = 28)$.</sub>
- C. $25\text{ meter}$  
  <sub>Salah: Siswa salah menerapkan tripel Pythagoras yang mengira $12$ dan $16$ berpasangan dengan $25$.</sub>
- D. $14\text{ meter}$  
  <sub>Salah: Siswa mengurangkan posisi koordinat tanpa memperhatikan arah yang berlawanan.</sub>

**Pembahasan:** Misalkan arah hadap Dika adalah sumbu $+y$, maka kanan Dika adalah sumbu $+x$:
- Posisi akhir Dika: $(9, 7)$
Karena Fani menghadap arah berlawanan (sumbu $-y$), maka kanan Fani adalah sumbu $-x$:
- Posisi akhir Fani: $(-7, -5)$

Hitung jarak lurus kedua posisi:
$\Delta x = 9 - (-7) = 16\text{ meter}$
$\Delta y = 7 - (-5) = 12\text{ meter}$

Jarak $= \sqrt{\Delta x^2 + \Delta y^2} = \sqrt{16^2 + 12^2} = \sqrt{256 + 144} = \sqrt{400} = 20\text{ meter}$.
**Acuan:** siswa — siswa hal.111 Soal Laihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas8-b02-e-medium-bt01-008
*orisinal | C3 | 2 langkah | jenis: panjang diagonal bangun datar*

Sebuah persegi panjang $PQRS$ memiliki titik-titik sudut $P(-2, 3)$, $Q(6, 3)$, $R(6, 9)$, dan $S(-2, 9)$ pada bidang Cartesius. Panjang diagonal $PR$ dari persegi panjang tersebut adalah ....

- A. $12$ satuan  
  <sub>Salah: Siswa salah menghitung selisih koordinat $x$ menjadi $6 - (-2) = 4$ dan menjumlahkannya dengan nilai lain.</sub>
- B. $8$ satuan  
  <sub>Salah: Siswa hanya menyebutkan panjang sisi horizontal $PQ$ sebagai diagonal.</sub>
- C. $14$ satuan  
  <sub>Salah: Siswa menjumlahkan panjang sisi panjang dan sisi lebar $(8 + 6 = 14)$.</sub>
- **D. $10$ satuan** ✅  
  <sub>Benar: $PR = \sqrt{(6 - (-2))^2 + (9 - 3)^2} = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10$.</sub>

**Pembahasan:** Panjang diagonal $PR$ dihitung dari jarak titik $P(-2, 3)$ ke titik $R(6, 9)$:
$d = \sqrt{(x_R - x_P)^2 + (y_R - y_P)^2}$
$d = \sqrt{(6 - (-2))^2 + (9 - 3)^2}$
$d = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10$ satuan.
Jadi, panjang diagonal persegi panjang tersebut adalah $10$ satuan.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas8-b02-e-medium-bt01-009
*orisinal | C3 | 2 langkah | jenis: diameter lingkaran pada koordinat*

Sebuah lingkaran berpusat di titik $P(3, -2)$ dan melalui titik $Q(8, 10)$ pada bidang koordinat. Panjang diameter lingkaran tersebut adalah ....

- A. $52$ satuan  
  <sub>Salah: Siswa salah mengalikan nilai jari-jari dengan empat.</sub>
- **B. $26$ satuan** ✅  
  <sub>Benar: Jari-jari $r = \sqrt{(8 - 3)^2 + (10 - (-2))^2} = \sqrt{5^2 + 12^2} = 13$, sehingga diameter $d = 2 \times 13 = 26$ satuan.</sub>
- C. $13$ satuan  
  <sub>Salah: Siswa hanya menghitung panjang jari-jari $r$ dan lupa mengalikannya dengan dua untuk mencari diameter.</sub>
- D. $17$ satuan  
  <sub>Salah: Siswa menjumlahkan selisih komponen $x$ dan $y$ yaitu $5 + 12 = 17$.</sub>

**Pembahasan:** Langkah 1: Tentukan jari-jari lingkaran ($r$) sebagai jarak titik pusat $P(3, -2)$ ke titik $Q(8, 10)$:
$r = \sqrt{(8 - 3)^2 + (10 - (-2))^2}$
$r = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13$ satuan.

Langkah 2: Tentukan panjang diameter ($d$):
$d = 2 \times r = 2 \times 13 = 26$ satuan.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas8-b02-e-medium-bt01-010
*variasi (konteks) | C3 | 2 langkah | jenis: jangkauan sinyal dua posisi*

Dua regu penyelamat saling berkomunikasi menggunakan perangkat radio genggam yang memiliki jangkauan sinyal maksimum $25\text{ meter}$. Jika Regu A berada pada koordinat $(3, 4)$ dan Regu B berada pada koordinat $(15, 20)$ dalam satuan meter, apakah kedua regu tersebut dapat saling berkomunikasi?

- A. Tidak dapat, karena jarak kedua regu adalah $28\text{ meter}$  
  <sub>Salah: Siswa menjumlahkan selisih koordinat secara langsung tanpa rumus Pythagoras: $(15 - 3) + (20 - 4) = 12 + 16 = 28\text{ m}$.</sub>
- B. Tidak dapat, karena jarak kedua regu adalah $26\text{ meter}$  
  <sub>Salah: Siswa salah menghitung $12^2 + 16^2 = 144 + 256 = 400$ tetapi salah memperkirakan nilai akarnya atau keliru mengira lebih besar dari batas.</sub>
- C. Dapat, karena jarak kedua regu adalah $15\text{ meter}$  
  <sub>Salah: Siswa salah melakukan operasi pengurangan pada koordinat mendatar dan tegak.</sub>
- **D. Dapat, karena jarak kedua regu adalah $20\text{ meter}$** ✅  
  <sub>Benar: Jarak kedua regu dihitung dengan $\sqrt{(15 - 3)^2 + (20 - 4)^2} = \sqrt{12^2 + 16^2} = \sqrt{144 + 256} = \sqrt{400} = 20\text{ m}$. Karena $20\text{ m} \le 25\text{ m}$, sinyal radio dapat terhubung.</sub>

**Pembahasan:** Langkah 1: Hitung jarak antara Regu A $(3, 4)$ dan Regu B $(15, 20)$ menggunakan rumus jarak.
$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
$d = \sqrt{(15 - 3)^2 + (20 - 4)^2} = \sqrt{12^2 + 16^2} = \sqrt{144 + 256} = \sqrt{400} = 20\text{ meter}$

Langkah 2: Bandingkan jarak kedua regu dengan jangkauan sinyal maksimum.
Karena jarak nyata ($20\text{ meter}$) kurang dari batas jangkauan maksimum radio ($25\text{ meter}$), kedua regu dapat saling berkomunikasi.
**Acuan:** siswa — siswa hal.111 Soal Laihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas8-b02-e-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: titik berjarak sama pada sumbu koordinat*

Sebuah titik $P$ terletak pada sumbu-$X$ dan memiliki jarak yang sama terhadap titik $A(2, 5)$ dan titik $B(6, 1)$. Koordinat titik $P$ tersebut adalah ....

- **A. $(1, 0)$** ✅  
  <sub>Benar: Misalkan $P(x, 0)$. Maka $PA^2 = PB^2 \implies (x - 2)^2 + (0 - 5)^2 = (x - 6)^2 + (0 - 1)^2 \implies x^2 - 4x + 29 = x^2 - 12x + 37 \implies 8x = 8 \implies x = 1$. Jadi koordinatnya $(1, 0)$.</sub>
- B. $(2, 0)$  
  <sub>Salah: Siswa salah saat mengoperasikan suku-suku konstan sehingga memperoleh $8x = 16$.</sub>
- C. $(0, 1)$  
  <sub>Salah: Siswa tertukar antara sumbu-$X$ dan sumbu-$Y$ sehingga meletakkan nilai pada ordinat.</sub>
- D. $(4, 0)$  
  <sub>Salah: Siswa mengambil titik tengah nilai $x$ antara titik $A$ dan $B$, yaitu $\frac{2 + 6}{2} = 4$ tanpa memperhitungkan ordinat titik.</sub>

**Pembahasan:** Langkah 1: Tentukan bentuk umum koordinat titik $P$.
Karena titik $P$ terletak pada sumbu-$X$, ordinatnya bernilai $0$, sehingga $P(x, 0)$.

Langkah 2: Susun persamaan jarak $PA = PB$ atau $PA^2 = PB^2$.
$PA^2 = (x - 2)^2 + (0 - 5)^2 = x^2 - 4x + 4 + 25 = x^2 - 4x + 29$
$PB^2 = (x - 6)^2 + (0 - 1)^2 = x^2 - 12x + 36 + 1 = x^2 - 12x + 37$

Langkah 3: Selesaikan nilai $x$.
$x^2 - 4x + 29 = x^2 - 12x + 37$
$-4x + 12x = 37 - 29$
$8x = 8 \implies x = 1$

Maka koordinat titik $P$ adalah $(1, 0)$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas8-b02-e-medium-bt01-012
*orisinal | C3 | 2 langkah | jenis: keliling belah ketupat koordinat*

Sebuah belah ketupat $ABCD$ memiliki titik-titik sudut berurutan $A(2, 1)$, $B(5, 5)$, $C(2, 9)$, dan $D(-1, 5)$ pada bidang Cartesius. Keliling belah ketupat $ABCD$ tersebut adalah ....

- A. $25$ satuan  
  <sub>Salah: Siswa menghitung luas persegi dari panjang sisi ($5^2 = 25$) bukan keliling belah ketupat.</sub>
- B. $24$ satuan  
  <sub>Salah: Siswa menjumlahkan panjang diagonal mendatar ($6$) dan vertikal ($8$) dikali dua atau salah menghitung nilai hipotenusa.</sub>
- **C. $20$ satuan** ✅  
  <sub>Benar: Panjang sisi $AB = \sqrt{(5 - 2)^2 + (5 - 1)^2} = \sqrt{3^2 + 4^2} = 5$ satuan. Karena keempat sisi belah ketupat sama panjang, kelilingnya adalah $4 \times 5 = 20$ satuan.</sub>
- D. $16$ satuan  
  <sub>Salah: Siswa keliru mengira panjang sisi belah ketupat adalah $4$ satuan.</sub>

**Pembahasan:** Langkah 1: Hitung panjang salah satu sisi belah ketupat, misalnya sisi $AB$ dari titik $A(2, 1)$ ke $B(5, 5)$.
$s = AB = \sqrt{(5 - 2)^2 + (5 - 1)^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5\text{ satuan}$

Langkah 2: Hitung keliling belah ketupat.
$\text{Keliling} = 4 \times s = 4 \times 5 = 20\text{ satuan}$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas8-b02-e-medium-bt01-013
*orisinal | C3 | 2 langkah | jenis: menentukan absis titik berjarak tertentu*

Titik $M(a, 6)$ memiliki jarak $10$ satuan dari titik pangkal $O(0, 0)$. Jika titik $M$ terletak di kuadran II pada bidang Cartesius, nilai $a$ adalah ....

- A. $-16$  
  <sub>Salah: Siswa salah saat menghitung $100 - 36$ atau keliru menarik akar kuadrat.</sub>
- B. $-4$  
  <sub>Salah: Siswa melakukan kesalahan aljabar dengan mengurangkan langsung $10 - 6 = 4$ lalu menambahkan tanda negatif.</sub>
- **C. $-8$** ✅  
  <sub>Benar: Jarak titik $M$ ke $O$ adalah $\sqrt{a^2 + 6^2} = 10 \implies a^2 + 36 = 100 \implies a^2 = 64 \implies a = \pm 8$. Karena berada di kuadran II, absis bernilai negatif, sehingga $a = -8$.</sub>
- D. $8$  
  <sub>Salah: Siswa mengabaikan syarat letak di kuadran II sehingga memilih nilai positif.</sub>

**Pembahasan:** Langkah 1: Gunakan rumus jarak dari titik pangkal $O(0, 0)$ ke titik $M(a, 6)$.
$OM = \sqrt{(a - 0)^2 + (6 - 0)^2} = \sqrt{a^2 + 36}$
Diketahui jarak $OM = 10$ satuan, maka:
$\sqrt{a^2 + 36} = 10$
$a^2 + 36 = 100$
$a^2 = 64$

Langkah 2: Tentukan nilai $a$ berdasarkan syarat kuadran.
$a = \pm\sqrt{64} = \pm 8$
Karena titik $M$ berada di kuadran II, nilai absis $x = a$ harus bernilai negatif ($a < 0$). Maka diperoleh $a = -8$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas8-b02-e-medium-bt01-014
*variasi (angka) | C4 | 3 langkah | jenis: uji jenis segitiga pada koordinat*

Diketahui $\triangle KLM$ memiliki titik-titik sudut $K(0, 7)$, $L(8, 7)$, dan $M(6, 11)$ pada bidang koordinat Cartesius. Apakah $\triangle KLM$ merupakan segitiga siku-siku?

- A. Ya, segitiga siku-siku di $M$ karena $LM^2 + KM^2 = 72$  
  <sub>Salah: Mengira jumlah kuadrat dua sisi otomatis menentukan kesikusikuan tanpa membandingkannya dengan kuadrat sisi terpanjang.</sub>
- **B. Bukan, karena kuadrat sisi terpanjang lebih kecil dari jumlah kuadrat dua sisi lainnya ($64 < 72$)** ✅  
  <sub>Benar: Kuadrat ketiga sisi adalah $KL^2 = 64$, $LM^2 = 20$, dan $KM^2 = 52$. Karena $KL^2 \neq LM^2 + KM^2$ ($64 < 20 + 52$), segitiga tersebut bukan segitiga siku-siku melainkan segitiga lancip.</sub>
- C. Ya, segitiga siku-siku di $K$ karena $KL^2 + KM^2 > LM^2$  
  <sub>Salah: Salah memahami syarat Teorema Pythagoras dengan menganggap ketidaksamaan lebih besar sebagai syarat siku-siku.</sub>
- D. Bukan, karena ketiga sisinya memiliki panjang yang sama  
  <sub>Salah: Keliru mengidentifikasi bahwa segitiga tersebut adalah segitiga sama sisi padahal panjang sisinya berbeda-beda.</sub>

**Pembahasan:** Langkah 1: Menghitung kuadrat panjang tiap sisi menggunakan rumus jarak:
$KL^2 = (8 - 0)^2 + (7 - 7)^2 = 8^2 + 0^2 = 64$
$LM^2 = (6 - 8)^2 + (11 - 7)^2 = (-2)^2 + 4^2 = 4 + 16 = 20$
$KM^2 = (6 - 0)^2 + (11 - 7)^2 = 6^2 + 4^2 = 36 + 16 = 52$

Langkah 2: Menentukan sisi terpanjang, yaitu $KL$ dengan $KL^2 = 64$.

Langkah 3: Menguji hubungan Pythagoras:
$LM^2 + KM^2 = 20 + 52 = 72$
Karena $KL^2 < LM^2 + KM^2$ ($64 < 72$), maka $\triangle KLM$ bukan merupakan segitiga siku-siku (melainkan segitiga lancip).
**Acuan:** pretest — kelas8-b02-p0111-soal-laihan-2-4-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas8-b02-e-medium-bt01-015
*variasi (konteks) | C4 | 3 langkah | jenis: jangkauan pendengaran posisi bertingkat*

Seorang petugas pos pengawas memanggil seorang pendaki menggunakan pelantang suara dengan jarak jangkauan dengar maksimum $50\text{ meter}$. Posisi petugas berada di menara pengawas pada ketinggian $45\text{ meter}$, sedangkan pendaki berada di permukaan tanah pada jarak mendatar $28\text{ meter}$ dari kaki menara. Dapatkah pendaki tersebut mendengar suara panggilan petugas pos pengawas?

- A. Dapat, karena jarak langsung antara petugas dan pendaki adalah $35\text{ meter}$  
  <sub>Salah: Melakukan pengurangan kuadrat $\sqrt{45^2 - 28^2} = \sqrt{2025 - 784} = \sqrt{1241} \approx 35{,}2\text{ meter}$ alih-alih menjumlahkannya.</sub>
- B. Tidak dapat, karena jarak langsung antara petugas dan pendaki adalah $73\text{ meter}$  
  <sub>Salah: Menjumlahkan jarak vertikal dan horizontal secara langsung ($45 + 28 = 73$) tanpa menggunakan Teorema Pythagoras.</sub>
- **C. Tidak dapat, karena jarak langsung antara petugas dan pendaki adalah $53\text{ meter}$** ✅  
  <sub>Benar: Jarak langsung dihitung menggunakan Teorema Pythagoras: $\sqrt{28^2 + 45^2} = \sqrt{784 + 2025} = \sqrt{2809} = 53\text{ meter}$. Karena $53\text{ meter} > 50\text{ meter}$, suara berada di luar jangkauan maksimum.</sub>
- D. Dapat, karena jarak langsung antara petugas dan pendaki adalah $45\text{ meter}$  
  <sub>Salah: Hanya memperhitungkan ketinggian menara secara vertikal dan mengabaikan jarak mendatar.</sub>

**Pembahasan:** Langkah 1: Mengidentifikasi sisi-sisi siku-siku dari segitiga yang terbentuk antara posisi petugas dan pendaki:
Jarak vertikal ($a$) = $45\text{ meter}$
Jarak mendatar ($b$) = $28\text{ meter}$

Langkah 2: Menghitung jarak langsung ($c$) antara petugas dan pendaki:
$c = \sqrt{a^2 + b^2}$
$c = \sqrt{28^2 + 45^2}$
$c = \sqrt{784 + 2025} = \sqrt{2809} = 53\text{ meter}$

Langkah 3: Membandingkan jarak langsung dengan jangkauan maksimum pelantang suara:
Karena jarak langsung ($53\text{ meter}$) lebih besar dari jangkauan dengar maksimum ($50\text{ meter}$), maka pendaki tidak dapat mendengar suara panggilan tersebut.
**Acuan:** siswa — siswa hal.111 Soal Laihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [hard] kelas8-b02-e-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: analisis jenis segitiga*

Diketahui $\triangle ABC$ dengan titik-titik sudut $A(-6, 0)$, $B(0, 8)$, dan $C(9, 2)$. Berdasarkan Teorema Pythagoras dan rumus jarak, apakah $\triangle ABC$ merupakan segitiga siku-siku? Berikan evaluasi yang tepat.

- A. Ya, karena $AB^2 + BC^2 = AC^2$ sehingga $\triangle ABC$ siku-siku di $B$.  
  <sub>Salah: Siswa salah menjumlahkan hasil kuadrat sisi sehingga keliru mengira segitiga siku-siku.</sub>
- B. Ya, karena $AC^2 + BC^2 = AB^2$ sehingga $\triangle ABC$ siku-siku di $C$.  
  <sub>Salah: Siswa keliru mengidentifikasi sisi terpanjang segitiga.</sub>
- **C. Bukan, karena $AC^2 > AB^2 + BC^2$ sehingga $\triangle ABC$ merupakan segitiga tumpul di $B$.** ✅  
  <sub>Benar: Kuadrat jarak ketiga sisi adalah $AB^2 = 100$, $BC^2 = 117$, dan $AC^2 = 229$. Karena $229 > 100 + 117$, segitiga tersebut merupakan segitiga tumpul di $B$.</sub>
- D. Bukan, karena $AC^2 < AB^2 + BC^2$ sehingga $\triangle ABC$ merupakan segitiga lancip.  
  <sub>Salah: Siswa terbalik dalam menerapkan tanda ketidaksamaan Teorema Pythagoras.</sub>

**Pembahasan:** 1. Hitung kuadrat panjang sisi-sisi segitiga menggunakan rumus jarak:
- $AB^2 = (0 - (-6))^2 + (8 - 0)^2 = 6^2 + 8^2 = 36 + 64 = 100$
- $BC^2 = (9 - 0)^2 + (2 - 8)^2 = 9^2 + (-6)^2 = 81 + 36 = 117$
- $AC^2 = (9 - (-6))^2 + (2 - 0)^2 = 15^2 + 2^2 = 225 + 4 = 229$

2. Bandingkan kuadrat sisi terpanjang ($AC^2$) dengan jumlah kuadrat dua sisi lainnya:
$AB^2 + BC^2 = 100 + 117 = 217$
Karena $AC^2 = 229 > 217$, maka $AC^2 > AB^2 + BC^2$.

3. Berdasarkan kebalikan Teorema Pythagoras, $\triangle ABC$ bukan segitiga siku-siku, melainkan segitiga tumpul di titik $B$.
**Acuan:** pretest — kelas8-b02-p0111-soal-laihan-2-4-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [hard] kelas8-b02-e-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: verifikasi bangun datar*

Diberikan empat titik koordinat $P(-2, 1)$, $Q(2, 4)$, $R(-1, 8)$, dan $S(-5, 5)$ yang membentuk segi empat $PQRS$. Dua siswa memberikan pendapat mengenai bentuk bangun tersebut:
- Siswa I: $PQRS$ adalah belah ketupat bukan persegi, karena keempat sisinya sama panjang tetapi diagonalnya tidak sama panjang.
- Siswa II: $PQRS$ adalah persegi, karena keempat sisinya sama panjang ($5$ satuan) dan kedua diagonalnya sama panjang ($\\sqrt{50}$ satuan) sehingga sudut-sudutnya siku-siku.

Evaluasi yang tepat mengenai pendapat kedua siswa tersebut adalah ....

- **A. Siswa II benar, karena keempat sisinya sama panjang dan kedua diagonalnya sama panjang sehingga memenuhi Teorema Pythagoras untuk membentuk sudut siku-siku.** ✅  
  <sub>Benar: Perhitungan jarak menunjukkan $PQ = QR = RS = SP = 5$ satuan dan panjang diagonal $PR = QS = \sqrt{50}$ satuan. Karena $PQ^2 + QR^2 = 25 + 25 = 50 = PR^2$, sudut $Q$ siku-siku sehingga bangun tersebut adalah persegi.</sub>
- B. Kedua siswa salah, karena $PQRS$ merupakan trapesium sembarang dengan sisi yang tidak sama panjang.  
  <sub>Salah: Siswa salah menerapkan rumus selisih koordinat dengan tanda negatif.</sub>
- C. Siswa II salah, karena Teorema Pythagoras menunjukkan bahwa $PQ^2 + QR^2 \neq PR^2$.  
  <sub>Salah: Siswa salah menjumlahkan kuadrat sisi siku-siku saat memverifikasi segitiga siku-siku.</sub>
- D. Siswa I benar, karena panjang diagonal $PR$ tidak sama dengan panjang diagonal $QS$.  
  <sub>Salah: Siswa salah menghitung panjang salah satu diagonal sehingga mengira panjang diagonalnya berbeda.</sub>

**Pembahasan:** 1. Hitung panjang keempat sisi segi empat $PQRS$:
- $PQ = \sqrt{(2 - (-2))^2 + (4 - 1)^2} = \sqrt{4^2 + 3^2} = 5$
- $QR = \sqrt{(-1 - 2)^2 + (8 - 4)^2} = \sqrt{(-3)^2 + 4^2} = 5$
- $RS = \sqrt{(-5 - (-1))^2 + (5 - 8)^2} = \sqrt{(-4)^2 + (-3)^2} = 5$
- $SP = \sqrt{(-2 - (-5))^2 + (1 - 5)^2} = \sqrt{3^2 + (-4)^2} = 5$
Semua sisi sama panjang ($5$ satuan).

2. Hitung panjang kedua diagonal:
- $PR = \sqrt{(-1 - (-2))^2 + (8 - 1)^2} = \sqrt{1^2 + 7^2} = \sqrt{50}$
- $QS = \sqrt{(-5 - 2)^2 + (5 - 4)^2} = \sqrt{(-7)^2 + 1^2} = \sqrt{50}$
Kedua diagonal sama panjang ($\sqrt{50}$ satuan).

3. Uji Teorema Pythagoras pada $\triangle PQR$:
$PQ^2 + QR^2 = 5^2 + 5^2 = 25 + 25 = 50 = PR^2$.
Karena memenuhi Teorema Pythagoras, sudut $PQR = 90^\circ$.

4. Segi empat yang memiliki empat sisi sama panjang dan sudut siku-siku adalah persegi. Jadi, pendapat Siswa II benar.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [hard] kelas8-b02-e-hard-bt01-003
*orisinal | C6 | 4 langkah | jenis: penentuan titik pembentuk bangun*

Titik $A(-1, 2)$ dan $B(7, 2)$ merupakan ujung-ujung hipotenusa dari segitiga siku-siku sama kaki $ABC$. Jika titik $C(x, y)$ berada di atas garis $AB$ (ordinat $y > 2$), koordinat titik $C$ adalah ....

- **A. $(3, 6)$** ✅  
  <sub>Benar: Panjang hipotenusa $AB = 8$, sehingga $AC^2 = BC^2 = \frac{1}{2}(8^2) = 32$. Dari kesimetrisan $x = 3$, dan substitusi ke jarak menghasilkan $(y - 2)^2 = 16 \implies y = 6$.</sub>
- B. $(3, 10)$  
  <sub>Salah: Siswa mengira tinggi segitiga sama dengan panjang hipotenusa ($8$ satuan) sehingga menghitung $y = 2 + 8 = 10$.</sub>
- C. $(4, 6)$  
  <sub>Salah: Siswa salah menghitung absis titik tengah sebagai selisih dibagi dua bukan rata-rata koordinat.</sub>
- D. $(3, 4)$  
  <sub>Salah: Siswa salah menarik akar kuadrat $(y - 2)^2 = 16$ menjadi $y - 2 = 2$ sehingga $y = 4$.</sub>

**Pembahasan:** 1. Hitung panjang hipotenusa $AB$:
$AB = \sqrt{(7 - (-1))^2 + (2 - 2)^2} = 8$ satuan.

2. Karena $\triangle ABC$ siku-siku sama kaki dengan hipotenusa $AB$, maka $AC = BC$ dan:
$AC^2 + BC^2 = AB^2 \implies 2AC^2 = 8^2 = 64 \implies AC^2 = 32$.

3. Tentukan absis $x$ dari $AC = BC$:
$(x - (-1))^2 + (y - 2)^2 = (x - 7)^2 + (y - 2)^2$
$(x + 1)^2 = (x - 7)^2 \implies x^2 + 2x + 1 = x^2 - 14x + 49 \implies 16x = 48 \implies x = 3$.

4. Tentukan ordinat $y$ dengan mensubstitusi $x = 3$ ke $AC^2 = 32$:
$(3 + 1)^2 + (y - 2)^2 = 32$
$16 + (y - 2)^2 = 32$
$(y - 2)^2 = 16$
Karena $y > 2$, maka $y - 2 = 4 \implies y = 6$.

Jadi, koordinat titik $C$ adalah $(3, 6)$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [hard] kelas8-b02-e-hard-bt01-004
*variasi (angka) | C5 | 4 langkah | jenis: evaluasi parameter jarak*

Diketahui jarak antara titik $A(p, -3)$ dan titik $B(9, 12)$ adalah $17$ satuan panjang. Siswa X menyatakan bahwa nilai $p$ yang memenuhi adalah $1$, sedangkan Siswa Y menyatakan bahwa nilai $p$ yang memenuhi adalah $17$. Evaluasi yang tepat terhadap pernyataan kedua siswa tersebut adalah ....

- **A. Kedua siswa benar karena kedua nilai $p$ tersebut menghasilkan jarak yang sama, yaitu $17$ satuan** ✅  
  <sub>Benar: Persamaan $(9 - p)^2 + (12 - (-3))^2 = 17^2$ menghasilkan $(9 - p)^2 = 64$, sehingga $9 - p = 8$ ($p = 1$) atau $9 - p = -8$ ($p = 17$). Kedua nilai memenuhi syarat jarak.</sub>
- B. Kedua siswa salah karena nilai $p$ yang tepat seharusnya adalah $-1$ atau $-17$  
  <sub>Salah: Siswa melakukan kesalahan tanda saat menyelesaikan bentuk aljabar $9 - p = \pm 8$.</sub>
- C. Hanya Siswa Y yang benar karena nilai $p$ negatif diabaikan dalam perhitungan jarak  
  <sub>Salah: Siswa keliru mengira $p = 1$ berasal dari perhitungan negatif yang tidak valid, padahal kedua nilai $p$ bernilai positif.</sub>
- D. Hanya Siswa X yang benar karena nilai $p$ harus lebih kecil dari absis titik $B$  
  <sub>Salah: Siswa salah berasumsi bahwa koordinat titik pertama harus selalu bernilai lebih kecil dari koordinat titik kedua.</sub>

**Pembahasan:** Gunakan rumus jarak antara dua titik:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
$$17 = \sqrt{(9 - p)^2 + (12 - (-3))^2}$$
Kuadratkan kedua sisi:
$$17^2 = (9 - p)^2 + 15^2$$
$$289 = (9 - p)^2 + 225$$
$$(9 - p)^2 = 289 - 225 = 64$$
Akar kuadratkan kedua sisi:
$$9 - p = 8 \implies p = 1$$
atau
$$9 - p = -8 \implies p = 17$$
Karena kedua nilai menghasilkan jarak yang tepat bernilai $17$ satuan, maka pernyataan Siswa X dan Siswa Y keduanya benar.
**Acuan:** pretest — kelas8-b02-p0110-rumus-jarak-b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [hard] kelas8-b02-e-hard-bt01-005
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi jangkauan sinyal*

Sebuah menara pemancar radio darurat terletak pada koordinat $M(-15, 10)$ dan sebuah kapal penyelamat berada pada koordinat $K(25, -20)$ (dalam satuan kilometer). Pemancar radio tersebut memiliki jangkauan sinyal efektif maksimum sebesar $48\text{ km}$. Berdasarkan data tersebut, apakah kapal penyelamat dapat menerima sinyal darurat dari menara pemancar?

- **A. Tidak dapat, karena jarak langsung kapal ke pemancar adalah $50\text{ km}$, melebihi batas jangkauan $48\text{ km}$** ✅  
  <sub>Benar: Jarak dihitung menggunakan teorema Pythagoras: $\sqrt{(25 - (-15))^2 + (-20 - 10)^2} = \sqrt{40^2 + (-30)^2} = 50\text{ km}$. Karena $50 > 48$, sinyal tidak terjangkau.</sub>
- B. Tidak dapat, karena jarak langsung kapal ke pemancar adalah $70\text{ km}$, melebihi batas jangkauan $48\text{ km}$  
  <sub>Salah: Siswa menjumlahkan langsung perubahan jarak vertikal dan horizontal $(40 + 30 = 70\text{ km})$ tanpa menerapkan rumus Pythagoras.</sub>
- C. Dapat, karena jarak langsung kapal ke pemancar adalah $35\text{ km}$, masih berada di dalam jangkauan $48\text{ km}$  
  <sub>Salah: Siswa salah menjumlahkan selisih komponen secara linier sebelum mengakar atau salah menghitung nilai kuadrat.</sub>
- D. Dapat, karena jarak mendatar kedua lokasi hanya $40\text{ km}$, yang nilainya kurang dari $48\text{ km}$  
  <sub>Salah: Siswa hanya mengevaluasi selisih absis horizontal dan mengabaikan selisih ordinat vertikal.</sub>

**Pembahasan:** Hitung jarak langsung antara menara pemancar $M(-15, 10)$ dan kapal $K(25, -20)$:
1. Selisih absis: $\Delta x = x_K - x_M = 25 - (-15) = 40\text{ km}$
2. Selisih ordinat: $\Delta y = y_K - y_M = -20 - 10 = -30\text{ km}$
3. Jarak langsung $d$:
$$d = \sqrt{(\Delta x)^2 + (\Delta y)^2} = \sqrt{40^2 + (-30)^2} = \sqrt{1600 + 900} = \sqrt{2500} = 50\text{ km}$$
4. Evaluasi jangkauan: Sinyal memiliki jangkauan maksimum $48\text{ km}$. Karena $50\text{ km} > 48\text{ km}$, kapal berada di luar jangkauan sinyal pemancar radio.
**Acuan:** siswa — siswa hal.111 Soal Laihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [hard] kelas8-b02-e-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: analisis titik pusat lingkaran luar*

Diberikan segitiga siku-siku $ABC$ dengan koordinat titik sudut $A(-3, 1)$, $B(5, 1)$, dan $C(-3, 7)$. Sebuah titik $P$ dirancang agar memiliki jarak yang sama terhadap ketiga titik sudut segitiga tersebut. Koordinat titik $P$ dan jaraknya ke masing-masing titik sudut adalah ....

- A. $P(1, 1)$ dengan jarak $4$ satuan  
  <sub>Salah: Siswa keliru menetapkan titik tengah sisi alas horizontal $AB$ sebagai titik pusat ekuidistan.</sub>
- B. $P(-3, 4)$ dengan jarak $3$ satuan  
  <sub>Salah: Siswa keliru menetapkan titik tengah sisi tegak vertikal $AC$ sebagai titik pusat ekuidistan.</sub>
- **C. $P(1, 4)$ dengan jarak $5$ satuan** ✅  
  <sub>Benar: Segitiga $ABC$ siku-siku di $A$. Titik yang berjarak sama ke ketiga titik sudut segitiga siku-siku adalah titik tengah sisi miring $BC$, yaitu $((5 + (-3))/2, (1 + 7)/2) = (1, 4)$. Jaraknya ke setiap titik sudut adalah $\sqrt{(1 - (-3))^2 + (4 - 1)^2} = 5$ satuan.</sub>
- D. $P(1, 4)$ dengan jarak $\sqrt{10}$ satuan  
  <sub>Salah: Siswa benar menemukan koordinat titik pusat tetapi salah saat menghitung jarak kuadrat pada rumus Pythagoras.</sub>

**Pembahasan:** 1. Identifikasi segitiga: Sisi $AB$ sejajar sumbu-$X$ (panjang $= 5 - (-3) = 8$) dan sisi $AC$ sejajar sumbu-$Y$ (panjang $= 7 - 1 = 6$). Karena $AB \perp AC$, segitiga siku-siku di $A(-3, 1)$ dengan hipotenusa $BC$.
2. Titik yang berjarak sama ke ketiga titik sudut segitiga siku-siku merupakan titik tengah hipotenusanya:
$$x_P = \frac{x_B + x_C}{2} = \frac{5 + (-3)}{2} = 1$$
$$y_P = \frac{y_B + y_C}{2} = \frac{1 + 7}{2} = 4$$
Jadi koordinat titik $P$ adalah $(1, 4)$.
3. Hitung jarak dari $P(1, 4)$ ke salah satu titik sudut, misalnya $A(-3, 1)$:
$$d = \sqrt{(1 - (-3))^2 + (4 - 1)^2} = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5\text{ satuan}$$
Semua jarak ke titik sudut bernilai sama, yaitu $5$ satuan.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas8-b02-e-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: evaluasi keliling poligon*

Sebuah lahan berbentuk trapesium memiliki titik-titik sudut $K(2, 1)$, $L(14, 1)$, $M(8, 9)$, dan $N(2, 9)$ pada bidang koordinat Cartesius (dalam satuan meter). Seorang pengawas menyatakan bahwa pagar kawat sepanjang $35\text{ meter}$ sudah cukup untuk memagari sekeliling lahan tersebut tanpa terputus. Evaluasi yang tepat terhadap pernyataan pengawas adalah ....

- A. Tepat, karena keliling lahan hanya $32\text{ meter}$, sehingga masih tersisa kawat sepanjang $3\text{ meter}$  
  <sub>Salah: Siswa salah menghitung panjang sisi miring $LM$ dengan menganggapnya sama dengan proyeksi horizontalnya atau salah operasi akar.</sub>
- **B. Tidak tepat, karena keliling lahan adalah $36\text{ meter}$, sehingga pagar kawat kurang $1\text{ meter}$** ✅  
  <sub>Benar: Panjang sisi horizontal $KL = 12\text{ m}$, sisi atas $MN = 6\text{ m}$, sisi tegak $NK = 8\text{ m}$, dan sisi miring $LM = \sqrt{(8 - 14)^2 + (9 - 1)^2} = 10\text{ m}$. Total keliling = $12 + 10 + 6 + 8 = 36\text{ m}$. Pagar $35\text{ m}$ tidak mencukupi.</sub>
- C. Tidak tepat, karena keliling lahan mencapai $40\text{ meter}$, sehingga kawat kurang sepanjang $5\text{ meter}$  
  <sub>Salah: Siswa menjumlahkan komponen selisih absis dan ordinat sisi miring $(6 + 8 = 14)$ alih-alih menggunakan rumus Pythagoras $\sqrt{6^2 + 8^2} = 10$.</sub>
- D. Tepat, karena keliling lahan tepat $35\text{ meter}$ sehingga kawat terpakai seluruhnya pas  
  <sub>Salah: Siswa melakukan kesalahan perhitungan penjumlahan sisi trapesium.</sub>

**Pembahasan:** Hitung masing-masing panjang sisi trapesium $KLMN$:
1. Sisi bawah $KL$: ruas garis horizontal dari $(2, 1)$ ke $(14, 1)$:
$$KL = |14 - 2| = 12\text{ m}$$
2. Sisi tegak $NK$: ruas garis vertikal dari $(2, 9)$ ke $(2, 1)$:
$$NK = |9 - 1| = 8\text{ m}$$
3. Sisi atas $MN$: ruas garis horizontal dari $(8, 9)$ ke $(2, 9)$:
$$MN = |8 - 2| = 6\text{ m}$$
4. Sisi miring $LM$: ruas garis dari $(14, 1)$ ke $(8, 9)$:
$$LM = \sqrt{(8 - 14)^2 + (9 - 1)^2} = \sqrt{(-6)^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\text{ m}$$
5. Keliling total lahan:
$$\text{Keliling} = KL + LM + MN + NK = 12 + 10 + 6 + 8 = 36\text{ m}$$
Karena keliling sebenarnya adalah $36\text{ meter}$, kawat sepanjang $35\text{ meter}$ tidak mencukupi (kurang $1\text{ meter}$). Pernyataan pengawas tidak tepat.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas8-b02-e-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: analisis optimasi jarak rute*

Sebuah pipa cabang utama harus diletakkan pada titik $P(x, 0)$ di sepanjang sumbu-$X$ untuk menyalurkan air ke dua lokasi fasilitas $A(0, 4)$ dan $B(6, 4)$. Dua opsi lokasi titik $P$ diusulkan, yaitu Opsi 1 pada posisi $P_1(3, 0)$ dan Opsi 2 pada posisi $P_2(0, 0)$. Berdasarkan total panjang pipa yang dibutuhkan $(PA + PB)$, kesimpulan yang paling tepat adalah ....

- A. Kedua opsi membutuhkan total panjang pipa yang sama karena jumlah komponen koordinat absis dan ordinatnya setara  
  <sub>Salah: Siswa menjumlahkan selisih koordinat secara terpisah tanpa memperhitungkan hubungan kuadratik pada Teorema Pythagoras.</sub>
- B. Opsi 2 lebih hemat karena pipa langsung menuju fasilitas $A$ hanya berjarak $4$ satuan sehingga totalnya kurang dari $10$ satuan  
  <sub>Salah: Siswa hanya melihat jarak terpendek ke satu titik dan mengabaikan jarak yang bertambah jauh ke titik kedua.</sub>
- C. Opsi 1 lebih boros karena titik $P_1(3, 0)$ berada di tengah-tengah sehingga total panjang pipanya mencapai $14$ satuan  
  <sub>Salah: Siswa salah dalam menghitung hipotenusa segitiga siku-siku dengan panjang sisi $3$ dan $4$.</sub>
- **D. Opsi 1 lebih hemat karena total panjang pipanya adalah $10$ satuan, sedangkan Opsi 2 membutuhkan $(4 + \sqrt{52})$ satuan** ✅  
  <sub>Benar: Untuk $P_1(3, 0)$: $P_1A = \sqrt{3^2 + (-4)^2} = 5$, $P_1B = \sqrt{(-3)^2 + (-4)^2} = 5$, total $= 10$. Untuk $P_2(0, 0)$: $P_2A = 4$, $P_2B = \sqrt{(-6)^2 + (-4)^2} = \sqrt{52} \approx 7,21$, total $= 4 + \sqrt{52} \approx 11,21$. Karena $10 < 11,21$, Opsi 1 lebih pendek.</sub>

**Pembahasan:** Hitung total panjang pipa untuk masing-masing opsi:
1. Untuk Opsi 1 di titik $P_1(3, 0)$:
- $P_1A = \sqrt{(3 - 0)^2 + (0 - 4)^2} = \sqrt{9 + 16} = 5$
- $P_1B = \sqrt{(3 - 6)^2 + (0 - 4)^2} = \sqrt{(-3)^2 + (-4)^2} = 5$
- Total panjang pipa Opsi 1: $5 + 5 = 10\text{ satuan}$

2. Untuk Opsi 2 di titik $P_2(0, 0)$:
- $P_2A = \sqrt{(0 - 0)^2 + (0 - 4)^2} = 4$
- $P_2B = \sqrt{(0 - 6)^2 + (0 - 4)^2} = \sqrt{36 + 16} = \sqrt{52} \approx 7,21$
- Total panjang pipa Opsi 2: $4 + \sqrt{52} \approx 11,21\text{ satuan}$

3. Perbandingan:
Karena $10 < 4 + \sqrt{52}$, penempatan pipa di Opsi 1 membutuhkan bahan yang lebih sedikit dan lebih hemat.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas8-b02-e-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: deteksi kesalahan prosedur*

Diberikan langkah pengerjaan seorang siswa saat menghitung jarak antara titik $P(-7, 2)$ dan titik $Q(5, -3)$:
- Langkah 1: Merumuskan $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
- Langkah 2: Mengisi nilai $d = \sqrt{(5 - (-7))^2 + (-3 - 2)^2}$
- Langkah 3: Menghitung selisih $d = \sqrt{(12)^2 + (-5)^2}$
- Langkah 4: Menghitung kuadrat $d = \sqrt{144 - 25} = \sqrt{119}$ satuan

Berdasarkan stimulus tersebut, evaluasi langkah pengerjaan siswa. Pada langkah manakah kesalahan pertama kali terjadi beserta penjelasannya?

- A. Langkah 1 salah, karena rumus jarak seharusnya menggunakan selisih kuadrat $d = \sqrt{(x_2^2 - x_1^2) + (y_2^2 - y_1^2)}$  
  <sub>Salah: Siswa salah memahami bentuk rumus dasar Pythagoras pada bidang koordinat.</sub>
- **B. Langkah 4 salah, karena $(-5)^2$ seharusnya bernilai positif $25$ sehingga operasi dalam akar adalah $144 + 25$** ✅  
  <sub>Benar: Pada langkah 4, siswa menguadratkan $-5$ dan menulisnya sebagai $-25$, padahal bilangan negatif jika dikuadratkan selalu menghasilkan bilangan positif ($(-5)^2 = 25$), sehingga bentuk yang benar adalah $\sqrt{144 + 25} = \sqrt{169} = 13$.</sub>
- C. Langkah 3 salah, karena $(-3 - 2)$ seharusnya menghasilkan $-1$  
  <sub>Salah: Siswa keliru menjumlahkan bilangan bulat berarah negatif.</sub>
- D. Langkah 2 salah, karena pengurangan bilangan negatif $(5 - (-7))$ seharusnya menghasilkan $-2$  
  <sub>Salah: Siswa salah memahami operasi aljabar tanda minus ganda $5 - (-7) = 5 + 7 = 12$.</sub>

**Pembahasan:** Analisis tiap langkah:
- Langkah 1: Rumus $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ benar.
- Langkah 2: Substitusi titik $P(-7, 2)$ dan $Q(5, -3)$ benar: $x_2 - x_1 = 5 - (-7)$ dan $y_2 - y_1 = -3 - 2$.
- Langkah 3: $5 - (-7) = 12$ dan $-3 - 2 = -5$ benar.
- Langkah 4: Kuadrat dari $(-5)$ adalah $(-5) \times (-5) = +25$, bukan $-25$. Seharusnya $d = \sqrt{144 + 25} = \sqrt{169} = 13$.
Jadi kesalahan pertama kali terjadi pada Langkah 4.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas8-b02-e-hard-bt01-010
*orisinal | C6 | 5 langkah | jenis: perancangan titik koordinat bangun datar*

Sebuah persegi $ABCD$ memiliki tiga titik sudut yang diketahui, yaitu $A(1, 2)$, $B(5, 5)$, dan $C(2, 9)$. Jika titik $D(x, y)$ dirancang untuk melengkapi bangun persegi tersebut, tentukan koordinat titik $D$ beserta panjang diagonal $AC$!

- A. $D(6, 12)$ dan panjang diagonal $AC = 5\sqrt{2}$ satuan  
  <sub>Salah: Siswa keliru menjumlahkan komponen vektor alih-alih mengurangkan sehingga titik berada di arah yang berlawanan.</sub>
- B. $D(-1, 5)$ dan panjang diagonal $AC = 7$ satuan  
  <sub>Salah: Siswa menebak koordinat titik tengah dan mengabaikan nilai akar $\sqrt{50}$.</sub>
- **C. $D(-2, 6)$ dan panjang diagonal $AC = 5\sqrt{2}$ satuan** ✅  
  <sub>Benar: Vektor perpindahan $B \to A$ adalah $(1-5, 2-5) = (-4, -3)$, sehingga koordinat $D = C + (-4, -3) = (2-4, 9-3) = (-2, 6)$. Sisi persegi $s = \sqrt{(5-1)^2 + (5-2)^2} = \sqrt{16 + 9} = 5$. Panjang diagonal $AC = \sqrt{(2-1)^2 + (9-2)^2} = \sqrt{1^2 + 7^2} = \sqrt{50} = 5\sqrt{2}$.</sub>
- D. $D(-2, 6)$ dan panjang diagonal $AC = 10$ satuan  
  <sub>Salah: Siswa salah menghitung diagonal sebagai dua kali panjang sisi ($2 \times 5$) alih-alih $s\sqrt{2}$.</sub>

**Pembahasan:** 1. Hitung panjang sisi $AB$:
$AB^2 = (5-1)^2 + (5-2)^2 = 4^2 + 3^2 = 25 \implies AB = 5$.
2. Hitung panjang sisi $BC$:
$BC^2 = (2-5)^2 + (9-5)^2 = (-3)^2 + 4^2 = 25 \implies BC = 5$.
3. Karena $ABCD$ persegi, ruas garis $AD$ sejajar dan sama panjang dengan ruas garis $BC$. Pergeseran dari $B(5, 5)$ ke $C(2, 9)$ adalah $\Delta x = 2 - 5 = -3$ dan $\Delta y = 9 - 5 = 4$. Pergeseran ini sama dari titik $A(1, 2)$ ke $D(x, y)$:
$x = 1 + (-3) = -2$
$y = 2 + 4 = 6$
Maka titik $D$ adalah $(-2, 6)$.
4. Hitung panjang diagonal $AC$:
$AC = \sqrt{(2-1)^2 + (9-2)^2} = \sqrt{1^2 + 7^2} = \sqrt{1 + 49} = \sqrt{50} = 5\sqrt{2}$ satuan.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas8-b02-e-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: evaluasi kondisi titik batas jarak*

Sebuah titik $K(x, y)$ terletak pada garis mendatar $y = 3$. Diketahui jarak titik $K$ terhadap titik $A(4, -1)$ tepat berjarak $2\sqrt{5}$ satuan panjang. Dua orang siswa memberikan pernyataan mengenai nilai absis $x$:
- Siswa I: $x = 2$
- Siswa II: $x = 6$
Manakah evaluasi yang paling tepat mengenai pernyataan kedua siswa tersebut?

- A. Hanya Siswa I yang benar, karena nilai absis yang lebih kecil selalu menjadi solusi utama  
  <sub>Salah: Siswa mengabaikan solusi akar positif dari persamaan kuadrat aljabar.</sub>
- B. Kedua siswa salah, karena nilai $x$ yang memenuhi seharusnya adalah $x = 4$ dan $x = 8$  
  <sub>Salah: Siswa salah menghitung $(2\sqrt{5})^2 = 20$, dikira $32$ sehingga $(x-4)^2 = 16$.</sub>
- C. Hanya Siswa II yang benar, karena absis tidak boleh lebih kecil dari ordinat garis $y = 3$  
  <sub>Salah: Siswa mengaitkan aturan yang tidak ada antara batas ordinat dan nilai absis.</sub>
- **D. Kedua siswa benar, karena persamaan kuadrat jarak menghasilkan dua nilai absis yang memenuhi yaitu $x = 2$ dan $x = 6$** ✅  
  <sub>Benar: Jarak $AK^2 = (x-4)^2 + (3-(-1))^2 = (2\sqrt{5})^2 \implies (x-4)^2 + 16 = 20 \implies (x-4)^2 = 4 \implies x-4 = 2$ atau $x-4 = -2$, sehingga didapat $x = 6$ atau $x = 2$.</sub>

**Pembahasan:** 1. Titik $K$ memiliki koordinat $(x, 3)$ karena berada pada garis $y = 3$.
2. Jarak $AK = 2\sqrt{5}$, maka kuadrat jaraknya adalah:
$AK^2 = (2\sqrt{5})^2 = 4 \times 5 = 20$.
3. Gunakan rumus jarak kuadrat antara $(x, 3)$ dan $(4, -1)$:
$(x - 4)^2 + (3 - (-1))^2 = 20$
$(x - 4)^2 + (4)^2 = 20$
$(x - 4)^2 + 16 = 20$
$(x - 4)^2 = 4$
4. Selesaikan persamaan kuadrat:
$x - 4 = 2 \implies x = 6$
$x - 4 = -2 \implies x = 2$
Dengan demikian, kedua nilai absis $x = 2$ dan $x = 6$ benar.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas8-b02-e-hard-bt01-012
*orisinal | C6 | 5 langkah | jenis: perancangan koordinat titik segitiga siku-siku*

Dua patok pembatas lahan diletakkan pada koordinat $A(0, -5)$ dan $B(0, 5)$ yang membentuk sisi hipotenusa dari segitiga siku-siku $ABC$. Patok ketiga $C$ harus diletakkan pada sumbu-$X$ positif ($x > 0$) agar sudut siku-siku berada di titik $C$ ($∠ACB = 90^\circ$). Koordinat patok $C$ dan luas segitiga $ABC$ yang terbentuk berturut-turut adalah ....

- A. $C(10, 0)$ dan luas $50\text{ satuan luas}$  
  <sub>Salah: Siswa langsung mengambil panjang hipotenusa $AB = 10$ sebagai nilai absis $x$.</sub>
- B. $C(\sqrt{50}, 0)$ dan luas $25\sqrt{2}\text{ satuan luas}$  
  <sub>Salah: Siswa keliru menyelesaikan persamaan $2x^2 = 100$ bukannya $2x^2 = 50$.</sub>
- C. $C(5, 0)$ dan luas $50\text{ satuan luas}$  
  <sub>Salah: Siswa lupa mengalikan faktor $\frac{1}{2}$ pada rumus luas segitiga.</sub>
- **D. $C(5, 0)$ dan luas $25\text{ satuan luas}$** ✅  
  <sub>Benar: Karena $C(x, 0)$ dengan $x > 0$, maka $AC^2 + BC^2 = AB^2 \implies (x^2 + 25) + (x^2 + 25) = 10^2 \implies 2x^2 + 50 = 100 \implies x^2 = 25 \implies x = 5$. Alas $AB = 10$, tinggi terhadap $AB$ adalah $x = 5$, sehingga luas $= \frac{1}{2} \times 10 \times 5 = 25$.</sub>

**Pembahasan:** Langkah-langkah perancangan koordinat:
1. Tentukan panjang hipotenusa $AB$:
   $AB = \sqrt{(0 - 0)^2 + (5 - (-5))^2} = \sqrt{0 + 10^2} = 10$.
2. Koordinat patok $C$ terletak di sumbu-$X$ positif, yaitu $C(x, 0)$ dengan $x > 0$.
3. Hitung jarak $AC$ dan $BC$:
   $AC^2 = (x - 0)^2 + (0 - (-5))^2 = x^2 + 25$
   $BC^2 = (x - 0)^2 + (0 - 5)^2 = x^2 + 25$
4. Karena $\triangle ABC$ siku-siku di $C$, berlaku Teorema Pythagoras:
   $AC^2 + BC^2 = AB^2$
   $(x^2 + 25) + (x^2 + 25) = 10^2$
   $2x^2 + 50 = 100$
   $2x^2 = 50 \implies x^2 = 25 \implies x = 5$ (karena $x > 0$).
   Jadi, koordinat patok $C$ adalah $(5, 0)$.
5. Hitung luas segitiga $ABC$:
   Karena $A(0, -5)$ dan $B(0, 5)$ berada di sumbu-$Y$, panjang alasnya adalah panjang ruas vertikal $AB = 10$.
   Tinggi segitiga yang ditarik dari $C(5, 0)$ tegak lurus ke sumbu-$Y$ adalah panjang proyeksi horizontalnya, yaitu $t = 5$.
   $\text{Luas } \triangle ABC = \frac{1}{2} \times \text{alas} \times \text{tinggi} = \frac{1}{2} \times 10 \times 5 = 25\text{ satuan luas}$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas8-b02-e-hard-bt01-013
*variasi (angka) | C5 | 4 langkah | jenis: evaluasi perpindahan posisi*

Dua robot penjelajah, Alpha dan Beta, mulai bergerak dari titik asal $(0, 0)$ pada bidang koordinat dengan saling bertolak belakang. Robot Alpha bergerak $12\text{ meter}$ ke arah utara lalu $11\text{ meter}$ ke arah timur. Pada saat bersamaan, Robot Beta bergerak $9\text{ meter}$ ke arah selatan lalu $9\text{ meter}$ ke arah barat. Teknisi Alpha mengklaim jarak lurus kedua robot pada posisi akhir adalah $29\text{ meter}$, sedangkan Teknisi Beta mengklaim jaraknya adalah $41\text{ meter}$. Manakah kesimpulan yang benar mengenai klaim kedua teknisi tersebut?

- A. Teknisi Beta benar, karena jarak dihitung dari total perubahan koordinat horizontal dan vertikal: $(11 + 9) + (12 + 9) = 41\text{ meter}$.  
  <sub>Salah: Siswa keliru menggunakan jarak Manhattan (penjumlahan selisih koordinat) alih-alih rumus jarak Pythagoras.</sub>
- B. Kedua teknisi salah, karena posisi Beta berada pada kuadran negatif sehingga jarak lurusnya adalah $\sqrt{2^2 + 3^2} = \sqrt{13}\text{ meter}$.  
  <sub>Salah: Siswa melakukan pengurangan koordinat secara keliru $(11 - 9)$ dan $(12 - 9)$ karena mengabaikan tanda negatif koordinat titik Beta.</sub>
- C. Teknisi Alpha benar, tetapi perhitungannya adalah menjumlahkan perpindahan total robot: $12 + 11 + 9 + 9 - 12 = 29\text{ meter}$.  
  <sub>Salah: Siswa mencocokkan angka hasil akhir melalui manipulasi aritmetika sembarang tanpa menerapkan rumus jarak dua titik.</sub>
- **D. Teknisi Alpha benar, karena jarak lurus kedua robot adalah $\sqrt{(11 - (-9))^2 + (12 - (-9))^2} = 29\text{ meter}$.** ✅  
  <sub>Benar: Posisi akhir Alpha adalah $(11, 12)$ dan Beta adalah $(-9, -9)$. Jarak lurus keduanya dihitung dengan rumus Pythagoras: $d = \sqrt{(11 - (-9))^2 + (12 - (-9))^2} = \sqrt{20^2 + 21^2} = \sqrt{400 + 441} = \sqrt{841} = 29\text{ meter}$. Jadi klaim Teknisi Alpha benar.</sub>

**Pembahasan:** Menentukan koordinat masing-masing robot:
- Robot Alpha: $x_1 = 11$, $y_1 = 12$ sehingga koordinatnya $(11, 12)$.
- Robot Beta (arah selatan dan barat bernilai negatif): $x_2 = -9$, $y_2 = -9$ sehingga koordinatnya $(-9, -9)$.

Menggunakan rumus jarak dua titik berdasarkan Teorema Pythagoras:
$d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$
$d = \sqrt{(11 - (-9))^2 + (12 - (-9))^2}$
$d = \sqrt{(20)^2 + (21)^2}$
$d = \sqrt{400 + 441} = \sqrt{841} = 29\text{ meter}$.

Dengan demikian, klaim Teknisi Alpha ($29\text{ meter}$) benar, sedangkan klaim Teknisi Beta salah.
**Acuan:** siswa — siswa hal.111 Soal Laihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas8-b02-e-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: evaluasi kolinearitas titik*

Seorang juru ukur tanah mengklaim bahwa tiga patok pembatas tanah yang terletak pada koordinat $P(-3, -2)$, $Q(1, 1)$, dan $R(9, 7)$ dapat dihubungkan membentuk bidang tanah berupa segitiga siku-siku di titik $Q$. Berdasarkan penerapan rumus jarak dan Teorema Pythagoras, apakah klaim juru ukur tersebut tepat?

- A. Klaim tepat, karena nilai $PQ^2 + QR^2 = 25 + 100 = 125$ mendekati kuadrat sisi terpanjang $PR^2 = 225$.  
  <sub>Salah: Siswa mengabaikan syarat kesamaan mutlak pada Teorema Pythagoras dan menganggap selisih nilai kuadrat masih dapat ditoleransi sebagai segitiga siku-siku.</sub>
- **B. Klaim tidak tepat, karena $PQ + QR = PR$ ($5 + 10 = 15$) sehingga ketiga titik terletak pada satu garis lurus (kolinear) dan tidak membentuk segitiga.** ✅  
  <sub>Benar: Jarak $PQ = \sqrt{(1 - (-3))^2 + (1 - (-2))^2} = \sqrt{4^2 + 3^2} = 5$. Jarak $QR = \sqrt{(9 - 1)^2 + (7 - 1)^2} = \sqrt{8^2 + 6^2} = 10$. Jarak $PR = \sqrt{(9 - (-3))^2 + (7 - (-2))^2} = \sqrt{12^2 + 9^2} = 15$. Karena $PQ + QR = 5 + 10 = 15 = PR$, ketiga titik segaris (kolinear) sehingga tidak dapat membentuk bangun segitiga apapun.</sub>
- C. Klaim tepat, karena $PQ = 5$, $QR = 10$, dan $PR = 15$ memenuhi kelipatan tripel Pythagoras $3, 4, 5$.  
  <sub>Salah: Siswa salah mengira bahwa kombinasi panjang $5, 10, 15$ adalah tripel Pythagoras padahal $5^2 + 10^2 \neq 15^2$ ($125 \neq 225$).</sub>
- D. Klaim tidak tepat, karena ketiga titik membentuk segitiga tumpul dengan sifat $PR^2 > PQ^2 + QR^2$.  
  <sub>Salah: Siswa lupa memeriksa ketaksamaan segitiga terlebih dahulu dan langsung menerapkan klasifikasi sudut pada titik yang sebenarnya kolinear.</sub>

**Pembahasan:** Hitung panjang ketiga segmen garis menggunakan rumus jarak dua titik:
1. $PQ = \sqrt{(1 - (-3))^2 + (1 - (-2))^2} = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5$
2. $QR = \sqrt{(9 - 1)^2 + (7 - 1)^2} = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10$
3. $PR = \sqrt{(9 - (-3))^2 + (7 - (-2))^2} = \sqrt{12^2 + 9^2} = \sqrt{144 + 81} = \sqrt{225} = 15$

Periksa hubungan ketiga panjang ruas garis:
$PQ + QR = 5 + 10 = 15 = PR$

Karena jumlah panjang dua ruas garis sama persis dengan panjang ruas garis terpanjang ($PQ + QR = PR$), ketiga titik tersebut terletak pada satu garis lurus yang sama (kolinear). Akibatnya, ketiga patok tidak membentuk segitiga sama sekali. Dengan demikian, klaim juru ukur tidak tepat.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas8-b02-e-hard-bt01-015
*orisinal | C6 | 5 langkah | jenis: penentuan posisi titik ekuidistan*

Sebuah stasiun pemancar $P$ dirancang agar terletak pada garis vertikal $x = 2$ sehingga koordinatnya berbentuk $(2, y)$. Stasiun tersebut harus dibangun sedemikian rupa sehingga jaraknya ke Pos Pemantau $A(-2, 1)$ sama dengan jaraknya ke Pos Pemantau $B(6, 5)$. Koordinat stasiun $P$ dan jarak langsung stasiun tersebut ke masing-masing pos pemantau adalah ....

- A. $P(2, 4)$ dengan jarak $5\text{ satuan}$  
  <sub>Salah: Siswa melakukan kesalahan aljabar saat menyelesaikan persamaan linier $-2y + 1 = -10y + 25$ menjadi $8y = 32$ sehingga memperoleh $y = 4$.</sub>
- **B. $P(2, 3)$ dengan jarak $2\sqrt{5}\text{ satuan}$** ✅  
  <sub>Benar: Persamaan jarak: $PA^2 = PB^2 \Leftrightarrow (2 - (-2))^2 + (y - 1)^2 = (2 - 6))^2 + (y - 5)^2 \Leftrightarrow 16 + y^2 - 2y + 1 = 16 + y^2 - 10y + 25 \Leftrightarrow -2y + 17 = -10y + 41 \Leftrightarrow 8y = 24 \Leftrightarrow y = 3$. Jarak $PA = \sqrt{4^2 + (3 - 1)^2} = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt{5}\text{ satuan}$.</sub>
- C. $P(2, 3)$ dengan jarak $20\text{ satuan}$  
  <sub>Salah: Siswa sudah menemukan ordinat $y = 3$ dengan benar, tetapi lupa menarik akar kuadrat dari nilai $PA^2 = 20$ saat menentukan jarak.</sub>
- D. $P(2, 2)$ dengan jarak $\sqrt{17}\text{ satuan}$  
  <sub>Salah: Siswa salah mengalikan tanda negatif pada penguraian bentuk kuadrat suku dua $(y - 5)^2$.</sub>

**Pembahasan:** Titik $P$ berada pada garis $x = 2$, maka koordinatnya adalah $P(2, y)$.

Syarat jarak stasiun $P$ ke pos $A(-2, 1)$ sama dengan jarak ke pos $B(6, 5)$:
$PA = PB \implies PA^2 = PB^2$

Menggunakan rumus jarak dari Teorema Pythagoras:
$PA^2 = (2 - (-2))^2 + (y - 1)^2 = 4^2 + (y^2 - 2y + 1) = y^2 - 2y + 17$
$PB^2 = (2 - 6)^2 + (y - 5)^2 = (-4)^2 + (y^2 - 10y + 25) = y^2 - 10y + 41$

Samakan kedua persamaan:
$y^2 - 2y + 17 = y^2 - 10y + 41$
$-2y + 10y = 41 - 17$
$8y = 24$
$y = 3$

Diperoleh koordinat stasiun $P(2, 3)$.

Hitung jarak $PA$:
$PA = \sqrt{(2 - (-2))^2 + (3 - 1)^2} = \sqrt{4^2 + 2^2} = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt{5}\text{ satuan}$.

Jadi, titik $P$ adalah $(2, 3)$ dengan jarak $2\sqrt{5}\text{ satuan}$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
