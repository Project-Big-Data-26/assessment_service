# Lembar koreksi — kelas12_tl SMA12L-B4 subbab G: Distribusi Normal

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b04-g-easy-bt01-001
*variasi (konteks) | C2 | 2 langkah | jenis: Peluang distribusi normal kumulatif*

Masa pakai sebuah komponen elektronik berdistribusi normal dengan rata-rata 1.000 jam dan simpangan baku 100 jam. Jika diketahui nilai $P(Z < -2,0) = 0,0228$, berapakah peluang sebuah komponen bertahan kurang dari 800 jam?

- **A. 0,0228** ✅  
  <sub>Benar: Skor baku dihitung dengan $z = \frac{x - \mu}{\sigma} = \frac{800 - 1.000}{100} = -2,0$. Peluangnya adalah $P(Z < -2,0) = 0,0228$.</sub>
- B. 0,4772  
  <sub>Salah: Siswa mengurangkan peluang kumulatif dengan luas separuh kurva $0,9772 - 0,5$ alih-alih mengambil luas ekor kiri.</sub>
- C. 0,9772  
  <sub>Salah: Siswa menggunakan skor $z = 2,0$ positif atau menghitung $P(Z > -2,0) = 1 - 0,0228$.</sub>
- D. 0,0456  
  <sub>Salah: Siswa menduplikasi nilai ekor kiri dengan mengalikan 2 (mengira luas dua sisi simetris).</sub>

**Pembahasan:** Diketahui $\mu = 1.000$ dan $\sigma = 100$.
Hitung nilai skor baku untuk $x = 800$:
$$z = \frac{x - \mu}{\sigma} = \frac{800 - 1.000}{100} = \frac{-200}{100} = -2,0$$
Maka peluangnya adalah:
$$P(X < 800) = P(Z < -2,0) = 0,0228$$
**Acuan:** pretest — kelas12_tl-b04-p0292-latihan-soal-distribusi-normal-2a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b04-g-easy-bt01-002
*variasi (angka) | C1 | 1 langkah | jenis: Nilai harapan distribusi normal*

Sebaran normal memiliki rata-rata $\mu = 75$ dan simpangan baku $\sigma = 12$. Tentukan nilai harapan $E(X)$ bahwa $X$ mengambil sebuah nilai 68.

- A. 12  
  <sub>Salah: Siswa salah mengira nilai harapan adalah simpangan baku sebaran.</sub>
- B. 87  
  <sub>Salah: Siswa menjumlahkan rata-rata dengan simpangan baku ($75 + 12$).</sub>
- **C. 75** ✅  
  <sub>Benar: Nilai harapan dari variabel acak berdistribusi normal $X$ selalu sama dengan rata-ratanya, yaitu $E(X) = \mu = 75$.</sub>
- D. 68  
  <sub>Salah: Siswa terkecoh menganggap nilai harapan sama dengan nilai observasi $x$ yang ditanyakan.</sub>

**Pembahasan:** Berdasarkan sifat distribusi normal, nilai harapan dari variabel acak kontinu berdistribusi normal selalu sama dengan rata-ratanya:
$$E(X) = \mu$$
Karena diketahui $\mu = 75$, maka nilai harapan bahwa $X$ mengambil nilai 68 adalah 75.
**Acuan:** siswa — siswa hal.290 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b04-g-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: Peluang interval distribusi normal*

Masa pakai lampu pijar berdistribusi normal dengan rata-rata 500 jam dan simpangan baku 50 jam. Jika diketahui peluang kumulatif $P(Z < 2,0) = 0,9772$ dan $P(Z < 0) = 0,5000$, tentukan peluang sebuah lampu padam antara 500 jam dan 600 jam.

- A. 0,0228  
  <sub>Salah: Siswa menghitung peluang ekor kanan $1 - 0,9772$.</sub>
- B. 0,5000  
  <sub>Salah: Siswa hanya menggunakan nilai peluang kumulatif pada titik rata-rata.</sub>
- C. 0,9772  
  <sub>Salah: Siswa hanya mengambil nilai peluang kumulatif di batas atas tanpa mengurangkan batas bawah.</sub>
- **D. 0,4772** ✅  
  <sub>Benar: Batas diubah ke skor baku: $z_1 = 0$ dan $z_2 = 2,0$. Peluang intervalnya adalah $P(0 < Z < 2,0) = 0,9772 - 0,5000 = 0,4772$.</sub>

**Pembahasan:** Konversikan kedua batas ke nilai $z$:
$$z_1 = \frac{500 - 500}{50} = 0$$
$$z_2 = \frac{600 - 500}{50} = \frac{100}{50} = 2,0$$
Peluang interval dihitung dengan selisih peluang kumulatif:
$$P(500 < X < 600) = P(0 < Z < 2,0) = P(Z < 2,0) - P(Z < 0) = 0,9772 - 0,5000 = 0,4772$$
**Acuan:** pretest — kelas12_tl-b04-p0292-latihan-soal-distribusi-normal-3a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b04-g-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: Karakteristik distribusi normal baku*

Distribusi normal umum dapat ditransformasikan ke dalam distribusi normal standar (baku). Manakah pasangan nilai rata-rata ($\mu$) dan simpangan baku ($\sigma$) yang mendefinisikan distribusi normal standar tersebut?

- A. $\mu = 1$ dan $\sigma = 1$  
  <sub>Salah: Siswa mengira kedua parameter pada bentuk satuan bernilai satu.</sub>
- **B. $\mu = 0$ dan $\sigma = 1$** ✅  
  <sub>Benar: Berdasarkan definisi pada buku teks, distribusi normal standar adalah distribusi normal yang memiliki rata-rata $\mu = 0$ dan simpangan baku $\sigma = 1$.</sub>
- C. $\mu = 0$ dan $\sigma = 0$  
  <sub>Salah: Siswa mengira kedua parameter pada bentuk standar harus bernilai nol.</sub>
- D. $\mu = 1$ dan $\sigma = 0$  
  <sub>Salah: Siswa terbalik antara nilai rata-rata dan simpangan baku.</sub>

**Pembahasan:** Distribusi normal baku (standar) didefinisikan secara khusus dengan parameter rata-rata $\mu = 0$ dan simpangan baku $\sigma = 1$.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b04-g-easy-bt01-005
*orisinal | C1 | 1 langkah | jenis: Sifat kurva distribusi normal*

Kurva distribusi normal berbentuk lonceng simetris terhadap sumbu vertikal yang melalui rata-rata ($\mu$). Jika luas total seluruh daerah di bawah kurva normal sama dengan 1, berapakah luas daerah di bawah kurva yang berada di sebelah kanan garis rata-rata $\mu$?

- A. 0,25  
  <sub>Salah: Siswa membagi kurva menjadi empat kuadran sehingga bernilai 0,25.</sub>
- B. 1,0  
  <sub>Salah: Siswa menyebut luas total seluruh daerah di bawah kurva normal.</sub>
- **C. 0,5** ✅  
  <sub>Benar: Karena luas total sama dengan 1 dan kurva simetris terhadap garis tengah $\mu$, luas di sebelah kanan garis tengah adalah separuh luas total, yaitu 0,5.</sub>
- D. 0  
  <sub>Salah: Siswa mengacaukan luas daerah dengan nilai titik tengah pada distribusi standar.</sub>

**Pembahasan:** Kurva distribusi normal bersifat simetris terhadap garis rata-ratanya $\mu$. Karena luas total di bawah kurva adalah 1, garis rata-rata membagi kurva menjadi dua bagian yang sama besar, sehingga luas di sebelah kanan (maupun kiri) $\mu$ adalah $\frac{1}{2} = 0,5$.
**Acuan:** siswa — siswa hal.285

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b04-g-easy-bt01-006
*variasi (angka) | C2 | 1 langkah | jenis: Nilai harapan distribusi normal*

Berat badan bayi yang baru lahir di sebuah rumah sakit berdistribusi normal dengan rata-rata 3.200 gram dan simpangan baku 180 gram. Nilai harapan dari berat badan bayi lahir tersebut adalah ....

- **A. 3.200 gram** ✅  
  <sub>Benar: Berdasarkan sifat distribusi normal, nilai harapan suatu variabel acak normal $X$ selalu sama dengan rata-ratanya, yaitu $E(X) = \mu = 3.200$ gram.</sub>
- B. 3.020 gram  
  <sub>Salah: Mengurangkan simpangan baku dari rata-rata ($\mu - \sigma$).</sub>
- C. 3.380 gram  
  <sub>Salah: Menjumlahkan rata-rata dengan simpangan baku ($\mu + \sigma$).</sub>
- D. 180 gram  
  <sub>Salah: Mengira nilai harapan sama dengan nilai simpangan baku ($\sigma$).</sub>

**Pembahasan:** Distribusi normal memiliki sifat bahwa nilai harapan variabel acak $X$ adalah nilai rata-ratanya, yaitu $E(X) = \mu$. Diketahui rata-rata $\mu = 3.200$ gram, sehingga nilai harapan bayi lahir tersebut adalah $3.200$ gram.
**Acuan:** siswa — siswa hal.291 Ayo Mencoba 4.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b04-g-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: Peluang interval distribusi normal*

Diketahui nilai peluang distribusi normal baku $P(Z < -1,0) = 0,1587$ dan $P(Z < 1,0) = 0,8413$.

Berat badan siswa suatu kelas berdistribusi normal dengan rata-rata 54 kg dan simpangan baku 6 kg. Peluang seorang siswa yang dipilih secara acak memiliki berat badan antara 48 kg dan 60 kg adalah ....

- A. 0,3413  
  <sub>Salah: Hanya menghitung luas separuh interval dari 0 hingga 1 ($0,8413 - 0,5000$).</sub>
- B. 0,5000  
  <sub>Salah: Mengasumsikan peluang simetris selalu bernilai tepat setengah kurva.</sub>
- **C. 0,6826** ✅  
  <sub>Benar: Skor baku untuk $x_1 = 48$ adalah $z_1 = \frac{48-54}{6} = -1,0$ dan untuk $x_2 = 60$ adalah $z_2 = \frac{60-54}{6} = 1,0$. Peluangnya adalah $P(Z < 1,0) - P(Z < -1,0) = 0,8413 - 0,1587 = 0,6826$.</sub>
- D. 1,0000  
  <sub>Salah: Menjumlahkan kedua nilai peluang kumulatif secara keliru ($0,8413 + 0,1587$).</sub>

**Pembahasan:** Transformasi ke skor baku $Z$:
$z_1 = \frac{48 - 54}{6} = -1,0$
$z_2 = \frac{60 - 54}{6} = 1,0$
Maka:
$P(48 < X < 60) = P(-1,0 < Z < 1,0) = P(Z < 1,0) - P(Z < -1,0) = 0,8413 - 0,1587 = 0,6826$.
**Acuan:** pretest — kelas12_tl-b04-p0292-latihan-soal-distribusi-normal-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b04-g-easy-bt01-008
*variasi (angka) | C1 | 1 langkah | jenis: Nilai harapan distribusi normal*

Sebuah mesin pemotong memproduksi pipa baja dengan panjang berdistribusi normal memiliki rata-rata 450 cm dan simpangan baku 15 cm. Nilai harapan dari panjang pipa baja hasil produksi mesin tersebut adalah ....

- A. 15 cm  
  <sub>Salah: Menjawab dengan parameter simpangan baku ($\sigma$).</sub>
- B. 30 cm  
  <sub>Salah: Mengalikan simpangan baku dengan dua ($2\sigma$).</sub>
- **C. 450 cm** ✅  
  <sub>Benar: Nilai harapan distribusi normal $E(X)$ setara dengan parameter rata-rata $\mu$, sehingga $E(X) = 450$ cm.</sub>
- D. 225 cm  
  <sub>Salah: Membagi nilai rata-rata dengan dua.</sub>

**Pembahasan:** Pada distribusi normal $N(\mu, \sigma^2)$, nilai harapan ditentukan oleh rumus $E(X) = \mu$. Karena rata-rata panjang pipa adalah $450$ cm, maka nilai harapannya adalah $450$ cm.
**Acuan:** siswa — siswa hal.292 Latihan Soal Distribusi Normal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b04-g-easy-bt01-009
*orisinal | C2 | 1 langkah | jenis: Transformasi nilai baku Z*

Suatu variabel acak $X$ berdistribusi normal dengan rata-rata $\mu = 70$ dan simpangan baku $\sigma = 8$. Nilai baku ($Z$) yang bersesuaian dengan $X = 86$ adalah ....

- A. -2,0  
  <sub>Salah: Terbalik dalam pengurangan pada pembilang $(\mu - X) / \sigma = (70 - 86) / 8$.</sub>
- B. 16,0  
  <sub>Salah: Hanya menghitung selisih pembilang $86 - 70 = 16$ tanpa membagi dengan simpangan baku.</sub>
- C. 1,5  
  <sub>Salah: Salah melakukan pengurangan $86 - 70 = 12$, lalu $12 / 8 = 1,5$.</sub>
- **D. 2,0** ✅  
  <sub>Benar: Menggunakan rumus transformasi $Z = \frac{X - \mu}{\sigma} = \frac{86 - 70}{8} = \frac{16}{8} = 2,0$.</sub>

**Pembahasan:** Rumus transformasi nilai baku adalah:
$$Z = \frac{X - \mu}{\sigma}$$
Substitusikan nilai yang diketahui:
$$Z = \frac{86 - 70}{8} = \frac{16}{8} = 2,0$$.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b04-g-easy-bt01-010
*orisinal | C1 | 1 langkah | jenis: Karakteristik kurva distribusi normal*

Sebuah fungsi distribusi normal memiliki nilai rata-rata $\mu = 85$ dan simpangan baku $\sigma = 10$. Kurva fungsi densitas distribusi normal tersebut mencapai nilai maksimum (modus) pada titik absis $x = ....$

- A. 95  
  <sub>Salah: Menghitung absis titik belok kurva di sebelah kanan ($x = \mu + \sigma$).</sub>
- B. 10  
  <sub>Salah: Menyebutkan nilai simpangan baku ($\sigma$).</sub>
- **C. 85** ✅  
  <sub>Benar: Fungsi densitas kurva normal simetris berbentuk lonceng dan mencapai puncak tertinggi (maksimum/modus) di titik $x = \mu = 85$.</sub>
- D. 0  
  <sub>Salah: Tertukar dengan titik pusat rata-rata pada kurva normal baku standar.</sub>

**Pembahasan:** Berdasarkan sifat-sifat kurva normal, titik pada sumbu horizontal yang menyebabkan fungsi densitas peluang bernilai maksimum (modus kurva) terjadi tepat pada nilai rata-ratanya, yaitu $x = \mu$. Karena $\mu = 85$, kurva mencapai maksimum pada $x = 85$.
**Acuan:** siswa — siswa hal.283

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b04-g-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: Peluang distribusi normal kumulatif*

Masa pakai baterai sebuah sensor pemantau cuaca berdistribusi normal dengan umur rata-rata 50 bulan dan simpangan baku 6 bulan. Jika diketahui nilai dari tabel normal baku $P(Z < -1,5) = 0,0668$, tentukan peluang bahwa baterai tersebut akan bertahan kurang dari 41 bulan.

- **A. 0,0668** ✅  
  <sub>Benar: Nilai Z dihitung dengan $Z = \frac{41 - 50}{6} = -1,5$, sehingga peluangnya adalah $P(Z < -1,5) = 0,0668$.</sub>
- B. 0,1336  
  <sub>Salah: Siswa mengalikan nilai peluang dengan 2 karena menganggap kurva simetris di dua sisi.</sub>
- C. 0,4332  
  <sub>Salah: Siswa mengurangkan nilai dari 0,5 yaitu $0,5 - 0,0668$ karena keliru membaca batas titik tengah kurva.</sub>
- D. 0,9332  
  <sub>Salah: Siswa menghitung komplemen $1 - 0,0668$ seolah-olah mencari peluang bertahan lebih dari 41 bulan.</sub>

**Pembahasan:** Diketahui $\mu = 50$ bulan, $\sigma = 6$ bulan, dan $X = 41$ bulan.

Transformasikan nilai $X$ ke nilai baku $Z$:
$$Z = \frac{X - \mu}{\sigma} = \frac{41 - 50}{6} = \frac{-9}{6} = -1,5$$

Peluang baterai bertahan kurang dari 41 bulan adalah:
$$P(X < 41) = P(Z < -1,5) = 0,0668$$
**Acuan:** pretest — kelas12_tl-b04-p0292-latihan-soal-distribusi-normal-2a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b04-g-easy-bt01-012
*variasi (konteks) | C1 | 1 langkah | jenis: Nilai harapan distribusi normal*

Masa simpan suatu jenis bibit tanaman berdistribusi normal dengan rata-rata 48 bulan dan simpangan baku 6 bulan. Nilai harapan dari masa simpan bibit tanaman tersebut adalah ....

- A. 54 bulan  
  <sub>Salah: Siswa menjumlahkan rata-rata dengan simpangan baku ($48 + 6$).</sub>
