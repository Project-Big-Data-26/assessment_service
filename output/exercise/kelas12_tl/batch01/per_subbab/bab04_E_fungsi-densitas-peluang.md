# Lembar koreksi — kelas12_tl SMA12L-B4 subbab E: Fungsi Densitas Peluang

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b04-e-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: peluang interval fungsi konstan*

Dalam masa pembatasan kunjungan, suatu galeri seni hanya beroperasi selama 300 menit, yaitu mulai pukul 10.00 hingga pukul 15.00. Pengunjung tidak diperbolehkan berada di dalam galeri sebelum pukul 10.00 dan harus meninggalkan galeri paling lambat pukul 15.00. Misalkan $X$ adalah variabel acak yang menyatakan lama pengunjung berada di dalam galeri (dalam menit). Fungsi densitas peluang $X$ dinyatakan dengan $f(x)=\begin{cases}\frac{1}{300}, & 0 \le x \le 300\\ 0, & x<0 \text{ atau } x>300\end{cases}$. Peluang seorang pengunjung berada di dalam galeri pada rentang waktu antara 60 dan 120 menit adalah ....

- A. $\frac{1}{3}$  
  <sub>Salah: Menggunakan jawaban acuan tanpa menghitung ulang dengan angka baru.</sub>
- **B. $\frac{1}{5}$** ✅  
  <sub>Benar: $P(60 \le X \le 120) = \int_{60}^{120} \frac{1}{300}\,dx = \frac{120 - 60}{300} = \frac{60}{300} = \frac{1}{5}$.</sub>
- C. $\frac{1}{10}$  
  <sub>Salah: Salah membagi selisih 60 dengan total rentang 600 menit.</sub>
- D. $\frac{2}{5}$  
  <sub>Salah: Menggunakan batas atas 120 dibagi 300 tanpa mengurangkan batas bawah.</sub>

**Pembahasan:** Peluang variabel acak kontinu pada selang $60 \le X \le 120$ dihitung dengan integral fungsi densitasnya:
$$P(60 \le X \le 120) = \int_{60}^{120} \frac{1}{300}\,dx = \frac{120 - 60}{300} = \frac{60}{300} = \frac{1}{5}$$
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b04-e-easy-bt01-002
*variasi (konteks) | C2 | 1 langkah | jenis: peluang interval variabel kontinu*

Waktu pengisian daya baterai sebuah perangkat hingga penuh dinyatakan sebagai variabel acak kontinu $T$ (dalam menit) dengan fungsi densitas peluang:
$$f(t)=\begin{cases}\frac{1}{80}, & 0 \le t \le 80\\ 0, & \text{untuk } t \text{ lainnya}\end{cases}$$
Peluang pengisian daya berlangsung dalam rentang waktu antara 20 dan 60 menit adalah ....

- **A. $\frac{1}{2}$** ✅  
  <sub>Benar: $P(20 \le T \le 60) = (60 - 20) \times \frac{1}{80} = \frac{40}{80} = \frac{1}{2}$.</sub>
- B. $\frac{3}{4}$  
  <sub>Salah: Menghitung dari 0 hingga 60 menit ($60/80 = 3/4$), bukan dari 20 menit.</sub>
- C. $\frac{1}{4}$  
  <sub>Salah: Mengambil jawaban soal acuan secara langsung tanpa menghitung selang baru.</sub>
- D. $\frac{1}{8}$  
  <sub>Salah: Salah menghitung selisih batas menjadi 10 menit kemudian dibagi 80.</sub>

**Pembahasan:** Peluang pengisian daya antara 20 dan 60 menit adalah:
$$P(20 \le T \le 60) = \int_{20}^{60} \frac{1}{80}\,dt = \frac{60 - 20}{80} = \frac{40}{80} = \frac{1}{2}$$
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-1b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b04-e-easy-bt01-003
*variasi (konteks) | C2 | 1 langkah | jenis: peluang batas bawah fungsi konstan*

Sebuah laboratorium komputer dibuka untuk sesi praktikum mandiri dengan durasi paling lama 6 jam. Misalkan $Y$ menyatakan waktu praktikum seorang mahasiswa (dalam jam) dengan fungsi densitas peluang $f(y) = \frac{1}{6}$ untuk $0 \le y \le 6$ dan $f(y) = 0$ untuk nilai lainnya. Peluang seorang mahasiswa melakukan praktikum selama 4 jam atau lebih adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: Menyalin jawaban soal acuan buku siswa.</sub>
- **B. $\frac{1}{3}$** ✅  
  <sub>Benar: $P(Y \ge 4) = \int_{4}^{6} \frac{1}{6}\,dy = \frac{6 - 4}{6} = \frac{2}{6} = \frac{1}{3}$.</sub>
- C. $\frac{2}{3}$  
  <sub>Salah: Menghitung peluang kurang dari 4 jam ($P(Y < 4) = 4/6 = 2/3$).</sub>
- D. $\frac{1}{6}$  
  <sub>Salah: Mengira peluang bernilai sama dengan nilai fungsi pada titik tersebut $f(4)$.</sub>

**Pembahasan:** Peluang praktikum berlangsung selama 4 jam atau lebih dihitung dengan mengintegralkan fungsi dari $y = 4$ hingga batas maksimum $y = 6$:
$$P(Y \ge 4) = \int_{4}^{6} \frac{1}{6}\,dy = \frac{6 - 4}{6} = \frac{2}{6} = \frac{1}{3}$$
**Acuan:** siswa — siswa hal.267 Contoh Soal 4.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b04-e-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: konsep peluang titik tunggal*

Jika $X$ merupakan variabel acak kontinu dengan fungsi densitas peluang $f(x)$, maka untuk sembarang nilai konstanta real $c$, nilai dari $P(X = c)$ adalah ....

- **A. $0$** ✅  
  <sub>Benar: Pada variabel acak kontinu, peluang pada nilai tunggal selalu bernilai 0 karena luas di bawah kurva pada titik tunggal adalah nol.</sub>
- B. $1$  
  <sub>Salah: Tertukar dengan peluang total pada seluruh ruang sampel.</sub>
- C. $f(c)$  
  <sub>Salah: Mengira nilai peluang pada titik sama dengan nilai fungsi densitasnya (seperti pada variabel acak diskret).</sub>
- D. $\frac{1}{c}$  
  <sub>Salah: Mengasumsikan bentuk kebalikan konstanta secara keliru.</sub>

**Pembahasan:** Dalam distribusi peluang variabel acak kontinu, peluang dihitung sebagai luas daerah di bawah kurva pada interval tertentu. Karena suatu titik tunggal tidak memiliki lebar interval (lebar $= 0$), maka:
$$P(X = c) = \int_{c}^{c} f(x)\,dx = 0$$
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b04-e-easy-bt01-005
*orisinal | C1 | 1 langkah | jenis: definisi integral peluang kontinu*

Diketahui $X$ adalah variabel acak kontinu dengan fungsi densitas peluang $f(x)$. Peluang bahwa $X$ berada pada selang $a$ hingga $b$, yaitu $P(a \le X \le b)$, secara matematis dinyatakan oleh ....

- A. $f(b) - f(a)$  
  <sub>Salah: Tertukar dengan selisih nilai fungsi densitas pada titik batas.</sub>
- B. $\frac{f(a) + f(b)}{2}$  
  <sub>Salah: Keliru menggunakan rumus rata-rata nilai fungsi pada batas interval.</sub>
- C. $\int_{-\infty}^{\infty} f(x)\,dx$  
  <sub>Salah: Bentuk ini merepresentasikan peluang total pada seluruh domain yang bernilai 1.</sub>
- **D. $\int_{a}^{b} f(x)\,dx$** ✅  
  <sub>Benar: Berdasarkan definisi, peluang pada interval $[a, b]$ dinyatakan sebagai integral tentu dari fungsi densitas $f(x)$ dengan batas bawah $a$ dan batas atas $b$.</sub>

**Pembahasan:** Peluang bahwa variabel acak kontinu $X$ bernilai di antara $a$ dan $b$ sama dengan luas daerah di bawah kurva fungsi densitas $f(x)$ dari $x = a$ sampai $x = b$, yang dinyatakan dengan integral tentu:
$$P(a \le X \le b) = \int_{a}^{b} f(x)\,dx$$
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b04-e-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: peluang interval seragam*

Sebuah wahana permainan buka selama 240 menit setiap sesi. Misalkan $X$ adalah variabel acak yang menyatakan lama waktu seorang pengunjung berada di wahana (dalam menit) dengan fungsi densitas peluang:
$$f(x) = \begin{cases} \frac{1}{240}, & 0 \le x \le 240 \\ 0, & x < 0 \text{ atau } x > 240 \end{cases}$$
Peluang seorang pengunjung berada di wahana tersebut pada rentang waktu antara 40 dan 160 menit adalah ....

- A. $\frac{5}{6}$  
  <sub>Salah: Menjumlahkan batas alih-alih mengurangkan: $\frac{160 + 40}{240} = \frac{200}{240} = \frac{5}{6}$.</sub>
- B. $\frac{2}{3}$  
  <sub>Salah: Hanya menghitung batas atas dibagi panjang total: $\frac{160}{240} = \frac{2}{3}$.</sub>
- **C. $\frac{1}{2}$** ✅  
  <sub>Benar: $P(40 \le X \le 160) = \int_{40}^{160} \frac{1}{240}\,dx = \frac{160 - 40}{240} = \frac{120}{240} = \frac{1}{2}$.</sub>
- D. $\frac{1}{6}$  
  <sub>Salah: Hanya menghitung batas bawah dibagi panjang total: $\frac{40}{240} = \frac{1}{6}$.</sub>

**Pembahasan:** Peluang variabel acak kontinu $X$ pada interval $40 \le X \le 160$ dihitung dengan integral:
$$P(40 \le X \le 160) = \int_{40}^{160} f(x)\,dx = \int_{40}^{160} \frac{1}{240}\,dx = \left[ \frac{x}{240} \right]_{40}^{160} = \frac{160 - 40}{240} = \frac{120}{240} = \frac{1}{2}.$$
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b04-e-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: peluang interval seragam*

Sebuah mesin pendingin beroperasi secara otomatis selama 120 menit dalam satu siklus kerja. Misalkan $X$ adalah variabel acak kontinu yang menyatakan durasi kerja mesin (dalam menit) dengan fungsi densitas:
$$f(x) = \begin{cases} \frac{1}{120}, & 0 \le x \le 120 \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Peluang mesin beroperasi dalam rentang waktu antara 45 menit dan 85 menit adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: Salah mengurangkan batas: $(85 - 45) = 30$, menghasilkan $\frac{30}{120} = \frac{1}{4}$.</sub>
- B. $\frac{3}{8}$  
  <sub>Salah: Hanya menghitung batas bawah dibagi total: $\frac{45}{120} = \frac{3}{8}$.</sub>
- C. $\frac{17}{24}$  
  <sub>Salah: Hanya menghitung batas atas dibagi total: $\frac{85}{120} = \frac{17}{24}$.</sub>
- **D. $\frac{1}{3}$** ✅  
  <sub>Benar: $P(45 \le X \le 85) = \int_{45}^{85} \frac{1}{120}\,dx = \frac{85 - 45}{120} = \frac{40}{120} = \frac{1}{3}$.</sub>

**Pembahasan:** Peluang $X$ berada pada selang $45 \le X \le 85$ dihitung melalui rumus integral:
$$P(45 \le X \le 85) = \int_{45}^{85} \frac{1}{120}\,dx = \frac{85 - 45}{120} = \frac{40}{120} = \frac{1}{3}.$$
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-1b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b04-e-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: peluang batas waktu variabel kontinu*

Sebuah ruang laboratorium disewa maksimal selama 8 jam dalam sehari. Waktu penggunaan laboratorium dinyatakan oleh variabel acak kontinu $Y$ (dalam jam) dengan fungsi densitas:
$$f(y) = \begin{cases} \frac{1}{8}, & 0 \le y \le 8 \\ 0, & \text{untuk } y \text{ lainnya} \end{cases}$$
Peluang laboratorium tersebut digunakan selama 6 jam atau lebih adalah ....

- A. $\frac{3}{8}$  
  <sub>Salah: Salah memasukkan batas integrasi, menghitung $\frac{6 - 3}{8} = \frac{3}{8}$.</sub>
- B. $\frac{3}{4}$  
  <sub>Salah: Menghitung peluang kebalikannya, yaitu $P(Y \le 6) = \frac{6}{8} = \frac{3}{4}$.</sub>
- C. $\frac{1}{8}$  
  <sub>Salah: Mengira nilai peluang langsung sama dengan nilai fungsi densitas $f(6) = \frac{1}{8}$.</sub>
- **D. $\frac{1}{4}$** ✅  
  <sub>Benar: $P(Y \ge 6) = \int_{6}^{8} \frac{1}{8}\,dy = \frac{8 - 6}{8} = \frac{2}{8} = \frac{1}{4}$.</sub>

**Pembahasan:** Karena laboratorium disewa paling lama 8 jam, maka peluang penggunaan selama 6 jam atau lebih adalah:
$$P(Y \ge 6) = \int_{6}^{8} f(y)\,dy = \int_{6}^{8} \frac{1}{8}\,dy = \left[ \frac{y}{8} \right]_{6}^{8} = \frac{8 - 6}{8} = \frac{2}{8} = \frac{1}{4}.$$
**Acuan:** siswa — siswa hal.267 Contoh Soal 4.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b04-e-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: sifat dasar variabel acak kontinu*

Perhitungan nilai peluang untuk suatu variabel acak kontinu tidak ditentukan berdasarkan nilai tunggal, melainkan dihitung berdasarkan ....

- **A. luas daerah di bawah kurva fungsi densitas pada suatu interval nilai** ✅  
  <sub>Benar: Sesuai konsep dasar materi, peluang variabel kontinu dipandang sebagai selang atau luas di bawah kurva pada suatu rentang/interval.</sub>
- B. nilai diskret dari fungsi densitas pada titik tersebut  
  <sub>Salah: Variabel acak kontinu tidak memiliki titik diskret.</sub>
- C. nilai gradien kurva fungsi densitas pada suatu titik tertentu  
  <sub>Salah: Peluang dihitung dari integral (luas), bukan turunan (gradien).</sub>
- D. jumlah nilai probabilitas semua titik diskret dalam sampel  
  <sub>Salah: Keliru menyamakan konsep variabel kontinu dengan variabel acak diskret.</sub>

**Pembahasan:** Dalam variabel acak kontinu, peluang suatu kejadian tidak dihitung berdasarkan nilai titik tunggal, melainkan berdasarkan interval nilai, yaitu direpresentasikan sebagai luas daerah di bawah kurva fungsi densitas pada interval tersebut.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b04-e-easy-bt01-010
*orisinal | C1 | 1 langkah | jenis: terminologi distribusi peluang kontinu*

Fungsi distribusi peluang yang menggambarkan sebaran nilai dari suatu variabel acak kontinu secara matematis disebut sebagai ....

- A. fungsi massa peluang  
  <sub>Salah: Fungsi massa peluang adalah istilah khusus untuk variabel acak diskret.</sub>
- B. frekuensi relatif  
  <sub>Salah: Frekuensi relatif adalah proporsi kemunculan data statistik empiris, bukan fungsi sebaran kontinu.</sub>
- C. fungsi frekuensi kumulatif  
  <sub>Salah: Bukan istilah fungsi distribusi peluang kontinu.</sub>
- **D. fungsi densitas** ✅  
  <sub>Benar: Buku siswa menyatakan secara eksplisit bahwa fungsi distribusi peluang variabel acak kontinu disebut fungsi densitas.</sub>

**Pembahasan:** Berdasarkan materi pengantar variabel acak kontinu pada buku teks, fungsi distribusi peluang untuk variabel acak kontinu disajikan dalam rumus fungsi yang disebut sebagai fungsi densitas.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b04-e-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: peluang interval fungsi linear*

Suatu variabel acak kontinu $X$, untuk nilai-nilai di antara $x=2$ dan $x=6$, memiliki fungsi densitas peluang $f(x)=\frac{x}{16}$. Nilai dari $P(X < 4)$ adalah ....

- **A. $\frac{3}{8}$** ✅  
  <sub>Benar: $\int_{2}^{4} \frac{x}{16}\,dx = \left[\frac{x^2}{32}\right]_2^4 = \frac{16 - 4}{32} = \frac{12}{32} = \frac{3}{8}$.</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: Hanya menghitung nilai ordinat titik $f(4) = \frac{4}{16} = \frac{1}{4}$.</sub>
- C. $\frac{1}{2}$  
  <sub>Salah: Mengintegrasikan dari batas 0 hingga 4, mengabaikan batas bawah definisi variabel acak yaitu $x=2$.</sub>
- D. $\frac{5}{8}$  
  <sub>Salah: Menghitung komplemennya yaitu $P(X > 4) = \int_4^6 \frac{x}{16}\,dx = \frac{36-16}{32} = \frac{20}{32} = \frac{5}{8}$.</sub>

**Pembahasan:** Batas bawah variabel acak kontinu $X$ adalah 2, sehingga:
$$P(X < 4) = \int_{2}^{4} \frac{x}{16}\,dx = \left[ \frac{x^2}{32} \right]_{2}^{4} = \frac{4^2}{32} - \frac{2^2}{32} = \frac{16 - 4}{32} = \frac{12}{32} = \frac{3}{8}.$$
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b04-e-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: peluang interval seragam kontekstual*

Seorang teknisi melakukan kalibrasi alat sensor dengan waktu pengerjaan yang tersebar merata dari 10 menit hingga 70 menit. Misalkan $X$ menyatakan waktu kalibrasi (dalam menit) dengan fungsi densitas peluang $f(x) = \frac{1}{60}$ untuk $10 \le x \le 70$, dan $f(x)=0$ untuk nilai lainnya.

