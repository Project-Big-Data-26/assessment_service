# Lembar koreksi — kelas11 SMA11U-B2 subbab A: Lingkaran dan Busur Lingkaran

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11-b02-a-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: menghitung besar sudut keliling*

Pada sebuah lingkaran berpusat di $O$, titik $B$, $C$, dan $E$ terletak pada lingkaran. Jika $\angle BOC$ adalah sudut pusat yang menghadap busur $BC$ dengan besar $76^\circ$, dan $\angle BEC$ adalah sudut keliling yang juga menghadap busur $BC$, berapakah besar $\angle BEC$?

- A. $76^\circ$  
  <sub>Salah: Menganggap besar sudut keliling sama dengan besar sudut pusat.</sub>
- B. $152^\circ$  
  <sub>Salah: Mengalikan sudut pusat dengan 2 alih-alih membaginya dengan 2.</sub>
- **C. $38^\circ$** ✅  
  <sub>Benar: Besar sudut keliling adalah setengah dari besar sudut pusat yang menghadap busur yang sama, sehingga $\angle BEC = \frac{1}{2} \times 76^\circ = 38^\circ$.</sub>
- D. $104^\circ$  
  <sub>Salah: Menghitung sudut pelurus ($180^\circ - 76^\circ$).</sub>

**Pembahasan:** Sudut pusat $\angle BOC$ dan sudut keliling $\angle BEC$ sama-sama menghadap busur $BC$. Hubungan sudut pusat dan sudut keliling yang menghadap busur yang sama adalah:
$$\angle BEC = \frac{1}{2} \times \angle BOC = \frac{1}{2} \times 76^\circ = 38^\circ$$
**Acuan:** pretest — kelas11-b02-p0074-latihan-21-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11-b02-a-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: menghitung panjang sisi segitiga siku-siku dalam lingkaran*

Ruas garis $AB$ merupakan diameter sebuah lingkaran berjari-jari $5\text{ cm}$. Titik $C$ terletak pada lingkaran sehingga panjang tali busur $AC = 6\text{ cm}$. Tentukan panjang tali busur $BC$.

- A. $\sqrt{136}\text{ cm}$  
  <sub>Salah: Menjumlahkan kuadrat sisi-sisi alih-alih mengurangkan ($10^2 + 6^2 = 136$).</sub>
- B. $4\text{ cm}$  
  <sub>Salah: Menggunakan jari-jari alih-alih diameter dalam rumus Pythagoras sehingga menghitung $\sqrt{5^2 - 3^2}$.</sub>
- C. $7\text{ cm}$  
  <sub>Salah: Mengurangkan nilai diameter dan tali busur secara langsung ($10 - 6 + 3$ atau kesalahan hitung).</sub>
- **D. $8\text{ cm}$** ✅  
  <sub>Benar: Diameter $AB = 2 \times 5 = 10\text{ cm}$. Karena $AB$ diameter, $\angle ACB = 90^\circ$. Dengan teorema Pythagoras, $BC = \sqrt{AB^2 - AC^2} = \sqrt{10^2 - 6^2} = 8\text{ cm}$.</sub>

**Pembahasan:** Berdasarkan Teorema Thales, setiap sudut keliling yang menghadap diameter adalah sudut siku-siku, sehingga $\angle ACB = 90^\circ$.
Panjang diameter $AB = 2 \times 5\text{ cm} = 10\text{ cm}$.
Pada segitiga siku-siku $ABC$:
$$BC = \sqrt{AB^2 - AC^2} = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8\text{ cm}$$
**Acuan:** pretest — kelas11-b02-p0074-latihan-21-4c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11-b02-a-easy-bt01-003
*variasi (angka) | C1 | 1 langkah | jenis: menghitung panjang diameter lingkaran*

Sebuah lingkaran berpusat di titik $O$ memiliki panjang jari-jari $13{,}5\text{ cm}$. Jika ruas garis $PQ$ merupakan diameter lingkaran tersebut, berapakah panjang $PQ$?

- A. $6{,}75\text{ cm}$  
  <sub>Salah: Membagi jari-jari dengan 2 alih-alih mengalikannya dengan 2.</sub>
- **B. $27\text{ cm}$** ✅  
  <sub>Benar: Diameter lingkaran sama dengan dua kali jari-jari, yaitu $2 \times 13{,}5\text{ cm} = 27\text{ cm}$.</sub>
- C. $15{,}5\text{ cm}$  
  <sub>Salah: Menambahkan 2 pada jari-jari alih-alih mengalikannya dengan 2.</sub>
- D. $26\text{ cm}$  
  <sub>Salah: Salah mengalikan bilangan desimal dengan pembulatan ke bawah.</sub>

**Pembahasan:** Diameter adalah ruas garis yang melalui titik pusat dan menghubungkan dua titik pada lingkaran, dengan panjang dua kali jari-jari:
$$d = 2r = 2 \times 13{,}5\text{ cm} = 27\text{ cm}$$
**Acuan:** siswa — siswa hal.74 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11-b02-a-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: identifikasi istilah lingkaran*

Sudut yang titik sudutnya terletak pada lingkaran dan kaki-kaki sudutnya berupa tali busur lingkaran disebut ....

- **A. sudut keliling** ✅  
  <sub>Benar: Sesuai definisi pada materi, sudut yang titik sudutnya terletak pada lingkaran dan kaki-kakinya tali busur adalah sudut keliling.</sub>
- B. sudut pusat  
  <sub>Salah: Terkecoh dengan sudut yang titik sudutnya berada di titik pusat lingkaran.</sub>
- C. sudut busur  
  <sub>Salah: Menggunakan istilah busur secara keliru sebagai nama jenis sudut.</sub>
- D. sudut juring  
  <sub>Salah: Mengira nama daerah juring menjadi nama sudut yang bersangkutan.</sub>

**Pembahasan:** Berdasarkan definisi pada buku teks Matematika Kelas XI:
- Sudut pusat: sudut yang titik sudutnya terletak pada pusat lingkaran dan kaki-kakinya adalah jari-jari lingkaran.
- Sudut keliling: sudut yang titik sudutnya terletak pada lingkaran dan kaki-kaki sudutnya berupa tali busur.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11-b02-a-easy-bt01-005
*orisinal | C2 | 1 langkah | jenis: menghitung sudut keliling sebangun busur*

Titik $K$, $L$, $M$, dan $N$ terletak pada busur lingkaran yang sama. Sudut keliling $\angle KML$ dan $\angle KNL$ sama-sama menghadap ke busur $KL$. Jika besar $\angle KML = 44^\circ$, berapakah besar $\angle KNL$?

- A. $22^\circ$  
  <sub>Salah: Salah membagi besar sudut dengan 2 karena mengira hubungan sudut pusat dan keliling.</sub>
- B. $88^\circ$  
  <sub>Salah: Salah mengalikan besar sudut dengan 2 karena mengira salah satunya adalah sudut pusat.</sub>
- **C. $44^\circ$** ✅  
  <sub>Benar: Sudut keliling yang menghadap busur yang sama memiliki besar sudut yang sama, sehingga $\angle KNL = \angle KML = 44^\circ$.</sub>
- D. $136^\circ$  
  <sub>Salah: Mencari sudut pelurus ($180^\circ - 44^\circ$) tanpa alasan geometris yang tepat.</sub>

**Pembahasan:** Salah satu sifat sudut keliling adalah sudut-sudut keliling yang menghadap ke busur yang sama memiliki besar sudut yang sama. Karena $\angle KML$ dan $\angle KNL$ keduanya menghadap busur $KL$, maka:
$$\angle KNL = \angle KML = 44^\circ$$
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11-b02-a-easy-bt01-006
*variasi (angka) | C2 | 1 langkah | jenis: menghitung besar sudut keliling*

Diketahui titik $O$ merupakan pusat lingkaran, serta titik $B$, $C$, dan $E$ terletak pada lingkaran. Jika $\angle BOC = 116^\circ$ menghadap busur $BC$ dan $\angle BEC$ merupakan sudut keliling yang juga menghadap busur $BC$, tentukan besar $\angle BEC$.

- A. $232^\circ$  
  <sub>Salah: Mengalikan sudut pusat dengan 2 alih-alih membaginya dengan 2.</sub>
- **B. $58^\circ$** ✅  
  <sub>Benar: Besar sudut keliling sama dengan setengah dari besar sudut pusat yang menghadap busur yang sama: $\frac{1}{2} \times 116^\circ = 58^\circ$.</sub>
- C. $116^\circ$  
  <sub>Salah: Menganggap sudut keliling sama besar dengan sudut pusat.</sub>
- D. $64^\circ$  
  <sub>Salah: Menghitung sudut pelurus kemudian membaginya salah: $180^\circ - 116^\circ = 64^\circ$.</sub>

**Pembahasan:** Berdasarkan hubungan sudut pusat dan sudut keliling yang menghadap busur yang sama:
$$\angle BEC = \frac{1}{2} \times \angle BOC = \frac{1}{2} \times 116^\circ = 58^\circ$$
**Acuan:** pretest — kelas11-b02-p0074-latihan-21-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11-b02-a-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: menghitung panjang sisi segitiga siku-siku dalam lingkaran*

Ruas garis $AB$ adalah diameter lingkaran yang berjari-jari $6{,}5\text{ cm}$. Titik $C$ terletak pada lingkaran sehingga membentuk segitiga $ABC$ siku-siku di $C$. Jika panjang $AC = 5\text{ cm}$, berapakah panjang ruas garis $BC$?

- **A. $12\text{ cm}$** ✅  
  <sub>Benar: Diameter lingkaran $AB = 2 \times 6{,}5 = 13\text{ cm}$. Dengan teorema Pythagoras, $BC = \sqrt{AB^2 - AC^2} = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12\text{ cm}$.</sub>
- B. $4{,}15\text{ cm}$  
  <sub>Salah: Menggunakan panjang jari-jari $6{,}5\text{ cm}$ sebagai sisi miring segitiga.</sub>
- C. $8\text{ cm}$  
  <sub>Salah: Mengira tripel Pythagoras yang dipakai adalah kelipatan 3-4-5.</sub>
- D. $14\text{ cm}$  
  <sub>Salah: Menjumlahkan panjang diameter dan tali busur lalu dikurangi nilai tertentu atau salah hitung kuadrat.</sub>

**Pembahasan:** Panjang diameter $AB = 2 \times r = 2 \times 6{,}5 = 13\text{ cm}$.
Karena $\angle ACB$ menghadap diameter, $\triangle ABC$ siku-siku di $C$.
Panjang $BC$ diperoleh dari teorema Pythagoras:
$$BC = \sqrt{AB^2 - AC^2} = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12\text{ cm}$$
**Acuan:** pretest — kelas11-b02-p0074-latihan-21-4c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11-b02-a-easy-bt01-008
*variasi (angka) | C2 | 1 langkah | jenis: menghitung panjang diameter lingkaran*

Ruas garis $AB$ merupakan diameter sebuah lingkaran. Jika panjang jari-jari lingkaran tersebut adalah $7{,}5\text{ cm}$, berapakah panjang $AB$?

- A. $22{,}5\text{ cm}$  
  <sub>Salah: Mengalikan jari-jari dengan tiga.</sub>
- B. $14\text{ cm}$  
  <sub>Salah: Salah mengalikan bilangan desimal $2 \times 7{,}5$ menjadi 14.</sub>
- C. $3{,}75\text{ cm}$  
  <sub>Salah: Membagi jari-jari dengan dua alih-alih mengalikannya.</sub>
- **D. $15\text{ cm}$** ✅  
  <sub>Benar: Diameter lingkaran memiliki panjang dua kali jari-jarinya: $2 \times 7{,}5\text{ cm} = 15\text{ cm}$.</sub>

**Pembahasan:** Panjang diameter adalah dua kali panjang jari-jari:
$$AB = 2 \times r = 2 \times 7{,}5\text{ cm} = 15\text{ cm}$$
**Acuan:** siswa — siswa hal.74 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11-b02-a-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: identifikasi istilah lingkaran*

Ruas garis yang menghubungkan titik pusat lingkaran dengan salah satu titik pada keliling lingkaran disebut ....

- A. apotema  
  <sub>Salah: Tertukar dengan ruas garis tegak lurus dari titik pusat ke tali busur.</sub>
- B. diameter  
  <sub>Salah: Tertukar dengan ruas garis yang menghubungkan dua titik pada lingkaran dan melalui titik pusat.</sub>
- **C. jari-jari** ✅  
  <sub>Benar: Sesuai definisi pada materi buku, ruas garis dari titik pusat ke salah satu titik pada lingkaran adalah jari-jari.</sub>
- D. tali busur  
  <sub>Salah: Tertukar dengan ruas garis yang menghubungkan dua titik sembarang pada lingkaran.</sub>

**Pembahasan:** Ruas garis yang menghubungkan titik pusat lingkaran dengan salah satu titik pada lingkaran disebut jari-jari lingkaran.
**Acuan:** siswa — siswa hal.65

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11-b02-a-easy-bt01-010
*orisinal | C2 | 1 langkah | jenis: menghitung besar sudut pusat*

Sebuah sudut keliling yang menghadap busur $PQ$ memiliki besar $36^\circ$. Berapakah besar sudut pusat yang menghadap busur $PQ$ pada lingkaran yang sama?

- A. $144^\circ$  
  <sub>Salah: Mengalikan sudut keliling dengan 4 alih-alih dengan 2.</sub>
- B. $18^\circ$  
  <sub>Salah: Membagi sudut keliling dengan 2 alih-alih mengalikannya dengan 2.</sub>
- C. $54^\circ$  
  <sub>Salah: Menghitung sudut komplementer: $90^\circ - 36^\circ = 54^\circ$.</sub>
- **D. $72^\circ$** ✅  
  <sub>Benar: Sudut pusat besarnya dua kali sudut keliling yang menghadap busur yang sama: $2 \times 36^\circ = 72^\circ$.</sub>

**Pembahasan:** Berdasarkan sifat sudut lingkaran, besar sudut pusat adalah dua kali besar sudut keliling yang menghadap busur yang sama:
$$\text{Sudut pusat} = 2 \times 36^\circ = 72^\circ$$
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11-b02-a-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: menghitung sudut segitiga kaki jari-jari*

Titik $P$ adalah titik pusat sebuah lingkaran. Titik $A$ dan $B$ terletak pada keliling lingkaran tersebut sehingga membentuk sudut pusat $\angle APB = 80^\circ$. Berapakah besar $\angle PAB$?

- A. $80^\circ$  
  <sub>Salah: Siswa salah mengira segitiga $PAB$ adalah segitiga sama sisi sehingga semua sudutnya dianggap sama besar.</sub>
- **B. $50^\circ$** ✅  
  <sub>Benar: Segitiga $PAB$ sama kaki karena $PA = PB$ (jari-jari lingkaran). Maka $\angle PAB = \frac{180^\circ - 80^\circ}{2} = 50^\circ$.</sub>
- C. $40^\circ$  
  <sub>Salah: Siswa membagi dua sudut pusat $80^\circ : 2$ karena keliru menyamakan dengan rumus sudut keliling.</sub>
- D. $100^\circ$  
  <sub>Salah: Siswa hanya menghitung sisa sudut segitiga $180^\circ - 80^\circ$ tanpa membaginya untuk dua sudut sama kaki.</sub>

**Pembahasan:** Ruas garis $PA$ dan $PB$ merupakan jari-jari lingkaran, sehingga panjang $PA = PB$. Hal ini menjadikan $\Delta PAB$ segitiga sama kaki dengan $\angle PAB = \angle PBA$.

Jumlah sudut dalam segitiga adalah $180^\circ$, maka:
$$\angle PAB + \angle PBA + \angle APB = 180^\circ$$
$$2 \times \angle PAB + 80^\circ = 180^\circ$$
$$2 \times \angle PAB = 100^\circ$$
$$\angle PAB = 50^\circ$$
**Acuan:** siswa — siswa hal.75 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11-b02-a-easy-bt01-012
*variasi (angka) | C2 | 1 langkah | jenis: menghitung sudut penyinaran pusat*

Sebuah lampu taman diletakkan di tepi kolam melingkar pada titik $M$ dan menyorot perosotan sepanjang busur $BC$ dengan sudut penyinaran $35^\circ$. Jika pengelola memindahkan lampu ke titik pusat kolam $O$ untuk menyorot perosotan pada busur $BC$ yang sama, berapakah besar sudut penyinaran yang dibutuhkan?