- **B. 48 bulan** ✅  
  <sub>Benar: Pada distribusi normal, nilai harapan selalu sama dengan nilai rata-rata distribusinya, yaitu $E(X) = \mu = 48$ bulan.</sub>
- C. 42 bulan  
  <sub>Salah: Siswa mengurangkan rata-rata dengan satu kali simpangan baku ($48 - 6$).</sub>
- D. 6 bulan  
  <sub>Salah: Siswa keliru menganggap simpangan baku sebagai nilai harapan.</sub>

**Pembahasan:** Berdasarkan sifat nilai harapan pada distribusi normal:
$$E(X) = \mu$$

Diketahui rata-rata $\mu = 48$ bulan. Maka nilai harapan dari masa simpan bibit tanaman tersebut adalah 48 bulan.
**Acuan:** siswa — siswa hal.292 Latihan Soal Distribusi Normal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b04-g-easy-bt01-013
*variasi (angka) | C2 | 2 langkah | jenis: Peluang interval distribusi normal*

Sebuah mesin pengisi minuman menghasilkan volume cairan berdistribusi normal dengan rata-rata 600 ml dan simpangan baku 50 ml. Jika diketahui nilai peluang kumulatif $P(Z < 0) = 0,5000$ dan $P(Z < 1,5) = 0,9332$, tentukan peluang sebuah kemasan terisi antara 600 ml dan 675 ml.

- A. 0,5668  
  <sub>Salah: Siswa melakukan operasi $1,5 - 0,9332$ karena salah memahami konsep peluang.</sub>
- **B. 0,4332** ✅  
  <sub>Benar: $P(0 < Z < 1,5) = P(Z < 1,5) - P(Z < 0) = 0,9332 - 0,5000 = 0,4332$.</sub>
- C. 0,0668  
  <sub>Salah: Siswa menghitung daerah ekor kanan dengan rumus $1 - 0,9332$.</sub>
- D. 0,9332  
  <sub>Salah: Siswa langsung mengambil nilai kumulatif $P(Z < 1,5)$ tanpa mengurangkan daerah di bawah rata-rata.</sub>

**Pembahasan:** Diketahui $\mu = 600$ ml dan $\sigma = 50$ ml.

Konversikan batas $X_1 = 600$ dan $X_2 = 675$ ke nilai Z:
$$Z_1 = \frac{600 - 600}{50} = 0$$
$$Z_2 = \frac{675 - 600}{50} = \frac{75}{50} = 1,5$$

Maka peluangnya adalah:
$$P(600 < X < 675) = P(0 < Z < 1,5) = P(Z < 1,5) - P(Z < 0)$$
$$P(0 < Z < 1,5) = 0,9332 - 0,5000 = 0,4332$$
**Acuan:** pretest — kelas12_tl-b04-p0292-latihan-soal-distribusi-normal-3a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b04-g-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: Sifat kurva distribusi normal*

Sebuah variabel acak kontinu berdistribusi normal memiliki rata-rata $\mu = 40$ dan simpangan baku $\sigma = 5$. Titik belok kurva distribusi normal tersebut berada pada nilai $x$ sama dengan ....

- **A. 35 dan 45** ✅  
  <sub>Benar: Titik belok kurva normal berada di $x = \mu \pm \sigma$, yaitu $40 - 5 = 35$ dan $40 + 5 = 45$.</sub>
- B. 25 dan 55  
  <sub>Salah: Siswa menggunakan formula $\mu \pm 3\sigma$ ($40 \pm 15$).</sub>
- C. 30 dan 50  
  <sub>Salah: Siswa menggunakan formula $\mu \pm 2\sigma$ ($40 \pm 10$).</sub>
- D. 40 saja  
  <sub>Salah: Siswa menyamakan titik belok dengan titik puncak atau modus ($x = \mu$).</sub>

**Pembahasan:** Berdasarkan sifat-sifat kurva normal, titik belok kurva fungsi distribusi normal terjadi tepat pada absis:
$$x = \mu \pm \sigma$$

Dengan $\mu = 40$ dan $\sigma = 5$:
$$x_1 = 40 - 5 = 35$$
$$x_2 = 40 + 5 = 45$$

Jadi, titik belok kurva berada pada $x = 35$ dan $x = 45$.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b04-g-easy-bt01-015
*orisinal | C2 | 1 langkah | jenis: Bentuk kurva distribusi normal*

Dua buah kurva distribusi normal $A$ dan $B$ memiliki nilai rata-rata yang sama, yaitu $\mu_A = \mu_B = 50$, tetapi simpangan bakunya berbeda dengan $\sigma_A = 4$ dan $\sigma_B = 10$. Pernyataan yang benar mengenai bentuk kurva $A$ dibandingkan dengan kurva $B$ adalah ....

- A. puncak kurva A berada di sebelah kiri puncak kurva B  
  <sub>Salah: Siswa mengira simpangan baku memengaruhi posisi horizontal titik puncak.</sub>
- B. kurva A lebih lebar dan lebih datar dibandingkan kurva B  
  <sub>Salah: Siswa mengira nilai simpangan baku yang lebih kecil menghasilkan kurva yang lebih datar.</sub>
- C. luas total daerah di bawah kurva A lebih kecil dari kurva B  
  <sub>Salah: Siswa mengira luas total kurva dipengaruhi oleh simpangan baku, padahal luas total selalu sama dengan 1.</sub>
- **D. kurva A lebih sempit dan lebih tinggi dibandingkan kurva B** ✅  
  <sub>Benar: Semakin kecil nilai simpangan baku $\sigma$, kurva akan semakin sempit dan puncaknya semakin tinggi (leptokurtik).</sub>

**Pembahasan:** Parameter simpangan baku ($\sigma$) menentukan sebaran data terhadap nilai rata-rata kurva normal:
1. Semakin kecil nilai $\sigma$, kurva tampak semakin sempit dan puncaknya semakin tinggi (leptokurtik).
2. Semakin besar nilai $\sigma$, kurva tampak semakin lebar dan mendatar (platikurtik).

Karena $\sigma_A = 4 < \sigma_B = 10$, maka kurva $A$ memiliki bentuk yang lebih sempit dan lebih tinggi dibandingkan kurva $B$.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b04-g-easy-bt01-016
*variasi (angka) | C1 | 1 langkah | jenis: Nilai harapan sebaran normal*

Sebuah mesin pemanas air memiliki umur pakai yang berdistribusi normal dengan rata-rata 8 tahun dan standar deviasi 1,5 tahun. Tentukan nilai harapan umur pakai mesin pemanas air tersebut.

- A. 1,5 tahun  
  <sub>Salah: Siswa keliru menganggap nilai harapan sama dengan nilai standar deviasi.</sub>
- **B. 8 tahun** ✅  
  <sub>Benar: Pada distribusi normal, nilai harapan selalu sama dengan nilai rata-ratanya, yaitu $E(X) = \mu = 8$ tahun.</sub>
- C. 6,5 tahun  
  <sub>Salah: Siswa keliru mengurangkan nilai rata-rata dengan standar deviasi ($8 - 1,5$).</sub>
- D. 9,5 tahun  
  <sub>Salah: Siswa keliru menjumlahkan nilai rata-rata dengan standar deviasi ($8 + 1,5$).</sub>

**Pembahasan:** Berdasarkan sifat distribusi normal, nilai harapan dari suatu variabel acak normal $X$ dengan rata-rata $\mu$ dan simpangan baku $\sigma$ dirumuskan sebagai:
$$E(X) = \mu$$
Diketahui $\mu = 8$ tahun dan $\sigma = 1,5$ tahun, sehingga:
$$E(X) = 8\text{ tahun}$$
**Acuan:** siswa — siswa hal.292 Latihan Soal Distribusi Normal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b04-g-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: Peluang interval sebaran normal*

Sebuah variabel acak $X$ berdistribusi normal memiliki rata-rata $\mu = 100$ dan simpangan baku $\sigma = 20$. Tentukan nilai peluang $P(100 < X < 128)$ jika diketahui nilai kumulatif $P(Z < 0) = 0,5000$ dan $P(Z < 1,4) = 0,9192$.

- A. 0,0808  
  <sub>Salah: Siswa menghitung komplemen $1 - 0,9192$ alih-alih menghitung luas interval di antara kedua batas.</sub>
- B. 0,9192  
  <sub>Salah: Siswa langsung mengambil nilai $P(Z < 1,4)$ tanpa mengurangkan dengan $P(Z < 0)$.</sub>
- C. 0,5808  
  <sub>Salah: Siswa salah menjumlahkan $1 - 0,4192$.</sub>
- **D. 0,4192** ✅  
  <sub>Benar: Nilai Z untuk 100 adalah 0 dan untuk 128 adalah 1,4, sehingga peluangnya $0,9192 - 0,5000 = 0,4192$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai baku $Z$ untuk masing-masing batas:
$$Z_1 = \frac{100 - 100}{20} = 0$$
$$Z_2 = \frac{128 - 100}{20} = \frac{28}{20} = 1,4$$

Langkah 2: Menghitung selisih peluang kumulatif:
$$P(100 < X < 128) = P(0 < Z < 1,4) = P(Z < 1,4) - P(Z < 0)$$
$$P(100 < X < 128) = 0,9192 - 0,5000 = 0,4192$$
**Acuan:** siswa — siswa hal.285 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b04-g-easy-bt01-018
*variasi (angka) | C1 | 1 langkah | jenis: Nilai harapan teoritis normal*

Nilai tes fisika suatu angkatan berdistribusi normal dengan rata-rata 6,8 dan standar deviasi 1,4. Berdasarkan model distribusi tersebut, tentukan nilai harapan siswa mencapai nilai 8,2.

- **A. 6,8** ✅  
  <sub>Benar: Nilai harapan dari variabel acak yang berdistribusi normal adalah rata-rata distribusinya itu sendiri ($E(X) = \mu = 6,8$).</sub>
- B. 1,0  
  <sub>Salah: Siswa menghitung skor baku $Z = \frac{8,2 - 6,8}{1,4} = 1,0$ alih-alih nilai harapan.</sub>
- C. 8,2  
  <sub>Salah: Siswa terkecoh memilih nilai batas pencapaian yang disebutkan pada soal.</sub>
- D. 1,4  
  <sub>Salah: Siswa keliru menganggap nilai harapan adalah nilai standar deviasi.</sub>

**Pembahasan:** Pada distribusi normal $X \sim N(\mu, \sigma^2)$, nilai harapan untuk sebaran data selalu sama dengan rata-rata populasi:
$$E(X) = \mu$$
Karena rata-rata yang diberikan adalah $\mu = 6,8$, maka nilai harapan siswa mencapai nilai 8,2 tetap bernilai 6,8.
**Acuan:** siswa — siswa hal.291 Ayo Mencoba 4.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b04-g-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: Asimtot kurva distribusi normal*

Manakah pernyataan yang paling tepat mengenai perilaku ujung-ujung grafik fungsi distribusi normal saat nilai $x$ bergerak menjauhi rata-rata?

- A. Mencapai nilai nol dan bernilai negatif saat nilai $x$ sangat kecil  
  <sub>Salah: Siswa keliru menganggap fungsi densitas dapat memotong sumbu mendatar menjadi negatif.</sub>
- **B. Mendekati sumbu horizontal sebagai asimtot ke arah kiri dan kanan tanpa pernah memotongnya** ✅  
  <sub>Benar: Sifat kurva normal menyatakan kedua ujung kurva mendekati asimtot sumbu horizontal (sumbu-X) ketika nilai x menjauhi rata-rata ke kiri maupun ke kanan.</sub>
- C. Memotong sumbu horizontal tepat pada jarak tiga kali simpangan baku dari rata-rata  
  <sub>Salah: Siswa keliru mengira kurva berhenti dan memotong sumbu mendatar pada batas $\mu \pm 3\sigma$.</sub>
- D. Mendekati sumbu vertikal yang melalui rata-rata sebagai garis asimtot tegak  
  <sub>Salah: Siswa keliru membedakan garis sumbu simetri vertikal dengan garis asimtot kurva.</sub>

**Pembahasan:** Berdasarkan sifat-sifat kurva normal, kurva berbentuk lonceng simetris dan kedua ujung ekor kurva mendekati asimtot sumbu horizontal (sumbu mendatar) secara asimtotik ketika nilai $x$ bergerak menjauhi rata-rata baik ke arah kiri maupun ke arah kanan, namun tidak akan pernah memotong atau menyentuh sumbu tersebut.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b04-g-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: Titik puncak kurva normal*

Sebuah variabel acak kontinu $X$ berdistribusi normal dengan rata-rata $\mu = 54$ dan simpangan baku $\sigma = 6$. Kurva fungsi densitas distribusi normal tersebut mencapai nilai puncak maksimum (modus) pada titik absis $x$ sama dengan ....

- A. 6  
  <sub>Salah: Siswa memilih nilai simpangan baku $\sigma$ alih-alih rata-rata.</sub>
- B. 48  
  <sub>Salah: Siswa memilih titik belok kiri kurva, yaitu $\mu - \sigma = 54 - 6 = 48$.</sub>
- C. 60  
  <sub>Salah: Siswa memilih titik belok kanan kurva, yaitu $\mu + \sigma = 54 + 6 = 60$.</sub>
- **D. 54** ✅  
  <sub>Benar: Puncak kurva normal (modus) terjadi tepat pada nilai rata-ratanya, yaitu $x = \mu = 54$.</sub>

**Pembahasan:** Salah satu sifat utama kurva distribusi normal adalah kurva mencapai nilai fungsi tertinggi (titik puncak atau modus) tepat pada titik rata-ratanya di sumbu horizontal, yaitu $x = \mu$.
Karena $\mu = 54$, maka kurva mencapai nilai maksimum pada $x = 54$.
**Acuan:** siswa — siswa hal.283

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b04-g-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: sistem persamaan parameter distribusi*

Dua orang siswa mengikuti ujian kemampuan akademik yang nilainya berdistribusi normal. Mereka masing-masing memperoleh skor baku ($Z$) sebesar $1,5$ dan $0,5$. Jika skor mentah kedua siswa tersebut berturut-turut adalah $85$ dan $65$, maka nilai rata-rata ($\mu$) dan simpangan baku ($\sigma$) dari skor ujian tersebut berturut-turut adalah ....

- A. $\mu = 50$ dan $\sigma = 20$  
  <sub>Salah: Siswa salah melakukan substitusi dengan mengurangkan $0,5 \times 20$ dari $60$ bukan dari $65$.</sub>
- B. $\mu = 55$ dan $\sigma = 10$  
  <sub>Salah: Siswa salah saat membagi selisih skor dengan selisih z, menghitung $(85 - 65) / (1,5 + 0,5) = 20 / 2 = 10$.</sub>
- C. $\mu = 75$ dan $\sigma = 20$  
  <sub>Salah: Siswa salah menerapkan tanda aljabar dengan menjumlahkan alih-alih mengurangkan: $\mu = 65 + 0,5(20) = 75$.</sub>
- **D. $\mu = 55$ dan $\sigma = 20$** ✅  
  <sub>Benar: Dari $Z = \frac{X - \mu}{\sigma}$, diperoleh $85 - \mu = 1,5\sigma$ dan $65 - \mu = 0,5\sigma$. Pengurangan kedua persamaan menghasilkan $20 = 1,0\sigma \Rightarrow \sigma = 20$. Substitusi nilai $\sigma$ memberikan $\mu = 65 - 0,5(20) = 55$.</sub>

**Pembahasan:** Diketahui hubungan skor mentah $X$ dan nilai baku $Z$ adalah:
$$Z = \frac{X - \mu}{\sigma} \iff X = \mu + Z\sigma$$

Untuk siswa pertama:
$$85 = \mu + 1,5\sigma \quad \text{...(1)}$$

Untuk siswa kedua:
$$65 = \mu + 0,5\sigma \quad \text{...(2)}$$

Kurangkan persamaan (1) dengan persamaan (2):
$$(85 - 65) = (1,5\sigma - 0,5\sigma)$$
$$20 = 1,0\sigma \implies \sigma = 20$$

Substitusikan $\sigma = 20$ ke persamaan (2):
$$65 = \mu + 0,5(20)$$
$$65 = \mu + 10 \implies \mu = 55$$

Jadi, rata-rata skor adalah $\mu = 55$ dan simpangan bakunya adalah $\sigma = 20$.
**Acuan:** siswa — siswa hal.293 Latihan Soal Distribusi Normal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b04-g-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: peluang variabel normal selang tertutup*

Sebuah pabrik pengolahan buah mengemas mangga ke dalam kotak kardus. Bobot buah mangga berdistribusi normal dengan rata-rata $400$ gram dan simpangan baku $50$ gram. Buah yang memenuhi standar mutu supermarket adalah buah dengan bobot antara $325$ gram dan $480$ gram. Jika diketahui $P(Z < -1,50) = 0,0668$ dan $P(Z < 1,60) = 0,9452$, tentukan peluang sebutir mangga yang dipilih secara acak memenuhi standar mutu supermarket.