Berdasarkan stimulus tersebut, tentukan peluang teknisi menyelesaikan kalibrasi dalam rentang waktu dari 25 menit hingga 55 menit.

- A. $\frac{7}{12}$  
  <sub>Salah: Menghitung integral dari batas bawah 10 hingga 45 menit.</sub>
- B. $\frac{3}{5}$  
  <sub>Salah: Membagi selisih waktu dengan batas atas rentang (50 menit) alih-alih panjang selang total 60 menit.</sub>
- **C. $\frac{1}{2}$** ✅  
  <sub>Benar: $\int_{25}^{55} \frac{1}{60}\,dx = \frac{55 - 25}{60} = \frac{30}{60} = \frac{1}{2}$.</sub>
- D. $\frac{1}{3}$  
  <sub>Salah: Salah menghitung selisih rentang waktu: $55 - 25 = 20$, lalu $20/60 = 1/3$.</sub>

**Pembahasan:** Peluang variabel acak $X$ berada dalam rentang $25 \le X \le 55$ menit:
$$P(25 \le X \le 55) = \int_{25}^{55} \frac{1}{60}\,dx = \frac{55 - 25}{60} = \frac{30}{60} = \frac{1}{2}.$$
**Acuan:** siswa — siswa hal.268 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b04-e-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: karakteristik variabel acak kontinu*

Distribusi peluang dari suatu variabel acak kontinu tidak dapat disajikan dalam bentuk tabel distribusi peluang diskret karena ....

- A. variabel acak kontinu hanya dapat bernilai bilangan bulat nonnegatif  
  <sub>Salah: Tertukar dengan karakteristik variabel acak diskret (khususnya hitungan/cacah).</sub>
- B. fungsi densitas peluang selalu bernilai konstan untuk semua interval  
  <sub>Salah: Salah, fungsi densitas tidak harus konstan, bisa fungsi linier atau kurva lainnya.</sub>
- **C. nilai-nilai variabel acak kontinu berada pada suatu selang yang tak terhingga banyaknya** ✅  
  <sub>Benar: Variabel acak kontinu terdefinisi pada interval/selang kontinu sehingga tidak mungkin didaftar satu per satu dalam tabel.</sub>
- D. jumlah seluruh peluang dari variabel acak kontinu tidak sama dengan satu  
  <sub>Salah: Salah, total peluang kurva densitas tetap harus sama dengan satu.</sub>

**Pembahasan:** Pada variabel acak kontinu, nilai-nilai yang mungkin tersebar secara kontinu dalam suatu selang (interval) yang memuat tak terhingga banyaknya titik real. Oleh karena itu, peluangnya tidak dapat dicacah satu per satu dalam bentuk tabel.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b04-e-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: interpretasi geometris fungsi densitas*

Pada grafik fungsi densitas peluang $f(x)$ dari suatu variabel acak kontinu $X$, luas daerah di bawah kurva yang dibatasi oleh garis $x = a$ dan $x = b$ serta sumbu-$x$ merepresentasikan ....

- A. nilai rata-rata dari variabel acak kontinu $X$  
  <sub>Salah: Rata-rata (ekspektasi) dihitung dengan integral $x f(x)$, bukan sekadar luas daerah di bawah $f(x)$.</sub>
- B. nilai peluang titik tunggal saat $X = b - a$  
  <sub>Salah: Peluang titik tunggal pada variabel kontinu adalah 0, bukan luas daerah interval.</sub>
- C. nilai varians dari variabel acak kontinu $X$  
  <sub>Salah: Varians melibatkan momen kedua, bukan representasi luas daerah kurva densitas biasa.</sub>
- **D. peluang variabel acak bernilai pada interval $a \le X \le b$** ✅  
  <sub>Benar: Sesuai konsep dasar materi, luas di bawah kurva densitas antara $a$ dan $b$ menyatakan $P(a \le X \le b)$.</sub>

**Pembahasan:** Dalam fungsi densitas peluang variabel acak kontinu, luas daerah di bawah kurva $f(x)$ yang dibatasi oleh interval $[a, b]$ dan sumbu-$x$ menyatakan nilai peluang kejadian tersebut, yaitu $P(a \le X \le b) = \int_{a}^{b} f(x)\,dx$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b04-e-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: kalkulasi integral fungsi linear*

Suatu variabel acak kontinu $X$, untuk nilai-nilai di antara $x=0$ dan $x=6$, didefinisikan dengan fungsi densitas peluang $f(x)=\frac{x+1}{24}$. Nilai dari $P(X < 2)$ adalah ....

- A. $\frac{1}{8}$  
  <sub>Salah: Hanya mengintegralkan suku $x$ tanpa mengintegralkan konstanta $1$.</sub>
- **B. $\frac{1}{6}$** ✅  
  <sub>Benar: $P(X < 2) = \int_{0}^{2} \frac{x+1}{24}\,dx = \left[ \frac{x^2/2 + x}{24} \right]_0^2 = \frac{2+2}{24} = \frac{4}{24} = \frac{1}{6}$.</sub>
- C. $\frac{1}{4}$  
  <sub>Salah: Salah menghitung hasil antiturunan saat evaluasi batas atas $x=2$.</sub>
- D. $\frac{1}{12}$  
  <sub>Salah: Langsung mensubstitusikan $x=2$ ke rumus fungsi densitas tanpa melakukan integrasi.</sub>

**Pembahasan:** Peluang dihitung dengan integral tentu fungsi densitas dari batas bawah 0 hingga 2:
$$P(X < 2) = \int_{0}^{2} \frac{x+1}{24}\,dx = \left[ \frac{\frac{1}{2}x^2 + x}{24} \right]_0^2 = \frac{2 + 2}{24} = \frac{4}{24} = \frac{1}{6}.$$
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b04-e-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: peluang seragam waktu kontinu*

Seorang pekerja magang mencatat durasi fokus kerja harian yang tersebar secara merata antara 30 menit hingga 150 menit. Jika $X$ menyatakan durasi waktu fokus tersebut (dalam menit), peluang pekerja tersebut fokus dalam rentang 50 menit hingga 90 menit adalah ....

- **A. $\frac{1}{3}$** ✅  
  <sub>Benar: $P(50 \le X \le 90) = \frac{90 - 50}{150 - 30} = \frac{40}{120} = \frac{1}{3}$.</sub>
- B. $\frac{2}{5}$  
  <sub>Salah: Salah menghitung panjang interval 90 dikurang 50 menjadi 50 bukan 40.</sub>
- C. $\frac{1}{4}$  
  <sub>Salah: Membagi selisih batas dengan batas maksimum saja tanpa mengurangi batas minimum.</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: Mengira rentang 50 hingga 90 menit merupakan separuh dari total durasi pengamatan.</sub>

**Pembahasan:** Panjang rentang total variabel adalah $150 - 30 = 120$ menit, sehingga fungsi densitasnya $f(x) = \frac{1}{120}$ untuk $30 \le x \le 150$.
Peluang durasi berada pada rentang 50 hingga 90 menit:
$$P(50 \le X \le 90) = \int_{50}^{90} \frac{1}{120}\,dx = \frac{90 - 50}{120} = \frac{40}{120} = \frac{1}{3}.$$
**Acuan:** siswa — siswa hal.268 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b04-e-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: kalkulasi integral fungsi seragam*

Seorang atlet renang mencatat waktu latihan fisik tambahan yang tersebar merata dari 15 menit hingga 75 menit. Jika durasi latihan dinyatakan oleh variabel acak kontinu $X$, peluang atlet tersebut berlatih dalam rentang waktu antara 25 menit hingga 65 menit adalah ....

- A. $\frac{1}{2}$  
  <sub>Salah: Mengira selang 25 sampai 65 menit adalah setengah dari keseluruhan selang.</sub>
- **B. $\frac{2}{3}$** ✅  
  <sub>Benar: $P(25 \le X \le 65) = \frac{65 - 25}{75 - 15} = \frac{40}{60} = \frac{2}{3}$.</sub>
- C. $\frac{1}{3}$  
  <sub>Salah: Menghitung komplemen peluang di luar rentang yang diminta.</sub>
- D. $\frac{3}{4}$  
  <sub>Salah: Salah melakukan penyederhanaan pecahan nilai 40 dibagi 60.</sub>

**Pembahasan:** Fungsi densitas kontinu seragam untuk rentang 15 hingga 75 menit bernilai $f(x) = \frac{1}{75 - 15} = \frac{1}{60}$.
Peluang pada selang $25 \le X \le 65$:
$$P(25 \le X \le 65) = \int_{25}^{65} \frac{1}{60}\,dx = \frac{65 - 25}{60} = \frac{40}{60} = \frac{2}{3}.$$
**Acuan:** siswa — siswa hal.268 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b04-e-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: karakteristik visual kurva densitas*

Berdasarkan representasi grafisnya, fungsi peluang dari suatu variabel acak kontinu disajikan dalam bentuk ....

- A. himpunan pasangan titik koordinat terputus  
  <sub>Salah: Ciri khas dari variabel diskret bukan kontinu.</sub>
- B. diagram batang terpisah dengan tinggi tertentu  
  <sub>Salah: Keliru mengidentifikasi representasi distribusi peluang variabel acak diskret.</sub>
- **C. kurva kontinu tanpa titik-titik diskret** ✅  
  <sub>Benar: Buku siswa halaman 265 menyatakan bahwa fungsi peluang kontinu digambarkan sebagai kurva kontinu yang tidak memiliki titik-titik diskret.</sub>
- D. garis bertangga dengan loncatan diskret pada tiap bilangan bulat  
  <sub>Salah: Deskripsi bentuk grafik fungsi tangga kumulatif diskret.</sub>

**Pembahasan:** Pada distribusi peluang variabel acak kontinu, nilai-nilai variabel tersebar kontinu dalam suatu interval sehingga fungsinya digambarkan berupa kurva mulus kontinu tanpa patahan titik-titik diskret.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b04-e-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: definisi perhitungan peluang kontinu*

Pada variabel acak kontinu, peluang suatu kejadian dalam suatu selang nilai tertentu dihitung berdasarkan ....

- A. penjumlahan nilai fungsi peluang pada titik-titik ujung interval  
  <sub>Salah: Mengira peluang kontinu dihitung seperti penjumlahan probabilitas diskret.</sub>
- **B. luas daerah di bawah kurva fungsi densitas** ✅  
  <sub>Benar: Konsep dasar probabilitas kontinu menyatakan bahwa peluang pada suatu interval dihitung sebagai luas daerah di bawah kurva fungsi densitas peluangnya.</sub>
- C. nilai ordinat tertinggi dari kurva fungsi densitas  
  <sub>Salah: Mengacaukan konsep luas daerah dengan nilai puncak atau modus distribusi.</sub>
- D. kemiringan garis singgung pada titik batas interval  
  <sub>Salah: Keliru mengaitkan turunan diferensial fungsi densitas dengan nilai peluang.</sub>

**Pembahasan:** Peluang variabel acak kontinu tidak diperoleh dari nilai tunggal titik pada kurva, melainkan dihitung melalui luas area di bawah kurva fungsi densitas pada selang yang bersangkutan via integral tentu.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b04-e-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: peluang durasi waktu seragam*

Seorang siswa mengikuti sesi bimbingan belajar mandiri selama 3 jam setiap sore, dari pukul 09.00—12.00. Ia mencatat waktu efektif belajar setiap hari dalam satuan menit. Berdasarkan pengamatan, waktu efektif tersebut tersebar merata dari 50 menit hingga 150 menit. Misalkan $X$ adalah variabel acak kontinu yang menyatakan lama waktu efektif belajar (dalam menit). Peluang bahwa siswa tersebut belajar efektif dalam rentang waktu dari 75 menit hingga 110 menit adalah ....

- A. $\frac{2}{5}$  
  <sub>Salah: Siswa menghitung peluang komplemen dari batas atas yang ditanyakan ke ujung domain, yaitu $\frac{150 - 110}{100} = \frac{40}{100} = \frac{2}{5}$.</sub>
- B. $\frac{7}{36}$  
  <sub>Salah: Siswa membagi panjang interval yang ditanyakan (35 menit) dengan total durasi bimbingan 3 jam (180 menit), bukan dengan panjang rentang sebaran variabel acak (100 menit).</sub>
- **C. $\frac{7}{20}$** ✅  
  <sub>Benar: Fungsi densitas peluang seragam pada selang $[50, 150]$ adalah $f(x) = \frac{1}{150 - 50} = \frac{1}{100}$. Peluang pada rentang $75 \le X \le 110$ adalah $P(75 \le X \le 110) = \int_{75}^{110} \frac{1}{100}\,dx = \frac{110 - 75}{100} = \frac{35}{100} = \frac{7}{20}$.</sub>
- D. $\frac{3}{5}$  
  <sub>Salah: Siswa menghitung selang dari batas bawah domain sampai batas atas yang ditanyakan, yaitu $\frac{110 - 50}{100} = \frac{60}{100} = \frac{3}{5}$.</sub>

**Pembahasan:** Diketahui variabel acak kontinu $X$ tersebar merata dari $x = 50$ hingga $x = 150$.
Panjang interval domain adalah $150 - 50 = 100$.
Fungsi densitas peluang $X$ adalah:
$$f(x) = \begin{cases} \frac{1}{100}, & 50 \le x \le 150 \\ 0, & x \text{ lainnya} \end{cases}$$

Peluang siswa belajar efektif dalam rentang waktu 75 menit hingga 110 menit dihitung dengan integral:
$$P(75 \le X \le 110) = \int_{75}^{110} f(x)\,dx = \int_{75}^{110} \frac{1}{100}\,dx = \left[ \frac{x}{100} \right]_{75}^{110} = \frac{110 - 75}{100} = \frac{35}{100} = \frac{7}{20}$$

Jadi, peluang siswa tersebut belajar efektif dalam rentang waktu 75 menit hingga 110 menit adalah $\frac{7}{20}$.
**Acuan:** siswa — siswa hal.268 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b04-e-medium-bt01-001
*variasi (angka) | C3 | 2 langkah | jenis: menghitung peluang dari fungsi densitas linear*

Suatu variabel acak kontinu $X$, untuk nilai-nilai di antara $x=3$ dan $x=7$, didefinisikan dengan fungsi densitas peluang $f(x)=\frac{x-1}{16}$, dan $f(x)=0$ untuk nilai $x$ lainnya. Nilai dari $P(X \ge 5)$ adalah ....

- **A. $\frac{5}{8}$** ✅  
  <sub>Benar: $P(X \ge 5) = \int_5^7 \frac{x-1}{16}\,dx = \left[\frac{x^2}{32} - \frac{x}{16}\right]_5^7 = \left(\frac{49}{32} - \frac{14}{32}\right) - \left(\frac{25}{32} - \frac{10}{32}\right) = \frac{35}{32} - \frac{15}{32} = \frac{20}{32} = \frac{5}{8}$.</sub>
- B. $\frac{3}{4}$  
  <sub>Salah: Siswa keliru memasukkan batas bawah $x=4$ alih-alih $x=5$ sehingga memperoleh $\frac{24}{32} = \frac{3}{4}$.</sub>
- C. $\frac{3}{8}$  
  <sub>Salah: Siswa menghitung peluang komplemennya yaitu $P(X < 5)$ alih-alih $P(X \ge 5)$.</sub>
- D. $\frac{7}{16}$  
  <sub>Salah: Siswa salah melakukan integrasi dan hanya menghitung selisih batas atas dan batas bawah dikalikan fungsi pada titik tengah.</sub>

**Pembahasan:** Peluang variabel acak kontinu $X$ pada interval $X \ge 5$ dalam domain $[3, 7]$ dihitung dengan integral tentu:
$$P(X \ge 5) = \int_5^7 f(x)\,dx = \int_5^7 \frac{x-1}{16}\,dx$$

Selesaikan integral:
$$\int_5^7 \frac{x-1}{16}\,dx = \left[ \frac{(x-1)^2}{32} \right]_5^7 = \frac{(7-1)^2}{32} - \frac{(5-1)^2}{32} = \frac{36}{32} - \frac{16}{32} = \frac{20}{32} = \frac{5}{8}$$

Jadi, nilai dari $P(X \ge 5)$ adalah $\frac{5}{8}$.
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b04-e-medium-bt01-002
*variasi (konteks) | C3 | 2 langkah | jenis: menghitung peluang durasi waktu seragam*

Seorang pengunjung kafe memanfaatkan fasilitas akses internet yang dibatasi paling lama 5 jam per sesi. Misalkan $W$ menyatakan variabel acak kontinu untuk durasi pemakaian internet (dalam jam) dengan fungsi densitas peluang $f(w) = \frac{1}{5}$ untuk $0 \le w \le 5$, dan $f(w) = 0$ untuk nilai $w$ lainnya. Peluang pengunjung tersebut memakai internet selama antara 1 jam hingga 3,5 jam adalah ....

- A. $\frac{7}{10}$  
  <sub>Salah: Siswa menghitung peluang kumulatif hingga batas atas $P(W \le 3{,}5) = \frac{3{,}5}{5} = \frac{7}{10}$ tanpa mengurangkan batas bawah.</sub>
- B. $\frac{1}{5}$  
  <sub>Salah: Siswa hanya menghitung peluang hingga batas bawah $P(W \le 1) = \frac{1}{5}$.</sub>
- C. $\frac{3}{10}$  
  <sub>Salah: Siswa menghitung komplemen batas atas $1 - \frac{7}{10} = \frac{3}{10}$.</sub>
- **D. $\frac{1}{2}$** ✅  
  <sub>Benar: $P(1 \le W \le 3{,}5) = \int_{1}^{3{,}5} \frac{1}{5}\,dw = \frac{1}{5}(3{,}5 - 1) = \frac{2{,}5}{5} = \frac{1}{2}$.</sub>