- A. $17{,}5^\circ$  
  <sub>Salah: Siswa terbalik membagi dua sudut keliling bukannya mengalikan dua.</sub>
- B. $55^\circ$  
  <sub>Salah: Siswa mengurangkan sudut dari sudut siku-siku $90^\circ - 35^\circ$.</sub>
- **C. $70^\circ$** ✅  
  <sub>Benar: Sudut di pusat besarnya dua kali sudut di keliling yang menghadap busur yang sama: $2 \times 35^\circ = 70^\circ$.</sub>
- D. $35^\circ$  
  <sub>Salah: Siswa menganggap besar sudut penyinaran di pusat sama dengan sudut di tepi kolam.</sub>

**Pembahasan:** Lampu di tepi kolam (titik $M$) membentuk sudut keliling $\angle BMC = 35^\circ$. Saat lampu dipindahkan ke titik pusat kolam ($O$), sudut penyinaran yang terbentuk adalah sudut pusat $\angle BOC$ yang menghadap busur $BC$ yang sama.

Berdasarkan sifat lingkaran, besar sudut pusat adalah dua kali besar sudut keliling:
$$\angle BOC = 2 \times \angle BMC = 2 \times 35^\circ = 70^\circ$$
**Acuan:** siswa — siswa hal.68 Eksplorasi 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11-b02-a-easy-bt01-013
*variasi (konteks) | C2 | 1 langkah | jenis: identifikasi diameter dari sudut siku-siku*

Titik $P$, $Q$, dan $R$ terletak pada lingkaran. Jika segitiga $PQR$ memiliki sudut siku-siku di titik $Q$ ($\angle PQR = 90^\circ$), maka ruas garis yang pasti merupakan diameter lingkaran tersebut adalah ....

- A. tidak dapat ditentukan  
  <sub>Salah: Siswa tidak mengenali hubungan antara sudut keliling $90^\circ$ dengan sisi diameter lingkaran.</sub>
- **B. ruas garis $PR$** ✅  
  <sub>Benar: Berdasarkan Teorema Thales, sudut keliling siku-siku selalu menghadap diameter lingkaran, yaitu ruas garis $PR$.</sub>
- C. ruas garis $QR$  
  <sub>Salah: Siswa keliru mengira kaki sudut siku-siku yang lain merupakan diameter.</sub>
- D. ruas garis $PQ$  
  <sub>Salah: Siswa keliru mengira salah satu kaki sudut siku-siku merupakan diameter.</sub>

**Pembahasan:** Menurut Teorema Thales, sudut keliling yang besarnya $90^\circ$ (sudut siku-siku) selalu menghadap ke diameter lingkaran. Karena $\angle PQR = 90^\circ$, maka busur yang dihadapinya adalah busur $PR$ dan sisi di hadapan sudut tersebut, yaitu ruas garis $PR$, merupakan diameter lingkaran.
**Acuan:** siswa — siswa hal.74 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11-b02-a-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: menghitung sudut segitiga pada diameter*

Titik $K$, $L$, dan $M$ terletak pada lingkaran dengan ruas garis $KL$ sebagai diameter lingkaran. Jika besar $\angle KLM = 64^\circ$, berapakah besar $\angle MKL$?

- A. $64^\circ$  
  <sub>Salah: Siswa mengira segitiga tersebut adalah segitiga sama kaki sehingga besar sudutnya sama.</sub>
- B. $116^\circ$  
  <sub>Salah: Siswa mengurangkan sudut langsung dari sudut lurus $180^\circ - 64^\circ$.</sub>
- C. $32^\circ$  
  <sub>Salah: Siswa membagi dua besar sudut $\angle KLM$ ($64^\circ : 2$).</sub>
- **D. $26^\circ$** ✅  
  <sub>Benar: $\angle KML = 90^\circ$ karena menghadap diameter, sehingga $\angle MKL = 180^\circ - 90^\circ - 64^\circ = 26^\circ$.</sub>

**Pembahasan:** Karena ruas garis $KL$ merupakan diameter lingkaran, maka sudut keliling $\angle KML$ menghadap diameter sehingga $\angle KML = 90^\circ$.

Jumlah sudut dalam $\Delta KLM$ adalah $180^\circ$:
$$\angle MKL + \angle KLM + \angle KML = 180^\circ$$
$$\angle MKL + 64^\circ + 90^\circ = 180^\circ$$
$$\angle MKL + 154^\circ = 180^\circ$$
$$\angle MKL = 26^\circ$$
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11-b02-a-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: identifikasi definisi elemen sudut lingkaran*

Sudut yang titik sudutnya terletak pada pusat lingkaran dan kaki-kaki sudutnya berupa jari-jari lingkaran disebut ....

- **A. sudut pusat** ✅  
  <sub>Benar: Sesuai definisi pada buku, sudut dengan titik sudut di pusat lingkaran dan kaki jari-jari adalah sudut pusat.</sub>
- B. busur mayor  
  <sub>Salah: Busur mayor adalah bagian garis lengkung lingkaran yang lebih besar, bukan sudut.</sub>
- C. tali busur  
  <sub>Salah: Tali busur adalah ruas garis penghubung dua titik pada lingkaran, bukan sudut.</sub>
- D. sudut keliling  
  <sub>Salah: Sudut keliling memiliki titik sudut pada garis lingkaran, bukan di pusat.</sub>

**Pembahasan:** Sudut pusat adalah sudut yang titik sudutnya terletak pada pusat lingkaran dan kaki-kaki sudutnya adalah jari-jari lingkaran. Sedangkan sudut keliling titik sudutnya terletak pada garis lingkaran dan kaki-kakinya berupa tali busur.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11-b02-a-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: menghitung sudut pada segitiga sama kaki lingkaran*

Titik $A$ adalah pusat sebuah lingkaran berjarak jari-jari $4\text{ cm}$. Titik $C$ dan $D$ terletak pada lingkaran sehingga membentuk segitiga $ACD$. Jika besar sudut pusat $\angle CAD = 76^\circ$, tentukan besar $\angle ACD$.

- **A. $52^\circ$** ✅  
  <sub>Benar: Ruas garis $AC$ dan $AD$ adalah jari-jari lingkaran, sehingga panjang $AC = AD$ dan $\triangle ACD$ merupakan segitiga sama kaki dengan $\angle ACD = \angle ADC$. Jumlah sudut dalam segitiga adalah $180^\circ$, maka $\angle ACD = \frac{180^\circ - 76^\circ}{2} = \frac{104^\circ}{2} = 52^\circ$.</sub>
- B. $26^\circ$  
  <sub>Salah: Siswa menghitung nilai $52^\circ$ lalu membaginya lagi dengan dua.</sub>
- C. $104^\circ$  
  <sub>Salah: Siswa hanya menghitung sisa sudut $180^\circ - 76^\circ$ tetapi lupa membaginya dengan dua.</sub>
- D. $38^\circ$  
  <sub>Salah: Siswa membagi langsung sudut pusat $76^\circ$ dengan dua tanpa mengurangkan dari $180^\circ$ terlebih dahulu.</sub>

**Pembahasan:** Karena titik $C$ dan $D$ terletak pada lingkaran berpusat di $A$, maka panjang $AC = AD = r = 4\text{ cm}$. Hal ini berarti $\triangle ACD$ adalah segitiga sama kaki dengan alas $CD$, sehingga besar $\angle ACD = \angle ADC$.

Jumlah sudut dalam suatu segitiga adalah $180^\circ$:
$$\angle CAD + \angle ACD + \angle ADC = 180^\circ$$
$$76^\circ + 2\angle ACD = 180^\circ$$
$$2\angle ACD = 180^\circ - 76^\circ = 104^\circ$$
$$\angle ACD = \frac{104^\circ}{2} = 52^\circ$$
**Acuan:** siswa — siswa hal.75 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11-b02-a-easy-bt01-017
*variasi (angka) | C2 | 1 langkah | jenis: menentukan sudut penyinaran pusat*

Sebuah lampu diletakkan di tepi kolam melingkar dan menyorot perosotan pada busur $BC$ dengan sudut penyinaran $42^\circ$. Jika lampu tersebut dipindahkan ke titik pusat kolam untuk menyorot busur $BC$ yang sama, berapa besar sudut penyinaran yang dibutuhkan?

- A. $21^\circ$  
  <sub>Salah: Siswa keliru membagi sudut keliling dengan dua, bukannya mengalikan dua.</sub>
- B. $138^\circ$  
  <sub>Salah: Siswa menghitung sudut pelurus $180^\circ - 42^\circ$.</sub>
- **C. $84^\circ$** ✅  
  <sub>Benar: Lampu di tepi kolam bertindak sebagai sudut keliling, sedangkan lampu di pusat bertindak sebagai sudut pusat. Sudut pusat adalah dua kali sudut keliling yang menghadap busur yang sama: $2 \times 42^\circ = 84^\circ$.</sub>
- D. $42^\circ$  
  <sub>Salah: Siswa mengira sudut penyinaran di pusat sama besarnya dengan sudut penyinaran di tepi keliling.</sub>

**Pembahasan:** Sudut penyinaran lampu di tepi kolam merupakan sudut keliling lingkaran ($\theta = 42^\circ$) yang menghadap busur $BC$.

Ketika lampu diletakkan di titik pusat kolam dan menyorot busur $BC$ yang sama, sudut yang dibutuhkan adalah sudut pusat ($\alpha$).

Berdasarkan teorema sudut pada lingkaran:
$$\alpha = 2 \times \theta = 2 \times 42^\circ = 84^\circ$$

Jadi, sudut penyinaran yang dibutuhkan adalah $84^\circ$.
**Acuan:** siswa — siswa hal.68 Eksplorasi 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11-b02-a-easy-bt01-018
*variasi (angka) | C2 | 2 langkah | jenis: menghitung sudut keliling dari tali busur*

Lingkaran $A$ memiliki panjang jari-jari $5\text{ satuan}$. Titik $B$ dan $C$ terletak pada lingkaran sedemikian sehingga panjang tali busur $BC = 5\sqrt{2}\text{ satuan}$. Jika titik $D$ terletak pada busur mayor $BC$, berapakah besar sudut keliling $\angle BDC$?

- A. $30^\circ$  
  <sub>Salah: Siswa keliru menganggap segitiga $ABC$ sama sisi seperti pada contoh soal di buku.</sub>
- **B. $45^\circ$** ✅  
  <sub>Benar: Karena $AB = AC = 5$ dan $BC = 5\sqrt{2}$, berlaku $AB^2 + AC^2 = 5^2 + 5^2 = 50 = (5\sqrt{2})^2 = BC^2$, sehingga sudut pusat $\angle BAC = 90^\circ$. Sudut keliling $\angle BDC$ menghadap busur yang sama, sehingga besarnya adalah $\frac{1}{2} \times 90^\circ = 45^\circ$.</sub>
- C. $60^\circ$  
  <sub>Salah: Siswa mengira sudut keliling adalah $60^\circ$ berdasarkan segitiga sama sisi.</sub>
- D. $90^\circ$  
  <sub>Salah: Siswa menghitung sudut pusat $\angle BAC$ tetapi lupa menghitung sudut kelilingnya.</sub>

**Pembahasan:** Perhatikan segitiga $ABC$ di dalam lingkaran:
- $AB = r = 5$
- $AC = r = 5$
- $BC = 5\sqrt{2}$

Uji dengan Teorema Pythagoras:
$$AB^2 + AC^2 = 5^2 + 5^2 = 25 + 25 = 50$$
$$BC^2 = (5\sqrt{2})^2 = 50$$

Karena $AB^2 + AC^2 = BC^2$, maka $\triangle ABC$ siku-siku di $A$. Artinya, besar sudut pusat $\angle BAC = 90^\circ$.

Sudut keliling $\angle BDC$ menghadap busur yang sama dengan sudut pusat $\angle BAC$, sehingga:
$$\angle BDC = \frac{1}{2} \times \angle BAC = \frac{1}{2} \times 90^\circ = 45^\circ$$
**Acuan:** siswa — siswa hal.74 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11-b02-a-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: identifikasi definisi lingkaran*

Tempat kedudukan titik-titik yang jaraknya sama terhadap suatu titik tertentu pada suatu bidang datar dinamakan ....

- **A. lingkaran** ✅  
  <sub>Benar: Sesuai definisi pada buku, lingkaran adalah tempat kedudukan titik-titik yang jaraknya sama dari suatu titik tertentu (pusat lingkaran).</sub>
- B. tali busur  
  <sub>Salah: Siswa memilih ruas garis yang menghubungkan dua titik pada lingkaran.</sub>
- C. jari-jari  
  <sub>Salah: Siswa tertukar antara kurva himpunan titik (lingkaran) dengan ukuran jarak konstan tersebut (jari-jari).</sub>
- D. busur lingkaran  
  <sub>Salah: Siswa memilih bagian dari garis keliling lingkaran.</sub>

**Pembahasan:** Berdasarkan definisi geometri pada buku teks:
**Lingkaran** adalah tempat kedudukan titik-titik yang jaraknya sama dari suatu titik tertentu (disebut pusat lingkaran).

Jarak yang sama tersebut disebut jari-jari.
**Acuan:** siswa — siswa hal.65

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11-b02-a-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: identifikasi istilah busur lingkaran*

Bagian kurva lingkaran yang berukuran lebih kecil dari setengah keliling lingkaran disebut ....

- A. busur mayor  
  <sub>Salah: Siswa memilih bagian busur lingkaran yang lebih besar.</sub>
- B. daerah lingkaran  
  <sub>Salah: Siswa memilih daerah dua dimensi yang dibatasi oleh lingkaran.</sub>
- C. tali busur  
  <sub>Salah: Siswa tertukar antara ruas garis lurus dengan bagian lengkung lingkaran.</sub>
- **D. busur minor** ✅  
  <sub>Benar: Bagian kurva lingkaran yang lebih kecil disebut busur minor, sedangkan bagian yang lebih besar disebut busur mayor.</sub>

**Pembahasan:** Bagian dari garis lengkung lingkaran disebut busur lingkaran. Busur yang berukuran lebih kecil disebut **busur minor**, sedangkan busur yang berukuran lebih besar disebut **busur mayor**.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11-b02-a-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: sudut keliling dari tali busur*

Sebuah lingkaran berpusat di titik $P$ memiliki jari-jari $6\text{ cm}$. Titik $Q$ dan $R$ terletak pada lingkaran sehingga panjang tali busur $QR = 6\sqrt{3}\text{ cm}$. Jika titik $S$ terletak pada busur mayor lingkaran tersebut, berapakah besar sudut keliling $\angle QSR$?

- **A. $60^\circ$** ✅  
  <sub>Benar: Pada $\triangle PQR$, $PQ = PR = 6\text{ cm}$ dan $QR = 6\sqrt{3}\text{ cm}$. Berdasarkan aturan kosinus, $\cos \angle QPR = \frac{6^2 + 6^2 - (6\sqrt{3})^2}{2 \cdot 6 \cdot 6} = \frac{72 - 108}{72} = -\frac{1}{2}$, sehingga sudut pusat $\angle QPR = 120^\circ$. Besar sudut keliling $\angle QSR = \frac{1}{2} \times \angle QPR = \frac{1}{2} \times 120^\circ = 60^\circ$.</sub>
- B. $120^\circ$  
  <sub>Salah: Siswa hanya menghitung besar sudut pusat $\angle QPR$ dan lupa membaginya dengan dua.</sub>
- C. $45^\circ$  
  <sub>Salah: Siswa menduga segitiga yang terbentuk adalah siku-siku sama kaki.</sub>
- D. $30^\circ$  
  <sub>Salah: Siswa keliru mengira perbandingan sinus menghasilkan sudut keliling $30^\circ$.</sub>

**Pembahasan:** Langkah 1: Menentukan besar sudut pusat $\angle QPR$ dengan aturan kosinus pada $\triangle PQR$:
$$\cos \angle QPR = \frac{PQ^2 + PR^2 - QR^2}{2 \cdot PQ \cdot PR}$$
$$\cos \angle QPR = \frac{6^2 + 6^2 - (6\sqrt{3})^2}{2 \cdot 6 \cdot 6} = \frac{36 + 36 - 108}{72} = -\frac{36}{72} = -\frac{1}{2}$$
Diperoleh sudut pusat $\angle QPR = 120^\circ$.