- A. $0,8780$  
  <sub>Salah: Siswa melakukan kesalahan hitung pengurangan pada digit terakhir desimal.</sub>
- B. $0,0120$  
  <sub>Salah: Siswa mengurangkan $1 - (0,9452 + 0,0668)$ karena keliru menerapkan aturan komplemen gabungan.</sub>
- **C. $0,8784$** ✅  
  <sub>Benar: $Z_1 = \frac{325-400}{50} = -1,50$ dan $Z_2 = \frac{480-400}{50} = 1,60$. Peluangnya adalah $P(Z < 1,60) - P(Z < -1,50) = 0,9452 - 0,0668 = 0,8784$.</sub>
- D. $0,9452$  
  <sub>Salah: Siswa hanya mengambil nilai peluang kumulatif batas atas tanpa mengurangkan batas bawah.</sub>

**Pembahasan:** Tentukan terlebih dahulu nilai baku $Z$ untuk masing-masing batas:
$$Z_1 = \frac{325 - 400}{50} = \frac{-75}{50} = -1,50$$
$$Z_2 = \frac{480 - 400}{50} = \frac{80}{50} = 1,60$$

Peluang bobot mangga antara $325$ gram dan $480$ gram dihitung dengan:
$$P(325 < X < 480) = P(-1,50 < Z < 1,60)$$
$$P(-1,50 < Z < 1,60) = P(Z < 1,60) - P(Z < -1,50)$$
$$= 0,9452 - 0,0668 = 0,8784$$

Jadi, peluang sebutir mangga memenuhi standar mutu supermarket adalah $0,8784$.
**Acuan:** pretest — kelas12_tl-b04-p0292-latihan-soal-distribusi-normal-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b04-g-medium-bt01-003
*orisinal | C4 | 3 langkah | jenis: inversi distribusi normal*

Waktu pengiriman paket kilat oleh suatu ekspedisi berdistribusi normal dengan simpangan baku $12$ jam. Berdasarkan rekapitulasi data pengiriman, sebanyak $10,56\%$ paket membutuhkan waktu pengiriman lebih dari $55$ jam. Berdasarkan tabel distribusi normal baku kumulatif, nilai yang memenuhi $P(Z < 1,25) = 0,8944$. Rata-rata waktu pengiriman paket tersebut adalah ....

- **A. $40$ jam** ✅  
  <sub>Benar: $P(X > 55) = 0,1056 \iff P(X < 55) = 0,8944$, yang berpadanan dengan $Z = 1,25$. Maka $55 = \mu + 1,25(12) = \mu + 15 \implies \mu = 40$.</sub>
- B. $35$ jam  
  <sub>Salah: Siswa salah mengalikan simpangan baku dengan $1,25$, menghasilkan $20$ lalu menghitung $55 - 20 = 35$.</sub>
- C. $45$ jam  
  <sub>Salah: Siswa keliru menggunakan nilai $Z = 0,83$ (dari $1 - 0,1056 \approx 0,90$) sehingga perkiraan rata-rata menjadi $45$ jam.</sub>
- D. $70$ jam  
  <sub>Salah: Siswa salah menggunakan rumus $X = \mu - Z\sigma$ sehingga diperoleh $\mu = 55 + 15 = 70$ jam.</sub>

**Pembahasan:** Diketahui:
- $\sigma = 12$
- $P(X > 55) = 10,56\% = 0,1056$

Maka peluang kumulatif di sebelah kiri batas adalah:
$$P(X < 55) = 1 - 0,1056 = 0,8944$$

Dari informasi tabel, luas di sebelah kiri $Z$ sebesar $0,8944$ bersesuaian dengan $Z = 1,25$.

Gunakan transformasi nilai baku:
$$Z = \frac{X - \mu}{\sigma}$$
$$1,25 = \frac{55 - \mu}{12}$$
$$1,25 \times 12 = 55 - \mu$$
$$15 = 55 - \mu$$
$$\mu = 55 - 15 = 40$$

Jadi, rata-rata waktu pengiriman paket tersebut adalah $40$ jam.
**Acuan:** siswa — siswa hal.292

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b04-g-medium-bt01-004
*orisinal | C4 | 3 langkah | jenis: analisis kecekungan kurva normal*

Suatu variabel acak kontinu $X$ memiliki fungsi distribusi normal dengan nilai rata-rata $\mu = 80$ dan varians $\sigma^2 = 144$. Kurva fungsi densitas peluang distribusi normal tersebut akan cekung ke bawah (cekung di bagian bawah) pada interval nilai $x$ ....

- **A. $68 < x < 92$** ✅  
  <sub>Benar: Simpangan baku $\sigma = \sqrt{144} = 12$. Sifat kurva normal menyatakan cekung ke bawah pada rentang $\mu - \sigma < x < \mu + \sigma$, yaitu $80 - 12 < x < 80 + 12 \iff 68 < x < 92$.</sub>
- B. $-64 < x < 224$  
  <sub>Salah: Siswa tidak mengakar varians dan langsung memakai varians sebagai simpangan baku: $80 \pm 144$.</sub>
- C. $56 < x < 104$  
  <sub>Salah: Siswa menggunakan interval $\mu \pm 2\sigma = 80 \pm 24$ alih-alih $\mu \pm \sigma$.</sub>
- D. $x < 68$ atau $x > 92$  
  <sub>Salah: Siswa tertukar dengan kondisi kurva cekung ke atas.</sub>

**Pembahasan:** Berdasarkan sifat distribusi normal pada buku teks:
1. Titik belok kurva normal terjadi pada $x = \mu \pm \sigma$.
2. Kurva cekung ke bawah apabila $\mu - \sigma < x < \mu + \sigma$, dan cekung ke atas untuk nilai $x$ lainnya.

Diketahui:
- $\mu = 80$
- Varians $\sigma^2 = 144 \implies \sigma = \sqrt{144} = 12$

Maka kurva cekung ke bawah pada interval:
$$\mu - \sigma < x < \mu + \sigma$$
$$80 - 12 < x < 80 + 12$$
$$68 < x < 92$$

Jadi, kurva cekung ke bawah pada rentang $68 < x < 92$.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b04-g-medium-bt01-005
*orisinal | C3 | 3 langkah | jenis: frekuensi harapan variabel normal*

Sebuah perusahaan menyelenggarakan uji seleksi kompetensi dasar bagi $1.500$ peserta. Nilai ujian berdistribusi normal dengan rata-rata $72$ dan simpangan baku $8$. Peserta yang memperoleh nilai di bawah $60$ dinyatakan tidak memenuhi kriteria minimal dan langsung gugur. Berdasarkan tabel distribusi normal baku, diketahui $P(Z < -1,50) = 0,0668$. Perkiraan banyaknya peserta yang gugur adalah ....

- A. $67$ orang  
  <sub>Salah: Siswa salah mengalikan $0,0668$ dengan $1.000$ (bukan $1.500$), menghasilkan sekitar $67$ orang.</sub>
- B. $135$ orang  
  <sub>Salah: Siswa salah membagi nilai z sebagai $-1,0$ sehingga menggunakan peluang $0,09$ atau salah operasi hitung.</sub>
- **C. $100$ orang** ✅  
  <sub>Benar: Batas gugur adalah $X < 60$. Nilai $Z = \frac{60 - 72}{8} = -1,50$. Peluangnya adalah $P(Z < -1,50) = 0,0668$. Frekuensi harapan peserta yang gugur $= 0,0668 \times 1.500 = 100,2 \approx 100$ orang.</sub>
- D. $1.400$ orang  
  <sub>Salah: Siswa menghitung banyaknya peserta yang lolos: $(1 - 0,0668) \times 1.500 \approx 1.400$ orang.</sub>

**Pembahasan:** Langkah 1: Menghitung nilai baku $Z$ untuk batas kelulusan $X = 60$:
$$Z = \frac{X - \mu}{\sigma} = \frac{60 - 72}{8} = \frac{-12}{8} = -1,50$$

Langkah 2: Menentukan peluang peserta memperoleh nilai di bawah $60$:
$$P(X < 60) = P(Z < -1,50) = 0,0668$$

Langkah 3: Menghitung frekuensi harapan peserta yang gugur dari total $1.500$ orang:
$$\text{Banyaknya peserta} = P(X < 60) \times N = 0,0668 \times 1.500 = 100,2 \approx 100\text{ orang}$$

Jadi, perkiraan banyaknya peserta yang gugur adalah $100$ orang.
**Acuan:** siswa — siswa hal.293

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b04-g-medium-bt01-006
*variasi (konteks) | C3 | 2 langkah | jenis: peluang kumulatif ekor kiri*

Tabel distribusi normal baku menunjukkan bahwa $P(Z < -1,75) = 0,0401$ dan $P(Z < 1,75) = 0,9599$.

Masa pakai ban sepeda motor jenis tertentu berdistribusi normal dengan rata-rata $24$ bulan dan standar deviasi $4$ bulan. Berdasarkan data stimulus, berapakah peluang bahwa sebuah ban yang dipilih secara acak akan bertahan kurang dari $17$ bulan?

- A. $0,0802$  
  <sub>Salah: Mengalikan peluang ekor dengan dua.</sub>
- **B. $0,0401$** ✅  
  <sub>Benar: Menghitung $Z = \frac{17 - 24}{4} = -1,75$, sehingga $P(X < 17) = P(Z < -1,75) = 0,0401$.</sub>
- C. $0,9599$  
  <sub>Salah: Mengabaikan tanda minus pada nilai Z dan mengambil nilai kumulatif Z positif.</sub>
- D. $0,4599$  
  <sub>Salah: Mengurangkan nilai peluang kumulatif dari 0,5.</sub>

**Pembahasan:** Diketahui $\mu = 24$ dan $\sigma = 4$.
Transformasi ke nilai baku $Z$ untuk $X = 17$:
$$Z = \frac{X - \mu}{\sigma} = \frac{17 - 24}{4} = -1,75$$
Peluang ban bertahan kurang dari $17$ bulan adalah:
$$P(X < 17) = P(Z < -1,75) = 0,0401$$
Jadi, peluangnya adalah $0,0401$.
**Acuan:** pretest — kelas12_tl-b04-p0292-latihan-soal-distribusi-normal-2a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b04-g-medium-bt01-007
*variasi (konteks) | C3 | 3 langkah | jenis: peluang variabel normal selang interval*

Diketahui nilai kumulatif distribusi normal baku $P(Z < -1,30) = 0,0968$ dan $P(Z < 2,10) = 0,9821$.

Kadar gula darah puasa sekelompok pasien berdistribusi normal dengan rata-rata $95\text{ mg/dL}$ dan simpangan baku $10\text{ mg/dL}$. Tentukan peluang seorang pasien yang dipilih secara acak memiliki kadar gula darah antara $82\text{ mg/dL}$ dan $116\text{ mg/dL}$.

- **A. $0,8853$** ✅  
  <sub>Benar: Menghitung selisih peluang kumulatif $P(Z < 2,10) - P(Z < -1,30) = 0,9821 - 0,0968 = 0,8853$.</sub>
- B. $1,0789$  
  <sub>Salah: Menjumlahkan kedua nilai kumulatif, bukan mengurangkannya.</sub>
- C. $0,8885$  
  <sub>Salah: Keliru dalam operasi hitung pengurangan desimal.</sub>
- D. $0,4821$  
  <sub>Salah: Hanya mengurangkan nilai kumulatif batas atas dengan $0,5$.</sub>

**Pembahasan:** Diketahui $\mu = 95$ dan $\sigma = 10$.
Hitung nilai $Z$ untuk kedua batas:
$$Z_1 = \frac{82 - 95}{10} = -1,30$$
$$Z_2 = \frac{116 - 95}{10} = 2,10$$
Peluang kadar gula darah antara $82\text{ mg/dL}$ dan $116\text{ mg/dL}$:
$$P(82 < X < 116) = P(-1,30 < Z < 2,10) = P(Z < 2,10) - P(Z < -1,30)$$
$$P(82 < X < 116) = 0,9821 - 0,0968 = 0,8853$$
Jadi, peluangnya adalah $0,8853$.
**Acuan:** pretest — kelas12_tl-b04-p0292-latihan-soal-distribusi-normal-3a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b04-g-medium-bt01-008
*variasi (konteks) | C3 | 3 langkah | jenis: persentase populasi ekor kanan*

Diketahui bahwa nilai peluang kumulatif pada kurva normal baku adalah $P(Z < 1,80) = 0,9641$.

Sebuah mesin pengisi kemasan minyak goreng diatur untuk mengeluarkan minyak dengan volume rata-rata $500\text{ ml}$ per kemasan dan simpangan baku $20\text{ ml}$ yang berdistribusi normal. Tentukan persentase kemasan minyak goreng yang berisi lebih dari $536\text{ ml}$.

- A. $96,41\%$  
  <sub>Salah: Lupa mengurangkan dari 1 untuk peluang 'lebih dari', langsung menggunakan peluang kumulatif.</sub>
- B. $0,36\%$  
  <sub>Salah: Salah melakukan pergeseran desimal saat mengubah pecahan desimal ke persentase.</sub>
- **C. $3,59\%$** ✅  
  <sub>Benar: Menghitung $P(Z > 1,80) = 1 - 0,9641 = 0,0359 = 3,59\%$.</sub>
- D. $46,41\%$  
  <sub>Salah: Mengurangkan nilai kumulatif dengan 0,5 alih-alih mengurangkannya dari 1.</sub>

**Pembahasan:** Diketahui $\mu = 500$ dan $\sigma = 20$.
Hitung nilai $Z$ untuk $X = 536$:
$$Z = \frac{536 - 500}{20} = \frac{36}{20} = 1,80$$
Peluang kemasan berisi lebih dari $536\text{ ml}$:
$$P(X > 536) = P(Z > 1,80) = 1 - P(Z < 1,80) = 1 - 0,9641 = 0,0359$$
Dalam bentuk persentase:
$$0,0359 \times 100\% = 3,59\%$$
Jadi, persentasenya adalah $3,59\%$.
**Acuan:** siswa — siswa hal.292 Latihan Soal Distribusi Normal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b04-g-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: penentuan simpangan baku distribusi normal*

Berdasarkan tabel distribusi normal baku, diperoleh nilai $P(Z < -2,0) = 0,0228$.

Berat bersih kemasan kopi bubuk berdistribusi normal dengan rata-rata $\mu = 250\text{ gram}$. Berdasarkan pemeriksaan mutu, sebanyak $2,28\%$ kemasan kopi memiliki berat kurang dari $234\text{ gram}$. Berapakah nilai simpangan baku ($\sigma$) dari berat kemasan kopi tersebut?

- A. $16\text{ gram}$  
  <sub>Salah: Hanya menghitung selisih $|234 - 250|$ tanpa membagi dengan nilai mutlak Z.</sub>
- B. $32\text{ gram}$  
  <sub>Salah: Mengalikan selisih data dengan nilai mutlak Z alih-alih membaginya.</sub>
- **C. $8\text{ gram}$** ✅  
  <sub>Benar: Dari $P(X < 234) = 0,0228$ diperoleh $Z = -2,0$. Melalui $-2,0 = \frac{234 - 250}{\sigma}$, didapat $\sigma = 8\text{ gram}$.</sub>
- D. $4\text{ gram}$  
  <sub>Salah: Membagi selisih dengan kuadrat nilai Z atau salah operasi aljabar.</sub>

**Pembahasan:** Diketahui $\mu = 250$ dan $P(X < 234) = 2,28\% = 0,0228$.
Berdasarkan tabel normal baku, peluang kumulatif $0,0228$ bersesuaian dengan $Z = -2,0$.
Substitusikan nilai ke dalam rumus nilai baku:
$$Z = \frac{X - \mu}{\sigma}$$
$$-2,0 = \frac{234 - 250}{\sigma}$$
$$-2,0 = \frac{-16}{\sigma}$$
$$\sigma = \frac{-16}{-2,0} = 8\text{ gram}$$
Jadi, nilai simpangan bakunya adalah $8\text{ gram}$.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b04-g-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: peluang gabungan daerah ekor kurva normal*

Diketahui bahwa nilai peluang kumulatif distribusi normal baku untuk $Z = -2,0$ adalah $P(Z < -2,0) = 0,0228$.

Sebuah pabrik baut memproduksi baut dengan diameter berdistribusi normal dengan rata-rata $10\text{ mm}$ dan simpangan baku $0,2\text{ mm}$. Baut dinyatakan cacat jika diameternya kurang dari $9,6\text{ mm}$ atau lebih dari $10,4\text{ mm}$. Berapakah peluang sebuah baut yang dipilih secara acak tergolong cacat?

- **A. $0,0456$** ✅  
  <sub>Benar: Menjumlahkan peluang kedua ekor simetris: $P(X < 9,6) + P(X > 10,4) = 0,0228 + 0,0228 = 0,0456$.</sub>
