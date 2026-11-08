# Lembar koreksi — kelas11 SMA11U-B3 subbab B: Regresi Linear

58 soal | easy 20, medium 20, hard 18 | variasi 28, orisinal 30
> **Kapasitas kurang (hard): 18 dari kuota 20** — 11 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11-b03-b-easy-bt01-001
*variasi (konteks) | C2 | 1 langkah | jenis: substitusi model regresi*

Hubungan antara lama belajar ($x$, dalam jam) dan skor tes matematika ($y$) dinyatakan dengan persamaan garis regresi $\hat{y} = 45 + 8x$. Jika seorang siswa belajar selama $4$ jam, prediksi skor tes matematika yang diperoleh siswa tersebut adalah...

- A. $53$  
  <sub>Salah: Siswa hanya menjumlahkan $45 + 8$ tanpa mengalikan dengan nilai $x = 4$.</sub>
- B. $69$  
  <sub>Salah: Siswa salah mengalikan dengan $3$, yaitu $45 + 8(3) = 69$.</sub>
- **C. $77$** ✅  
  <sub>Benar: Substitusi $x = 4$ menghasilkan $\hat{y} = 45 + 8(4) = 45 + 32 = 77$.</sub>
- D. $85$  
  <sub>Salah: Siswa menambahkan koefisien sebelum substitusi atau salah hitung menjadi $45 + 8(5) = 85$.</sub>

**Pembahasan:** Persamaan regresi: $\hat{y} = 45 + 8x$
Substitusikan $x = 4$:
$$\hat{y} = 45 + 8(4) = 45 + 32 = 77$$
Jadi, prediksi skor tes matematika siswa tersebut adalah $77$.
**Acuan:** pretest — kelas11-b03-p0121-latihan-34-1e

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11-b03-b-easy-bt01-002
*variasi (konteks) | C2 | 1 langkah | jenis: estimasi nilai variabel dependen*

Sebuah penelitian mengamati hubungan antara dosis pupuk cair ($x$, dalam mL) terhadap pertambahan tinggi tanaman ($y$, dalam cm) dengan model regresi $\hat{y} = 6 + 1{,}5x$. Prediksi pertambahan tinggi tanaman yang diberi pupuk cair sebanyak $8\text{ mL}$ adalah...

- A. $15\text{ cm}$  
  <sub>Salah: Siswa salah menghitung $1{,}5 \times 8$ menjadi $9$, lalu ditambah $6$ menjadi $15$.</sub>
- B. $12\text{ cm}$  
  <sub>Salah: Siswa hanya menghitung suku $1{,}5(8)$ dan lupa menambahkan konstanta $6$.</sub>
- C. $20\text{ cm}$  
  <sub>Salah: Siswa salah menghitung operasi perkalian desimal menjadi $6 + 14 = 20$.</sub>
- **D. $18\text{ cm}$** ✅  
  <sub>Benar: Substitusi $x = 8$ ke dalam model: $\hat{y} = 6 + 1{,}5(8) = 6 + 12 = 18\text{ cm}$.</sub>

**Pembahasan:** Persamaan regresi:
$$\hat{y} = 6 + 1{,}5x$$
Untuk $x = 8$:
$$\hat{y} = 6 + 1{,}5(8) = 6 + 12 = 18\text{ cm}$$
**Acuan:** siswa — siswa hal.120 Eksplorasi 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11-b03-b-easy-bt01-003
*variasi (konteks) | C2 | 2 langkah | jenis: pemilihan garis regresi terbaik*

| Beban ($x$, kg) | Biaya ($y$, ribuan rupiah) |
|---|---|
| $2$ | $15$ |
| $4$ | $25$ |
| $6$ | $35$ |

Berdasarkan tabel data di atas, garis regresi linear yang paling tepat mewakili data tersebut adalah...

- A. $\hat{y} = 3 + 6x$  
  <sub>Salah: Siswa terbalik memilih gradien dan konstanta sehingga jumlah kuadrat residunya tidak minimal.</sub>
- **B. $\hat{y} = 5 + 5x$** ✅  
  <sub>Benar: Model $\hat{y} = 5 + 5x$ menghasilkan prediksi persis sama dengan data teramati: $5+5(2)=15$, $5+5(4)=25$, $5+5(6)=35$, sehingga jumlah kuadrat residunya bernilai nol.</sub>
- C. $\hat{y} = 10 + 3x$  
  <sub>Salah: Garis tidak melalui titik rata-rata $(4, 25)$ dan memiliki residu lebih besar.</sub>
- D. $\hat{y} = 7 + 4x$  
  <sub>Salah: Prediksi model menghasilkan jumlah kuadrat residu lebih besar daripada nol.</sub>

**Pembahasan:** Uji model $\hat{y} = 5 + 5x$:
- $x = 2 \implies \hat{y} = 5 + 5(2) = 15$ (residu $15 - 15 = 0$)
- $x = 4 \implies \hat{y} = 5 + 5(4) = 25$ (residu $25 - 25 = 0$)
- $x = 6 \implies \hat{y} = 5 + 5(6) = 35$ (residu $35 - 35 = 0$)
Jumlah kuadrat residu bernilai $0$, yang merupakan nilai terkecil yang mungkin tercapai. Maka model yang paling tepat adalah $\hat{y} = 5 + 5x$.
**Acuan:** pretest — kelas11-b03-p0117-latihan-33-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11-b03-b-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: karakteristik garis regresi*

Titik koordinat yang selalu dilalui oleh garis regresi linear yang ditentukan dengan metode kuadrat terkecil adalah...

- A. $(x_{\text{min}}, y_{\text{min}})$  
  <sub>Salah: Siswa mengira garis regresi menghubungkan titik terendah dari data observasi.</sub>
- **B. $(\bar{x}, \bar{y})$** ✅  
  <sub>Benar: Garis regresi linear selalu melewati pasangan koordinat nilai rata-rata variabel independen dan dependen $(\bar{x}, \bar{y})$.</sub>
- C. $(x_{\text{maks}}, y_{\text{maks}})$  
  <sub>Salah: Siswa mengira garis regresi wajib melalui data bernilai maksimum.</sub>
- D. $(0, 0)$  
  <sub>Salah: Siswa mengira garis regresi harus selalu berpangkal pada titik asal sumbu koordinat.</sub>

**Pembahasan:** Salah satu sifat pasti dari garis regresi linear hasil metode kuadrat terkecil adalah garis tersebut selalu melewati pasangan titik koordinat rata-rata nilai $x$ dan $y$, yaitu $(\bar{x}, \bar{y})$.
**Acuan:** siswa — siswa hal.113

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11-b03-b-easy-bt01-005
*orisinal | C2 | 1 langkah | jenis: penghitungan residu*

Pada suatu data pengamatan, nilai variabel dependen yang diamati adalah $y = 30$, sedangkan nilai prediksi dari garis regresi linear untuk data tersebut adalah $\hat{y} = 26$. Nilai residu ($\varepsilon$) dari pengamatan tersebut adalah...

- A. $56$  
  <sub>Salah: Siswa menjumlahkan nilai asli dan nilai prediksi alih-alih mencari selisihnya.</sub>
- B. $16$  
  <sub>Salah: Siswa menghitung kuadrat residu $(30 - 26)^2 = 16$ alih-alih nilai residunya.</sub>
- C. $-4$  
  <sub>Salah: Siswa terbalik melakukan pengurangan menjadi $\hat{y} - y = 26 - 30 = -4$.</sub>
- **D. $4$** ✅  
  <sub>Benar: Residu dihitung dengan rumus $\varepsilon = y - \hat{y} = 30 - 26 = 4$.</sub>

**Pembahasan:** Berdasarkan definisi residu:
$$\varepsilon = y - \hat{y}$$
Substitusikan nilai yang diketahui:
$$\varepsilon = 30 - 26 = 4$$
Jadi, nilai residunya adalah $4$.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11-b03-b-easy-bt01-006
*variasi (konteks) | C2 | 1 langkah | jenis: prediksi model linear*

Hubungan antara lama latihan mandiri per minggu ($x$, dalam jam) dan kenaikan skor tes ($y$, dalam poin) dimodelkan oleh persamaan garis regresi $\hat{y} = 0,5 + 0,4x$. Prediksi kenaikan skor tes seorang siswa yang berlatih mandiri selama $5$ jam per minggu adalah...

- A. $2,9\text{ poin}$  
  <sub>Salah: Tertukar operasi perkalian dan penjumlahan: menghitung $(0,5 + 0,4) + 2$ atau salah hitung aritmetika.</sub>
- **B. $2,5\text{ poin}$** ✅  
  <sub>Benar: Substitusikan $x = 5$ ke persamaan $\hat{y} = 0,5 + 0,4(5) = 0,5 + 2,0 = 2,5\text{ poin}$.</sub>
- C. $4,5\text{ poin}$  
  <sub>Salah: Salah melakukan perkalian $0,4 \times 5$ menjadi $4,0$ lalu ditambah $0,5$.</sub>
- D. $2,0\text{ poin}$  
  <sub>Salah: Hanya menghitung nilai suku $bx = 0,4 \times 5$ dan lupa menambahkan konstanta $a = 0,5$.</sub>

**Pembahasan:** Diketahui persamaan garis regresi $\hat{y} = 0,5 + 0,4x$. Untuk $x = 5$ jam:
$$\hat{y} = 0,5 + 0,4(5) = 0,5 + 2,0 = 2,5\text{ poin}$$
Jadi, prediksi kenaikan skor tes adalah $2,5\text{ poin}$.
**Acuan:** siswa — siswa hal.120 Eksplorasi 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11-b03-b-easy-bt01-007
*variasi (konteks) | C2 | 1 langkah | jenis: estimasi nilai regresi*

Pertumbuhan tinggi bibit tanaman cabai ($y$, dalam cm) berdasarkan usia tanam ($x$, dalam minggu) dinyatakan dengan persamaan garis regresi $\hat{y} = 12 + 6,5x$. Berdasarkan model tersebut, prediksi tinggi bibit tanaman yang telah berumur $4$ minggu adalah...

- **A. $38\text{ cm}$** ✅  
  <sub>Benar: Substitusi langsung $x = 4$ menghasilkan $\hat{y} = 12 + 6,5(4) = 12 + 26 = 38\text{ cm}$.</sub>
- B. $74\text{ cm}$  
  <sub>Salah: Menjumlahkan konstanta dengan koefisien terlebih dahulu: $(12 + 6,5) \times 4 = 18,5 \times 4 = 74$.</sub>
- C. $32\text{ cm}$  
  <sub>Salah: Salah mengalikan $6,5 \times 4$ menjadi $20$ sehingga $12 + 20 = 32$.</sub>
- D. $26\text{ cm}$  
  <sub>Salah: Hanya menghitung pertambahan tinggi $6,5 \times 4$ tanpa menambahkan tinggi awal $12\text{ cm}$.</sub>

**Pembahasan:** Substitusikan nilai usia tanam $x = 4$ ke persamaan garis regresi:
$$\hat{y} = 12 + 6,5(4) = 12 + 26 = 38\text{ cm}$$
Jadi, prediksi tinggi bibit tanaman tersebut adalah $38\text{ cm}$.
**Acuan:** siswa — siswa hal.122 Latihan 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11-b03-b-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: evaluasi model regresi*

| Paket Pengiriman | Berat ($x$, kg) | Biaya ($y$, ribu rupiah) |
|---|---|---|
| P | 10 | 50 |
| Q | 20 | 70 |
| R | 30 | 90 |

Berdasarkan data pada tabel di atas, model garis regresi mana yang lebih tepat untuk memprediksi biaya terhadap berat pengiriman?

- A. $\hat{y} = 10 + 2x$  
  <sub>Salah: Memberikan residu yang besar (contoh untuk $x=10$, $\hat{y}=30$ padahal data aslinya $y=50$).</sub>
- **B. $\hat{y} = 30 + 2x$** ✅  
  <sub>Benar: Model $\hat{y} = 30 + 2x$ menghasilkan nilai residu tepat nol untuk semua titik data, sehingga jumlah kuadrat residunya minimum ($0$).</sub>
- C. $\hat{y} = 50 + x$  
  <sub>Salah: Hanya cocok pada titik pertama ($x=10, y=60 \neq 50$) dan memiliki kesalahan estimasi besar di titik lainnya.</sub>
- D. $\hat{y} = 30 + 4x$  
  <sub>Salah: Gradien terlalu besar sehingga menghasilkan prediksi yang jauh menyimpang dari data aktual.</sub>

**Pembahasan:** Uji titik $(x, y)$ pada model $\hat{y} = 30 + 2x$:
- Untuk $x = 10 \Rightarrow \hat{y} = 30 + 2(10) = 50$ (residu $50 - 50 = 0$)
- Untuk $x = 20 \Rightarrow \hat{y} = 30 + 2(20) = 70$ (residu $70 - 70 = 0$)
- Untuk $x = 30 \Rightarrow \hat{y} = 30 + 2(30) = 90$ (residu $90 - 90 = 0$)
Jumlah kuadrat residu adalah $0$, sehingga model $\hat{y} = 30 + 2x$ adalah model garis regresi yang paling tepat.
**Acuan:** pretest — kelas11-b03-p0117-latihan-33-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11-b03-b-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: istilah regresi linear*  **[warning validator]**

Proses penggunaan model persamaan regresi untuk memprediksi nilai variabel dependen pada nilai variabel independen yang masih berada di dalam rentang jangkauan data pengamatan disebut...

- A. korelasi  
  <sub>Salah: Korelasi mengukur kekuatan dan arah hubungan antardua variabel, bukan proses prediksi.</sub>
- B. residu  
  <sub>Salah: Residu adalah selisih antara nilai pengamatan aktual dan nilai prediksi.</sub>
- **C. interpolasi** ✅  
  <sub>Benar: Sesuai definisi pada buku teks, memprediksi nilai di dalam rentang jangkauan data disebut interpolasi.</sub>
- D. ekstrapolasi  
  <sub>Salah: Ekstrapolasi adalah prediksi nilai yang berada di luar jangkauan rentang data.</sub>

**Pembahasan:** Berdasarkan materi Buku Siswa Matematika Kelas XI, proses memprediksi nilai variabel yang berada di dalam jangkauan rentang data yang diamati disebut interpolasi, sedangkan prediksi di luar jangkauan data disebut ekstrapolasi.
**Acuan:** siswa — siswa hal.121
**Warning:** kelas11-b03-b-easy-bt01-009 sangat mirip dengan kelas11-b03-b-easy-bt01-014 (0.85) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11-b03-b-easy-bt01-010
*orisinal | C1 | 1 langkah | jenis: interpretasi koefisien regresi*

Pada bentuk umum persamaan regresi linear $\hat{y} = a + bx$, konstanta $a$ menyatakan...

- **A. titik potong garis regresi terhadap sumbu $y$** ✅  
  <sub>Benar: Konstanta $a$ merupakan nilai $\hat{y}$ ketika $x = 0$, yaitu titik potong garis pada sumbu $y$ (intersep).</sub>
- B. gradien kemiringan garis regresi  
  <sub>Salah: Gradien garis regresi dinyatakan oleh koefisien $b$.</sub>
- C. selisih nilai data pengamatan dengan nilai prediksi  
  <sub>Salah: Selisih nilai data aktual dengan prediksi disebut residu.</sub>
- D. rata-rata dari nilai variabel independen  
  <sub>Salah: Rata-rata variabel independen dilambangkan dengan $\bar{x}$.</sub>

**Pembahasan:** Dalam model persamaan regresi linear $\hat{y} = a + bx$, nilai $a$ merupakan intersep atau titik potong garis terhadap sumbu $y$, sedangkan $b$ menyatakan gradien (kemiringan) garis regresi.
**Acuan:** siswa — siswa hal.118

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11-b03-b-easy-bt01-011
*variasi (konteks) | C2 | 1 langkah | jenis: prediksi nilai data*

Hubungan antara lama pengisian daya gawai ($x$, dalam jam) dan persentase daya baterai ($y$, dalam %) dapat dimodelkan dengan persamaan garis regresi $\hat{y} = 15 + 22x$. Berapakah prediksi persentase daya baterai setelah pengisian daya berlangsung selama $3,5$ jam?