**Pembahasan:** Peluang bahwa durasi pemakaian $W$ berada di antara 1 jam dan 3,5 jam dinyatakan oleh:
$$P(1 \le W \le 3{,}5) = \int_{1}^{3{,}5} f(w)\,dw$$

Substitusi fungsi densitas peluang:
$$P(1 \le W \le 3{,}5) = \int_{1}^{3{,}5} \frac{1}{5}\,dw = \left[ \frac{w}{5} \right]_{1}^{3{,}5} = \frac{3{,}5 - 1}{5} = \frac{2{,}5}{5} = \frac{1}{2}$$

Jadi, peluang pemakaian internet antara 1 jam hingga 3,5 jam adalah $\frac{1}{2}$.
**Acuan:** siswa — siswa hal.267 Contoh Soal 4.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b04-e-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: menentukan konstanta fungsi densitas*

Suatu variabel acak kontinu $X$ memiliki fungsi densitas peluang yang dinyatakan oleh:
$$f(x) = \begin{cases} kx^2, & 0 \le x \le 3 \\ 0, & x \text{ lainnya} \end{cases}$$
Nilai dari $P(1 \le X \le 2)$ adalah ....

- A. $\frac{1}{9}$  
  <sub>Salah: Siswa mengira nilai konstanta $k = \frac{1}{9}$ adalah jawaban akhir peluang yang ditanyakan.</sub>
- B. $\frac{8}{27}$  
  <sub>Salah: Siswa hanya mengevaluasi integral pada batas atas $x=2$ tanpa mengurangkan hasil evaluasi batas bawah $x=1$.</sub>
- C. $\frac{7}{9}$  
  <sub>Salah: Siswa lupa mengalikan faktor $\frac{1}{3}$ hasil integrasi $x^2$ pada langkah kedua sehingga menghitung $\frac{1}{9}(2^3 - 1^3)$ alih-alih $\frac{1}{27}(8 - 1)$.</sub>
- **D. $\frac{7}{27}$** ✅  
  <sub>Benar: Pertama cari nilai $k$: $\int_0^3 kx^2\,dx = 1 \implies k\left[\frac{x^3}{3}\right]_0^3 = 9k = 1 \implies k = \frac{1}{9}$. Kemudian hitung $P(1 \le X \le 2) = \int_1^2 \frac{1}{9}x^2\,dx = \frac{1}{9}\left[\frac{x^3}{3}\right]_1^2 = \frac{8 - 1}{27} = \frac{7}{27}$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai konstanta $k$ menggunakan syarat total peluang bernilai 1:
$$\int_{-\infty}^{\infty} f(x)\,dx = 1$$
$$\int_0^3 kx^2\,dx = 1 \implies k \left[ \frac{x^3}{3} \right]_0^3 = 1 \implies k \left(\frac{27}{3}\right) = 1 \implies 9k = 1 \implies k = \frac{1}{9}$$

Langkah 2: Menghitung $P(1 \le X \le 2)$:
$$P(1 \le X \le 2) = \int_1^2 \frac{1}{9}x^2\,dx = \left[ \frac{x^3}{27} \right]_1^2 = \frac{2^3 - 1^3}{27} = \frac{8 - 1}{27} = \frac{7}{27}$$

Jadi, nilai $P(1 \le X \le 2)$ adalah $\frac{7}{27}$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b04-e-medium-bt01-004
*orisinal | C3 | 2 langkah | jenis: menghitung peluang komplemen dari fungsi densitas kuadrat*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang sebagai berikut:
$$f(x) = \begin{cases} \frac{3}{8}x^2, & 0 \le x \le 2 \\ 0, & x \text{ lainnya} \end{cases}$$
Nilai dari $P(X > 1)$ adalah ....

- A. $\frac{5}{8}$  
  <sub>Salah: Siswa salah mengevaluasi nilai $2^3$ menjadi $6$ sehingga menghitung $\frac{6 - 1}{8} = \frac{5}{8}$.</sub>
- B. $\frac{3}{4}$  
  <sub>Salah: Siswa salah saat mengintegrasikan $x^2$ menjadi $x$ sehingga menghitung $\frac{3}{8}(2^2 - 1^2) = \frac{9}{8}$ lalu dikurangi atau salah operasi menjadi $\frac{3}{4}$.</sub>
- C. $\frac{1}{8}$  
  <sub>Salah: Siswa menghitung komplemennya yaitu $P(X \le 1) = \int_0^1 \frac{3}{8}x^2\,dx = \frac{1}{8}$.</sub>
- **D. $\frac{7}{8}$** ✅  
  <sub>Benar: $P(X > 1) = \int_1^2 \frac{3}{8}x^2\,dx = \left[\frac{x^3}{8}\right]_1^2 = \frac{2^3 - 1^3}{8} = \frac{8 - 1}{8} = \frac{7}{8}$.</sub>

**Pembahasan:** Karena fungsi hanya bernilai tak nol pada interval $[0, 2]$, batas atas untuk $X > 1$ adalah $x = 2$:
$$P(X > 1) = \int_1^2 f(x)\,dx = \int_1^2 \frac{3}{8}x^2\,dx$$

Integralkan fungsi tersebut:
$$\int_1^2 \frac{3}{8}x^2\,dx = \left[ \frac{3}{8} \cdot \frac{x^3}{3} \right]_1^2 = \left[ \frac{x^3}{8} \right]_1^2 = \frac{2^3}{8} - \frac{1^3}{8} = \frac{8}{8} - \frac{1}{8} = \frac{7}{8}$$

Jadi, nilai dari $P(X > 1)$ adalah $\frac{7}{8}$.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b04-e-medium-bt01-005
*orisinal | C4 | 4 langkah | jenis: menghitung peluang fungsi densitas sepotong*

Suatu variabel acak kontinu $X$ memiliki fungsi densitas peluang sepotong yang didefinisikan sebagai:
$$f(x) = \begin{cases} \frac{1}{4}x, & 0 \le x \le 2 \\ \frac{1}{2}, & 2 < x \le 3 \\ 0, & x \text{ lainnya} \end{cases}$$
Nilai dari peluang $P(1 \le X \le 2{,}5)$ adalah ....

- A. $\frac{7}{8}$  
  <sub>Salah: Siswa keliru menggunakan fungsi $\frac{1}{2}$ untuk seluruh rentang dari $1$ hingga $2{,}5$ atau salah menjumlahkan pecahan.</sub>
- **B. $\frac{5}{8}$** ✅  
  <sub>Benar: $P(1 \le X \le 2{,}5) = \int_1^2 \frac{1}{4}x\,dx + \int_2^{2{,}5} \frac{1}{2}\,dx = \left[\frac{x^2}{8}\right]_1^2 + \left[\frac{x}{2}\right]_2^{2{,}5} = \left(\frac{4-1}{8}\right) + \frac{1}{2}(0{,}5) = \frac{3}{8} + \frac{1}{4} = \frac{5}{8}$.</sub>
- C. $\frac{3}{8}$  
  <sub>Salah: Siswa hanya mengintegrasikan bagian pertama pada interval $[1, 2]$ dan mengabaikan bagian kedua.</sub>
- D. $\frac{1}{4}$  
  <sub>Salah: Siswa hanya menghitung bagian kedua pada interval $[2, 2{,}5]$ dan mengabaikan bagian pertama.</sub>

**Pembahasan:** Interval $[1, 2{,}5]$ melintasi titik batas $x = 2$, sehingga integral harus dipecah menjadi dua bagian:
$$P(1 \le X \le 2{,}5) = \int_1^2 f(x)\,dx + \int_2^{2{,}5} f(x)\,dx$$

Hitung masing-masing integral:
1. Bagian pertama ($1 \le x \le 2$):
$$\int_1^2 \frac{1}{4}x\,dx = \left[ \frac{x^2}{8} \right]_1^2 = \frac{2^2 - 1^2}{8} = \frac{3}{8}$$

2. Bagian kedua ($2 < x \le 2{,}5$):
$$\int_2^{2{,}5} \frac{1}{2}\,dx = \left[ \frac{1}{2}x \right]_2^{2{,}5} = \frac{1}{2}(2{,}5 - 2) = \frac{1}{2}(0{,}5) = 0{,}25 = \frac{2}{8}$$

Jumlahkan kedua hasil:
$$P(1 \le X \le 2{,}5) = \frac{3}{8} + \frac{2}{8} = \frac{5}{8}$$

Jadi, nilai dari $P(1 \le X \le 2{,}5)$ adalah $\frac{5}{8}$.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b04-e-medium-bt01-006
*variasi (angka) | C3 | 2 langkah | jenis: menghitung peluang interval waktu operasional*

Dalam masa pembatasan kunjungan, suatu pameran buku hanya dibuka selama 150 menit, yaitu mulai pukul 09.00 hingga pukul 11.30. Pengunjung tidak diperbolehkan berada di area pameran sebelum pukul 09.00 dan wajib meninggalkan area paling lambat pukul 11.30. Misalkan $X$ adalah variabel acak yang menyatakan lama pengunjung berada di dalam area pameran (dalam menit) dengan fungsi densitas peluang:
$$f(x) = \begin{cases} \frac{1}{150}, & 0 \le x \le 150 \\ 0, & x < 0 \text{ atau } x > 150 \end{cases}$$
Berapakah peluang seorang pengunjung berada di area pameran pada rentang waktu antara 45 dan 105 menit?

- **A. $\frac{2}{5}$** ✅  
  <sub>Benar: $P(45 \le X \le 105) = \int_{45}^{105} \frac{1}{150}\,dx = \frac{105 - 45}{150} = \frac{60}{150} = \frac{2}{5}$.</sub>
- B. $\frac{7}{15}$  
  <sub>Salah: Hanya menghitung peluang terhadap batas atas $105/150 = 7/10$ lalu dikurangi $1/3$.</sub>
- C. $\frac{3}{10}$  
  <sub>Salah: Salah menghitung selisih $105 - 45$ menjadi $45$, lalu $45/150 = 3/10$.</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: Membagi langsung titik tengah interval $(105 + 45)/2 = 75$, sehingga $75/150 = 1/2$.</sub>

**Pembahasan:** Peluang pengunjung berada di area pameran antara 45 dan 105 menit dihitung dengan integral:
$$P(45 \le X \le 105) = \int_{45}^{105} f(x)\,dx = \int_{45}^{105} \frac{1}{150}\,dx$$
$$P(45 \le X \le 105) = \left[ \frac{x}{150} \right]_{45}^{105} = \frac{105 - 45}{150} = \frac{60}{150} = \frac{2}{5}$$
Jadi, peluangnya adalah $\frac{2}{5}$.
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b04-e-medium-bt01-007
*orisinal | C3 | 3 langkah | jenis: menentukan nilai fungsi distribusi kumulatif*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang sebagai berikut:
$$f(x) = \begin{cases} \frac{3}{64}x^2, & 0 \le x \le 4 \\ 0, & x \text{ lainnya} \end{cases}$$
Jika $F(x)$ merupakan fungsi distribusi kumulatif dari $X$, berapakah nilai dari $F(2)$?

- **A. $\frac{1}{8}$** ✅  
  <sub>Benar: $F(2) = \int_{0}^{2} \frac{3}{64}t^2\,dt = \left[ \frac{t^3}{64} \right]_0^2 = \frac{8}{64} = \frac{1}{8}$.</sub>
- B. $\frac{1}{16}$  
  <sub>Salah: Membagi hasil pangkat secara keliru menjadi $2^2 / 64 = 4/64 = 1/16$.</sub>
- C. $\frac{1}{4}$  
  <sub>Salah: Lupa mengalikan koefisien $1/3$ saat mengintegralkan $x^2$, memperoleh $\frac{3}{64}(2^2) = \frac{12}{64}$ lalu membulatkan keliru.</sub>
- D. $\frac{3}{16}$  
  <sub>Salah: Langsung mensubstitusikan $x=2$ ke dalam fungsi densitas $f(2) = \frac{3}{64}(4) = \frac{3}{16}$.</sub>

**Pembahasan:** Berdasarkan definisi fungsi distribusi kumulatif untuk variabel acak kontinu:
$$F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\,dt$$
Untuk $0 \le x \le 4$:
$$F(x) = \int_{0}^{x} \frac{3}{64}t^2\,dt = \left[ \frac{3}{64} \cdot \frac{t^3}{3} \right]_0^x = \frac{x^3}{64}$$
Maka nilai untuk $F(2)$ adalah:
$$F(2) = \frac{2^3}{64} = \frac{8}{64} = \frac{1}{8}$$
Jadi, nilai $F(2)$ adalah $\frac{1}{8}$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b04-e-medium-bt01-008
*orisinal | C4 | 3 langkah | jenis: menentukan nilai konstanta dan peluang integral*

Suatu variabel acak kontinu $X$ memiliki fungsi densitas peluang:
$$f(x) = \begin{cases} c(4-x), & 0 \le x \le 4 \\ 0, & x \text{ lainnya} \end{cases}$$
Nilai dari $P(1 \le X \le 3)$ adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: Salah menghitung nilai $c = 1/16$, sehingga nilai peluang menjadi setengah dari yang seharusnya.</sub>
- B. $\frac{3}{8}$  
  <sub>Salah: Keliru pada batas pengintegralan, menghitung dari $x=2$ sampai $x=4$.</sub>
- C. $\frac{5}{8}$  
  <sub>Salah: Salah dalam substitusi batas bawah $x=1$ saat menghitung $[4(1) - 1/2] = 3,5$ dihitung sebagai $2,5$.</sub>
- **D. $\frac{1}{2}$** ✅  
  <sub>Benar: Total luas $\int_0^4 c(4-x)\,dx = c[4x - x^2/2]_0^4 = 8c = 1 \implies c = 1/8$. Maka $P(1 \le X \le 3) = \int_1^3 \frac{1}{8}(4-x)\,dx = \frac{1}{8}[4x - x^2/2]_1^3 = \frac{1}{8}(7,5 - 3,5) = \frac{4}{8} = \frac{1}{2}$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai konstanta $c$.
Karena total luas di bawah kurva densitas peluang harus sama dengan 1:
$$\int_{-\infty}^{\infty} f(x)\,dx = 1$$
$$\int_{0}^{4} c(4-x)\,dx = 1$$
$$c \left[ 4x - \frac{x^2}{2} \right]_0^4 = 1$$
$$c \left( 16 - 8 \right) = 1 \implies 8c = 1 \implies c = \frac{1}{8}$$

Langkah 2: Menghitung $P(1 \le X \le 3)$.
$$P(1 \le X \le 3) = \int_{1}^{3} \frac{1}{8}(4-x)\,dx$$
$$P(1 \le X \le 3) = \frac{1}{8} \left[ 4x - \frac{x^2}{2} \right]_1^3$$
$$P(1 \le X \le 3) = \frac{1}{8} \left( \left( 12 - \frac{9}{2} \right) - \left( 4 - \frac{1}{2} \right) \right)$$
$$P(1 \le X \le 3) = \frac{1}{8} \left( \frac{15}{2} - \frac{7}{2} \right) = \frac{1}{8} (4) = \frac{1}{2}$$
Jadi, nilai dari $P(1 \le X \le 3)$ adalah $\frac{1}{2}$.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b04-e-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: menghitung peluang dari fungsi densitas linear*

Suatu variabel acak kontinu $X$, untuk nilai-nilai di antara $x=6$ dan $x=10$, dinyatakan dengan fungsi densitas peluang $f(x)=\frac{x-6}{8}$, dan bernilai $0$ untuk nilai $x$ lainnya. Tentukan nilai dari $P(X<8)$.

- A. 0,125  
  <sub>Salah: Siswa lupa mengalikan penyebut 8 dengan pangkat integrasi 2, sehingga membagi dengan 8 bukan 16.</sub>
- **B. 0,25** ✅  
  <sub>Benar: P(X < 8) dihitung dengan mengintegralkan fungsi f(x) dari 6 hingga 8, menghasilkan [ (x - 6)^2 / 16 ] dari 6 ke 8 = 4/16 = 0,25.</sub>
- C. 0,50  
  <sub>Salah: Siswa salah mengira titik x = 8 adalah median sehingga langsung membagi peluang menjadi setengah.</sub>
- D. 0,75  
  <sub>Salah: Siswa menghitung P(X > 8) bukan P(X < 8).</sub>

**Pembahasan:** Peluang variabel acak kontinu $X < 8$ ditentukan melalui integral tentu fungsi densitas peluangnya:
$$P(X < 8) = \int_{6}^{8} \frac{x-6}{8}\,dx$$
Misalkan $u = x - 6$, maka $du = dx$. Untuk $x = 6$, $u = 0$, dan untuk $x = 8$, $u = 2$:
$$P(X < 8) = \int_{0}^{2} \frac{u}{8}\,du = \left[ \frac{u^2}{16} \right]_{0}^{2} = \frac{2^2}{16} - 0 = \frac{4}{16} = \frac{1}{4} = 0,25$$
Jadi, nilai dari $P(X < 8)$ adalah $0,25$.
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b04-e-medium-bt01-010
*variasi (konteks) | C3 | 2 langkah | jenis: menghitung peluang durasi waktu seragam*

Uji ketahanan baterai suatu gawai dilakukan paling lama 10 jam. Durasi pengujian dinyatakan oleh variabel acak kontinu $T$ (dalam jam) dengan fungsi densitas peluang seragam $f(t) = \frac{1}{10}$ untuk $0 \le t \le 10$, dan $f(t) = 0$ untuk nilai lainnya. Berapa peluang uji ketahanan berlangsung selama 7 jam atau lebih?

- A. $\frac{1}{5}$  
  <sub>Salah: Siswa salah menghitung selang waktu integral menjadi 10 - 8 = 2 jam sehingga menghasilkan 2/10 = 1/5.</sub>
- B. $\frac{2}{5}$  
  <sub>Salah: Siswa menjumlahkan batas 7 dan 10 lalu keliru menentukan selang.</sub>