- B. $0,9544$  
  <sub>Salah: Menghitung peluang komplemen (peluang baut tidak cacat/memenuhi standar).</sub>
- C. $0,4772$  
  <sub>Salah: Menghitung selisih antara nilai tengah dan luas ekor ($0,5 - 0,0228$).</sub>
- D. $0,0228$  
  <sub>Salah: Hanya menghitung peluang salah satu sisi ekor saja.</sub>

**Pembahasan:** Diketahui $\mu = 10\text{ mm}$ dan $\sigma = 0,2\text{ mm}$.
Hitung nilai $Z$ untuk kedua batas spesifikasi:
$$Z_1 = \frac{9,6 - 10}{0,2} = -2,0$$
$$Z_2 = \frac{10,4 - 10}{0,2} = 2,0$$
Baut dinyatakan cacat jika $X < 9,6$ atau $X > 10,4$.
Peluang baut berdiameter kurang dari $9,6\text{ mm}$ adalah:
$$P(X < 9,6) = P(Z < -2,0) = 0,0228$$
Karena kurva berdistribusi normal simetris di sekitar rata-rata:
$$P(X > 10,4) = P(Z > 2,0) = P(Z < -2,0) = 0,0228$$
Maka peluang total ditemukannya baut cacat adalah:
$$P(\text{cacat}) = P(X < 9,6) + P(X > 10,4) = 0,0228 + 0,0228 = 0,0456$$
Jadi, peluang baut tergolong cacat adalah $0,0456$.
**Acuan:** siswa — siswa hal.285

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b04-g-medium-bt01-011
*variasi (angka) | C3 | 3 langkah | jenis: persentase daerah ekor kurva normal*

Tabel distribusi normal baku memberikan nilai $P(Z < 2,00) = 0,9772$.

Tinggi rata-rata suatu jenis tanaman hias adalah $50\text{ cm}$ dengan standar deviasi $6\text{ cm}$ dan berdistribusi normal. Tentukan persentase tanaman hias tersebut yang memiliki tinggi lebih dari $62\text{ cm}$.

- A. $47,72\%$  
  <sub>Salah: Mengurangkan nilai tabel dengan 0,5 bukannya mengurangkan dari 1.</sub>
- B. $97,72\%$  
  <sub>Salah: Mengambil langsung luas daerah di sebelah kiri batas $P(Z < 2,00)$ tanpa mengurangkannya dari 1.</sub>
- C. $4,56\%$  
  <sub>Salah: Menghitung luas dua sisi kurva (mengalikan dua hasil daerah ekor kanan).</sub>
- **D. $2,28\%$** ✅  
  <sub>Benar: Menghitung nilai baku $Z = \frac{62 - 50}{6} = 2,00$, kemudian peluang lebih dari adalah $P(Z > 2,00) = 1 - 0,9772 = 0,0228 = 2,28\%$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai standar $Z$ untuk $x = 62$:
$$Z = \frac{x - \mu}{\sigma} = \frac{62 - 50}{6} = \frac{12}{6} = 2,00$$

Langkah 2: Menentukan peluang nilai lebih dari $62\text{ cm}$:
$$P(X > 62) = P(Z > 2,00) = 1 - P(Z < 2,00) = 1 - 0,9772 = 0,0228$$

Langkah 3: Mengubah peluang ke dalam bentuk persentase:
$$0,0228 \times 100\% = 2,28\%$$
**Acuan:** siswa — siswa hal.292 Latihan Soal Distribusi Normal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b04-g-medium-bt01-012
*variasi (angka) | C3 | 3 langkah | jenis: peluang variabel normal selang simetris*

Diketahui data tabel distribusi normal baku: $P(Z < -1,50) = 0,0668$ dan $P(Z < 1,50) = 0,9332$.

Rata-rata jarak tempuh armada bus antarkota adalah $4.000\text{ km}$ per bulan dengan standar deviasi $800\text{ km}$ dan mengikuti sebaran normal. Tentukan peluang sebuah armada bus menempuh jarak antara $2.800\text{ km}$ dan $5.200\text{ km}$ dalam satu bulan.

- A. $0,8000$  
  <sub>Salah: Membagi selisih batas jarak dengan standar deviasi $((5.200 - 2.800) / 3.000)$ secara keliru.</sub>
- B. $0,4332$  
  <sub>Salah: Hanya menghitung luas daerah dari rata-rata ke salah satu batas ($0,9332 - 0,5000$).</sub>
- **C. $0,8664$** ✅  
  <sub>Benar: Menghitung $Z_1 = \frac{2.800 - 4.000}{800} = -1,50$ dan $Z_2 = \frac{5.200 - 4.000}{800} = 1,50$, lalu $P(-1,50 < Z < 1,50) = 0,9332 - 0,0668 = 0,8664$.</sub>
- D. $0,9332$  
  <sub>Salah: Hanya mengambil luas kumulatif hingga batas atas tanpa mengurangi luas di bawah batas bawah.</sub>

**Pembahasan:** Langkah 1: Menghitung nilai baku untuk kedua batas:
$$Z_1 = \frac{2.800 - 4.000}{800} = \frac{-1.200}{800} = -1,50$$
$$Z_2 = \frac{5.200 - 4.000}{800} = \frac{1.200}{800} = 1,50$$

Langkah 2: Menghitung selisih peluang kumulatif:
$$P(2.800 < X < 5.200) = P(-1,50 < Z < 1,50) = P(Z < 1,50) - P(Z < -1,50)$$
$$P(-1,50 < Z < 1,50) = 0,9332 - 0,0668 = 0,8664$$
**Acuan:** siswa — siswa hal.294 Uji Kompetensi Bab 4 B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b04-g-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: penentuan parameter dari titik belok*

Grafik fungsi densitas distribusi normal dari suatu variabel acak kontinu $X$ memiliki titik belok di $x = 42$ dan $x = 58$. Tentukan nilai varians ($\sigma^2$) dari distribusi normal tersebut.

- A. $8$  
  <sub>Salah: Hanya menghitung nilai simpangan baku $\sigma$ dan lupa menguadratkannya untuk memperoleh varians.</sub>
- **B. $64$** ✅  
  <sub>Benar: Titik belok berada pada $\mu \pm \sigma$. Selisih kedua titik belok adalah $2\sigma = 58 - 42 = 16 \Rightarrow \sigma = 8$, sehingga varians $\sigma^2 = 8^2 = 64$.</sub>
- C. $50$  
  <sub>Salah: Menghitung titik tengah atau nilai rata-rata $\mu = \frac{42 + 58}{2} = 50$.</sub>
- D. $16$  
  <sub>Salah: Menganggap jarak kedua titik belok ($2\sigma = 16$) sebagai nilai varians.</sub>

**Pembahasan:** Langkah 1: Mengetahui bahwa titik belok kurva normal terletak pada $x = \mu - \sigma$ dan $x = \mu + \sigma$.

Langkah 2: Menghitung simpangan baku $\sigma$ dari jarak antar-titik belok:
$$(\mu + \sigma) - (\mu - \sigma) = 58 - 42$$
$$2\sigma = 16 \iff \sigma = 8$$

Langkah 3: Menghitung nilai varians ($\sigma^2$):
$$\sigma^2 = 8^2 = 64$$
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b04-g-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: ambang batas persentil distribusi normal*

Tabel distribusi normal baku menunjukkan bahwa $P(Z < -1,00) = 0,1587$.

Nilai ujian suatu mata kuliah berdistribusi normal dengan rata-rata $68$ dan simpangan baku $12$. Jika $15,87\%$ peserta dengan nilai terendah diwajibkan mengikuti ujian remidi, batas nilai maksimal peserta yang wajib mengikuti remidi adalah ....

- A. $80$  
  <sub>Salah: Menggunakan nilai $Z = +1,00$ sehingga menjumlahkan simpangan baku ke rata-rata.</sub>
- **B. $56$** ✅  
  <sub>Benar: Peluang $15,87\% = 0,1587$ bersesuaian dengan $Z = -1,00$. Nilai batas adalah $x = \mu + Z\sigma = 68 + (-1,00)(12) = 56$.</sub>
- C. $44$  
  <sub>Salah: Mengurangkan dua kali simpangan baku ($Z = -2,00$).</sub>
- D. $52$  
  <sub>Salah: Salah memperkirakan nilai baku menjadi $Z = -1,33$ sehingga mengurangkan $16$ dari rata-rata.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai baku $Z$ yang luas di sebelah kirinya sebesar $15,87\% = 0,1587$:
Berdasarkan data stimulus, $P(Z < -1,00) = 0,1587$, maka $Z = -1,00$.

Langkah 2: Menghubungkan skor baku $Z$ dengan nilai asal $x$:
$$Z = \frac{x - \mu}{\sigma}$$
$$-1,00 = \frac{x - 68}{12}$$

Langkah 3: Menghitung nilai $x$:
$$x - 68 = -1,00 \times 12 = -12$$
$$x = 68 - 12 = 56$$
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b04-g-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: perbandingan nilai baku variabel normal*

Dua orang siswa, Andi dan Budi, mengikuti tes kemampuan akademik pada kelompok yang berbeda. Nilai kelompok Andi berdistribusi normal dengan rata-rata $70$ dan simpangan baku $5$. Nilai kelompok Budi berdistribusi normal dengan rata-rata $75$ dan simpangan baku $6$. Jika Andi memperoleh skor $80$ dan Budi memperoleh skor $84$, selisih nilai standar baku ($Z$) antara Andi dan Budi adalah ....

- A. $4,00$  
  <sub>Salah: Hanya menghitung selisih skor mentah $(84 - 80 = 4)$ tanpa melakukan standardisasi.</sub>
- **B. $0,50$** ✅  
  <sub>Benar: Skor baku Andi adalah $Z_A = \frac{80 - 70}{5} = 2,00$. Skor baku Budi adalah $Z_B = \frac{84 - 75}{6} = 1,50$. Selisihnya adalah $|2,00 - 1,50| = 0,50$.</sub>
- C. $1,00$  
  <sub>Salah: Menghitung selisih simpangan baku $(6 - 5 = 1)$ kedua kelompok tes.</sub>
- D. $0,33$  
  <sub>Salah: Salah membagi selisih skor terhadap simpangan baku kelompok Budi $((84 - 75)/6 - (80 - 75)/6)$.</sub>

**Pembahasan:** Langkah 1: Menghitung nilai baku ($Z$) untuk Andi:
$$Z_A = \frac{x_A - \mu_A}{\sigma_A} = \frac{80 - 70}{5} = \frac{10}{5} = 2,00$$

Langkah 2: Menghitung nilai baku ($Z$) untuk Budi:
$$Z_B = \frac{x_B - \mu_B}{\sigma_B} = \frac{84 - 75}{6} = \frac{9}{6} = 1,50$$

Langkah 3: Menghitung selisih nilai standar baku keduanya:
$$\text{Selisih} = |Z_A - Z_B| = |2,00 - 1,50| = 0,50$$
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b04-g-medium-bt01-016
*variasi (angka) | C3 | 3 langkah | jenis: estimasi jumlah subjek populasi normal*

Tabel distribusi normal baku menunjukkan nilai kumulatif $P(Z < -2,00) = 0,0228$.

Sebanyak $2.500$ orang pelamar mengikuti tes seleksi kerja yang nilainya berdistribusi normal dengan rata-rata $75$ dan simpangan baku $10$. Jika perusahaan menetapkan batas nilai kelulusan minimal $55$, berapakah perkiraan banyak pelamar yang ditolak karena tidak memenuhi kriteria tersebut?

- A. $48$ orang  
  <sub>Salah: Keliru mengambil nilai peluang $P(Z < -2,07) = 0,0192$ dari tabel normal baku sehingga $2.500 \times 0,0192 = 48$.</sub>
- B. $71$ orang  
  <sub>Salah: Keliru menggunakan nilai peluang $P(Z < -1,90) = 0,0287$ sehingga memperoleh $2.500 \times 0,0287 \approx 71$.</sub>
- C. $114$ orang  
  <sub>Salah: Mengalikan peluang dua arah ekor simetris ($2 \times 0,0228 = 0,0456$) dengan jumlah total pelamar.</sub>
- **D. $57$ orang** ✅  
  <sub>Benar: Skor baku dihitung dengan $Z = \frac{55 - 75}{10} = -2,00$. Peluang nilai di bawah standar adalah $P(Z < -2,00) = 0,0228$. Banyak pelamar yang ditolak adalah $2.500 \times 0,0228 = 57$ orang.</sub>

**Pembahasan:** Nilai batas penolakan adalah $X < 55$. Transformasi ke nilai baku:
$$Z = \frac{X - \mu}{\sigma} = \frac{55 - 75}{10} = -2,00$$
Berdasarkan tabel distribusi normal, peluang seorang pelamar mendapat nilai di bawah $55$ adalah:
$$P(X < 55) = P(Z < -2,00) = 0,0228$$
Banyak pelamar yang diperkirakan tidak lulus seleksi:
$$N = 2.500 \times 0,0228 = 57\text{ orang}$$
**Acuan:** siswa — siswa hal.292 Latihan Soal Distribusi Normal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b04-g-medium-bt01-017
*variasi (angka) | C3 | 3 langkah | jenis: persentase melebihi ambang batas*

Tabel distribusi normal baku menunjukkan bahwa $P(Z < 1,30) = 0,9032$.

Sebuah mesin pengisi cairan otomatis diatur untuk mengisi botol dengan volume rata-rata $250\text{ ml}$ dan simpangan baku $20\text{ ml}$. Jika distribusi volume cairan menyebar normal, berapa persentase botol yang berisi lebih dari $276\text{ ml}$?

- **A. $9,68\%$** ✅  
  <sub>Benar: Nilai baku $Z = \frac{276 - 250}{20} = 1,30$. Peluang lebih dari $276\text{ ml}$ adalah $P(Z > 1,30) = 1 - 0,9032 = 0,0968 = 9,68\%$.</sub>
- B. $9,03\%$  
  <sub>Salah: Kesalahan pembulatan atau pergeseran desimal dari angka desimal $0,9032$.</sub>
- C. $90,32\%$  
  <sub>Salah: Langsung menggunakan nilai tabel kumulatif $P(Z < 1,30)$ tanpa mengurangkan dari $1$.</sub>
- D. $8,08\%$  
  <sub>Salah: Keliru membaca nilai tabel untuk $Z = 1,40$ yang bernilai $0,9192$ sehingga menghitung $1 - 0,9192 = 0,0808$.</sub>

**Pembahasan:** Hitung nilai baku ($Z$) untuk $X = 276$:
$$Z = \frac{X - \mu}{\sigma} = \frac{276 - 250}{20} = \frac{26}{20} = 1,30$$
Peluang volume lebih dari $276\text{ ml}$ dihitung melalui komplemen luas kurva:
$$P(X > 276) = P(Z > 1,30) = 1 - P(Z < 1,30)$$
$$P(X > 276) = 1 - 0,9032 = 0,0968$$
Dalam bentuk persentase:
$$0,0968 \times 100\% = 9,68\%$$
**Acuan:** siswa — siswa hal.292 Latihan Soal Distribusi Normal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b04-g-medium-bt01-018
*variasi (konteks) | C3 | 3 langkah | jenis: peluang selang interval variabel kontinu*

Tabel distribusi normal baku memberikan nilai $P(Z < -1,80) = 0,0359$ dan $P(Z < 1,20) = 0,8849$.

Sebuah pabrik beras mengemas beras dengan berat bersih berdistribusi normal memiliki rata-rata $25\text{ kg}$ dan simpangan baku $0,5\text{ kg}$. Tentukan peluang sebuah karung beras yang dipilih secara acak memiliki berat antara $24,1\text{ kg}$ dan $25,6\text{ kg}$.

- A. $0,8489$  
  <sub>Salah: Kesalahan hitung selisih desimal pada digit terakhir ($0,8849 - 0,0360$).</sub>
- B. $0,1151$  
  <sub>Salah: Mengurangkan nilai $P(Z < 1,20)$ dari $1$ ($1 - 0,8849$) sehingga hanya menghitung luas ekor kanan.</sub>
- C. $0,9208$  
  <sub>Salah: Menjumlahkan kedua nilai peluang kumulatif alih-alih mengurangkannya ($0,8849 + 0,0359$).</sub>
- **D. $0,8490$** ✅  
  <sub>Benar: Nilai baku batas bawah $Z_1 = \frac{24,1 - 25}{0,5} = -1,80$ dan batas atas $Z_2 = \frac{25,6 - 25}{0,5} = 1,20$. Peluang interval adalah $P(Z < 1,20) - P(Z < -1,80) = 0,8849 - 0,0359 = 0,8490$.</sub>