Langkah 2: Menghitung sudut keliling $\angle QSR$ yang menghadap busur yang sama:
$$\angle QSR = \frac{1}{2} \times \angle QPR = \frac{1}{2} \times 120^\circ = 60^\circ$$
**Acuan:** siswa — siswa hal.74 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11-b02-a-medium-bt01-002
*variasi (angka) | C3 | 2 langkah | jenis: sudut segitiga dalam lingkaran*

Titik $P$ adalah pusat sebuah lingkaran berjarak jari-jari $7\text{ cm}$. Titik $K$ dan $L$ terletak pada keliling lingkaran tersebut sehingga membentuk sudut pusat $\angle KPL = 50^\circ$. Berapakah besar $\angle PKL$?

- A. $25^\circ$  
  <sub>Salah: Siswa mengira $\angle PKL$ adalah setengah dari sudut pusat $\angle KPL$.</sub>
- B. $130^\circ$  
  <sub>Salah: Siswa menghitung $180^\circ - 50^\circ$ tetapi lupa membaginya dengan dua.</sub>
- **C. $65^\circ$** ✅  
  <sub>Benar: Ruas garis $PK$ dan $PL$ merupakan jari-jari lingkaran sehingga panjangnya sama ($PK = PL$). Oleh karena itu, $\triangle PKL$ adalah segitiga sama kaki dengan $\angle PKL = \angle PLK$. Besar $\angle PKL = \frac{180^\circ - 50^\circ}{2} = 65^\circ$.</sub>
- D. $50^\circ$  
  <sub>Salah: Siswa mengira $\triangle PKL$ adalah segitiga sama sisi sehingga semua sudutnya sama.</sub>

**Pembahasan:** Langkah 1: Identifikasi jenis segitiga.
Karena $PK$ dan $PL$ adalah jari-jari lingkaran, maka $PK = PL = 7\text{ cm}$. Artinya, $\triangle PKL$ merupakan segitiga sama kaki, sehingga besar $\angle PKL = \angle PLK$.

Langkah 2: Menghitung besar $\angle PKL$.
Jumlah sudut dalam segitiga adalah $180^\circ$, maka:
$$\angle PKL + \angle PLK + \angle KPL = 180^\circ$$
$$2\angle PKL + 50^\circ = 180^\circ$$
$$2\angle PKL = 130^\circ$$
$$\angle PKL = 65^\circ$$
**Acuan:** siswa — siswa hal.75 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11-b02-a-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: persamaan sudut pusat dan keliling*

Pada sebuah lingkaran berpusat di $O$, sudut pusat $\angle AOB$ dan sudut keliling $\angle ACB$ sama-sama menghadap busur $AB$. Jika besar $\angle AOB = (3x + 20)^\circ$ dan $\angle ACB = (x + 25)^\circ$, berapakah besar $\angle AOB$?

- A. $35^\circ$  
  <sub>Salah: Siswa salah mengalikan ruas kanan menjadi $2x + 25$ sehingga memperoleh $x = 5$ dan $\angle AOB = 35^\circ$.</sub>
- B. $55^\circ$  
  <sub>Salah: Siswa menghitung besar sudut keliling $\angle ACB$, bukan sudut pusat $\angle AOB$.</sub>
- C. $30^\circ$  
  <sub>Salah: Siswa hanya mencari nilai variabel $x$ dan lupa mensubstitusikannya ke persamaan sudut.</sub>
- **D. $110^\circ$** ✅  
  <sub>Benar: Sudut pusat sama dengan dua kali sudut keliling yang menghadap busur yang sama, sehingga $3x + 20 = 2(x + 25) \iff 3x + 20 = 2x + 50 \iff x = 30$. Maka $\angle AOB = 3(30) + 20 = 110^\circ$.</sub>

**Pembahasan:** Langkah 1: Menyusun persamaan berdasarkan teorema sudut pusat dan sudut keliling.
$$\angle AOB = 2 \times \angle ACB$$
$$3x + 20 = 2(x + 25)$$

Langkah 2: Menyelesaikan nilai $x$.
$$3x + 20 = 2x + 50$$
$$3x - 2x = 50 - 20$$
$$x = 30$$

Langkah 3: Menghitung besar $\angle AOB$.
$$\angle AOB = 3(30) + 20 = 90 + 20 = 110^\circ$$
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11-b02-a-medium-bt01-004
*orisinal | C3 | 3 langkah | jenis: sudut segitiga menghadap diameter*

Titik $K$, $L$, dan $M$ terletak pada keliling sebuah lingkaran dengan ruas garis $KM$ sebagai diameter lingkaran. Jika besar sudut $\angle KML = (3x + 5)^\circ$ dan $\angle MKL = (2x + 10)^\circ$, berapakah besar $\angle KML$?

- A. $20^\circ$  
  <sub>Salah: Siswa menyamakan kedua sudut keliling $3x + 5 = 2x + 10$ sehingga diperoleh $x = 5$ dan $\angle KML = 20^\circ$.</sub>
- **B. $50^\circ$** ✅  
  <sub>Benar: Karena $KM$ adalah diameter, Teorema Thales menyatakan $\angle KLM = 90^\circ$. Maka $\angle KML + \angle MKL = 90^\circ \iff (3x + 5) + (2x + 10) = 90 \iff 5x + 15 = 90 \iff x = 15$. Besar $\angle KML = 3(15) + 5 = 50^\circ$.</sub>
- C. $40^\circ$  
  <sub>Salah: Siswa menghitung besar sudut $\angle MKL$, bukan $\angle KML$.</sub>
- D. $15^\circ$  
  <sub>Salah: Siswa berhenti pada perhitungan nilai $x$.</sub>

**Pembahasan:** Langkah 1: Menentukan besar $\angle KLM$.
Berdasarkan Teorema Thales, sudut keliling yang menghadap diameter besarnya $90^\circ$, sehingga $\angle KLM = 90^\circ$.

Langkah 2: Menentukan nilai $x$ dari jumlah sudut pada $\triangle KLM$.
$$\angle KML + \angle MKL + \angle KLM = 180^\circ$$
$$(3x + 5)^\circ + (2x + 10)^\circ + 90^\circ = 180^\circ$$
$$5x + 105 = 180$$
$$5x = 75$$
$$x = 15$$

Langkah 3: Menghitung besar $\angle KML$.
$$\angle KML = 3(15) + 5 = 45 + 5 = 50^\circ$$
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11-b02-a-medium-bt01-005
*orisinal | C3 | 2 langkah | jenis: kombinasi sudut pusat dan keliling*

Titik $P$, $Q$, dan $R$ terletak pada lingkaran sedemikian sehingga $\angle APB$, $\angle AQB$, dan $\angle ARB$ merupakan sudut-sudut keliling yang menghadap busur minor $AB$. Jika $\angle APB + \angle AQB + \angle ARB = 108^\circ$, berapakah besar sudut pusat $\angle AOB$ yang menghadap busur minor $AB$?

- A. $108^\circ$  
  <sub>Salah: Siswa mengira besar sudut pusat sama dengan jumlah ketiga sudut keliling tersebut.</sub>
- B. $36^\circ$  
  <sub>Salah: Siswa hanya menghitung besar salah satu sudut keliling dan lupa mengalikannya dengan dua.</sub>
- **C. $72^\circ$** ✅  
  <sub>Benar: Sudut-sudut keliling yang menghadap busur yang sama bernilai sama, sehingga $\angle APB = \angle AQB = \angle ARB = \frac{108^\circ}{3} = 36^\circ$. Besar sudut pusat $\angle AOB = 2 \times 36^\circ = 72^\circ$.</sub>
- D. $54^\circ$  
  <sub>Salah: Siswa membagi jumlah ketiga sudut keliling dengan dua ($108^\circ / 2$).</sub>

**Pembahasan:** Langkah 1: Menentukan besar masing-masing sudut keliling.
Karena $\angle APB$, $\angle AQB$, dan $\angle ARB$ menghadap busur yang sama ($AB$), maka besarnya sama:
$$\angle APB = \angle AQB = \angle ARB$$
$$3 \times \angle APB = 108^\circ$$
$$\angle APB = 36^\circ$$

Langkah 2: Menghitung besar sudut pusat $\angle AOB$.
Sudut pusat besarnya dua kali sudut keliling yang menghadap busur yang sama:
$$\angle AOB = 2 \times \angle APB = 2 \times 36^\circ = 72^\circ$$
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11-b02-a-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: panjang tali busur lingkaran*

Ruas garis $AB$ merupakan diameter pada sebuah lingkaran berjari-jari $12{,}5\text{ cm}$. Titik $C$ terletak pada lingkaran sehingga panjang tali busur $AC = 7\text{ cm}$. Tentukan panjang tali busur $BC$.

- **A. $24\text{ cm}$** ✅  
  <sub>Benar: Diameter lingkaran $AB = 2 \times 12{,}5\text{ cm} = 25\text{ cm}$. Karena $AB$ adalah diameter, maka sudut keliling $\angle ACB = 90^\circ$. Berdasarkan teorema Pythagoras pada segitiga siku-siku $ABC$, $BC = \sqrt{AB^2 - AC^2} = \sqrt{25^2 - 7^2} = \sqrt{625 - 49} = \sqrt{576} = 24\text{ cm}$.</sub>
- B. $17\text{ cm}$  
  <sub>Salah: Mengurangi diameter langsung dengan panjang tali busur yang diketahui ($25 - 8$ atau operasi pengurangan langsung tanpa Pythagoras).</sub>
- C. $20\text{ cm}$  
  <sub>Salah: Keliru mengira perbandingan tripel Pythagoras 3-4-5 dengan hipotenusa 25.</sub>
- D. $25\text{ cm}$  
  <sub>Salah: Mengira panjang $BC$ sama dengan panjang diameter lingkaran.</sub>

**Pembahasan:** Diameter $AB = 2r = 2 \times 12{,}5 = 25\text{ cm}$. Karena sudut $\angle ACB$ menghadap diameter lingkaran, maka $\angle ACB = 90^\circ$. Sesuai teorema Pythagoras pada segitiga $ABC$:
$$BC = \sqrt{AB^2 - AC^2} = \sqrt{25^2 - 7^2} = \sqrt{625 - 49} = \sqrt{576} = 24\text{ cm}.$$
**Acuan:** pretest — kelas11-b02-p0074-latihan-21-4c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11-b02-a-medium-bt01-007
*variasi (angka) | C3 | 2 langkah | jenis: panjang tali busur siku-siku*

Sebuah lingkaran berpusat di titik $P$ memiliki jari-jari $9\text{ cm}$. Titik $Q$ dan $R$ terletak pada lingkaran sedemikian sehingga besar sudut pusat $\angle QPR = 90^\circ$. Tentukan panjang tali busur $QR$.

- A. $9\sqrt{3}\text{ cm}$  
  <sub>Salah: Keliru menggunakan rumus sisi segitiga sama sisi atau salah rasio trigonometri.</sub>
- **B. $9\sqrt{2}\text{ cm}$** ✅  
  <sub>Benar: Ruas garis $PQ$ dan $PR$ keduanya merupakan jari-jari lingkaran sehingga $PQ = PR = 9\text{ cm}$. Karena $\angle QPR = 90^\circ$, segitiga $PQR$ adalah segitiga siku-siku di $P$. Dengan teorema Pythagoras, $QR = \sqrt{PQ^2 + PR^2} = \sqrt{9^2 + 9^2} = \sqrt{81 \times 2} = 9\sqrt{2}\text{ cm}$.</sub>
- C. $9\text{ cm}$  
  <sub>Salah: Mengira tali busur sama panjang dengan jari-jari lingkaran.</sub>
- D. $18\text{ cm}$  
  <sub>Salah: Menjumlahkan langsung kedua panjang jari-jari $9 + 9$.</sub>

**Pembahasan:** Segitiga $PQR$ adalah segitiga sama kaki dan siku-siku di $P$ karena $PQ = PR = r = 9\text{ cm}$ dan $\angle QPR = 90^\circ$. Maka:
$$QR = \sqrt{PQ^2 + PR^2} = \sqrt{9^2 + 9^2} = 9\sqrt{2}\text{ cm}.$$
**Acuan:** siswa — siswa hal.75 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11-b02-a-medium-bt01-008
*variasi (angka) | C3 | 2 langkah | jenis: sudut segitiga sama kaki lingkaran*

Sebuah lingkaran berpusat di titik $M$ memiliki panjang jari-jari $8\text{ cm}$. Titik $K$ dan $L$ terletak pada lingkaran sedemikian sehingga besar sudut pusat $\angle KML = 104^\circ$. Berapakah besar $\angle MKL$?

- **A. $38^\circ$** ✅  
  <sub>Benar: Ruas garis $MK$ dan $ML$ adalah jari-jari lingkaran, sehingga panjang $MK = ML = 8\text{ cm}$ dan $\triangle KLM$ adalah segitiga sama kaki dengan $\angle MKL = \angle MLK$. Jumlah sudut dalam segitiga adalah $180^\circ$, maka $\angle MKL = \frac{180^\circ - 104^\circ}{2} = \frac{76^\circ}{2} = 38^\circ$.</sub>
- B. $52^\circ$  
  <sub>Salah: Langsung membagi besar sudut pusat $104^\circ$ dengan 2.</sub>
- C. $42^\circ$  
  <sub>Salah: Keliru melakukan pengurangan $180^\circ - 104^\circ = 84^\circ$, lalu membaginya dengan 2.</sub>
- D. $76^\circ$  
  <sub>Salah: Hanya menghitung selisih sudut $180^\circ - 104^\circ$ tanpa membaginya menjadi dua sudut yang sama besar.</sub>

**Pembahasan:** Karena $MK = ML = r$, maka $\triangle KLM$ merupakan segitiga sama kaki dengan $\angle MKL = \angle MLK$. Jumlah sudut pada segitiga adalah $180^\circ$:
$$\angle MKL + \angle MLK + \angle KML = 180^\circ$$
$$2\angle MKL + 104^\circ = 180^\circ$$
$$2\angle MKL = 76^\circ$$
$$\angle MKL = 38^\circ.$$
**Acuan:** siswa — siswa hal.75 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11-b02-a-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: aljabar sudut pusat dan keliling*

Titik $O$ merupakan titik pusat lingkaran. Titik $A$, $B$, dan $C$ terletak pada lingkaran sehingga sudut pusat $\angle AOC$ dan sudut keliling $\angle ABC$ sama-sama menghadap busur $AC$. Jika jumlah besar kedua sudut tersebut adalah $135^\circ$ ($\angle AOC + \angle ABC = 135^\circ$), berapakah besar sudut pusat $\angle AOC$?

- A. $67{,}5^\circ$  
  <sub>Salah: Membagi dua secara langsung jumlah kedua sudut ($135^\circ / 2$).</sub>
- B. $45^\circ$  
  <sub>Salah: Menghitung besar sudut keliling $\angle ABC$, bukan sudut pusat $\angle AOC$.</sub>
- C. $100^\circ$  
  <sub>Salah: Keliru dalam operasi aljabar pembagian $135 / 3$.</sub>
- **D. $90^\circ$** ✅  
  <sub>Benar: Karena menghadap busur yang sama, berlaku $\angle AOC = 2 \times \angle ABC$. Substitusikan ke dalam persamaan: $2\angle ABC + \angle ABC = 135^\circ \implies 3\angle ABC = 135^\circ \implies \angle ABC = 45^\circ$. Dengan demikian, besar sudut pusat $\angle AOC = 2 \times 45^\circ = 90^\circ$.</sub>

**Pembahasan:** Berdasarkan hubungan sudut pusat dan sudut keliling yang menghadap busur sama:
$$\angle AOC = 2 \times \angle ABC$$
Diketahui:
$$\angle AOC + \angle ABC = 135^\circ$$
$$2\angle ABC + \angle ABC = 135^\circ$$
$$3\angle ABC = 135^\circ \implies \angle ABC = 45^\circ$$
Besar sudut pusat:
$$\angle AOC = 2 \times 45^\circ = 90^\circ.$$
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11-b02-a-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: aljabar sudut keliling diameter*

Pada sebuah lingkaran, ruas garis $AB$ adalah diameter lingkaran dan titik $C$ terletak pada keliling lingkaran. Jika besar $\angle BAC = (5x)^\circ$ dan besar $\angle ABC = (4x)^\circ$, berapakah nilai $x$?

- A. $15$  
  <sub>Salah: Keliru menganggap sudut keliling menghadap diameter bernilai $45^\circ$, sehingga $9x = 135$ menghasilkan $x = 15$.</sub>