- **C. $\frac{3}{10}$** ✅  
  <sub>Benar: P(T >= 7) adalah integral f(t) dari 7 hingga 10, yaitu (10 - 7)/10 = 3/10.</sub>
- D. $\frac{7}{10}$  
  <sub>Salah: Siswa menghitung P(T <= 7) alih-alih durasi 7 jam atau lebih.</sub>

**Pembahasan:** Peluang pengujian berlangsung selama 7 jam atau lebih dinyatakan oleh $P(T \ge 7)$:
$$P(T \ge 7) = \int_{7}^{10} f(t)\,dt = \int_{7}^{10} \frac{1}{10}\,dt = \left[ \frac{t}{10} \right]_{7}^{10} = \frac{10 - 7}{10} = \frac{3}{10}$$
Jadi, peluang uji ketahanan berlangsung selama 7 jam atau lebih adalah $\frac{3}{10}$.
**Acuan:** siswa — siswa hal.267 Contoh Soal 4.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b04-e-medium-bt01-011
*variasi (angka) | C3 | 2 langkah | jenis: menghitung peluang interval waktu operasional*

Dalam masa pemeliharaan sistem, suatu server lokal hanya beroperasi selama 200 menit, yaitu mulai pukul 07.00 hingga pukul 10.20. Pengguna hanya dapat mengakses server pada rentang waktu operasional tersebut. Misalkan $X$ adalah variabel acak yang menyatakan waktu akses pengguna terhubung (dalam menit sejak server dibuka). Fungsi densitas peluang $X$ dinyatakan dengan:
$$f(x)=\begin{cases}\frac{1}{200}, & 0 \le x \le 200\\ 0, & x<0 \text{ atau } x>200\end{cases}$$
Berapakah peluang seorang pengguna terhubung ke server pada rentang waktu antara 40 dan 160 menit?

- A. $\frac{2}{5}$  
  <sub>Salah: Siswa menghitung peluang di luar rentang waktu tersebut (komplemennya) yaitu (40 + 40)/200 = 80/200 = 2/5.</sub>
- B. $\frac{1}{5}$  
  <sub>Salah: Siswa hanya menggunakan batas bawah 40/200 = 1/5.</sub>
- **C. $\frac{3}{5}$** ✅  
  <sub>Benar: P(40 <= X <= 160) = (160 - 40) / 200 = 120 / 200 = 3/5.</sub>
- D. $\frac{4}{5}$  
  <sub>Salah: Siswa hanya menggunakan batas atas 160/200 = 4/5.</sub>

**Pembahasan:** Peluang pengguna terhubung pada rentang waktu 40 hingga 160 menit dihitung menggunakan integral fungsi densitas peluang:
$$P(40 \le X \le 160) = \int_{40}^{160} f(x)\,dx = \int_{40}^{160} \frac{1}{200}\,dx = \left[ \frac{x}{200} \right]_{40}^{160} = \frac{160 - 40}{200} = \frac{120}{200} = \frac{3}{5}$$
Jadi, peluangnya adalah $\frac{3}{5}$.
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-1b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b04-e-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: menghitung peluang dari kurva parabola*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang sebagai berikut:
$$f(x) = \begin{cases} \frac{3}{32}(4x - x^2), & 0 \le x \le 4 \\ 0, & x \text{ lainnya} \end{cases}$$
Tentukan nilai peluang $P(1 \le X \le 3)$.

- A. $\frac{7}{16}$  
  <sub>Salah: Siswa salah mengevaluasi batas bawah x = 1.</sub>
- **B. $\frac{11}{16}$** ✅  
  <sub>Benar: Integral f(x) dari 1 hingga 3 menghasilkan (3/32) * [2x^2 - x^3/3] dari 1 ke 3 = (3/32) * (22/3) = 11/16.</sub>
- C. $\frac{9}{16}$  
  <sub>Salah: Siswa salah mengintegrasikan 4x menjadi 4x^2 bukan 2x^2.</sub>
- D. $\frac{5}{16}$  
  <sub>Salah: Siswa menghitung nilai peluang komplemennya yaitu 1 - 11/16 = 5/16.</sub>

**Pembahasan:** Peluang $P(1 \le X \le 3)$ dihitung dengan integral tentu:
$$P(1 \le X \le 3) = \int_{1}^{3} \frac{3}{32}(4x - x^2)\,dx$$
Hitung antiturunan dari fungsinya:
$$\int (4x - x^2)\,dx = 2x^2 - \frac{x^3}{3}$$
Evaluasi batas dari 1 hingga 3:
Untuk $x = 3$: $2(3)^2 - \frac{3^3}{3} = 18 - 9 = 9$
Untuk $x = 1$: $2(1)^2 - \frac{1^3}{3} = 2 - \frac{1}{3} = \frac{5}{3}$
Selisih nilai evaluasi:
$$9 - \frac{5}{3} = \frac{22}{3}$$
Kalikan dengan konstanta $\frac{3}{32}$:
$$P(1 \le X \le 3) = \frac{3}{32} \times \frac{22}{3} = \frac{22}{32} = \frac{11}{16}$$
Jadi, nilai peluangnya adalah $\frac{11}{16}$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b04-e-medium-bt01-013
*orisinal | C3 | 2 langkah | jenis: menghitung peluang dari fungsi kumulatif*

Fungsi distribusi kumulatif dari suatu variabel acak kontinu $X$ didefinisikan sebagai:
$$F(x) = \begin{cases} 0, & x < 0 \\ \frac{x^2 + 2x}{8}, & 0 \le x \le 2 \\ 1, & x > 2 \end{cases}$$
Tentukan nilai dari $P(X \ge 1)$.

- A. $\frac{1}{4}$  
  <sub>Salah: Siswa hanya menghitung x^2/8 untuk x=1 atau keliru dalam operasi pecahan.</sub>
- **B. $\frac{5}{8}$** ✅  
  <sub>Benar: P(X >= 1) = 1 - F(1) = 1 - (1^2 + 2(1))/8 = 1 - 3/8 = 5/8.</sub>
- C. $\frac{3}{8}$  
  <sub>Salah: Siswa menghitung nilai F(1) yaitu P(X <= 1) tanpa mengurangkannya dari 1.</sub>
- D. $\frac{7}{8}$  
  <sub>Salah: Siswa lupa memperhitungkan suku 2x pada pembilang F(x).</sub>

**Pembahasan:** Berdasarkan definisi fungsi distribusi kumulatif, peluang variabel acak kontinu bernilai $X \ge 1$ adalah komplemen dari $F(1)$:
$$P(X \ge 1) = 1 - P(X < 1) = 1 - F(1)$$
Substitusikan $x = 1$ ke dalam rumus $F(x)$:
$$F(1) = \frac{1^2 + 2(1)}{8} = \frac{1 + 2}{8} = \frac{3}{8}$$
Maka diperoleh:
$$P(X \ge 1) = 1 - \frac{3}{8} = \frac{5}{8}$$
Jadi, nilai dari $P(X \ge 1)$ adalah $\frac{5}{8}$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b04-e-medium-bt01-014
*variasi (angka) | C3 | 2 langkah | jenis: menghitung peluang interval waktu operasional*

Dalam masa pembatasan jam operasional, suatu apotek hanya beroperasi selama 250 menit, yaitu mulai pukul 08.00 hingga pukul 12.10. Pembeli tidak diperbolehkan berada di dalam apotek tersebut sebelum pukul 08.00 dan harus meninggalkan apotek paling lambat pukul 12.10. Misalkan $X$ adalah variabel acak yang menyatakan lama pembeli berada di dalam apotek (dalam menit). Fungsi densitas peluang $X$ dinyatakan dengan:
$$f(x)=\begin{cases}\frac{1}{250}, & 0 \le x \le 250\\ 0, & x<0 \text{ atau } x>250\end{cases}$$
Berapakah peluang seorang pembeli berada di apotek pada rentang waktu antara 45 dan 120 menit?

- **A. $\frac{3}{10}$** ✅  
  <sub>Benar: $P(45 \le X \le 120) = \int_{45}^{120} \frac{1}{250}\,dx = \frac{120 - 45}{250} = \frac{75}{250} = \frac{3}{10}$.</sub>
- B. $\frac{9}{25}$  
  <sub>Salah: Hanya menghitung batas atas $x = 90$ atau salah hitung selisih batas menjadi $90$.</sub>
- C. $\frac{7}{20}$  
  <sub>Salah: Salah membaca selang batas bawah menjadi $32,5$ atau salah menyederhanakan pecahan.</sub>
- D. $\frac{1}{5}$  
  <sub>Salah: Mengurangkan nilai salah $120 - 70 = 50$, menghasilkan $\frac{50}{250} = \frac{1}{5}$.</sub>

**Pembahasan:** Peluang variabel acak kontinu $X$ pada selang $45 \le x \le 120$ dihitung dengan mengintegralkan fungsi densitas peluangnya:
$$P(45 \le X \le 120) = \int_{45}^{120} f(x)\,dx = \int_{45}^{120} \frac{1}{250}\,dx$$
$$P(45 \le X \le 120) = \left[ \frac{x}{250} \right]_{45}^{120} = \frac{120 - 45}{250} = \frac{75}{250} = \frac{3}{10}$$
Jadi, peluangnya adalah $\frac{3}{10}$.
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b04-e-medium-bt01-015
*variasi (angka) | C3 | 2 langkah | jenis: menghitung peluang interval waktu operasional*

Dalam masa perbaikan fasilitas, suatu perpustakaan daerah hanya beroperasi selama 240 menit, yaitu mulai pukul 09.00 hingga pukul 13.00. Pengunjung tidak diperbolehkan berada di dalam perpustakaan sebelum pukul 09.00 dan harus meninggalkan gedung paling lambat pukul 13.00. Misalkan $X$ adalah variabel acak yang menyatakan lama pengunjung berada di dalam perpustakaan (dalam menit). Fungsi densitas peluang $X$ dinyatakan dengan:
$$f(x)=\begin{cases}\frac{1}{240}, & 0 \le x \le 240\\ 0, & x<0 \text{ atau } x>240\end{cases}$$
Berapakah peluang seorang pengunjung berada di perpustakaan pada rentang waktu antara 30 dan 110 menit?

- A. $\frac{1}{4}$  
  <sub>Salah: Memakai jawaban acuan asli atau salah menghitung selisih menjadi $60$ menit.</sub>
- B. $\frac{7}{24}$  
  <sub>Salah: Salah mengurangkan batas $110 - 40 = 70$, menghasilkan $\frac{70}{240} = \frac{7}{24}$.</sub>
- **C. $\frac{1}{3}$** ✅  
  <sub>Benar: $P(30 \le X \le 110) = \int_{30}^{110} \frac{1}{240}\,dx = \frac{110 - 30}{240} = \frac{80}{240} = \frac{1}{3}$.</sub>
- D. $\frac{5}{12}$  
  <sub>Salah: Salah menghitung selisih batas menjadi $100$, menghasilkan $\frac{100}{240} = \frac{5}{12}$.</sub>

**Pembahasan:** Peluang bahwa pengunjung berada di perpustakaan antara 30 dan 110 menit diperoleh melalui integral:
$$P(30 \le X \le 110) = \int_{30}^{110} \frac{1}{240}\,dx = \left[ \frac{x}{240} \right]_{30}^{110} = \frac{110 - 30}{240} = \frac{80}{240} = \frac{1}{3}$$
Jadi, peluangnya adalah $\frac{1}{3}$.
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-1b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b04-e-medium-bt01-016
*variasi (konteks) | C3 | 2 langkah | jenis: menghitung peluang durasi seragam*

Seorang atlet panahan berlatih memanah selama 2 jam setiap pagi, dari pukul 07.00—09.00. Ia mencatat durasi fokus membidik sebelum melepaskan anak panah setiap sesi dalam satuan detik. Berdasarkan catatan, durasi fokus tersebut tersebar merata dari 10 detik hingga 50 detik. Misalkan $X$ adalah variabel acak kontinu yang menyatakan durasi fokus membidik (dalam detik). Peluang atlet tersebut fokus membidik dalam rentang waktu dari 18 detik hingga 42 detik adalah ....

- A. $\frac{9}{20}$  
  <sub>Salah: Hanya menghitung rasio batas bawah target terhadap panjang selang: $\frac{18}{40} = \frac{9}{20}$.</sub>
- B. $\frac{12}{25}$  
  <sub>Salah: Menggunakan batas atas 50 detik sebagai penyebut langsung tanpa dikurangi batas bawah: $\frac{42 - 18}{50} = \frac{24}{50} = \frac{12}{25}$.</sub>
- **C. $\frac{3}{5}$** ✅  
  <sub>Benar: Karena $X$ tersebar seragam pada $[10, 50]$, fungsi densitasnya adalah $f(x) = \frac{1}{50 - 10} = \frac{1}{40}$ untuk $10 \le x \le 50$. Peluangnya adalah $P(18 \le X \le 42) = \int_{18}^{42} \frac{1}{40}\,dx = \frac{42 - 18}{40} = \frac{24}{40} = \frac{3}{5}$.</sub>
- D. $\frac{4}{5}$  
  <sub>Salah: Menghitung selisih dari batas bawah interval asal: $\frac{42 - 10}{40} = \frac{32}{40} = \frac{4}{5}$.</sub>

**Pembahasan:** Variabel acak kontinu $X$ tersebar merata dari $a = 10$ hingga $b = 50$, sehingga fungsi densitas peluangnya:
$$f(x) = \begin{cases} \frac{1}{50 - 10} = \frac{1}{40}, & 10 \le x \le 50 \\ 0, & x \text{ lainnya} \end{cases}$$

Peluang fokus membidik antara 18 hingga 42 detik adalah:
$$P(18 \le X \le 42) = \int_{18}^{42} \frac{1}{40}\,dx = \left[ \frac{x}{40} \right]_{18}^{42} = \frac{42 - 18}{40} = \frac{24}{40} = \frac{3}{5}$$

Jadi, peluangnya adalah $\frac{3}{5}$.
**Acuan:** siswa — siswa hal.268 Ayo Mencoba 4.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b04-e-medium-bt01-017
*variasi (konteks) | C3 | 2 langkah | jenis: menghitung peluang durasi seragam*

Seorang pianis melakukan latihan teknik setiap malam selama 2 jam, dari pukul 19.00—21.00. Ia mencatat durasi pemanasan jari setiap sesi latihan dalam satuan menit. Berdasarkan pengamatan, durasi pemanasan tersebut berdistribusi merata dari 15 menit hingga 45 menit. Jika $X$ menyatakan variabel acak kontinu untuk durasi pemanasan jari (dalam menit), peluang pianis tersebut melakukan pemanasan dalam rentang 21 menit hingga 33 menit adalah ....

- A. $\frac{4}{15}$  
  <sub>Salah: Membagi panjang selang target dengan batas atas 45: $\frac{12}{45} = \frac{4}{15}$.</sub>
- **B. $\frac{2}{5}$** ✅  
  <sub>Benar: Fungsi densitas peluang $X$ adalah $f(x) = \frac{1}{45 - 15} = \frac{1}{30}$ untuk $15 \le x \le 45$. Maka $P(21 \le X \le 33) = \frac{33 - 21}{30} = \frac{12}{30} = \frac{2}{5}$.</sub>
- C. $\frac{1}{3}$  
  <sub>Salah: Salah melakukan pengurangan batas $33 - 21 = 10$, menghasilkan $\frac{10}{30} = \frac{1}{3}$.</sub>
- D. $\frac{7}{15}$  
  <sub>Salah: Menghitung rasio batas bawah target terhadap batas atas interval: $\frac{21}{45} = \frac{7}{15}$.</sub>

**Pembahasan:** Variabel acak kontinu $X$ terdistribusi merata pada rentang $[15, 45]$. Panjang interval adalah $45 - 15 = 30$, sehingga fungsi densitas peluangnya:
$$f(x) = \begin{cases} \frac{1}{30}, & 15 \le x \le 45 \\ 0, & x \text{ lainnya} \end{cases}$$

Peluang durasi pemanasan berada dalam rentang 21 hingga 33 menit:
$$P(21 \le X \le 33) = \int_{21}^{33} \frac{1}{30}\,dx = \frac{33 - 21}{30} = \frac{12}{30} = \frac{2}{5}$$

Jadi, peluangnya adalah $\frac{2}{5}$.
**Acuan:** siswa — siswa hal.268 Ayo Mencoba 4.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b04-e-medium-bt01-018
*orisinal | C3 | 2 langkah | jenis: menghitung peluang dari kurva pangkat tiga*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang yang dinyatakan oleh:
$$f(x) = \begin{cases} \frac{1}{4}x^3, & 0 \le x \le 2 \\ 0, & x \text{ lainnya} \end{cases}$$
Nilai peluang $P(1 \le X \le 2)$ adalah ....

- A. $\frac{7}{16}$  
  <sub>Salah: Salah menghitung $2^4 - 1^4$ sebagai $8 - 1 = 7$, sehingga mendapatkan $\frac{7}{16}$.</sub>
- B. $\frac{1}{16}$  
  <sub>Salah: Hanya menghitung nilai integral dari 0 sampai 1, yaitu komplemen yang salah dievaluasi: $P(0 \le X \le 1) = \frac{1}{16}$.</sub>
- C. $\frac{7}{8}$  
  <sub>Salah: Salah melakukan integrasi menjadi $\frac{x^3}{8}$, lalu menghitung $\frac{8 - 1}{8} = \frac{7}{8}$.</sub>
- **D. $\frac{15}{16}$** ✅  
  <sub>Benar: $P(1 \le X \le 2) = \int_1^2 \frac{1}{4}x^3\,dx = \left[ \frac{x^4}{16} \right]_1^2 = \frac{16 - 1}{16} = \frac{15}{16}$.</sub>