**Pembahasan:** Standarisasi nilai batas bawah dan batas atas:
$$Z_1 = \frac{24,1 - 25}{0,5} = \frac{-0,9}{0,5} = -1,80$$
$$Z_2 = \frac{25,6 - 25}{0,5} = \frac{0,6}{0,5} = 1,20$$
Peluang berat karung berada di antara kedua batas tersebut:
$$P(24,1 < X < 25,6) = P(-1,80 < Z < 1,20)$$
$$P(-1,80 < Z < 1,20) = P(Z < 1,20) - P(Z < -1,80)$$
$$P(-1,80 < Z < 1,20) = 0,8849 - 0,0359 = 0,8490$$
**Acuan:** pretest — kelas12_tl-b04-p0292-latihan-soal-distribusi-normal-3a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b04-g-medium-bt01-019
*orisinal | C3 | 2 langkah | jenis: rekonstruksi nilai variabel dari skor baku*

Nilai hasil tes potensi akademik suatu angkatan berdistribusi normal dengan rata-rata $\mu = 520$ dan varians $\sigma^2 = 625$. Jika seorang peserta memperoleh skor baku $Z = 1,60$, berapakah nilai asli tes peserta tersebut?

- A. $536$  
  <sub>Salah: Salah mengalikan nilai $Z$ dengan asumsi simpangan baku bernilai $10$ ($520 + 1,60 \times 10 = 536$).</sub>
- B. $480$  
  <sub>Salah: Salah menerapkan operasi dengan mengurangkan $Z \cdot \sigma$ dari rata-rata ($520 - 40$).</sub>
- C. $1.520$  
  <sub>Salah: Langsung mengalikan nilai baku $Z$ dengan varians $625$ tanpa menarik akar kuadrat ($520 + 1,60 \times 625$).</sub>
- **D. $560$** ✅  
  <sub>Benar: Simpangan baku adalah $\sigma = \sqrt{625} = 25$. Nilai mentah dihitung dengan $X = \mu + Z \cdot \sigma = 520 + (1,60 \times 25) = 520 + 40 = 560$.</sub>

**Pembahasan:** Diketahui rata-rata $\mu = 520$ dan varians $\sigma^2 = 625$.
Simpangan baku didapat dari akar varians:
$$\sigma = \sqrt{625} = 25$$
Rumus transformasi nilai baku:
$$Z = \frac{X - \mu}{\sigma}$$
Substitusikan nilai yang diketahui:
$$1,60 = \frac{X - 520}{25}$$
$$X - 520 = 1,60 \times 25$$
$$X - 520 = 40$$
$$X = 520 + 40 = 560$$
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b04-g-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: peluang variabel normal ekor kanan*

Tabel distribusi normal baku menunjukkan nilai $P(Z < 0,75) = 0,7734$.

Waktu pelayanan nasabah pada loket sebuah kantor pos berdistribusi normal dengan rata-rata $15\text{ menit}$ dan simpangan baku $4\text{ menit}$. Tentukan peluang seorang nasabah yang datang dilayani lebih dari $18\text{ menit}$.

- A. $0,7734$  
  <sub>Salah: Menggunakan peluang kumulatif kiri $P(Z < 0,75)$ tanpa mengurangkannya dari $1$.</sub>
- **B. $0,2266$** ✅  
  <sub>Benar: Nilai baku $Z = \frac{18 - 15}{4} = 0,75$. Peluang ekor kanan adalah $P(Z > 0,75) = 1 - P(Z < 0,75) = 1 - 0,7734 = 0,2266$.</sub>
- C. $0,2296$  
  <sub>Salah: Keliru mengambil nilai dari baris tabel untuk $Z = 0,74$ yang bernilai $0,7704$ sehingga didapat $1 - 0,7704 = 0,2296$.</sub>
- D. $0,2734$  
  <sub>Salah: Mengurangkan nilai kumulatif dengan $0,5$ ($0,7734 - 0,5$) bukan mengurangkan dari $1$.</sub>

**Pembahasan:** Hitung nilai baku ($Z$) dari $X = 18$:
$$Z = \frac{X - \mu}{\sigma} = \frac{18 - 15}{4} = \frac{3}{4} = 0,75$$
Karena dicari peluang waktu pelayanan lebih dari $18\text{ menit}$:
$$P(X > 18) = P(Z > 0,75) = 1 - P(Z < 0,75)$$
Berdasarkan nilai tabel normal baku:
$$P(X > 18) = 1 - 0,7734 = 0,2266$$
**Acuan:** siswa — siswa hal.285

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b04-g-hard-bt01-001
*variasi (konteks) | C5 | 4 langkah | jenis: penentuan parameter distribusi*

Tabel distribusi normal baku memberikan nilai kumulatif $P(Z < 1,50) = 0,9332$ dan $P(Z < -2,00) = 0,0228$.

Masa pakai baterai laptop merek tertentu diketahui berdistribusi normal dengan simpangan baku $\sigma = 6$ bulan. Hasil evaluasi layanan purnajual mencatat bahwa tepat $6,68\%$ baterai mampu bertahan lebih dari $45$ bulan. Pabrik berencana memberikan garansi penggantian penuh jika baterai rusak sebelum batas waktu $t$ bulan. Jika pabrik menetapkan kebijakan agar klaim garansi tidak melebihi $2,28\%$ dari total produksi, berapakah batas masa pakai $t$ yang harus ditetapkan?

- **A. $24\text{ bulan}$** ✅  
  <sub>Benar: Dari persentase ekor kanan $P(X > 45) = 0,0668$, diperoleh $P(Z < z) = 1 - 0,0668 = 0,9332$, sehingga $z = 1,50$. Rata-rata populasi dihitung melalui $45 = \mu + 1,50(6) \iff \mu = 36\text{ bulan}$. Batas klaim $2,28\%$ bersesuaian dengan ekor kiri $P(Z < -2,00) = 0,0228$, sehingga $t = \mu + z\sigma = 36 + (-2,00)(6) = 24\text{ bulan}$.</sub>
- B. $48\text{ bulan}$  
  <sub>Salah: Siswa salah menggunakan nilai $Z$ positif untuk batas bawah garansi ($36 + 2(6) = 48$).</sub>
- C. $30\text{ bulan}$  
  <sub>Salah: Siswa salah menentukan rata-rata populasi menjadi $\mu = 42$ karena mengurangkan separuh deviasi, lalu menghitung $42 - 2(6) = 30$.</sub>
- D. $27\text{ bulan}$  
  <sub>Salah: Siswa salah mengambil nilai $z = -1,50$ alih-alih $-2,00$ saat menghitung batas garansi ($36 - 1,50(6) = 27$).</sub>

**Pembahasan:** Langkah 1: Menentukan nilai $z_1$ dari persentase ekor kanan.
Diketahui $P(X > 45) = 6,68\% = 0,0668$.
Maka $P(X \le 45) = 1 - 0,0668 = 0,9332$.
Berdasarkan tabel normal, $P(Z < 1,50) = 0,9332$, sehingga $z_1 = 1,50$.

Langkah 2: Menghitung rata-rata populasi ($\mu$).
$z_1 = \frac{x_1 - \mu}{\sigma} \implies 1,50 = \frac{45 - \mu}{6} \implies 45 - \mu = 9 \implies \mu = 36\text{ bulan}$.

Langkah 3: Menentukan nilai baku untuk klaim garansi $2,28\%$.
Pabrik menghendaki $P(X < t) \le 0,0228$.
Berdasarkan tabel distribusi normal, $P(Z < -2,00) = 0,0228$, maka $z_2 = -2,00$.

Langkah 4: Menghitung batas waktu $t$.
$t = \mu + z_2\sigma = 36 + (-2,00)(6) = 36 - 12 = 24\text{ bulan}$.
**Acuan:** siswa — siswa hal.292 Latihan Soal Distribusi Normal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b04-g-hard-bt01-002
*variasi (angka) | C5 | 5 langkah | jenis: analisis kategori peluang*

Tabel distribusi normal baku menunjukkan nilai kumulatif berikut:
- $P(Z < 0,50) = 0,6915$
- $P(Z < 1,50) = 0,9332$

Nilai ujian seleksi masuk suatu program pelatihan berdistribusi normal dengan rata-rata $70$ dan varians $100$. Peserta dinyatakan lulus dengan predikat Utama jika nilai minimal $85$, predikat Madya jika nilai paling rendah $75$ tetapi kurang dari $85$, dan predikat Dasar jika nilai di bawah $75$. Panitia ingin membandingkan proporsi peserta yang memperoleh predikat Madya terhadap peserta yang memperoleh predikat Utama. Berapakah selisih persentase antara peserta predikat Madya dan peserta predikat Utama?

- A. $30,85\%$  
  <sub>Salah: Siswa menghitung komplemen dari nilai $P(Z < 0,50)$ saja ($1 - 0,6915 = 0,3085$).</sub>
- B. $24,17\%$  
  <sub>Salah: Siswa hanya menghitung persentase peserta predikat Madya tanpa mengurangkan persentase predikat Utama.</sub>
- **C. $17,49\%$** ✅  
  <sub>Benar: Simpangan baku $\sigma = \sqrt{100} = 10$. Skor baku batas 75 adalah $z = 0,50$ dan batas 85 adalah $z = 1,50$. Peluang Utama ($X \ge 85$) adalah $1 - 0,9332 = 0,0668$ ($6,68\%$). Peluang Madya ($75 \le X < 85$) adalah $0,9332 - 0,6915 = 0,2417$ ($24,17\%$). Selisih persentase keduanya adalah $24,17\% - 6,68\% = 17,49\%$.</sub>
- D. $13,29\%$  
  <sub>Salah: Siswa salah menggunakan varians 100 langsung sebagai pembagi saat standardisasi alih-alih simpangan baku 10.</sub>

**Pembahasan:** Langkah 1: Menentukan simpangan baku dari varians.
$\sigma = \sqrt{100} = 10$.

Langkah 2: Menghitung skor baku masing-masing batas nilai.
Untuk $x = 75 \implies z_1 = \frac{75 - 70}{10} = 0,50$.
Untuk $x = 85 \implies z_2 = \frac{85 - 70}{10} = 1,50$.

Langkah 3: Menghitung peluang masing-masing predikat.
- Predikat Utama ($X \ge 85$):
$P(X \ge 85) = P(Z \ge 1,50) = 1 - P(Z < 1,50) = 1 - 0,9332 = 0,0668 = 6,68\%$.
- Predikat Madya ($75 \le X < 85$):
$P(75 \le X < 85) = P(0,50 \le Z < 1,50) = P(Z < 1,50) - P(Z < 0,50) = 0,9332 - 0,6915 = 0,2417 = 24,17\%$.

Langkah 4: Menghitung selisih persentase kedua kelompok predikat.
$\text{Selisih} = 24,17\% - 6,68\% = 17,49\%$.
**Acuan:** siswa — siswa hal.295 Uji Kompetensi Bab 4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b04-g-hard-bt01-003
*orisinal | C6 | 4 langkah | jenis: perancangan batas toleransi*

Tabel distribusi normal baku menunjukkan nilai kumulatif $P(Z < 1,96) = 0,9750$ dan $P(Z < -1,96) = 0,0250$.

Sebuah industri manufaktur memproduksi poros silinder logam dengan diameter berdistribusi normal, memiliki rata-rata $\mu = 50\text{ mm}$ dan simpangan baku $\sigma = 0,25\text{ mm}$. Tim perancang mesin harus menentukan interval toleransi diameter poros $[50 - k, 50 + k]$ agar tepat $95\%$ produk yang dihasilkan lolos pemeriksaan (diterima) secara simetris di sekitar rata-rata. Berapakah nilai rentang toleransi total ($2k$) yang harus dirancang?

- A. $0,49\text{ mm}$  
  <sub>Salah: Siswa hanya menghitung nilai deviasi satu sisi ($k$) bukan rentang total toleransi ($2k$).</sub>
- B. $0,80\text{ mm}$  
  <sub>Salah: Siswa salah menggunakan nilai $z = 1,60$ saat menghitung toleransi simetris.</sub>
- C. $1,96\text{ mm}$  
  <sub>Salah: Siswa mengira rentang toleransi langsung sama dengan nilai $Z$ tanpa mengalikan dengan simpangan baku.</sub>
- **D. $0,98\text{ mm}$** ✅  
  <sub>Benar: Interval simetris 95% di sekitar rata-rata menyisakan masing-masing 2,5% pada ujung kiri dan kanan. Dari $P(Z < -z) = 0,0250$, diperoleh $z = 1,96$. Nilai setengah rentang adalah $k = 1,96 \times 0,25 = 0,49\text{ mm}$, sehingga rentang toleransi total $2k = 2 \times 0,49 = 0,98\text{ mm}$.</sub>

**Pembahasan:** Langkah 1: Menentukan luas ekor kurva pada perancangan simetris 95%.
Luas daerah penerimaan adalah $P(\mu - k \le X \le \mu + k) = 0,95$.
Karena distribusi normal simetris di sekitar $\mu$, luas masing-masing ekor penolakan adalah:
$\alpha / 2 = \frac{1 - 0,95}{2} = 0,0250$.

Langkah 2: Menentukan nilai skor baku $Z$.
Dari tabel kumulatif, nilai yang menghasilkan peluang kumulatif $0,0250$ adalah $z = -1,96$, dan sisi kanannya bersesuaian dengan $z = +1,96$.

Langkah 3: Menghitung deviasi batas toleransi ($k$).
$k = z \times \sigma = 1,96 \times 0,25\text{ mm} = 0,49\text{ mm}$.

Langkah 4: Menghitung rentang toleransi total ($2k$).
$\text{Rentang total} = (50 + k) - (50 - k) = 2k = 2 \times 0,49\text{ mm} = 0,98\text{ mm}$.
**Acuan:** siswa — siswa hal.285

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b04-g-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: evaluasi komparasi kurva normal*

Dua mesin pemotong kayu ($M_1$ dan $M_2$) memotong papan dengan ketebalan berdistribusi normal:
- Mesin $M_1$: rata-rata $\mu_1 = 20\text{ cm}$ dan varians $\sigma_1^2 = 16\text{ cm}^2$
- Mesin $M_2$: rata-rata $\mu_2 = 24\text{ cm}$ dan varians $\sigma_2^2 = 36\text{ cm}^2$

Diketahui dari tabel normal baku bahwa $P(Z < 1,00) = 0,8413$ dan $P(Z < 1,50) = 0,9332$.

Seorang teknisi menyatakan dua klaim berikut:
(1) Puncak grafik fungsi densitas mesin $M_1$ lebih tinggi (lebih leptokurtik) dibandingkan puncak grafik mesin $M_2$.
(2) Peluang mesin $M_1$ memotong papan dengan ketebalan melebihi $26\text{ cm}$ sama besarnya dengan peluang mesin $M_2$ memotong papan dengan ketebalan melebihi $30\text{ cm}$.

Manakah evaluasi yang tepat mengenai kebenaran kedua klaim teknisi tersebut?

- A. Kedua klaim salah, karena kurva distribusi normal selalu memiliki tinggi puncak yang identik terlepas dari variansnya  
  <sub>Salah: Siswa keliru menganggap bahwa luas kurva 1 mengharuskan tinggi puncak kurva konstan untuk semua simpangan baku.</sub>
- B. Kedua klaim benar, karena kedua mesin memiliki selisih nilai potong yang sama persis yaitu $6\text{ cm}$ terhadap masing-masing rata-ratanya  
  <sub>Salah: Siswa mengabaikan pengaruh simpangan baku terhadap skor baku Z dan hanya melihat selisih mutlak $(x - \mu) = 6$.</sub>
- C. Klaim (1) salah dan klaim (2) benar, karena kurva dengan varians lebih besar akan memiliki puncak yang lebih curam  
  <sub>Salah: Siswa terbalik memahami konsep kurva leptokurtik dan platikurtik terhadap nilai varians.</sub>
- **D. Klaim (1) benar, tetapi klaim (2) salah karena peluang mesin $M_1$ melebihi $26\text{ cm}$ adalah $6,68\%$ sedangkan peluang mesin $M_2$ melebihi $30\text{ cm}$ adalah $15,87\%$** ✅  
  <sub>Benar: Simpangan baku $M_1$ adalah $\sigma_1 = 4$ dan $M_2$ adalah $\sigma_2 = 6$. Karena $\sigma_1 < \sigma_2$, kurva $M_1$ lebih tinggi (leptokurtik), maka klaim (1) benar. Untuk klaim (2): $z_1 = (26 - 20)/4 = 1,50 \implies P(X_1 > 26) = 1 - 0,9332 = 0,0668$, sedangkan $z_2 = (30 - 24)/6 = 1,00 \implies P(X_2 > 30) = 1 - 0,8413 = 0,1587$. Nilai peluang keduanya tidak sama, sehingga klaim (2) salah.</sub>

**Pembahasan:** Langkah 1: Menganalisis simpangan baku masing-masing mesin.
- Mesin $M_1$: $\sigma_1 = \sqrt{16} = 4\text{ cm}$.
- Mesin $M_2$: $\sigma_2 = \sqrt{36} = 6\text{ cm}$.
Karena $\sigma_1 < \sigma_2$, kurva mesin $M_1$ lebih sempit dan lebih tinggi (leptokurtik) daripada kurva mesin $M_2$. Maka Klaim (1) BENAR.