- A. $82\%$  
  <sub>Salah: Kesalahan perhitungan saat mengalikan $22 \times 3,5$ menjadi $67$.</sub>
- B. $77\%$  
  <sub>Salah: Hanya menghitung nilai dari $22 \times 3,5$ tanpa menambahkan nilai konstanta $15$.</sub>
- **C. $92\%$** ✅  
  <sub>Benar: Substitusi $x = 3,5$ ke persamaan menghasilkan $\hat{y} = 15 + 22(3,5) = 15 + 77 = 92\%$.</sub>
- D. $95\%$  
  <sub>Salah: Kesalahan menjumlahkan konstanta $15$ ditambah $80$.</sub>

**Pembahasan:** Diketahui persamaan regresi linear $\hat{y} = 15 + 22x$.
Untuk $x = 3,5$ jam:
$$\hat{y} = 15 + 22(3,5) = 15 + 77 = 92\%$$
Jadi, prediksi persentase daya baterai adalah $92\%$.
**Acuan:** pretest — kelas11-b03-p0121-latihan-34-1e

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11-b03-b-easy-bt01-012
*variasi (angka) | C2 | 1 langkah | jenis: prediksi nilai data*

Model regresi linear untuk rata-rata tinggi badan anak ($y$, dalam cm) terhadap usia ($x$, dalam tahun) diberikan oleh persamaan $\hat{y} = 76 + 6,5x$. Berdasarkan model tersebut, berapa prediksi tinggi badan anak yang berusia $4$ tahun?

- **A. $102\text{ cm}$** ✅  
  <sub>Benar: Substitusi $x = 4$ menghasilkan $\hat{y} = 76 + 6,5(4) = 76 + 26 = 102\text{ cm}$.</sub>
- B. $98\text{ cm}$  
  <sub>Salah: Salah mengalikan $6,5 \times 4 = 22$, sehingga diperoleh $76 + 22 = 98$.</sub>
- C. $82,5\text{ cm}$  
  <sub>Salah: Salah mengoperasikan persamaan dengan menghitung $(76 + 6,5) \times 4 / 4$ atau lupa mengalikan dengan usia secara tepat.</sub>
- D. $106\text{ cm}$  
  <sub>Salah: Salah melakukan penjumlahan $76 + 26$ menjadi $106$.</sub>

**Pembahasan:** Persamaan garis regresi: $\hat{y} = 76 + 6,5x$.
Substitusikan usia $x = 4$ tahun:
$$\hat{y} = 76 + 6,5(4) = 76 + 26 = 102\text{ cm}$$
Jadi, prediksi tinggi badan anak tersebut adalah $102\text{ cm}$.
**Acuan:** siswa — siswa hal.122 Latihan 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11-b03-b-easy-bt01-013
*variasi (konteks) | C2 | 1 langkah | jenis: substitusi persamaan regresi*

Seorang pengelola kedai kopi menemukan bahwa rata-rata banyak cangkir kopi yang terjual per hari ($y$) berkaitan dengan lama jam operasional kedai ($x$, dalam jam) melalui model regresi $\hat{y} = 20 + 15x$. Berapa prediksi banyak cangkir kopi yang terjual jika kedai beroperasi selama $8$ jam per hari?

- **A. $140\text{ cangkir}$** ✅  
  <sub>Benar: Substitusi $x = 8$ menghasilkan $\hat{y} = 20 + 15(8) = 20 + 120 = 140$.</sub>
- B. $160\text{ cangkir}$  
  <sub>Salah: Salah menjumlahkan konstanta atau salah mengalikan $15 \times 8 = 140$ lalu ditambah $20$.</sub>
- C. $120\text{ cangkir}$  
  <sub>Salah: Hanya menghitung nilai $15 \times 8$ dan mengabaikan nilai konstanta $20$.</sub>
- D. $135\text{ cangkir}$  
  <sub>Salah: Salah dalam perkalian dasar $15 \times 8$ menjadi $115$, ditambah $20$ menjadi $135$.</sub>

**Pembahasan:** Substitusikan nilai $x = 8$ ke dalam persamaan regresi:
$$\hat{y} = 20 + 15(8) = 20 + 120 = 140$$
Jadi, prediksi cangkir kopi yang terjual adalah $140\text{ cangkir}$.
**Acuan:** siswa — siswa hal.124 Ayo Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11-b03-b-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: pemahaman konsep regresi*  **[warning validator]**

Proses penggunaan model regresi untuk memprediksi nilai variabel dependen pada nilai variabel independen yang berada di luar jangkauan data pengamatan disebut...

- **A. ekstrapolasi** ✅  
  <sub>Benar: Ekstrapolasi adalah prediksi nilai di luar rentang data pengamatan berdasarkan asumsi tren tetap berlaku.</sub>
- B. interpolasi  
  <sub>Salah: Interpolasi adalah proses memprediksi nilai yang berada di dalam jangkauan data pengamatan.</sub>
- C. korelasi  
  <sub>Salah: Korelasi adalah ukuran keeratan hubungan antara dua variabel kuantitatif, bukan metode prediksi di luar jangkauan.</sub>
- D. eliminasi  
  <sub>Salah: Eliminasi adalah metode penyelesaian sistem aljabar, bukan istilah prediksi data regresi.</sub>

**Pembahasan:** Berdasarkan materi Buku Siswa, ekstrapolasi didefinisikan sebagai penggunaan hubungan antarvariabel untuk memprediksi nilai yang berada di luar jangkauan data dengan asumsi hubungan tersebut tetap berlaku.
**Acuan:** siswa — siswa hal.121
**Warning:** kelas11-b03-b-easy-bt01-009 sangat mirip dengan kelas11-b03-b-easy-bt01-014 (0.85) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11-b03-b-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: komponen bentuk umum regresi*

Pada persamaan garis regresi linear $\hat{y} = a + bx$, nilai $b$ menyatakan...

- A. titik potong garis regresi terhadap sumbu y  
  <sub>Salah: Titik potong garis regresi dengan sumbu y dinyatakan oleh nilai konstanta a, bukan b.</sub>
- B. nilai residu model regresi  
  <sub>Salah: Residu dinyatakan oleh selisih nilai pengamatan dan nilai prediksi (epsilon = y - y topi).</sub>
- C. nilai variabel dependen yang diamati  
  <sub>Salah: Nilai variabel dependen yang diamati disimbolkan dengan y, bukan b.</sub>
- **D. gradien garis regresi** ✅  
  <sub>Benar: Dalam bentuk umum regresi linear y topi = a + bx, nilai b adalah gradien atau kemiringan garis regresi.</sub>

**Pembahasan:** Berdasarkan Buku Siswa, pada bentuk umum garis regresi $\hat{y} = a + bx$, konstanta $a$ adalah titik potong sumbu $y$, sedangkan $b$ menyatakan gradien garis regresi.
**Acuan:** siswa — siswa hal.118

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11-b03-b-easy-bt01-016
*variasi (konteks) | C2 | 1 langkah | jenis: aplikasi model regresi*

Hubungan antara lama waktu pembuatan konten ($x$, dalam jam per hari) dan pertambahan pengikut baru mingguan ($y$, dalam puluhan akun) pada suatu kanal media sosial dimodelkan dengan garis regresi $\hat{y} = 15 + 4x$. Berapa prediksi pertambahan pengikut jika seorang kreator meluangkan waktu rata-rata $6$ jam per hari?

- A. $24\text{ puluh akun}$  
  <sub>Salah: Hanya menghitung nilai perubahan $bx = 4 \times 6 = 24$ tanpa menambahkan konstanta $a$.</sub>
- **B. $39\text{ puluh akun}$** ✅  
  <sub>Benar: Substitusi $x = 6$ ke $\hat{y} = 15 + 4(6) = 15 + 24 = 39$.</sub>
- C. $94\text{ puluh akun}$  
  <sub>Salah: Menjumlahkan koefisien terlebih dahulu sebelum perkalian, yaitu $(15 + 4) \times 6 = 19 \times 6 = 114$ atau tertukar urutan operasi.</sub>
- D. $35\text{ puluh akun}$  
  <sub>Salah: Salah melakukan operasi hitung perkalian $4 \times 6$ menjadi $20$, lalu ditambah $15$.</sub>

**Pembahasan:** Substitusikan nilai $x = 6$ ke persamaan garis regresi:
$$\hat{y} = 15 + 4(6) = 15 + 24 = 39$$
Jadi, prediksi pertambahan pengikut adalah $39\text{ puluh akun}$.
**Acuan:** siswa — siswa hal.124 Ayo Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11-b03-b-easy-bt01-017
*variasi (angka) | C2 | 1 langkah | jenis: perhitungan nilai duga*

Persamaan garis regresi yang menyatakan hubungan antara kecepatan sepeda motor ($x$, dalam km/jam) dan jarak reaksi pengereman ($y$, dalam meter) adalah $\hat{y} = 1,2 + 0,18x$. Berdasarkan persamaan tersebut, prediksi jarak reaksi jika pengendara melaju dengan kecepatan $45\text{ km/jam}$ adalah...

- A. $10,3\text{ m}$  
  <sub>Salah: Salah menjumlahkan desimal $1,2 + 8,1$ menjadi $10,3$.</sub>
- B. $7,3\text{ m}$  
  <sub>Salah: Keliru mengurangkan konstanta dari hasil kali, yaitu $8,1 - 1,2 = 6,9$ atau salah hitung aritmetika dasar.</sub>
- C. $8,1\text{ m}$  
  <sub>Salah: Siswa lupa menjumlahkan konstanta $a = 1,2$ dan hanya menghitung $0,18 \times 45$.</sub>
- **D. $9,3\text{ m}$** ✅  
  <sub>Benar: Substitusi $x = 45$ menghasilkan $\hat{y} = 1,2 + 0,18(45) = 1,2 + 8,1 = 9,3\text{ m}$.</sub>

**Pembahasan:** Substitusikan nilai $x = 45$ ke dalam persamaan regresi:
$$\hat{y} = 1,2 + 0,18(45) = 1,2 + 8,1 = 9,3\text{ m}$$
**Acuan:** siswa — siswa hal.122 Latihan 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11-b03-b-easy-bt01-018
*variasi (konteks) | C2 | 1 langkah | jenis: estimasi nilai ekstrapolasi*

Hubungan antara masa kerja seorang karyawan ($x$, dalam tahun) dan skor evaluasi kinerjanya ($y$, dalam poin) dinyatakan dengan model regresi $\hat{y} = 50 + 2,5x$. Berdasarkan model tersebut, nilai perkiraan skor evaluasi kinerja untuk karyawan yang telah bekerja selama $20\text{ tahun}$ adalah...

- A. $105\text{ poin}$  
  <sub>Salah: Salah menjumlahkan atau menghitung $2,5 \times 20$ menjadi $55$.</sub>
- B. $75\text{ poin}$  
  <sub>Salah: Salah melakukan perkalian $2,5 \times 20$ menjadi $25$, lalu ditambahkan $50$.</sub>
- **C. $100\text{ poin}$** ✅  
  <sub>Benar: Substitusi $x = 20$ ke $\hat{y} = 50 + 2,5(20) = 50 + 50 = 100$.</sub>
- D. $50\text{ poin}$  
  <sub>Salah: Hanya menghitung nilai dari komponen gradien $2,5 \times 20$ tanpa menambahkan konstanta $50$.</sub>

**Pembahasan:** Substitusikan $x = 20$ ke dalam persamaan garis regresi:
$$\hat{y} = 50 + 2,5(20) = 50 + 50 = 100\text{ poin}$$
**Acuan:** siswa — siswa hal.122 Latihan 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11-b03-b-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: definisi residu regresi*

Pada analisis regresi linear, selisih antara nilai variabel dependen yang diamati ($y$) dan nilai variabel dependen yang diprediksi oleh garis regresi ($\hat{y}$) dinamakan...

- A. interpolasi  
  <sub>Salah: Tertukar dengan proses estimasi nilai di dalam rentang jangkauan data.</sub>
- B. intersep  
  <sub>Salah: Tertukar dengan titik potong garis pada sumbu vertikal ($a$).</sub>
- **C. residu** ✅  
  <sub>Benar: Sesuai definisi pada materi buku siswa, selisih antara nilai riil amatan ($y$) dan nilai estimasi garis regresi ($\hat{y}$) disebut residu ($e = y - \hat{y}$).</sub>
- D. gradien  
  <sub>Salah: Tertukar dengan koefisien kemiringan arah garis regresi ($b$).</sub>

**Pembahasan:** Berdasarkan materi Buku Siswa, selisih antara nilai variabel dependen yang diamati ($y$) dan nilai variabel dependen yang diprediksi ($\hat{y}$) didefinisikan sebagai residu ($\varepsilon = y - \hat{y}$).
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11-b03-b-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: konsep metode kuadrat terkecil*

Metode umum yang digunakan untuk menentukan garis regresi paling tepat (best-fit) dengan cara meminimumkan jumlah kuadrat dari nilai-nilai residu dinamakan...

- A. metode nilai mutlak rata-rata  
  <sub>Salah: Terkecoh oleh alternatif meminimumkan nilai mutlak yang sempat dibahas sebagai konsep awal.</sub>
- B. metode bagi dua  
  <sub>Salah: Menyebutkan metode pencarian akar numerik (bisection method).</sub>
- C. metode eliminasi murni  
  <sub>Salah: Menyebutkan metode penyelesaian sistem persamaan linear aljabar.</sub>
- **D. metode kuadrat terkecil** ✅  
  <sub>Benar: Metode yang meminimumkan jumlah kuadrat selisih titik data terhadap garis regresi adalah metode kuadrat terkecil (least squares method).</sub>

**Pembahasan:** Metode umum untuk menempatkan garis lurus ke data observasi dengan meminimumkan jumlah kuadrat residu disebut metode kuadrat terkecil.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11-b03-b-medium-bt01-001
*variasi (konteks) | C4 | 3 langkah | jenis: perbandingan model regresi*

| Waktu Uji ($x$, jam) | Suhu Mesin ($y$, $^{\circ}\text{C}$) |
|---|---|
| $1$ | $3$ |
| $2$ | $5$ |
| $3$ | $8$ |

Dua peneliti mengajukan model garis regresi yang berbeda untuk data pada tabel di atas, yaitu Model A: $\hat{y} = 0,5 + 2,5x$ dan Model B: $\hat{y} = 1 + 2x$. Berdasarkan metode kuadrat terkecil, berapakah jumlah kuadrat residu dari model yang lebih tepat?

- A. $1,00$  
  <sub>Salah: Siswa memilih jumlah kuadrat residu dari Model B yang sebenarnya lebih besar dan kurang tepat.</sub>
- B. $0,50$  
  <sub>Salah: Siswa menghitung jumlah nilai mutlak residu, bukan jumlah kuadrat residu.</sub>
- **C. $0,25$** ✅  
  <sub>Benar: Pada Model A, nilai prediksi berturut-turut adalah $3$, $5,5$, dan $8$. Residu masing-masing adalah $3 - 3 = 0$, $5 - 5,5 = -0,5$, dan $8 - 8 = 0$, sehingga jumlah kuadrat residunya $0^2 + (-0,5)^2 + 0^2 = 0,25$. Pada Model B, nilai prediksi adalah $3$, $5$, dan $7$. Residu masing-masing adalah $3 - 3 = 0$, $5 - 5 = 0$, dan $8 - 7 = 1$, sehingga jumlah kuadrat residunya $0^2 + 0^2 + 1^2 = 1$. Model A lebih tepat karena memiliki jumlah kuadrat residu lebih kecil, yaitu $0,25$.</sub>
- D. $1,25$  
  <sub>Salah: Siswa menjumlahkan total kuadrat residu dari kedua model regresi.</sub>