**Pembahasan:** Berdasarkan definisi peluang variabel acak kontinu, peluang pada selang $[1, 2]$ dihitung dengan integral fungsi densitas:
$$P(1 \le X \le 2) = \int_{1}^{2} \frac{1}{4}x^3\,dx$$

Menghitung integral tentu:
$$\int_{1}^{2} \frac{1}{4}x^3\,dx = \left[ \frac{1}{4} \cdot \frac{x^4}{4} \right]_{1}^{2} = \left[ \frac{x^4}{16} \right]_{1}^{2} = \frac{2^4}{16} - \frac{1^4}{16} = \frac{16 - 1}{16} = \frac{15}{16}$$

Jadi, nilai dari $P(1 \le X \le 2)$ adalah $\frac{15}{16}$.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b04-e-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: menghitung peluang densitas linear*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang yang didefinisikan sebagai:
$$f(x) = \begin{cases} 2 - 2x, & 0 \le x \le 1 \\ 0, & x \text{ lainnya} \end{cases}$$
Nilai dari $P\left(X \le \frac{1}{2}\right)$ adalah ....

- A. $\frac{1}{2}$  
  <sub>Salah: Siswa mengabaikan kemiringan fungsi densitas dan mengasumsikan distribusi seragam sehingga membagi rentang sama rata.</sub>
- B. $\frac{3}{8}$  
  <sub>Salah: Siswa keliru saat melakukan integrasi antiturunan fungsi menjadi $x - x^2$ alih-alih $2x - x^2$.</sub>
- **C. $\frac{3}{4}$** ✅  
  <sub>Benar: $P(X \le 1/2) = \int_0^{1/2} (2 - 2x)\,dx = \left[2x - x^2\right]_0^{1/2} = 2\left(\frac{1}{2}\right) - \left(\frac{1}{2}\right)^2 = 1 - \frac{1}{4} = \frac{3}{4}$.</sub>
- D. $\frac{1}{4}$  
  <sub>Salah: Siswa menghitung peluang komplemennya $P(X > 1/2)$ atau salah dalam pengurangan batas evaluasi.</sub>

**Pembahasan:** Peluang variabel acak kontinu pada selang $0 \le X \le \frac{1}{2}$ dihitung dengan mengintegralkan fungsi densitas peluangnya:
$$P\left(X \le \frac{1}{2}\right) = \int_{0}^{\frac{1}{2}} (2 - 2x)\,dx$$
Antiturunan dari $2 - 2x$ adalah $2x - x^2$. Evaluasi pada batas $[0, \frac{1}{2}]$:
$$\left[ 2x - x^2 \right]_{0}^{\frac{1}{2}} = \left(2\left(\frac{1}{2}\right) - \left(\frac{1}{2}\right)^2\right) - (0) = 1 - \frac{1}{4} = \frac{3}{4}$$
Jadi, nilai dari $P\left(X \le \frac{1}{2}\right)$ adalah $\frac{3}{4}$.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b04-e-medium-bt01-020
*orisinal | C3 | 2 langkah | jenis: menentukan rumus distribusi kumulatif*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang sebagai berikut:
$$f(x) = \begin{cases} \frac{1}{9}x^2, & 0 \le x \le 3 \\ 0, & x \text{ lainnya} \end{cases}$$
Untuk interval $0 \le x \le 3$, fungsi distribusi kumulatif $F(x)$ dinyatakan oleh ....

- **A. $\frac{x^3}{27}$** ✅  
  <sub>Benar: $F(x) = \int_0^x f(t)\,dt = \int_0^x \frac{1}{9}t^2\,dt = \left[\frac{t^3}{27}\right]_0^x = \frac{x^3}{27}$.</sub>
- B. $\frac{x^2}{9}$  
  <sub>Salah: Siswa tidak melakukan integrasi dan menyamakan fungsi distribusi kumulatif dengan fungsi densitas peluang.</sub>
- C. $\frac{2x}{9}$  
  <sub>Salah: Siswa menurunkan fungsi densitas peluang alih-alih mengintegralkannya.</sub>
- D. $\frac{x^3}{9}$  
  <sub>Salah: Siswa melakukan integrasi variabel $x$ menjadi $x^3$ tetapi lupa membagi koefisien dengan pangkat baru 3.</sub>

**Pembahasan:** Fungsi distribusi kumulatif $F(x)$ diperoleh dari integral fungsi densitas peluang $f(t)$ dari batas bawah hingga $x$:
$$F(x) = \int_{0}^{x} f(t)\,dt$$
Untuk selang $0 \le x \le 3$:
$$F(x) = \int_{0}^{x} \frac{1}{9}t^2\,dt = \left[ \frac{t^3}{27} \right]_{0}^{x} = \frac{x^3}{27} - 0 = \frac{x^3}{27}$$
Jadi, untuk $0 \le x \le 3$, fungsi distribusi kumulatifnya adalah $F(x) = \frac{x^3}{27}$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b04-e-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: penentuan batas peluang*

Suatu variabel acak kontinu $X$, untuk nilai-nilai di antara $x=1$ dan $x=6$, didefinisikan dengan fungsi densitas peluang $f(x)=\frac{2x+1}{40}$, dan bernilai $0$ untuk nilai $x$ lainnya. Jika diketahui $P(X \ge k) = \frac{11}{20}$, nilai batas $k$ yang memenuhi adalah ....

- A. $5$  
  <sub>Salah: Siswa salah dalam mengintegralkan $2x$ menjadi $2x^2$ alih-alih $x^2$ sehingga mendapatkan nilai akar yang keliru.</sub>
- B. $2$  
  <sub>Salah: Siswa lupa mengikutsertakan suku $+x$ dari integral konstanta $1$, hanya menyelesaikan $36 - k^2 = 22$ lalu membulatkan.</sub>
- C. $3$  
  <sub>Salah: Siswa salah menggunakan rumus peluang kumulatif $P(X \le k) = \frac{11}{20}$, bukan $P(X \ge k)$.</sub>
- **D. $4$** ✅  
  <sub>Benar: Peluang dihitung melalui integral: $P(X \ge k) = \int_{k}^{6} \frac{2x+1}{40}\,dx = \left[ \frac{x^2+x}{40} \right]_k^6 = \frac{42 - (k^2+k)}{40}$. Diketahui nilai peluang ini adalah $\frac{11}{20} = \frac{22}{40}$, sehingga $42 - (k^2+k) = 22 \iff k^2 + k - 20 = 0$. Faktorisasi menghasilkan $(k+5)(k-4) = 0$. Karena $1 \le k \le 6$, nilai yang memenuhi adalah $k = 4$.</sub>

**Pembahasan:** Diketahui fungsi densitas $f(x) = \frac{2x+1}{40}$ untuk $1 \le x \le 6$.

Langkah 1: Tuliskan bentuk integral untuk $P(X \ge k)$:
$$P(X \ge k) = \int_{k}^{6} \frac{2x+1}{40}\,dx$$

Langkah 2: Hitung antiturunan:
$$\int_{k}^{6} \frac{2x+1}{40}\,dx = \left[ \frac{x^2+x}{40} \right]_k^6 = \frac{(6^2+6) - (k^2+k)}{40} = \frac{42 - (k^2+k)}{40}$$

Langkah 3: Samakan dengan nilai peluang yang diketahui:
$$\frac{42 - (k^2+k)}{40} = \frac{11}{20} = \frac{22}{40}$$
$$42 - (k^2+k) = 22$$
$$k^2 + k - 20 = 0$$

Langkah 4: Faktorkan persamaan kuadrat:
$$(k+5)(k-4) = 0$$
Diperoleh $k = -5$ atau $k = 4$. Karena selang definisi adalah $1 \le x \le 6$, maka nilai $k$ yang memenuhi adalah $4$.
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b04-e-hard-bt01-002
*variasi (konteks) | C5 | 4 langkah | jenis: peluang bersyarat kontinu*

Seorang teknisi menguji ketahanan baterai gawai dalam rentang waktu 60 menit hingga 240 menit. Misalkan $T$ adalah variabel acak kontinu yang menyatakan durasi waktu layar menyala (dalam menit) dengan fungsi densitas peluang:
$$f(t) = \begin{cases} \frac{1}{180}, & 60 \le t \le 240 \\ 0, & t < 60 \text{ atau } t > 240 \end{cases}$$
Jika diketahui gawai tersebut telah menyala selama minimal 120 menit, peluang bahwa gawai tersebut mati sebelum mencapai 180 menit adalah ....

- A. $\frac{2}{3}$  
  <sub>Salah: Siswa menghitung nilai penyebut $P(T \ge 120)$ saja alih-alih nilai rasio peluang bersyarat.</sub>
- B. $\frac{1}{3}$  
  <sub>Salah: Siswa hanya menghitung peluang tanpa syarat $P(120 \le T \le 180)$ tanpa membaginya dengan ruang sampel bersyarat $P(T \ge 120)$.</sub>
- C. $\frac{1}{4}$  
  <sub>Salah: Siswa salah menghitung panjang selang pembilang sebagai $180 - 135 = 45$ sehingga mendapatkan $\frac{45}{180} = \frac{1}{4}$.</sub>
- **D. $\frac{1}{2}$** ✅  
  <sub>Benar: Peluang bersyarat dihitung dengan $P(T \le 180 \mid T \ge 120) = \frac{P(120 \le T \le 180)}{P(T \ge 120)}$. Nilai $P(120 \le T \le 180) = \frac{180-120}{180} = \frac{60}{180} = \frac{1}{3}$, dan $P(T \ge 120) = \frac{240-120}{180} = \frac{120}{180} = \frac{2}{3}$. Hasil pembagiannya adalah $\frac{1/3}{2/3} = \frac{1}{2}$.</sub>

**Pembahasan:** Masalah ini merupakan penentuan peluang bersyarat pada variabel acak kontinu: $P(T \le 180 \mid T \ge 120)$.

Langkah 1: Gunakan definisi peluang bersyarat:
$$P(T \le 180 \mid T \ge 120) = \frac{P(120 \le T \le 180)}{P(T \ge 120)}$$

Langkah 2: Hitung peluang pembilang:
$$P(120 \le T \le 180) = \int_{120}^{180} \frac{1}{180}\,dt = \frac{180 - 120}{180} = \frac{60}{180} = \frac{1}{3}$$

Langkah 3: Hitung peluang penyebut (kondisi yang diketahui):
$$P(T \ge 120) = \int_{120}^{240} \frac{1}{180}\,dt = \frac{240 - 120}{180} = \frac{120}{180} = \frac{2}{3}$$

Langkah 4: Hitung nilai peluang bersyarat:
$$P(T \le 180 \mid T \ge 120) = \frac{\frac{1}{3}}{\frac{2}{3}} = \frac{1}{2}$$
**Acuan:** siswa — siswa hal.268 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b04-e-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: kontinuitas dan fungsi densitas*

Suatu variabel acak kontinu $X$ memiliki fungsi peluang sepotong yang didefinisikan sebagai:
$$f(x) = \begin{cases} ax, & 0 \le x < 2 \\ b, & 2 \le x \le 4 \\ 0, & x \text{ lainnya} \end{cases}$$
Agar fungsi $f(x)$ kontinu pada interval $[0, 4]$ dan merupakan fungsi densitas peluang yang sah, nilai dari $P(1 \le X \le 3)$ adalah ....

- A. $\frac{1}{2}$  
  <sub>Salah: Siswa langsung mengasumsikan nilai tengah interval $[1, 3]$ dari total interval berpanjang 4 sehingga menduga peluangnya $\frac{2}{4} = \frac{1}{2}$.</sub>
- B. $\frac{5}{12}$  
  <sub>Salah: Siswa salah saat mengintegralkan $\frac{1}{6}x$ menjadi $\frac{1}{6}x^2$ alih-alih $\frac{1}{12}x^2$, lalu menjumlahkannya dengan nilai konstanta.</sub>
- **C. $\frac{7}{12}$** ✅  
  <sub>Benar: Syarat kontinuitas di $x=2$: $\lim_{x \to 2^-} ax = a(2) = 2a$ harus sama dengan $b$, maka $b = 2a$. Syarat luas total = 1: $\int_0^2 ax\,dx + \int_2^4 b\,dx = [\frac{a x^2}{2}]_0^2 + 2b = 2a + 2b = 1$. Substitusi $b=2a$ menghasilkan $2a + 4a = 6a = 1 \Rightarrow a = \frac{1}{6}$ dan $b = \frac{1}{3}$. Nilai $P(1 \le X \le 3) = \int_1^2 \frac{1}{6}x\,dx + \int_2^3 \frac{1}{3}\,dx = [\frac{x^2}{12}]_1^2 + \frac{1}{3} = (\frac{4}{12} - \frac{1}{12}) + \frac{1}{3} = \frac{3}{12} + \frac{4}{12} = \frac{7}{12}$.</sub>
- D. $\frac{2}{3}$  
  <sub>Salah: Siswa lupa memotong integral di $x=2$ dan langsung menggunakan $f(x) = b = \frac{1}{3}$ untuk seluruh selang $[1, 3]$.</sub>

**Pembahasan:** Langkah 1: Terapkan syarat kekontinuan fungsi di titik perbatasan $x = 2$:
$$\lim_{x \to 2^-} ax = f(2) \implies 2a = b$$

Langkah 2: Terapkan syarat fungsi densitas peluang, yaitu integral total sama dengan 1:
$$\int_{0}^{4} f(x)\,dx = \int_{0}^{2} ax\,dx + \int_{2}^{4} b\,dx = 1$$
$$\left[ \frac{a x^2}{2} \right]_0^2 + [bx]_2^4 = 1$$
$$(2a - 0) + (4b - 2b) = 1 \implies 2a + 2b = 1$$

Langkah 3: Selesaikan sistem persamaan dengan mensubstitusi $b = 2a$:
$$2a + 2(2a) = 1 \implies 6a = 1 \implies a = \frac{1}{6}$$
$$b = 2\left(\frac{1}{6}\right) = \frac{1}{3}$$

Langkah 4: Hitung peluang $P(1 \le X \le 3)$ dengan memecah integral pada titik batas $x = 2$:
$$P(1 \le X \le 3) = \int_{1}^{2} \frac{1}{6}x\,dx + \int_{2}^{3} \frac{1}{3}\,dx$$
$$= \left[ \frac{x^2}{12} \right]_1^2 + \left[ \frac{1}{3}x \right]_2^3$$
$$= \left( \frac{4}{12} - \frac{1}{12} \right) + \frac{1}{3}(3 - 2) = \frac{3}{12} + \frac{1}{3} = \frac{1}{4} + \frac{1}{3} = \frac{7}{12}$$
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b04-e-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: persentil fungsi kumulatif*

Fungsi distribusi kumulatif dari suatu variabel acak kontinu $X$ didefinisikan sebagai:
$$F(x) = \begin{cases} 0, & x < 2 \\ c(x-2)^2, & 2 \le x \le 6 \\ 1, & x > 6 \end{cases}$$
Jika diketahui $P(X > k) = \frac{7}{16}$ untuk nilai $2 \le k \le 6$, maka nilai $k$ yang memenuhi adalah ....

- A. $\sqrt{7}+2$  
  <sub>Salah: Siswa menyamakan $(k-2)^2$ langsung dengan pembilang $7$ dari peluang yang diketahui.</sub>
- B. $3$  
  <sub>Salah: Siswa keliru menyamakan $F(k) = \frac{7}{16}$ secara langsung tanpa menggunakan komplemen $1 - F(k)$.</sub>
- **C. $5$** ✅  
  <sub>Benar: Berdasarkan sifat fungsi distribusi kumulatif kontinu, $F(6) = 1 \implies c(6-2)^2 = 1 \implies 16c = 1 \implies c = \frac{1}{16}$. Hubungan peluang ekor kanan dengan fungsi kumulatif: $P(X > k) = 1 - F(k) = \frac{7}{16} \implies F(k) = \frac{9}{16}$. Dengan demikian, $\frac{1}{16}(k-2)^2 = \frac{9}{16} \implies (k-2)^2 = 9$. Karena $k \ge 2$, maka $k - 2 = 3 \implies k = 5$.</sub>
- D. $4$  
  <sub>Salah: Siswa mengabaikan perpangkatan dua pada $(k-2)^2$ dan menyelesaikan persamaan linier secara keliru.</sub>

**Pembahasan:** Langkah 1: Tentukan nilai konstanta $c$ menggunakan sifat batas atas fungsi distribusi kumulatif kontinu pada titik ujung $x = 6$:
$$F(6) = 1 \implies c(6 - 2)^2 = 1 \implies 16c = 1 \implies c = \frac{1}{16}$$
Sehingga fungsi kumulatif pada selang $2 \le x \le 6$ adalah $F(x) = \frac{(x-2)^2}{16}$.

Langkah 2: Hubungkan peluang yang diberikan dengan fungsi distribusi kumulatif:
$$P(X > k) = 1 - P(X \le k) = 1 - F(k)$$
$$1 - F(k) = \frac{7}{16} \implies F(k) = 1 - \frac{7}{16} = \frac{9}{16}$$

Langkah 3: Substitusikan $F(k)$ ke dalam rumus fungsinya:
$$\frac{(k - 2)^2}{16} = \frac{9}{16}$$
$$(k - 2)^2 = 9$$

Langkah 4: Selesaikan persamaan kuadrat untuk nilai $k$ dalam selang $[2, 6]$:
$$k - 2 = 3 \implies k = 5$$
(Akar $k - 2 = -3 \implies k = -1$ tidak memenuhi karena berada di luar selang).
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b04-e-hard-bt01-005
*orisinal | C5 | 5 langkah | jenis: peluang selang nilai mutlak*