- B. $20$  
  <sub>Salah: Mengabaikan fakta bahwa $\angle ACB = 90^\circ$ dan langsung membagi $180 / 9 = 20$.</sub>
- **C. $10$** ✅  
  <sub>Benar: Berdasarkan Teorema Thales, karena ruas garis $AB$ merupakan diameter, sudut keliling yang menghadap diameter adalah siku-siku, yaitu $\angle ACB = 90^\circ$. Jumlah sudut dalam segitiga $ABC$ adalah $180^\circ$: $\angle BAC + \angle ABC + \angle ACB = 180^\circ \implies 5x + 4x + 90 = 180 \implies 9x = 90 \implies x = 10$.</sub>
- D. $9$  
  <sub>Salah: Salah melakukan penyelesaian aljabar pada tahap $9x = 90$.</sub>

**Pembahasan:** Berdasarkan Teorema Thales, sudut keliling yang menghadap diameter bernilai siku-siku, sehingga $\angle ACB = 90^\circ$.
Jumlah sudut dalam $\triangle ABC$:
$$\angle BAC + \angle ABC + \angle ACB = 180^\circ$$
$$5x + 4x + 90 = 180$$
$$9x = 90$$
$$x = 10.$$
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11-b02-a-medium-bt01-011
*variasi (angka) | C3 | 2 langkah | jenis: sudut keliling tali busur sama sisi*

Lingkaran $P$ memiliki jari-jari sepanjang $6\text{ cm}$. Titik $A$, $B$, dan $C$ terletak pada lingkaran tersebut. Jika panjang tali busur $AB = 6\text{ cm}$ dan titik $C$ terletak pada busur mayor $AB$, berapakah besar sudut keliling $\angle ACB$?

- A. $60^\circ$  
  <sub>Salah: Siswa menjawab langsung besar sudut pusat tanpa membaginya dengan dua untuk sudut keliling.</sub>
- B. $120^\circ$  
  <sub>Salah: Siswa mengalikan sudut pusat dengan 2 alih-alih membaginya dengan 2.</sub>
- C. $45^\circ$  
  <sub>Salah: Siswa mengira segitiga yang terbentuk adalah segitiga siku-siku sama kaki dengan sudut pusat $90^\circ$ lalu membaginya dua.</sub>
- **D. $30^\circ$** ✅  
  <sub>Benar: Panjang jari-jari $PA = PB = 6\text{ cm}$ dan panjang tali busur $AB = 6\text{ cm}$, sehingga $\triangle PAB$ merupakan segitiga sama sisi dengan sudut pusat $\angle APB = 60^\circ$. Sudut $\angle ACB$ adalah sudut keliling yang menghadap busur $AB$, sehingga besarnya adalah $\frac{1}{2} \times 60^\circ = 30^\circ$.</sub>

**Pembahasan:** Segitiga $PAB$ dibentuk oleh dua jari-jari $PA = PB = 6\text{ cm}$ dan tali busur $AB = 6\text{ cm}$. Karena ketiga sisinya sama panjang, $\triangle PAB$ adalah segitiga sama sisi, sehingga besar sudut pusat $\angle APB = 60^\circ$.

Besar sudut keliling $\angle ACB$ yang menghadap busur $AB$ adalah setengah dari sudut pusatnya:
$$\angle ACB = \frac{1}{2} \times \angle APB = \frac{1}{2} \times 60^\circ = 30^\circ$$
**Acuan:** siswa — siswa hal.74 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11-b02-a-medium-bt01-012
*variasi (angka) | C3 | 2 langkah | jenis: panjang tali busur diameter*

Ruas garis $AB$ adalah diameter lingkaran yang berjari-jari $10\text{ cm}$. Titik $C$ terletak pada lingkaran sehingga panjang tali busur $AC = 12\text{ cm}$. Tentukan panjang tali busur $BC$.

- A. $23{,}3\text{ cm}$  
  <sub>Salah: Siswa menjumlahkan kuadrat sisi: $\sqrt{20^2 + 12^2} = \sqrt{544} \approx 23{,}3\text{ cm}$ karena mengira $BC$ adalah sisi miring.</sub>
- B. $8\text{ cm}$  
  <sub>Salah: Siswa salah menggunakan panjang jari-jari $10\text{ cm}$ sebagai sisi miring segitiga ($BC = \sqrt{10^2 - 12^2}$ tidak dapat dihitung atau mengurangkan nilai sembarangan).</sub>
- C. $14\text{ cm}$  
  <sub>Salah: Siswa salah menjumlahkan dan mengurangkan suku tanpa mengakar secara benar: $(20 + 12)/2 - 2 = 14$.</sub>
- **D. $16\text{ cm}$** ✅  
  <sub>Benar: Diameter $AB = 2 \times 10 = 20\text{ cm}$. Berdasarkan Teorema Thales, $\angle ACB = 90^\circ$. Maka $BC = \sqrt{AB^2 - AC^2} = \sqrt{20^2 - 12^2} = \sqrt{400 - 144} = \sqrt{256} = 16\text{ cm}$.</sub>

**Pembahasan:** Langkah 1: Menentukan panjang diameter $AB$.
$$AB = 2 \times r = 2 \times 10 = 20\text{ cm}$$

Langkah 2: Berdasarkan Teorema Thales, sudut keliling yang menghadap diameter adalah sudut siku-siku, sehingga $\angle ACB = 90^\circ$. Gunakan Teorema Pythagoras:
$$BC = \sqrt{AB^2 - AC^2} = \sqrt{20^2 - 12^2} = \sqrt{400 - 144} = \sqrt{256} = 16\text{ cm}$$
**Acuan:** pretest — kelas11-b02-p0074-latihan-21-4c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11-b02-a-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: aljabar sudut keliling dan pusat*

Titik $A$, $B$, $C$, dan $D$ terletak pada sebuah lingkaran berpusat di titik $O$. Sudut keliling $\angle ABD$ dan $\angle ACD$ sama-sama menghadap ke busur $AD$. Jika besar $\angle ABD = (2x + 15)^\circ$ dan besar $\angle ACD = (3x - 10)^\circ$, berapakah besar sudut pusat $\angle AOD$?

- A. $260^\circ$  
  <sub>Salah: Siswa mengalikan dua sebanyak dua kali ($65^\circ \times 4$).</sub>
- B. $50^\circ$  
  <sub>Salah: Siswa mengira nilai $2x = 50^\circ$ adalah besar sudut yang dicari.</sub>
- C. $65^\circ$  
  <sub>Salah: Siswa hanya menghitung besar sudut keliling dan lupa mengalikannya dengan dua untuk mendapatkan sudut pusat.</sub>
- **D. $130^\circ$** ✅  
  <sub>Benar: Karena menghadap busur yang sama, $\angle ABD = \angle ACD \implies 2x + 15 = 3x - 10 \implies x = 25$. Sudut keliling bernilai $2(25) + 15 = 65^\circ$. Sudut pusat $\angle AOD = 2 \times 65^\circ = 130^\circ$.</sub>

**Pembahasan:** Langkah 1: Karena $\angle ABD$ dan $\angle ACD$ menghadap busur yang sama ($AD$), maka besarnya sama:
$$2x + 15 = 3x - 10$$
$$3x - 2x = 15 + 10$$
$$x = 25$$

Langkah 2: Menghitung besar sudut keliling:
$$\angle ABD = 2(25) + 15 = 65^\circ$$

Langkah 3: Menghitung sudut pusat $\angle AOD$ yang menghadap busur $AD$:
$$\angle AOD = 2 \times \angle ABD = 2 \times 65^\circ = 130^\circ$$
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11-b02-a-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: sudut keliling dari segitiga sama kaki*

Titik $O$ adalah pusat sebuah lingkaran. Titik $A$ dan $B$ terletak pada keliling lingkaran sehingga membentuk segitiga sama kaki $OAB$ dengan $OA = OB$. Titik $C$ terletak pada busur mayor $AB$. Jika besar $\angle OBA = 54^\circ$, berapakah besar sudut keliling $\angle ACB$?

- A. $54^\circ$  
  <sub>Salah: Siswa mengira besar sudut keliling sama dengan besar sudut kaki segitiga.</sub>
- B. $27^\circ$  
  <sub>Salah: Siswa membagi sudut alas kaki segitiga ($54^\circ$) dengan dua alih-alih membagi sudut pusat.</sub>
- **C. $36^\circ$** ✅  
  <sub>Benar: $\triangle OAB$ sama kaki sehingga $\angle OAB = \angle OBA = 54^\circ$. Sudut pusat $\angle AOB = 180^\circ - (54^\circ + 54^\circ) = 72^\circ$. Sudut keliling $\angle ACB = \frac{1}{2} \times 72^\circ = 36^\circ$.</sub>
- D. $72^\circ$  
  <sub>Salah: Siswa berhenti pada langkah perhitungan sudut pusat tanpa membaginya dengan dua.</sub>

**Pembahasan:** Langkah 1: Segitiga $OAB$ memiliki sisi $OA = OB$ (keduanya jari-jari lingkaran), sehingga $\triangle OAB$ sama kaki dengan $\angle OAB = \angle OBA = 54^\circ$.

Langkah 2: Menghitung sudut pusat $\angle AOB$:
$$\angle AOB = 180^\circ - (54^\circ + 54^\circ) = 180^\circ - 108^\circ = 72^\circ$$

Langkah 3: Sudut $\angle ACB$ adalah sudut keliling yang menghadap busur yang sama dengan sudut pusat $\angle AOB$:
$$\angle ACB = \frac{1}{2} \times \angle AOB = \frac{1}{2} \times 72^\circ = 36^\circ$$
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11-b02-a-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: perbandingan sudut segitiga diameter*

Ruas garis $PQ$ merupakan diameter sebuah lingkaran. Titik $R$ terletak pada keliling lingkaran tersebut sehingga terbentuk segitiga $PQR$. Jika perbandingan besar $\angle PQR : \angle QPR = 2 : 3$, tentukan besar $\angle QPR$.

- **A. $54^\circ$** ✅  
  <sub>Benar: Berdasarkan Teorema Thales, sudut keliling menghadap diameter adalah $\angle PRQ = 90^\circ$. Maka $\angle PQR + \angle QPR = 90^\circ$. Dengan perbandingan $2 : 3$, besar $\angle QPR = \frac{3}{2 + 3} \times 90^\circ = \frac{3}{5} \times 90^\circ = 54^\circ$.</sub>
- B. $45^\circ$  
  <sub>Salah: Siswa membagi $90^\circ$ menjadi dua sama rata.</sub>
- C. $108^\circ$  
  <sub>Salah: Siswa menggunakan jumlah sudut segitiga $180^\circ$ langsung pada pecahan $\frac{3}{5} \times 180^\circ$ tanpa memperhitungkan sudut siku-siku $90^\circ$.</sub>
- D. $36^\circ$  
  <sub>Salah: Siswa menghitung sudut $\angle PQR$ yang berbanding 2, bukan $\angle QPR$.</sub>

**Pembahasan:** Langkah 1: Ruas garis $PQ$ adalah diameter lingkaran, sehingga menurut Teorema Thales besar sudut keliling $\angle PRQ = 90^\circ$.

Langkah 2: Jumlah sudut-sudut dalam $\triangle PQR$ adalah $180^\circ$, sehingga:
$$\angle PQR + \angle QPR = 180^\circ - 90^\circ = 90^\circ$$

Langkah 3: Diketahui perbandingan $\angle PQR : \angle QPR = 2 : 3$. Jumlah bagian perbandingan $= 2 + 3 = 5$. Maka besar $\angle QPR$ adalah:
$$\angle QPR = \frac{3}{5} \times 90^\circ = 54^\circ$$
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11-b02-a-medium-bt01-016
*variasi (angka) | C3 | 3 langkah | jenis: aljabar sudut pusat lingkaran*

Titik $O$ adalah pusat lingkaran, sedangkan titik $B$, $C$, dan $E$ terletak pada lingkaran. Sudut pusat $\angle BOC$ dan sudut keliling $\angle BEC$ sama-sama menghadap ke busur minor $BC$. Jika besar $\angle BOC = (4x + 16)^\circ$ dan besar $\angle BEC = (3x - 8)^\circ$, berapakah besar $\angle BEC$?

- A. $16^\circ$  
  <sub>Salah: Siswa berhenti setelah menemukan nilai $x$ tanpa menyubstitusikan ke besar sudut yang ditanyakan.</sub>
- **B. $40^\circ$** ✅  
  <sub>Benar: Sudut pusat besarnya dua kali sudut keliling: $4x + 16 = 2(3x - 8) \Leftrightarrow 4x + 16 = 6x - 16 \Leftrightarrow 2x = 32 \Leftrightarrow x = 16$. Nilai $\angle BEC = 3(16) - 8 = 40^\circ$.</sub>
- C. $80^\circ$  
  <sub>Salah: Siswa menghitung besar sudut pusat $\angle BOC$ bukan sudut keliling $\angle BEC$.</sub>
- D. $48^\circ$  
  <sub>Salah: Siswa hanya menghitung suku $3x$ yaitu $3 \times 16$ dan lupa mengurangkan 8.</sub>

**Pembahasan:** Sudut pusat besarnya dua kali sudut keliling yang menghadap busur yang sama:
$$\angle BOC = 2 \times \angle BEC$$
$$4x + 16 = 2(3x - 8)$$
$$4x + 16 = 6x - 16$$
$$6x - 4x = 16 + 16$$
$$2x = 32$$
$$x = 16$$

Substitusikan nilai $x = 16$ ke persamaan sudut keliling:
$$\angle BEC = (3(16) - 8)^\circ = (48 - 8)^\circ = 40^\circ$$
**Acuan:** pretest — kelas11-b02-p0074-latihan-21-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11-b02-a-medium-bt01-017
*variasi (angka) | C3 | 2 langkah | jenis: panjang tali busur sudut siku-siku*

Lingkaran $P$ memiliki panjang jari-jari $7\text{ cm}$. Titik $C$ dan $D$ terletak pada lingkaran tersebut sedemikian sehingga sudut pusat $\angle CPD = 90^\circ$. Berapakah panjang tali busur $CD$?

- A. $7\text{ cm}$  
  <sub>Salah: Siswa mengira segitiga $PCD$ adalah segitiga sama sisi sehingga panjang tali busur sama dengan panjang jari-jari.</sub>
- **B. $7\sqrt{2}\text{ cm}$** ✅  
  <sub>Benar: Ruas garis $PC$ dan $PD$ adalah jari-jari lingkaran ($PC = PD = 7\text{ cm}$). Segitiga $PCD$ siku-siku di $P$, sehingga $CD = \sqrt{7^2 + 7^2} = 7\sqrt{2}\text{ cm}$.</sub>
- C. $14\text{ cm}$  
  <sub>Salah: Siswa menjumlahkan panjang kedua jari-jari ($7 + 7$) seolah-olah membentuk garis lurus diameter.</sub>
- D. $7\sqrt{3}\text{ cm}$  
  <sub>Salah: Siswa tertukar dengan rumus tali busur yang menghadap sudut pusat $120^\circ$.</sub>

**Pembahasan:** Karena $PC$ dan $PD$ adalah jari-jari lingkaran, maka $PC = PD = 7\text{ cm}$.
Diketahui $\angle CPD = 90^\circ$, sehingga segitiga $PCD$ adalah segitiga siku-siku di $P$.
Berdasarkan teorema Pythagoras:
$$CD = \sqrt{PC^2 + PD^2}$$
$$CD = \sqrt{7^2 + 7^2} = \sqrt{49 + 49} = \sqrt{98} = 7\sqrt{2}\text{ cm}$$
**Acuan:** siswa — siswa hal.75 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11-b02-a-medium-bt01-018
*variasi (konteks) | C3 | 3 langkah | jenis: aplikasi sudut pusat dan keliling*

Sebuah panggung pertunjukan memiliki batas depan berbentuk busur lingkaran $AB$. Sebuah lampu penyorot diletakkan di tepi tribun penonton yang berada pada keliling lingkaran dan menyinari busur $AB$ dengan sudut penyinaran $(2x + 12)^\circ$. Jika lampu serupa diletakkan di titik pusat panggung untuk menyinari busur $AB$ yang sama, sudut penyinaran yang dibutuhkan adalah $(5x - 6)^\circ$. Berapakah besar sudut penyinaran lampu jika diletakkan di pusat panggung?