**Pembahasan:** Langkah 1: Hitung kuadrat residu Model A:
- Untuk $x = 1$: $\hat{y} = 0,5 + 2,5(1) = 3 \implies (3 - 3)^2 = 0$
- Untuk $x = 2$: $\hat{y} = 0,5 + 2,5(2) = 5,5 \implies (5 - 5,5)^2 = (-0,5)^2 = 0,25$
- Untuk $x = 3$: $\hat{y} = 0,5 + 2,5(3) = 8 \implies (8 - 8)^2 = 0$
Jumlah kuadrat residu Model A $= 0 + 0,25 + 0 = 0,25$.

Langkah 2: Hitung kuadrat residu Model B:
- Untuk $x = 1$: $\hat{y} = 1 + 2(1) = 3 \implies (3 - 3)^2 = 0$
- Untuk $x = 2$: $\hat{y} = 1 + 2(2) = 5 \implies (5 - 5)^2 = 0$
- Untuk $x = 3$: $\hat{y} = 1 + 2(3) = 7 \implies (8 - 7)^2 = 1^2 = 1$
Jumlah kuadrat residu Model B $= 0 + 0 + 1 = 1$.

Langkah 3: Menurut metode kuadrat terkecil, model yang lebih tepat adalah model dengan jumlah kuadrat residu terkecil, yaitu Model A dengan nilai $0,25$.
**Acuan:** pretest — kelas11-b03-p0117-latihan-33-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11-b03-b-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: prediksi regresi*

Pada suatu percobaan fisika, diperoleh rata-rata nilai variabel bebas $\bar{x} = 25$ dan rata-rata nilai variabel terikat $\bar{y} = 15$. Jika kemiringan garis regresi (gradien $b$) yang dihasilkan adalah $0,4$, berapakah nilai prediksi $\hat{y}$ untuk nilai $x = 30$?

- A. $22$  
  <sub>Salah: Siswa salah menghitung tanda intersep menjadi $a = \bar{y} + b\bar{x} = 25$, lalu memperoleh nilai yang keliru.</sub>
- **B. $17$** ✅  
  <sub>Benar: Konstanta $a$ dicari dari titik rata-rata: $a = \bar{y} - b\bar{x} = 15 - 0,4(25) = 15 - 10 = 5$. Persamaan regresi adalah $\hat{y} = 5 + 0,4x$. Untuk $x = 30$, diperoleh $\hat{y} = 5 + 0,4(30) = 5 + 12 = 17$.</sub>
- C. $35$  
  <sub>Salah: Siswa terbalik menukar nilai $\bar{x}$ dan $\bar{y}$ saat menghitung persamaan garis regresi.</sub>
- D. $12$  
  <sub>Salah: Siswa hanya menghitung nilai $bx = 0,4 \times 30 = 12$ tanpa menambahkan konstanta $a$.</sub>

**Pembahasan:** Langkah 1: Tentukan nilai titik potong sumbu $y$ ($a$):
$$a = \bar{y} - b\bar{x} = 15 - (0,4)(25) = 15 - 10 = 5$$

Langkah 2: Tuliskan persamaan garis regresi linearnya:
$$\hat{y} = a + bx = 5 + 0,4x$$

Langkah 3: Hitung nilai prediksi untuk $x = 30$:
$$\hat{y} = 5 + 0,4(30) = 5 + 12 = 17$$
**Acuan:** pretest — kelas11-b03-p0121-latihan-34-1e

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11-b03-b-medium-bt01-003
*orisinal | C3 | 2 langkah | jenis: penentuan parameter regresi*

Dari pengolahan data bivariat diperoleh nilai $SS_{xy} = 180$, $SS_{xx} = 60$, rata-rata variabel independen $\bar{x} = 12$, dan rata-rata variabel dependen $\bar{y} = 45$. Berapakah nilai titik potong sumbu $y$ (nilai $a$) pada model regresi linear tersebut?

- **A. $9$** ✅  
  <sub>Benar: Nilai gradien adalah $b = \frac{SS_{xy}}{SS_{xx}} = \frac{180}{60} = 3$. Selanjutnya, titik potong sumbu $y$ adalah $a = \bar{y} - b\bar{x} = 45 - 3(12) = 45 - 36 = 9$.</sub>
- B. $41$  
  <sub>Salah: Siswa terbalik menghitung gradien sebagai $b = \frac{SS_{xx}}{SS_{xy}} = \frac{60}{180} = \frac{1}{3}$, lalu mendapatkan $a = 45 - \frac{1}{3}(12) = 41$.</sub>
- C. $81$  
  <sub>Salah: Siswa salah menggunakan tanda pada rumus intersep sehingga menghitung $a = \bar{y} + b\bar{x} = 45 + 36 = 81$.</sub>
- D. $3$  
  <sub>Salah: Siswa hanya menyelesaikan langkah pertama, yaitu menghitung nilai gradien $b$.</sub>

**Pembahasan:** Langkah 1: Menghitung gradien ($b$):
$$b = \frac{SS_{xy}}{SS_{xx}} = \frac{180}{60} = 3$$

Langkah 2: Menghitung nilai intersep ($a$):
Karena garis regresi selalu melalui titik $(\bar{x}, \bar{y})$, maka:
$$a = \bar{y} - b\bar{x} = 45 - 3(12) = 45 - 36 = 9$$
**Acuan:** siswa — siswa hal.119

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11-b03-b-medium-bt01-004
*orisinal | C4 | 2 langkah | jenis: analisis residu*

Hubungan antara dua variabel dirumuskan oleh persamaan regresi linear $\hat{y} = 14 + 2,5x$. Jika untuk suatu titik pengamatan dengan nilai $x = 8$ diperoleh nilai residu $\varepsilon = -3,5$, berapakah nilai variabel dependen aktual ($y$) dari data pengamatan tersebut?

- A. $26,5$  
  <sub>Salah: Siswa mengurangkan residu dua kali atau salah dalam operasi aljabar pemindahan ruas.</sub>
- **B. $30,5$** ✅  
  <sub>Benar: Nilai prediksi garis regresi untuk $x = 8$ adalah $\hat{y} = 14 + 2,5(8) = 14 + 20 = 34$. Berdasarkan rumus residu $\varepsilon = y - \hat{y}$, maka $-3,5 = y - 34$, sehingga $y = 34 - 3,5 = 30,5$.</sub>
- C. $37,5$  
  <sub>Salah: Siswa salah menggunakan definisi residu menjadi $\varepsilon = \hat{y} - y$, sehingga menghitung $y = 34 + 3,5 = 37,5$.</sub>
- D. $34,0$  
  <sub>Salah: Siswa hanya menghitung nilai prediksi $\hat{y}$ tanpa memperhitungkan nilai residu.</sub>

**Pembahasan:** Langkah 1: Hitung nilai prediksi regresi ($\hat{y}$) pada saat $x = 8$:
$$\hat{y} = 14 + 2,5(8) = 14 + 20 = 34$$

Langkah 2: Tentukan nilai aktual $y$ menggunakan hubungan residu $\varepsilon = y - \hat{y}$:
$$-3,5 = y - 34 \iff y = 34 + (-3,5) = 30,5$$
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11-b03-b-medium-bt01-005
*orisinal | C4 | 2 langkah | jenis: interpretasi dan sifat prediksi*

Sebuah eksperimen mencatat data waktu pemanasan ($x$, dalam menit) pada rentang $2 \le x \le 10$ terhadap suhu cairan ($y$, dalam $^{\circ}\text{C}$) dengan persamaan regresi $\hat{y} = 42 + 4,5x$. Berapakah selisih suhu prediksi antara waktu pemanasan $14$ menit dan $6$ menit, serta apa istilah jenis prediksi yang dilakukan pada saat $x = 14$ menit?

- A. $63^{\circ}\text{C}$ dan interpolasi  
  <sub>Salah: Siswa menghitung nilai prediksi $\hat{y}$ pada $x = 6$ lalu mengiranya sebagai selisih, serta salah mengklasifikasikan metode prediksi.</sub>
- **B. $36^{\circ}\text{C}$ dan ekstrapolasi** ✅  
  <sub>Benar: Selisih prediksi suhu adalah $b \times \Delta x = 4,5 \times (14 - 6) = 4,5 \times 8 = 36^{\circ}\text{C}$. Karena $x = 14$ berada di luar rentang pengamatan ($2 \le x \le 10$), proses prediksi tersebut dinamakan ekstrapolasi.</sub>
- C. $36^{\circ}\text{C}$ dan interpolasi  
  <sub>Salah: Perhitungan selisih benar, tetapi salah mengidentifikasi proses prediksi di luar rentang data sebagai interpolasi.</sub>
- D. $45^{\circ}\text{C}$ dan ekstrapolasi  
  <sub>Salah: Siswa salah menghitung selisih waktu menjadi $10$ menit sehingga memperoleh selisih $4,5 \times 10 = 45$.</sub>

**Pembahasan:** Langkah 1: Hitung selisih prediksi suhu antara $x = 14$ dan $x = 6$:
$$\hat{y}(14) - \hat{y}(6) = (42 + 4,5 \times 14) - (42 + 4,5 \times 6) = 4,5 \times (14 - 6) = 4,5 \times 8 = 36^{\circ}\text{C}$$

Langkah 2: Tentukan jenis prediksinya:
Karena data pengamatan memiliki jangkauan waktu $2 \le x \le 10$ menit, nilai $x = 14$ menit berada di luar jangkauan data pengamatan. Oleh karena itu, penggunaan model regresi untuk nilai $x = 14$ menit disebut ekstrapolasi.
**Acuan:** siswa — siswa hal.121

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11-b03-b-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: estimasi nilai prediksi*

Hubungan antara kecepatan laju mobil ($x$, dalam km/jam) dan jarak reaksi pengereman ($y$, dalam meter) dinyatakan oleh persamaan regresi linear $\hat{y} = 0,8 + 0,22x$.

Berdasarkan persamaan garis regresi tersebut, taksiran jarak reaksi pengereman mobil yang sedang melaju dengan kecepatan $45\text{ km/jam}$ adalah...

- **A. $10,7\text{ m}$** ✅  
  <sub>Benar: Substitusi $x = 45$ ke persamaan: $\hat{y} = 0,8 + 0,22(45) = 0,8 + 9,9 = 10,7\text{ m}$.</sub>
- B. $9,9\text{ m}$  
  <sub>Salah: Hanya menghitung nilai $bx = 0,22 \times 45$ tanpa menjumlahkan konstanta $a = 0,8$.</sub>
- C. $11,5\text{ m}$  
  <sub>Salah: Kesalahan aritmetika saat mengalikan $0,22 \times 45 = 10,7$ lalu ditambah $0,8 = 11,5$.</sub>
- D. $17,9\text{ m}$  
  <sub>Salah: Tertukar posisi koefisien menjadi $\hat{y} = 45 \times 0,8 - 0,22$ atau operasi tidak beraturan.</sub>

**Pembahasan:** Persamaan regresi: $\hat{y} = a + bx = 0,8 + 0,22x$.
Substitusikan $x = 45$:
$$\hat{y} = 0,8 + 0,22(45) = 0,8 + 9,9 = 10,7\text{ m}$$
Jadi, taksiran jarak reaksi pengereman adalah $10,7\text{ m}$.
**Acuan:** pretest — kelas11-b03-p0121-latihan-34-1e

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11-b03-b-medium-bt01-007
*variasi (angka) | C4 | 3 langkah | jenis: analisis residu pencilan*

Seorang peneliti mencatat harga jual ($y$, dalam ribuan rupiah) dari bubuk kopi kemasan terhadap persentase kemurnian ($x$, dalam persen). Model regresi linearnya adalah $\hat{y} = 12 + 1,4x$. Salah satu sampel produk dengan kadar kemurnian $60\%$ dijual dengan harga aktual sebesar Rp105.000,00 ($y = 105$).

Berdasarkan model regresi tersebut, besar nilai residu ($e = y - \hat{y}$) untuk produk kopi tersebut adalah...

- A. Rp96.000,00  
  <sub>Salah: Hanya menghitung nilai prediksi $\hat{y}$ tanpa menghitung selisih residu.</sub>
- B. Rp21.000,00  
  <sub>Salah: Lupa menjumlahkan intersep $12$, sehingga $\hat{y} = 84$, lalu $e = 105 - 84 = 21$ ribu rupiah.</sub>
- **C. Rp9.000,00** ✅  
  <sub>Benar: $\hat{y} = 12 + 1,4(60) = 12 + 84 = 96$ (ribu rupiah). Residu: $e = 105 - 96 = 9$ ribu rupiah atau Rp9.000,00.</sub>
- D. -Rp9.000,00  
  <sub>Salah: Tertukar urutan pengurangan residu menjadi $e = \hat{y} - y = 96 - 105 = -9$ ribu rupiah.</sub>

**Pembahasan:** Langkah 1: Tentukan nilai estimasi $\hat{y}$ untuk $x = 60$.
$$\hat{y} = 12 + 1,4(60) = 12 + 84 = 96\text{ (ribu rupiah)}$$
Langkah 2: Hitung residu ($e = y - \hat{y}$).
$$e = 105 - 96 = 9\text{ (ribu rupiah)} = \text{Rp9.000,00}$$
Jadi, nilai residunya adalah Rp9.000,00.
**Acuan:** siswa — siswa hal.118 Latihan 3.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11-b03-b-medium-bt01-008
*variasi (angka) | C4 | 3 langkah | jenis: evaluasi model regresi*

| Data ke- | $x$ | $y$ |
|---|---|---|
| 1 | $2$ | $5$ |
| 2 | $4$ | $9$ |
| 3 | $6$ | $13$ |

Terdapat dua kandidat model regresi linear: Model I: $\hat{y}_1 = 1 + 2x$ dan Model II: $\hat{y}_2 = 2 + 1,8x$.

Berdasarkan kriteria metode kuadrat terkecil, model yang lebih tepat beserta jumlah kuadrat residunya adalah...

- **A. Model I dengan jumlah kuadrat residu $0$** ✅  
  <sub>Benar: Untuk Model I: pada $x=2, 4, 6$, $\hat{y} = 5, 9, 13$. Semua residu bernilai $0$, sehingga jumlah kuadrat residunya $0$.</sub>
- B. Model II dengan jumlah kuadrat residu $0,32$  
  <sub>Salah: Salah dalam perhitungan kuadrat residu dan salah memilih model optimum.</sub>
- C. Model I dengan jumlah kuadrat residu $1$  
  <sub>Salah: Salah menghitung residu Model I dengan menganggap residu sama dengan intersep.</sub>
- D. Model II dengan jumlah kuadrat residu $0,08$  
  <sub>Salah: Keliru memilih model dengan jumlah kuadrat residu lebih besar padahal Model I bernilai 0.</sub>

**Pembahasan:** Uji Model I ($\hat{y}_1 = 1 + 2x$):
- $x = 2 \Rightarrow \hat{y}_1 = 1 + 4 = 5$, residu $e_1 = 5 - 5 = 0$.
- $x = 4 \Rightarrow \hat{y}_1 = 1 + 8 = 9$, residu $e_2 = 9 - 9 = 0$.
- $x = 6 \Rightarrow \hat{y}_1 = 1 + 12 = 13$, residu $e_3 = 13 - 13 = 0$.
Jumlah kuadrat residu Model I $= 0^2 + 0^2 + 0^2 = 0$.
Karena jumlah kuadrat residunya nol (minimum sempurna), Model I adalah model yang lebih tepat.
**Acuan:** pretest — kelas11-b03-p0117-latihan-33-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11-b03-b-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: kalkulasi intersep dan prediksi*

Suatu kumpulan data berpasangan menghasilkan rata-rata nilai variabel bebas $\bar{x} = 8$ dan rata-rata variabel terikat $\bar{y} = 26$. Gradien garis regresi yang dihitung dengan metode kuadrat terkecil adalah $b = 2,5$.

Persamaan garis regresi linear data tersebut dan nilai prediksinya saat $x = 10$ adalah...

- A. $\hat{y} = -6 + 2,5x$ dan $\hat{y} = 19$  
  <sub>Salah: Tertukar tanda operasi pengurangan $a = b\bar{x} - \bar{y} = 20 - 26 = -6$.</sub>