Langkah 2: Menghitung skor baku dan peluang untuk mesin $M_1$ ($X_1 > 26$).
$z_1 = \frac{26 - 20}{4} = \frac{6}{4} = 1,50$.
$P(X_1 > 26) = 1 - P(Z < 1,50) = 1 - 0,9332 = 0,0668 = 6,68\%$.

Langkah 3: Menghitung skor baku dan peluang untuk mesin $M_2$ ($X_2 > 30$).
$z_2 = \frac{30 - 24}{6} = \frac{6}{6} = 1,00$.
$P(X_2 > 30) = 1 - P(Z < 1,00) = 1 - 0,8413 = 0,1587 = 15,87\%$.

Langkah 4: Evaluasi komparatif peluang.
Karena $0,0668 \ne 0,1587$, peluang kedua mesin tidak sama. Maka Klaim (2) SALAH.

Kesimpulan: Klaim (1) benar, tetapi klaim (2) salah.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b04-g-hard-bt01-005
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi kelulusan berbasis skor baku*

Dua peserta seleksi calon staf administrasi memperoleh skor baku $Z_1 = 1,40$ dan $Z_2 = -0,60$ pada tes tertulis yang nilainya berdistribusi normal. Skor mentah yang mereka peroleh berturut-turut adalah $82$ dan $52$. Panitia seleksi memutuskan bahwa hanya peserta dengan skor mentah minimal $70$ yang berhak lolos ke tahap wawancara. Jika diketahui nilai tabel distribusi normal baku $P(Z < 0,60) = 0,7257$, persentase peserta seleksi yang lolos ke tahap wawancara adalah ....

- A. $22,57\%$  
  <sub>Salah: Siswa salah menghitung selisih $1 - 0,7257$ akibat kesalahan operasi pengurangan desimal.</sub>
- B. $72,57\%$  
  <sub>Salah: Siswa langsung menggunakan nilai kumulatif $P(Z < 0,60)$ yang sebenarnya merupakan persentase peserta yang tidak lolos.</sub>
- C. $47,43\%$  
  <sub>Salah: Siswa salah menghitung peluang dengan mengurangkan $0,7257$ dengan $0,25$ alih-alih melakukan komplementasi penuh dari $1$.</sub>
- **D. $27,43\%$** ✅  
  <sub>Benar: Dari persamaan skor baku diperoleh sistem linear $82 = \mu + 1,40\sigma$ dan $52 = \mu - 0,60\sigma$. Mengurangkan kedua persamaan menghasilkan $2,00\sigma = 30 \implies \sigma = 15$, sehingga $\mu = 52 + 0,60(15) = 61$. Untuk nilai ambang batas $X = 70$, nilai bakunya adalah $Z = \frac{70 - 61}{15} = 0,60$. Peluang peserta lolos adalah $P(X \ge 70) = P(Z \ge 0,60) = 1 - P(Z < 0,60) = 1 - 0,7257 = 0,2743 = 27,43\%$.</sub>

**Pembahasan:** Langkah 1: Menentukan parameter distribusi (rata-rata $\mu$ dan simpangan baku $\sigma$).
Berdasarkan rumus $Z = \frac{X - \mu}{\sigma} \iff X = \mu + Z\sigma$:
(1) $82 = \mu + 1,40\sigma$
(2) $52 = \mu - 0,60\sigma$

Kurangkan persamaan (1) dengan (2):
$30 = 2,00\sigma \implies \sigma = 15$

Substitusikan $\sigma = 15$ ke persamaan (2):
$\mu = 52 + 0,60(15) = 52 + 9 = 61$

Langkah 2: Menghitung skor baku untuk nilai ambang batas $X = 70$:
$Z = \frac{70 - 61}{15} = \frac{9}{15} = 0,60$

Langkah 3: Menghitung peluang dan persentase kelulusan:
$P(X \ge 70) = P(Z \ge 0,60) = 1 - P(Z < 0,60) = 1 - 0,7257 = 0,2743$
Dalam bentuk persentase: $0,2743 \times 100\% = 27,43\%$.
**Acuan:** pretest — kelas12_tl-b04-p0292-latihan-soal-distribusi-normal-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b04-g-hard-bt01-006
*orisinal | C6 | 4 langkah | jenis: perancangan batas toleransi variabilitas*

Sebuah mesin pengisi cairan otomatis diatur untuk mengisi botol detergen dengan volume rata-rata $\mu = 500\text{ ml}$. Botol dikategorikan cacat jika volumenya melebihi kapasitas maksimum wadah yaitu $524\text{ ml}$. Berdasarkan tabel distribusi normal baku, diketahui $P(Z < 2,00) = 0,9772$. Agar persentase botol cacat yang diproduksi tidak melebihi $2,28\%$, rancangan batas maksimum simpangan baku ($\sigma$) yang diperbolehkan untuk mesin tersebut adalah ....

- A. $6\text{ ml}$  
  <sub>Salah: Siswa keliru membagi selisih $24$ dengan kuadrat dari nilai $Z$ ($2^2 = 4$).</sub>
- **B. $12\text{ ml}$** ✅  
  <sub>Benar: Kondisi cacat terjadi saat $X > 524$. Syarat peluang cacat $P(X > 524) \le 0,0228 \iff P(X \le 524) \ge 0,9772$. Karena $P(Z \le 2,00) = 0,9772$, maka nilai baku ambang batas harus memenuhi $Z = \frac{524 - 500}{\sigma} \ge 2,00 \iff \frac{24}{\sigma} \ge 2,00 \iff \sigma \le 12\text{ ml}$. Dengan demikian, batas maksimum simpangan baku adalah $12\text{ ml}$.</sub>
- C. $48\text{ ml}$  
  <sub>Salah: Siswa terbalik melakukan operasi perhitungan dengan mengalikan selisih $24$ dengan $Z = 2,00$.</sub>
- D. $24\text{ ml}$  
  <sub>Salah: Siswa hanya menghitung selisih $524 - 500 = 24$ tanpa membaginya dengan nilai skor baku $Z = 2,00$.</sub>

**Pembahasan:** Langkah 1: Mengidentifikasi kondisi probabilitas.
Botol cacat jika $X > 524\text{ ml}$.
Diinginkan persentase cacat $\le 2,28\%$, maka:
$P(X > 524) \le 0,0228 \iff P(X \le 524) \ge 1 - 0,0228 = 0,9772$

Langkah 2: Menghubungkan dengan nilai baku $Z$.
Dari tabel distribusi normal baku, $P(Z < 2,00) = 0,9772$.
Agar $P(X \le 524) \ge 0,9772$, posisi nilai $X = 524$ harus berada setidaknya pada $Z = 2,00$ atau lebih ke kanan:
$\frac{X - \mu}{\sigma} \ge 2,00$

Langkah 3: Menyelesaikan pertidaksamaan untuk parameter $\sigma$:
$\frac{524 - 500}{\sigma} \ge 2,00$
$\frac{24}{\sigma} \ge 2,00 \iff \sigma \le \frac{24}{2,00} = 12\text{ ml}$

Jadi, batas maksimum simpangan baku yang diperbolehkan adalah $12\text{ ml}$.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b04-g-hard-bt01-007
*orisinal | C5 | 3 langkah | jenis: evaluasi komparasi posisi relatif*

Dua kelompok siswa, Kelas A dan Kelas B, menempuh tes matematika dengan distribusi skor berdistribusi normal:
- Kelas A memiliki rata-rata $\mu_A = 68$ dengan simpangan baku $\sigma_A = 8$.
- Kelas B memiliki rata-rata $\mu_B = 75$ dengan simpangan baku $\sigma_B = 10$.

Siswa P dari Kelas A memperoleh nilai mentah 80, sedangkan Siswa Q dari Kelas B memperoleh nilai mentah 90. Berdasarkan perbandingan skor baku ($Z$) pada kurva normal masing-masing kelas, evaluasilah pernyataan yang paling tepat mengenai posisi relatif prestasi kedua siswa tersebut!

- A. Siswa Q memiliki posisi relatif lebih unggul daripada Siswa P karena nilai mentah Siswa Q ($90$) lebih tinggi daripada nilai mentah Siswa P ($80$).  
  <sub>Salah: Siswa terjebak membandingkan nilai mentah secara langsung tanpa menstandarisasikannya ke dalam distribusi normal kelompok.</sub>
- B. Siswa Q memiliki posisi relatif lebih unggul daripada Siswa P karena selisih nilai terhadap rata-rata kelasnya lebih besar ($15$ poin berbanding $12$ poin).  
  <sub>Salah: Siswa hanya melihat deviasi absolut dari rata-rata tanpa membaginya dengan simpangan baku masing-masing kelompok.</sub>
- **C. Kedua siswa memiliki posisi relatif yang sama unggul terhadap kelompoknya masing-masing karena nilai baku keduanya sama ($Z_P = Z_Q = 1,50$).** ✅  
  <sub>Benar: Nilai baku Siswa P adalah $Z_P = \frac{80 - 68}{8} = 1,50$. Nilai baku Siswa Q adalah $Z_Q = \frac{90 - 75}{10} = 1,50$. Karena nilai baku kedua siswa bernilai persis sama, kedudukan relatif persentil keduanya terhadap masing-masing kelompok adalah identik.</sub>
- D. Siswa P memiliki posisi relatif lebih unggul daripada Siswa Q karena simpangan baku Kelas A lebih kecil sehingga sebaran nilainya lebih homogen.  
  <sub>Salah: Siswa salah menafsirkan simpangan baku yang lebih kecil sebagai tanda keunggulan posisi individu secara sepihak.</sub>

**Pembahasan:** Langkah 1: Menghitung skor baku Siswa P dari Kelas A:
$Z_P = \frac{X_P - \mu_A}{\sigma_A} = \frac{80 - 68}{8} = \frac{12}{8} = 1,50$

Langkah 2: Menghitung skor baku Siswa Q dari Kelas B:
$Z_Q = \frac{X_Q - \mu_B}{\sigma_B} = \frac{90 - 75}{10} = \frac{15}{10} = 1,50$

Langkah 3: Evaluasi perbandingan posisi relatif:
Karena $Z_P = Z_Q = 1,50$, kedua siswa berada tepat $1,50$ simpangan baku di atas rata-rata populasinya. Pada kurva normal standar, keduanya memiliki luas daerah di sebelah kiri yang identik, sehingga posisi relatif prestasi kedua siswa adalah sama unggul terhadap kelompok masing-masing.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b04-g-hard-bt01-008
*orisinal | C5 | 3 langkah | jenis: evaluasi sifat geometri kurva normal*

Kurva fungsi densitas peluang suatu variabel acak normal kontinu $X$ diketahui memiliki titik belok di $x = 55$ dan $x = 75$.
Seorang analis menyimpulkan tiga hal mengenai distribusi tersebut:
(1) Rata-rata distribusi adalah $\mu = 65$.
(2) Simpangan baku distribusi adalah $\sigma = 20$.
(3) Kurva berbentuk cekung ke bawah pada interval $55 < x < 75$.

Berdasarkan sifat-sifat kurva normal, evaluasilah kesimpulan analis tersebut: manakah pernyataan yang benar?

- A. Pernyataan (1) dan (2) saja  
  <sub>Salah: Siswa salah memahami sifat kecekungan kurva normal dan keliru dalam menentukan simpangan baku.</sub>
- B. Pernyataan (1) saja  
  <sub>Salah: Siswa meragukan sifat kecekungan kurva di sekitar nilai rata-rata.</sub>
- **C. Pernyataan (1) dan (3) saja** ✅  
  <sub>Benar: Titik belok kurva normal terletak di $x = \mu \pm \sigma$. Maka $\mu - \sigma = 55$ dan $\mu + \sigma = 75$. Nilai $\mu = \frac{55 + 75}{2} = 65$ (pernyataan 1 benar). Nilai $\sigma = \frac{75 - 55}{2} = 10$, bukan 20 (pernyataan 2 salah). Kurva normal cekung ke bawah tepat pada interval $\mu - \sigma < x < \mu + \sigma$, yaitu $55 < x < 75$ (pernyataan 3 benar).</sub>
- D. Pernyataan (1), (2), dan (3)  
  <sub>Salah: Siswa keliru menganggap simpangan baku $\sigma$ sama dengan jarak horizontal antarkedua titik belok ($2\sigma = 20$).</sub>

**Pembahasan:** Langkah 1: Menganalisis titik belok kurva normal.
Kurva distribusi normal memiliki titik belok pada absis $x = \mu - \sigma$ dan $x = \mu + \sigma$.
Diketahui titik belok berada di $x_1 = 55$ dan $x_2 = 75$.

Langkah 2: Menghitung rata-rata dan simpangan baku.
- Rata-rata: $\mu = \frac{x_1 + x_2}{2} = \frac{55 + 75}{2} = 65$ (Pernyataan 1 BENAR).
- Simpangan baku: $2\sigma = 75 - 55 = 20 \implies \sigma = 10$. Nilai pada pernyataan (2) tertulis $\sigma = 20$ (Pernyataan 2 SALAH).

Langkah 3: Meninjau kecekungan kurva.
Berdasarkan sifat distribusi normal, kurva cekung di bagian bawah (cekung ke bawah) apabila $\mu - \sigma < x < \mu + \sigma$, yang berarti $55 < x < 75$ (Pernyataan 3 BENAR).

Jadi, pernyataan yang benar adalah (1) dan (3) saja.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b04-g-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: penentuan interval spesifikasi simetris*

Tabel distribusi normal baku menunjukkan nilai peluang kumulatif:
- $P(Z < -1,25) = 0,1056$
- $P(Z < 1,25) = 0,8944$

Sebuah industri manufaktur memproduksi komponen poros silinder dengan diameter berdistribusi normal yang memiliki rata-rata $\mu = 25\text{ mm}$ dan varians $\sigma^2 = 0,16\text{ mm}^2$. Komponen yang dapat dipasarkan sebagai "Kualitas Presisi" harus memiliki diameter dalam rentang simetris di sekitar rata-rata yang mencakup tepat $78,88\%$ dari seluruh hasil produksi. Rentang diameter untuk komponen "Kualitas Presisi" tersebut adalah ....

- A. $24,8\text{ mm} \le X \le 25,2\text{ mm}$  
  <sub>Salah: Siswa langsung mengalikan nilai baku $Z = 1,25$ dengan varians $\sigma^2 = 0,16$ tanpa menarik akarnya terlebih dahulu menjadi simpangan baku ($0,4$).</sub>
- **B. $24,5\text{ mm} \le X \le 25,5\text{ mm}$** ✅  
  <sub>Benar: Luas daerah simetris di tengah adalah $0,7888$, sehingga total luas kedua ekor adalah $1 - 0,7888 = 0,2112$. Masing-masing ekor memiliki luas $\frac{0,2112}{2} = 0,1056$, yang bersesuaian dengan $Z = -1,25$ dan $Z = 1,25$. Simpangan baku adalah $\sigma = \sqrt{0,16} = 0,4\text{ mm}$. Batas deviasi adalah $d = 1,25 \times 0,4 = 0,5\text{ mm}$. Rentang diameter menjadi $25 - 0,5 \le X \le 25 + 0,5$, yaitu $24,5\text{ mm} \le X \le 25,5\text{ mm}$.</sub>
- C. $24,0\text{ mm} \le X \le 26,0\text{ mm}$  
  <sub>Salah: Siswa salah menentukan nilai batas deviasi menjadi $1,0\text{ mm}$ akibat salah membaca nilai tabel.</sub>
- D. $23,75\text{ mm} \le X \le 26,25\text{ mm}$  
  <sub>Salah: Siswa langsung menjumlahkan dan mengurangkan nilai $Z = 1,25$ ke rata-rata $\mu = 25$ tanpa mengalikannya dengan simpangan baku.</sub>

**Pembahasan:** Langkah 1: Menghitung luas ekor distribusi normal.
Daerah simetris di tengah kurva memiliki luas $78,88\% = 0,7888$.
Luas daerah di luar interval tersebut adalah $1 - 0,7888 = 0,2112$.
Karena kurva normal simetris di sekitar rata-rata, luas pada masing-masing ekor (kiri dan kanan) adalah:
$\alpha = \frac{0,2112}{2} = 0,1056$

Langkah 2: Menentukan nilai baku $Z$.
Dari tabel distribusi normal baku:
$P(Z < Z_1) = 0,1056 \implies Z_1 = -1,25$
$P(Z < Z_2) = 1 - 0,1056 = 0,8944 \implies Z_2 = 1,25$

Langkah 3: Menghitung simpangan baku $\sigma$.
Diketahui varians $\sigma^2 = 0,16\text{ mm}^2$, maka:
$\sigma = \sqrt{0,16} = 0,4\text{ mm}$

Langkah 4: Menentukan rentang diameter.
Batas toleransi $d = Z \times \sigma = 1,25 \times 0,4 = 0,5\text{ mm}$.
- Batas bawah: $X_1 = \mu - d = 25 - 0,5 = 24,5\text{ mm}$
- Batas atas: $X_2 = \mu + d = 25 + 0,5 = 25,5\text{ mm}$