- **A. $144^\circ$** ✅  
  <sub>Benar: Sudut di pusat panggung merupakan sudut pusat dan sudut di tepi tribun merupakan sudut keliling: $5x - 6 = 2(2x + 12) \Leftrightarrow 5x - 6 = 4x + 24 \Leftrightarrow x = 30$. Sudut pusat $= 5(30) - 6 = 144^\circ$.</sub>
- B. $108^\circ$  
  <sub>Salah: Siswa melakukan kesalahan perhitungan aljabar saat memindahkan ruas konstanta.</sub>
- C. $72^\circ$  
  <sub>Salah: Siswa menghitung besar sudut penyinaran dari tepi tribun ($2(30) + 12$), bukan dari pusat panggung.</sub>
- D. $30^\circ$  
  <sub>Salah: Siswa berhenti pada pencarian nilai variabel $x$.</sub>

**Pembahasan:** Sudut lampu di pusat lingkaran adalah sudut pusat, sedangkan sudut lampu di tepi tribun adalah sudut keliling yang menghadap busur yang sama ($AB$).
$$\text{Sudut Pusat} = 2 \times \text{Sudut Keliling}$$
$$5x - 6 = 2(2x + 12)$$
$$5x - 6 = 4x + 24$$
$$5x - 4x = 24 + 6$$
$$x = 30$$

Besar sudut penyinaran dari pusat panggung:
$$(5(30) - 6)^\circ = (150 - 6)^\circ = 144^\circ$$
**Acuan:** siswa — siswa hal.68 Eksplorasi 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11-b02-a-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: trigonometri segitiga diameter lingkaran*

Ruas garis $AB$ merupakan diameter sebuah lingkaran dengan panjang jari-jari $10\text{ cm}$. Titik $C$ terletak pada keliling lingkaran sehingga membentuk segitiga $ABC$. Jika besar $\angle BAC = 60^\circ$, berapakah panjang sisi $BC$?

- A. $10\text{ cm}$  
  <sub>Salah: Siswa menghitung panjang sisi $AC$ menggunakan $\cos(60^\circ)$ bukan sisi $BC$.</sub>
- **B. $10\sqrt{3}\text{ cm}$** ✅  
  <sub>Benar: Menurut Teorema Thales, karena $AB$ diameter maka $\angle ACB = 90^\circ$. Panjang $AB = 2 \times 10 = 20\text{ cm}$. Sisi $BC = AB \times \sin(60^\circ) = 20 \times \frac{1}{2}\sqrt{3} = 10\sqrt{3}\text{ cm}$.</sub>
- C. $10\sqrt{2}\text{ cm}$  
  <sub>Salah: Siswa mengasumsikan segitiga siku-siku sama kaki dengan sudut $45^\circ$.</sub>
- D. $20\sqrt{3}\text{ cm}$  
  <sub>Salah: Siswa langsung mengalikan panjang diameter dengan $\sqrt{3}$ tanpa mengalikan nilai $\sin(60^\circ) = \frac{1}{2}\sqrt{3}$.</sub>

**Pembahasan:** 1. Karena ruas garis $AB$ merupakan diameter lingkaran, maka berdasarkan Teorema Thales sudut keliling yang menghadap diameter adalah siku-siku:
$$\angle ACB = 90^\circ$$

2. Diameter lingkaran:
$$AB = 2 \times r = 2 \times 10 = 20\text{ cm}$$

3. Pada segitiga siku-siku $ABC$:
$$\sin(\angle BAC) = \frac{BC}{AB}$$
$$\sin(60^\circ) = \frac{BC}{20}$$
$$BC = 20 \times \frac{1}{2}\sqrt{3} = 10\sqrt{3}\text{ cm}$$
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11-b02-a-medium-bt01-020
*orisinal | C3 | 2 langkah | jenis: sudut refleks dan sudut keliling*

Titik $K$, $L$, dan $M$ terletak pada keliling lingkaran yang berpusat di titik $O$. Diketahui sudut pusat refleks $\angle KOM$ memiliki besar $236^\circ$. Jika sudut keliling $\angle KLM$ menghadap ke busur minor $KM$, berapakah besar $\angle KLM$?

- A. $59^\circ$  
  <sub>Salah: Siswa membagi sudut keliling pelurus ($118^\circ : 2$) karena kekeliruan konsep.</sub>
- B. $124^\circ$  
  <sub>Salah: Siswa hanya menghitung besar sudut pusat minor dan lupa membaginya dengan 2.</sub>
- **C. $62^\circ$** ✅  
  <sub>Benar: Sudut pusat minor $\angle KOM = 360^\circ - 236^\circ = 124^\circ$. Sudut keliling $\angle KLM = \frac{1}{2} \times 124^\circ = 62^\circ$.</sub>
- D. $118^\circ$  
  <sub>Salah: Siswa membagi langsung sudut refleks dengan 2 ($236^\circ : 2 = 118^\circ$) yang merupakan sudut keliling menghadap busur mayor.</sub>

**Pembahasan:** 1. Satu putaran penuh sudut adalah $360^\circ$. Sudut pusat minor $\angle KOM$ yang menghadap busur minor $KM$ adalah:
$$\angle KOM = 360^\circ - 236^\circ = 124^\circ$$

2. Sudut keliling $\angle KLM$ menghadap ke busur minor $KM$ yang sama dengan sudut pusat minor $\angle KOM$, sehingga:
$$\angle KLM = \frac{1}{2} \times \angle KOM$$
$$\angle KLM = \frac{1}{2} \times 124^\circ = 62^\circ$$
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11-b02-a-hard-bt01-001
*variasi (angka) | C5 | 5 langkah | jenis: segitiga dalam lingkaran*

Ruas garis $AB$ merupakan diameter sebuah lingkaran dengan panjang jari-jari $13\text{ cm}$. Titik $C$ terletak pada lingkaran sedemikian sehingga keliling segitiga $ABC$ adalah $60\text{ cm}$. Luas segitiga $ABC$ tersebut adalah ....

- **A. $120\text{ cm}^2$** ✅  
  <sub>Benar: Karena $AB$ adalah diameter, Teorema Thales menyatakan bahwa $\angle ACB = 90^\circ$. Panjang diameter $AB = 2 \times 13 = 26\text{ cm}$. Dari keliling segitiga diperoleh $AC + BC = 60 - 26 = 34\text{ cm}$. Menurut teorema Pythagoras, $AC^2 + BC^2 = AB^2 = 26^2 = 676$. Menggunakan identitas aljabar: $(AC + BC)^2 = AC^2 + BC^2 + 2(AC \times BC) \Rightarrow 34^2 = 676 + 2(AC \times BC) \Rightarrow 1.156 - 676 = 2(AC \times BC) \Rightarrow 2(AC \times BC) = 480 \Rightarrow AC \times BC = 240$. Luas segitiga $ABC = \frac{1}{2} \times AC \times BC = \frac{1}{2} \times 240 = 120\text{ cm}^2$.</sub>
- B. $240\text{ cm}^2$  
  <sub>Salah: Siswa lupa mengalikan dengan faktor setengah pada rumus luas segitiga siku-siku.</sub>
- C. $156\text{ cm}^2$  
  <sub>Salah: Siswa langsung mengalikan jari-jari dengan setengah keliling alas secara keliru ($13 \times 12$).</sub>
- D. $60\text{ cm}^2$  
  <sub>Salah: Siswa membagi luas yang benar dengan dua karena salah mengira rumus luas segitiga.</sub>

**Pembahasan:** Langkah 1: Tentukan panjang diameter $AB = 2r = 2 \times 13\text{ cm} = 26\text{ cm}$.
Langkah 2: Berdasarkan Teorema Thales, sudut keliling yang menghadap diameter adalah siku-siku, sehingga $\angle ACB = 90^\circ$ dan berlaku $AC^2 + BC^2 = 26^2 = 676$.
Langkah 3: Dari keliling segitiga $ABC = 60\text{ cm}$, maka $AC + BC + 26 = 60 \Rightarrow AC + BC = 34\text{ cm}$.
Langkah 4: Gunakan pengkuadratan aljabar:
$(AC + BC)^2 = AC^2 + BC^2 + 2 \cdot AC \cdot BC$
$34^2 = 676 + 2 \cdot AC \cdot BC$
$1.156 = 676 + 2 \cdot AC \cdot BC$
$2 \cdot AC \cdot BC = 480 \Rightarrow AC \cdot BC = 240$.
Langkah 5: Hitung luas segitiga:
$\text{Luas } \triangle ABC = \frac{1}{2} \times AC \times BC = \frac{1}{2} \times 240 = 120\text{ cm}^2$.
**Acuan:** pretest — kelas11-b02-p0074-latihan-21-4c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11-b02-a-hard-bt01-002
*variasi (konteks) | C5 | 4 langkah | jenis: selisih sudut busur lingkaran*

Sebuah lingkaran berpusat di titik $O$ memiliki panjang jari-jari $6\text{ cm}$. Dua titik $P$ dan $Q$ terletak pada lingkaran sehingga panjang tali busur $PQ = 6\sqrt{3}\text{ cm}$. Titik $R$ terletak pada busur mayor $PQ$, sedangkan titik $S$ terletak pada busur minor $PQ$. Selisih antara besar $\angle PSQ$ dan $\angle PRQ$ adalah ....

- A. $0^\circ$  
  <sub>Salah: Siswa beranggapan semua sudut keliling besarnya sama tanpa membedakan posisi pada busur mayor dan minor.</sub>
- B. $30^\circ$  
  <sub>Salah: Siswa salah menghitung $\angle PRQ$ sebagai setengah dari $60^\circ$ bukannya setengah dari $120^\circ$.</sub>
- **C. $60^\circ$** ✅  
  <sub>Benar: Pada $\triangle OPQ$, panjang $OP = OQ = 6$ dan $PQ = 6\sqrt{3}$. Melalui aturan cosinus: $\cos \angle POQ = \frac{6^2 + 6^2 - (6\sqrt{3})^2}{2 \cdot 6 \cdot 6} = \frac{72 - 108}{72} = -\frac{1}{2}$, sehingga sudut pusat minor $\angle POQ = 120^\circ$. Titik $R$ pada busur mayor menghadap busur minor $PQ$, sehingga $\angle PRQ = \frac{1}{2} \times 120^\circ = 60^\circ$. Titik $S$ pada busur minor menghadap busur mayor $PQ$ yang bersudut pusat $360^\circ - 120^\circ = 240^\circ$, sehingga $\angle PSQ = \frac{1}{2} \times 240^\circ = 120^\circ$. Selisihnya adalah $|120^\circ - 60^\circ| = 60^\circ$.</sub>
- D. $90^\circ$  
  <sub>Salah: Siswa keliru menganggap kedua sudut keliling tersebut saling berkomplemen.</sub>

**Pembahasan:** Langkah 1: Hitung besar sudut pusat $\angle POQ$ menggunakan aturan cosinus pada $\triangle OPQ$ dengan $OP = 6$, $OQ = 6$, dan $PQ = 6\sqrt{3}$:
$\cos \angle POQ = \frac{6^2 + 6^2 - (6\sqrt{3})^2}{2 \times 6 \times 6} = \frac{36 + 36 - 108}{72} = -\frac{36}{72} = -\frac{1}{2}$
Maka sudut pusat minor $\angle POQ = 120^\circ$.
Langkah 2: Hitung besar $\angle PRQ$. Titik $R$ berada di busur mayor dan menghadap busur minor $PQ$:
$\angle PRQ = \frac{1}{2} \times 120^\circ = 60^\circ$.
Langkah 3: Hitung besar $\angle PSQ$. Titik $S$ berada di busur minor dan menghadap busur mayor $PQ$. Sudut pusat busur mayor $= 360^\circ - 120^\circ = 240^\circ$:
$\angle PSQ = \frac{1}{2} \times 240^\circ = 120^\circ$.
Langkah 4: Hitung selisih kedua sudut:
$|\angle PSQ - \angle PRQ| = |120^\circ - 60^\circ| = 60^\circ$.
**Acuan:** siswa — siswa hal.74 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11-b02-a-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: geometri sudut lingkaran*

Pada sebuah lingkaran dengan pusat $O$, sudut pusat $\angle AOB = (4x + 16)^\circ$ dan sudut keliling $\angle ACB = (3x - 14)^\circ$ sama-sama menghadap busur minor $AB$. Jika titik $D$ terletak pada busur minor $AB$, berapakah besar sudut keliling $\angle ADB$?

- A. $76^\circ$  
  <sub>Salah: Siswa menghitung pelurus dari sudut pusat $180^\circ - 104^\circ$.</sub>
- B. $104^\circ$  
  <sub>Salah: Siswa menjawab sebesar sudut pusat busur minor $\angle AOB$.</sub>
- C. $52^\circ$  
  <sub>Salah: Siswa mengira $\angle ADB$ sama besar dengan $\angle ACB$ karena sama-sama sudut keliling lingkaran.</sub>
- **D. $128^\circ$** ✅  
  <sub>Benar: Sudut pusat sama dengan dua kali sudut keliling yang menghadap busur yang sama: $4x + 16 = 2(3x - 14) \Rightarrow 4x + 16 = 6x - 28 \Rightarrow 2x = 44 \Rightarrow x = 22$. Sudut pusat busur minor adalah $\angle AOB = 4(22) + 16 = 104^\circ$. Karena titik $D$ berada pada busur minor $AB$, maka $\angle ADB$ menghadap ke busur mayor $AB$. Sudut pusat busur mayor $= 360^\circ - 104^\circ = 256^\circ$. Dengan demikian, $\angle ADB = \frac{1}{2} \times 256^\circ = 128^\circ$.</sub>

**Pembahasan:** Langkah 1: Gunakan hubungan sudut pusat dan keliling pada busur minor $AB$:
$\angle AOB = 2 \times \angle ACB$
$4x + 16 = 2(3x - 14)$
Langkah 2: Selesaikan persamaan linier:
$4x + 16 = 6x - 28$
$2x = 44 \Rightarrow x = 22$.
Langkah 3: Hitung sudut pusat busur minor $\angle AOB$:
$\angle AOB = 4(22) + 16 = 104^\circ$.
Langkah 4: Hitung sudut pusat busur mayor $AB$ yang dihadapi oleh $\angle ADB$:
$\text{Sudut refleks } \angle AOB = 360^\circ - 104^\circ = 256^\circ$.
Langkah 5: Tentukan besar sudut keliling $\angle ADB$:
$\angle ADB = \frac{1}{2} \times 256^\circ = 128^\circ$.
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11-b02-a-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: sudut perpotongan tali busur*

Ruas garis $AB$ merupakan diameter sebuah lingkaran. Titik $C$ terletak pada lingkaran sehingga $\angle ABC = 58^\circ$. Titik $D$ terletak pada busur $BC$ sedemikian sehingga garis $AD$ memotong tali busur $BC$ di titik $E$. Jika besar $\angle BAD = 22^\circ$, berapakah besar sudut $\angle AEB$?

- A. $90^\circ$  
  <sub>Salah: Siswa salah berasumsi bahwa garis $AD$ dan $BC$ berpotongan tegak lurus.</sub>
- B. $110^\circ$  
  <sub>Salah: Siswa keliru menghitung selisih sudut dalam $\triangle ABC$.</sub>
- C. $80^\circ$  
  <sub>Salah: Siswa hanya menjumlahkan dua sudut yang diketahui ($22^\circ + 58^\circ$) tanpa mengurangkannya dari $180^\circ$.</sub>
- **D. $100^\circ$** ✅  
  <sub>Benar: Berdasarkan Teorema Thales, karena $AB$ adalah diameter lingkaran, maka $\angle ACB = 90^\circ$. Pada segitiga $ABC$, $\angle CAB = 180^\circ - 90^\circ - 58^\circ = 32^\circ$. Ruas garis $AD$ berada di antara kaki sudut $\angle CAB$ dengan $\angle BAD = 22^\circ$. Perhatikan segitiga $ABE$, titik $E$ terletak pada ruas garis $AD$ dan $BC$, sehingga sudut-sudut segitiga $ABE$ adalah $\angle BAE = \angle BAD = 22^\circ$ dan $\angle ABE = \angle ABC = 58^\circ$. Jumlah sudut dalam segitiga $ABE$ adalah $180^\circ$, sehingga $\angle AEB = 180^\circ - (22^\circ + 58^\circ) = 180^\circ - 80^\circ = 100^\circ$.</sub>