- B. $\hat{y} = 6 + 2,5x$ dan $\hat{y} = 25$  
  <sub>Salah: Hanya menghitung nilai $2,5 \times 10 = 25$ tanpa menambahkan konstanta $a=6$.</sub>
- C. $\hat{y} = 46 + 2,5x$ dan $\hat{y} = 71$  
  <sub>Salah: Salah rumus intersep dengan menjumlahkan $a = \bar{y} + b\bar{x} = 26 + 20 = 46$.</sub>
- **D. $\hat{y} = 6 + 2,5x$ dan $\hat{y} = 31$** ✅  
  <sub>Benar: $a = \bar{y} - b\bar{x} = 26 - 2,5(8) = 26 - 20 = 6$. Persamaan $\hat{y} = 6 + 2,5x$. Untuk $x = 10$, $\hat{y} = 6 + 2,5(10) = 31$.</sub>

**Pembahasan:** Garis regresi selalu melalui titik rata-rata $(\bar{x}, \bar{y})$:
$$\bar{y} = a + b\bar{x} \implies a = \bar{y} - b\bar{x}$$
$$a = 26 - 2,5(8) = 26 - 20 = 6$$
Sehingga persamaan regresinya adalah $\hat{y} = 6 + 2,5x$.
Untuk $x = 10$:
$$\hat{y} = 6 + 2,5(10) = 6 + 25 = 31$$
**Acuan:** siswa — siswa hal.119

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11-b03-b-medium-bt01-010
*variasi (konteks) | C3 | 2 langkah | jenis: prediksi nilai variabel*

Hubungan antara umur bibit pohon jati ($x$, dalam tahun) dengan keliling lingkar batangnya ($y$, dalam cm) untuk rentang $1 \le x \le 10$ dinyatakan oleh model regresi linear $\hat{y} = 12,4 + 5,5x$. Berdasarkan model tersebut, prediksi keliling lingkar batang pohon jati yang berumur $6,4$ tahun adalah...

- **A. $47,6\text{ cm}$** ✅  
  <sub>Benar: $\hat{y} = 12,4 + 5,5(6,4) = 12,4 + 35,2 = 47,6\text{ cm}$.</sub>
- B. $44,3\text{ cm}$  
  <sub>Salah: Melakukan kesalahan operasi desimal pada perkalian $5,5 \times 6,4 = 31,9$.</sub>
- C. $35,2\text{ cm}$  
  <sub>Salah: Hanya menghitung suku $bx$ tanpa menjumlahkannya dengan nilai intersep $a$.</sub>
- D. $50,2\text{ cm}$  
  <sub>Salah: Tertukar menempatkan nilai variabel bebas ke intersep $a$ atau salah menjumlahkan desimal.</sub>

**Pembahasan:** Substitusikan $x = 6,4$ ke dalam persamaan garis regresi:
$$\hat{y} = 12,4 + 5,5(6,4)$$
$$\hat{y} = 12,4 + 35,2 = 47,6\text{ cm}$$
Jadi, prediksi lingkar batangnya adalah $47,6\text{ cm}$.
**Acuan:** siswa — siswa hal.122 Latihan 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11-b03-b-medium-bt01-011
*variasi (konteks) | C4 | 3 langkah | jenis: deteksi nilai pencilan residu*

| Merek Madu | Kadar Kemurnian ($x$, %) | Harga ($y$, ribu rupiah) |
|---|---|---|
| P | $40$ | $85$ |
| Q | $50$ | $130$ |
| R | $60$ | $115$ |
| S | $80$ | $145$ |

Seorang peneliti memperoleh model regresi linear $\hat{y} = 25 + 1,5x$ untuk memprediksi harga sebotol madu ($y$, dalam ribuan rupiah) berdasarkan persentase kemurniannya ($x$). Berdasarkan tabel data di atas, merek madu yang harganya paling jauh lebih mahal daripada harga prediksi model regresi (memiliki residu positif terbesar) adalah...

- A. Merek R  
  <sub>Salah: Residu merek R adalah $115 - (25 + 1,5(60)) = 115 - 115 = 0$.</sub>
- **B. Merek Q** ✅  
  <sub>Benar: Merek Q memiliki residu $130 - (25 + 1,5(50)) = 130 - 100 = +30$ ribu rupiah, paling tinggi di antara semua merek.</sub>
- C. Merek S  
  <sub>Salah: Terkecoh memilih nilai harga $y$ tertinggi di tabel, padahal residunya $145 - (25 + 1,5(80)) = 145 - 145 = 0$.</sub>
- D. Merek P  
  <sub>Salah: Residu merek P adalah $85 - (25 + 1,5(40)) = 85 - 85 = 0$.</sub>

**Pembahasan:** Hitung harga prediksi $\hat{y} = 25 + 1,5x$ dan residu $\varepsilon = y - \hat{y}$ tiap merek:
- P ($x = 40$): $\hat{y} = 25 + 60 = 85 \rightarrow \varepsilon = 85 - 85 = 0$
- Q ($x = 50$): $\hat{y} = 25 + 75 = 100 \rightarrow \varepsilon = 130 - 100 = +30$
- R ($x = 60$): $\hat{y} = 25 + 90 = 115 \rightarrow \varepsilon = 115 - 115 = 0$
- S ($x = 80$): $\hat{y} = 25 + 120 = 145 \rightarrow \varepsilon = 145 - 145 = 0$
Merek yang harganya paling jauh lebih mahal dari prediksi adalah Merek Q dengan selisih Rp30.000,00 di atas garis.
**Acuan:** siswa — siswa hal.118 Latihan 3.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11-b03-b-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: penyusunan persamaan regresi*

Dari pengamatan sekumpulan data bivariat diperoleh $SS_{xy} = 96$, $SS_{xx} = 32$, nilai rata-rata variabel independen $\bar{x} = 6$, dan nilai rata-rata variabel dependen $\bar{y} = 22$. Persamaan garis regresi linear yang memenuhi kriteria metode kuadrat terkecil adalah...

- A. $\hat{y} = 3 + 4x$  
  <sub>Salah: Tertukar posisi nilai kemiringan garis regresi $b$ dan intersep $a$.</sub>
- B. $\hat{y} = 14 + 1,33x$  
  <sub>Salah: Menghitung gradien terbalik $b = SS_{xx} / SS_{xy} = 32/96 \approx 0,33$ lalu salah hitung intersep.</sub>
- C. $\hat{y} = 40 - 3x$  
  <sub>Salah: Salah menggunakan rumus titik potong dengan menjumlahkan $a = \bar{y} + b\bar{x} = 22 + 18 = 40$.</sub>
- **D. $\hat{y} = 4 + 3x$** ✅  
  <sub>Benar: $b = 96/32 = 3$; $a = 22 - 3(6) = 4$. Persamaan regresi $\hat{y} = 4 + 3x$.</sub>

**Pembahasan:** Langkah 1: Tentukan nilai kemiringan garis ($b$):
$$b = \frac{SS_{xy}}{SS_{xx}} = \frac{96}{32} = 3$$
Langkah 2: Tentukan nilai perpotongan sumbu $y$ ($a$) menggunakan titik rata-rata $(\bar{x}, \bar{y})$:
$$a = \bar{y} - b\bar{x} = 22 - 3(6) = 22 - 18 = 4$$
Langkah 3: Tulis persamaan garis regresi:
$$\hat{y} = a + bx \implies \hat{y} = 4 + 3x$$
**Acuan:** siswa — siswa hal.119

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11-b03-b-medium-bt01-013
*orisinal | C3 | 2 langkah | jenis: perhitungan nilai residu*

Model regresi linear untuk memprediksi hasil panen ($y$, dalam kuintal) berdasarkan luas lahan ($x$, dalam hektare) adalah $\hat{y} = 3,5 + 4,2x$. Pada suatu petak lahan dengan luas $5$ hektare diperoleh hasil panen riil sebesar $23$ kuintal. Nilai residu pada data pengamatan tersebut adalah...

- A. $-2,5\text{ kuintal}$  
  <sub>Salah: Salah menjumlahkan konstanta regresi dengan luas lahan terlebih dahulu.</sub>
- B. $-0,5\text{ kuintal}$  
  <sub>Salah: Kesalahan perhitungan pada substitusi $4,2 \times 5 = 20$ (seharusnya $21$).</sub>
- C. $1,5\text{ kuintal}$  
  <sub>Salah: Terbalik mengurangkan rumus residu menjadi $\hat{y} - y$.</sub>
- **D. $-1,5\text{ kuintal}$** ✅  
  <sub>Benar: $\hat{y} = 3,5 + 4,2(5) = 24,5$; residu $\varepsilon = y - \hat{y} = 23 - 24,5 = -1,5$.</sub>

**Pembahasan:** Langkah 1: Hitung nilai prediksi ($\hat{y}$) saat $x = 5$:
$$\hat{y} = 3,5 + 4,2(5) = 3,5 + 21 = 24,5$$
Langkah 2: Hitung nilai residu:
$$\varepsilon = y - \hat{y} = 23 - 24,5 = -1,5\text{ kuintal}$$
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11-b03-b-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: analisis jangkauan prediksi*

Seorang ilmuwan mengumpulkan data waktu pemanasan logam ($x$, dalam menit) pada interval $4 \le x \le 20$ terhadap pemuaian panjangnya ($y$, dalam mm). Persamaan regresi yang dihasilkan adalah $\hat{y} = 0,6 + 0,15x$. Jika model tersebut digunakan untuk memprediksi pemuaian panjang pada waktu pemanasan $24$ menit, nilai pemuaian yang diprediksi dan kategori proses prediksi tersebut adalah...

- A. $4,2\text{ mm}$ dan interpolasi  
  <sub>Salah: Menghitung nilai prediksi dengan benar tetapi keliru mengidentifikasi sebagai interpolasi.</sub>
- B. $4,8\text{ mm}$ dan ekstrapolasi  
  <sub>Salah: Kesalahan aritmetika saat mengalikan $0,15 \times 24$ menjadi $4,2$ lalu ditambahkan $0,6$ menjadi $4,8$.</sub>
- **C. $4,2\text{ mm}$ dan ekstrapolasi** ✅  
  <sub>Benar: $\hat{y} = 0,6 + 0,15(24) = 4,2\text{ mm}$; karena $x = 24$ berada di luar rentang sampel $4 \le x \le 20$, proses tersebut adalah ekstrapolasi.</sub>
- D. $3,6\text{ mm}$ dan ekstrapolasi  
  <sub>Salah: Lupa menambahkan nilai intersep $0,6$ pada hasil perkalian $0,15 \times 24 = 3,6$.</sub>

**Pembahasan:** Langkah 1: Hitung nilai prediksi pemuaian ($\hat{y}$) untuk $x = 24$:
$$\hat{y} = 0,6 + 0,15(24) = 0,6 + 3,6 = 4,2\text{ mm}$$
Langkah 2: Tinjau rentang nilai variabel independen data pengamatan, yaitu $4 \le x \le 20$. Karena nilai $x = 24$ berada di luar jangkauan sampel pengamatan ($24 > 20$), maka penggunaan model tersebut dikategorikan sebagai ekstrapolasi.
**Acuan:** siswa — siswa hal.121

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11-b03-b-medium-bt01-015
*variasi (konteks) | C3 | 2 langkah | jenis: prediksi regresi linear*

Hubungan antara usia bibit pohon sengon ($x$, dalam bulan) untuk rentang $2 \le x \le 14$ dengan rata-rata tinggi batangnya ($y$, dalam cm) dirumuskan oleh persamaan regresi $\hat{y} = 42 + 6,8x$. Berdasarkan model tersebut, berapa prediksi tinggi bibit pohon yang berumur $7,5$ bulan?

- A. $89,6\text{ cm}$  
  <sub>Salah: Siswa salah mengalikan $6,8 \times 7 = 47,6$ tanpa memperhitungkan pecahan desimal $0,5$ sehingga $42 + 47,6 = 89,6$.</sub>
- **B. $93,0\text{ cm}$** ✅  
  <sub>Benar: Substitusi $x = 7,5$ menghasilkan $\hat{y} = 42 + 6,8(7,5) = 42 + 51,0 = 93,0\text{ cm}$.</sub>
- C. $95,5\text{ cm}$  
  <sub>Salah: Siswa salah menjumlahkan hasil kali menjadi $53,5$ sehingga memperoleh $42 + 53,5 = 95,5$.</sub>
- D. $102,0\text{ cm}$  
  <sub>Salah: Siswa salah memasukkan nilai $x = 7,5$ ke konstanta intersep atau menjumlahkan intersep dengan dua kali hasil perkalian.</sub>

**Pembahasan:** Diketahui persamaan garis regresi $\hat{y} = 42 + 6,8x$. Untuk memprediksi tinggi tanaman pada usia $x = 7,5$ bulan, substitusikan $x = 7,5$ ke dalam persamaan:
$$\hat{y} = 42 + 6,8(7,5)$$
$$\hat{y} = 42 + 51,0 = 93,0\text{ cm}$$
Jadi, prediksi tinggi bibit pohon tersebut adalah $93,0\text{ cm}$.
**Acuan:** siswa — siswa hal.122 Latihan 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11-b03-b-medium-bt01-016
*variasi (konteks) | C4 | 3 langkah | jenis: evaluasi prediksi regresi*

Sebuah penelitian mengamati hubungan antara kadar pupuk tambahan ($x$, dalam gram) pada rentang $5 \le x \le 25$ terhadap pertambahan massa buah melon ($y$, dalam gram) dengan model regresi linear $\hat{y} = 120 + 14,5x$. Seorang petani menggunakan model tersebut untuk memprediksi pertambahan massa buah melon jika diberikan pupuk sebanyak $80\text{ gram}$. Berapakah nilai prediksi tersebut dan bagaimana keandalan estimasinya?

- A. $1.280\text{ gram}$, prediksi sangat andal karena merupakan proses interpolasi  
  <sub>Salah: Siswa benar menghitung nilai tetapi salah memahami definisi ekstrapolasi sebagai interpolasi.</sub>
- B. $1.400\text{ gram}$, prediksi sangat andal karena diperoleh dari model linear yang valid  
  <sub>Salah: Siswa salah melakukan operasi perkalian dan menganggap ekstrapolasi selalu valid tanpa batas.</sub>
- **C. $1.280\text{ gram}$, prediksi kurang andal karena merupakan ekstrapolasi jauh di luar rentang data** ✅  
  <sub>Benar: $\hat{y} = 120 + 14,5(80) = 120 + 1.160 = 1.280\text{ gram}$, dan $x = 80$ berada jauh di luar interval $5 \le x \le 25$ sehingga hasil ekstrapolasi tidak reliabel.</sub>
- D. $1.160\text{ gram}$, prediksi kurang andal karena merupakan ekstrapolasi jauh di luar rentang data  
  <sub>Salah: Siswa lupa menambahkan nilai konstanta intersep $a = 120$.</sub>

**Pembahasan:** Substitusikan nilai $x = 80$ ke persamaan regresi:
$$\hat{y} = 120 + 14,5(80) = 120 + 1.160 = 1.280\text{ gram}$$
Karena nilai $x = 80\text{ gram}$ terletak jauh di luar jangkauan sampel pengamatan ($5 \le x \le 25$), penaksiran ini merupakan proses ekstrapolasi. Model linear pertumbuhan tidak selalu berlaku di luar rentang uji (efek kejenuhan pupuk), sehingga hasil estimasinya kurang dapat dipercaya (kurang andal).
**Acuan:** siswa — siswa hal.122 Latihan 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11-b03-b-medium-bt01-017
*variasi (angka) | C3 | 2 langkah | jenis: prediksi nilai bivariat*

Jarak pengereman darurat ($y$, dalam meter) sebuah kendaraan roda dua yang melaju dengan kecepatan ($x$, dalam km/jam) pada selang $20 \le x \le 80$ dimodelkan oleh persamaan regresi $\hat{y} = -2,4 + 0,26x$. Berapakah estimasi jarak pengereman jika kendaraan melaju dengan kecepatan $65\text{ km/jam}$?