Jadi, rentang diameter komponen Kualitas Presisi adalah $24,5\text{ mm} \le X \le 25,5\text{ mm}$.
**Acuan:** siswa — siswa hal.285

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b04-g-hard-bt01-010
*variasi (konteks) | C5 | 5 langkah | jenis: evaluasi kuota rekrutmen ambang ganda*

Tabel distribusi normal baku memberikan nilai kumulatif berikut:
- $P(Z < -1,25) = 0,1056$
- $P(Z < 2,00) = 0,9772$

Sebuah perusahaan menyelenggarakan tes seleksi potensi akademik yang diikuti oleh $1.200$ peserta. Skor tes berdistribusi normal dengan rata-rata $76$ dan simpangan baku $8$. Manajemen menetapkan aturan: peserta dengan skor kurang dari $66$ langsung dinyatakan gugur, sedangkan peserta dengan skor minimal $92$ langsung diterima tanpa wawancara. Peserta dengan skor di antara kedua batas tersebut diwajibkan mengikuti tahap wawancara. Banyaknya peserta yang dipanggil untuk mengikuti tahap wawancara adalah ....

- A. $1.173$ orang  
  <sub>Salah: Hanya menghitung peserta yang tidak langsung diterima tanpa mengurangkan peserta yang gugur ($1.200 \times 0,9772$).</sub>
- **B. $1.046$ orang** ✅  
  <sub>Benar: Skor z untuk $x_1 = 66$ adalah $z_1 = \frac{66 - 76}{8} = -1,25$. Skor z untuk $x_2 = 92$ adalah $z_2 = \frac{92 - 76}{8} = 2,00$. Peluang peserta masuk tahap wawancara adalah $P(66 \le X < 92) = P(-1,25 \le Z < 2,00) = P(Z < 2,00) - P(Z < -1,25) = 0,9772 - 0,1056 = 0,8716$. Banyak peserta yang dipanggil adalah $1.200 \times 0,8716 = 1.045,92 \approx 1.046$ orang.</sub>
- C. $1.073$ orang  
  <sub>Salah: Salah membaca tabel dengan menghitung $P(Z < 2,00) - (1 - P(Z < 2,00)) = 0,9772 - 0,0228 = 0,9544 \times 1.200$.</sub>
- D. $926$ orang  
  <sub>Salah: Keliru menggunakan nilai $P(Z < 1,25) = 0,8944$ lalu mengurangkannya dari $0,9772$ ($0,0828 \times 1.200 = 99$, lalu $1.200 - 99 - 175$).</sub>

**Pembahasan:** Transformasikan kedua batas skor ke skor baku $Z$:
$$z_1 = \frac{66 - 76}{8} = -1,25$$
$$z_2 = \frac{92 - 76}{8} = 2,00$$

Hitung peluang skor di antara $66$ dan $92$:
$$P(66 \le X < 92) = P(-1,25 \le Z < 2,00) = P(Z < 2,00) - P(Z < -1,25)$$
$$P = 0,9772 - 0,1056 = 0,8716$$

Hitung perkiraan jumlah peserta yang mengikuti wawancara:
$$\text{Banyak peserta} = 1.200 \times 0,8716 = 1.045,92 \approx 1.046\text{ orang}$$

Jadi, banyaknya peserta yang dipanggil untuk wawancara adalah $1.046$ orang.
**Acuan:** siswa — siswa hal.293 Latihan Soal Distribusi Normal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b04-g-hard-bt01-011
*variasi (angka) | C5 | 5 langkah | jenis: analisis risiko anomali armada*

Tabel distribusi normal baku menunjukkan nilai kumulatif:
- $P(Z < -1,50) = 0,0668$
- $P(Z < 1,50) = 0,9332$

Jarak tempuh bulanan armada taksi listrik pada suatu perusahaan berdistribusi normal dengan rata-rata $4.200\text{ km}$ dan simpangan baku $600\text{ km}$. Manajemen menetapkan bahwa jarak tempuh antara $3.300\text{ km}$ hingga $5.100\text{ km}$ per bulan merupakan pemakaian wajar. Taksi yang beroperasi di luar rentang tersebut dinyatakan mengalami anomali pemakaian (terlalu rendah atau terlalu tinggi) sehingga memerlukan inspeksi teknis khusus. Persentase armada taksi yang memerlukan inspeksi teknis khusus tersebut adalah ....

- A. $86,64\%$  
  <sub>Salah: Menghitung persentase armada dengan pemakaian wajar, bukan persentase anomali pemakaian.</sub>
- B. $6,68\%$  
  <sub>Salah: Hanya menghitung salah satu ekor kurva anomali ($P(Z < -1,50)$ saja atau $P(Z > 1,50)$ saja).</sub>
- **C. $13,36\%$** ✅  
  <sub>Benar: Skor z batas bawah $z_1 = \frac{3.300 - 4.200}{600} = -1,50$. Skor z batas atas $z_2 = \frac{5.100 - 4.200}{600} = 1,50$. Peluang pemakaian normal adalah $P(-1,50 \le Z \le 1,50) = 0,9332 - 0,0668 = 0,8664$. Persentase yang di luar batas normal adalah $1 - 0,8664 = 0,1336 = 13,36\%$.</sub>
- D. $26,72\%$  
  <sub>Salah: Salah mengalikan dua hasil anomali dari $0,1336$ menjadi $0,2672$.</sub>

**Pembahasan:** Hitung skor baku kedua batas pemakaian:
$$z_1 = \frac{3.300 - 4.200}{600} = -1,50$$
$$z_2 = \frac{5.100 - 4.200}{600} = 1,50$$

Peluang armada berada pada rentang pemakaian wajar:
$$P(3.300 \le X \le 5.100) = P(-1,50 \le Z \le 1,50)$$
$$P = P(Z < 1,50) - P(Z < -1,50) = 0,9332 - 0,0668 = 0,8664$$

Peluang armada mengalami anomali pemakaian (di luar batas wajar):
$$P(\text{anomali}) = 1 - P(3.300 \le X \le 5.100) = 1 - 0,8664 = 0,1336$$

Dalam persentase:
$$0,1336 \times 100\% = 13,36\%$$

Jadi, persentase armada taksi yang memerlukan inspeksi teknis khusus adalah $13,36\%$.
**Acuan:** siswa — siswa hal.294 Uji Kompetensi Bab 4 B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b04-g-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: pengujian hipotesis parameter titik belok*

Tabel distribusi normal baku menunjukkan nilai kumulatif $P(Z < -1,75) = 0,0401$.

Sebuah mesin pencetak pelat logam memproduksi pelat dengan ketebalan yang berdistribusi normal. Kurva fungsi densitas ketebalan pelat tersebut memiliki titik belok di $x = 4,65\text{ mm}$ dan $x = 5,35\text{ mm}$. Pelat dianggap cacat tipis jika ketebalannya kurang dari $4,3875\text{ mm}$. Berdasarkan karakteristik kurva tersebut, peluang sebuah pelat yang diproduksi mengalami cacat tipis adalah ....

- A. $0,9599$  
  <sub>Salah: Menghitung komplemennya $1 - 0,0401 = 0,9599$ (peluang pelat tidak cacat tipis).</sub>
- **B. $0,0401$** ✅  
  <sub>Benar: Titik belok berada di $\mu - \sigma = 4,65$ dan $\mu + \sigma = 5,35$. Menjumlahkan keduanya: $2\mu = 10,00 \implies \mu = 5,00\text{ mm}$. Mengurangkannya: $2\sigma = 0,70 \implies \sigma = 0,35\text{ mm}$. Skor baku batas cacat: $z = \frac{4,3875 - 5,00}{0,35} = \frac{-0,6125}{0,35} = -1,75$. Dari stimulus, $P(Z < -1,75) = 0,0401$.</sub>
- C. $0,0802$  
  <sub>Salah: Keliru mengalikan dua peluang karena menganggap cacat terjadi di kedua ujung.</sub>
- D. $0,0200$  
  <sub>Salah: Keliru membagi dua nilai peluang pada tabel.</sub>

**Pembahasan:** Berdasarkan sifat kurva distribusi normal, titik belok berada pada $x = \mu - \sigma$ dan $x = \mu + \sigma$.
Diketahui:
$$\mu - \sigma = 4,65$$
$$\mu + \sigma = 5,35$$

Jumlahkan kedua persamaan:
$$2\mu = 10,00 \implies \mu = 5,00\text{ mm}$$

Kurangkan kedua persamaan:
$$2\sigma = 0,70 \implies \sigma = 0,35\text{ mm}$$

Hitung skor baku untuk batas cacat tipis $x = 4,3875\text{ mm}$:
$$z = \frac{4,3875 - 5,00}{0,35} = \frac{-0,6125}{0,35} = -1,75$$

Peluang pelat mengalami cacat tipis adalah:
$$P(X < 4,3875) = P(Z < -1,75) = 0,0401$$

Jadi, peluang pelat mengalami cacat tipis adalah $0,0401$.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b04-g-hard-bt01-013
*orisinal | C6 | 4 langkah | jenis: perancangan batas dispersi relatif*

Dua divisi dalam sebuah korporasi menempuh uji kelayakan tahunan dengan skor berdistribusi normal:
- Divisi A memiliki skor rata-rata $\mu_A = 72$ dengan simpangan baku $\sigma_A = 6$.
- Divisi B memiliki skor rata-rata $\mu_B = 80$ dengan simpangan baku $\sigma_B$.

Karyawan teladan dari Divisi A memperoleh skor $81$. Seorang karyawan dari Divisi B memperoleh skor $95$. Agar posisi prestasi relatif (skor baku $Z$) karyawan Divisi B tersebut lebih unggul secara statistik dibandingkan karyawan teladan dari Divisi A, simpangan baku Divisi B ($\sigma_B$) harus memenuhi syarat ....

- A. $0 < \sigma_B < 15$  
  <sub>Salah: Lupa mengalikan dengan $1,50$ dan langsung mengambil selisih skor $95 - 80 = 15$.</sub>
- B. $\sigma_B > 12$  
  <sub>Salah: Keliru membagi $15$ dengan perbandingan varians bukan skor baku.</sub>
- C. $\sigma_B > 10$  
  <sub>Salah: Membalik tanda pertidaksamaan saat membagi dengan bilangan positif.</sub>
- **D. $0 < \sigma_B < 10$** ✅  
  <sub>Benar: Skor baku karyawan Divisi A: $Z_A = \frac{81 - 72}{6} = \frac{9}{6} = 1,50$. Skor baku karyawan Divisi B: $Z_B = \frac{95 - 80}{\sigma_B} = \frac{15}{\sigma_B}$. Agar prestasi relatif karyawan Divisi B lebih unggul, disyaratkan $Z_B > Z_A \implies \frac{15}{\sigma_B} > 1,50 \implies \sigma_B < \frac{15}{1,50} = 10$. Karena simpangan baku selalu bernilai positif, maka $0 < \sigma_B < 10$.</sub>

**Pembahasan:** Hitung skor baku ($Z$) untuk karyawan dari Divisi A:
$$Z_A = \frac{X_A - \mu_A}{\sigma_A} = \frac{81 - 72}{6} = \frac{9}{6} = 1,50$$

Hitung bentuk skor baku ($Z$) untuk karyawan dari Divisi B:
$$Z_B = \frac{X_B - \mu_B}{\sigma_B} = \frac{95 - 80}{\sigma_B} = \frac{15}{\sigma_B}$$

Agar prestasi relatif karyawan Divisi B lebih unggul daripada karyawan Divisi A, maka harus dipenuhi:
$$Z_B > Z_A$$
$$\frac{15}{\sigma_B} > 1,50$$

Karena simpangan baku $\sigma_B$ merupakan ukuran dispersi yang wajib bernilai positif ($\sigma_B > 0$):
$$15 > 1,50\sigma_B \implies \sigma_B < \frac{15}{1,50} = 10$$

Dengan demikian, batas nilai simpangan baku Divisi B adalah $0 < \sigma_B < 10$.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b04-g-hard-bt01-014
*orisinal | C5 | 6 langkah | jenis: perbandingan sensitivitas dispersi kurva*

Tabel distribusi normal baku memberikan nilai peluang kumulatif:
- $P(Z < -1,00) = 0,1587$ dan $P(Z < 1,00) = 0,8413$
- $P(Z < -0,50) = 0,3085$ dan $P(Z < 0,50) = 0,6915$

Dua lini mesin pengemasan gula, Mesin I dan Mesin II, menghasilkan berat kemasan berdistribusi normal dengan rata-rata yang sama, yaitu $\mu = 1.000\text{ gram}$. Namun, tingkat presisinya berbeda: Mesin I memiliki simpangan baku $\sigma_1 = 10\text{ gram}$, sedangkan Mesin II memiliki simpangan baku $\sigma_2 = 20\text{ gram}$. Sebuah kemasan dikategorikan memiliki berat sangat presisi apabila berada pada rentang $990\text{ gram} \le X \le 1.010\text{ gram}$. Selisih peluang kemasan berstatus sangat presisi antara Mesin I dan Mesin II adalah ....

- **A. $0,2996$** ✅  
  <sub>Benar: Untuk Mesin I: interval $[990, 1010]$ menghasilkan $z_1 = \frac{990 - 1000}{10} = -1,00$ dan $z_2 = 1,00$. Peluangnya $P_1 = 0,8413 - 0,1587 = 0,6826$. Untuk Mesin II: interval $[990, 1010]$ menghasilkan $z_1 = \frac{990 - 1000}{20} = -0,50$ dan $z_2 = 0,50$. Peluangnya $P_2 = 0,6915 - 0,3085 = 0,3830$. Selisih peluang keduanya adalah $|P_1 - P_2| = 0,6826 - 0,3830 = 0,2996$.</sub>
- B. $0,3830$  
  <sub>Salah: Mengambil peluang Mesin II saja tanpa menghitung selisih dengan Mesin I.</sub>
- C. $0,6826$  
  <sub>Salah: Mengambil peluang Mesin I saja tanpa menghitung selisih dengan Mesin II.</sub>
- D. $0,1498$  
  <sub>Salah: Hanya menghitung selisih setengah sisi kurva ($0,8413 - 0,6915 = 0,1498$).</sub>

**Pembahasan:** Hitung peluang kemasan sangat presisi untuk Mesin I:
- Batas nilai z:
$$z_1 = \frac{990 - 1.000}{10} = -1,00$$
$$z_2 = \frac{1.010 - 1.000}{10} = 1,00$$
- Peluang Mesin I:
$$P_1 = P(-1,00 \le Z \le 1,00) = P(Z < 1,00) - P(Z < -1,00) = 0,8413 - 0,1587 = 0,6826$$

Hitung peluang kemasan sangat presisi untuk Mesin II:
- Batas nilai z:
$$z_1 = \frac{990 - 1.000}{20} = -0,50$$
$$z_2 = \frac{1.010 - 1.000}{20} = 0,50$$
- Peluang Mesin II:
$$P_2 = P(-0,50 \le Z \le 0,50) = P(Z < 0,50) - P(Z < -0,50) = 0,6915 - 0,3085 = 0,3830$$

Hitung selisih peluang kemasan berstatus sangat presisi:
$$\Delta P = P_1 - P_2 = 0,6826 - 0,3830 = 0,2996$$

Jadi, selisih peluang antara Mesin I dan Mesin II adalah $0,2996$.
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b04-g-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: analisis ekor ganda distribusi*

Tabel distribusi normal baku memuat nilai kumulatif berikut:
- $P(Z < -1,80) = 0,0359$
- $P(Z < 2,20) = 0,9861$

Sebuah mesin produksi pipa baja menghasilkan pipa dengan diameter rata-rata $\mu = 50\text{ mm}$ dan simpangan baku $\sigma = 2,5\text{ mm}$. Pipa dinyatakan cacat dan harus dilebur kembali apabila diameternya kurang dari $45,5\text{ mm}$ atau lebih dari $55,5\text{ mm}$. Berapakah persentase total pipa yang dinyatakan cacat?

- A. $2,20\%$  
  <sub>Salah: Hanya menghitung salah satu ekor atau mengambil nilai $Z$ sebagai persentase.</sub>
- B. $95,02\%$  
  <sub>Salah: Menghitung persentase produk yang tidak cacat (diterima) bukan produk cacat.</sub>
- C. $7,18\%$  
  <sub>Salah: Mengalikan peluang ekor kiri dengan 2 secara keliru: $2 \times 0,0359 = 0,0718$ tanpa memperhitungkan batas atas yang asimetris terhadap rata-rata.</sub>
- **D. $4,98\%$** ✅  
  <sub>Benar: Menghitung $Z_1 = (45,5 - 50)/2,5 = -1,80$ dengan peluang $P(Z < -1,80) = 0,0359$. Menghitung $Z_2 = (55,5 - 50)/2,5 = 2,20$ dengan ekor atas $P(Z > 2,20) = 1 - 0,9861 = 0,0139$. Total persentase cacat adalah $(0,0359 + 0,0139) \times 100\% = 0,0498 \times 100\% = 4,98\%$.</sub>