**Pembahasan:** Langkah 1: Terapkan Teorema Thales pada $\triangle ABC$. Karena $AB$ diameter, $\angle ACB = 90^\circ$.
Langkah 2: Tentukan besar $\angle CAB$ dalam $\triangle ABC$:
$\angle CAB = 180^\circ - (90^\circ + 58^\circ) = 32^\circ$.
Langkah 3: Identifikasi sudut-sudut pada segitiga $ABE$:
Titik $E$ adalah titik potong $AD$ dan $BC$, sehingga ruas garis $AE$ berimpit dengan $AD$ dan ruas garis $BE$ berimpit dengan $BC$.
Didapatkan $\angle BAE = \angle BAD = 22^\circ$ dan $\angle ABE = \angle ABC = 58^\circ$.
Langkah 4: Hitung besar $\angle AEB$ menggunakan jumlah sudut dalam $\triangle ABE$:
$\angle AEB = 180^\circ - (\angle BAE + \angle ABE) = 180^\circ - (22^\circ + 58^\circ) = 180^\circ - 80^\circ = 100^\circ$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11-b02-a-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: aplikasi sudut lingkaran*

Dua mercusuar $P$ dan $Q$ terletak pada batas lingkaran zona bahaya karang yang berpusat di $O$. Sudut pusat busur minor karang tersebut adalah $\angle POQ = 80^\circ$. Sebuah kapal $K$ bernavigasi dan mengamati kedua mercusuar dengan mengukur sudut pandang $\angle PKQ$ pada sisi yang sama dengan busur mayor. Agar kapal dipastikan berada di luar zona bahaya lingkaran tersebut, kapten kapal harus menjaga agar besar sudut $\angle PKQ$ memenuhi syarat ....

- **A. $\angle PKQ < 40^\circ$** ✅  
  <sub>Benar: Jika kapal berada tepat pada keliling lingkaran, sudut keliling yang terbentuk menghadap busur minor $PQ$ adalah $\frac{1}{2} \times \angle POQ = \frac{1}{2} \times 80^\circ = 40^\circ$. Berdasarkan sifat geometris, jika titik pengamatan menjauh ke luar lingkaran, sudut pandang terhadap tali busur $PQ$ akan mengecil (kurang dari sudut keliling lingkaran). Sebaliknya, jika kapal masuk ke dalam lingkaran zona bahaya, sudut pandang akan membesar ($> 40^\circ$). Jadi, syarat agar kapal berada di luar zona bahaya adalah $\angle PKQ < 40^\circ$.</sub>
- B. $\angle PKQ > 40^\circ$  
  <sub>Salah: Siswa terbalik mengira bahwa berada di luar lingkaran menghasilkan sudut pandang yang lebih besar daripada sudut keliling.</sub>
- C. $\angle PKQ = 40^\circ$  
  <sub>Salah: Siswa memilih kondisi saat kapal berada tepat pada batas lingkaran zona bahaya.</sub>
- D. $\angle PKQ < 80^\circ$  
  <sub>Salah: Siswa membandingkan langsung dengan sudut pusat $80^\circ$ bukannya sudut keliling lingkaran.</sub>

**Pembahasan:** Langkah 1: Hitung besar sudut batas saat kapal berada tepat pada keliling lingkaran. Sudut keliling yang menghadap busur minor $PQ$ adalah:
$\angle PKQ_{\text{batas}} = \frac{1}{2} \times \angle POQ = \frac{1}{2} \times 80^\circ = 40^\circ$.
Langkah 2: Analisis posisi titik pengamat terhadap lingkaran:
- Titik pada lingkaran memiliki besar sudut pandang $= 40^\circ$.
- Titik di dalam lingkaran memiliki sudut pandang $> 40^\circ$.
- Titik di luar lingkaran memiliki sudut pandang $< 40^\circ$.
Langkah 3: Simpulkan syarat keamanan kapal:
Agar kapal tetap berada di luar daerah bahaya, sudut pandang harus memenuhi $\angle PKQ < 40^\circ$.
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11-b02-a-hard-bt01-006
*variasi (angka) | C5 | 3 langkah | jenis: panjang tali busur diameter*

Ruas garis $AB$ adalah diameter pada sebuah lingkaran. Jari-jari lingkaran tersebut adalah $32{,}5\text{ cm}$ dan panjang tali busur $AC = 39\text{ cm}$. Tentukan panjang tali busur $BC$.

- A. $26\text{ cm}$  
  <sub>Salah: Siswa langsung menggunakan panjang jari-jari $32{,}5\text{ cm}$ sebagai sisi miring segitiga alih-alih panjang diameter $65\text{ cm}$, lalu membulatkan atau salah menghitung $\sqrt{32{,}5^2 - 39^2}$.</sub>
- **B. $52\text{ cm}$** ✅  
  <sub>Benar: Diameter lingkaran adalah $AB = 2 \times 32{,}5 = 65\text{ cm}$. Berdasarkan Teorema Thales, karena $AB$ adalah diameter, maka sudut keliling $\angle ACB = 90^\circ$. Dengan teorema Pythagoras pada segitiga siku-siku $ABC$, $BC = \sqrt{AB^2 - AC^2} = \sqrt{65^2 - 39^2} = \sqrt{4225 - 1521} = \sqrt{2704} = 52\text{ cm}$.</sub>
- C. $48\text{ cm}$  
  <sub>Salah: Siswa salah menggunakan tripel Pythagoras $7-24-25$ yang diskalakan dua ($14-48-50$) karena keliru mengingat nilai diameter.</sub>
- D. $75{,}8\text{ cm}$  
  <sub>Salah: Siswa menjumlahkan kuadrat kedua sisi ($AB^2 + AC^2$) seolah-olah $BC$ adalah sisi miring hipotenusa.</sub>

**Pembahasan:** Langkah 1: Menghitung diameter lingkaran.
$AB = 2 \times r = 2 \times 32{,}5\text{ cm} = 65\text{ cm}$.

Langkah 2: Menentukan jenis segitiga $ABC$.
Berdasarkan Teorema Thales, setiap sudut keliling yang menghadap diameter lingkaran merupakan sudut siku-siku, sehingga $\angle ACB = 90^\circ$.

Langkah 3: Menghitung panjang $BC$ menggunakan teorema Pythagoras pada $\triangle ABC$.
$$BC = \sqrt{AB^2 - AC^2}$$
$$BC = \sqrt{65^2 - 39^2} = \sqrt{4225 - 1521} = \sqrt{2704} = 52\text{ cm}$$.

Jadi, panjang tali busur $BC$ adalah $52\text{ cm}$.
**Acuan:** pretest — kelas11-b02-p0074-latihan-21-4c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11-b02-a-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: sudut perpotongan tali busur diameter*

Ruas garis $AB$ merupakan diameter sebuah lingkaran. Titik $C$ dan $D$ terletak pada lingkaran di sisi yang sama terhadap $AB$ sedemikian sehingga tali busur $AC$ dan $BD$ berpotongan di titik $P$ di dalam lingkaran. Jika besar $\angle CAB = 32^\circ$ dan besar $\angle DBA = 46^\circ$, berapakah besar sudut lancip yang dibentuk oleh perpotongan kedua tali busur tersebut di titik $P$?

- A. $102^\circ$  
  <sub>Salah: Siswa menentukan sudut tumpul $\angle APB$ dan lupa bahwa pertanyaan meminta besar sudut lancip.</sub>
- B. $58^\circ$  
  <sub>Salah: Siswa hanya mencari penyiku dari $\angle CAB$, yaitu $90^\circ - 32^\circ = 58^\circ$ tanpa memperhitungkan tali busur $BD$.</sub>
- C. $76^\circ$  
  <sub>Salah: Siswa salah menjumlahkan $32^\circ + 46^\circ = 78^\circ$ lalu mengurangkannya dari $90^\circ$ sehingga menghasilkan $12^\circ$ atau salah hitung aritmetika $180 - 104$.</sub>
- **D. $78^\circ$** ✅  
  <sub>Benar: Pada segitiga $PAB$, titik $P$ adalah titik potong $AC$ dan $BD$. Maka sudut-sudut alasnya adalah $\angle PAB = \angle CAB = 32^\circ$ dan $\angle PBA = \angle DBA = 46^\circ$. Jumlah sudut dalam $\triangle PAB$ adalah $180^\circ$, sehingga $\angle APB = 180^\circ - 32^\circ - 46^\circ = 102^\circ$. Sudut lancip pelurusnya yang dibentuk oleh perpotongan kedua tali busur adalah $180^\circ - 102^\circ = 78^\circ$.</sub>

**Pembahasan:** Langkah 1: Mengidentifikasi posisi titik dan sudut pada segitiga yang terbentuk.
Tali busur $AC$ dan $BD$ berpotongan di titik $P$ di dalam lingkaran. Terbentuk segitiga $PAB$ dengan titik-titik sudut $P$, $A$, dan $B$.

Langkah 2: Menentukan sudut-sudut dalam $\triangle PAB$.
Diketahui bahwa $\angle PAB = \angle CAB = 32^\circ$ dan $\angle PBA = \angle DBA = 46^\circ$.

Langkah 3: Menghitung sudut $\angle APB$.
Jumlah sudut-sudut dalam suatu segitiga adalah $180^\circ$, maka:
$$\angle APB = 180^\circ - (\angle PAB + \angle PBA) = 180^\circ - (32^\circ + 46^\circ) = 180^\circ - 78^\circ = 102^\circ$$

Langkah 4: Menentukan sudut lancip hasil perpotongan kedua garis.
Perpotongan dua garis membentuk dua pasang sudut yang saling bertolak belakang dan berpelurus. Karena $\angle APB = 102^\circ$ tumpul, maka sudut lancip yang dibentuk adalah pelurusnya:
$$180^\circ - 102^\circ = 78^\circ$$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11-b02-a-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: sudut keliling busur gabungan*

Titik $A$, $B$, $C$, dan $D$ terletak pada keliling lingkaran berpusat di $O$ sedemikian sehingga ruas garis $AC$ merupakan diameter lingkaran. Titik $B$ dan $D$ terletak pada sisi yang berseberangan terhadap diameter $AC$. Jika besar sudut pusat $\angle AOB = 70^\circ$ dan sudut pusat $\angle COD = 80^\circ$, berapakah besar sudut keliling $\angle BED$ dengan $E$ adalah sembarang titik pada busur mayor $BD$?

- **A. $85^\circ$** ✅  
  <sub>Benar: Karena $AC$ garis lurus (diameter), maka sudut pusat $\angle BOC = 180^\circ - \angle AOB = 180^\circ - 70^\circ = 110^\circ$. Sudut pusat mayor yang melalui $C$ adalah $\angle BOD = \angle BOC + \angle COD = 110^\circ + 80^\circ = 190^\circ$. Maka sudut pusat minor $\angle BOD = 360^\circ - 190^\circ = 170^\circ$. Karena titik $E$ berada pada busur mayor $BD$, maka sudut keliling $\angle BED$ menghadap ke busur minor $BD$, sehingga $\angle BED = \frac{1}{2} \times 170^\circ = 85^\circ$.</sub>
- B. $170^\circ$  
  <sub>Salah: Siswa menghitung sudut pusat minor $170^\circ$ dengan benar tetapi lupa membaginya dengan dua untuk memperoleh sudut keliling.</sub>
- C. $75^\circ$  
  <sub>Salah: Siswa salah menjumlahkan $\angle AOB + \angle COD = 150^\circ$ lalu langsung membaginya dengan dua ($150^\circ / 2 = 75^\circ$).</sub>
- D. $95^\circ$  
  <sub>Salah: Siswa menghitung setengah dari sudut pusat mayor $190^\circ$, yaitu $95^\circ$, tanpa menyadari bahwa sudut keliling pada busur mayor menghadap busur minor.</sub>

**Pembahasan:** Langkah 1: Menentukan besar sudut pusat $\angle BOC$.
Ruas garis $AC$ merupakan diameter lingkaran, sehingga titik $A$, $O$, dan $C$ segaris ($180^\circ$).
$$\angle BOC = 180^\circ - \angle AOB = 180^\circ - 70^\circ = 110^\circ$$

Langkah 2: Menentukan sudut pusat yang memuat titik $C$.
Karena titik $B$ dan $D$ berada pada sisi berlawanan dari $AC$, besar sudut pusat $\angle BOD$ yang melalui $C$ adalah:
$$\angle BOD_{\text{mayor}} = \angle BOC + \angle COD = 110^\circ + 80^\circ = 190^\circ$$

Langkah 3: Menentukan besar sudut pusat minor yang menghadap busur minor $BD$.
$$\angle BOD_{\text{minor}} = 360^\circ - 190^\circ = 170^\circ$$

Langkah 4: Menghitung sudut keliling $\angle BED$.
Titik $E$ terletak pada busur mayor $BD$, sehingga sudut keliling $\angle BED$ menghadap ke busur minor $BD$. Berdasarkan sifat sudut lingkaran:
$$\angle BED = \frac{1}{2} \times \angle BOD_{\text{minor}} = \frac{1}{2} \times 170^\circ = 85^\circ$$.

Jadi, besar sudut keliling $\angle BED$ adalah $85^\circ$.
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11-b02-a-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: perbandingan keliling dan luas segitiga thales*

Ruas garis $AB$ merupakan diameter sebuah lingkaran. Titik $C$ terletak pada lingkaran tersebut sehingga terbentuk segitiga $ABC$. Diketahui luas segitiga $ABC$ adalah $120\text{ cm}^2$ dan selisih panjang kedua sisi tegaknya adalah $BC - AC = 14\text{ cm}$. Berapakah panjang jari-jari lingkaran tersebut?

- A. $26\text{ cm}$  
  <sub>Salah: Siswa menghitung panjang diameter $AB = 26\text{ cm}$ tetapi lupa membaginya dengan dua untuk memperoleh jari-jari.</sub>
- **B. $13\text{ cm}$** ✅  
  <sub>Benar: Berdasarkan Teorema Thales, karena $AB$ adalah diameter, segitiga $ABC$ siku-siku di $C$. Luas segitiga $L = \frac{1}{2} \times AC \times BC = 120 \implies AC \times BC = 240$. Dengan $BC - AC = 14$, maka $(BC + AC)^2 = (BC - AC)^2 + 4(AC \times BC) = 14^2 + 4(240) = 196 + 960 = 1156$, sehingga $BC + AC = 34\text{ cm}$. Diperoleh $BC = 24\text{ cm}$ dan $AC = 10\text{ cm}$. Maka diameter $AB = \sqrt{AC^2 + BC^2} = \sqrt{10^2 + 24^2} = 26\text{ cm}$. Jari-jari lingkaran adalah $r = \frac{AB}{2} = 13\text{ cm}$.</sub>
- C. $12\text{ cm}$  
  <sub>Salah: Siswa keliru menganggap panjang sisi tegak $BC = 24\text{ cm}$ sebagai diameter sehingga jari-jarinya $12\text{ cm}$.</sub>
- D. $17\text{ cm}$  
  <sub>Salah: Siswa mengambil nilai setengah dari $(AC + BC) = 34 / 2 = 17\text{ cm}$ bukan jari-jari lingkaran.</sub>

**Pembahasan:** Langkah 1: Menentukan sifat segitiga $ABC$.
Berdasarkan Teorema Thales, karena $AB$ adalah diameter lingkaran, maka sudut keliling $\angle ACB = 90^\circ$, sehingga segitiga $ABC$ siku-siku di $C$ dengan sisi tegak $AC$ dan $BC$.

Langkah 2: Menyusun persamaan dari luas dan selisih sisi tegak.
Luas $\triangle ABC = \frac{1}{2} \times AC \times BC = 120\text{ cm}^2 \implies AC \times BC = 240$.
Diketahui $BC - AC = 14$.

Langkah 3: Mencari panjang sisi $AC$ dan $BC$.
$$(BC + AC)^2 = (BC - AC)^2 + 4(AC \times BC)$$
$$(BC + AC)^2 = 14^2 + 4(240) = 196 + 960 = 1156$$
$$BC + AC = \sqrt{1156} = 34$$
Dari $BC - AC = 14$ dan $BC + AC = 34$, diperoleh:
$$2BC = 48 \implies BC = 24\text{ cm}$$
$$AC = 34 - 24 = 10\text{ cm}$$

Langkah 4: Menghitung diameter $AB$ dan jari-jari lingkaran.
$$AB = \sqrt{AC^2 + BC^2} = \sqrt{10^2 + 24^2} = \sqrt{100 + 576} = \sqrt{676} = 26\text{ cm}$$
Panjang jari-jari lingkaran $r$ adalah:
$$r = \frac{AB}{2} = \frac{26}{2} = 13\text{ cm}$$.

