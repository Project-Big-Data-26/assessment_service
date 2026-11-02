# Lembar koreksi — kelas12_tl SMA12L-B4 subbab C: Variabel Acak Kontinu

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b04-c-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: notasi ruang sampel*

Sebuah proses pemanasan logam menghasilkan suhu pelat yang berkisar dari $41,5^\circ\text{C}$ hingga $48,0^\circ\text{C}$. Misalkan $X$ adalah variabel acak yang menyatakan suhu pelat tersebut dalam derajat Celsius. Bentuk ruang sampel $S$ dari variabel acak $X$ adalah ....

- A. $S = \{x \mid 41,5 \le x \le 48,0,\ x \in \mathbb{Z}\}$  
  <sub>Salah: Siswa keliru menganggap anggota ruang sampel variabel acak berupa bilangan bulat (integers).</sub>
- B. $S = \{x \mid 41,5 < x < 48,0,\ x \in \mathbb{N}\}$  
  <sub>Salah: Siswa salah menggunakan himpunan bilangan asli dan tanda pertidaksamaan tanpa memuat batas.</sub>
- **C. $S = \{x \mid 41,5 \le x \le 48,0,\ x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Suhu pelat merupakan variabel acak kontinu pada interval tertutup $41,5$ sampai $48,0$, sehingga ruang sampelnya berupa semua bilangan real pada rentang tersebut.</sub>
- D. $S = \{41,5;\ 42,0;\ 43,0;\ 44,0;\ 45,0;\ 46,0;\ 47,0;\ 48,0\}$  
  <sub>Salah: Siswa menganggap ruang sampel kontinu dapat dicacah secara diskret dengan interval tertentu.</sub>

**Pembahasan:** Variabel acak suhu merupakan variabel acak kontinu yang nilainya berupa bilangan real dalam rentang tertentu. Nilai suhu berada di antara $41,5^\circ\text{C}$ hingga $48,0^\circ\text{C}$ secara inklusif, sehingga ruang sampelnya adalah $S = \{x \mid 41,5 \le x \le 48,0,\ x \in \mathbb{R}\}$.
**Acuan:** pretest — kelas12_tl-b04-p0257-latihan-soal-variabel-acak-kontinu-b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b04-c-easy-bt01-002
*variasi (konteks) | C1 | 1 langkah | jenis: sifat ketercacahan nilai*

Berat sekarung beras hasil pengemasan pabrik berkisar antara $49,5\text{ kg}$ hingga $50,5\text{ kg}$. Jika $W$ menyatakan berat karung beras tersebut dalam kg, apakah semua kemungkinan nilai $W$ dapat dihitung satu per satu? Berikan alasan yang tepat.

- **A. Tidak dapat, karena $W$ memuat semua bilangan real dalam interval tersebut sehingga nilainya tak terhitung (uncountable).** ✅  
  <sub>Benar: Nilai variabel kontinu mencakup seluruh bilangan real pada suatu interval sehingga memiliki sifat tak terhitung (uncountable).</sub>
- B. Dapat, karena selisih nilai batas atas dan batas bawah hanya sebesar $1\text{ kg}$.  
  <sub>Salah: Siswa menyamakan panjang interval yang berhingga dengan banyaknya nilai variabel.</sub>
- C. Dapat, karena setiap penimbangan selalu dibulatkan ke satu angka desimal terdekat.  
  <sub>Salah: Siswa keliru membedakan keterbatasan alat ukur dengan sifat teoretis variabel acak kontinu.</sub>
- D. Tidak dapat, karena batas atas interval berat tidak terdefinisi dengan pasti.  
  <sub>Salah: Siswa salah memahami penyebab ketaktercacahan, mengira batas interval tidak diketahui.</sub>

**Pembahasan:** Variabel acak $W$ merupakan variabel acak kontinu dengan nilai pada interval $[49,5;\ 50,5]$. Di antara dua bilangan real sembarang selalu terdapat bilangan real lain yang tak berhingga banyaknya, sehingga nilai $W$ tidak dapat dihitung satu per satu (tak terhitung / *uncountable*).
**Acuan:** pretest — kelas12_tl-b04-p0257-latihan-soal-variabel-acak-kontinu-c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b04-c-easy-bt01-003
*variasi (konteks) | C2 | 1 langkah | jenis: klasifikasi variabel acak*

Sebuah dispenser otomatis mengisi botol oli dengan volume nominal $800\text{ mL}$. Akibat variasi tekanan pompa, volume oli yang terisi berada pada rentang $792\text{ mL}$ hingga $808\text{ mL}$. Misalkan $V$ menyatakan volume oli yang terisi. Pernyataan yang paling tepat mengenai variabel acak $V$ adalah ....

- A. $V$ merupakan variabel acak kontinu karena nilainya dapat dicacah secara berurutan dari $792$ sampai $808$  
  <sub>Salah: Siswa benar mengidentifikasi kontinu tetapi keliru pada definisi pencacahan nilai.</sub>
- **B. $V$ merupakan variabel acak kontinu karena nilainya diperoleh melalui pengukuran dan membentuk interval bilangan real** ✅  
  <sub>Benar: Volume diperoleh lewat pengukuran kontinu sehingga membentuk interval bilangan real pada garis bilangan.</sub>
- C. $V$ merupakan variabel acak diskret karena volume botol dibatasi angka $800\text{ mL}$  
  <sub>Salah: Siswa mengira keberadaan nilai nominal menjadikan variabel bernilai tunggal/diskret.</sub>
- D. $V$ merupakan variabel acak diskret karena nilai minimum dan maksimumnya berupa bilangan bulat  
  <sub>Salah: Siswa terkecoh oleh batas interval yang tertulis dalam bentuk bilangan bulat.</sub>

**Pembahasan:** Variabel $V$ menyatakan volume cairan yang diperoleh melalui proses pengukuran. Nilai $V$ berada dalam rentang $[792, 808]$ pada bilangan real dan tidak dapat dicacah satu per satu, sehingga $V$ merupakan variabel acak kontinu.
**Acuan:** siswa — siswa hal.255 Contoh Soal 4.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b04-c-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: identifikasi variabel acak*

Di antara variabel acak berikut, manakah yang merupakan contoh variabel acak kontinu?

- A. Jumlah gol yang tercipta selama satu babak pertandingan  
  <sub>Salah: Siswa memilih data cacah bulat non-negatif (variabel diskret).</sub>
- B. Banyaknya lemparan bebas yang berhasil masuk dalam permainan bola basket  
  <sub>Salah: Siswa memilih hasil percobaan binomial diskret.</sub>
- **C. Waktu yang dibutuhkan seorang atlet untuk menyelesaikan lari $400\text{ meter}$** ✅  
  <sub>Benar: Waktu tempuh diperoleh melalui proses pengukuran dan nilainya berada dalam rentang bilangan real tak terputus.</sub>
- D. Banyaknya penonton yang menghadiri pertandingan sepak bola di stadion  
  <sub>Salah: Siswa memilih data hasil perhitungan/pencacahan (variabel acak diskret).</sub>

**Pembahasan:** Variabel acak kontinu nilainya diperoleh dari hasil pengukuran (seperti panjang, massa, suhu, atau waktu) dan berupa bilangan real dalam suatu interval. Waktu tempuh lari diperoleh melalui pengukuran, sedangkan banyak penonton, jumlah gol, dan lemparan bebas diperoleh melalui pencacahan (variabel acak diskret).
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b04-c-easy-bt01-005
*variasi (angka) | C2 | 1 langkah | jenis: representasi ruang sampel*

Dalam suatu perlombaan renang gaya dada lintasan $50\text{ meter}$, waktu tempuh setiap perenang dicatat dalam detik. Misalkan $T$ adalah variabel acak yang menyatakan waktu tempuh perenang dan nilainya berada pada rentang $28,4\text{ detik}$ hingga $32,6\text{ detik}$. Bentuk ruang sampel $S$ dari variabel acak waktu tempuh tersebut adalah ....

- **A. $S = \{t \mid 28,4 \le t \le 32,6,\ t \in \mathbb{R}\}$** ✅  
  <sub>Benar: Waktu tempuh adalah variabel acak kontinu yang memuat seluruh bilangan real dalam interval tertutup $[28,4; 32,6]$, sehingga himpunan ruang sampelnya ditulis $S = \{t \mid 28,4 \le t \le 32,6,\ t \in \mathbb{R}\}$.</sub>
- B. $S = \{t \mid t \ge 28,4,\ t \in \mathbb{R}\}$  
  <sub>Salah: Mengabaikan batas atas rentang waktu tempuh.</sub>
- C. $S = \{28,4; 28,5; 28,6; \dots; 32,6\}$  
  <sub>Salah: Menganggap waktu hanya bernilai diskret dengan kenaikan satu desimal.</sub>
- D. $S = \{t \mid 28,4 < t < 32,6,\ t \in \mathbb{Z}\}$  
  <sub>Salah: Salah menggunakan himpunan bilangan bulat dan pertidaksamaan terbuka.</sub>

**Pembahasan:** Waktu tempuh merupakan besaran kontinu. Karena nilainya berada pada rentang $28,4$ sampai $32,6$ detik, ruang sampel memuat semua bilangan real $t$ di mana $28,4 \le t \le 32,6$. Jadi, $S = \{t \mid 28,4 \le t \le 32,6,\ t \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.256 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b04-c-easy-bt01-006
*variasi (konteks) | C2 | 1 langkah | jenis: analisis jenis variabel*

Sebuah mesin pengemas semen otomatis mengisi kantong dengan berat nominal $40\text{ kg}$. Akibat fluktuasi mekanis, berat riil semen per kantong bervariasi dari $39,2\text{ kg}$ sampai $40,8\text{ kg}$. Jika $Y$ menyatakan berat semen dalam suatu kantong, alasan yang paling tepat mengapa $Y$ merupakan variabel acak kontinu adalah ....

- **A. nilai $Y$ mencakup semua bilangan real dalam rentang $[39,2; 40,8]$ dan tidak dapat dihitung satu per satu** ✅  
  <sub>Benar: Berat adalah hasil pengukuran kontinu, sehingga ruang sampelnya berupa interval bilangan real tak terhitung (uncountable).</sub>
- B. banyaknya kemungkinan berat semen yang dihasilkan mesin tepat sebanyak $17$ kemungkinan  
  <sub>Salah: Memperlakukan nilai desimal berketelitian satu angka di belakang koma sebagai himpunan berhingga diskret.</sub>
- C. nilai $Y$ dapat ditentukan secara pasti tanpa melalui proses penimbangan  
  <sub>Salah: Salah memahami konsep variabel acak pengukuran.</sub>
- D. nilai $Y$ selalu berupa bilangan bulat yang berada di antara $39$ dan $41$  
  <sub>Salah: Keliru mengira variabel kontinu hanya bernilai bulat.</sub>

**Pembahasan:** Variabel acak kontinu didefinisikan pada ruang sampel yang mencakup seluruh bilangan real pada suatu interval tak terputus. Karena berat semen berada pada rentang $39,2\text{ kg}$ hingga $40,8\text{ kg}$, nilainya tak terhitung banyaknya (uncountable), sehingga $Y$ adalah variabel acak kontinu.
**Acuan:** siswa — siswa hal.255 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b04-c-easy-bt01-007
*variasi (konteks) | C2 | 1 langkah | jenis: ketercacahan nilai ruang sampel*

Tekanan udara di dalam ban sebuah truk ekspedisi berada pada rentang $110,0\text{ psi}$ hingga $125,0\text{ psi}$. Misalkan $P$ menyatakan tekanan udara ban tersebut dalam satuan psi. Apakah seluruh kemungkinan nilai $P$ dalam ruang sampel tersebut dapat dihitung satu per satu (tercacah)?

- A. Dapat, karena selisih nilai tertinggi dan terendah bernilai pasti yaitu $15\text{ psi}$.  
  <sub>Salah: Mengacaukan panjang interval terhingga dengan banyaknya anggota himpunan nilai.</sub>
- B. Dapat, asalkan alat ukur manometer yang digunakan hanya menampilkan bilangan bulat.  
  <sub>Salah: Menyamakan keterbatasan resolusi alat ukur dengan sifat teoretis variabel acak itu sendiri.</sub>
- **C. Tidak dapat, karena nilai $P$ memuat semua bilangan real dalam interval tersebut sehingga sifatnya tak terhitung (uncountable).** ✅  
  <sub>Benar: Di antara dua nilai real pada variabel kontinu selalu terdapat tak berhingga bilangan real lainnya sehingga tidak dapat didaftar atau dicacah satu per satu.</sub>
- D. Tidak dapat, karena batas atas tekanan ban tidak dapat ditentukan secara teoretis.  
  <sub>Salah: Alasan keliru, batas atas jelas tertulis $125,0\text{ psi}$.</sub>

**Pembahasan:** Tekanan udara merupakan variabel acak kontinu. Ruang sampelnya memuat semua bilangan real pada selang $[110,0; 125,0]$. Antara dua nilai desimal selalu ada nilai desimal lain yang tak berhingga banyaknya, sehingga elemen ruang sampelnya tidak dapat dicacah satu per satu (uncountable).
**Acuan:** pretest — kelas12_tl-b04-p0257-latihan-soal-variabel-acak-kontinu-c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b04-c-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: karakteristik perolehan data*

Berdasarkan karakteristiknya pada materi statistika, nilai-nilai dari suatu variabel acak kontinu pada umumnya diperoleh melalui proses ....

- A. pengelompokan berdasarkan kategori nama objek  
  <sub>Salah: Merupakan ciri variabel nominal.</sub>
- **B. pengukuran menggunakan alat ukur** ✅  
  <sub>Benar: Buku siswa menyatakan bahwa nilai variabel acak kontinu diperoleh dari hasil pengukuran (seperti panjang, massa, waktu, atau suhu).</sub>
- C. pengurutan data kualitatif berdasar peringkat  
  <sub>Salah: Merupakan ciri skala ordinal pada data kategorik.</sub>
- D. penghitungan atau pencacahan satu per satu  
  <sub>Salah: Merupakan karakteristik perolehan nilai variabel acak diskret.</sub>

**Pembahasan:** Sesuai ciri-ciri variabel acak kontinu di Buku Siswa, nilainya diperoleh dari hasil pengukuran (misalnya pengukuran tinggi badan, waktu, volume, atau suhu), sedangkan variabel acak diskret diperoleh dari hasil pembilangan/pencacahan.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b04-c-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: representasi geometris variabel acak*

Pada garis bilangan, nilai-nilai dari suatu variabel acak kontinu direpresentasikan dalam bentuk ....

- A. sebuah titik tunggal yang tidak memiliki panjang  
  <sub>Salah: Representasi sebuah konstanta, bukan variabel acak kontinu.</sub>
- B. titik-titik terpisah yang tidak saling terhubung  
  <sub>Salah: Merupakan representasi geometris dari variabel acak diskret.</sub>
- C. kumpulan titik yang hanya berada pada koordinat bilangan cacah  
  <sub>Salah: Keliru menyamakan representasi kontinu dengan himpunan diskret non-negatif.</sub>
- **D. deretan titik yang terhubung membentuk ruas garis** ✅  
  <sub>Benar: Variabel acak kontinu mencakup interval bilangan real tak terputus sehingga membentuk segmen/ruas garis tersambung.</sub>

**Pembahasan:** Berdasarkan Buku Siswa Matematika Tingkat Lanjut Kelas XII halaman 255, nilai-nilai variabel acak kontinu berupa bilangan real yang membentuk rentang tak terputus, sehingga representasinya pada garis bilangan berupa deretan titik yang terhubung dan membentuk garis (interval).
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b04-c-easy-bt01-010
*variasi (angka) | C2 | 1 langkah | jenis: penulisan ruang sampel kontinu*

Kadar kelembapan biji kopi yang baru dikeringkan berkisar dari $10,5\%$ hingga $14,0\%$. Misalkan $K$ adalah variabel acak kontinu yang menyatakan kadar kelembapan biji kopi tersebut (dalam persen). Taksiran bentuk notasi ruang sampel $S$ dari variabel acak tersebut adalah ....

- A. $S = \{k \mid k \ge 10,5,\ k \in \mathbb{R}\}$  
  <sub>Salah: Lupa menyertakan batas atas interval kadar kelembapan.</sub>
- **B. $S = \{k \mid 10,5 \le k \le 14,0,\ k \in \mathbb{R}\}$** ✅  
  <sub>Benar: Ruang sampel memuat seluruh nilai bilangan real tak terputus dari batas bawah 10,5 hingga batas atas 14,0.</sub>
- C. $S = \{11, 12, 13, 14\}$  
  <sub>Salah: Memperlakukan data kontinu sebagai bilangan bulat diskret.</sub>
- D. $S = \{k \mid 10,5 < k < 14,0,\ k \in \mathbb{Z}\}$  
  <sub>Salah: Menggunakan pertidaksamaan terbuka murni dan domain bilangan bulat.</sub>

**Pembahasan:** Kadar kelembapan merupakan variabel acak kontinu yang nilainya berada pada interval $10,5$ hingga $14,0$ pada himpunan bilangan real $\mathbb{R}$. Dengan demikian, ruang sampelnya ditulis sebagai himpunan berlanjut:
$$S = \{k \mid 10,5 \le k \le 14,0,\ k \in \mathbb{R}\}$$
**Acuan:** pretest — kelas12_tl-b04-p0257-latihan-soal-variabel-acak-kontinu-b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b04-c-easy-bt01-011
*variasi (konteks) | C2 | 1 langkah | jenis: formulasi interval kontinu*

Tegangan listrik pada suatu instalasi laboratorium berfluktuasi secara kontinu pada rentang $218,5\text{ V}$ hingga $224,2\text{ V}$. Jika $V$ menyatakan variabel acak tegangan listrik tersebut, maka penulisan ruang sampel $S$ yang tepat adalah ....

- **A. $S = \{v \mid 218,5 \le v \le 224,2,\ v \in \mathbb{R}\}$** ✅  
  <sub>Benar: Fluktuasi tegangan membentuk interval kontinu dari 218,5 sampai 224,2 pada himpunan bilangan real.</sub>
- B. $S = \{218,5;\ 224,2\}$  
  <sub>Salah: Hanya mendaftarkan kedua ujung rentang sebagai himpunan beranggotakan dua nilai.</sub>
- C. $S = \{v \mid v \le 224,2,\ v \in \mathbb{R}\}$  
  <sub>Salah: Mengabaikan batas bawah fluktuasi tegangan listrik.</sub>
- D. $S = \{v \mid 218,5 \le v \le 224,2,\ v \in \mathbb{N}\}$  
  <sub>Salah: Menggunakan domain bilangan asli yang bersifat diskret.</sub>

**Pembahasan:** Tegangan listrik adalah variabel acak kontinu yang mencakup semua nilai di antara nilai minimum dan maksimumnya. Rentang nilai dari $218,5$ hingga $224,2$ pada semesta bilangan real $\mathbb{R}$ dinyatakan sebagai:
$$S = \{v \mid 218,5 \le v \le 224,2,\ v \in \mathbb{R}\}$$
**Acuan:** siswa — siswa hal.256 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b04-c-easy-bt01-012
*variasi (konteks) | C1 | 1 langkah | jenis: penentuan variabel tak terhitung*

Perhatikan variabel-variabel acak berikut:
(1) Jumlah penonton di sebuah bioskop
(2) Panjang bentang kabel transmisi listrik
(3) Banyaknya kendaraan yang melintasi gerbang tol
(4) Banyak gol yang dicetak dalam pertandingan sepak bola

Variabel acak yang memiliki nilai tak terhitung banyaknya (uncountable) dalam suatu rentang adalah ....

- A. (1)  
  <sub>Salah: Jumlah penonton diperoleh lewat pencacahan sehingga berhingga dan terhitung (diskret).</sub>
- B. (3)  
  <sub>Salah: Banyaknya kendaraan diperoleh dari hasil menghitung satu per satu (diskret).</sub>
- **C. (2)** ✅  
  <sub>Benar: Panjang kabel merupakan besaran hasil pengukuran yang bernilai bilangan real kontinu sehingga tak terhitung banyaknya.</sub>
- D. (4)  
  <sub>Salah: Banyak gol merupakan bilangan cacah berhingga yang terhitung (diskret).</sub>

**Pembahasan:** Variabel acak kontinu memiliki nilai tak terhitung banyaknya (uncountable) dalam suatu interval karena diperoleh dari pengukuran. Di antara pilihan yang ada, panjang bentang kabel (2) diperoleh melalui pengukuran panjang dan bernilai kontinu pada rentang bilangan real, sedangkan (1), (3), dan (4) diperoleh melalui proses pencacahan atau perhitungan satu per satu (variabel acak diskret).
**Acuan:** siswa — siswa hal.254 Ayo Berdiskusi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b04-c-easy-bt01-013
*orisinal | C2 | 1 langkah | jenis: analisis kepadatan nilai kontinu*

Tinggi kecambah kacang hijau pada hari ketiga pengamatan berada pada interval $4,0\text{ cm}$ hingga $5,0\text{ cm}$. Berdasarkan sifat variabel acak kontinu, di antara nilai tinggi $4,2\text{ cm}$ dan $4,3\text{ cm}$ pasti terdapat kemungkinan muncul nilai tinggi lain karena ....

- A. alat ukur yang digunakan selalu menghasilkan galat perhitungan acak  
  <sub>Salah: Menghubungkan sifat teoretis variabel acak dengan galat mekanis alat.</sub>
- B. nilai variabel acak kontinu hanya terdiri dari bilangan bulat yang berurutan  
  <sub>Salah: Salah memahami variabel kontinu sebagai bilangan bulat.</sub>
- **C. nilai variabel acak kontinu berupa bilangan real yang membentuk rentang tak terputus** ✅  
  <sub>Benar: Sifat densitas/kepadatan bilangan real pada variabel acak kontinu memungkinkan nilai pecahan tak terhingga di antara dua nilai.</sub>
- D. ruang sampel variabel acak selalu berupa himpunan terhitung  
  <sub>Salah: Menyebut himpunan kontinu sebagai himpunan terhitung, padahal tak terhitung.</sub>

**Pembahasan:** Berdasarkan ciri-ciri variabel acak kontinu, nilainya berupa bilangan real yang membentuk rentang tak terputus. Sifat ini menjamin bahwa di antara dua nilai riil berapapun (misalnya antara $4,2\text{ cm}$ dan $4,3\text{ cm}$), selalu terdapat tak berhingga nilai lain (misalnya $4,25\text{ cm}$ atau $4,218\text{ cm}$) yang mungkin tercapai.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b04-c-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: karakteristik desimal kontinu*

Alasan utama besaran hasil pengukuran seperti volume cairan atau tinggi badan dikelompokkan sebagai variabel acak kontinu adalah karena ....

- A. banyaknya kemungkinan hasil selalu berhingga dan mudah didaftar seluruhnya  
  <sub>Salah: Menyatakan ciri himpunan diskret berhingga.</sub>
- B. nilainya selalu berupa bilangan bulat positif yang dapat dihitung berurutan  
  <sub>Salah: Mendeskripsikan karakteristik variabel acak diskret.</sub>
- C. ruang sampelnya tidak dapat digambarkan pada garis bilangan sama sekali  
  <sub>Salah: Bertentangan dengan fakta bahwa variabel kontinu dapat digambar sebagai garis bilangan.</sub>
- **D. nilainya dapat berupa bilangan desimal dalam rentang tertentu dan tidak dapat dihitung satu per satu** ✅  
  <sub>Benar: Merupakan definisi eksplisit pada buku teks mengenai alasan suatu besaran pengukuran tergolong kontinu.</sub>

**Pembahasan:** Hasil pengukuran seperti volume cairan dan tinggi badan dikategorikan sebagai variabel acak kontinu karena nilainya dapat berada di antara dua bilangan real manapun (berupa desimal/pecahan dalam rentang tertentu) serta titik-titik sampelnya tak terhitung (uncountable).
**Acuan:** siswa — siswa hal.254

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b04-c-easy-bt01-015
*variasi (konteks) | C2 | 1 langkah | jenis: klasifikasi variabel tak terhitung*

Perhatikan variabel-variabel acak berikut:
(1) Banyaknya telur ayam dalam sebuah rak penyimpanan
(2) Lama waktu pengisian daya baterai telepon pintar
(3) Banyaknya kendaraan yang parkir di sebuah gedung
(4) Jumlah lembaran uang kertas di dalam dompet

Berdasarkan keempat variabel acak tersebut, variabel yang memiliki kemungkinan nilai tak terhitung banyaknya dalam suatu rentang kontinu adalah ....

- A. (3)  
  <sub>Salah: Mengira banyaknya kendaraan bermotor adalah variabel kontinu, padahal merupakan variabel acak diskret bernilai bilangan cacah.</sub>
- B. (1)  
  <sub>Salah: Mengira banyaknya butir telur adalah variabel kontinu, padahal merupakan variabel acak diskret dari hasil pencacahan.</sub>
- C. (4)  
  <sub>Salah: Mengira jumlah lembaran uang adalah variabel kontinu, padahal merupakan variabel acak diskret.</sub>
- **D. (2)** ✅  
  <sub>Benar: Lama waktu pengisian daya merupakan variabel acak kontinu yang diperoleh dari pengukuran sehingga nilainya tak terhitung (uncountable) dalam suatu interval bilangan real.</sub>

**Pembahasan:** Variabel acak kontinu memiliki nilai yang tak terhitung banyaknya dalam suatu interval dan diperoleh dari hasil pengukuran. Dari keempat variabel di atas, lama waktu pengisian daya (2) merupakan variabel kontinu, sedangkan (1), (3), dan (4) diperoleh melalui pencacahan (counting) sehingga bernilai diskret.
**Acuan:** siswa — siswa hal.254 Ayo Berdiskusi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b04-c-easy-bt01-016
*variasi (konteks) | C2 | 1 langkah | jenis: penyebab sifat uncountable*

Nilai-nilai pada variabel acak kontinu seperti waktu tempuh atau massa benda tidak dapat dihitung satu per satu (uncountable). Penyebab utama hal tersebut adalah karena nilainya ....

- A. selalu bernilai lebih besar daripada batas ukur alat ukur  
  <sub>Salah: Terkecoh oleh batas fisik alat ukur, bukan sifat matematis rentang bilangan real.</sub>
- **B. mencakup seluruh bilangan real pada suatu interval tanpa terputus** ✅  
  <sub>Benar: Variabel acak kontinu didefinisikan pada interval bilangan real yang padat dan tak terhitung banyaknya.</sub>
- C. hanya terdiri atas bilangan bulat tak berhingga  
  <sub>Salah: Keliru menganggap himpunan bilangan bulat tak berhingga sebagai himpunan tak terhitung (uncountable).</sub>
- D. hanya dapat dituliskan dalam bentuk pecahan biasa  
  <sub>Salah: Keliru mengira bilangan kontinu terbatas pada bilangan rasional berbentuk pecahan.</sub>

**Pembahasan:** Nilai-nilai variabel acak kontinu tidak dapat dihitung satu per satu (uncountable) karena mencakup seluruh bilangan real pada suatu rentang tanpa terputus, di mana antara dua nilai sembarang selalu terdapat bilangan real lainnya.
**Acuan:** siswa — siswa hal.254 Ayo Berdiskusi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b04-c-easy-bt01-017
*variasi (angka) | C1 | 1 langkah | jenis: identifikasi nilai kontinu*

Sebuah variabel acak kontinu $X$ menyatakan suhu cairan pada suatu termometer dengan rentang $74,0^\circ\text{C} \le X \le 78,0^\circ\text{C}$. Nilai berikut yang mungkin merupakan salah satu nilai dari variabel acak $X$ tersebut adalah ....

- A. $73,85^\circ\text{C}$  
  <sub>Salah: Memilih nilai yang berada di bawah batas minimum interval ($73,85 < 74,0$).</sub>
- B. $78,25^\circ\text{C}$  
  <sub>Salah: Memilih nilai yang melampaui batas maksimum interval ($78,25 > 78,0$).</sub>
- C. $84,10^\circ\text{C}$  
  <sub>Salah: Salah membaca interval batas sehingga memilih nilai yang jauh di luar rentang.</sub>
- **D. $76,45^\circ\text{C}$** ✅  
  <sub>Benar: Nilai $76,45^\circ\text{C}$ berada di dalam interval rentang $[74,0^\circ\text{C},\ 78,0^\circ\text{C}]$.</sub>

**Pembahasan:** Variabel acak $X$ didefinisikan pada interval $74,0^\circ\text{C} \le X \le 78,0^\circ\text{C}$. Dari pilihan yang ada, hanya $76,45^\circ\text{C}$ yang terletak di dalam rentang tersebut.
**Acuan:** siswa — siswa hal.256 Ayo Mencoba 4.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b04-c-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: definisi ruang sampel kontinu*

Ruang sampel suatu percobaan acak yang terdiri atas titik-titik hasil yang tak berhingga banyaknya dan tidak dapat dihitung satu per satu disebut ....

- A. ruang sampel acak murni  
  <sub>Salah: Menggunakan istilah buatan yang tidak dikenal dalam teori peluang.</sub>
- **B. ruang sampel kontinu** ✅  
  <sub>Benar: Sesuai definisi pada buku teks matematika, ruang sampel yang memuat titik hasil tak berhingga dan tak terhitung disebut ruang sampel kontinu.</sub>
- C. ruang sampel diskret  
  <sub>Salah: Tertukar dengan ruang sampel diskret yang titik-titik hasilnya dapat dicacah satu per satu.</sub>
- D. ruang sampel berhingga  
  <sub>Salah: Salah memahami istilah, mengira titik hasil tak terhitung sebagai himpunan berhingga.</sub>

**Pembahasan:** Berdasarkan materi Buku Siswa halaman 255, jika ruang sampel suatu percobaan acak terdiri atas titik-titik hasil yang tak berhingga banyaknya dan tidak dapat dihitung satu per satu, ruang sampel tersebut dinamakan ruang sampel kontinu.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b04-c-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: sifat densitas nilai kontinu*

Salah satu ciri utama dari variabel acak kontinu adalah nilainya membentuk rentang tak terputus. Hal ini memiliki arti bahwa di antara dua nilai sembarang pada rentang tersebut selalu ....

- A. memiliki selisih tetap sebesar bilangan cacah  
  <sub>Salah: Menyamakan variabel kontinu dengan barisan aritmetika atau variabel diskret berjarak tetap.</sub>
- B. terdapat celah kosong yang tidak memiliki nilai peluang  
  <sub>Salah: Bertentangan dengan konsep rentang kontinu yang tak terputus.</sub>
- C. terdapat tepat satu bilangan bulat perantara  
  <sub>Salah: Keliru mengasumsikan nilai perantara harus berupa bilangan bulat tunggal.</sub>
- **D. mungkin terdapat nilai lain yang termasuk dalam variabel tersebut** ✅  
  <sub>Benar: Karakteristik bilangan real pada variabel kontinu menjamin adanya nilai perantara tak hingga banyaknya di antara dua nilai sembarang.</sub>

**Pembahasan:** Menurut ciri-ciri variabel acak kontinu di Buku Siswa halaman 255, nilainya berupa bilangan real yang membentuk rentang tak terputus. Konsekuensinya, antara dua nilai tertentu selalu terdapat kemungkinan terdapat nilai lain yang masih termasuk dalam variabel tersebut.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b04-c-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: definisi variabel acak kontinu*

Variabel acak yang didefinisikan pada ruang sampel kontinu disebut ....

- **A. variabel acak kontinu** ✅  
  <sub>Benar: Berdasarkan definisi pada Buku Siswa, variabel acak yang didefinisikan pada ruang sampel kontinu dinamakan variabel acak kontinu.</sub>
- B. variabel acak kualitatif  
  <sub>Salah: Mengira variabel acak digolongkan berdasarkan jenis data non-numerik.</sub>
- C. variabel acak diskret  
  <sub>Salah: Tertukar dengan variabel acak yang ruang sampelnya berhingga atau tak berhingga terbilang.</sub>
- D. variabel acak biner  
  <sub>Salah: Terkecoh dengan istilah variabel yang hanya memiliki dua kemungkinan nilai diskret.</sub>

**Pembahasan:** Berdasarkan Buku Siswa Matematika Tingkat Lanjut Kelas XII, suatu ruang sampel yang terdiri atas titik-titik hasil yang tak berhingga banyaknya dan tidak dapat dihitung satu per satu disebut ruang sampel kontinu. Selanjutnya, variabel acak yang didefinisikan pada ruang sampel kontinu disebut variabel acak kontinu.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b04-c-medium-bt01-001
*variasi (konteks) | C3 | 2 langkah | jenis: penentuan ruang sampel*

Sebuah eksperimen laboratorium menguji daya regang kawat baja tipis hingga putus. Gaya tarik yang terukur pada saat kawat putus berada dalam rentang $84,6\text{ N}$ sampai dengan $92,8\text{ N}$. Jika variabel acak $F$ menyatakan besar gaya tarik yang memutus kawat tersebut, bentuk notasi himpunan ruang sampel $S$ yang tepat adalah ....

- A. $S = \{F \mid F \le 84,6 \text{ atau } F \ge 92,8,\ F \in \mathbb{R}\}$  
  <sub>Salah: Salah mengartikan interval rentang menjadi bagian luar dari nilai batas.</sub>
- B. $S = \{F \mid 84,6 < F < 92,8,\ F \in \mathbb{Z}\}$  
  <sub>Salah: Menggunakan himpunan bilangan bulat dan pertidaksamaan murni sehingga mengabaikan nilai desimal dan batas rentang.</sub>
- **C. $S = \{F \mid 84,6 \le F \le 92,8,\ F \in \mathbb{R}\}$** ✅  
  <sub>Benar: Gaya tarik adalah besaran kontinu hasil pengukuran sehingga ruang sampelnya mencakup seluruh bilangan real pada interval $[84,6; 92,8]$.</sub>
- D. $S = \{84,6;\ 85,0;\ 86,0;\ \dots;\ 92,8\}$  
  <sub>Salah: Memperlakukan variabel acak kontinu sebagai variabel diskret dengan pencacahan satu per satu.</sub>

**Pembahasan:** Besaran gaya tarik diperoleh melalui pengukuran alat ukur mekanis dan memiliki nilai tak hingga banyaknya di antara batas ukur. Dengan demikian, $F$ merupakan variabel acak kontinu. Ruang sampel untuk nilai gaya antara $84,6\text{ N}$ dan $92,8\text{ N}$ dinyatakan sebagai interval tertutup bilangan real: $S = \{F \mid 84,6 \le F \le 92,8,\ F \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.256 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b04-c-medium-bt01-002
*variasi (angka) | C4 | 3 langkah | jenis: analisis sifat variabel*

Sebuah dispenser industri mengisikan sirup ke dalam wadah bertarget $350\text{ mL}$. Karena toleransi katup pompa, volume sirup yang terisi bervariasi secara acak dari $342,5\text{ mL}$ hingga $357,5\text{ mL}$. Misalkan $Y$ menyatakan volume sirup dalam sebuah wadah. Manakah simpulan yang paling tepat mengenai variabel acak $Y$ beserta alasannya?

- A. $Y$ merupakan variabel acak kontinu hanya jika selisih pengisian antarwadah selalu tepat bernilai kelipatan $0,5\text{ mL}$.  
  <sub>Salah: Membatasi nilai pada kisi diskret kelipatan tertentu yang justru merupakan ciri variabel diskret.</sub>
- **B. $Y$ merupakan variabel acak kontinu karena ruang nilainya memuat seluruh bilangan real pada interval $[342,5; 357,5]$ sehingga tak terhitung satu per satu.** ✅  
  <sub>Benar: Volume diperoleh lewat pengukuran kontinu sehingga nilai pada interval tersebut membentuk himpunan bagian bilangan real yang tak terhitung.</sub>
- C. $Y$ merupakan variabel acak diskret karena volume cairan dapat dibulatkan ke satu angka desimal terdekat.  
  <sub>Salah: Menyamakan pembulatan pembacaan alat dengan hakikat teoritis variabel acak kontinu.</sub>
- D. $Y$ merupakan variabel acak diskret karena rentang volumenya memiliki batas bawah $342,5\text{ mL}$ dan batas atas $357,5\text{ mL}$ yang bernilai terhingga.  
  <sub>Salah: Keliru menganggap interval berhingga (bounded) sebagai himpunan berhingga (finite).</sub>

**Pembahasan:** Variabel acak kontinu didefinisikan pada ruang sampel di mana titik-titik hasilnya tak berhingga dan tak terhitung (uncountable). Karena volume sirup $Y$ diperoleh melalui pengukuran dan dapat bernilai pecahan/desimal sembarang di antara $342,5\text{ mL}$ dan $357,5\text{ mL}$, ruang nilainya merupakan himpunan bagian dari bilangan real $\mathbb{R}$. Jadi, $Y$ adalah variabel acak kontinu.
**Acuan:** siswa — siswa hal.255 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b04-c-medium-bt01-003
*orisinal | C4 | 3 langkah | jenis: klasifikasi variabel acak*

Perhatikan empat variabel acak yang diamati pada suatu laboratorium riset pertanian berikut:
(1) $K$: Konsentrasi pupuk cair dalam larutan hidroponik (dalam $\text{ppm}$)
(2) $B$: Banyaknya daun yang menguning pada satu pohon tomat
(3) $T$: Waktu yang dibutuhkan benih jagung hingga berkecambah pertama kali (dalam jam)
(4) $N$: Jumlah bulir padi yang hampa pada satu malai

Berdasarkan stimulus tersebut, pasangan variabel acak yang keduanya tergolong sebagai variabel acak kontinu adalah ....

- A. (1) dan (2)  
  <sub>Salah: Keliru mengelompokkan jumlah daun yang merupakan data cacah/diskret.</sub>
- B. (3) dan (4)  
  <sub>Salah: Keliru menganggap jumlah bulir hampa sebagai besaran kontinu.</sub>
- C. (2) dan (4)  
  <sub>Salah: Memilih pasangan variabel acak diskret (keduanya hasil proses membilang).</sub>
- **D. (1) dan (3)** ✅  
  <sub>Benar: Konsentrasi zat cair dan durasi waktu diperoleh melalui pengukuran fisik yang nilainya berada pada interval kontinu bilangan real.</sub>

**Pembahasan:** Variabel acak kontinu nilainya diperoleh melalui pengukuran dan berada dalam interval bilangan real tak terputus. Pada daftar:
- (1) $K$ (konsentrasi) diukur dengan instrumen kimia, nilainya kontinu.
- (2) $B$ (banyak daun) diperoleh dari mencacah satu per satu, nilainya diskret.
- (3) $T$ (waktu perkecambahan) diukur dengan stopwatch/alat pencatat waktu, nilainya kontinu.
- (4) $N$ (jumlah bulir) diperoleh dari membilang, nilainya diskret.
Dengan demikian, variabel kontinu adalah (1) dan (3).
**Acuan:** siswa — siswa hal.254

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b04-c-medium-bt01-004
*orisinal | C4 | 3 langkah | jenis: analisis kerapatan interval*

Sebuah sensor termal mengukur suhu cairan pendingin mesin $T$ pada interval $60,00^\circ\text{C} \le T \le 60,50^\circ\text{C}$. Dua kali pencatatan berturut-turut menghasilkan nilai $t_1 = 60,12^\circ\text{C}$ dan $t_2 = 60,13^\circ\text{C}$. Berdasarkan sifat variabel acak kontinu, pernyataan yang paling tepat mengenai kemungkinan nilai suhu di antara $t_1$ dan $t_2$ adalah ....

- **A. Terdapat tak hingga banyak nilai suhu real yang mungkin muncul di antara $t_1$ dan $t_2$.** ✅  
  <sub>Benar: Variabel acak kontinu didefinisikan pada himpunan bilangan real yang memiliki sifat kerapatan, sehingga di antara dua bilangan real selalu ada tak terhingga bilangan real lainnya.</sub>
- B. Tepat ada satu nilai suhu yang mungkin muncul di antara keduanya, yaitu nilai tengahnya $60,125^\circ\text{C}$.  
  <sub>Salah: Hanya menghitung titik tengah aritmetika dan mengabaikan nilai real lainnya pada interval tersebut.</sub>
- C. Hanya ada sembilan nilai suhu tambahan jika dicatat hingga tiga angka di belakang koma.  
  <sub>Salah: Terpaku pada pembatasan representasi desimal 3 angka di belakang koma.</sub>
- D. Tidak ada nilai suhu lain yang mungkin karena selisihnya sudah mencapai batas ketelitian $0,01^\circ\text{C}$.  
  <sub>Salah: Menyamakan keterbatasan resolusi tampilan alat dengan sifat matematis kontinu dari variabel tersebut.</sub>

**Pembahasan:** Salah satu ciri utama variabel acak kontinu adalah nilainya berupa bilangan real yang membentuk rentang tak terputus. Mengacu pada materi Buku Siswa hal 255: 'antara dua nilai tertentu selalu terdapat kemungkinan terdapat nilai lain yang masih termasuk dalam variabel tersebut'. Karena himpunan bilangan real bersifat rapat (dense), di antara dua nilai real sembarang $t_1 < t_2$ terdapat tak hingga banyaknya bilangan real lainnya.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b04-c-medium-bt01-005
*variasi (konteks) | C4 | 2 langkah | jenis: justifikasi ketakterhitungan*

Tekanan uap gas dalam suatu tabung reaksi selama eksperimen berlangsung berada pada rentang $4,2\text{ bar}$ hingga $6,8\text{ bar}$. Misalkan $P$ adalah variabel acak yang menyatakan tekanan uap gas tersebut (dalam bar). Apakah seluruh kemungkinan nilai pada ruang sampel variabel acak $P$ dapat dicacah atau dihitung satu per satu? Berikan alasan matematis yang tepat.

- A. Tidak dapat, karena nilai batas atas $6,8\text{ bar}$ dan batas bawah $4,2\text{ bar}$ tidak terdefinisi secara pasti.  
  <sub>Salah: Keliru menganggap ketakterhitungan disebabkan oleh batas interval yang tidak pasti, padahal batasnya jelas berhingga.</sub>
- B. Dapat, karena pembacaan alat ukur tekanan uap memiliki angka desimal dengan ketelitian tertentu.  
  <sub>Salah: Menyamakan keterbatasan resolusi alat ukur fisik dengan sifat teoritis ruang sampel variabel acak kontinu.</sub>
- C. Dapat, karena selisih antara nilai tertinggi dan terendah bernilai tetap yaitu $2,6\text{ bar}$.  
  <sub>Salah: Mengira bahwa panjang interval yang berhingga membuat anggota di dalamnya berhingga dan dapat dicacah.</sub>
- **D. Tidak dapat, karena ruang sampel $P$ memuat semua bilangan real pada interval $[4,2;\ 6,8]$ yang sifatnya tak terhitung (*uncountable*).** ✅  
  <sub>Benar: Tekanan gas merupakan variabel acak kontinu yang nilainya berada pada interval kontinu bilangan real, sehingga himpunan nilainya berdensitas rapat dan tak terhitung (uncountable).</sub>

**Pembahasan:** Variabel acak $P$ merepresentasikan besaran fisik hasil pengukuran kontinu pada rentang $[4,2;\ 6,8]$. Karena mencakup seluruh bilangan real di antara $4,2$ dan $6,8$, anggota ruang sampelnya tidak berhingga dan bersifat *uncountable* (tak terhitung). Oleh karena itu, nilai-nilainya tidak dapat dicacah satu per satu.
**Acuan:** pretest — kelas12_tl-b04-p0257-latihan-soal-variabel-acak-kontinu-c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b04-c-medium-bt01-006
*variasi (konteks) | C3 | 2 langkah | jenis: penentuan karakteristik kontinu*

Sebuah mesin pemotong pelat memproduksi lembaran logam tipis dengan ketebalan nominal $2,0\text{ mm}$. Akibat getaran mekanik mesin, ketebalan riil lembaran logam yang dihasilkan bervariasi dari $1,8\text{ mm}$ hingga $2,4\text{ mm}$. Misalkan $T$ menyatakan ketebalan lembaran logam yang diproduksi. Apakah $T$ merupakan variabel acak kontinu dan apa alasannya?

- A. Tidak, karena rentang ketebalan dibatasi secara tegas antara $1,8\text{ mm}$ dan $2,4\text{ mm}$.  
  <sub>Salah: Mengira bahwa variabel kontinu harus memiliki rentang tak berhingga ($-\infty$ sampai $\infty$).</sub>
- B. Tidak, karena tebal lembaran pelat dapat dikelompokkan ke dalam ukuran persepuluhan milimeter.  
  <sub>Salah: Mengacaukan proses pembulatan diskret dengan sifat kontinu dari variabel aslinya.</sub>
- C. Ya, karena nilai $T$ selalu berupa bilangan bulat positif yang tersebar merata.  
  <sub>Salah: Keliru menyebut sifat nilai variabel acak kontinu sebagai bilangan bulat, padahal bilangan real.</sub>
- **D. Ya, karena nilai $T$ diperoleh melalui proses pengukuran dan mencakup seluruh bilangan real pada interval $[1,8;\ 2,4]$ sehingga tak terhitung.** ✅  
  <sub>Benar: Ketebalan diperoleh melalui pengukuran dan nilainya membentuk selang kontinu bilangan real yang tak terhitung (*uncountable*).</sub>

**Pembahasan:** Ketebalan $T$ diperoleh dari pengukuran fisik dan nilainya dapat berupa bilangan desimal berapapun di antara $1,8\text{ mm}$ dan $2,4\text{ mm}$. Karena ruang nilainya membentuk interval kontinu pada himpunan bilangan real dan tidak dapat dicacah satu per satu, $T$ memenuhi definisi variabel acak kontinu.
**Acuan:** siswa — siswa hal.255 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b04-c-medium-bt01-007
*orisinal | C4 | 3 langkah | jenis: identifikasi ruang sampel kontinu*

Perhatikan empat definisi ruang sampel untuk variabel acak berikut:
(1) $S_1 = \{x \mid 10 \le x \le 20,\ x \in \mathbb{N}\}$
(2) $S_2 = \{x \mid 0 < x < 1,\ x \in \mathbb{Q}\}$
(3) $S_3 = \{x \mid 5,0 \le x \le 8,5,\ x \in \mathbb{R}\}$
(4) $S_4 = \{x \mid x = 2n,\ n \in \mathbb{Z}^+\}$

Berdasarkan Definisi 4.3 mengenai variabel acak kontinu, ruang sampel yang mendefinisikan variabel acak kontinu adalah ....

- A. (2) dan (3)  
  <sub>Salah: Mengira himpunan bilangan rasional $\mathbb{Q}$ bersifat tak terhitung karena padat di antara 0 dan 1, padahal $\mathbb{Q}$ bersifat terhitung (*countable*).</sub>
- **B. (3) saja** ✅  
  <sub>Benar: Definisi 4.3 mensyaratkan ruang sampel tak terhitung (uncountable), yang hanya dipenuhi oleh interval bilangan real $S_3$.</sub>
- C. (2), (3), dan (4)  
  <sub>Salah: Menganggap semua himpunan beranggotakan tak hingga otomatis tak terhitung (*uncountable*).</sub>
- D. (1) dan (4)  
  <sub>Salah: Memilih himpunan diskret yang jelas-jelas terhitung (*countable*).</sub>

**Pembahasan:** Berdasarkan Definisi 4.3, variabel acak kontinu didefinisikan pada ruang sampel yang tak terhitung (*uncountable*).
- $S_1$ berhingga (terhitung).
- $S_2$ merupakan himpunan bilangan rasional, yang secara matematis beranggotakan tak hingga tetapi terhitung (*countably infinite*).
- $S_3$ merupakan interval tertutup pada bilangan real $\mathbb{R}$, yang bersifat tak terhitung (*uncountable*).
- $S_4$ merupakan himpunan bilangan genap positif yang terhitung (*countably infinite*).
Jadi, hanya (3) yang mendefinisikan variabel acak kontinu.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b04-c-medium-bt01-008
*orisinal | C3 | 2 langkah | jenis: pemilahan tipe data pengukuran*

Seorang petugas kesehatan mencatat beberapa variabel acak dari sejumlah balita di posyandu:
(1) $W$: Berat badan balita (dalam kg)
(2) $N$: Frekuensi kunjungan imunisasi yang telah diikuti balita
(3) $L$: Panjang lingkar kepala balita (dalam cm)
(4) $G$: Banyaknya gigi susu yang telah tumbuh

Pasangan variabel acak yang keduanya tergolong variabel acak kontinu adalah ....

- **A. (1) dan (3)** ✅  
  <sub>Benar: Berat badan ($W$) dan lingkar kepala ($L$) diperoleh melalui pengukuran kontinu dan nilainya tak terhitung dalam suatu rentang.</sub>
- B. (2) dan (4)  
  <sub>Salah: Keduanya merupakan variabel acak diskret hasil penghitungan bilangan bulat nonnegatif.</sub>
- C. (3) dan (4)  
  <sub>Salah: $G$ adalah hasil pencacahan (diskret), bukan variabel acak kontinu.</sub>
- D. (1) dan (2)  
  <sub>Salah: $N$ adalah hasil membilang/menghitung sehingga merupakan variabel acak diskret.</sub>

**Pembahasan:** Variabel acak kontinu diperoleh dari proses pengukuran fisik dan nilainya dapat berupa bilangan desimal dalam rentang tertentu yang tidak dapat dicacah satu per satu. Berat badan ($W$) dan lingkar kepala ($L$) diperoleh dari pengukuran menggunakan alat ukur, sehingga keduanya merupakan variabel acak kontinu. Sebaliknya, frekuensi kunjungan ($N$) dan banyak gigi susu ($G$) diperoleh dari proses mencacah/menghitung satu per satu, sehingga merupakan variabel acak diskret.
**Acuan:** siswa — siswa hal.254

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b04-c-medium-bt01-009
*variasi (konteks) | C3 | 2 langkah | jenis: formulasi ruang sampel kontinu*

Suatu larutan kimia memerlukan waktu pengendapan partikel yang dicatat dalam menit. Misalkan $T$ adalah variabel acak kontinu yang menyatakan waktu pengendapan tersebut, dengan hasil pengamatan selalu berada pada rentang $6,4\text{ menit}$ hingga $9,8\text{ menit}$. Bentuk penulisan ruang sampel $S$ yang tepat untuk variabel acak tersebut adalah ....

- A. $S = \{t \mid 6,4 \le t \le 9,8,\ t \in \mathbb{Z}\}$  
  <sub>Salah: Menggunakan himpunan bilangan bulat (Z), bukan bilangan real (R).</sub>
- B. $S = \{6,4;\ 7,0;\ 8,0;\ 9,0;\ 9,8\}$  
  <sub>Salah: Menuliskan ruang sampel secara diskret diskrit tercacah padahal variabel kontinu memuat tak terhingga nilai desimal.</sub>
- **C. $S = \{t \mid 6,4 \le t \le 9,8,\ t \in \mathbb{R}\}$** ✅  
  <sub>Benar: Ruang sampel variabel acak kontinu memuat seluruh bilangan real pada interval batas ukur, ditulis $S = \{t \mid 6,4 \le t \le 9,8,\ t \in \mathbb{R}\}$.</sub>
- D. $S = \{t \mid 6,4 < t < 9,8,\ t \in \mathbb{Q}\}$  
  <sub>Salah: Mengabaikan nilai batas (pertidaksamaan murni) dan membatasi pada bilangan rasional (Q).</sub>

**Pembahasan:** Variabel acak $T$ merupakan variabel acak kontinu karena diperoleh dari pengukuran waktu. Nilai $T$ mencakup seluruh bilangan real dari batas bawah $6,4$ hingga batas atas $9,8$, termasuk kedua batas tersebut. Oleh karena itu, bentuk notasi pembentuk himpunan untuk ruang sampelnya adalah:
$$S = \{t \mid 6,4 \le t \le 9,8,\ t \in \mathbb{R}\}$$
**Acuan:** siswa — siswa hal.256 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b04-c-medium-bt01-010
*variasi (konteks) | C4 | 2 langkah | jenis: evaluasi ketaktercacahan nilai*

Laju alir cairan pelarut melalui suatu pipa kapiler berkisar dari $15,2\text{ mL/s}$ hingga $19,6\text{ mL/s}$. Misalkan $Q$ adalah variabel acak yang menyatakan laju alir tersebut dalam satuan $\text{mL/s}$. Apakah seluruh kemungkinan nilai laju alir dalam ruang sampel tersebut dapat dihitung atau dicacah satu per satu? Berikan penjelasan yang tepat.

- **A. Tidak dapat, karena ruang sampel $Q$ memuat seluruh bilangan real dalam interval tersebut sehingga jumlah nilainya tak terhitung (uncountable).** ✅  
  <sub>Benar: Variabel acak kontinu didefinisikan pada interval bilangan real yang nilainya rapat dan tak terhitung (uncountable).</sub>
- B. Dapat, asalkan nilai laju alir dibulatkan ke satu tempat desimal terdekat.  
  <sub>Salah: Memaksa pembulatan instrumen pengukuran sehingga mengubah sifat kontinu alami menjadi diskret.</sub>
- C. Dapat, karena selisih nilai terbesar dan terkecil berhingga yaitu $4,4\text{ mL/s}$.  
  <sub>Salah: Mengacaukan panjang rentang (interval berhingga) dengan banyak titik sampel di dalam rentang.</sub>
- D. Tidak dapat, karena nilai batas atas $19,6\text{ mL/s}$ tidak pasti tercapai dalam eksperimen.  
  <sub>Salah: Memberikan alasan empiris tentang kepastian nilai batas, bukan sifat ketakterhitungan bilangan real.</sub>

**Pembahasan:** Laju alir $Q$ adalah variabel acak kontinu yang terbentuk dari proses pengukuran. Ruang sampel variabel acak ini berupa interval bilangan real $[15,2;\ 19,6]$. Karena antara sembarang dua bilangan real selalu memuat tak hingga banyak bilangan real lainnya, kemungkinan nilai laju alir tidak dapat dicacah atau dihitung satu per satu (uncountable).
**Acuan:** pretest — kelas12_tl-b04-p0257-latihan-soal-variabel-acak-kontinu-c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b04-c-medium-bt01-011
*orisinal | C4 | 2 langkah | jenis: analisis densitas rentang kontinu*

Seorang laboran mengamati massa endapan $M$ (dalam gram) hasil suatu reaksi kimia yang berada pada rentang $2,40\text{ gram} \le M \le 2,50\text{ gram}$. Dari pengujian berulang, tercatat dua hasil yaitu $2,42\text{ gram}$ dan $2,43\text{ gram}$. Berdasarkan sifat variabel acak kontinu, pernyataan yang paling tepat mengenai kemungkinan nilai massa endapan di antara kedua nilai tersebut adalah ....

- **A. Terdapat tak hingga banyak kemungkinan nilai massa riil di antara $2,42\text{ gram}$ dan $2,43\text{ gram}$ karena nilainya membentuk rentang tak terputus.** ✅  
  <sub>Benar: Nilai variabel acak kontinu membentuk rentang tak terputus pada bilangan real sehingga di antara dua nilai sembarang selalu ada nilai lain tak hingga banyaknya.</sub>
- B. Hanya terdapat tepat satu nilai di tengah, yaitu nilai rata-rata $2,425\text{ gram}$.  
  <sub>Salah: Mengira hanya nilai tengah rata-rata aritmetika yang dapat menjadi nilai variabel.</sub>
- C. Tidak ada kemungkinan nilai lain karena data pengukuran hanya menggunakan dua angka di belakang koma.  
  <sub>Salah: Menganggap format penyajian desimal membatasi keberadaan nilai kontinu sebenarnya.</sub>
- D. Hanya terdapat tepat sembilan kemungkinan nilai baru jika ketelitian dinaikkan menjadi dua desimal berikutnya.  
  <sub>Salah: Membatasi ketelitian instrumen pada digit diskret tertentu, bukan sifat kontinu teoritis.</sub>

**Pembahasan:** Salah satu ciri utama variabel acak kontinu adalah nilainya berupa bilangan real yang membentuk rentang tak terputus. Hal ini berarti di antara dua nilai tertentu ($2,42$ dan $2,43$), selalu terdapat kemungkinan nilai lain dalam jumlah tak hingga banyaknya (seperti $2,421$; $2,4256$; $2,42981$, dst.) yang masih termasuk dalam variabel acak tersebut.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b04-c-medium-bt01-012
*orisinal | C3 | 2 langkah | jenis: identifikasi variabel kontinu*

Perhatikan empat variabel acak yang diamati pada suatu pabrik farmasi berikut:
(1) Tekanan gas dalam tabung reaksi yang berada pada rentang $1,8\text{ atm}$ hingga $2,4\text{ atm}$.
(2) Jumlah botol sirup yang cacat selama proses pengemasan per giliran kerja.
(3) Konsentrasi zat aktif dalam larutan uji yang berkisar antara $0,05\text{ mg/mL}$ hingga $0,15\text{ mg/mL}$.
(4) Banyaknya teknisi laboratorium yang bertugas pada shift pagi.

Berdasarkan stimulus tersebut, variabel acak yang tergolong sebagai variabel acak kontinu adalah ....

- A. (1) dan (2)  
  <sub>Salah: Salah mengklasifikasikan jumlah botol cacat (diskret) sebagai variabel acak kontinu.</sub>
- **B. (1) dan (3)** ✅  
  <sub>Benar: (1) dan (3) diperoleh dari hasil pengukuran dan nilainya berada dalam rentang kontinu desimal tak terhitung.</sub>
- C. (2) dan (4)  
  <sub>Salah: Memilih variabel acak diskret yang diperoleh melalui proses menghitung/mencacah bilangan bulat nonnegatif.</sub>
- D. (2) dan (3)  
  <sub>Salah: Mencampurkan satu variabel acak diskret (jumlah botol) dengan satu variabel acak kontinu (konsentrasi).</sub>

**Pembahasan:** Variabel acak kontinu diperoleh dari hasil pengukuran, memiliki nilai berupa bilangan real dalam suatu rentang, dan nilainya tak terhitung (uncountable):
- (1) Tekanan gas: diukur, bernilai real kontinu.
- (2) Jumlah botol: dihitung (cacah), bernilai bulat (diskret).
- (3) Konsentrasi zat aktif: diukur, bernilai real kontinu.
- (4) Banyaknya teknisi: dihitung (cacah), bernilai bulat (diskret).
Jadi, variabel acak kontinu adalah (1) dan (3).
**Acuan:** siswa — siswa hal.254

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b04-c-medium-bt01-013
*variasi (angka) | C3 | 2 langkah | jenis: penentuan ruang sampel kontinu*

Pada musim penghujan, suhu udara harian di sebuah dataran tinggi berkisar dari $18,4^\circ\text{C}$ hingga $24,0^\circ\text{C}$. Misalkan $X$ adalah variabel acak yang menyatakan suhu udara harian dalam derajat Celsius. Bentuk taksiran ruang sampel dari variabel acak suhu harian tersebut adalah ....

- A. $S = \{18,4;\ 19,0;\ 20,0;\ 21,0;\ 22,0;\ 23,0;\ 24,0\}$  
  <sub>Salah: Siswa mendaftar nilai secara diskret dan mengabaikan nilai desimal tak terhitung di antara dua titik.</sub>
- B. $S = \{x \mid 18,4 \le x \le 24,0,\ x \in \mathbb{Z}\}$  
  <sub>Salah: Siswa keliru menganggap anggota ruang sampel variabel acak kontinu berupa bilangan bulat.</sub>
- C. $S = \{x \mid 18,4 < x < 24,0,\ x \in \mathbb{Q}\}$  
  <sub>Salah: Siswa salah menggunakan tanda pertidaksamaan ketat dan membatasi himpunan hanya pada bilangan rasional.</sub>
- **D. $S = \{x \mid 18,4 \le x \le 24,0,\ x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Suhu udara diperoleh dari pengukuran sehingga merupakan variabel acak kontinu yang memuat seluruh nilai bilangan real dalam rentang batas tersebut.</sub>

**Pembahasan:** Suhu udara merupakan variabel acak kontinu karena nilainya diperoleh melalui pengukuran dan dapat bernilai pecahan atau desimal tak terhitung dalam suatu rentang. Oleh karena itu, ruang sampelnya mencakup semua bilangan real dari batas bawah hingga batas atas, yaitu $S = \{x \mid 18,4 \le x \le 24,0,\ x \in \mathbb{R}\}$.
**Acuan:** pretest — kelas12_tl-b04-p0257-latihan-soal-variabel-acak-kontinu-b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b04-c-medium-bt01-014
*variasi (konteks) | C3 | 2 langkah | jenis: formulasi rentang ruang sampel*

Arus listrik yang mengalir melalui suatu elemen pemanas laboratorium berfluktuasi secara acak pada rentang $3,50\text{ A}$ hingga $5,25\text{ A}$. Jika $I$ adalah variabel acak kontinu yang menyatakan kuat arus listrik tersebut dalam ampere, representasi ruang sampel yang tepat untuk variabel acak $I$ adalah ....

- **A. $S = \{i \mid 3,50 \le i \le 5,25,\ i \in \mathbb{R}\}$** ✅  
  <sub>Benar: Kuat arus listrik adalah besaran kontinu hasil pengukuran sehingga mencakup semua bilangan real dalam interval tertutup $[3,50; 5,25]$.</sub>
- B. $S = \{3,50;\ 4,00;\ 4,50;\ 5,00;\ 5,25\}$  
  <sub>Salah: Siswa menganggap ruang sampel hanya terdiri dari nilai-nilai diskret kelipatan desimal tertentu.</sub>
- C. $S = \{i \mid 3,50 < i < 5,25,\ i \in \mathbb{R}\}$  
  <sub>Salah: Siswa keliru tidak memasukkan nilai batas pengukuran dengan menggunakan pertidaksamaan terbuka.</sub>
- D. $S = \{i \mid 3,50 \le i \le 5,25,\ i \in \mathbb{N}\}$  
  <sub>Salah: Siswa keliru menggunakan himpunan bilangan asli untuk variabel hasil pengukuran kontinu.</sub>

**Pembahasan:** Kuat arus listrik $I$ merupakan variabel acak kontinu karena nilainya dapat berada di sembarang titik real pada selang batas pengukuran. Dengan demikian, ruang sampelnya didefinisikan sebagai himpunan semua bilangan real dari $3,50$ sampai $5,25$, yaitu $S = \{i \mid 3,50 \le i \le 5,25,\ i \in \mathbb{R}\}$.
**Acuan:** pretest — kelas12_tl-b04-p0257-latihan-soal-variabel-acak-kontinu-b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b04-c-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: karakteristik interval kontinu*

Sebuah eksperimen kimia mengukur volume gas hidrogen $V$ yang dihasilkan dalam rentang $12,0\text{ mL} \le V \le 15,0\text{ mL}$. Dua data pencatatan berturut-turut menunjukkan volume sebesar $13,4\text{ mL}$ dan $13,5\text{ mL}$. Berdasarkan ciri-ciri variabel acak kontinu, simpulan yang benar mengenai nilai-nilai yang mungkin berada di antara kedua hasil pengukuran tersebut adalah ....

- A. Tidak ada kemungkinan nilai lain di antara keduanya karena resolusi pencatatan sudah berhenti pada satu tempat desimal.  
  <sub>Salah: Siswa menyamakan keterbatasan alat ukur dengan karakteristik teoretis dari ruang sampel variabel acak kontinu.</sub>
- **B. Terdapat tak hingga banyak kemungkinan nilai volume lain di antara $13,4\text{ mL}$ dan $13,5\text{ mL}$ karena nilainya membentuk rentang tak terputus pada bilangan real.** ✅  
  <sub>Benar: Variabel acak kontinu membentuk rentang tak terputus pada himpunan bilangan real sehingga di antara sembarang dua nilai selalu ada tak hingga banyaknya nilai real lain.</sub>
- C. Hanya terdapat sembilan kemungkinan nilai lain, yaitu dari $13,41\text{ mL}$ sampai $13,49\text{ mL}$.  
  <sub>Salah: Siswa membatasi nilai bilangan real hanya pada presisi dua tempat desimal.</sub>
- D. Hanya terdapat tepat satu nilai perantara, yaitu nilai rata-rata dari kedua pengukuran sebesar $13,45\text{ mL}$.  
  <sub>Salah: Siswa keliru menganggap hanya nilai tengah yang mungkin muncul di antara dua pengukuran.</sub>

**Pembahasan:** Menurut sifat variabel acak kontinu, nilainya mencakup seluruh bilangan real pada interval tertentu dan membentuk rentang tak terputus. Oleh karena itu, di antara dua nilai sembarang seperti $13,4\text{ mL}$ dan $13,5\text{ mL}$, selalu terdapat tak hingga banyak nilai desimal lain yang mungkin terjadi.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b04-c-medium-bt01-016
*orisinal | C3 | 2 langkah | jenis: klasifikasi variabel acak*

Seorang petugas stasiun meteorologi mencatat empat variabel acak selama pengamatan cuaca harian:
(1) Kecepatan hembusan angin (dalam km/jam)
(2) Banyaknya hari hujan dalam satu bulan
(3) Curah hujan harian (dalam mm)
(4) Banyaknya stasiun pemantau cuaca yang aktif

Pasangan variabel acak yang tergolong sebagai variabel acak kontinu adalah ....

- A. (2) dan (4)  
  <sub>Salah: Siswa memilih pasangan variabel acak diskret alih-alih variabel acak kontinu.</sub>
- B. (1) dan (2)  
  <sub>Salah: Siswa salah mengira banyaknya hari hujan adalah variabel kontinu, padahal merupakan variabel diskret hasil pencacahan.</sub>
- **C. (1) dan (3)** ✅  
  <sub>Benar: Kecepatan angin dan curah hujan diperoleh dari hasil pengukuran dan nilainya berada dalam rentang bilangan real tak terhitung.</sub>
- D. (3) dan (4)  
  <sub>Salah: Siswa keliru mengidentifikasi banyaknya stasiun pemantau sebagai variabel kontinu.</sub>

**Pembahasan:** Variabel acak kontinu diperoleh melalui proses pengukuran dan nilainya berupa bilangan real dalam suatu interval (uncountable). Dari keempat variabel tersebut, kecepatan angin (1) dan curah hujan harian (3) diperoleh melalui alat ukur sehingga merupakan variabel acak kontinu. Sedangkan banyaknya hari hujan (2) dan banyaknya stasiun (4) diperoleh dari hasil pencacahan (bilangan cacah) sehingga merupakan variabel acak diskret.
**Acuan:** siswa — siswa hal.254

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b04-c-medium-bt01-017
*orisinal | C4 | 3 langkah | jenis: analisis ruang sampel tak terhitung*

Perhatikan daerah nilai dari empat variabel acak yang berkaitan dengan operasional bus antarkota berikut:
- $R_P = \{t \in \mathbb{R} \mid 0 \le t \le 120\}$ (waktu keterlambatan bus dalam menit)
- $R_Q = \{n \in \mathbb{N} \mid 0 \le n \le 60\}$ (jumlah penumpang di dalam bus)
- $R_R = \{20, 25, 30, 35, 40\}$ (pilihan tarif bagasi lebih dalam ribuan rupiah)
- $R_S = \{v \in \mathbb{R} \mid 40 \le v \le 100\}$ (kecepatan rata-rata bus dalam km/jam)

Variabel acak yang memiliki ruang sampel kontinu adalah ....

- A. $P$ dan $Q$  
  <sub>Salah: Siswa mengira $R_Q$ kontinu hanya karena dibatasi oleh rentang $0 \le n \le 60$, mengabaikan syarat $n \in \mathbb{N}$.</sub>
- **B. $P$ dan $S$** ✅  
  <sub>Benar: Daerah nilai $R_P$ dan $R_S$ memuat seluruh bilangan real dalam interval tertutup sehingga bersifat tak terhitung (uncountable).</sub>
- C. $Q$ dan $R$  
  <sub>Salah: Siswa memilih himpunan bilangan bulat dan berhingga yang merupakan representasi ruang sampel diskret.</sub>
- D. $R$ dan $S$  
  <sub>Salah: Siswa gagal membedakan himpunan nilai diskret berhingga pada $R_R$ dengan interval bilangan real kontinu pada $R_S$.</sub>

**Pembahasan:** Ruang sampel kontinu adalah ruang sampel yang titik-titik anggotanya tak terhitung banyaknya (uncountable), biasanya didefinisikan pada interval bilangan real $\mathbb{R}$. Pada $R_P$ dan $R_S$, nilai variabel mencakup seluruh bilangan real pada rentang masing-masing sehingga keduanya merupakan variabel acak kontinu. Sebaliknya, $R_Q$ terdiri atas bilangan asli (terhitung) dan $R_R$ berupa himpunan terhingga diskret.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b04-c-medium-bt01-018
*variasi (konteks) | C4 | 2 langkah | jenis: pengelompokan variabel tak terhitung*

Perhatikan lima variabel acak yang diamati pada jalur perakitan suatu pabrik otomotif berikut:
(1) Waktu yang dibutuhkan seorang teknisi untuk merakit satu unit transmisi
(2) Banyaknya cacat las yang terdeteksi pada rangka bodi mobil
(3) Tekanan oli hidrolik pada sistem kemudi saat dilakukan uji jalan
(4) Banyaknya baut yang terpasang pada satu blok mesin kendaraan
(5) Konsumsi bahan bakar kendaraan selama pengujian emisi sejauh $100\text{ km}$

Manakah dari variabel-variabel acak di atas yang memiliki nilai tak terhitung banyaknya dalam suatu rentang?

- A. (1), (2), dan (3)  
  <sub>Salah: Menyertakan variabel (2) banyaknya cacat las yang merupakan variabel diskret terbilang.</sub>
- B. (2) dan (4)  
  <sub>Salah: Memilih variabel acak diskret hasil pencacahan atau perhitungan satu per satu yang nilainya terhitung (countable).</sub>
- C. (3), (4), dan (5)  
  <sub>Salah: Menyertakan variabel (4) banyaknya baut yang merupakan variabel diskret hasil pencacahan.</sub>
- **D. (1), (3), dan (5)** ✅  
  <sub>Benar: Variabel (1) waktu, (3) tekanan, dan (5) volume konsumsi bahan bakar merupakan besaran hasil pengukuran yang bernilai bilangan real kontinu dalam suatu interval sehingga memiliki nilai tak terhitung banyaknya (uncountable).</sub>

**Pembahasan:** Variabel acak kontinu dicirikan oleh perolehan nilainya melalui proses pengukuran sehingga mencakup semua bilangan real pada suatu interval tak terputus. Akibatnya, nilai-nilai tersebut tak terhitung banyaknya (_uncountable_).
- (1) Waktu perakitan $\rightarrow$ hasil pengukuran waktu (kontinu, tak terhitung).
- (2) Banyak cacat las $\rightarrow$ hasil membilang/mencacah (diskret, terhitung).
- (3) Tekanan oli $\rightarrow$ hasil pengukuran tekanan (kontinu, tak terhitung).
- (4) Banyak baut $\rightarrow$ hasil membilang/mencacah (diskret, terhitung).
- (5) Konsumsi bahan bakar $\rightarrow$ hasil pengukuran volume cairan (kontinu, tak terhitung).
Jadi, variabel yang memiliki nilai tak terhitung banyaknya adalah (1), (3), dan (5).
**Acuan:** siswa — siswa hal.254 Ayo Berdiskusi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b04-c-medium-bt01-019
*variasi (konteks) | C4 | 2 langkah | jenis: analisis ketercacahan peubah acak*

Sebuah tim peneliti di stasiun pemantauan gunung api mencatat lima variabel acak selama masa observasi:
(1) Frekuensi gempa vulkanik dangkal yang terekam seismograf per hari
(2) Laju curah hujan per jam di lereng kawah yang dicatat sensor otomatis
(3) Jumlah kera liar yang terpantau melintas di sekitar pos pengamatan
(4) Konsentrasi gas belerang di udara ambien pada radius pengamanan
(5) Perubahan elevasi kubah lava hasil pengukuran teodolit digital

Berdasarkan karakteristik variabel acak, kelompok variabel yang memiliki kemungkinan nilai tak terhitung banyaknya dalam suatu selang adalah ....

- A. (1) dan (3)  
  <sub>Salah: Memilih variabel acak diskret yang diperoleh dari proses membilang atau pencacahan kejadian.</sub>
- B. (1), (2), dan (4)  
  <sub>Salah: Keliru menganggap frekuensi gempa sebagai variabel kontinu padahal menyatakan banyak kejadian diskret.</sub>
- **C. (2), (4), dan (5)** ✅  
  <sub>Benar: Laju curah hujan, konsentrasi gas belerang, dan perubahan elevasi diperoleh melalui instrumen pengukuran fisik sehingga nilainya dapat berupa sembarang bilangan real pada suatu selang (kontinu dan tak terhitung).</sub>
- D. (2), (3), dan (5)  
  <sub>Salah: Menyertakan jumlah kera liar yang merupakan peubah diskret berhingga atau terhitung.</sub>

**Pembahasan:** Variabel acak yang memiliki nilai tak berhingga dan tak terhitung (_uncountable_) pada suatu rentang adalah variabel acak kontinu yang diperoleh melalui pengukuran besaran fisik:
- (1) Frekuensi gempa $\rightarrow$ pencacahan kejadian bulat $0, 1, 2, \dots$ (diskret, terhitung).
- (2) Laju curah hujan $\rightarrow$ pengukuran volume/tinggi air per satuan waktu (kontinu, tak terhitung).
- (3) Jumlah kera liar $\rightarrow$ pencacahan individu (diskret, terhitung).
- (4) Konsentrasi gas $\rightarrow$ pengukuran kadar/fraksi zat dalam udara (kontinu, tak terhitung).
- (5) Perubahan elevasi $\rightarrow$ pengukuran panjang/ketinggian (kontinu, tak terhitung).
Dengan demikian, variabel yang memiliki nilai tak terhitung banyaknya dalam suatu selang adalah (2), (4), dan (5).
**Acuan:** siswa — siswa hal.254 Ayo Berdiskusi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b04-c-medium-bt01-020
*orisinal | C3 | 2 langkah | jenis: representasi garis bilangan kontinu*

Sebuah mesin pemanas induksi memanaskan pelat logam selama rentang waktu $X$ menit dengan batas $6 \le X \le 15$. Jika $X$ dimodelkan sebagai variabel acak kontinu, representasi yang paling tepat untuk ruang hasil dari variabel $X$ pada garis bilangan real adalah ....

- A. himpunan titik-titik diskret berjarak tetap 0,1 unit di sepanjang interval 6 hingga 15  
  <sub>Salah: Mengira nilai kontinu dibatasi oleh resolusi alat ukur tertentu dan bukan seluruh bilangan real.</sub>
- B. kumpulan sepuluh titik terpisah tepat di atas bilangan bulat 6, 7, 8, sampai 15  
  <sub>Salah: Memodelkan variabel acak diskret yang hanya bernilai bilangan bulat terpisah.</sub>
- **C. ruas garis padat tak terputus dari angka 6 hingga 15 karena memuat seluruh bilangan real di antara kedua titik tersebut** ✅  
  <sub>Benar: Sesuai definisi representasi garis bilangan variabel acak kontinu, nilainya mencakup seluruh bilangan real pada interval $[6, 15]$ sehingga membentuk segmen garis kontinu tak berlubang.</sub>
- D. hanya dua buah titik penanda batas pada posisi angka 6 dan angka 15  
  <sub>Salah: Hanya menandai batas interval tanpa menyertakan deretan nilai kontinu di antara batas tersebut.</sub>

**Pembahasan:** Berdasarkan ciri-ciri variabel acak kontinu pada buku pelajaran, nilai-nilai variabel kontinu merupakan bilangan real yang membentuk rentang tak terputus. Pada garis bilangan, ruang sampel ini direpresentasikan berupa deretan titik yang terhubung rapat tanpa celah sehingga membentuk suatu ruas garis (segmen garis) padat dari batas bawah 6 hingga batas atas 15.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b04-c-hard-bt01-001
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi kesimpulan*

Sebuah mesin otomatis mengemas bubuk detergen ke dalam kantong dengan target massa $1.000\text{ gram}$. Akibat getaran mekanik corong tuang, massa detergen riil $M$ terdistribusi acak dalam rentang $990\text{ gram} \le M \le 1.010\text{ gram}$. Seorang teknisi menyatakan bahwa $M$ bukan variabel acak kontinu dengan alasan: timbangan digital pabrik hanya memiliki presisi satu desimal ($0,1\text{ gram}$), sehingga nilai $M$ yang mungkin dicatat hanyalah nilai-nilai diskret kelipatan $0,1\text{ gram}$ sebanyak 201 kemungkinan nilai.

Bagaimanakah penilaian yang benar terhadap klaim teknisi tersebut berdasarkan konsep variabel acak kontinu?

- A. Klaim benar, karena variabel acak didefinisikan secara ketat berdasarkan data numerik yang benar-benar tercatat pada memori alat ukur digital.  
  <sub>Salah: Siswa terjebak definisi empiris sempit dan mengabaikan definisi matematis ruang sampel teoritis.</sub>
- B. Klaim salah, karena variabel acak kontinu hanya boleh memiliki batas rentang yang bernilai pecahan, bukan bilangan bulat seperti 990 dan 1.010.  
  <sub>Salah: Siswa memiliki miskonsepsi bahwa batas interval variabel kontinu tidak boleh bilangan bulat.</sub>
- C. Klaim benar, karena jika suatu besaran dapat dicacah menjadi 201 nilai, variabel tersebut otomatis berubah menjadi variabel diskret permanen.  
  <sub>Salah: Siswa mengira pembulatan alat ukur membatalkan status kontinuitas fisik variabel.</sub>
- **D. Klaim salah, karena diskretisasi pencatatan oleh timbangan hanyalah aproksimasi pengukuran, sedangkan massa fisik detergen sebenarnya mencakup seluruh nilai real tak terhitung pada interval $[990, 1010]$.** ✅  
  <sub>Benar: Secara hakiki besaran massa diperoleh dari proses pengukuran kontinu dengan rentang tak terputus dalam bilangan real, sehingga keterbatasan tampilan digital tidak membatalkan sifat kontinunya.</sub>

**Pembahasan:** Berdasarkan konsep variabel acak kontinu, nilai besaran massa merupakan hasil pengukuran kontinu di mana antara dua nilai selalu terdapat nilai lain di dalam bilangan real (uncountable). Fakta bahwa timbangan digital menampilkan data berjarak 0,1 gram hanyalah batasan instrumen pengukuran (kuantisasi alat), bukan karakteristik dari variabel acak massa detergen itu sendiri. Jadi, klaim teknisi tersebut salah.
**Acuan:** siswa — siswa hal.255 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b04-c-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: analisis representasi*

Diberikan empat model matematis himpunan nilai suatu variabel acak $X$:
(1) $R_1 = \{x \in \mathbb{R} \mid 2 < x < 5\}$
(2) $R_2 = \{x \in \mathbb{Q} \mid 2 \le x \le 5\}$
(3) $R_3 = \{x \in \mathbb{R} \mid x = 2 + 0,1k,\ k \in \mathbb{Z},\ 0 \le k \le 30\}$
(4) $R_4 = [2, 3] \cup [4, 5]$ dengan $x \in \mathbb{R}$

Himpunan manakah yang jika digambarkan pada garis bilangan secara teoretis benar-benar membentuk segmen garis padat tak terputus (memenuhi representasi variabel acak kontinu)?

- **A. (1) saja di antara (1), (2), dan (3), serta komponen rentang pada (4) masing-masing berupa garis padat.** ✅  
  <sub>Benar: Himpunan bilangan real pada interval terbuka maupun tertutup membentuk garis padat kontinu tanpa celah, sedangkan bilangan rasional atau himpunan titik berjarak diskret memiliki tak hingga banyak celah kosong.</sub>
- B. (3) saja, karena memiliki jarak langkah yang seragam dan pasti di sepanjang interval.  
  <sub>Salah: Siswa mengira sekumpulan titik diskret rapat sama dengan garis kontinu padat.</sub>
- C. (1) dan (2), karena keduanya mencakup batas bawah 2 hingga batas atas 5.  
  <sub>Salah: Siswa mengabaikan perbedaan mendasar antara kerapatan himpunan rasional (tidak kontinu/lengkap) dengan kelengkapan himpunan bilangan real.</sub>
- D. (2) saja, karena himpunan bilangan rasional mencakup seluruh pecahan desimal terukur.  
  <sub>Salah: Siswa mengabaikan keberadaan bilangan irasional di antara dua bilangan rasional yang menyebabkan garis bilangan berlubang.</sub>

**Pembahasan:** Berdasarkan ciri-ciri variabel acak kontinu, nilainya berupa bilangan real yang membentuk rentang tak terputus sehingga pada garis bilangan terwakili oleh ruas garis padat yang utuh. 
- $R_1 = (2, 5)$ pada $\mathbb{R}$ adalah segmen garis terbuka yang padat dan tak terputus.
- $R_2$ hanya memuat bilangan rasional; di dalamnya berlubang pada setiap bilangan irasional, sehingga bukan garis padat tak terputus.
- $R_3$ terdiri atas 31 titik diskret terpisah.
- $R_4$ memuat dua segmen garis padat terpisah.
Oleh karena itu, di antara himpunan tunggal berkesinambungan (1), (2), dan (3), hanya (1) yang memenuhi representasi segmen garis padat tak terputus sejati.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b04-c-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: evaluasi perbandingan*

Seorang guru meminta dua siswa membandingkan dua variabel acak:
- Variabel $A$: Banyaknya tetesan air hujan yang jatuh pada suatu wadah dalam selang waktu 1 menit.
- Variabel $B$: Volume total air hujan (dalam mililiter) yang terkumpul dalam wadah tersebut selama 1 menit.

Siswa 1 menyatakan: "Kedua variabel acak bernilai tak hingga, sehingga keduanya sama-sama tergolong variabel acak kontinu."
Siswa 2 menyatakan: "Variabel $A$ dapat didaftar satu per satu nilainya menggunakan bilangan cacah $\{0, 1, 2, \dots\}$, sedangkan nilai variabel $B$ membentuk selang bilangan real tak terputus sehingga tak terhitung (uncountable). Oleh karena itu, $A$ diskret dan $B$ kontinu."

Pernyataan evaluasi yang paling tepat mengenai pendapat kedua siswa tersebut adalah ....

- A. Pendapat Siswa 1 benar, karena setiap variabel yang memiliki kemungkinan nilai tak berhingga secara otomatis merupakan variabel acak kontinu.  
  <sub>Salah: Siswa gagal membedakan antara tak berhingga terhitung (countably infinite) dan tak terhitung (uncountable).</sub>
- B. Kedua siswa salah, karena variabel A dan variabel B keduanya memiliki batas fisik penampung sehingga kedua variabel pasti berhingga dan diskret.  
  <sub>Salah: Siswa menyamakan adanya batas fisis maksimum dengan ketercacahan diskret.</sub>
- C. Pendapat Siswa 2 salah, karena volume air tersusun atas molekul-molekul diskret sehingga variabel B seharusnya tergolong diskret.  
  <sub>Salah: Siswa membawa konsep atomik fisika murni keluar dari konteks pemodelan makroskopik variabel acak kontinu.</sub>
- **D. Pendapat Siswa 2 benar, karena variabel acak diskret dapat memiliki nilai tak terhingga asalkan terhitung (countable), sedangkan variabel acak kontinu bersifat tak terhitung (uncountable).** ✅  
  <sub>Benar: Kriteria pembeda bukan terletak pada apakah nilainya berhingga atau tak hingga, melainkan apakah ruang sampelnya terhitung (countable) seperti himpunan bilangan cacah atau tak terhitung (uncountable) pada interval bilangan real.</sub>

**Pembahasan:** Ruang sampel tak berhingga terbagi menjadi dua: tak berhingga terhitung (countably infinite) dan tak berhingga tak terhitung (uncountable). Variabel $A$ (banyak tetesan) memiliki nilai pada $\mathbb{N}_0 = \{0, 1, 2, \dots\}$ yang terhitung, menjadikannya variabel acak diskret. Variabel $B$ (volume air) berupa hasil pengukuran pada interval bilangan real kontinu yang tak terhitung, menjadikannya variabel acak kontinu. Dengan demikian, pendapat Siswa 2 sepenuhnya tepat.
**Acuan:** siswa — siswa hal.254

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b04-c-hard-bt01-004
*variasi (konteks) | C5 | 3 langkah | jenis: evaluasi keterhitungan*

Dalam uji coba termal mesin, suhu fluida pendingin $T$ berfluktuasi secara kontinu pada rentang $82,5^\circ\text{C}$ hingga $91,0^\circ\text{C}$. Seorang asisten laboratorium berpendapat bahwa seluruh kemungkinan nilai $T$ dalam ruang sampel tersebut dapat didaftar dan dihitung satu per satu karena termometer digital yang digunakan memiliki resolusi pembacaan hingga 3 desimal ($0,001^\circ\text{C}$). Bagaimana evaluasi yang tepat terhadap pendapat asisten tersebut?

- A. Pendapat salah, karena variabel acak kontinu hanya dapat dihitung satu per satu apabila resolusi alat ukur diperluas hingga tidak berhingga banyak desimal.  
  <sub>Salah: Siswa mengira himpunan tak terhitung dapat dicacah jika alat ukurnya sempurna secara teoretis.</sub>
- B. Pendapat benar, karena pembacaan dengan presisi hingga 3 desimal memastikan seluruh kemungkinan titik suhu dapat dicacah secara tuntas sebanyak 8.501 nilai.  
  <sub>Salah: Siswa keliru menyamakan ruang pembacaan instrumen diskret dengan ruang sampel variabel acak kontinu yang sebenarnya.</sub>
- **C. Pendapat salah, karena resolusi alat ukur hanya membatasi pembacaan teknis, sedangkan nilai riil $T$ mencakup seluruh bilangan real pada rentang tersebut yang bersifat tak terhitung (uncountable).** ✅  
  <sub>Benar: Variabel acak kontinu didefinisikan pada ruang sampel bilangan real pada rentang tak terputus. Batasan resolusi alat ukur digital merupakan diskretisasi pengukuran, bukan representasi sifat ruang sampel aslinya yang tetap tak terhitung.</sub>
- D. Pendapat benar, karena rentang $82,5^\circ\text{C}$ sampai $91,0^\circ\text{C}$ merupakan himpunan berhingga sehingga seluruh anggotanya pasti dapat dihitung satu per satu.  
  <sub>Salah: Siswa salah memahami panjang interval yang berhingga sebagai jumlah anggota yang berhingga.</sub>

**Pembahasan:** Ruang sampel dari variabel acak kontinu suhu $T$ adalah $S = \{t \in \mathbb{R} \mid 82,5 \le t \le 91,0\}$. Meskipun alat ukur hanya dapat membaca nilai diskret dengan lompatan $0,001^\circ\text{C}$ (diskretisasi), nilai fisik sebenarnya dari $T$ mencakup seluruh bilangan real dalam interval tersebut. Karena interval bilangan real bersifat tak terhitung (_uncountable_), nilai-nilai ruang sampel tidak dapat dihitung satu per satu. Dengan demikian, pendapat asisten tersebut salah.
**Acuan:** pretest — kelas12_tl-b04-p0257-latihan-soal-variabel-acak-kontinu-c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b04-c-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: evaluasi model ruang sampel*

Diberikan empat usulan ruang sampel untuk memodelkan suatu variabel acak pengukuran:
1. $S_1 = \{x \in \mathbb{Q} \mid 0 \le x \le 5\}$
2. $S_2 = \{x \in \mathbb{R} \mid 0 \le x \le 5\}$
3. $S_3 = \{x \in \mathbb{R} \mid x = \frac{n}{100},\ n \in \mathbb{N},\ 0 \le n \le 500\}$
4. $S_4 = (1, 2) \cup (3, 4)$ dengan seluruh titik merupakan bilangan real

Berdasarkan Definisi 4.3 mengenai variabel acak kontinu, model ruang sampel yang valid sebagai ruang sampel variabel acak kontinu adalah ....

- **A. $S_2$ dan $S_4$ saja** ✅  
  <sub>Benar: $S_2$ dan $S_4$ keduanya memuat interval bilangan real yang tak berhingga dan tak terhitung (uncountable). Sebaliknya, $S_1$ (himpunan bilangan rasional) dan $S_3$ (himpunan bilangan pecahan diskret berhingga) keduanya bersifat terhitung (countable).</sub>
- B. $S_1$ dan $S_2$ saja  
  <sub>Salah: Siswa mengira bilangan rasional $\mathbb{Q}$ pada interval rapat membentuk variabel acak kontinu, padahal $\mathbb{Q}$ bersifat terhitung (countable).</sub>
- C. $S_2$ saja  
  <sub>Salah: Siswa mengabaikan bahwa gabungan interval real tak terputus seperti $S_4$ tetap bersifat tak terhitung (uncountable) dan memenuhi definisi variabel acak kontinu.</sub>
- D. $S_2$, $S_3$, dan $S_4$  
  <sub>Salah: Siswa terkecoh menganggap $S_3$ adalah kontinu karena memiliki 501 titik pecahan rapat.</sub>

**Pembahasan:** Definisi 4.3 menyatakan bahwa variabel acak kontinu memiliki ruang sampel yang tak terhitung (_uncountable_).
1. $S_1$: Himpunan bilangan rasional $\mathbb{Q}$ dalam interval $[0, 5]$ bersifat terhitung (_countable_), sehingga bukan kontinu.
2. $S_2$: Interval tertutup bilangan real $[0, 5]$ bersifat tak terhitung (_uncountable_), memenuhi syarat kontinu.
3. $S_3$: Himpunan berhingga dengan 501 elemen terhitung, merupakan variabel acak diskret.
4. $S_4$: Gabungan dua interval terbuka bilangan real $(1, 2) \cup (3, 4)$ tetap merupakan himpunan tak terhitung (_uncountable_), sehingga memenuhi syarat kontinu.
Jadi, model yang valid adalah $S_2$ dan $S_4$ saja.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b04-c-hard-bt01-006
*orisinal | C5 | 3 langkah | jenis: analisis densitas rentang*

Sebuah instrumen presisi mencatat waktu reaksi kimia $T$ (dalam detik) sebagai variabel acak kontinu pada interval $10,00 \le T \le 15,00$. Dalam dua kali percobaan berturut-turut, terukur waktu reaksi $t_1 = 12,450\text{ detik}$ dan $t_2 = 12,451\text{ detik}$. Seorang peneliti menyimpulkan bahwa tidak ada nilai waktu reaksi riil lain yang mungkin terjadi di antara kedua hasil pengukuran tersebut karena selisihnya sudah merupakan batas toleransi terkecil instrumen ($0,001\text{ detik}$). Evaluasi manakah yang paling tepat terhadap kesimpulan tersebut?

- A. Kesimpulan tersebut benar, asalkan kedua pengukuran dilakukan pada kondisi lingkungan laboratorium yang identik sempurna.  
  <sub>Salah: Siswa mengaitkan permasalahan sifat kontinum matematis dengan kondisi fisis eksperimen.</sub>
- **B. Kesimpulan tersebut salah, karena di antara dua nilai sembarang pada rentang variabel acak kontinu selalu terdapat tak hingga banyak nilai riil lain yang mungkin secara teoretis.** ✅  
  <sub>Benar: Sifat dasar variabel acak kontinu adalah nilainya membentuk rentang tak terputus pada bilangan real, sehingga di antara dua nilai sembarang selalu ada nilai bilangan real lainnya terlepas dari keterbatasan resolusi alat ukur.</sub>
- C. Kesimpulan tersebut salah, karena hanya terdapat tepat satu nilai riil di antara keduanya, yaitu nilai rata-ratanya $12,4505\text{ detik}$.  
  <sub>Salah: Siswa hanya memikirkan titik tengah (rata-rata) tanpa menyadari terdapat tak berhingga banyak titik bilangan real.</sub>
- D. Kesimpulan tersebut benar, karena selisih $0,001\text{ detik}$ sudah merupakan batas diskretisasi fisik sehingga ruang di antara keduanya hampa.  
  <sub>Salah: Siswa menyamakan batas resolusi pembacaan instrumen dengan sifat kontinum ruang sampel variabel acak.</sub>

**Pembahasan:** Berdasarkan ciri-ciri variabel acak kontinu pada Buku Siswa Matematika Tingkat Lanjut Kelas XII halaman 255, nilai variabel acak kontinu berupa bilangan real yang membentuk rentang tak terputus. Di antara dua nilai bilangan real berapa pun (bahkan yang berjarak sangat dekat seperti $12,450$ dan $12,451$), selalu terdapat tak hingga banyak bilangan real lainnya (misalnya $12,4501; 12,45025; \dots$). Keterbatasan instrumen pengukur tidak menghapus keberadaan nilai-nilai tersebut secara teoretis dalam ruang sampel. Jadi, kesimpulan peneliti tersebut salah.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b04-c-hard-bt01-007
*orisinal | C6 | 4 langkah | jenis: rancang representasi grafis*

Dua buah sensor suhu, Sensor A dan Sensor B, bekerja pada suatu bejana pemanas. Variabel acak $X$ menyatakan suhu yang terdeteksi oleh Sensor A dengan ruang sampel $S_A = \{x \in \mathbb{R} \mid 50,0 \le x \le 85,0\}$. Variabel acak $Y$ menyatakan suhu yang terdeteksi oleh Sensor B dengan ruang sampel $S_B = \{y \in \mathbb{R} \mid 70,0 < y \le 100,0\}$. Suatu sistem kendali otomatis hanya aktif jika kedua sensor mendeteksi suhu secara bersamaan dalam rentang kerja masing-masing (irisan dari kedua ruang sampel).

Bentuk representasi matematis dan visualisasi garis bilangan yang tepat untuk memodelkan rentang kerja sistem kendali otomatis tersebut adalah ....

- A. Ruang sampel $S = \{t \in \mathbb{R} \mid 70,0 \le t \le 85,0\}$, direpresentasikan sebagai ruas garis padat yang menghubungkan $70,0$ dan $85,0$ dengan kedua ujung berupa titik penuh.  
  <sub>Salah: Siswa tidak teliti pada batas terbuka di $70,0$ pada $S_B$ ($y > 70,0$).</sub>
- B. Ruang sampel $S = \{t \in \mathbb{R} \mid 70,0 < t < 85,0\}$, direpresentasikan sebagai ruas garis padat dengan kedua ujung berupa titik berlubang.  
  <sub>Salah: Siswa keliru menganggap batas atas $85,0$ juga bersifat terbuka.</sub>
- C. Ruang sampel $S = \{t \in \mathbb{R} \mid 50,0 \le t \le 100,0\}$, direpresentasikan sebagai ruas garis padat utuh dari $50,0$ hingga $100,0$.  
  <sub>Salah: Siswa melakukan operasi gabungan (union) alih-alih irisan (intersection).</sub>
- **D. Ruang sampel $S = \{t \in \mathbb{R} \mid 70,0 < t \le 85,0\}$, direpresentasikan sebagai ruas garis padat yang menghubungkan $70,0$ dan $85,0$ dengan titik berlubang di $70,0$ dan titik penuh di $85,0$.** ✅  
  <sub>Benar: Irisan dari $[50,0; 85,0]$ dan $(70,0; 100,0]$ adalah $(70,0; 85,0]$. Pada garis bilangan, pertidaksamaan tegas ($>$) digambarkan dengan bulatan berlubang, sedangkan pertidaksamaan non-tegas ($\le$) digambarkan dengan bulatan penuh.</sub>

**Pembahasan:** Langkah 1: Menentukan daerah kerja bersama (irisan) dari kedua rentang variabel acak kontinu:
$S = S_A \cap S_B = [50,0; 85,0] \cap (70,0; 100,0] = (70,0; 85,0]$.
Langkah 2: Notasi himpunannya adalah $S = \{t \in \mathbb{R} \mid 70,0 < t \le 85,0\}$.
Langkah 3: Karakteristik variabel acak kontinu direpresentasikan berupa deretan titik yang terhubung membentuk garis pada garis bilangan.
Langkah 4: Karena $t > 70,0$, titik di $70,0$ tidak termasuk dalam daerah (digambarkan sebagai bulatan kosong/berlubang). Karena $t \le 85,0$, titik di $85,0$ termasuk dalam daerah (digambarkan sebagai bulatan padat/penuh).
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b04-c-hard-bt01-008
*orisinal | C5 | 3 langkah | jenis: evaluasi klasifikasi variabel*

Dua orang siswa memperdebatkan klasifikasi dua variabel acak berikut:
- Variabel $P$: Tekanan hidrostatis di dasar tangki penampungan minyak (dalam kilopascal).
- Variabel $Q$: Banyaknya tetesan minyak yang keluar per menit dari keran pengeluaran tangki.

Siswa 1 menyatakan: "Variabel $P$ dan $Q$ keduanya adalah variabel acak kontinu karena keduanya berkaitan dengan zat cair dan nilainya sama-sama diperoleh dari pengamatan di laboratorium."
Siswa 2 menyatakan: "Variabel $P$ adalah variabel acak kontinu karena nilainya merupakan hasil pengukuran yang membentuk rentang tak terputus, sedangkan $Q$ adalah variabel acak diskret karena nilainya diperoleh melalui pencacahan (counting) dan berupa bilangan bulat nonnegatif."

Manakah evaluasi yang paling tepat mengenai perdebatan kedua siswa tersebut?

- A. Pernyataan Siswa 1 benar, karena seluruh fenomena fisis fluida menghasilkan variabel acak kontinu.  
  <sub>Salah: Siswa salah berasumsi bahwa sifat fisik zat (cair) otomatis menentukan tipe variabel acak.</sub>
- B. Pernyataan Siswa 2 salah, karena variabel $Q$ dapat dinyatakan dalam laju desimal tetesan per detik sehingga tergolong kontinu.  
  <sub>Salah: Siswa mengabaikan definisi variabel $Q$ sebagai 'banyaknya tetesan' yang selalu berupa bilangan bulat cacah.</sub>
- C. Kedua siswa salah, karena variabel $P$ adalah variabel acak diskret mengingat alat ukur tekanan memiliki jarum penunjuk dengan skala bertingkat tertentu.  
  <sub>Salah: Siswa tertukar antara sifat keterbatasan skala instrumen dengan sifat variabel acak teoretis.</sub>
- **D. Pernyataan Siswa 2 benar, sedangkan pernyataan Siswa 1 salah karena klasifikasi variabel acak didasarkan pada sifat keterhitungan ruang sampel dan cara perolehannya, bukan pada wujud fisik materi yang diamati.** ✅  
  <sub>Benar: Tekanan hidrostatis $P$ diperoleh melalui proses pengukuran dengan nilai bilangan real kontinu tak terhitung (uncountable). Banyaknya tetesan $Q$ diperoleh melalui proses membilang/mencacah satu per satu sehingga merupakan variabel acak diskret terhitung (countable).</sub>

**Pembahasan:** Berdasarkan materi Buku Siswa halaman 254-255:
1. Variabel acak kontinu diperoleh dari proses pengukuran (seperti tekanan, waktu, suhu, tinggi badan) dan nilainya mencakup rentang tak terputus bilangan real yang tak dapat dihitung satu per satu (_uncountable_). Dengan demikian, variabel $P$ (tekanan hidrostatis) adalah variabel acak kontinu.
2. Variabel acak diskret diperoleh dari proses membilang atau mencacah (_counting_) dan nilainya berupa bilangan bulat terpisah yang dapat dihitung satu per satu. Dengan demikian, variabel $Q$ (banyaknya tetesan) adalah variabel acak diskret.
Oleh karena itu, pernyataan Siswa 2 sepenuhnya benar dan pernyataan Siswa 1 salah.
**Acuan:** siswa — siswa hal.254

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b04-c-hard-bt01-009
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi ruang sampel*

Debit aliran fluida $Q$ (dalam liter/detik) yang keluar dari suatu pipa venturi berfluktuasi secara acak pada rentang $14,5\text{ L/s}$ hingga $18,2\text{ L/s}$. Empat orang siswa mengusulkan penulisan ruang sampel $S$ untuk variabel acak kontinu $Q$ tersebut sebagai berikut:

1. $S_1 = \{14,5;\ 14,6;\ 14,7;\ \dots;\ 18,2\}$
2. $S_2 = \{q \in \mathbb{Q} \mid 14,5 \le q \le 18,2\}$
3. $S_3 = \{q \in \mathbb{R} \mid 14,5 \le q \le 18,2\}$
4. $S_4 = \{q \in \mathbb{Z} \mid 15 \le q \le 18\}$

Berdasarkan definisi variabel acak kontinu, usulan notasi ruang sampel yang tepat secara matematis adalah ....

- A. $S_1$ dan $S_3$  
  <sub>Salah: Mengira $S_1$ mewakili interval kontinu padahal $S_1$ merupakan himpunan terhitung dengan langkah desimal diskret.</sub>
- B. $S_2$ dan $S_3$  
  <sub>Salah: Mengira himpunan bilangan rasional $\mathbb{Q}$ mencakup seluruh titik pada rentang kontinu padahal bilangan irasional terabaikan.</sub>
- **C. $S_3$ saja** ✅  
  <sub>Benar: Ruang sampel variabel acak kontinu memuat seluruh bilangan real dalam rentang tak terputus, sehingga harus didefinisikan pada himpunan bilangan real $\mathbb{R}$.</sub>
- D. $S_2$ saja  
  <sub>Salah: Tertukar antara definisi bilangan rasional $\mathbb{Q}$ dan bilangan real $\mathbb{R}$ untuk ruang sampel kontinu.</sub>

**Pembahasan:** Debit fluida merupakan besaran kontinu yang nilainya berupa bilangan real tak terputus dalam rentang yang ditentukan. Ruang sampel kontinu mencakup semua bilangan real (baik rasional maupun irasional) dalam rentang $[14,5;\ 18,2]$. Notasi $S_1$ merupakan himpunan diskret terhitung, $S_2$ hanya memuat bilangan rasional (ada lubang pada bilangan irasional), dan $S_4$ adalah himpunan bilangan bulat. Oleh karena itu, hanya $S_3 = \{q \in \mathbb{R} \mid 14,5 \le q \le 18,2\}$ yang tepat.
**Acuan:** pretest — kelas12_tl-b04-p0257-latihan-soal-variabel-acak-kontinu-b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b04-c-hard-bt01-010
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi model matematis*

Sebuah eksperimen mengukur konsentrasi larutan garam $C$ (dalam g/L) yang berada pada rentang $22,4\text{ g/L}$ hingga $27,8\text{ g/L}$. Seorang peneliti menyatakan bahwa ruang sampel variabel acak $C$ dapat dituliskan sebagai interval tertutup $[22,4;\ 27,8]$ pada garis bilangan real $\mathbb{R}$. Asisten peneliti mengajukan kritik bahwa jika alat ukur hanya menampilkan 2 angka desimal, maka model interval kontinu tersebut keliru dan harus diganti menjadi himpunan bilangan desimal dua angka di belakang koma. Bagaimana evaluasi yang benar terhadap kritik asisten tersebut?

- **A. Kritik asisten keliru, karena keterbatasan resolusi alat ukur tidak mengubah sifat variabel acak konsentrasi yang secara alami bernilai kontinu pada rentang real.** ✅  
  <sub>Benar: Keterbatasan presisi alat ukur merupakan pencatatan teknis, sedangkan nilai teoritis variabel acak kontinu tetap mencakup seluruh bilangan real pada interval tersebut.</sub>
- B. Kritik asisten benar, karena ruang sampel suatu variabel acak harus selalu disesuaikan dengan angka desimal yang mampu ditampilkan oleh alat ukur.  
  <sub>Salah: Menyamakan keterbatasan resolusi pembacaan instrumen dengan ruang sampel teoretis variabel acak.</sub>
- C. Kritik asisten benar, karena variabel acak berubah menjadi variabel acak diskret begitu nilainya dicatat oleh instrumen digital.  
  <sub>Salah: Keliru menganggap proses diskretisasi alat ukur mengubah sifat bawaan variabel acak fisis dari kontinu menjadi diskret.</sub>
- D. Kritik asisten keliru, karena interval $[22,4;\ 27,8]$ pada garis bilangan real sebenarnya hanya terdiri dari bilangan desimal berhingga.  
  <sub>Salah: Salah memahami konsep bilangan real, mengira interval real hanya memuat desimal berhingga.</sub>

**Pembahasan:** Variabel acak kontinu didefinisikan berdasarkan karakteristik besaran yang diukur, yang dapat bernilai sembarang bilangan real pada interval tak terputus. Resolusi alat ukur yang terbatas pada dua angka desimal hanyalah aproksimasi teknis dari proses pengukuran. Nilai sejati dari konsentrasi larutan tersebut tetap berada pada interval kontinu $[22,4;\ 27,8]$ pada $\mathbb{R}$. Dengan demikian, kritik asisten keliru.
**Acuan:** siswa — siswa hal.256 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b04-c-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: evaluasi sifat kerapatan*

Sebuah termometer inframerah mendeteksi suhu permukaan pipa uap $T$ pada interval $105,0^\circ\text{C} \le T \le 115,0^\circ\text{C}$. Dua orang teknisi berdiskusi mengenai nilai-nilai suhu yang mungkin terjadi:

- Teknisi A berpendapat bahwa di antara nilai suhu $108,25^\circ\text{C}$ dan $108,26^\circ\text{C}$ tidak mungkin ada nilai suhu lain karena selisihnya sudah mencapai batas ketelitian $0,01^\circ\text{C}$.
- Teknisi B berpendapat bahwa secara teoretis selalu terdapat tak berhingga banyaknya kemungkinan nilai suhu di antara $108,25^\circ\text{C}$ dan $108,26^\circ\text{C}$.

Berdasarkan karakteristik variabel acak kontinu, manakah simpulan yang tepat mengenai pendapat kedua teknisi?

- A. Teknisi A benar, karena nilai suhu hanya diakui jika sesuai dengan nilai pembacaan alat ukur.  
  <sub>Salah: Membatasi ruang nilai variabel kontinu hanya pada skala terbaca oleh alat ukur.</sub>
- B. Teknisi A benar, karena selisih $0,01^\circ\text{C}$ merupakan jarak terkecil antar-bilangan real pada skala pengukuran suhu.  
  <sub>Salah: Keliru mengira bilangan real memiliki jarak minimum atau selisih diskret terkecil.</sub>
- **C. Teknisi B benar, karena variabel acak kontinu membentuk rentang tak terputus sehingga di antara dua nilai sembarang selalu terdapat nilai real lainnya.** ✅  
  <sub>Benar: Karakteristik variabel acak kontinu adalah nilainya berada pada himpunan bilangan real yang padat (rentang tak terputus), sehingga di antara dua nilai real selalu ada tak berhingga nilai real lainnya.</sub>
- D. Teknisi B benar, karena di antara dua nilai tersebut hanya ada tepat satu nilai tengah yaitu $108,255^\circ\text{C}$.  
  <sub>Salah: Mengira hanya ada satu nilai tengah, mengabaikan bahwa ada tak berhingga banyak bilangan real di antara dua nilai.</sub>

**Pembahasan:** Karakteristik utama variabel acak kontinu adalah nilainya berupa bilangan real yang membentuk rentang tak terputus. Akibat sifat kerapatan bilangan real, di antara dua nilai sembarang (seperti $108,25^\circ\text{C}$ dan $108,26^\circ\text{C}$), selalu terdapat tak berhingga banyak nilai real lain yang mungkin muncul (misalnya $108,251^\circ\text{C}$, $108,2543^\circ\text{C}$, dan seterusnya). Keterbatasan alat ukur tidak meniadakan keberadaan nilai-nilai tersebut secara teoretis. Maka pendapat Teknisi B benar.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b04-c-hard-bt01-012
*orisinal | C6 | 5 langkah | jenis: analisis himpunan nilai*

Seorang mahasiswa merancang empat model himpunan nilai $R$ untuk mendeskripsikan hasil suatu pengukuran:

1. $R_1 = \{x \in \mathbb{R} \mid 5 < x < 9\}$
2. $R_2 = \{x \in \mathbb{Q} \mid 5 \le x \le 9\}$
3. $R_3 = \{5 + 0,1k \mid k \in \mathbb{N}\text{ dan } 0 \le k \le 40\}$
4. $R_4 = [5, 9] \setminus \{7\}$ dengan domain semesta $\mathbb{R}$

Berdasarkan Definisi 4.3 bahwa variabel acak kontinu memiliki ruang nilai tak terhitung (*uncountable*), model himpunan nilai yang memenuhi kriteria variabel acak kontinu adalah ....

- A. $R_1$ saja  
  <sub>Salah: Mengira pengurangan satu titik pada $R_4$ merusak sifat tak terhitung pada interval real.</sub>
- **B. $R_1$ dan $R_4$ saja** ✅  
  <sub>Benar: Himpunan $R_1$ (interval buka bilangan real) dan $R_4$ (interval real yang dihilangkan satu titik) bersifat tak terhitung (uncountable), sedangkan himpunan bilangan rasional $R_2$ dan himpunan berhingga $R_3$ bersifat terhitung (countable).</sub>
- C. $R_1$ dan $R_2$ saja  
  <sub>Salah: Mengira $R_2$ kontinu dan menganggap $R_4$ bukan interval kontinu karena terputus di satu titik.</sub>
- D. $R_1$, $R_2$, dan $R_4$  
  <sub>Salah: Mengira himpunan bilangan rasional $R_2$ bersifat tak terhitung karena tak berhingga banyaknya, padahal $\mathbb{Q}$ terhitung (countable).</sub>

**Pembahasan:** Menurut Definisi 4.3, variabel acak kontinu memiliki ruang sampel tak terhitung (*uncountable*).
- $R_1 = (5, 9) \subset \mathbb{R}$ merupakan interval kontinu pada bilangan real, sehingga bersifat tak berhingga dan tak terhitung (*uncountable*).
- $R_2 \subset \mathbb{Q}$ adalah himpunan bilangan rasional. Himpunan bilangan rasional bersifat terhitung (*countable*), sehingga bukan kontinu.
- $R_3$ adalah himpunan berhingga dengan 41 anggota, sehingga terhitung (*countable*).
- $R_4 = [5, 9] \setminus \{7\}$ terdiri dari gabungan dua interval $[5, 7) \cup (7, 9]$ pada $\mathbb{R}$, yang keduanya tak terhitung (*uncountable*).
Jadi, model yang memenuhi adalah $R_1$ dan $R_4$ saja.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b04-c-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim pengukuran*

Perhatikan argumen berikut mengenai klasifikasi variabel acak:
"Sebuah timbangan digital di laboratorium analitik memiliki tampilan dengan presisi hingga $0,0001\text{ gram}$. Karena angka pembacaannya selalu melompat dengan selisih kelipatan $0,0001\text{ gram}$ dan tidak dapat menampilkan angka di antaranya, maka massa zat kimia yang ditimbang dengan alat tersebut pada dasarnya merupakan variabel acak diskret, bukan kontinu."

Evaluasi yang paling tepat terhadap argumen di atas adalah ....

- A. Argumen salah, karena timbangan analitik tidak pernah menghasilkan bilangan desimal berulang.  
  <sub>Salah: Memberikan alasan yang keliru tentang sifat bilangan desimal berulang pada timbangan.</sub>
- B. Argumen benar, asalkan massa zat kimia yang ditimbang tidak melebihi kapasitas maksimum timbangan.  
  <sub>Salah: Memasukkan syarat kapasitas alat yang tidak relevan dengan sifat diskret atau kontinu.</sub>
- C. Argumen benar, karena variabel acak hanya dapat didefinisikan secara operasional dari angka-angka riil yang dihasilkan oleh alat ukur.  
  <sub>Salah: Menyamakan definisi teoretis variabel acak dengan nilai kuantisasi keluaran sensor alat ukur.</sub>
- **D. Argumen salah, karena sifat kontinu ditentukan oleh besaran fisis massa yang dapat bernilai sembarang bilangan real tak terputus, bukan oleh keterbatasan pembacaan digit alat ukur.** ✅  
  <sub>Benar: Massa adalah variabel acak kontinu secara alami; diskretisasi nilai terjadi semata-mata karena keterbatasan tampilan alat ukur digital.</sub>

**Pembahasan:** Massa merupakan hasil proses pengukuran yang secara teoretis mencakup semua bilangan real pada rentang tertentu dan bersifat tak terhitung (*uncountable*). Adanya resolusi minimum seperti $0,0001\text{ gram}$ pada timbangan digital merupakan batasan teknologi instrumen (kuantisasi alat), bukan sifat esensial dari variabel acak massa itu sendiri. Oleh karena itu, variabel acak massa tetap merupakan variabel acak kontinu dan argumen tersebut salah.
**Acuan:** siswa — siswa hal.254

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b04-c-hard-bt01-014
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi model ruang sampel*

Sebuah eksperimen mengamati waktu pengeringan lapisan cat pelindung pipa minyak, $T$ (dalam jam), yang bervariasi pada selang 4,2 jam hingga 8,6 jam. Empat peneliti merumuskan model ruang sampel $S$ untuk variabel acak $T$ sebagai berikut:

1. $S_1 = \{t \in \mathbb{Q} \mid 4,2 \le t \le 8,6\}$
2. $S_2 = \{t \in \mathbb{R} \mid 4,2 < t < 8,6\}$
3. $S_3 = \{t \in \mathbb{R} \mid 4,2 \le t \le 8,6\}$
4. $S_4 = \{4,2;\ 4,3;\ 4,4;\ \dots;\ 8,6\}$

Berdasarkan hakikat variabel acak kontinu yang merepresentasikan seluruh kemungkinan nilai waktu pengeringan pada selang tersebut, model ruang sampel yang tepat secara matematis adalah ....

- **A. $S_3$ saja** ✅  
  <sub>Benar: Variabel acak kontinu memuat seluruh bilangan real pada interval tertutup yang ditentukan, bukan hanya rasional atau diskret berjarak tertentu.</sub>
- B. $S_1$ dan $S_3$  
  <sub>Salah: Mengira bilangan rasional cukup untuk mendefinisikan variabel acak kontinu.</sub>
- C. $S_2$ dan $S_3$  
  <sub>Salah: Mengabaikan batas interval tertutup [4,2; 8,6] yang mencakup kedua ujungnya.</sub>
- D. $S_3$ dan $S_4$  
  <sub>Salah: Terkecoh dengan pembulatan satu desimal pada $S_4$ seolah mewakili seluruh ruang sampel.</sub>

**Pembahasan:** Variabel acak kontinu didefinisikan pada ruang sampel kontinu yang mencakup seluruh bilangan real pada rentang tersebut tanpa terputus. Karena rentang waktu pengeringan mencakup nilai dari 4,2 jam hingga 8,6 jam secara inklusif, model yang benar adalah interval tertutup pada bilangan real: $S_3 = \{t \in \mathbb{R} \mid 4,2 \le t \le 8,6\}$. Pilihan $S_1$ salah karena hanya memuat bilangan rasional (terputus pada bilangan irasional), $S_2$ salah karena tidak memuat batas ujungnya, dan $S_4$ salah karena merupakan himpunan diskret terhitung.
**Acuan:** siswa — siswa hal.256 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b04-c-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: evaluasi representasi grafis*

Dua orang analis memperdebatkan representasi grafis himpunan nilai dari dua variabel acak pada garis bilangan:
- Analis 1: "Variabel acak $X$ menyatakan massa serbuk kimia dalam rentang $3\text{ gram} \le X \le 7\text{ gram}$. Jika direpresentasikan pada garis bilangan, grafiknya berupa deretan titik-titik terpisah yang sangat rapat dan berhingga banyaknya."
- Analis 2: "Variabel acak $Y$ menyatakan jumlah gelembung udara dalam cairan reaksi ($0 \le Y \le 50$). Jika direpresentasikan pada garis bilangan, grafiknya berupa ruas garis padat tak terputus dari angka 0 hingga 50."

Evaluasi yang benar mengenai pernyataan kedua analis tersebut adalah ....

- **A. Kedua analis salah dalam mengidentifikasi bentuk representasi grafis masing-masing variabel** ✅  
  <sub>Benar: Analis 1 salah karena variabel kontinu berupa garis padat tak terputus, sedangkan Analis 2 salah karena variabel diskret berupa titik-titik terpisah.</sub>
- B. Kedua analis memberikan pernyataan yang benar sesuai prinsip garis bilangan  
  <sub>Salah: Tertukar konsep representasi antara variabel acak kontinu dan variabel acak diskret.</sub>
- C. Pernyataan Analis 2 benar, sedangkan Analis 1 salah  
  <sub>Salah: Mengira variabel diskret dengan rentang nilai berhingga dapat digambar sebagai garis padat tak terputus.</sub>
- D. Pernyataan Analis 1 benar, sedangkan Analis 2 salah  
  <sub>Salah: Mengira variabel kontinu diwakili oleh titik-titik terpisah yang sangat rapat.</sub>

**Pembahasan:** Massa serbuk kimia $X$ merupakan variabel acak kontinu yang nilainya membentuk rentang tak terputus pada bilangan real, sehingga pada garis bilangan harus direpresentasikan sebagai ruas garis padat tak terputus, bukan deretan titik terpisah. Sebaliknya, jumlah gelembung udara $Y$ merupakan variabel acak diskret (hasil pembilangan), sehingga representasinya pada garis bilangan adalah titik-titik terpisah yang berhingga, bukan garis tak terputus. Jadi, kedua analis salah.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b04-c-hard-bt01-016
*orisinal | C6 | 5 langkah | jenis: analisis struktur kardinalitas*

Perhatikan empat definisi himpunan hasil kemungkinan nilai variabel acak berikut:

1. $H_1 = \{x \in \mathbb{Z} \mid x > 0\}$
2. $H_2 = \{x \in \mathbb{Q} \mid 0 \le x \le 1\}$
3. $H_3 = \{x \in \mathbb{R} \mid 5 < x < 6\}$
4. $H_4 = \{x \in \mathbb{R} \mid x = 2k + 1,\ k \in \mathbb{N}\}$

Berdasarkan Definisi 4.3 pada materi variabel acak kontinu, himpunan yang memenuhi syarat sebagai ruang sampel dari suatu variabel acak kontinu karena beranggotakan himpunan yang tak terhitung (*uncountable*) adalah ....

- A. $H_1, H_2,$ dan $H_3$  
  <sub>Salah: Menyamakan konsep tak hingga (*infinite*) dengan tak terhitung (*uncountable*).</sub>
- **B. $H_3$ saja** ✅  
  <sub>Benar: $H_3$ merupakan interval bilangan real yang tak terhitung, sedangkan $H_1, H_2,$ dan $H_4$ adalah himpunan terhitung.</sub>
- C. $H_2$ dan $H_3$  
  <sub>Salah: Menganggap himpunan bilangan rasional pada interval padat berifat tak terhitung (*uncountable*).</sub>
- D. $H_3$ dan $H_4$  
  <sub>Salah: Terkecoh oleh simbol bilangan real pada $H_4$ padahal indeks variabelnya bilangan asli terhitung.</sub>

**Pembahasan:** Berdasarkan Definisi 4.3, variabel acak kontinu memiliki ruang sampel yang tak terhitung (*uncountable*). Suatu himpunan tak hingga dapat bersifat terhitung (*countable*) atau tak terhitung (*uncountable*). Himpunan $H_1$ (bilangan bulat positif) dan $H_4$ (bilangan ganjil positif) dapat dipasangkan satu-satu dengan $\mathbb{N}$ sehingga terhitung. Himpunan $H_2$ (bilangan rasional) juga terhitung (*countable*). Hanya himpunan $H_3 = \{x \in \mathbb{R} \mid 5 < x < 6\}$ (interval kontinu bilangan real) yang bersifat tak terhitung (*uncountable*). Oleh karena itu, hanya $H_3$ yang memenuhi syarat sebagai ruang sampel kontinu.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b04-c-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: evaluasi kesimpulan eksperimen*

Dalam suatu uji coba aerodinamika, kecepatan aliran udara $V$ (dalam m/s) pada permukaan sayap pesawat berfluktuasi secara kontinu pada selang $65,0 \le V \le 72,0$. Sebuah sensor kecepatan berkecepatan tinggi mencatat dua data berturut-turut pada saat uji coba, yaitu $68,421\text{ m/s}$ dan $68,422\text{ m/s}$. Seorang teknisi menyimpulkan:
"Karena selisih kedua data tersebut sangat kecil ($0,001\text{ m/s}$), tidak ada lagi nilai kecepatan fisik aliran udara yang mungkin terjadi di antara kedua angka tersebut."

Penilaian yang paling tepat terhadap kesimpulan teknisi tersebut adalah ....

- A. Salah, karena di antara kedua angka tersebut tepat hanya ada sembilan nilai baru jika resolusi ditambah satu desimal  
  <sub>Salah: Memandang pembagian desimal hanya sebatas satu tingkat desimal berikutnya, bukan kepadatan kontinu.</sub>
- **B. Salah, karena sifat bilangan real pada variabel acak kontinu menjamin adanya tak hingga banyak kemungkinan nilai lain di antara dua nilai sembarang** ✅  
  <sub>Benar: Rentang tak terputus variabel acak kontinu berarti di antara dua bilangan real sembarang selalu terdapat tak hingga nilai real lain.</sub>
- C. Benar, karena aliran fluida yang kontinu selalu berubah secara melompat pada skala mikroskopis  
  <sub>Salah: Menyatakan premis keliru bahwa kontinu berarti melompat pada skala kecil.</sub>
- D. Benar, karena selisih $0,001\text{ m/s}$ sudah merupakan batas keterbagian terkecil dalam mekanika fluida  
  <sub>Salah: Mencampurkan keterbatasan resolusi alat pencatat dengan konsep kontinu teoritis matematis.</sub>

**Pembahasan:** Ciri utama variabel acak kontinu adalah nilainya berupa bilangan real yang membentuk rentang tak terputus. Sesuai sifat kerapatan bilangan real, di antara dua nilai sembarang (seperti $68,421$ dan $68,422$) selalu terdapat tak hingga banyak nilai bilangan real lain (misalnya $68,4215$; $68,42107$; dst.). Kesimpulan teknisi salah karena keterbatasan angka yang tercatat merupakan akibat resolusi alat, sedangkan secara matematis variabel kontinu memiliki tak hingga banyak kemungkinan nilai di antara dua titik.
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b04-c-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim klasifikasi*

Perhatikan argumen berikut:
"Variabel acak $W$ menyatakan waktu tunggu transaksi di mesin ATM (dalam detik). Jika pencatatan dilakukan dengan membulatkan nilai waktu ke detik bulat terdekat (misalnya 15 detik, 16 detik, 17 detik), maka variabel acak waktu tunggu tersebut otomatis berubah status hakikinya menjadi variabel acak diskret."

Evaluasi yang tepat terhadap argumen di atas adalah ....

- A. Argumen tidak tepat, karena semua variabel acak waktu selalu bertipe diskret apa pun alat ukurnya  
  <sub>Salah: Keliru menganggap waktu adalah variabel acak diskret.</sub>
- **B. Argumen tidak tepat, karena pembulatan atau batasan instrumen pengukuran tidak mengubah sifat intrinsik waktu tunggu sebagai variabel acak kontinu yang bernilai pada ruang kontinu** ✅  
  <sub>Benar: Klasifikasi variabel acak kontinu ditentukan oleh sifat dasar besaran fisis teoritisnya (hasil pengukuran pada rentang bilangan real), bukan keterbatasan cara manusia mencatatnya.</sub>
- C. Argumen tepat, karena data yang dihasilkan berupa bilangan bulat yang dapat dihitung satu per satu sehingga memenuhi syarat variabel diskret  
  <sub>Salah: Mengacaukan data hasil diskretisasi praktis dengan sifat dasar variabel acak itu sendiri.</sub>
- D. Argumen tepat, asalkan rentang waktu tunggu bernilai positif dan tidak melebihi 60 detik  
  <sub>Salah: Menjadikan batas interval berhingga sebagai pembenaran perubahan status variabel kontinu ke diskret.</sub>

**Pembahasan:** Variabel acak kontinu diperoleh dari proses pengukuran terhadap besaran kontinu (seperti waktu, panjang, atau massa) yang pada hakikatnya dapat mengambil nilai sembarang bilangan real pada suatu interval. Tindakan membulatkan angka pencatatan ke bilangan bulat terdekat hanyalah proses pembatasan presisi atau diskretisasi pencatatan teknis, bukan mengubah hakikat besaran waktu itu sendiri. Jadi, argumen tersebut tidak tepat.
**Acuan:** siswa — siswa hal.254

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b04-c-hard-bt01-019
*variasi (konteks) | C5 | 3 langkah | jenis: evaluasi karakteristik variabel*

Sebuah tungku induksi pabrik diatur untuk memanaskan cairan baja pada suhu target $1.500^\circ\text{C}$. Karena kestabilan tegangan listrik yang tidak selalu konstan, suhu cairan baja yang dihasilkan berfluktuasi dari $1.485^\circ\text{C}$ hingga $1.515^\circ\text{C}$. Misalkan $T$ menyatakan suhu cairan baja yang dihasilkan oleh tungku tersebut. Apakah $T$ memenuhi kriteria sebagai variabel acak kontinu? Evaluasilah simpulan dan alasan teoritis berikut yang paling tepat.

- A. $T$ bukan variabel acak kontinu karena suhunya berfluktuasi di sekitar nilai acuan $1.500^\circ\text{C}$ dengan simpangan tetap sebesar $15^\circ\text{C}$  
  <sub>Salah: Mengira fluktuasi simetris di sekitar nilai target mengubah sifat kontinu menjadi diskret berjarak tetap.</sub>
- B. $T$ bukan variabel acak kontinu karena batas suhu terendah dan tertingginya telah dipatok secara pasti berupa bilangan bulat  
  <sub>Salah: Keliru menganggap bahwa interval dengan batas bilangan bulat membuat seluruh anggotanya menjadi bilangan bulat.</sub>
- **C. $T$ merupakan variabel acak kontinu karena nilainya diperoleh melalui proses pengukuran dan ruang nilainya mencakup semua bilangan real dalam rentang $[1.485, 1.515]$ sehingga tak terhitung banyaknya** ✅  
  <sub>Benar: Suhu diperoleh melalui pengukuran dan memuat interval kontinu bilangan real tak terhitung (uncountable) di antara 1.485 dan 1.515.</sub>
- D. $T$ merupakan variabel acak kontinu hanya jika nilai suhu yang terukur dicatat dengan pembulatan ke derajat terdekat tanpa angka desimal  
  <sub>Salah: Terbalik memahami konsep; pembulatan ke satuan terdekat justru mendiskretkan hasil pencatatan instrumen.</sub>

**Pembahasan:** Berdasarkan Definisi 4.3 dan ciri-ciri variabel acak kontinu:
1. Suhu merupakan besaran fisis yang diperoleh melalui pengukuran.
2. Suhu lelehan baja berfluktuasi pada interval tertutup $[1.485, 1.515]$. Di antara dua nilai suhu sembarang pada interval tersebut selalu ada nilai suhu lain yang tak terhingga banyaknya dalam bilangan real.
3. Karena ruang sampelnya memuat seluruh bilangan real dalam rentang tersebut, nilainya tak terhitung banyaknya (*uncountable*). Dengan demikian, $T$ adalah variabel acak kontinu.
**Acuan:** siswa — siswa hal.255 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12_tl-b04-c-hard-bt01-020
*orisinal | C5 | 4 langkah | jenis: evaluasi validitas definisi*

Perhatikan empat pernyataan evaluatif mengenai konsep ruang sampel dan variabel acak kontinu berikut:
(1) Setiap variabel acak yang memiliki ruang sampel berupa himpunan tak berhingga pasti tergolong sebagai variabel acak kontinu.
(2) Ruang sampel kontinu dicirikan oleh himpunan nilai yang tak terhitung banyaknya (*uncountable*) yang membentuk rentang tak terputus pada bilangan real.
(3) Suatu variabel acak yang nilainya diperoleh dari proses mencacah objek berulang tanpa batas waktu tergolong sebagai variabel acak kontinu.
(4) Di antara dua nilai sembarang pada rentang variabel acak kontinu selalu dapat ditemukan kemungkinan nilai lain yang termasuk dalam variabel tersebut.

Pernyataan yang bernilai benar berdasarkan konsep teoretis variabel acak kontinu adalah ....

- A. (1) dan (2)  
  <sub>Salah: Mengabaikan fakta bahwa himpunan tak berhingga pada variabel diskret (seperti bilangan asli) bersifat terhitung (countable).</sub>
- B. (3) dan (4)  
  <sub>Salah: Salah mengklasifikasikan proses mencacah/menghitung objek sebagai variabel kontinu padahal itu adalah variabel diskret.</sub>
- **C. (2) dan (4)** ✅  
  <sub>Benar: Pernyataan (2) sesuai Definisi 4.3 (uncountable) dan pernyataan (4) sesuai ciri kerapatan/rentang tak terputus.</sub>
- D. (1) dan (3)  
  <sub>Salah: Keliru mengidentifikasi himpunan tak berhingga terhitung (countably infinite dari proses cacah) sebagai variabel kontinu.</sub>

**Pembahasan:** Evaluasi setiap pernyataan:
- Pernyataan (1) SALAH: Ruang sampel tak berhingga dapat berupa tak berhingga terhitung (*countably infinite*, misalnya himpunan bilangan bulat positif $\{1, 2, 3, \dots\}$), yang merupakan variabel acak diskret.
- Pernyataan (2) BENAR: Menurut Definisi 4.3 pada Buku Siswa, variabel acak kontinu memiliki ruang sampel yang tak terhitung (*uncountable*) dan membentuk selang kontinu bilangan real.
- Pernyataan (3) SALAH: Proses mencacah menghasilkan data hitungan (*countable*), sehingga merupakan variabel acak diskret, bukan kontinu.
- Pernyataan (4) BENAR: Sesuai ciri-ciri variabel acak kontinu, nilainya membentuk rentang tak terputus sehingga di antara dua nilai selalu terdapat nilai lain di dalamnya.

Jadi, pernyataan yang benar adalah (2) dan (4).
**Acuan:** siswa — siswa hal.255

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