Suatu variabel acak kontinu $X$ memiliki fungsi densitas peluang berbentuk kurva segitiga simetris:
$$f(x) = \begin{cases} c x, & 0 \le x \le 2 \\ c(4 - x), & 2 < x \le 4 \\ 0, & x \text{ lainnya} \end{cases}$$
Nilai peluang bahwa simpangan nilai $X$ terhadap nilai tengah $2$ tidak lebih dari $1$ satuan, yaitu $P(|X - 2| \le 1)$, adalah ....

- A. $\frac{7}{8}$  
  <sub>Salah: Siswa hanya mengurangkan satu segitiga ekor luar selang ($1 - \frac{1}{8} = \frac{7}{8}$), lupa bahwa ada dua ekor luar yang harus dikurangkan.</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: Siswa hanya menghitung peluang setengah bagian saja dari selang $[2, 3]$ atau membagi panjang interval $[1, 3]$ dengan 4.</sub>
- C. $\frac{5}{8}$  
  <sub>Salah: Siswa salah saat menghitung luas komplemen segitiga ekor luar atau salah menentukan nilai konstanta $c$.</sub>
- **D. $\frac{3}{4}$** ✅  
  <sub>Benar: Luas total di bawah kurva segitiga dari $x=0$ hingga $x=4$ adalah $\frac{1}{2} \times \text{alas} \times \text{tinggi} = \frac{1}{2} \times 4 \times (2c) = 4c = 1 \implies c = \frac{1}{4}$. Pertidaksamaan $|X - 2| \le 1$ ekuivalen dengan selang $-1 \le X - 2 \le 1 \iff 1 \le X \le 3$. Menggunakan komplemen luas segitiga luar pada interval $[0, 1]$ dan $[3, 4]$: untuk $x \in [0, 1]$, luas segitiga adalah $\frac{1}{2} \times 1 \times f(1) = \frac{1}{2} \times 1 \times \frac{1}{4} = \frac{1}{8}$. Karena kurva simetris, luas segitiga pada $[3, 4]$ juga $\frac{1}{8}$. Maka $P(1 \le X \le 3) = 1 - (\frac{1}{8} + \frac{1}{8}) = 1 - \frac{1}{4} = \frac{3}{4}$.</sub>

**Pembahasan:** Langkah 1: Tentukan nilai konstanta $c$ menggunakan syarat luas total fungsi densitas sama dengan 1. Karena grafiknya berbentuk segitiga dengan alas $[0, 4]$ dan puncak di $x=2$ dengan tinggi $f(2) = 2c$:
$$\text{Luas} = \frac{1}{2} \times 4 \times 2c = 4c = 1 \implies c = \frac{1}{4}$$

Langkah 2: Jabarkan pertidaksamaan nilai mutlak:
$$|X - 2| \le 1 \iff -1 \le X - 2 \le 1 \iff 1 \le X \le 3$$
Sehingga yang dicari adalah $P(1 \le X \le 3)$.

Langkah 3: Hitung peluang daerah komplemen (daerah di luar selang $[1, 3]$) untuk mempermudah:
- Bagian kiri ($0 \le x < 1$): berbentuk segitiga dengan alas $1$ dan tinggi $f(1) = \frac{1}{4}(1) = \frac{1}{4}$:
$$P(0 \le X < 1) = \frac{1}{2} \times 1 \times \frac{1}{4} = \frac{1}{8}$$
- Bagian kanan ($3 < x \le 4$): karena simetris terhadap $x=2$, luasnya sama:
$$P(3 < X \le 4) = \frac{1}{8}$$

Langkah 4: Hitung nilai peluang yang ditanyakan:
$$P(1 \le X \le 3) = 1 - [P(0 \le X < 1) + P(3 < X \le 4)] = 1 - \left( \frac{1}{8} + \frac{1}{8} \right) = 1 - \frac{1}{4} = \frac{3}{4}$$
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b04-e-hard-bt01-006
*variasi (angka) | C5 | 4 langkah | jenis: peluang selang pertidaksamaan kuadrat*

Suatu variabel acak kontinu $X$, untuk nilai-nilai di antara $x=2$ dan $x=8$, dinyatakan dengan fungsi densitas peluang $f(x)=\frac{2x+3}{78}$, dan bernilai $0$ untuk nilai $x$ lainnya. Nilai dari peluang $P(X^2 - 9X + 18 < 0)$ adalah ....

- A. $\frac{5}{13}$  
  <sub>Salah: Siswa salah mengintegralkan suku linear atau salah mensubstitusikan batas bawah sehingga pembilang menjadi $30$, menghasilkan $\frac{30}{78} = \frac{5}{13}$.</sub>
- B. $\frac{7}{13}$  
  <sub>Salah: Siswa salah melakukan pengurangan nilai batas atas dan bawah $(54 - 12 = 42)$ sehingga menghasilkan $\frac{42}{78} = \frac{7}{13}$.</sub>
- **C. $\frac{6}{13}$** ✅  
  <sub>Benar: Pertidaksamaan $X^2 - 9X + 18 < 0$ memiliki pembuat nol $x=3$ dan $x=6$, sehingga solusinya adalah $3 < X < 6$. Karena selang $(3, 6)$ berada di dalam interval definisi $[2, 8]$, peluangnya dihitung melalui integral: $P(3 < X < 6) = \int_{3}^{6} \frac{2x+3}{78}\,dx = \frac{1}{78} \left[ x^2 + 3x \right]_{3}^{6} = \frac{1}{78} \left( (36 + 18) - (9 + 9) \right) = \frac{1}{78}(54 - 18) = \frac{36}{78} = \frac{6}{13}$.</sub>
- D. $\frac{9}{26}$  
  <sub>Salah: Siswa lupa mengintegralkan suku konstanta $3$ dan hanya menghitung integral dari $2x$ saja, memperoleh $\frac{36 - 9}{78} = \frac{27}{78} = \frac{9}{26}$.</sub>

**Pembahasan:** Langkah 1: Tentukan selang nilai $X$ yang memenuhi kejadian:
$$X^2 - 9X + 18 < 0 \iff (X - 3)(X - 6) < 0 \iff 3 < X < 6$$

Langkah 2: Hitung peluang pada selang tersebut dengan integral fungsi densitas:
$$P(3 < X < 6) = \int_{3}^{6} f(x)\,dx = \int_{3}^{6} \frac{2x+3}{78}\,dx$$

Langkah 3: Tentukan antiturunan:
$$\int \frac{2x+3}{78}\,dx = \frac{1}{78}(x^2 + 3x)$$

Langkah 4: Evaluasi batas integrasi:
$$\frac{1}{78}\left[(6^2 + 3(6)) - (3^2 + 3(3))\right] = \frac{1}{78}\left[(36 + 18) - (9 + 9)\right] = \frac{1}{78}(54 - 18) = \frac{36}{78} = \frac{6}{13}$$

Jadi, peluangnya adalah $\frac{6}{13}$.
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b04-e-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: evaluasi peluang bersyarat densitas simetris*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang simetris berbentuk:
$$f(x) = \begin{cases} k(x-1), & 1 \le x < 3 \\ k(5-x), & 3 \le x \le 5 \\ 0, & x \text{ lainnya} \end{cases}$$
Nilai dari peluang bersyarat $P(X > 2 \mid X < 4)$ adalah ....

- A. $\frac{7}{8}$  
  <sub>Salah: Siswa keliru menganggap nilai yang dicari adalah probabilitas peristiwa pensyarat $P(X < 4)$.</sub>
- B. $\frac{4}{7}$  
  <sub>Salah: Siswa salah menghitung integral irisan pada selang sepotong sehingga memperoleh pembilang $\frac{1}{2}$ alih-alih $\frac{3}{4}$.</sub>
- C. $\frac{3}{4}$  
  <sub>Salah: Siswa hanya menghitung nilai peluang irisan $P(2 < X < 4)$ dan lupa membaginya dengan probabilitas syarat $P(X < 4)$.</sub>
- **D. $\frac{6}{7}$** ✅  
  <sub>Benar: Dari syarat total peluang $\int_1^5 f(x)\,dx = 1$, diperoleh $4k = 1 \implies k = \frac{1}{4}$. Peluang $P(X < 4) = 1 - P(X \ge 4) = 1 - \int_4^5 \frac{1}{4}(5-x)\,dx = 1 - \frac{1}{8} = \frac{7}{8}$. Peluang irisan $P(2 < X < 4) = \int_2^3 \frac{1}{4}(x-1)\,dx + \int_3^4 \frac{1}{4}(5-x)\,dx = \frac{3}{8} + \frac{3}{8} = \frac{6}{8} = \frac{3}{4}$. Maka $P(X > 2 \mid X < 4) = \frac{P(2 < X < 4)}{P(X < 4)} = \frac{3/4}{7/8} = \frac{6}{7}$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai konstanta $k$ menggunakan sifat total integral kurva densitas bernilai 1:
$$\int_{1}^{3} k(x-1)\,dx + \int_{3}^{5} k(5-x)\,dx = 1$$
$$k\left[\frac{(x-1)^2}{2}\right]_1^3 + k\left[-\frac{(5-x)^2}{2}\right]_3^5 = 1 \implies 2k + 2k = 1 \implies 4k = 1 \implies k = \frac{1}{4}$$

Langkah 2: Menghitung $P(X < 4)$:
$$P(X < 4) = 1 - P(X \ge 4) = 1 - \int_{4}^{5} \frac{1}{4}(5-x)\,dx = 1 - \frac{1}{4}\left[5x - \frac{x^2}{2}\right]_4^5 = 1 - \frac{1}{8} = \frac{7}{8}$$

Langkah 3: Menghitung peluang irisan $P(2 < X < 4)$:
$$P(2 < X < 4) = \int_{2}^{3} \frac{1}{4}(x-1)\,dx + \int_{3}^{4} \frac{1}{4}(5-x)\,dx$$
$$= \frac{1}{4}\left[\frac{x^2}{2} - x\right]_2^3 + \frac{1}{4}\left[5x - \frac{x^2}{2}\right]_3^4 = \frac{3}{8} + \frac{3}{8} = \frac{3}{4}$$

Langkah 4: Menghitung peluang bersyarat:
$$P(X > 2 \mid X < 4) = \frac{P(2 < X < 4)}{P(X < 4)} = \frac{\frac{3}{4}}{\frac{7}{8}} = \frac{3}{4} \times \frac{8}{7} = \frac{6}{7}$$

Jadi, peluang bersyaratnya adalah $\frac{6}{7}$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b04-e-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: rekonstruksi nilai densitas dari fungsi kumulatif*

Fungsi distribusi kumulatif dari suatu variabel acak kontinu $X$ dinyatakan oleh:
$$F(x) = \begin{cases} 0, & x < 0 \\ ax^2 + bx, & 0 \le x \le 2 \\ 1, & x > 2 \end{cases}$$
Jika diketahui $P(X \le 1) = \frac{3}{8}$, maka nilai fungsi densitas peluang $f(x)$ pada saat $x = 1,5$ adalah ....

- **A. $\frac{5}{8}$** ✅  
  <sub>Benar: Dari sifat $F(2) = 1$, diperoleh $4a + 2b = 1$. Diketahui $F(1) = P(X \le 1) = \frac{3}{8}$, sehingga $a + b = \frac{3}{8}$. Mengalikan persamaan kedua dengan 2 menghasilkan $2a + 2b = \frac{3}{4}$. Eliminasi: $(4a+2b) - (2a+2b) = 1 - \frac{3}{4} \implies 2a = \frac{1}{4} \implies a = \frac{1}{8}$, sehingga $b = \frac{3}{8} - \frac{1}{8} = \frac{1}{4}$. Fungsi densitas $f(x) = F'(x) = 2ax + b = \frac{1}{4}x + \frac{1}{4}$. Pada $x = 1,5 = \frac{3}{2}$, nilainya adalah $f(1,5) = \frac{1}{4}\left(\frac{3}{2}\right) + \frac{1}{4} = \frac{3}{8} + \frac{2}{8} = \frac{5}{8}$.</sub>
- B. $\frac{21}{32}$  
  <sub>Salah: Siswa keliru mengevaluasi langsung ke fungsi distribusi kumulatif $F(1,5)$ alih-alih fungsi densitas $f(1,5) = F'(1,5)$.</sub>
- C. $\frac{7}{16}$  
  <sub>Salah: Siswa salah saat menurunkan fungsi kumulatif karena lupa mengikutsertakan konstanta linear $b$, hanya menghitung $2ax$ sehingga didapat $2\left(\frac{1}{8}\right)(1,5) = \frac{3}{8}$.</sub>
- D. $\frac{3}{4}$  
  <sub>Salah: Siswa melakukan kesalahan perhitungan tanda saat menyelesaikan eliminasi sistem persamaan sehingga mendapatkan $a = \frac{1}{4}$ dan $b = \frac{1}{8}$.</sub>

**Pembahasan:** Langkah 1: Gunakan sifat kumulatif batas atas $F(2) = 1$:
$$a(2)^2 + b(2) = 1 \implies 4a + 2b = 1$$

Langkah 2: Gunakan informasi nilai $P(X \le 1) = F(1) = \frac{3}{8}$:
$$a(1)^2 + b(1) = \frac{3}{8} \implies a + b = \frac{3}{8}$$

Langkah 3: Selesaikan sistem persamaan untuk mencari $a$ dan $b$:
Kalikan persamaan kedua dengan 2: $2a + 2b = \frac{3}{4}$.
Kurangkan dari persamaan pertama:
$$(4a + 2b) - (2a + 2b) = 1 - \frac{3}{4} \implies 2a = \frac{1}{4} \implies a = \frac{1}{8}$$
Maka, $b = \frac{3}{8} - \frac{1}{8} = \frac{2}{8} = \frac{1}{4}$.

Langkah 4: Tentukan fungsi densitas $f(x) = F'(x)$ pada selang $0 \le x \le 2$:
$$f(x) = \frac{d}{dx}\left(\frac{1}{8}x^2 + \frac{1}{4}x\right) = \frac{1}{4}x + \frac{1}{4}$$
Substitusikan $x = 1,5 = \frac{3}{2}$:
$$f(1,5) = \frac{1}{4}\left(\frac{3}{2}\right) + \frac{1}{4} = \frac{3}{8} + \frac{2}{8} = \frac{5}{8}$$

Jadi, nilai densitasnya adalah $\frac{5}{8}$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b04-e-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: penentuan kuartil dan peluang bersyarat*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang:
$$f(x) = \begin{cases} c(4-x), & 0 \le x \le 4 \\ 0, & x \text{ lainnya} \end{cases}$$
Jika $k$ adalah suatu konstanta yang memenuhi $P(X > k) = \frac{1}{4}$, maka nilai dari peluang bersyarat $P(X \ge 1 \mid X \le k)$ adalah ....

- A. $\frac{5}{16}$  
  <sub>Salah: Siswa hanya menghitung peluang irisan $P(1 \le X \le 2)$ dan lupa membaginya dengan probabilitas syarat $P(X \le 2)$.</sub>
- B. $\frac{7}{12}$  
  <sub>Salah: Siswa menghitung peluang komplemen $P(X < 1 \mid X \le k)$ alih-alih $P(X \ge 1 \mid X \le k)$.</sub>
- **C. $\frac{5}{12}$** ✅  
  <sub>Benar: Total luas $\int_0^4 c(4-x)\,dx = 8c = 1 \implies c = \frac{1}{8}$. Karena $P(X > k) = \frac{1}{4}$, maka $P(X \le k) = \frac{3}{4}$. Menghitung $k$: $\int_0^k \frac{1}{8}(4-x)\,dx = \frac{1}{8}(4k - \frac{k^2}{2}) = \frac{3}{4} \implies k^2 - 8k + 12 = 0$. Faktornya $(k-2)(k-6) = 0$. Karena $0 \le k \le 4$, maka $k = 2$. Peluang irisan $P(1 \le X \le 2) = \int_1^2 \frac{1}{8}(4-x)\,dx = \frac{1}{8}\left[4x - \frac{x^2}{2}\right]_1^2 = \frac{1}{8}(6 - 3,5) = \frac{2,5}{8} = \frac{5}{16}$. Peluang bersyarat $P(X \ge 1 \mid X \le 2) = \frac{P(1 \le X \le 2)}{P(X \le 2)} = \frac{5/16}{3/4} = \frac{5}{12}$.</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: Siswa salah memilih nilai batas $k$ dengan menganggap $k$ adalah nilai tengah selang (median kurva) yaitu $k=2$ didapat dari estimasi tanpa menghitung rasio luas yang tepat.</sub>

**Pembahasan:** Langkah 1: Cari nilai konstanta $c$:
$$\int_{0}^{4} c(4-x)\,dx = c\left[4x - \frac{x^2}{2}\right]_0^4 = c(16 - 8) = 8c = 1 \implies c = \frac{1}{8}$$

Langkah 2: Tentukan nilai $k$ dari $P(X > k) = \frac{1}{4} \iff P(X \le k) = \frac{3}{4}$:
$$\int_{0}^{k} \frac{1}{8}(4-x)\,dx = \frac{3}{4} \implies \frac{1}{8}\left(4k - \frac{k^2}{2}\right) = \frac{3}{4}$$
$$4k - \frac{k^2}{2} = 6 \implies 8k - k^2 = 12 \implies k^2 - 8k + 12 = 0$$
$$(k - 2)(k - 6) = 0$$
Karena nilai $X$ terdefinisi pada $[0, 4]$, maka nilai yang memenuhi adalah $k = 2$.

Langkah 3: Hitung peluang irisan $P(1 \le X \le 2)$:
$$P(1 \le X \le 2) = \int_{1}^{2} \frac{1}{8}(4-x)\,dx = \frac{1}{8}\left[4x - \frac{x^2}{2}\right]_1^2 = \frac{1}{8}\left((8 - 2) - \left(4 - \frac{1}{2}\right)\right) = \frac{1}{8}\left(6 - \frac{7}{2}\right) = \frac{5}{16}$$