Jadi, panjang jari-jari lingkaran tersebut adalah $13\text{ cm}$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11-b02-a-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: evaluasi sudut busur mayor minor*

Titik $A$ dan $B$ terletak pada lingkaran yang berpusat di $O$. Titik $C$ terletak pada busur mayor $AB$, sedangkan titik $D$ terletak pada busur minor $AB$. Sudut keliling $\angle ACB$ menghadap busur minor $AB$, sedangkan sudut keliling $\angle ADB$ menghadap busur mayor $AB$. Jika diketahui selisih besar sudut $\angle ADB - \angle ACB = 50^\circ$, berapakah besar sudut pusat minor $\angle AOB$?

- **A. $130^\circ$** ✅  
  <sub>Benar: Misalkan sudut pusat minor $\angle AOB = \alpha$. Karena $\angle ACB$ menghadap busur minor $AB$, maka $\angle ACB = \frac{1}{2}\alpha$. Sudut pusat refleks yang menghadap busur mayor $AB$ adalah $360^\circ - \alpha$, sehingga sudut keliling $\angle ADB = \frac{1}{2}(360^\circ - \alpha) = 180^\circ - \frac{1}{2}\alpha$. Selisihnya adalah $\angle ADB - \angle ACB = (180^\circ - \frac{1}{2}\alpha) - \frac{1}{2}\alpha = 180^\circ - \alpha$. Diketahui selisihnya $50^\circ$, maka $180^\circ - \alpha = 50^\circ \implies \alpha = 130^\circ$.</sub>
- B. $65^\circ$  
  <sub>Salah: Siswa menghitung nilai sudut keliling $\angle ACB = \frac{130^\circ}{2} = 65^\circ$ alih-alih sudut pusat minor $\angle AOB$.</sub>
- C. $100^\circ$  
  <sub>Salah: Siswa mengira selisih sudut keliling langsung bernilai setengah dari sudut pusat minor, sehingga $\alpha = 2 \times 50^\circ = 100^\circ$.</sub>
- D. $115^\circ$  
  <sub>Salah: Siswa menghitung nilai sudut keliling $\angle ADB = 180^\circ - 65^\circ = 115^\circ$ alih-alih sudut pusat minor $\angle AOB$.</sub>

**Pembahasan:** Langkah 1: Memisalkan besar sudut pusat minor $\angle AOB$.
Misalkan besar sudut pusat minor $\angle AOB = \alpha$.

Langkah 2: Menentukan besar sudut keliling $\angle ACB$.
Karena sudut keliling $\angle ACB$ menghadap busur minor $AB$ yang sama dengan sudut pusat minor $\angle AOB$:
$$\angle ACB = \frac{1}{2}\alpha$$

Langkah 3: Menentukan besar sudut pusat refleks dan sudut keliling $\angle ADB$.
Sudut pusat refleks $\angle AOB$ yang menghadap busur mayor $AB$ adalah $360^\circ - \alpha$.
Karena sudut keliling $\angle ADB$ menghadap busur mayor $AB$, maka:
$$\angle ADB = \frac{1}{2}(360^\circ - \alpha) = 180^\circ - \frac{1}{2}\alpha$$

Langkah 4: Menyusun persamaan dari selisih sudut yang diketahui.
$$\angle ADB - \angle ACB = 50^\circ$$
$$\left(180^\circ - \frac{1}{2}\alpha\right) - \frac{1}{2}\alpha = 50^\circ$$
$$180^\circ - \alpha = 50^\circ$$

Langkah 5: Menyelesaikan nilai $\alpha$.
$$\alpha = 180^\circ - 50^\circ = 130^\circ$$

Jadi, besar sudut pusat minor $\angle AOB$ adalah $130^\circ$.
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11-b02-a-hard-bt01-011
*variasi (konteks) | C5 | 4 langkah | jenis: relasi sudut refleks dan keliling*

Titik $B$, $C$, dan $E$ terletak pada keliling sebuah lingkaran yang berpusat di titik $O$, dengan titik $E$ terletak pada busur mayor $BC$. Sudut keliling $\angle BEC$ menghadap busur minor $BC$ dan dinyatakan dengan $(\alpha - 10)^\circ$. Sudut refleks $\angle BOC$ menghadap busur mayor $BC$ dan dinyatakan dengan $(3\alpha + 60)^\circ$. Tentukan besar sudut $\angle BEC$.

- A. $64^\circ$  
  <sub>Salah: Hanya mencari nilai variabel $\alpha$ tanpa mensubstitusikannya kembali ke $(\alpha - 10)^\circ$.</sub>
- B. $108^\circ$  
  <sub>Salah: Menghitung besar sudut pusat minor $\angle BOC$, bukan sudut keliling $\angle BEC$.</sub>
- **C. $54^\circ$** ✅  
  <sub>Benar: Sudut pusat minor $\angle BOC = 2 \times \angle BEC = 2(\alpha - 10)^\circ = (2\alpha - 20)^\circ$. Jumlah sudut pusat minor dan refleks adalah $360^\circ$, sehingga $(3\alpha + 60)^\circ + (2\alpha - 20)^\circ = 360^\circ \implies 5\alpha + 40^\circ = 360^\circ \implies 5\alpha = 320^\circ \implies \alpha = 64^\circ$. Besar $\angle BEC = 64^\circ - 10^\circ = 54^\circ$.</sub>
- D. $44^\circ$  
  <sub>Salah: Mengabaikan faktor 2 pada hubungan sudut pusat dan sudut keliling sehingga menuliskan persamaan $(3\alpha + 60) + (\alpha - 10) = 360$.</sub>

**Pembahasan:** 1. Sudut pusat minor $\angle BOC$ besarnya dua kali sudut keliling $\angle BEC$ yang menghadap busur yang sama:
   $$\angle BOC_{\text{minor}} = 2(\alpha - 10)^\circ = (2\alpha - 20)^\circ$$
2. Sudut satu putaran penuh adalah $360^\circ$, sehingga:
   $$\angle BOC_{\text{minor}} + \angle BOC_{\text{refleks}} = 360^\circ$$
   $$(2\alpha - 20)^\circ + (3\alpha + 60)^\circ = 360^\circ$$
   $$5\alpha + 40^\circ = 360^\circ$$
   $$5\alpha = 320^\circ \implies \alpha = 64^\circ$$
3. Menghitung besar $\angle BEC$:
   $$\angle BEC = 64^\circ - 10^\circ = 54^\circ$$
**Acuan:** pretest — kelas11-b02-p0074-latihan-21-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11-b02-a-hard-bt01-012
*variasi (angka) | C5 | 4 langkah | jenis: selisih sudut keliling berseberangan*

Lingkaran $A$ memiliki jari-jari sebesar $8\text{ satuan}$. Titik $B$ dan $C$ terletak pada lingkaran sedemikian sehingga panjang tali busur $BC = 8\sqrt{2}\text{ satuan}$. Titik $D$ terletak pada busur mayor $BC$, sedangkan titik $E$ terletak pada busur minor $BC$. Tentukan nilai dari $\angle BEC - \angle BDC$.

- A. $135^\circ$  
  <sub>Salah: Hanya menghitung nilai sudut keliling $\angle BEC$ tanpa mengurangkannya dengan $\angle BDC$.</sub>
- B. $45^\circ$  
  <sub>Salah: Hanya menghitung nilai salah satu sudut keliling yaitu $\angle BDC$.</sub>
- **C. $90^\circ$** ✅  
  <sub>Benar: Karena $AB = AC = 8$ dan $AB^2 + AC^2 = 64 + 64 = 128 = (8\sqrt{2})^2 = BC^2$, maka $\angle BAC = 90^\circ$. Sudut keliling $\angle BDC = \frac{1}{2} \times 90^\circ = 45^\circ$. Sudut keliling $\angle BEC$ menghadap busur mayor bernilai $180^\circ - 45^\circ = 135^\circ$. Selisihnya adalah $135^\circ - 45^\circ = 90^\circ$.</sub>
- D. $60^\circ$  
  <sub>Salah: Keliru mengira segitiga $ABC$ merupakan segitiga sama sisi sehingga sudut pusat dianggap $60^\circ$.</sub>

**Pembahasan:** 1. Periksa jenis $\triangle ABC$ dengan jari-jari $AB = AC = 8$ dan $BC = 8\sqrt{2}$:
   $$AB^2 + AC^2 = 8^2 + 8^2 = 64 + 64 = 128$$
   $$BC^2 = (8\sqrt{2})^2 = 128$$
   Karena $AB^2 + AC^2 = BC^2$, maka $\triangle ABC$ siku-siku di titik pusat $A$, sehingga sudut pusat busur minor $BC$ adalah $\angle BAC = 90^\circ$.
2. Titik $D$ berada pada busur mayor $BC$, sehingga menghadap busur minor $BC$:
   $$\angle BDC = \frac{1}{2} \times \angle BAC = \frac{1}{2} \times 90^\circ = 45^\circ$$
3. Titik $E$ berada pada busur minor $BC$, sehingga menghadap busur mayor $BC$ yang memiliki sudut pusat $360^\circ - 90^\circ = 270^\circ$:
   $$\angle BEC = \frac{1}{2} \times 270^\circ = 135^\circ$$
4. Hitung selisihnya:
   $$\angle BEC - \angle BDC = 135^\circ - 45^\circ = 90^\circ$$
**Acuan:** siswa — siswa hal.74 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11-b02-a-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: garis tinggi segitiga thales*

Ruas garis $AB$ merupakan diameter sebuah lingkaran dengan jari-jari $25\text{ cm}$. Titik $C$ terletak pada keliling lingkaran tersebut. Garis tinggi segitiga $ABC$ yang ditarik dari titik $C$ tegak lurus terhadap $AB$ dan memotong diameter $AB$ di titik $D$. Jika panjang $AD = 18\text{ cm}$, tentukan luas segitiga $ABC$.

- A. $576\text{ cm}^2$  
  <sub>Salah: Menganggap luas segitiga sama dengan nilai kuadrat garis tinggi ($CD^2 = 576$).</sub>
- B. $1200\text{ cm}^2$  
  <sub>Salah: Lupa mengalikan dengan faktor $\frac{1}{2}$ pada rumus luas segitiga ($50 \times 24$).</sub>
- **C. $600\text{ cm}^2$** ✅  
  <sub>Benar: Diameter $AB = 2 \times 25 = 50\text{ cm}$. Panjang $BD = 50 - 18 = 32\text{ cm}$. Karena $\angle ACB = 90^\circ$ (Teorema Thales), berlaku tinggi $CD = \sqrt{AD \times BD} = \sqrt{18 \times 32} = \sqrt{576} = 24\text{ cm}$. Maka luas segitiga $ABC = \frac{1}{2} \times AB \times CD = \frac{1}{2} \times 50 \times 24 = 600\text{ cm}^2$.</sub>
- D. $450\text{ cm}^2$  
  <sub>Salah: Menggunakan jari-jari sebagai alas bukan diameter dalam perhitungan luas segitiga ($\frac{1}{2} \times 25 \times 36$ atau kesalahan alas $r$).</sub>

**Pembahasan:** 1. Panjang diameter lingkaran:
   $$AB = 2r = 2 \times 25\text{ cm} = 50\text{ cm}$$
2. Menentukan panjang segmen $BD$ pada diameter:
   $$BD = AB - AD = 50\text{ cm} - 18\text{ cm} = 32\text{ cm}$$
3. Berdasarkan Teorema Thales, karena $AB$ diameter, maka $\angle ACB = 90^\circ$. Pada segitiga siku-siku $ABC$ dengan garis tinggi $CD \perp AB$, berlaku relasi proyeksi:
   $$CD^2 = AD \times BD = 18 \times 32 = 576$$
   $$CD = \sqrt{576} = 24\text{ cm}$$
4. Menghitung luas $\triangle ABC$:
   $$\text{Luas} = \frac{1}{2} \times AB \times CD = \frac{1}{2} \times 50 \times 24 = 600\text{ cm}^2$$
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11-b02-a-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: perpotongan tali busur dalam*

Titik $A$, $B$, $C$, dan $D$ terletak berurutan pada sebuah lingkaran yang berpusat di titik $O$. Ruas garis $AC$ dan ruas garis $BD$ merupakan tali busur yang berpotongan di titik $M$ di dalam lingkaran. Diketahui besar sudut pusat $\angle AOB = 76^\circ$ dan sudut pusat $\angle COD = 48^\circ$. Tentukan besar sudut $\angle AMD$.

- A. $94^\circ$  
  <sub>Salah: Salah menghitung sudut keliling hanya pada salah satu sudut pusat ($180^\circ - 48^\circ - 38^\circ$).</sub>
- **B. $118^\circ$** ✅  
  <sub>Benar: Sudut keliling $\angle ADB = \frac{1}{2} \angle AOB = 38^\circ$. Sudut keliling $\angle CAD = \frac{1}{2} \angle COD = 24^\circ$. Pada $\triangle AMD$, $\angle MAD = 24^\circ$ dan $\angle ADM = 38^\circ$. Maka $\angle AMD = 180^\circ - (24^\circ + 38^\circ) = 180^\circ - 62^\circ = 118^\circ$.</sub>
- C. $62^\circ$  
  <sub>Salah: Menghitung sudut pelurus dari $\angle AMD$ (yaitu $\angle AMB$ atau sudut luar).</sub>
- D. $124^\circ$  
  <sub>Salah: Langsung menjumlahkan kedua sudut pusat $76^\circ + 48^\circ$ tanpa membaginya menjadi sudut keliling.</sub>

**Pembahasan:** 1. Sudut keliling $\angle ADB$ menghadap busur $AB$ yang sama dengan sudut pusat $\angle AOB$:
   $$\angle ADB = \frac{1}{2} \times \angle AOB = \frac{1}{2} \times 76^\circ = 38^\circ$$
2. Sudut keliling $\angle CAD$ menghadap busur $CD$ yang sama dengan sudut pusat $\angle COD$:
   $$\angle CAD = \frac{1}{2} \times \angle COD = \frac{1}{2} \times 48^\circ = 24^\circ$$
3. Perhatikan $\triangle AMD$. Sudut-sudut dalamnya adalah $\angle MAD = \angle CAD = 24^\circ$ dan $\angle ADM = \angle ADB = 38^\circ$.
4. Jumlah sudut dalam segitiga adalah $180^\circ$, sehingga:
   $$\angle AMD = 180^\circ - (\angle MAD + \angle ADM) = 180^\circ - (24^\circ + 38^\circ) = 180^\circ - 62^\circ = 118^\circ$$
**Acuan:** siswa — siswa hal.70

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas11-b02-a-hard-bt01-015
*variasi (konteks) | C5 | 3 langkah | jenis: evaluasi kesalahan sifat sudut lingkaran*

Seorang siswa membuat pernyataan berikut:
"Titik $O$ adalah pusat lingkaran, sedangkan titik $A, B,$ dan $C$ terletak pada keliling lingkaran. Jika sudut pusat minor $\angle AOB = 100^\circ$, maka besar sudut keliling $\angle ACB$ pasti selalu bernilai $50^\circ$, di mana pun posisi titik $C$ diletakkan pada keliling lingkaran tersebut."

Manakah evaluasi yang paling tepat mengenai kesalahan pernyataan siswa tersebut?

- **A. Pernyataan salah, karena jika titik $C$ berada pada busur minor $AB$, besar $\angle ACB$ adalah $130^\circ$.** ✅  
  <sub>Benar: Sudut keliling bernilai setengah sudut pusat hanya jika menghadap busur yang sama. Jika $C$ di busur minor $AB$, $\angle ACB$ menghadap busur mayor $AB$ yang bersudut pusat $360^\circ - 100^\circ = 260^\circ$, sehingga $\angle ACB = \frac{1}{2} \times 260^\circ = 130^\circ$.</sub>
- B. Pernyataan salah, karena jika titik $C$ berada pada busur mayor $AB$, besar $\angle ACB$ adalah $80^\circ$.  
  <sub>Salah: Salah mengira sudut keliling adalah pelurus dari sudut pusat minor.</sub>
- C. Pernyataan salah, karena sudut keliling $\angle ACB$ seharusnya dua kali lipat sudut pusat, yaitu $200^\circ$.  
  <sub>Salah: Tertukar antara definisi sudut pusat dan sudut keliling.</sub>