- **A. $14,5\text{ m}$** ✅  
  <sub>Benar: $\hat{y} = -2,4 + 0,26(65) = -2,4 + 16,9 = 14,5\text{ m}$.</sub>
- B. $13,9\text{ m}$  
  <sub>Salah: Siswa keliru menghitung perkalian desimal menjadi $16,3$ sehingga $16,3 - 2,4 = 13,9$.</sub>
- C. $16,9\text{ m}$  
  <sub>Salah: Siswa hanya menghitung suku gradien $0,26 \times 65$ dan mengabaikan intersep negatif.</sub>
- D. $19,3\text{ m}$  
  <sub>Salah: Siswa salah menerapkan tanda intersep dengan menjumlahkannya: $2,4 + 16,9 = 19,3$.</sub>

**Pembahasan:** Persamaan garis regresi: $\hat{y} = -2,4 + 0,26x$.
Substitusi nilai kecepatan $x = 65\text{ km/jam}$:
$$\hat{y} = -2,4 + 0,26(65)$$
$$\hat{y} = -2,4 + 16,9 = 14,5\text{ m}$$
Jadi, perkiraan jarak pengereman yang dibutuhkan adalah $14,5\text{ m}$.
**Acuan:** siswa — siswa hal.121 Latihan 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11-b03-b-medium-bt01-018
*orisinal | C3 | 2 langkah | jenis: karakteristik titik rata-rata regresi*

Garis regresi linear yang diperoleh dari sekumpulan data sampel berpasangan memiliki persamaan $\hat{y} = 15 + 2,4x$. Jika rata-rata nilai variabel bebas dari data tersebut adalah $\bar{x} = 8$, berapakah rata-rata nilai variabel terikatnya ($\bar{y}$)?

- A. $31,8$  
  <sub>Salah: Siswa salah menghitung perkalian desimal $2,4 \times 8 = 16,8$ lalu menambahkannya dengan $15$.</sub>
- B. $27,0$  
  <sub>Salah: Siswa salah menjumlahkan $15 + 2,4$ terlebih dahulu lalu dikalikan dengan $8$, atau salah operasi aritmetika dasar.</sub>
- C. $19,2$  
  <sub>Salah: Siswa hanya menghitung $b\bar{x}$ tanpa menambahkan konstanta $a$.</sub>
- **D. $34,2$** ✅  
  <sub>Benar: Garis regresi selalu melalui $(\bar{x}, \bar{y})$, sehingga $\bar{y} = 15 + 2,4(8) = 15 + 19,2 = 34,2$.</sub>

**Pembahasan:** Salah satu sifat utama garis regresi linear dengan metode kuadrat terkecil adalah garis tersebut selalu melalui titik koordinat rata-rata data, yaitu $(\bar{x}, \bar{y})$.
Dengan menyubstitusikan koordinat rata-rata ke persamaan garis regresi $\hat{y} = a + bx$:
$$\bar{y} = 15 + 2,4(\bar{x})$$
$$\bar{y} = 15 + 2,4(8) = 15 + 19,2 = 34,2$$
Jadi, nilai rata-rata variabel terikatnya adalah $34,2$.
**Acuan:** siswa — siswa hal.119

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11-b03-b-medium-bt01-019
*orisinal | C3 | 2 langkah | jenis: rekonstruksi nilai pengamatan dari residu*

Sebuah garis regresi linear memiliki persamaan $\hat{y} = 7 + 1,6x$. Pada suatu data pengamatan dengan nilai variabel independen $x = 10$, diperoleh nilai residu sebesar $\varepsilon = -2,5$. Berapakah nilai variabel dependen yang sebenarnya ($y$) dari data pengamatan tersebut?

- A. $25,5$  
  <sub>Salah: Siswa keliru menggunakan rumus residu menjadi $\varepsilon = \hat{y} - y$ atau menambahkan residu secara positif: $23 + 2,5 = 25,5$.</sub>
- B. $23,0$  
  <sub>Salah: Siswa hanya menghitung nilai prediksi $\hat{y}$ tanpa memperhitungkan residu.</sub>
- **C. $20,5$** ✅  
  <sub>Benar: $\hat{y} = 7 + 1,6(10) = 23$. Residu $\varepsilon = y - \hat{y} \Rightarrow -2,5 = y - 23 \Rightarrow y = 20,5$.</sub>
- D. $18,0$  
  <sub>Salah: Siswa salah menghitung nilai perkalian pada persamaan regresi menjadi $7 + 13,5 = 20,5$ lalu dikurangi $2,5$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai prediksi $\hat{y}$ untuk $x = 10$:
$$\hat{y} = 7 + 1,6(10) = 7 + 16 = 23$$

Langkah 2: Menghitung nilai teramati $y$ berdasarkan rumus residu:
$$\varepsilon = y - \hat{y}$$
$$-2,5 = y - 23$$
$$y = 23 - 2,5 = 20,5$$

Jadi, nilai variabel dependen yang sebenarnya dari data tersebut adalah $20,5$.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11-b03-b-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: kalkulasi jumlah kuadrat residu*

| $x$ | $y$ |
|---|---|
| $2$ | $5$ |
| $4$ | $8$ |
| $6$ | $12$ |

Berdasarkan tabel data pengamatan di atas, sebuah garis regresi linear diajukan dengan persamaan $\hat{y} = 1,5 + 1,7x$. Jumlah kuadrat residu dari model regresi tersebut adalah...

- A. $0,70$  
  <sub>Salah: Siswa menjumlahkan nilai mutlak residu tanpa menguadratkannya: $|0,1| + |-0,3| + |0,3| = 0,70$.</sub>
- B. $0,10$  
  <sub>Salah: Siswa menjumlahkan nilai residu secara langsung tanpa dikuadratkan: $0,1 + (-0,3) + 0,3 = 0,10$.</sub>
- C. $0,13$  
  <sub>Salah: Siswa salah melakukan operasi kuadrat bilangan desimal: menganggap $(\pm 0,3)^2 = 0,06$, sehingga diperoleh $0,01 + 0,06 + 0,06 = 0,13$.</sub>
- **D. $0,19$** ✅  
  <sub>Benar: Untuk $x = 2$, $\hat{y} = 1,5 + 1,7(2) = 4,9$, sehingga residu $e_1 = 5 - 4,9 = 0,1$ dan $e_1^2 = 0,01$. Untuk $x = 4$, $\hat{y} = 1,5 + 1,7(4) = 8,3$, sehingga residu $e_2 = 8 - 8,3 = -0,3$ dan $e_2^2 = 0,09$. Untuk $x = 6$, $\hat{y} = 1,5 + 1,7(6) = 11,7$, sehingga residu $e_3 = 12 - 11,7 = 0,3$ dan $e_3^2 = 0,09$. Jumlah kuadrat residu $= 0,01 + 0,09 + 0,09 = 0,19$.</sub>

**Pembahasan:** Langkah-langkah menghitung jumlah kuadrat residu:
1. Hitung nilai prediksi $\hat{y} = 1,5 + 1,7x$ untuk setiap data:
- Data 1 ($x=2$): $\hat{y}_1 = 1,5 + 1,7(2) = 4,9$
- Data 2 ($x=4$): $\hat{y}_2 = 1,5 + 1,7(4) = 8,3$
- Data 3 ($x=6$): $\hat{y}_3 = 1,5 + 1,7(6) = 11,7$

2. Tentukan nilai residu $e = y - \hat{y}$:
- $e_1 = 5 - 4,9 = 0,1$
- $e_2 = 8 - 8,3 = -0,3$
- $e_3 = 12 - 11,7 = 0,3$

3. Kuadratkan masing-masing residu lalu jumlahkan:
- $e_1^2 = (0,1)^2 = 0,01$
- $e_2^2 = (-0,3)^2 = 0,09$
- $e_3^2 = (0,3)^2 = 0,09$

$\sum (y - \hat{y})^2 = 0,01 + 0,09 + 0,09 = 0,19$.

Jadi, jumlah kuadrat residu dari model tersebut adalah $0,19$.
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11-b03-b-hard-bt01-001
*variasi (konteks) | C5 | 4 langkah | jenis: analisis residu dan pencilan*

| Gerai UMKM | Biaya Promosi ($x$, juta rupiah) | Penjualan Aktual ($y$, puluh juta rupiah) |
|---|---|---|
| P | $2$ | $6$ |
| Q | $4$ | $15$ |
| R | $6$ | $14$ |
| S | $8$ | $18$ |

Hubungan antara biaya promosi dan hasil penjualan dimodelkan oleh garis regresi linear $\hat{y} = 2 + 2x$. Seorang manajer penjualan mencurigai ada satu gerai yang memiliki lonjakan performa penjualan sangat tinggi melebihi estimasi model.

Gerai manakah yang dimaksud oleh manajer tersebut dan berapakah selisih nilai penjualan aktualnya terhadap prediksi model regresi?

- A. Gerai R, dengan selisih penjualan aktual terhadap prediksi sebesar $4$ puluh juta rupiah  
  <sub>Salah: Siswa salah menghitung substitusi $x = 6$ menjadi $\hat{y} = 10$ sehingga mendapatkan residu $14 - 10 = 4$.</sub>
- B. Gerai S, dengan selisih penjualan aktual terhadap prediksi sebesar $2$ puluh juta rupiah  
  <sub>Salah: Siswa keliru mengira gerai dengan penjualan nominal tertinggi (S = 18) adalah pencilan, dan salah menghitung selisih prediksinya.</sub>
- C. Gerai Q, dengan selisih penjualan aktual terhadap prediksi sebesar $10$ puluh juta rupiah  
  <sub>Salah: Siswa menyebutkan nilai hasil prediksi $\hat{y} = 10$, bukan selisih antara nilai aktual dan prediksi.</sub>
- **D. Gerai Q, dengan selisih penjualan aktual terhadap prediksi sebesar $5$ puluh juta rupiah** ✅  
  <sub>Benar: Nilai prediksi regresi untuk gerai Q adalah $\hat{y} = 2 + 2(4) = 10$, sedangkan penjualan aktualnya $y = 15$. Residunya adalah $15 - 10 = +5$ puluh juta rupiah, yang merupakan deviasi positif terbesar dibandingkan gerai lainnya (gerai P, R, dan S semuanya memiliki residu $0$).</sub>

**Pembahasan:** Langkah 1: Hitung nilai prediksi ($\hat{y}$) untuk setiap gerai menggunakan persamaan $\hat{y} = 2 + 2x$:
- Gerai P ($x = 2$): $\hat{y} = 2 + 2(2) = 6$
- Gerai Q ($x = 4$): $\hat{y} = 2 + 2(4) = 10$
- Gerai R ($x = 6$): $\hat{y} = 2 + 2(6) = 14$
- Gerai S ($x = 8$): $\hat{y} = 2 + 2(8) = 18$

Langkah 2: Hitung nilai residu ($y - \hat{y}$):
- Gerai P: $6 - 6 = 0$
- Gerai Q: $15 - 10 = +5$
- Gerai R: $14 - 14 = 0$
- Gerai S: $18 - 18 = 0$

Langkah 3: Evaluasi titik yang menyimpang paling tinggi:
Gerai Q memiliki nilai residu positif paling besar ($+5$).

Langkah 4: Simpulkan bahwa Gerai Q melampaui prediksi sebesar $5$ puluh juta rupiah.
**Acuan:** siswa — siswa hal.118 Latihan 3.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11-b03-b-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: rekonstruksi nilai pengamatan*

Sebuah penelitian mencatat $5$ pasangan data pengamatan $(x, y)$. Diketahui bahwa jumlah nilai variabel independen adalah $\sum_{i=1}^5 x_i = 35$, dan persamaan garis regresi kuadrat terkecil yang terbentuk adalah $\hat{y} = -4 + 1,8x$. Empat dari lima nilai variabel dependen $y$ yang tercatat adalah $6$, $8$, $9$, dan $12$. Jika catatan nilai $y$ kelima tidak sengaja terhapus, tentukan nilai $y$ kelima tersebut!

- A. $10$  
  <sub>Salah: Siswa lupa mengurangkan konstanta $-4$ sehingga mendapatkan $\bar{y} = 1,8(7) - 4$ yang salah hitung menjadi $9$ lalu memperoleh $45 - 35 = 10$.</sub>
- B. $6$  
  <sub>Salah: Siswa salah menghitung rata-rata nilai $y$ menjadi $8,2$ sehingga total $\sum y = 41$ dan menghasilkan nilai $41 - 35 = 6$.</sub>
- **C. $8$** ✅  
  <sub>Benar: Rata-rata variabel bebas adalah $\bar{x} = 35 / 5 = 7$. Karena garis regresi kuadrat terkecil pasti melewati $(\bar{x}, \bar{y})$, maka $\bar{y} = -4 + 1,8(7) = 8,6$. Jumlah seluruh nilai $y$ adalah $\sum y = 5 \times 8,6 = 43$. Nilai data kelima adalah $43 - (6 + 8 + 9 + 12) = 43 - 35 = 8$.</sub>
- D. $8,6$  
  <sub>Salah: Siswa berhenti pada perhitungan nilai rata-rata $\bar{y}$ dan menganggapnya sebagai nilai data kelima.</sub>

**Pembahasan:** Langkah 1: Tentukan rata-rata nilai $x$ ($\bar{x}$):
$\bar{x} = \frac{\sum x_i}{n} = \frac{35}{5} = 7$.

Langkah 2: Gunakan sifat garis regresi bahwa garis selalu melewati $(\bar{x}, \bar{y})$ untuk mencari $\bar{y}$:
$\bar{y} = -4 + 1,8(7) = -4 + 12,6 = 8,6$.

Langkah 3: Hitung total jumlah seluruh nilai variabel dependen ($\sum y_i$):
$\sum y_i = n \times \bar{y} = 5 \times 8,6 = 43$.

Langkah 4: Hitung nilai data ke-5 yang terhapus:
$y_5 = \sum y_i - (y_1 + y_2 + y_3 + y_4) = 43 - (6 + 8 + 9 + 12) = 43 - 35 = 8$.
**Acuan:** siswa — siswa hal.113

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11-b03-b-hard-bt01-003
*variasi (konteks) | C5 | 3 langkah | jenis: evaluasi prediksi regresi*

Seorang insinyur menguji konsumsi energi harian ($y$, dalam kWh) sebuah mesin pendingin pada berbagai suhu lingkungan ($x$, dalam $^{\circ}\text{C}$) pada rentang operasional $16 \le x \le 32$. Berdasarkan data sampel, diperoleh persamaan garis regresi linear $\hat{y} = 1,5 + 0,25x$. Insinyur tersebut ingin memprediksi konsumsi energi jika mesin dioperasikan pada suhu lingkungan $48^{\circ}\text{C}$.

Berdasarkan konteks data dan metode regresi linear, evaluasi yang paling tepat mengenai nilai prediksi konsumsi energi pada suhu $48^{\circ}\text{C}$ adalah...

- A. prediksi sebesar $12,0\text{ kWh}$ dan kurang dapat dipercaya karena merupakan hasil ekstrapolasi  
  <sub>Salah: Siswa hanya menghitung suku gradien $0,25 \times 48 = 12$ tanpa menjumlahkan konstanta $a = 1,5$.</sub>
- B. prediksi sebesar $14,0\text{ kWh}$, tetapi kurang dapat dipercaya karena merupakan hasil ekstrapolasi  
  <sub>Salah: Siswa melakukan kesalahan aritmetika dalam perkalian desimal atau penjumlahan nilai konstanta.</sub>
- **C. prediksi sebesar $13,5\text{ kWh}$, tetapi kurang dapat dipercaya karena merupakan hasil ekstrapolasi** ✅  
  <sub>Benar: Substitusi $x = 48$ menghasilkan $\hat{y} = 1,5 + 0,25(48) = 1,5 + 12 = 13,5\text{ kWh}$. Karena nilai $x = 48$ berada di luar rentang data sampel ($16 \le x \le 32$), prediksi ini merupakan ekstrapolasi sehingga tingkat reliabilitasnya rendah.</sub>