Langkah 4: Hitung peluang bersyarat $P(X \ge 1 \mid X \le 2)$:
$$P(X \ge 1 \mid X \le 2) = \frac{P(1 \le X \le 2)}{P(X \le 2)} = \frac{\frac{5}{16}}{\frac{3}{4}} = \frac{5}{16} \times \frac{4}{3} = \frac{5}{12}$$

Jadi, peluang bersyarat tersebut bernilai $\frac{5}{12}$.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b04-e-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: peluang gabungan selang kejadian kontinu*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang:
$$f(x) = \begin{cases} \frac{3}{2}(1 - x^2), & 0 \le x \le 1 \\ 0, & x \text{ lainnya} \end{cases}$$
Jika peristiwa $A$ didefinisikan sebagai kejadian saat $X \le \frac{1}{2}$ dan peristiwa $B$ adalah kejadian saat $\frac{1}{3} \le X \le \frac{2}{3}$, maka nilai peluang gabungan $P(A \cup B)$ adalah ....

- A. $\frac{11}{16}$  
  <sub>Salah: Siswa hanya menghitung nilai peluang kejadian $A$ saja, yaitu $\int_0^{1/2} \frac{3}{2}(1-x^2)\,dx = \frac{11}{16}$.</sub>
- **B. $\frac{23}{27}$** ✅  
  <sub>Benar: Peristiwa $A$ adalah interval $[0, \frac{1}{2}]$ dan peristiwa $B$ adalah interval $[\frac{1}{3}, \frac{2}{3}]$. Karena $\frac{1}{3} < \frac{1}{2}$, kedua interval saling tumpang tindih sehingga gabungannya adalah interval tunggal $A \cup B = [0, \frac{2}{3}]$. Peluang gabungan dihitung langsung dengan mengintegralkan fungsi densitas pada selang gabungan tersebut: $P(A \cup B) = \int_{0}^{2/3} \frac{3}{2}(1 - x^2)\,dx = \frac{3}{2}\left[x - \frac{x^3}{3}\right]_0^{2/3} = \frac{3}{2}\left(\frac{2}{3} - \frac{8}{81}\right) = \frac{3}{2}\left(\frac{46}{81}\right) = \frac{23}{27}$.</sub>
- C. $\frac{457}{432}$  
  <sub>Salah: Siswa menjumlahkan $P(A) + P(B)$ secara langsung $\left(\frac{11}{16} + \frac{10}{27}\right)$ tanpa mengurangkan peluang irisan $P(A \cap B)$, sehingga hasilnya tidak masuk akal (lebih dari 1).</sub>
- D. $\frac{10}{27}$  
  <sub>Salah: Siswa hanya menghitung nilai peluang kejadian $B$ saja, yaitu $\int_{1/3}^{2/3} \frac{3}{2}(1-x^2)\,dx = \frac{10}{27}$.</sub>

**Pembahasan:** Langkah 1: Analisis gabungan kejadian dalam bentuk interval bilangan real:
Peristiwa $A = \left[0, \frac{1}{2}\right]$ dan peristiwa $B = \left[\frac{1}{3}, \frac{2}{3}\right]$.
Karena $\frac{1}{3} \approx 0,333 < \frac{1}{2} = 0,5$, kedua selang saling beririsan, sehingga:
$$A \cup B = \left[0, \frac{2}{3}\right]$$

Langkah 2: Hitung peluang gabungan dengan integral pada interval $\left[0, \frac{2}{3}\right]$:
$$P(A \cup B) = \int_{0}^{2/3} \frac{3}{2}(1 - x^2)\,dx$$

Langkah 3: Tentukan fungsi antiturunan:
$$\int \frac{3}{2}(1 - x^2)\,dx = \frac{3}{2}\left(x - \frac{x^3}{3}\right)$$

Langkah 4: Evaluasi batas integrasi dari $0$ hingga $\frac{2}{3}$:
$$\frac{3}{2}\left[\frac{2}{3} - \frac{\left(\frac{2}{3}\right)^3}{3}\right] = \frac{3}{2}\left(\frac{2}{3} - \frac{\frac{8}{27}}{3}\right) = \frac{3}{2}\left(\frac{2}{3} - \frac{8}{81}\right)$$
$$= \frac{3}{2}\left(\frac{54 - 8}{81}\right) = \frac{3}{2} \times \frac{46}{81} = \frac{23}{27}$$

Jadi, nilai dari $P(A \cup B)$ adalah $\frac{23}{27}$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b04-e-hard-bt01-011
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi peluang bersyarat seragam*

Seorang pengrajin keramik melakukan proses pembakaran tungku setiap hari. Waktu pembakaran efektif (dalam menit) menyebar merata dan dimodelkan oleh variabel acak kontinu $X$ pada interval $50 \le x \le 250$ dengan fungsi densitas peluang seragam. Jika diketahui pembakaran telah berlangsung setidaknya selama $100$ menit, berapakah peluang pembakaran tersebut akan selesai dalam waktu tidak lebih dari $190$ menit?

- A. $\frac{2}{5}$  
  <sub>Salah: Menghitung komplemennya $1 - \frac{3}{5} = \frac{2}{5}$.</sub>
- B. $\frac{7}{10}$  
  <sub>Salah: Menghitung $P(X \le 190) = \frac{190-50}{200} = \frac{140}{200} = \frac{7}{10}$ mengabaikan syarat $X \ge 100$.</sub>
- C. $\frac{9}{20}$  
  <sub>Salah: Menghitung peluang tanpa syarat $P(100 \le X \le 190) = \frac{90}{200}$.</sub>
- **D. $\frac{3}{5}$** ✅  
  <sub>Benar: $f(x) = \frac{1}{200}$ untuk $50 \le x \le 250$. Peluang bersyarat $P(X \le 190 \mid X \ge 100) = \frac{P(100 \le X \le 190)}{P(X \ge 100)} = \frac{(190 - 100)/200}{(250 - 100)/200} = \frac{90}{150} = \frac{3}{5}$.</sub>

**Pembahasan:** Variabel acak kontinu $X$ terdistribusi seragam pada $[50, 250]$, sehingga fungsi densitasnya adalah:
$$f(x) = \begin{cases} \frac{1}{250 - 50} = \frac{1}{200}, & 50 \le x \le 250 \\ 0, & x \text{ lainnya} \end{cases}$$
Kita diminta menentukan peluang bersyarat $P(X \le 190 \mid X \ge 100)$:
$$P(X \le 190 \mid X \ge 100) = \frac{P(100 \le X \le 190)}{P(X \ge 100)}$$
Hitung masing-masing peluang:
$$P(100 \le X \le 190) = \int_{100}^{190} \frac{1}{200}\,dx = \frac{190 - 100}{200} = \frac{90}{200}$$
$$P(X \ge 100) = \int_{100}^{250} \frac{1}{200}\,dx = \frac{250 - 100}{200} = \frac{150}{200}$$
Maka:
$$P(X \le 190 \mid X \ge 100) = \frac{\frac{90}{200}}{\frac{150}{200}} = \frac{90}{150} = \frac{3}{5}$$
**Acuan:** siswa — siswa hal.268 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b04-e-hard-bt01-012
*variasi (angka) | C5 | 5 langkah | jenis: inversi batas persentil seragam*

Dalam masa perawatan mesin, sebuah kompresor industri dioperasikan tidak lebih dari $360$ menit per siklus, dengan durasi $X$ (dalam menit) memiliki fungsi densitas peluang:
$$f(x) = \begin{cases} \frac{1}{360}, & 0 \le x \le 360 \\ 0, & x < 0 \text{ atau } x > 360 \end{cases}$$
Suatu selang waktu $[180 - k, 180 + k]$ dirancang sedemikian sehingga peluang durasi operasi mesin berada dalam rentang tersebut tepat bernilai $\frac{2}{3}$. Nilai $k$ yang memenuhi adalah ....

- **A. $120$** ✅  
  <sub>Benar: $P(180 - k \le X \le 180 + k) = \frac{(180+k) - (180-k)}{360} = \frac{2k}{360} = \frac{k}{180}$. Disamakan dengan $\frac{2}{3}$, diperoleh $k = 180 \times \frac{2}{3} = 120$.</sub>
- B. $60$  
  <sub>Salah: Menyamakan $\frac{k}{360} = \frac{2}{3}$ sehingga salah membagi dua panjang interval.</sub>
- C. $90$  
  <sub>Salah: Menganggap peluang bernilai $\frac{1}{2}$ sehingga $k = 180 \times \frac{1}{2} = 90$.</sub>
- D. $240$  
  <sub>Salah: Menghitung panjang total interval $2k = 240$ dan bukan nilai $k$.</sub>

**Pembahasan:** Diketahui $X$ berdistribusi seragam pada $[0, 360]$ dengan densitas $f(x) = \frac{1}{360}$.
Peluang pada interval $[180 - k, 180 + k]$ adalah:
$$P(180 - k \le X \le 180 + k) = \int_{180 - k}^{180 + k} \frac{1}{360}\,dx = \frac{(180 + k) - (180 - k)}{360} = \frac{2k}{360} = \frac{k}{180}$$
Diketahui peluang tersebut sama dengan $\frac{2}{3}$:
$$\frac{k}{180} = \frac{2}{3} \implies k = 180 \times \frac{2}{3} = 120$$
Jadi, nilai $k$ yang memenuhi adalah $120$.
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b04-e-hard-bt01-013
*orisinal | C5 | 5 langkah | jenis: analisis perbandingan rasio peluang*

Variabel acak kontinu $X$ menyatakan waktu tunggu (dalam jam) di suatu antrean dan memiliki fungsi densitas peluang:
$$f(x) = \begin{cases} \frac{1}{4}x^3, & 0 \le x \le 2 \\ 0, & x \text{ lainnya} \end{cases}$$
Nilai peluang bersyarat bahwa $X$ bernilai lebih dari $1$ jam, jika diketahui $X$ bernilai tidak lebih dari $\sqrt{3}$ jam, yaitu $P(X > 1 \mid X \le \sqrt{3})$, adalah ....

- A. $\frac{1}{2}$  
  <sub>Salah: Menghitung selisih batas $\frac{8}{16} = \frac{1}{2}$ tanpa membagi dengan peluang syaratnya.</sub>
- **B. $\frac{8}{9}$** ✅  
  <sub>Benar: $P(X > 1 \mid X \le \sqrt{3}) = \frac{P(1 < X \le \sqrt{3})}{P(X \le \sqrt{3})}$. Antiturunan $\frac{1}{4}x^3$ adalah $\frac{x^4}{16}$. $P(X \le \sqrt{3}) = \frac{(\sqrt{3})^4}{16} = \frac{9}{16}$. $P(1 < X \le \sqrt{3}) = \frac{(\sqrt{3})^4 - 1^4}{16} = \frac{9 - 1}{16} = \frac{8}{16}$. Rasio $= \frac{8/16}{9/16} = \frac{8}{9}$.</sub>
- C. $\frac{1}{9}$  
  <sub>Salah: Menghitung komplemen dari rasio yang dicari terhadap satu.</sub>
- D. $\frac{7}{9}$  
  <sub>Salah: Salah menghitung pemangkatan empat dari $(\sqrt{3})^4$ menjadi $8$ sehingga pembilang menjadi $7$.</sub>

**Pembahasan:** Peluang bersyarat didefinisikan sebagai:
$$P(X > 1 \mid X \le \sqrt{3}) = \frac{P(1 < X \le \sqrt{3})}{P(X \le \sqrt{3})}$$
Fungsi kumulatif untuk $0 \le x \le 2$ diperoleh dari:
$$F(x) = \int_0^x \frac{1}{4}t^3\,dt = \left[ \frac{t^4}{16} \right]_0^x = \frac{x^4}{16}$$
Hitung masing-masing bagian:
1. $P(X \le \sqrt{3}) = F(\sqrt{3}) = \frac{(\sqrt{3})^4}{16} = \frac{9}{16}$
2. $P(1 < X \le \sqrt{3}) = F(\sqrt{3}) - F(1) = \frac{9}{16} - \frac{1^4}{16} = \frac{8}{16}$

Maka nilai peluang bersyaratnya adalah:
$$P(X > 1 \mid X \le \sqrt{3}) = \frac{\frac{8}{16}}{\frac{9}{16}} = \frac{8}{9}$$
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b04-e-hard-bt01-014
*variasi (konteks) | C5 | 3 langkah | jenis: analisis peluang bersyarat durasi seragam*

Sebuah stasiun pengisian kendaraan listrik melayani pengisian daya baterai dengan durasi paling lama $120$ menit per sesi. Pengemudi tidak dapat memulai pengisian sebelum pukul 13.00 dan wajib melepaskan soket daya paling lambat pukul 15.00. Waktu pengisian daya baterai (dalam menit) dimodelkan oleh variabel acak kontinu $X$ dengan fungsi densitas peluang:
$$f(x) = \begin{cases} \frac{1}{120}, & 0 \le x \le 120 \\ 0, & x < 0 \text{ atau } x > 120 \end{cases}$$
Jika diketahui suatu kendaraan telah mengisi daya lebih dari $40$ menit, berapakah peluang kendaraan tersebut menyelesaikan pengisian daya dalam waktu tidak lebih dari $90$ menit?

- **A. $\frac{5}{8}$** ✅  
  <sub>Benar: Peluang kejadian syarat adalah $P(X > 40) = \int_{40}^{120} \frac{1}{120}\,dx = \frac{120 - 40}{120} = \frac{80}{120} = \frac{2}{3}$. Peluang irisan kedua kejadian adalah $P(40 < X \le 90) = \int_{40}^{90} \frac{1}{120}\,dx = \frac{90 - 40}{120} = \frac{50}{120} = \frac{5}{12}$. Dengan demikian, peluang bersyaratnya adalah $P(X \le 90 \mid X > 40) = \frac{P(40 < X \le 90)}{P(X > 40)} = \frac{5/12}{2/3} = \frac{5}{12} \times \frac{3}{2} = \frac{5}{8}$.</sub>
- B. $\frac{3}{4}$  
  <sub>Salah: Menghitung peluang tanpa syarat $P(X \le 90) = \frac{90}{120} = \frac{3}{4}$ dan mengabaikan informasi bahwa durasi telah melebihi 40 menit.</sub>
- C. $\frac{5}{12}$  
  <sub>Salah: Hanya menghitung peluang irisan $P(40 < X \le 90)$ tanpa membaginya dengan probabilitas syarat $P(X > 40)$.</sub>
- D. $\frac{7}{12}$  
  <sub>Salah: Keliru mengurangkan penyebut atau menghitung selang komplementer $(120 - 50)/120$.</sub>

**Pembahasan:** Diketahui $f(x) = \frac{1}{120}$ untuk $0 \le x \le 120$.

Langkah 1: Menghitung peluang kejadian prasyarat $P(X > 40)$:
$$P(X > 40) = \int_{40}^{120} \frac{1}{120}\,dx = \frac{120 - 40}{120} = \frac{80}{120} = \frac{2}{3}$$

Langkah 2: Menghitung peluang irisan $P(40 < X \le 90)$:
$$P(40 < X \le 90) = \int_{40}^{90} \frac{1}{120}\,dx = \frac{90 - 40}{120} = \frac{50}{120} = \frac{5}{12}$$

Langkah 3: Menghitung peluang bersyarat $P(X \le 90 \mid X > 40)$:
$$P(X \le 90 \mid X > 40) = \frac{P(40 < X \le 90)}{P(X > 40)} = \frac{\frac{5}{12}}{\frac{2}{3}} = \frac{5}{12} \times \frac{3}{2} = \frac{5}{8}$$

Jadi, peluang kendaraan tersebut selesai mengisi daya tidak lebih dari 90 menit adalah $\frac{5}{8}$.
**Acuan:** pretest — kelas12_tl-b04-p0269-latihan-soal-fungsi-densitas-peluang-1b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b04-e-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: penentuan parameter linier fungsi densitas*

Suatu variabel acak kontinu $X$ memiliki fungsi densitas peluang berbentuk linear:
$$f(x) = \begin{cases} ax + b, & 0 \le x \le 2 \\ 0, & x \text{ lainnya} \end{cases}$$
Jika diketahui bahwa $P(X < 1) = \frac{1}{3}$, maka nilai dari $P\left(X > \frac{3}{2}\right)$ adalah ....

- **A. $\frac{3}{8}$** ✅  
  <sub>Benar: Dari syarat total luas $\int_0^2 (ax+b)\,dx = 1$, diperoleh $2a + 2b = 1 \iff a + b = \frac{1}{2}$. Dari $P(X < 1) = \int_0^1 (ax+b)\,dx = \frac{a}{2} + b = \frac{1}{3}$. Eliminasi menghasilkan $a = \frac{1}{3}$ dan $b = \frac{1}{6}$. Kemudian dihitung $P(X > \frac{3}{2}) = \int_{3/2}^2 (\frac{1}{3}x + \frac{1}{6})\,dx = [\frac{x^2}{6} + \frac{x}{6}]_{3/2}^2 = 1 - \frac{15}{24} = \frac{9}{24} = \frac{3}{8}$.</sub>
- B. $\frac{7}{16}$  
  <sub>Salah: Kesalahan substitusi $x = 3/2$ ke dalam fungsi antiturunan.</sub>
- C. $\frac{5}{12}$  
  <sub>Salah: Keliru mengintegralkan batas bawah tanpa mengkuadratkan batas pecahan.</sub>
- D. $\frac{1}{4}$  
  <sub>Salah: Menganggap fungsi konstan rata-rata pada subinterval selang panjang 0,5.</sub>

**Pembahasan:** Langkah 1: Menggunakan sifat fungsi densitas $\int_{-\infty}^{\infty} f(x)\,dx = 1$:
$$\int_0^2 (ax + b)\,dx = \left[ \frac{a}{2}x^2 + bx \right]_0^2 = 2a + 2b = 1 \implies a + b = \frac{1}{2}$$