- D. Pernyataan salah, karena besar $\angle ACB$ selalu bergantung pada panjang jari-jari lingkaran.  
  <sub>Salah: Mengira besar sudut keliling berubah jika ukuran jari-jari lingkaran membesar atau mengecil.</sub>

**Pembahasan:** Hubungan bahwa besar sudut keliling sama dengan setengah sudut pusat hanya berlaku jika kedua sudut tersebut menghadap ke busur yang sama.
1. Jika titik $C$ terletak pada busur mayor $AB$, sudut keliling $\angle ACB$ menghadap busur minor $AB$, sehingga besarnya $\frac{1}{2} \times 100^\circ = 50^\circ$.
2. Jika titik $C$ terletak pada busur minor $AB$, sudut keliling $\angle ACB$ menghadap busur mayor $AB$. Besar sudut pusat refleks busur mayor $AB$ adalah $360^\circ - 100^\circ = 260^\circ$.
3. Maka besar $\angle ACB = \frac{1}{2} \times 260^\circ = 130^\circ$.
Jadi, pernyataan siswa keliru karena nilai $50^\circ$ tidak berlaku jika $C$ terletak pada busur minor $AB$.
**Acuan:** siswa — siswa hal.75 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas11-b02-a-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: garis tinggi perbandingan tali busur diameter*

Ruas garis $AB$ merupakan diameter sebuah lingkaran berjari-jari $10\text{ cm}$. Titik $C$ terletak pada keliling lingkaran sedemikian sehingga perbandingan panjang tali busur $AC : BC = 3 : 4$. Dari titik $C$, ditarik garis tinggi tegak lurus terhadap diameter $AB$ yang memotong ruas garis $AB$ di titik $D$. Panjang ruas garis $CD$ adalah ....

- A. $11{,}2\text{ cm}$  
  <sub>Salah: Salah menerapkan perbandingan Pythagoras sehingga mendapatkan panjang sisi siku-siku yang keliru.</sub>
- B. $7{,}2\text{ cm}$  
  <sub>Salah: Menghitung proyeksi ruas garis $AD$ bukan tinggi garis $CD$.</sub>
- **C. $9{,}6\text{ cm}$** ✅  
  <sub>Benar: Diameter $AB = 20\text{ cm}$. Berdasarkan Teorema Thales, $\triangle ABC$ siku-siku di $C$. Dengan perbandingan $3 : 4$, $AC = 12\text{ cm}$ dan $BC = 16\text{ cm}$. Luas segitiga $L = \frac{1}{2} \times 12 \times 16 = 96\text{ cm}^2$. Maka $CD = \frac{2L}{AB} = \frac{192}{20} = 9{,}6\text{ cm}$.</sub>
- D. $4{,}8\text{ cm}$  
  <sub>Salah: Lupa mengalikan 2 saat menghitung tinggi dari rumus luas, yaitu langsung membagi luas dengan diameter.</sub>

**Pembahasan:** Langkah-langkah penyelesaian:
1. Ruas garis $AB$ adalah diameter lingkaran, sehingga panjang $AB = 2 \times 10\text{ cm} = 20\text{ cm}$. Berdasarkan Teorema Thales, sudut keliling yang menghadap diameter adalah siku-siku, sehingga $\angle ACB = 90^\circ$.
2. Misalkan $AC = 3x$ dan $BC = 4x$. Dengan Teorema Pythagoras pada $\triangle ABC$:
   $AC^2 + BC^2 = AB^2$
   $(3x)^2 + (4x)^2 = 20^2$
   $25x^2 = 400 \implies x^2 = 16 \implies x = 4$.
   Diperoleh panjang $AC = 3(4) = 12\text{ cm}$ dan $BC = 4(4) = 16\text{ cm}$.
3. Luas $\triangle ABC$ dapat dihitung melalui sisi siku-siku:
   $\text{Luas} = \frac{1}{2} \times AC \times BC = \frac{1}{2} \times 12 \times 16 = 96\text{ cm}^2$.
4. Luas $\triangle ABC$ juga dapat dihitung menggunakan alas $AB$ dan garis tinggi $CD$:
   $\text{Luas} = \frac{1}{2} \times AB \times CD$
   $96 = \frac{1}{2} \times 20 \times CD$
   $96 = 10 \times CD \implies CD = 9{,}6\text{ cm}$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas11-b02-a-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: analisis sudut pusat tali busur diameter*

Titik $K, L, M,$ dan $N$ terletak berurutan pada keliling lingkaran yang berpusat di $O$, dengan ruas garis $KM$ merupakan diameter lingkaran. Tali busur $LN$ memotong diameter $KM$ di titik $P$ di dalam lingkaran sedemikian sehingga $\angle KPL = 70^\circ$. Jika sudut pusat $\angle KOL = 80^\circ$, berapakah besar sudut pusat $\angle MON$ yang menghadap busur minor $MN$?

- A. $40^\circ$  
  <sub>Salah: Mengira $\angle MON$ sama dengan setengah dari sudut pusat $\angle KOL$.</sub>
- **B. $60^\circ$** ✅  
  <sub>Benar: $\angle LOM = 180^\circ - 80^\circ = 100^\circ$, maka $\angle LKM = 50^\circ$. Pada $\triangle KPL$, $\angle PLK = 180^\circ - (70^\circ + 50^\circ) = 60^\circ$. Karena $KM$ diameter, $\angle KLM = 90^\circ$, sehingga $\angle NLM = 90^\circ - 60^\circ = 30^\circ$. Sudut pusat $\angle MON = 2 \times \angle NLM = 2 \times 30^\circ = 60^\circ$.</sub>
- C. $30^\circ$  
  <sub>Salah: Hanya menghitung sudut keliling $\angle NLM$ dan lupa mengalikan dua untuk mendapatkan sudut pusat.</sub>
- D. $80^\circ$  
  <sub>Salah: Menganggap busur $MN$ sama panjang dengan busur $KL$ tanpa menghitung posisi titik potong.</sub>

**Pembahasan:** Langkah-langkah penyelesaian:
1. Ruas garis $KM$ adalah garis lurus berdiameter yang melalui pusat $O$, sehingga $\angle KOL + \angle LOM = 180^\circ$. Dengan $\angle KOL = 80^\circ$, diperoleh $\angle LOM = 180^\circ - 80^\circ = 100^\circ$.
2. Sudut keliling $\angle LKM$ menghadap busur $LM$ yang bersudut pusat $\angle LOM = 100^\circ$, sehingga $\angle LKM = \frac{1}{2} \times 100^\circ = 50^\circ$.
3. Pada $\triangle KPL$, jumlah sudut segitiga adalah $180^\circ$:
   $\angle PLK = 180^\circ - (\angle KPL + \angle PKL) = 180^\circ - (70^\circ + 50^\circ) = 60^\circ$.
   Maka $\angle NLK = 60^\circ$.
4. Karena ruas garis $KM$ adalah diameter lingkaran, berdasarkan Teorema Thales, besar sudut keliling $\angle KLM = 90^\circ$.
   Diperoleh $\angle NLM = \angle KLM - \angle NLK = 90^\circ - 60^\circ = 30^\circ$.
5. Sudut keliling $\angle NLM$ menghadap busur minor $MN$. Sudut pusat $\angle MON$ juga menghadap busur minor $MN$, sehingga:
   $\angle MON = 2 \times \angle NLM = 2 \times 30^\circ = 60^\circ$.
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas11-b02-a-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: perancangan tali busur dan sudut pemantauan*

Sebuah kolam rekreasi berbentuk lingkaran memiliki garis tengah diameter $AB = 24\text{ m}$. Sepanjang busur minor $BC$ dipasang lintasan perosotan air. Sebuah lampu sorot dipasang di titik $A$ pada tepi kolam dan dapat menyinari seluruh busur $BC$ dengan sudut sorot $\angle BAC = 30^\circ$. Pengelola kolam ingin memindahkan lampu sorot ke titik pusat kolam $O$ agar tepat menyinari busur $BC$, serta memasang tali pembatas lurus langsung dari titik $B$ ke $C$. Berapakah besar sudut sorot lampu di titik pusat $O$ dan panjang tali pembatas lurus $BC$ berturut-turut?

- A. $60^\circ\text{ dan }24\text{ m}$  
  <sub>Salah: Menggunakan panjang diameter kolam sebagai panjang tali pembatas $BC$.</sub>
- **B. $60^\circ\text{ dan }12\text{ m}$** ✅  
  <sub>Benar: Sudut pusat $\angle BOC = 2 \times \angle BAC = 60^\circ$. Karena jari-jari $OB = OC = 12\text{ m}$ dan $\angle BOC = 60^\circ$, $\triangle OBC$ adalah segitiga sama sisi, sehingga $BC = 12\text{ m}$.</sub>
- C. $30^\circ\text{ dan }12\text{ m}$  
  <sub>Salah: Mengira sudut di pusat lingkaran sama dengan sudut di tepi lingkaran.</sub>
- D. $60^\circ\text{ dan }12\sqrt{2}\text{ m}$  
  <sub>Salah: Menganggap segitiga $BOC$ adalah segitiga siku-siku sama kaki.</sub>

**Pembahasan:** Langkah-langkah penyelesaian:
1. Titik $A$ terletak pada keliling lingkaran, sehingga $\angle BAC = 30^\circ$ adalah sudut keliling yang menghadap busur minor $BC$.
2. Lampu yang dipindahkan ke titik pusat $O$ membentuk sudut pusat $\angle BOC$ yang menghadap busur minor yang sama ($BC$).
   Berdasarkan sifat lingkaran, besar sudut pusat adalah dua kali besar sudut keliling:
   $\angle BOC = 2 \times \angle BAC = 2 \times 30^\circ = 60^\circ$.
3. Jari-jari kolam lingkaran adalah $r = \frac{1}{2} \times AB = \frac{1}{2} \times 24\text{ m} = 12\text{ m}$.
   Panjang ruas garis $OB = OC = r = 12\text{ m}$.
4. Perhatikan segitiga $OBC$:
   Karena $OB = OC$, maka segitiga $OBC$ adalah segitiga sama kaki dengan sudut puncak $\angle BOC = 60^\circ$.
   Besar sudut alasnya adalah $\frac{180^\circ - 60^\circ}{2} = 60^\circ$.
   Karena ketiga sudutnya sama besar ($60^\circ$), maka $\triangle OBC$ merupakan segitiga sama sisi.
5. Oleh karena itu, panjang tali pembatas lurus $BC = OB = OC = 12\text{ m}$.
Jadi, sudut sorot di titik pusat adalah $60^\circ$ dan panjang tali pembatas adalah $12\text{ m}$.
**Acuan:** siswa — siswa hal.68

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas11-b02-a-hard-bt01-019
*orisinal | C5 | 5 langkah | jenis: sudut pusat tali busur tegak lurus*

Titik $P, Q, R,$ dan $S$ terletak berurutan pada keliling lingkaran yang berpusat di titik $O$. Ruas garis $PR$ dan ruas garis $QS$ merupakan dua tali busur yang saling berpotongan tegak lurus di titik $T$ di dalam lingkaran. Jika besar sudut pusat $\angle POS = 116^\circ$, berapakah besar sudut pusat $\angle QOR$?

- A. $58^\circ$  
  <sub>Salah: Hanya menghitung setengah dari besar sudut pusat $\angle POS$.</sub>
- B. $74^\circ$  
  <sub>Salah: Salah menghitung selisih sudut pelurus ($180^\circ - 116^\circ$ dihitung keliru sebagai $74^\circ$).</sub>
- C. $116^\circ$  
  <sub>Salah: Mengira dua sudut pusat yang berseberangan pada tali busur tegak lurus pasti sama besar.</sub>
- **D. $64^\circ$** ✅  
  <sub>Benar: Pada segitiga siku-siku $PTQ$, $\angle TPQ + \angle TQP = 90^\circ$. Sudut keliling $\angle TPQ$ menghadap busur $QR$ dan $\angle TQP$ menghadap busur $PS$. Maka $\angle QOR + \angle POS = 2(\angle TPQ + \angle TQP) = 2 \times 90^\circ = 180^\circ$. Diperoleh $\angle QOR = 180^\circ - 116^\circ = 64^\circ$.</sub>

**Pembahasan:** Langkah-langkah penyelesaian:
1. Ruas garis $PR$ dan ruas garis $QS$ berpotongan tegak lurus di titik $T$, sehingga $\angle PTQ = 90^\circ$.
2. Perhatikan segitiga siku-siku $PTQ$:
   Jumlah sudut dalam segitiga adalah $180^\circ$, sehingga:
   $\angle TPQ + \angle TQP = 180^\circ - \angle PTQ = 180^\circ - 90^\circ = 90^\circ$.
3. Identifikasi sudut keliling:
   - Sudut $\angle TPQ$ sama dengan sudut keliling $\angle RPQ$, yang menghadap busur $QR$. Maka sudut pusat $\angle QOR = 2 \times \angle TPQ$.
   - Sudut $\angle TQP$ sama dengan sudut keliling $\angle SQP$, yang menghadap busur $PS$. Maka sudut pusat $\angle POS = 2 \times \angle TQP$.
4. Jumlahkan kedua sudut pusat tersebut:
   $\angle QOR + \angle POS = 2 \times \angle TPQ + 2 \times \angle TQP = 2(\angle TPQ + \angle TQP)$.
   $\angle QOR + \angle POS = 2 \times 90^\circ = 180^\circ$.
5. Substitusikan nilai $\angle POS = 116^\circ$:
   $\angle QOR + 116^\circ = 180^\circ$
   $\angle QOR = 180^\circ - 116^\circ = 64^\circ$.
**Acuan:** siswa — siswa hal.70

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas11-b02-a-hard-bt01-020
*orisinal | C5 | 4 langkah | jenis: panjang tali busur tegak lurus diameter*

Ruas garis $AB$ merupakan diameter sebuah lingkaran. Tali busur $CD$ memotong tegak lurus diameter $AB$ di titik $H$. Jika panjang ruas garis $AH = 4\text{ cm}$ dan $HB = 16\text{ cm}$, maka panjang tali busur $CD$ adalah ....

- A. $8\sqrt{5}\text{ cm}$  
  <sub>Salah: Menggunakan rumus tinggi segitiga siku-siku pada proyeksi yang salah atau menjumlahkan kuadrat komponen.</sub>
- B. $12\text{ cm}$  
  <sub>Salah: Salah mengurangkan langsung jari-jari atau salah menerapkan teorema Pythagoras.</sub>
- C. $8\text{ cm}$  
  <sub>Salah: Hanya menghitung setengah panjang tali busur ($CH$) dan lupa mengalikannya dengan 2.</sub>
- **D. $16\text{ cm}$** ✅  
  <sub>Benar: Panjang diameter $AB = 4 + 16 = 20\text{ cm}$, sehingga jari-jari lingkaran $r = 10\text{ cm}$. Jarak titik $H$ ke pusat lingkaran $O$ adalah $OH = 10 - 4 = 6\text{ cm}$. Pada segitiga siku-siku $OCH$, $CH = \sqrt{r^2 - OH^2} = \sqrt{10^2 - 6^2} = 8\text{ cm}$. Karena diameter yang tegak lurus tali busur membagi tali busur menjadi dua bagian sama panjang, maka $CD = 2 \times CH = 2 \times 8 = 16\text{ cm}$.</sub>

**Pembahasan:** Langkah 1: Hitung panjang diameter dan jari-jari lingkaran.
$AB = AH + HB = 4\text{ cm} + 16\text{ cm} = 20\text{ cm}$
Jari-jari lingkaran $r = \frac{20}{2} = 10\text{ cm}$.

Langkah 2: Tentukan jarak titik potong $H$ ke pusat lingkaran $O$.
$OH = r - AH = 10\text{ cm} - 4\text{ cm} = 6\text{ cm}$.

Langkah 3: Tentukan panjang ruas garis $CH$.
Hubungkan pusat lingkaran $O$ ke titik $C$ sehingga terbentuk segitiga siku-siku $OHC$ dengan sisi miring $OC = r = 10\text{ cm}$.
$CH = \sqrt{OC^2 - OH^2} = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8\text{ cm}$.

Langkah 4: Tentukan panjang tali busur $CD$.
Karena diameter $AB$ tegak lurus dengan tali busur $CD$, ruas garis $AB$ membagi dua sama panjang tali busur $CD$, sehingga:
$CD = 2 \times CH = 2 \times 8\text{ cm} = 16\text{ cm}$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