- D. prediksi sebesar $13,5\text{ kWh}$ dan sangat andal karena merupakan hasil interpolasi  
  <sub>Salah: Siswa salah mengira prediksi di luar rentang data sebagai interpolasi yang andal.</sub>

**Pembahasan:** Langkah 1: Hitung nilai prediksi untuk $x = 48^{\circ}\text{C}$:
$$\hat{y} = 1,5 + 0,25(48) = 1,5 + 12 = 13,5\text{ kWh}$$

Langkah 2: Periksa posisi nilai $x = 48$ terhadap jangkauan data pengamatan ($16 \le x \le 32$). Karena $48 > 32$, proses prediksi ini tergolong ekstrapolasi.

Langkah 3: Evaluasi reliabilitas model. Pada Buku Siswa halaman 121 dijelaskan bahwa ekstrapolasi menggunakan asumsi tren tetap berlaku di luar jangkauan data, sehingga hasilnya lebih rentan bias dan kurang dapat dipercaya dibandingkan interpolasi. Jadi, prediksi bernilai $13,5\text{ kWh}$, tetapi kurang dapat dipercaya karena merupakan ekstrapolasi.
**Acuan:** pretest — kelas11-b03-p0121-latihan-34-1e

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11-b03-b-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: optimasi parameter kuadrat terkecil*

Tiga titik data hasil percobaan disajikan dalam tabel berikut:

| $x$ | $y$ |
|---|---|
| $1$ | $2$ |
| $2$ | $5$ |
| $3$ | $7$ |

Seorang peneliti memodelkan hubungan data tersebut dengan garis regresi yang dipaksa melalui titik asal $(0,0)$, yaitu $\hat{y} = mx$.

Berdasarkan prinsip metode kuadrat terkecil, nilai gradien $m$ yang meminimumkan jumlah kuadrat residu pada data tersebut adalah...

- A. $\frac{14}{33}$  
  <sub>Salah: Siswa membalik perbandingan antara $\sum xy$ dan $\sum x^2$.</sub>
- B. $\frac{7}{3}$  
  <sub>Salah: Siswa hanya menggunakan gradien rata-rata titik akhir terhadap titik awal $(7/3)$ alih-alih metode kuadrat terkecil.</sub>
- C. $\frac{33}{28}$  
  <sub>Salah: Siswa salah menggunakan rumus titik balik kuadrat dengan menggandakan penyebut dua kali lipat.</sub>
- **D. $\frac{33}{14}$** ✅  
  <sub>Benar: Fungsi jumlah kuadrat residu adalah $S(m) = (2 - m)^2 + (5 - 2m)^2 + (7 - 3m)^2 = 14m^2 - 66m + 78$. Nilai minimum fungsi kuadrat tercapai pada sumbu simetri $m = -\frac{-66}{2(14)} = \frac{33}{14}$.</sub>

**Pembahasan:** Langkah 1: Tentukan residu untuk setiap titik terhadap model $\hat{y} = mx$:
- Untuk $(1, 2)$: $\varepsilon_1 = 2 - m(1) = 2 - m$
- Untuk $(2, 5)$: $\varepsilon_2 = 5 - m(2) = 5 - 2m$
- Untuk $(3, 7)$: $\varepsilon_3 = 7 - m(3) = 7 - 3m$

Langkah 2: Susun fungsi jumlah kuadrat residu $S(m)$:
$$S(m) = (2 - m)^2 + (5 - 2m)^2 + (7 - 3m)^2$$
$$S(m) = (4 - 4m + m^2) + (25 - 20m + 4m^2) + (49 - 42m + 9m^2)$$
$$S(m) = 14m^2 - 66m + 78$$

Langkah 3: Cari nilai $m$ yang meminimumkan fungsi parabola terbuka ke atas $f(m) = Am^2 + Bm + C$ menggunakan titik balik $m = -\frac{B}{2A}$:
$$m = -\frac{-66}{2 \times 14} = \frac{66}{28} = \frac{33}{14}$$

Jadi, nilai $m$ yang meminimumkan jumlah kuadrat residu adalah $\frac{33}{14}$.
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11-b03-b-hard-bt01-005
*orisinal | C6 | 5 langkah | jenis: transformasi variabel regresi*

Model regresi linear awal dari sekumpulan data bivariat $(x, y)$ adalah $\hat{y} = a + bx$. Jika seluruh nilai variabel independen diubah menjadi $u = 3x$ dan seluruh nilai variabel dependen diubah menjadi $v = y - 4$, persamaan garis regresi linear baru $\hat{v}$ yang menyatakan hubungan antara $v$ atas $u$ adalah...

- **A. $\hat{v} = (a - 4) + \frac{b}{3}u$** ✅  
  <sub>Benar: Gradien baru $b' = \frac{SS_{uv}}{SS_{uu}} = \frac{3 SS_{xy}}{9 SS_{xx}} = \frac{b}{3}$. Konstanta baru $a' = \bar{v} - b'\bar{u} = (\bar{y} - 4) - \frac{b}{3}(3\bar{x}) = \bar{y} - b\bar{x} - 4 = a - 4$. Maka $\hat{v} = (a - 4) + \frac{b}{3}u$.</sub>
- B. $\hat{v} = (a - 4) + 3bu$  
  <sub>Salah: Siswa mengalikan gradien dengan faktor skala $3$, bukan membaginya.</sub>
- C. $\hat{v} = (a + 4) + \frac{b}{3}u$  
  <sub>Salah: Siswa keliru menandai translasi variabel terikat menjadi penjumlahan alih-alih pengurangan.</sub>
- D. $\hat{v} = a + \frac{b}{3}u$  
  <sub>Salah: Siswa lupa menerapkan pengurangan konstanta $-4$ pada nilai titik potong sumbu.</sub>

**Pembahasan:** Langkah 1: Analisis perubahan rata-rata kedua variabel:
$$\bar{u} = 3\bar{x}$$
$$\bar{v} = \bar{y} - 4$$

Langkah 2: Tentukan nilai jumlah kuadrat terdistribusi untuk variabel baru:
$$u_i - \bar{u} = 3(x_i - \bar{x}) \implies SS_{uu} = \sum (3(x_i - \bar{x}))^2 = 9 SS_{xx}$$
$$v_i - \bar{v} = (y_i - 4) - (\bar{y} - 4) = y_i - \bar{y}$$
$$SS_{uv} = \sum 3(x_i - \bar{x})(y_i - \bar{y}) = 3 SS_{xy}$$