**Pembahasan:** Langkah 1: Transformasi batas bawah diameter ($x_1 = 45,5\text{ mm}$) ke skor baku:
$$Z_1 = \frac{45,5 - 50}{2,5} = \frac{-4,5}{2,5} = -1,80$$
Langkah 2: Transformasi batas atas diameter ($x_2 = 55,5\text{ mm}$) ke skor baku:
$$Z_2 = \frac{55,5 - 50}{2,5} = \frac{5,5}{2,5} = 2,20$$
Langkah 3: Menghitung peluang cacat pada masing-masing ekor distribusi:
- Peluang terlalu kecil: $P(X < 45,5) = P(Z < -1,80) = 0,0359$
- Peluang terlalu besar: $P(X > 55,5) = P(Z > 2,20) = 1 - P(Z < 2,20) = 1 - 0,9861 = 0,0139$
Langkah 4: Menjumlahkan kedua peluang cacat dan mengonversi ke persentase:
$$P(\text{Cacat}) = 0,0359 + 0,0139 = 0,0498$$
$$\text{Persentase} = 0,0498 \times 100\% = 4,98\%$$
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b04-g-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: analisis nilai batas persentil*

Tabel distribusi normal baku menunjukkan nilai peluang kumulatif:
- $P(Z < -0,84) = 0,2005$
- $P(Z < 0,84) = 0,7995$

Masa pakai kompresor kulkas berdistribusi normal dengan rata-rata $10\text{ tahun}$ dan simpangan baku $2,5\text{ tahun}$. Pabrik ingin menetapkan batas masa garansi sedemikian rupa sehingga paling banyak $20\%$ dari seluruh kompresor yang terjual memerlukan klaim garansi. Berdasarkan data tabel, batas masa garansi paling lama yang dapat ditetapkan oleh pabrik adalah ...

- A. $8,4\text{ tahun}$  
  <sub>Salah: Mengurangi rata-rata langsung dengan nilai skor baku: $10 - 0,84 \times 2$ atau salah hitung perkalian.</sub>
- **B. $7,9\text{ tahun}$** ✅  
  <sub>Benar: Peluang kumulatif garansi adalah $20\% = 0,20$. Dari tabel, $P(Z < -0,84) \approx 0,2005$. Maka $Z = -0,84$. Nilai $x = \mu + Z\sigma = 10 + (-0,84)(2,5) = 10 - 2,1 = 7,9\text{ tahun}$.</sub>
- C. $12,1\text{ tahun}$  
  <sub>Salah: Menggunakan skor baku positif: $10 + 2,1 = 12,1\text{ tahun}$ yang menghasilkan persentil $80\%$ teratas.</sub>
- D. $7,5\text{ tahun}$  
  <sub>Salah: Hanya mengurangkan satu kali simpangan baku dari rata-rata: $10 - 2,5 = 7,5$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai peluang kumulatif yang menjadi batas garansi:
Pabrik menginginkan klaim garansi mencakup $20\%$ atau $0,20$ data paling kiri pada kurva normal: $P(X < x) \le 0,20$.
Langkah 2: Menentukan nilai $Z$ yang bersesuaian dari tabel distribusi normal:
Dari data stimulus, $P(Z < -0,84) = 0,2005 \approx 0,20$, sehingga nilai skor baku adalah $Z = -0,84$.
Langkah 3: Menggunakan rumus transformasi nilai baku $Z = \frac{x - \mu}{\sigma}$:
$$-0,84 = \frac{x - 10}{2,5}$$
Langkah 4: Menyelesaikan nilai $x$:
$$x - 10 = -0,84 \times 2,5$$
$$x - 10 = -2,1$$
$$x = 10 - 2,1 = 7,9\text{ tahun}$$
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b04-g-hard-bt01-017
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi ambang mutu bersyarat*

Tabel distribusi normal baku memberikan nilai peluang kumulatif berikut:
- $P(Z < -1,80) = 0,0359$
- $P(Z < 1,80) = 0,9641$

Sebuah industri komponen mesin memproduksi poros engsel dengan diameter yang berdistribusi normal. Rata-rata diameter poros adalah $48\text{ mm}$ dengan simpangan baku $5\text{ mm}$. Standar kelayakan mengharuskan diameter poros berada pada rentang antara $39\text{ mm}$ dan $57\text{ mm}$. Komponen yang berada di luar rentang tersebut dinyatakan tidak lolos seleksi dan harus didaur ulang. Dari total produksi sebanyak $5.000$ unit poros engsel, perkiraan banyaknya komponen yang harus didaur ulang adalah ....

- A. $4.641\text{ unit}$  
  <sub>Salah: Siswa menghitung banyaknya komponen yang lolos seleksi kelayakan, bukan yang harus didaur ulang ($5.000 \times 0,9282$).</sub>
- B. $180\text{ unit}$  
  <sub>Salah: Siswa hanya menghitung komponen yang gagal pada salah satu sisi ekor distribusi ($5.000 \times 0,0359 = 179,5 \approx 180$).</sub>
- **C. $359\text{ unit}$** ✅  
  <sub>Benar: Nilai baku batas bawah adalah $z_1 = \frac{39 - 48}{5} = -1,80$ dan batas atas adalah $z_2 = \frac{57 - 48}{5} = 1,80$. Peluang poros memenuhi standar kelayakan adalah $P(-1,80 < Z < 1,80) = P(Z < 1,80) - P(Z < -1,80) = 0,9641 - 0,0359 = 0,9282$. Maka peluang poros tidak lolos (harus didaur ulang) adalah $1 - 0,9282 = 0,0718$. Jadi, perkiraan banyak komponen yang didaur ulang adalah $5.000 \times 0,0718 = 359\text{ unit}$.</sub>
- D. $718\text{ unit}$  
  <sub>Salah: Siswa salah memperlakukan persentase kegagalan $0,0718$ sebagai desimal yang dikalikan basis $10.000$ bukan $5.000$.</sub>

**Pembahasan:** Transformasikan nilai batas ke nilai baku $Z$:
$$z_1 = \frac{39 - 48}{5} = -1,80$$
$$z_2 = \frac{57 - 48}{5} = 1,80$$
Peluang produk memenuhi standar spesifikasi:
$$P(39 < X < 57) = P(-1,80 < Z < 1,80) = P(Z < 1,80) - P(Z < -1,80) = 0,9641 - 0,0359 = 0,9282$$
Peluang produk gagal dan harus didaur ulang:
$$P(\text{daur ulang}) = 1 - 0,9282 = 0,0718$$
Banyaknya komponen yang harus didaur ulang:
$$N = 5.000 \times 0,0718 = 359\text{ unit}$$
**Acuan:** pretest — kelas12_tl-b04-p0292-latihan-soal-distribusi-normal-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b04-g-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: evaluasi probabilitas bersyarat distribusi normal*

Tabel distribusi normal baku menunjukkan nilai peluang kumulatif berikut:
- $P(Z < 0,50) = 0,6915$
- $P(Z < 1,50) = 0,9332$

Masa pakai lampu penerangan jalan berdistribusi normal dengan rata-rata $\mu = 4.000\text{ jam}$ dan simpangan baku $\sigma = 500\text{ jam}$. Sebuah lampu yang terpasang telah bertahan menyala selama $4.250\text{ jam}$. Peluang bahwa lampu tersebut masih akan terus berfungsi melampaui $4.750\text{ jam}$ adalah ....

- **A. $0,2165$** ✅  
  <sub>Benar: Nilai baku untuk $4.250\text{ jam}$ adalah $z_1 = \frac{4.250 - 4.000}{500} = 0,50$ sehingga $P(X > 4.250) = 1 - 0,6915 = 0,3085$. Nilai baku untuk $4.750\text{ jam}$ adalah $z_2 = \frac{4.750 - 4.000}{500} = 1,50$ sehingga $P(X > 4.750) = 1 - 0,9332 = 0,0668$. Peluang bersyaratnya adalah $P(X > 4.750 \mid X > 4.250) = \frac{P(X > 4.750)}{P(X > 4.250)} = \frac{0,0668}{0,3085} \approx 0,2165$.</sub>
- B. $0,2417$  
  <sub>Salah: Siswa salah mengira peluang bersyarat sebagai pengurangan selisih peluang langsung ($0,3085 - 0,0668$).</sub>
- C. $0,0668$  
  <sub>Salah: Siswa hanya menghitung peluang tanpa syarat bahwa lampu bertahan lebih dari $4.750\text{ jam}$.</sub>
- D. $0,0966$  
  <sub>Salah: Siswa membagi nilai $P(X > 4.750)$ dengan $P(X \le 4.250)$ yaitu $\frac{0,0668}{0,6915} \approx 0,0966$.</sub>

**Pembahasan:** Hitung nilai baku masing-masing ambang batas:
$$z_1 = \frac{4.250 - 4.000}{500} = 0,50$$
$$z_2 = \frac{4.750 - 4.000}{500} = 1,50$$
Tentukan peluang ekor kanan:
$$P(X > 4.250) = 1 - P(Z < 0,50) = 1 - 0,6915 = 0,3085$$
$$P(X > 4.750) = 1 - P(Z < 1,50) = 1 - 0,9332 = 0,0668$$
Karena kejadian $X > 4.750$ merupakan himpunan bagian dari $X > 4.250$, peluang bersyaratnya adalah:
$$P(X > 4.750 \mid X > 4.250) = \frac{P(X > 4.750 \cap X > 4.250)}{P(X > 4.250)} = \frac{P(X > 4.750)}{P(X > 4.250)} = \frac{0,0668}{0,3085} \approx 0,2165$$
**Acuan:** siswa — siswa hal.285

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b04-g-hard-bt01-019
*orisinal | C5 | 5 langkah | jenis: evaluasi spesifikasi mutu sistemik*

Tabel distribusi normal baku menunjukkan nilai peluang kumulatif berikut:
- $P(Z < -2,00) = 0,0228$
- $P(Z < -1,50) = 0,0668$
- $P(Z < 1,00) = 0,8413$

Kuat tarik kawat baja yang dihasilkan suatu mesin berdistribusi normal dengan rata-rata $\mu$ dan simpangan baku $\sigma$. Pengujian laboratorium menunjukkan bahwa sebanyak $6,68\%$ kawat memiliki kuat tarik kurang dari $470\text{ MPa}$, sedangkan $84,13\%$ kawat memiliki kuat tarik kurang dari $520\text{ MPa}$. Standar konstruksi menetapkan bahwa kawat baja dapat diterima jika memiliki kuat tarik minimal $460\text{ MPa}$. Persentase kawat baja yang memenuhi standar konstruksi tersebut adalah ....

- **A. $97,72\%$** ✅  
  <sub>Benar: Dari tabel, $P(Z < -1,50) = 0,0668$ dan $P(Z < 1,00) = 0,8413$, menghasilkan persamaan $\mu - 1,50\sigma = 470$ dan $\mu + 1,00\sigma = 520$. Selisihnya memberikan $2,50\sigma = 50 \implies \sigma = 20\text{ MPa}$ dan $\mu = 500\text{ MPa}$. Untuk kuat tarik minimal $460\text{ MPa}$, diperoleh skor baku $z = \frac{460 - 500}{20} = -2,00$. Peluang memenuhi standar adalah $P(X \ge 460) = 1 - P(Z < -2,00) = 1 - 0,0228 = 0,9772 = 97,72\%$.</sub>
- B. $93,32\%$  
  <sub>Salah: Siswa mengira batas minimal adalah $470\text{ MPa}$ sehingga langsung menghitung $1 - 0,0668 = 0,9332$.</sub>
- C. $2,28\%$  
  <sub>Salah: Siswa menghitung persentase kawat yang gagal memenuhi standar konstruksi ($P(Z < -2,00)$).</sub>
- D. $84,13\%$  
  <sub>Salah: Siswa langsung mengambil angka persentil kedua dari soal tanpa menelaah batas spesifikasi $460\text{ MPa}$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai baku dari peluang kumulatif yang diketahui:
- $P(X < 470) = 0,0668 \implies z_1 = -1,50$
- $P(X < 520) = 0,8413 \implies z_2 = 1,00$

Langkah 2: Menyusun dan menyelesaikan sistem persamaan linear:
$$\frac{470 - \mu}{\sigma} = -1,50 \implies \mu - 1,50\sigma = 470$$
$$\frac{520 - \mu}{\sigma} = 1,00 \implies \mu + 1,00\sigma = 520$$
Kurangkan persamaan kedua dengan persamaan pertama:
$$2,50\sigma = 50 \implies \sigma = 20\text{ MPa}$$
$$\mu = 520 - 1,00(20) = 500\text{ MPa}$$

Langkah 3: Menghitung skor baku untuk ambang batas spesifikasi $X = 460\text{ MPa}$:
$$z = \frac{460 - 500}{20} = -2,00$$

Langkah 4: Menghitung persentase kawat yang memenuhi standar ($X \ge 460\text{ MPa}$):
$$P(X \ge 460) = 1 - P(Z < -2,00) = 1 - 0,0228 = 0,9772 = 97,72\%$$
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12_tl-b04-g-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: evaluasi komparasi risiko cacat ganda*

Tabel distribusi normal baku menunjukkan nilai peluang kumulatif berikut:
- $P(Z < -1,00) = 0,1587$
- $P(Z < 1,50) = 0,9332$
- $P(Z < 2,00) = 0,9772$

Dua mesin pengisi cairan botol saus beroperasi secara terpisah:
- Mesin A: volume berdistribusi normal dengan rata-rata $\mu_A = 300\text{ ml}$ dan simpangan baku $\sigma_A = 4\text{ ml}$.
- Mesin B: volume berdistribusi normal dengan rata-rata $\mu_B = 305\text{ ml}$ dan simpangan baku $\sigma_B = 2\text{ ml}$.

Sebuah botol dinyatakan cacat jika volumenya kurang dari $296\text{ ml}$ (kurang isi) atau lebih dari $308\text{ ml}$ (meluap). Berdasarkan kriteria tersebut, selisih persentase total botol cacat antara Mesin A dan Mesin B adalah ....

- **A. $11,47\%$** ✅  
  <sub>Benar: Untuk Mesin A, batas bawah $z_1 = \frac{296-300}{4} = -1,00$ ($P = 0,1587$) dan batas atas $z_2 = \frac{308-300}{4} = 2,00$ ($P = 1 - 0,9772 = 0,0228$). Total cacat Mesin A adalah $0,1587 + 0,0228 = 0,1815 = 18,15\%$. Untuk Mesin B, batas bawah $z_1 = \frac{296-305}{2} = -4,50$ ($P \approx 0$) dan batas atas $z_2 = \frac{308-305}{2} = 1,50$ ($P = 1 - 0,9332 = 0,0668 = 6,68\%$). Total cacat Mesin B adalah $6,68\%$. Selisih persentase cacat keduanya adalah $18,15\% - 6,68\% = 11,47\%$.</sub>
- B. $9,19\%$  
  <sub>Salah: Siswa lupa memperhitungkan cacat meluap pada Mesin A dan hanya mengurangkan $15,87\% - 6,68\% = 9,19\%$.</sub>
- C. $24,83\%$  
  <sub>Salah: Siswa menjumlahkan total tingkat kecacatan kedua mesin bukannya mencari selisihnya ($18,15\% + 6,68\% = 24,83\%$).</sub>
- D. $4,40\%$  
  <sub>Salah: Siswa hanya membandingkan selisih persentase cacat meluap antara Mesin B dan Mesin A ($6,68\% - 2,28\% = 4,40\%$).</sub>

**Pembahasan:** Langkah 1: Menghitung persentase cacat Mesin A
- Cacat kurang isi ($X < 296\text{ ml}$):
$$z = \frac{296 - 300}{4} = -1,00 \implies P(Z < -1,00) = 0,1587$$
- Cacat meluap ($X > 308\text{ ml}$):
$$z = \frac{308 - 300}{4} = 2,00 \implies P(Z > 2,00) = 1 - 0,9772 = 0,0228$$
- Total cacat Mesin A:
$$P_A = 0,1587 + 0,0228 = 0,1815 = 18,15\%$$

Langkah 2: Menghitung persentase cacat Mesin B
- Cacat kurang isi ($X < 296\text{ ml}$):
$$z = \frac{296 - 305}{2} = -4,50 \implies P(Z < -4,50) \approx 0,0000$$
- Cacat meluap ($X > 308\text{ ml}$):
$$z = \frac{308 - 305}{2} = 1,50 \implies P(Z > 1,50) = 1 - 0,9332 = 0,0668$$
- Total cacat Mesin B:
$$P_B = 0,0000 + 0,0668 = 0,0668 = 6,68\%$$

Langkah 3: Menghitung selisih persentase cacat:
$$\Delta P = 18,15\% - 6,68\% = 11,47\%$$
**Acuan:** siswa — siswa hal.284

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