Langkah 2: Menggunakan informasi peluang $P(X < 1) = \frac{1}{3}$:
$$\int_0^1 (ax + b)\,dx = \left[ \frac{a}{2}x^2 + bx \right]_0^1 = \frac{a}{2} + b = \frac{1}{3}$$

Langkah 3: Menyelesaikan sistem persamaan linear:
$$(a + b) - \left(\frac{a}{2} + b\right) = \frac{1}{2} - \frac{1}{3} \implies \frac{a}{2} = \frac{1}{6} \implies a = \frac{1}{3}$$
$$b = \frac{1}{2} - a = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$$
Maka $f(x) = \frac{1}{3}x + \frac{1}{6}$ untuk $0 \le x \le 2$.

Langkah 4: Menghitung $P\left(X > \frac{3}{2}\right)$:
$$P\left(X > \frac{3}{2}\right) = \int_{3/2}^2 \left(\frac{1}{3}x + \frac{1}{6}\right)dx = \left[ \frac{x^2}{6} + \frac{x}{6} \right]_{3/2}^2$$
$$= \left(\frac{4}{6} + \frac{2}{6}\right) - \left(\frac{(3/2)^2}{6} + \frac{3/2}{6}\right) = 1 - \left(\frac{9/4}{6} + \frac{3/2}{6}\right) = 1 - \left(\frac{9}{24} + \frac{6}{24}\right) = 1 - \frac{15}{24} = \frac{9}{24} = \frac{3}{8}$$

Jadi, nilai $P\left(X > \frac{3}{2}\right)$ adalah $\frac{3}{8}$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b04-e-hard-bt01-016
*orisinal | C5 | 3 langkah | jenis: peluang selang simetris kuadratik*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang sebagai berikut:
$$f(x) = \begin{cases} \frac{3}{4}(1 - x^2), & -1 \le x \le 1 \\ 0, & x \text{ lainnya} \end{cases}$$
Peluang bahwa nilai $X$ berada pada rentang yang memenuhi pertidaksamaan $|X| \le \frac{1}{2}$ adalah ....

- A. $\frac{11}{32}$  
  <sub>Salah: Hanya menghitung integral pada selang positif $0 \le X \le 1/2$ tanpa mengalikan dua untuk memperhitungkan simetri nilai mutlak.</sub>
- **B. $\frac{11}{16}$** ✅  
  <sub>Benar: Pertidaksamaan $|X| \le \frac{1}{2}$ ekuivalen dengan selang $-\frac{1}{2} \le X \le \frac{1}{2}$. Karena fungsi genap, $P(|X| \le 1/2) = 2 \int_0^{1/2} \frac{3}{4}(1 - x^2)\,dx = \frac{3}{2} [x - \frac{x^3}{3}]_0^{1/2} = \frac{3}{2} (\frac{1}{2} - \frac{1}{24}) = \frac{3}{2} (\frac{11}{24}) = \frac{11}{16}$.</sub>
- C. $\frac{9}{16}$  
  <sub>Salah: Salah dalam pengurangan pecahan saat mengevaluasi $\frac{1}{2} - \frac{1}{24}$ menjadi $\frac{9}{24}$.</sub>
- D. $\frac{3}{4}$  
  <sub>Salah: Mengabaikan suku $x^2$ pada saat integrasi sehingga menghitung $\frac{3}{4} \times 1$.</sub>

**Pembahasan:** Langkah 1: Menentukan batas integrasi dari pertidaksamaan nilai mutlak:
$$|X| \le \frac{1}{2} \iff -\frac{1}{2} \le X \le \frac{1}{2}$$

Langkah 2: Memanfaatkan sifat kesimetrisan kurva genap $f(-x) = f(x)$:
$$P\left(|X| \le \frac{1}{2}\right) = \int_{-1/2}^{1/2} \frac{3}{4}(1 - x^2)\,dx = 2 \int_0^{1/2} \frac{3}{4}(1 - x^2)\,dx = \frac{3}{2} \int_0^{1/2} (1 - x^2)\,dx$$

Langkah 3: Mengevaluasi integral:
$$\frac{3}{2} \left[ x - \frac{x^3}{3} \right]_0^{1/2} = \frac{3}{2} \left( \frac{1}{2} - \frac{(1/2)^3}{3} \right) = \frac{3}{2} \left( \frac{1}{2} - \frac{1}{24} \right) = \frac{3}{2} \left( \frac{11}{24} \right) = \frac{33}{48} = \frac{11}{16}$$

Jadi, peluangnya adalah $\frac{11}{16}$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b04-e-hard-bt01-017
*orisinal | C5 | 3 langkah | jenis: integrasi densitas fungsi rasional*

Waktu penguraian suatu zat aktif di dalam tubuh (dalam jam) dimodelkan oleh variabel acak kontinu $X$ dengan fungsi densitas peluang:
$$f(x) = \begin{cases} \frac{k}{(x+1)^2}, & 0 \le x \le 3 \\ 0, & x \text{ lainnya} \end{cases}$$
Peluang bahwa zat aktif tersebut terurai dalam rentang waktu $1$ hingga $3$ jam adalah ....

- A. $\frac{1}{2}$  
  <sub>Salah: Kesalahan tanda saat mengevaluasi integral antiturunan $-\frac{1}{x+1}$.</sub>
- **B. $\frac{1}{3}$** ✅  
  <sub>Benar: Dari syarat total luas $\int_0^3 \frac{k}{(x+1)^2}\,dx = k\left[-\frac{1}{x+1}\right]_0^3 = k(-\frac{1}{4} + 1) = \frac{3}{4}k = 1$, diperoleh $k = \frac{4}{3}$. Kemudian dihitung $P(1 \le X \le 3) = \int_1^3 \frac{4/3}{(x+1)^2}\,dx = \frac{4}{3}\left[-\frac{1}{x+1}\right]_1^3 = \frac{4}{3}\left(-\frac{1}{4} + \frac{1}{2}\right) = \frac{4}{3}\left(\frac{1}{4}\right) = \frac{1}{3}$.</sub>
- C. $\frac{1}{4}$  
  <sub>Salah: Menggunakan nilai $k = 1$ secara langsung tanpa mencari tetapan normalisasi terlebih dahulu.</sub>
- D. $\frac{2}{3}$  
  <sub>Salah: Menghitung komplemennya yaitu $P(0 \le X < 1) = 1 - 1/3$ alih-alih selang yang diminta.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai konstanta $k$ agar $\int_0^3 f(x)\,dx = 1$:
$$\int_0^3 \frac{k}{(x+1)^2}\,dx = k \left[ -\frac{1}{x+1} \right]_0^3 = k \left( -\frac{1}{3+1} - \left(-\frac{1}{0+1}\right) \right)$$
$$= k \left( -\frac{1}{4} + 1 \right) = \frac{3}{4}k = 1 \implies k = \frac{4}{3}$$

Langkah 2: Menuliskan fungsi densitas peluang lengkap:
$$f(x) = \frac{4}{3(x+1)^2}, \quad 0 \le x \le 3$$

Langkah 3: Menghitung peluang $P(1 \le X \le 3)$:
$$P(1 \le X \le 3) = \int_1^3 \frac{4}{3(x+1)^2}\,dx = \frac{4}{3} \left[ -\frac{1}{x+1} \right]_1^3$$
$$= \frac{4}{3} \left( -\frac{1}{4} - \left(-\frac{1}{2}\right) \right) = \frac{4}{3} \left( \frac{1}{4} \right) = \frac{1}{3}$$

Jadi, peluang zat aktif tersebut terurai antara 1 hingga 3 jam adalah $\frac{1}{3}$.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b04-e-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: evaluasi peluang bersyarat kumulatif kuadratik*

Fungsi distribusi kumulatif dari suatu variabel acak kontinu $X$ didefinisikan sebagai:
$$F(x) = \begin{cases} 0, & x < 0 \\ c(4x - x^2), & 0 \le x \le 2 \\ 1, & x > 2 \end{cases}$$
Nilai dari peluang bersyarat $P(X \ge 1 \mid X \le 1{,}5)$ adalah ....

- **A. $\frac{1}{5}$** ✅  
  <sub>Benar: Karena $F(2) = 1$, maka $c(4(2) - 2^2) = 4c = 1 \implies c = \frac{1}{4}$. Peluang syarat adalah $P(X \le 1{,}5) = F(1{,}5) = \frac{1}{4}(4(1{,}5) - (1{,}5)^2) = \frac{1}{4}(6 - 2{,}25) = \frac{3{,}75}{4} = \frac{15}{16}$. Peluang irisan adalah $P(1 \le X \le 1{,}5) = F(1{,}5) - F(1) = \frac{15}{16} - \frac{1}{4}(4(1) - 1^2) = \frac{15}{16} - \frac{3}{4} = \frac{3}{16}$. Peluang bersyarat adalah $\frac{3/16}{15/16} = \frac{3}{15} = \frac{1}{5}$.</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: Salah menghitung nilai $F(1{,}5)$ atau menyederhanakan pecahan irisan secara keliru.</sub>
- C. $\frac{3}{16}$  
  <sub>Salah: Hanya menghitung nilai probabilitas irisan $P(1 \le X \le 1{,}5)$ tanpa membaginya dengan probabilitas syarat.</sub>
- D. $\frac{4}{5}$  
  <sub>Salah: Menghitung peluang komplemen $P(X < 1 \mid X \le 1{,}5) = 1 - 1/5$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai konstanta $c$ menggunakan sifat kumulatif di batas atas interval $F(2) = 1$:
$$F(2) = c(4(2) - 2^2) = c(8 - 4) = 4c = 1 \implies c = \frac{1}{4}$$
Sehingga untuk $0 \le x \le 2$, fungsi kumulatifnya adalah $F(x) = \frac{4x - x^2}{4}$.

Langkah 2: Menghitung peluang prasyarat $P(X \le 1{,}5)$:
$$P(X \le 1{,}5) = F(1{,}5) = \frac{4(1{,}5) - (1{,}5)^2}{4} = \frac{6 - 2{,}25}{4} = \frac{3{,}75}{4} = \frac{15}{16}$$

Langkah 3: Menghitung peluang irisan $P(1 \le X \le 1{,}5)$:
$$F(1) = \frac{4(1) - 1^2}{4} = \frac{3}{4} = \frac{12}{16}$$
$$P(1 \le X \le 1{,}5) = F(1{,}5) - F(1) = \frac{15}{16} - \frac{12}{16} = \frac{3}{16}$$

Langkah 4: Menghitung peluang bersyarat $P(X \ge 1 \mid X \le 1{,}5)$:
$$P(X \ge 1 \mid X \le 1{,}5) = \frac{P(1 \le X \le 1{,}5)}{P(X \le 1{,}5)} = \frac{\frac{3}{16}}{\frac{15}{16}} = \frac{3}{15} = \frac{1}{5}$$

Jadi, nilai peluang bersyarat tersebut adalah $\frac{1}{5}$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b04-e-hard-bt01-019
*orisinal | C5 | 5 langkah | jenis: evaluasi peluang sepotong dengan mutlak*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang yang didefinisikan sebagai:
$$f(x) = \begin{cases} k(x + 1), & 0 \le x \le 2 \\ k(5 - x), & 2 < x \le 4 \\ 0, & x \text{ lainnya} \end{cases}$$
Nilai dari $P(|X - 2| \le 1)$ adalah ....

- A. $\frac{3}{8}$  
  <sub>Salah: Menghitung komplemen dari kejadian yang ditanyakan, yaitu $P(|X - 2| > 1)$.</sub>
- B. $\frac{3}{4}$  
  <sub>Salah: Mengintegralkan fungsi cabang pertama $k(x+1)$ langsung dari rentang $1$ hingga $3$ tanpa memecah integral pada titik batas $x=2$.</sub>
- **C. $\frac{5}{8}$** ✅  
  <sub>Benar: Syarat fungsi densitas $\int_{-\infty}^{\infty} f(x)\,dx = 1$ menghasilkan $k = \frac{1}{8}$. Pertidaksamaan $|X - 2| \le 1$ ekuivalen dengan $1 \le X \le 3$. Menjumlahkan $\int_1^2 \frac{1}{8}(x+1)\,dx + \int_2^3 \frac{1}{8}(5-x)\,dx = \frac{5}{16} + \frac{5}{16} = \frac{5}{8}$.</sub>
- D. $\frac{5}{16}$  
  <sub>Salah: Hanya mengintegralkan salah satu cabang interval, yaitu pada selang $[1, 2]$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai konstanta $k$ agar $\int_{-\infty}^{\infty} f(x)\,dx = 1$.
$$\int_0^2 k(x+1)\,dx + \int_2^4 k(5-x)\,dx = 1$$
$$k\left[\frac{1}{2}x^2 + x\right]_0^2 + k\left[5x - \frac{1}{2}x^2\right]_2^4 = 1$$
$$k(2 + 2) + k((20 - 8) - (10 - 2)) = 1$$
$$4k + 4k = 1 \implies 8k = 1 \implies k = \frac{1}{8}$$

Langkah 2: Menentukan batas interval dari pertidaksamaan nilai mutlak:
$$|X - 2| \le 1 \iff -1 \le X - 2 \le 1 \iff 1 \le X \le 3$$

Langkah 3: Menghitung $P(1 \le X \le 3)$ dengan memecah integral pada $x = 2$:
$$P(1 \le X \le 3) = \int_1^2 \frac{1}{8}(x+1)\,dx + \int_2^3 \frac{1}{8}(5-x)\,dx$$
$$\int_1^2 \frac{1}{8}(x+1)\,dx = \frac{1}{8}\left[\frac{1}{2}x^2 + x\right]_1^2 = \frac{1}{8}\left(4 - \frac{3}{2}\right) = \frac{5}{16}$$
$$\int_2^3 \frac{1}{8}(5-x)\,dx = \frac{1}{8}\left[5x - \frac{1}{2}x^2\right]_2^3 = \frac{1}{8}\left(\frac{21}{2} - 8\right) = \frac{5}{16}$$

Langkah 4: Menjumlahkan kedua hasil integral:
$$P(1 \le X \le 3) = \frac{5}{16} + \frac{5}{16} = \frac{10}{16} = \frac{5}{8}$$
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12_tl-b04-e-hard-bt01-020
*orisinal | C5 | 4 langkah | jenis: evaluasi median dan peluang bersyarat*

Variabel acak kontinu $X$ memiliki fungsi densitas peluang:
$$f(x) = \begin{cases} k(2x - x^2), & 0 \le x \le 2 \\ 0, & x \text{ lainnya} \end{cases}$$
Jika $m$ adalah median dari $X$ (nilai sedemikian sehingga $P(X \le m) = 0{,}5$), maka nilai dari $P(X \ge 1{,}5 \mid X \ge m)$ adalah ....

- A. $\frac{5}{32}$  
  <sub>Salah: Hanya menghitung $P(X \ge 1{,}5)$ tanpa membaginya dengan peluang syarat $P(X \ge m)$.</sub>
- **B. $\frac{5}{16}$** ✅  
  <sub>Benar: Konstanta $k = \frac{3}{4}$ didapat dari $\int_0^2 k(2x-x^2)\,dx = 1$. Karena kurva simetris pada $[0, 2]$, median $m = 1$. Peluang irisan $P(X \ge 1{,}5) = \int_{1{,}5}^2 \frac{3}{4}(2x-x^2)\,dx = \frac{5}{32}$. Nilai $P(X \ge 1) = \frac{1}{2}$, sehingga $P(X \ge 1{,}5 \mid X \ge 1) = \frac{5/32}{1/2} = \frac{5}{16}$.</sub>
- C. $\frac{3}{16}$  
  <sub>Salah: Kesalahan saat melakukan evaluasi integral batas $[1{,}5; 2]$.</sub>
- D. $\frac{5}{24}$  
  <sub>Salah: Lupa mengalikan nilai integral $\int_{1{,}5}^2 (2x-x^2)\,dx = \frac{5}{24}$ dengan konstanta $k = \frac{3}{4}$ sebelum dibagi peluang syarat.</sub>

**Pembahasan:** 1. Menentukan konstanta $k$:
$$\int_{-\infty}^{\infty} f(x)\,dx = \int_0^2 k(2x - x^2)\,dx = 1$$
$$k \left[ x^2 - \frac{1}{3}x^3 \right]_0^2 = k \left( 4 - \frac{8}{3} \right) = \frac{4}{3}k = 1 \implies k = \frac{3}{4}$$

2. Menentukan median $m$:
Karena fungsi $f(x) = \frac{3}{4}(2x - x^2)$ simetris terhadap $x = 1$ pada interval $[0, 2]$, maka $m = 1$, sehingga $P(X \ge 1) = \frac{1}{2}$.

3. Menghitung $P(X \ge 1{,}5)$:
$$P(X \ge 1{,}5) = \int_{1{,}5}^2 \frac{3}{4}(2x - x^2)\,dx = \frac{3}{4} \left[ x^2 - \frac{1}{3}x^3 \right]_{\frac{3}{2}}^2$$
$$= \frac{3}{4} \left[ \left(4 - \frac{8}{3}\right) - \left(\frac{9}{4} - \frac{9}{8}\right) \right] = \frac{3}{4} \left( \frac{4}{3} - \frac{9}{8} \right) = \frac{3}{4} \left( \frac{5}{24} \right) = \frac{5}{32}$$

4. Menghitung peluang bersyarat:
$$P(X \ge 1{,}5 \mid X \ge 1) = \frac{P(X \ge 1{,}5 \cap X \ge 1)}{P(X \ge 1)} = \frac{P(X \ge 1{,}5)}{P(X \ge 1)} = \frac{\frac{5}{32}}{\frac{1}{2}} = \frac{5}{16}$$
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