Langkah 3: Hitung gradien garis regresi baru ($b'$):
$$b' = \frac{SS_{uv}}{SS_{uu}} = \frac{3 SS_{xy}}{9 SS_{xx}} = \frac{1}{3} \frac{SS_{xy}}{SS_{xx}} = \frac{b}{3}$$

Langkah 4: Hitung titik potong sumbu baru ($a'$):
$$a' = \bar{v} - b'\bar{u} = (\bar{y} - 4) - \left(\frac{b}{3}\right)(3\bar{x}) = \bar{y} - b\bar{x} - 4$$
Karena pada model awal $a = \bar{y} - b\bar{x}$, maka:
$$a' = a - 4$$

Langkah 5: Susun persamaan garis regresi baru:
$$\hat{v} = (a - 4) + \frac{b}{3}u$$
**Acuan:** siswa — siswa hal.119

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11-b03-b-hard-bt01-006
*variasi (angka) | C5 | 5 langkah | jenis: pemodelan dan evaluasi residu*

| Kecepatan ($x$, km/jam) | Jarak Reaksi ($y$, m) |
|---|---|
| $30$ | $7$ |
| $40$ | $9$ |
| $50$ | $12$ |
| $60$ | $16$ |

Berdasarkan data pada tabel di atas, tentukan persamaan garis regresi linear $\hat{y} = a + bx$ dengan metode kuadrat terkecil. Jika pada uji coba kecepatan $55\text{ km/jam}$ jarak reaksi terukur sesungguhnya adalah $14,8\text{ m}$, berapakah nilai residu dari pengamatan tersebut?

- A. $+1,2\text{ m}$  
  <sub>Salah: Kesalahan menentukan nilai intersep $a$ akibat keliru menghitung tanda negatif.</sub>
- **B. $+0,8\text{ m}$** ✅  
  <sub>Benar: Rata-rata: $\bar{x} = 45$, $\bar{y} = 11$. Nilai $SS_{xx} = (-15)^2 + (-5)^2 + 5^2 + 15^2 = 500$. Nilai $SS_{xy} = (-15)(-4) + (-5)(-2) + 5(1) + 15(5) = 60 + 10 + 5 + 75 = 150$. Gradien $b = \frac{150}{500} = 0,3$. Intersep $a = 11 - 0,3(45) = -2,5$. Persamaan regresi: $\hat{y} = -2,5 + 0,3x$. Prediksi pada $x = 55$: $\hat{y} = -2,5 + 0,3(55) = 14,0\text{ m}$. Residu: $\varepsilon = y - \hat{y} = 14,8 - 14,0 = +0,8\text{ m}$.</sub>
- C. $-0,8\text{ m}$  
  <sub>Salah: Keliru menghitung residu terbalik sebagai prediksi dikurangi amatan asli $(\hat{y} - y)$.</sub>
- D. $+0,3\text{ m}$  
  <sub>Salah: Keliru menganggap nilai gradien $b$ sebagai nilai residu amatan.</sub>

**Pembahasan:** Langkah 1: Menghitung rata-rata:
$$\bar{x} = \frac{30 + 40 + 50 + 60}{4} = 45$$
$$\bar{y} = \frac{7 + 9 + 12 + 16}{4} = 11$$

Langkah 2: Menghitung $SS_{xx}$ dan $SS_{xy}$:
$$SS_{xx} = (30-45)^2 + (40-45)^2 + (50-45)^2 + (60-45)^2 = 225 + 25 + 25 + 225 = 500$$
$$SS_{xy} = (30-45)(7-11) + (40-45)(9-11) + (50-45)(12-11) + (60-45)(16-11)$$
$$SS_{xy} = (-15)(-4) + (-5)(-2) + (5)(1) + (15)(5) = 60 + 10 + 5 + 75 = 150$$

Langkah 3: Menentukan parameter garis regresi:
$$b = \frac{SS_{xy}}{SS_{xx}} = \frac{150}{500} = 0,3$$
$$a = \bar{y} - b\bar{x} = 11 - 0,3(45) = 11 - 13,5 = -2,5$$
Persamaan regresi: $\hat{y} = -2,5 + 0,3x$.

Langkah 4: Menghitung nilai prediksi saat $x = 55$:
$$\hat{y} = -2,5 + 0,3(55) = -2,5 + 16,5 = 14,0\text{ m}$$

Langkah 5: Menghitung residu:
$$\varepsilon = y - \hat{y} = 14,8 - 14,0 = +0,8\text{ m}$$
**Acuan:** pretest — kelas11-b03-p0121-latihan-34-1e

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11-b03-b-hard-bt01-007
*variasi (konteks) | C5 | 3 langkah | jenis: evaluasi reliabilitas prediksi*

Sebuah penelitian mengamati pertumbuhan tinggi bibit tanaman sengon dari usia $2$ hingga $10$ bulan dan menghasilkan model regresi linear $\hat{y} = 25 + 18x$, dengan $x$ menyatakan usia tanaman (dalam bulan) dan $\hat{y}$ menyatakan tinggi tanaman (dalam cm). Seorang peneliti menggunakan model tersebut untuk memprediksi tinggi tanaman saat berusia $30$ tahun ($360$ bulan), yaitu $\hat{y} = 25 + 18(360) = 6.505\text{ cm} = 65,05\text{ m}$. Manakah evaluasi yang paling tepat mengenai reliabilitas prediksi tersebut?

- A. Sangat reliabel karena model regresi linear kuadrat terkecil selalu berlaku untuk setiap nilai $x$ positif berapapun besarnya.  
  <sub>Salah: Mengabaikan batasan interval data dan menganggap garis regresi berlaku mutlak tanpa batas.</sub>
- **B. Sangat tidak reliabel karena merupakan ekstrapolasi yang berada sangat jauh di luar jangkauan data pengamatan ($2 \le x \le 10$ bulan), di mana laju pertumbuhan biologis pohon tidak lagi linier konstan.** ✅  
  <sub>Benar: Ekstrapolasi jauh di luar jangkauan data pengamatan memiliki reliabilitas yang sangat rendah karena asumsi pola pertumbuhan linear konstan tidak lagi berlaku ketika tanaman mencapai fase kedewasaan.</sub>
- C. Tidak reliabel semata-mata karena nilai konstanta intersep $a = 25$ menghasilkan nilai positif pada saat $x = 0$.  
  <sub>Salah: Salah mengidentifikasi alasan ketidakandalan, menyalahkan nilai intersep alih-alih ekstrapolasi ekstrem.</sub>
- D. Cukup reliabel karena nilai prediksi dapat divalidasi menggunakan proses interpolasi pada nilai rata-rata sampel.  
  <sub>Salah: Tertukar antara definisi proses interpolasi (di dalam rentang data) dengan ekstrapolasi (di luar jangkauan data).</sub>

**Pembahasan:** Evaluasi terhadap hasil prediksi regresi linear:
1. Jangkauan data pengamatan asal adalah $2 \le x \le 10$ bulan.
2. Nilai yang diprediksi adalah $x = 360$ bulan, yang berada sangat jauh di luar jangkauan data pengamatan (ekstrapolasi).
3. Secara biologis, laju pertambahan tinggi tanaman akan melambat dan berhenti mendatar (kurva sigmoid) saat memasuki usia dewasa, sehingga hubungan linear tidak lagi bertahan.
Oleh karena itu, prediksi tersebut sangat tidak reliabel karena bahaya ekstrapolasi di luar jangkauan data.
**Acuan:** siswa — siswa hal.122 Latihan 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11-b03-b-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: rekonstruksi data regresi*

Suatu data bivariat terdiri atas $4$ pasangan data dengan nilai rata-rata variabel independen $\bar{x} = 6$ dan rata-rata variabel dependen $\bar{y} = 15$. Persamaan garis regresi kuadrat terkecil dari data tersebut adalah $\hat{y} = 3 + 2x$. Peneliti bermaksud menambahkan $1$ data pengamatan baru ke-5 dengan nilai $x_5 = 11$. Berapakah nilai variabel dependen $y_5$ yang harus dicatat agar titik rata-rata gabungan yang baru $(\bar{x}_{baru}, \bar{y}_{baru})$ tetap dilalui oleh garis regresi tersebut?

- **A. $25$** ✅  
  <sub>Benar: Garis regresi selalu melalui titik rata-rata $(\bar{x}, \bar{y})$. Rata-rata baru $\bar{x}_{baru} = \frac{4(6) + 11}{5} = 7$. Agar garis $\hat{y} = 3 + 2x$ melalui $(\bar{x}_{baru}, \bar{y}_{baru})$, maka $\bar{y}_{baru} = 3 + 2(7) = 17$. Karena $\bar{y}_{baru} = \frac{4(15) + y_5}{5} = \frac{60 + y_5}{5} = 17$, diperoleh $60 + y_5 = 85 \implies y_5 = 25$.</sub>
- B. $22$  
  <sub>Salah: Kesalahan substitusi nilai rata-rata baru ke dalam fungsi tanpa menghitung bobot nilai total.</sub>
- C. $17$  
  <sub>Salah: Keliru mengidentifikasi nilai rata-rata baru $\bar{y}_{baru}$ sebagai nilai data individu $y_5$.</sub>
- D. $28$  
  <sub>Salah: Keliru mengalikan gradien dengan rata-rata lama kemudian menjumlahkannya dengan nilai $x_5$.</sub>

**Pembahasan:** Langkah 1: Menghitung rata-rata variabel independen yang baru:
$$\bar{x}_{baru} = \frac{\sum_{i=1}^4 x_i + x_5}{5} = \frac{4(6) + 11}{5} = \frac{35}{5} = 7$$

Langkah 2: Menentukan syarat agar $(\bar{x}_{baru}, \bar{y}_{baru})$ terletak pada garis $\hat{y} = 3 + 2x$:
$$\bar{y}_{baru} = 3 + 2(\bar{x}_{baru}) = 3 + 2(7) = 17$$

Langkah 3: Menghitung jumlah nilai variabel dependen yang baru:
$$\sum_{i=1}^5 y_i = 5 \times \bar{y}_{baru} = 5 \times 17 = 85$$

Langkah 4: Menentukan nilai data ke-5 ($y_5$):
$$\sum_{i=1}^4 y_i = 4 \times 15 = 60$$
$$y_5 = 85 - 60 = 25$$
**Acuan:** siswa — siswa hal.113

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11-b03-b-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: inferensi residu dan nilai amatan*

Dari $4$ pasangan data pengamatan bivariat $(x, y)$, diperoleh model regresi linear kuadrat terkecil $\hat{y} = 1,5 + 1,2x$. Tiga nilai residu pertama diketahui berturut-turut adalah $\varepsilon_1 = 0,4$, $\varepsilon_2 = -0,9$, dan $\varepsilon_3 = 0,2$. Jika pada data pengamatan ke-4 nilai variabel independennya adalah $x_4 = 5$, berapakah nilai variabel dependen aktual ($y_4$) dari pengamatan ke-4 tersebut?

- **A. $7,8$** ✅  
  <sub>Benar: Pada metode kuadrat terkecil dengan intersep, jumlah seluruh residu adalah nol: $\sum_{i=1}^4 \varepsilon_i = 0$. Maka $0,4 - 0,9 + 0,2 + \varepsilon_4 = 0 \implies \varepsilon_4 = 0,3$. Nilai prediksi $\hat{y}_4 = 1,5 + 1,2(5) = 7,5$. Karena $\varepsilon_4 = y_4 - \hat{y}_4$, maka $y_4 = 7,5 + 0,3 = 7,8$.</sub>
- B. $8,1$  
  <sub>Salah: Kesalahan tanda saat menyelesaikan persamaan jumlah residu sehingga mengira $\varepsilon_4 = 0,6$.</sub>
- C. $7,2$  
  <sub>Salah: Keliru mengurangkan nilai residu dari nilai prediksi ($y_4 = \hat{y}_4 - \varepsilon_4$).</sub>
- D. $7,5$  
  <sub>Salah: Hanya menghitung nilai prediksi $\hat{y}_4$ dan mengabaikan residu amatan ke-4.</sub>

**Pembahasan:** Langkah 1: Menggunakan karakteristik garis regresi kuadrat terkecil bahwa jumlah seluruh residu sama dengan nol:
$$\sum_{i=1}^4 \varepsilon_i = 0$$
$$\varepsilon_1 + \varepsilon_2 + \varepsilon_3 + \varepsilon_4 = 0$$
$$0,4 + (-0,9) + 0,2 + \varepsilon_4 = 0$$
$$-0,3 + \varepsilon_4 = 0 \implies \varepsilon_4 = +0,3$$

Langkah 2: Menghitung nilai prediksi $\hat{y}_4$ untuk $x_4 = 5$:
$$\hat{y}_4 = 1,5 + 1,2(5) = 1,5 + 6,0 = 7,5$$

Langkah 3: Menggunakan rumus residu $\varepsilon_4 = y_4 - \hat{y}_4$ untuk mencari nilai pengamatan asli $y_4$:
$$0,3 = y_4 - 7,5$$
$$y_4 = 7,5 + 0,3 = 7,8$$
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11-b03-b-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: rekonstruksi koefisien regresi*

Pada suatu analisis regresi linear terhadap $10$ sampel data, diperoleh informasi sebagai berikut:
$$\sum_{i=1}^{10} x_i = 60, \quad \sum_{i=1}^{10} y_i = 150, \quad SS_{xx} = 40$$
Seorang analis menemukan bahwa jika nilai gradien garis regresi $b$ dinaikkan sebesar $25\%$, garis regresi yang baru dengan titik pusat $(\bar{x}, \bar{y})$ yang sama akan memotong sumbu-$y$ di titik $(0, 0)$.

Berdasarkan informasi tersebut, berapakah nilai awal dari jumlah kuadrat selisih silang ($SS_{xy}$)?

- **A. $80$** ✅  
  <sub>Benar: Langkah 1: $\bar{x} = 60 / 10 = 6$, $\bar{y} = 150 / 10 = 15$.
Langkah 2: Garis regresi selalu melalui $(\bar{x}, \bar{y}) = (6, 15)$.
Jika garis regresi yang baru memiliki titik potong sumbu-$y$ di $(0, 0)$, maka persamaan garis regresi baru adalah $\hat{y} = b_{\text{baru}} x$.
Karena melalui $(6, 15)$, maka $15 = b_{\text{baru}} (6) \implies b_{\text{baru}} = 15 / 6 = 2,5$.
Langkah 3: Nilai gradien baru diperoleh dengan menaikkan gradien awal sebesar $25\%$, artinya:
$b_{\text{baru}} = 1,25 \times b_{\text{awal}} \implies 2,5 = 1,25 b_{\text{awal}} \implies b_{\text{awal}} = 2$.
Langkah 4: Rumus gradien regresi adalah $b_{\text{awal}} = \frac{SS_{xy}}{SS_{xx}}$.
$2 = \frac{SS_{xy}}{40} \implies SS_{xy} = 2 \times 40 = 80$.</sub>
- B. $64$  
  <sub>Salah: Siswa salah menghitung penurunan dengan membagi $2$ dengan $1,25$ bukannya $2,5$ dibagi $1,25$.</sub>
- C. $100$  
  <sub>Salah: Siswa menggunakan gradien baru $b = 2,5$ langsung pada rumus $SS_{xy} = 2,5 \times 40 = 100$.</sub>
- D. $50$  
  <sub>Salah: Siswa mengalikan nilai rata-rata $15$ dengan $b$ atau salah operasi pembagian awal.</sub>

**Pembahasan:** Langkah 1: Menghitung rata-rata nilai variabel:
$\bar{x} = \frac{\sum x}{n} = \frac{60}{10} = 6$
$\bar{y} = \frac{\sum y}{n} = \frac{150}{10} = 15$

Langkah 2: Menggunakan sifat titik rata-rata pada garis regresi baru:
Garis regresi baru tetap melalui titik koordinat $(\bar{x}, \bar{y}) = (6, 15)$ dan memotong sumbu-$y$ di titik $(0, 0)$, yang berarti konstanta titik potong $a_{\text{baru}} = 0$.
Maka:
$\bar{y} = a_{\text{baru}} + b_{\text{baru}} \bar{x}$
$15 = 0 + b_{\text{baru}} (6) \implies b_{\text{baru}} = \frac{15}{6} = 2,5$

Langkah 3: Menentukan gradien awal $b_{\text{awal}}$:
Diketahui bahwa $b_{\text{baru}}$ merupakan hasil kenaikan $25\%$ dari $b_{\text{awal}}$:
$b_{\text{baru}} = b_{\text{awal}} (1 + 0,25) = 1,25 b_{\text{awal}}$
$2,5 = 1,25 b_{\text{awal}} \implies b_{\text{awal}} = \frac{2,5}{1,25} = 2$

Langkah 4: Menentukan nilai $SS_{xy}$ menggunakan rumus gradien:
$b_{\text{awal}} = \frac{SS_{xy}}{SS_{xx}}$
$2 = \frac{SS_{xy}}{40} \implies SS_{xy} = 2 \times 40 = 80$.

Jadi, nilai awal dari $SS_{xy}$ adalah $80$.
**Acuan:** siswa — siswa hal.119

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11-b03-b-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: evaluasi kelayakan ekstrapolasi*

Seorang teknisi laboratorium meneliti laju pengeringan kadar air gabah ($y$, dalam persen) terhadap lama penyinaran menggunakan mesin pengering ($x$, dalam jam). Data dikumpulkan pada interval waktu pengeringan $2 \le x \le 8$ jam dan menghasilkan model regresi kuadrat terkecil:
$$\hat{y} = 28 - 2,5x$$

Teknisi tersebut ingin memprediksi kadar air gabah jika proses pengeringan dilanjutkan hingga $x = 12$ jam. Berdasarkan konsep regresi, manakah evaluasi yang paling tepat mengenai nilai prediksi tersebut?

- **A. Hasil prediksi adalah $-2\%$; nilai ini diperoleh melalui ekstrapolasi dan tidak realistis karena kadar air tidak dapat bernilai negatif.** ✅  
  <sub>Benar: Untuk $x = 12$ jam: $\hat{y} = 28 - 2,5(12) = 28 - 30 = -2\%$.
Karena $x = 12$ berada di luar rentang pengamatan $2 \le x \le 8$, proses ini adalah ekstrapolasi.
Kadar air gabah secara fisik tidak mungkin bernilai negatif (kurang dari $0\%$), sehingga asumsi linearitas sudah tidak berlaku di luar rentang data pengamatan.</sub>
- B. Hasil prediksi adalah $-2\%$; nilai ini diperoleh melalui ekstrapolasi dan tetap dapat dipercaya penuh karena model memiliki gradien negatif.  
  <sub>Salah: Siswa menganggap ekstrapolasi selalu valid tanpa memperhatikan apakah nilai prediksi masuk akal dalam konteks nyata.</sub>
- C. Hasil prediksi adalah $2\%$; nilai ini realistis dan reliabel karena berada di dalam batas jangkauan kemampuan mesin pengering.  
  <sub>Salah: Siswa salah melakukan operasi aritmetika sehingga menghasilkan nilai positif dan salah menyimpulkan reliabilitasnya.</sub>
- D. Hasil prediksi adalah $-2\%$; nilai ini diperoleh melalui interpolasi dan sangat reliabel karena mengikuti garis regresi kuadrat terkecil.  
  <sub>Salah: Siswa salah mengidentifikasi ekstrapolasi sebagai interpolasi dan mengabaikan batasan nilai fisis kadar air.</sub>

**Pembahasan:** Langkah 1: Menghitung nilai prediksi variabel dependen untuk $x = 12$:
$\hat{y} = 28 - 2,5(12) = 28 - 30 = -2$.
Jadi, prediksi kadar air adalah $-2\%$.

Langkah 2: Menentukan jenis prediksi:
Rentang jangkauan data pengamatan adalah $2 \le x \le 8$ jam.
Karena nilai $x = 12$ berada di luar jangkauan data pengamatan ($12 > 8$), proses prediksi ini disebut sebagai **ekstrapolasi**.

Langkah 3: Mengevaluasi keabsahan konteks dan reliabilitas:
Kadar air suatu bahan secara fisis tidak mungkin bernilai negatif. Nilai $-2\%$ menunjukkan bahwa tren garis lurus tidak lagi berlaku jika pemanasan diteruskan melampaui rentang data asli (kadar air akan melambat penurunannya dan mendekati batas konstan tertentu, tidak terus turun secara linear hingga bernilai negatif).

Oleh karena itu, hasil prediksi adalah $-2\%$, merupakan proses ekstrapolasi, dan tidak realistis secara praktis.
**Acuan:** siswa — siswa hal.121

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11-b03-b-hard-bt01-012
*variasi (konteks) | C5 | 3 langkah | jenis: evaluasi reliabilitas ekstrapolasi*

Penelitian mengamati laju fotosintesis suatu jenis daun tanaman air terhadap suhu lingkungan ($x$, dalam $^{\circ}\text{C}$) pada rentang pengamatan $10 \le x \le 30$. Diperoleh model regresi linear $\hat{y} = 5 + 1,8x$, dengan $y$ menyatakan volume gas oksigen yang dihasilkan (mL/jam). Seorang asisten peneliti menggunakan model ini untuk memprediksi volume gas yang dihasilkan pada suhu $60^{\circ}\text{C}$.

Berapakah hasil prediksi volume oksigen pada suhu $60^{\circ}\text{C}$ dan bagaimana evaluasi yang tepat terhadap reliabilitas prediksi tersebut?

- A. $113\text{ mL/jam}$, dan prediksi reliabel asalkan lingkungan diberi cahaya yang cukup  
  <sub>Salah: Mengabaikan fakta biologis rusaknya enzim fotosintesis pada suhu ekstrem.</sub>
- **B. $113\text{ mL/jam}$, dan prediksi tidak reliabel karena ekstrapolasi mengabaikan denaturasi enzim pada suhu tinggi** ✅  
  <sub>Benar: Prediksi = 5 + 1,8(60) = 5 + 108 = 113 mL/jam. Karena 60 jauh di luar rentang data pengamatan (10-30), ini ekstrapolasi. Pada suhu 60 derajat Celsius enzim rusak (denaturasi), sehingga laju fotosintesis justru anjlok mendekati 0, membuat hasil prediksi linear sama sekali tidak reliabel.</sub>
- C. $113\text{ mL/jam}$, dan prediksi sangat reliabel karena nilai koefisien regresi bernilai positif  
  <sub>Salah: Menganggap ekstrapolasi selalu reliabel jika gradien positif.</sub>
- D. $108\text{ mL/jam}$, dan prediksi tidak reliabel karena merupakan proses interpolasi  
  <sub>Salah: Lupa menjumlahkan konstanta regresi dan salah mengenali ekstrapolasi sebagai interpolasi.</sub>

**Pembahasan:** 1. Perhitungan nilai prediksi:
$\hat{y} = 5 + 1,8(60) = 5 + 108 = 113\text{ mL/jam}$.

2. Evaluasi reliabilitas:
Nilai $x = 60^{\circ}\text{C}$ berada jauh di luar rentang data pengamatan ($10 \le x \le 30^{\circ}\text{C}$), sehingga proses ini merupakan ekstrapolasi. Secara saintifik/biologis, enzim tumbuhan mengalami denaturasi pada suhu tinggi (mendekati $60^{\circ}\text{C}$) sehingga fotosintesis terhenti. Oleh karena itu, model linear tidak lagi berlaku dan prediksi ini sama sekali tidak reliabel.
**Acuan:** siswa — siswa hal.122 Latihan 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11-b03-b-hard-bt01-013
*orisinal | C6 | 5 langkah | jenis: rekonstruksi nilai variabel terikat*

Suatu eksperimen menghasilkan $4$ pasangan data $(x_i, y_i)$ dengan model regresi kuadrat terkecil $\hat{y} = 4 + 1,5x$. Tiga titik data yang diketahui memiliki nilai $x$: $x_1 = 2$, $x_2 = 4$, $x_3 = 6$, dan $x_4 = 8$. Diketahui tiga nilai amatan variabel dependen pertama adalah $y_1 = 6$, $y_2 = 11$, dan $y_3 = 12$.

Berdasarkan karakteristik metode kuadrat terkecil (di mana total seluruh nilai residu bernilai nol), berapakah nilai amatan variabel dependen keempat ($y_4$)?

- A. $18$  
  <sub>Salah: Salah menghitung jumlah akumulasi residu sebelumnya menjadi -2.</sub>
- B. $16$  
  <sub>Salah: Hanya menghitung nilai prediksi y_hat_4 tanpa menambahkan nilai residu e_4.</sub>
- C. $15$  
  <sub>Salah: Keliru mengurangkan nilai residu (16 - 1 = 15).</sub>
- **D. $17$** ✅  
  <sub>Benar: Prediksi y_hat:
y_hat_1 = 4 + 1,5(2) = 7 -> e_1 = 6 - 7 = -1
y_hat_2 = 4 + 1,5(4) = 10 -> e_2 = 11 - 10 = +1
y_hat_3 = 4 + 1,5(6) = 13 -> e_3 = 12 - 13 = -1
Karena jumlah seluruh residu harus 0: e_1 + e_2 + e_3 + e_4 = 0 -> -1 + 1 - 1 + e_4 = 0 -> e_4 = +1.
Nilai prediksi keempat: y_hat_4 = 4 + 1,5(8) = 16.
Nilai amatan keempat: y_4 = y_hat_4 + e_4 = 16 + 1 = 17.</sub>

**Pembahasan:** Langkah 1: Hitung nilai prediksi $\hat{y}$ untuk tiap pengamatan:
- $\hat{y}_1 = 4 + 1,5(2) = 7$
- $\hat{y}_2 = 4 + 1,5(4) = 10$
- $\hat{y}_3 = 4 + 1,5(6) = 13$
- $\hat{y}_4 = 4 + 1,5(8) = 16$

Langkah 2: Hitung residu dari tiga data pertama ($e = y - \hat{y}$):
- $e_1 = 6 - 7 = -1$
- $e_2 = 11 - 10 = 1$
- $e_3 = 12 - 13 = -1$

Langkah 3: Gunakan sifat garis regresi kuadrat terkecil di mana $\sum e_i = 0$:
$$e_1 + e_2 + e_3 + e_4 = 0 \Rightarrow (-1) + 1 + (-1) + e_4 = 0 \Rightarrow e_4 = 1$$

Langkah 4: Tentukan nilai amatan $y_4$:
$$y_4 = \hat{y}_4 + e_4 = 16 + 1 = 17$$
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11-b03-b-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: analisis sifat residu kuadrat terkecil*

Sebuah penelitian mengumpulkan $5$ pasang data pengamatan $(x, y)$ dan menghasilkan persamaan garis regresi kuadrat terkecil $\hat{y} = 5 + 1,5x$. Diketahui empat nilai residu dari data pertama hingga keempat berturut-turut adalah $-2,4$; $1,6$; $-0,8$; dan $3,2$. Jika titik pengamatan kelima memiliki nilai $x = 12$, berapakah nilai aktual $y$ untuk pengamatan kelima tersebut?

- A. $19,8$  
  <sub>Salah: Siswa langsung mengurangkan nilai residu data keempat ($23 - 3,2$) ke nilai prediksi.</sub>
- B. $23,0$  
  <sub>Salah: Siswa mengabaikan keberadaan residu data kelima dan hanya menghitung nilai prediksi $\hat{y}$.</sub>
- C. $24,6$  
  <sub>Salah: Siswa salah tanda residu sehingga menjumlahkan residu positif $23 + 1,6$ bukannya $23 - 1,6$.</sub>
- **D. $21,4$** ✅  
  <sub>Benar: Pada metode kuadrat terkecil, jumlah seluruh residu adalah nol, sehingga $e_5 = -1,6$ dan $y = \hat{y} + e = 23 + (-1,6) = 21,4$.</sub>

**Pembahasan:** Pada garis regresi kuadrat terkecil, jumlah seluruh residu sama dengan nol:
$$\sum_{i=1}^5 e_i = 0$$
$$(-2,4) + 1,6 + (-0,8) + 3,2 + e_5 = 0$$
$$1,6 + e_5 = 0 \implies e_5 = -1,6$$

Untuk data kelima dengan $x_5 = 12$, nilai prediksinya adalah:
$$\hat{y}_5 = 5 + 1,5(12) = 5 + 18 = 23$$

Karena residu $e_5 = y_5 - \hat{y}_5$, maka nilai amatan aktual adalah:
$$y_5 = \hat{y}_5 + e_5 = 23 + (-1,6) = 21,4$$
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas11-b03-b-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: analisis perubahan titik data regresi*

Sebuah analisis regresi linear kuadrat terkecil dilakukan terhadap $4$ pasang data pengamatan. Awalnya diperoleh rata-rata $\bar{x} = 5$ dan $\bar{y} = 14$. Setelah diteliti kembali, terdapat kesalahan pencatatan: satu titik data yang awalnya tertulis $(x, y) = (4, 12)$ seharusnya bernilai $(8, 20)$. Titik koordinat manakah yang pasti dilalui oleh garis regresi linear yang baru setelah data tersebut diperbaiki?

- A. $(6, 14)$  
  <sub>Salah: Siswa hanya memperbaiki nilai variabel independen $x$ namun lupa mengoreksi nilai rata-rata variabel dependen $y$.</sub>
- **B. $(6, 16)$** ✅  
  <sub>Benar: Jumlah data baru menghasilkan rata-rata $\bar{x}_{\text{baru}} = 6$ dan $\bar{y}_{\text{baru}} = 16$, dan garis regresi pasti melewati $(\bar{x}, \bar{y})$.</sub>
- C. $(7, 18)$  
  <sub>Salah: Siswa langsung menambahkan data baru ke data lama tanpa mengurangkan data yang salah catat.</sub>
- D. $(5, 16)$  
  <sub>Salah: Siswa hanya memperbaiki nilai variabel dependen $y$ namun lupa mengoreksi nilai rata-rata variabel independen $x$.</sub>

**Pembahasan:** Garis regresi kuadrat terkecil selalu melewati titik koordinat rata-rata $(\bar{x}, \bar{y})$.

1. Hitung jumlah awal data untuk $n = 4$:
$$\sum x = 4 \times 5 = 20$$
$$\sum y = 4 \times 14 = 56$$

2. Koreksi jumlah nilai variabel dengan mengurangi nilai salah dan menambah nilai benar:
$$\sum x_{\text{baru}} = 20 - 4 + 8 = 24$$
$$\sum y_{\text{baru}} = 56 - 12 + 20 = 64$$

3. Hitung rata-rata baru:
$$\bar{x}_{\text{baru}} = \frac{24}{4} = 6$$
$$\bar{y}_{\text{baru}} = \frac{64}{4} = 16$$

Jadi, garis regresi baru pasti melewati titik koordinat rata-rata $(\bar{x}_{\text{baru}}, \bar{y}_{\text{baru}}) = (6, 16)$.
**Acuan:** siswa — siswa hal.113

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas11-b03-b-hard-bt01-016
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi kelayakan model regresi*

| Luas Stan ($x$, $\text{m}^2$) | Tarif Sewa ($y$, ratus ribu rupiah) |
|---|---|
| $10$ | $25$ |
| $20$ | $42$ |
| $30$ | $65$ |

Berdasarkan data pada tabel di atas, diajukan dua kandidat model regresi linear untuk memprediksi tarif sewa stan:
- Model A: $\hat{y} = 4 + 2x$
- Model B: $\hat{y} = 5 + 2x$

Berdasarkan kriteria metode kuadrat terkecil, manakah model yang lebih tepat dan berapakah selisih jumlah kuadrat residunya?

- A. Model B lebih tepat, dengan selisih jumlah kuadrat residu sebesar $1$  
  <sub>Salah: Siswa hanya menggunakan jumlah mutlak residu, bukan kuadrat residu.</sub>
- B. Model A lebih tepat, dengan selisih jumlah kuadrat residu sebesar $5$  
  <sub>Salah: Siswa salah menjumlahkan kuadrat residu Model B menjadi 11 bukannya 9.</sub>
- **C. Model A lebih tepat, dengan selisih jumlah kuadrat residu sebesar $3$** ✅  
  <sub>Benar: Model A menghasilkan jumlah kuadrat residu $6$, sedangkan Model B menghasilkan $9$; selisihnya adalah $9 - 6 = 3$, sehingga Model A lebih tepat.</sub>
- D. Model B lebih tepat, dengan selisih jumlah kuadrat residu sebesar $3$  
  <sub>Salah: Siswa keliru menganggap jumlah kuadrat residu yang lebih besar menandakan model yang lebih baik.</sub>

**Pembahasan:** Evaluasi kedua model menggunakan metode kuadrat terkecil:

1. Menghitung kuadrat residu untuk Model A ($\hat{y} = 4 + 2x$):
- $x = 10 \implies \hat{y} = 4 + 2(10) = 24$, residu $e_1 = 25 - 24 = 1 \implies e_1^2 = 1$
- $x = 20 \implies \hat{y} = 4 + 2(20) = 44$, residu $e_2 = 42 - 44 = -2 \implies e_2^2 = 4$
- $x = 30 \implies \hat{y} = 4 + 2(30) = 64$, residu $e_3 = 65 - 64 = 1 \implies e_3^2 = 1$
Jumlah kuadrat residu Model A: $SS_{\text{res(A)}} = 1 + 4 + 1 = 6$.

2. Menghitung kuadrat residu untuk Model B ($\hat{y} = 5 + 2x$):
- $x = 10 \implies \hat{y} = 5 + 2(10) = 25$, residu $e_1 = 25 - 25 = 0 \implies e_1^2 = 0$
- $x = 20 \implies \hat{y} = 5 + 2(20) = 45$, residu $e_2 = 42 - 45 = -3 \implies e_2^2 = 9$
- $x = 30 \implies \hat{y} = 5 + 2(30) = 65$, residu $e_3 = 65 - 65 = 0 \implies e_3^2 = 0$
Jumlah kuadrat residu Model B: $SS_{\text{res(B)}} = 0 + 9 + 0 = 9$.

3. Membandingkan kedua model:
Karena $SS_{\text{res(A)}} < SS_{\text{res(B)}}$ ($6 < 9$), maka Model A lebih tepat dengan selisih jumlah kuadrat residu sebesar $9 - 6 = 3$.
**Acuan:** pretest — kelas11-b03-p0117-latihan-33-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas11-b03-b-hard-bt01-017
*orisinal | C5 | 5 langkah | jenis: estimasi nilai hilang dan intersep*

| Data ke- | $x$ | $y$ |
|---|---|---|
| 1 | $2$ | $3$ |
| 2 | $4$ | $7$ |
| 3 | $6$ | $8$ |
| 4 | $8$ | $p$ |

Sebuah eksperimen menghasilkan $4$ pasangan data $(x, y)$ seperti tercantum pada tabel di atas. Jika diketahui bahwa garis regresi kuadrat terkecil dari data tersebut memiliki gradien kemiringan $b = 1,4$, maka nilai $p$ dan nilai intersep sumbu $y$ ($a$) dari persamaan regresi tersebut adalah...

- A. $p = 12$ dan $a = 1,4$  
  <sub>Salah: Siswa keliru menganggap nilai intersep sama dengan nilai kemiringan b.</sub>
- B. $p = 10$ dan $a = 1,0$  
  <sub>Salah: Siswa salah menghitung persamaan pembilang gradien sehingga memperoleh p = 10.</sub>
- **C. $p = 12$ dan $a = 0,5$** ✅  
  <sub>Benar: Nilai $SS_{xx} = 20$, $SS_{xy} = -8 + 3p$. Dari $b = SS_{xy}/SS_{xx} = 1,4$, diperoleh $p = 12$. Rata-rata $\bar{x} = 5$ dan $\bar{y} = 7,5$, sehingga $a = \bar{y} - b\bar{x} = 7,5 - 1,4(5) = 0,5$.</sub>
- D. $p = 14$ dan $a = -0,2$  
  <sub>Salah: Siswa salah menggunakan rumus jumlah kuadrat silang variabel.</sub>

**Pembahasan:** Langkah 1: Menghitung rata-rata variabel independen ($\bar{x}$):
$$\bar{x} = \frac{2 + 4 + 6 + 8}{4} = \frac{20}{4} = 5$$

Langkah 2: Menghitung $SS_{xx}$:
$$SS_{xx} = (2-5)^2 + (4-5)^2 + (6-5)^2 + (8-5)^2 = (-3)^2 + (-1)^2 + 1^2 + 3^2 = 9 + 1 + 1 + 9 = 20$$

Langkah 3: Menghitung $SS_{xy}$ dan mencari nilai $p$:
$$SS_{xy} = \sum_{i=1}^4 (x_i - \bar{x})y_i = (-3)(3) + (-1)(7) + (1)(8) + (3)(p) = -9 - 7 + 8 + 3p = -8 + 3p$$
Karena gradien $b = 1,4$:
$$b = \frac{SS_{xy}}{SS_{xx}} \implies 1,4 = \frac{-8 + 3p}{20}$$
$$-8 + 3p = 28 \implies 3p = 36 \implies p = 12$$

Langkah 4: Menghitung rata-rata variabel dependen ($\bar{y}$):
$$\bar{y} = \frac{3 + 7 + 8 + 12}{4} = \frac{30}{4} = 7,5$$

Langkah 5: Menghitung intersep $a$:
$$a = \bar{y} - b\bar{x} = 7,5 - (1,4)(5) = 7,5 - 7,0 = 0,5$$

Jadi, diperoleh nilai $p = 12$ dan $a = 0,5$.
**Acuan:** siswa — siswa hal.119

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas11-b03-b-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: analisis sifat residu dan total amatan*

Sebuah penelitian mengamati hubungan antara biaya promosi harian ($x$, dalam jutaan rupiah) dan omzet penjualan ($y$, dalam jutaan rupiah) di $5$ cabang toko ritel. Rata-rata biaya promosi dari kelima cabang tersebut adalah $\bar{x} = 8$ juta rupiah, dan model regresi kuadrat terkecil yang terbentuk adalah $\hat{y} = 10 + 2,5x$.

Dari $4$ cabang pertama, tercatat nilai residu berturut-turut adalah $e_1 = -3$, $e_2 = +2$, $e_3 = -1$, dan $e_4 = +4$. Jika cabang ke-5 mengeluarkan biaya promosi sebesar $x_5 = 12$ juta rupiah, berapakah omzet penjualan aktual ($y_5$) cabang ke-5 serta jumlah total omzet penjualan ($\sum_{i=1}^5 y_i$) dari seluruh kelima cabang tersebut?

- A. $y_5 = 40$ juta rupiah dan $\sum_{i=1}^5 y_i = 160$ juta rupiah  
  <sub>Salah: Siswa mengabaikan residu data ke-5 dan mengasumsikan nilai aktual sama dengan nilai prediksi garis regresi.</sub>
- B. $y_5 = 38$ juta rupiah dan $\sum_{i=1}^5 y_i = 140$ juta rupiah  
  <sub>Salah: Siswa salah mengalikan rata-rata dependen dengan n - 1 bukan n.</sub>
- C. $y_5 = 42$ juta rupiah dan $\sum_{i=1}^5 y_i = 150$ juta rupiah  
  <sub>Salah: Siswa salah menerapkan tanda residu menjadi e_5 = +2 sehingga y_5 = 40 + 2 = 42.</sub>
- **D. $y_5 = 38$ juta rupiah dan $\sum_{i=1}^5 y_i = 150$ juta rupiah** ✅  
  <sub>Benar: Jumlah residu kuadrat terkecil selalu nol sehingga $e_5 = -2$. Prediksi $\hat{y}_5 = 10 + 2,5(12) = 40$, maka $y_5 = 40 + (-2) = 38$. Titik rata-rata dilalui garis regresi sehingga $\bar{y} = 10 + 2,5(8) = 30$, menghasilkan total amatan $5 \times 30 = 150$.</sub>

**Pembahasan:** Langkah 1: Menggunakan sifat metode kuadrat terkecil bahwa jumlah seluruh residu adalah nol ($\sum_{i=1}^n e_i = 0$):
$$e_1 + e_2 + e_3 + e_4 + e_5 = 0$$
$$(-3) + 2 + (-1) + 4 + e_5 = 0$$
$$2 + e_5 = 0 \implies e_5 = -2$$

Langkah 2: Menghitung nilai prediksi ($\hat{y}_5$) untuk cabang ke-5 dengan $x_5 = 12$:
$$\hat{y}_5 = 10 + 2,5(12) = 10 + 30 = 40\text{ juta rupiah}$$

Langkah 3: Menghitung omzet aktual ($y_5$) cabang ke-5 menggunakan rumus residu $e_5 = y_5 - \hat{y}_5$:
$$y_5 = \hat{y}_5 + e_5 = 40 + (-2) = 38\text{ juta rupiah}$$

Langkah 4: Menghitung jumlah total omzet ($\sum_{i=1}^5 y_i$):
Garis regresi kuadrat terkecil selalu melalui titik $(\bar{x}, \bar{y})$. Oleh karena itu:
$$\bar{y} = 10 + 2,5\bar{x} = 10 + 2,5(8) = 10 + 20 = 30\text{ juta rupiah}$$
Jumlah seluruh nilai aktual variabel $y$ adalah:
$$\sum_{i=1}^5 y_i = n \times \bar{y} = 5 \times 30 = 150\text{ juta rupiah}$$

Jadi, diperoleh $y_5 = 38$ juta rupiah dan $\sum_{i=1}^5 y_i = 150$ juta rupiah.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
