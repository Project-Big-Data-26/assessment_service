# Lembar koreksi — kelas10 SMA10-B2 subbab B: Deret

55 soal | easy 20, medium 20, hard 15 | variasi 19, orisinal 36
> **Kapasitas kurang (hard): 15 dari kuota 20** — Acuan siswa bersih di p66-p80 sudah dipakai easy/medium (sisanya dibuang karena ambigu atau rusak); materi hanya deret aritmetika, geometri, dan tak hingga tanpa sigma. Hard bermakna hanya lewat penalaran (klaim, penyangkal, parameter, perbandingan, perancangan), hanya sekitar 15 soal yang tidak nyaris kembar dengan easy/medium; tidak dipaksa sampai 20.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas10-b02-b-easy-bt01-001
*orisinal | C1 | 1 langkah | jenis: definisi deret*

Deret bilangan adalah ....

- A. selisih antara dua suku yang berurutan pada suatu barisan  
  <sub>Salah: tertukar dengan pengertian beda</sub>
- **B. jumlah suku-suku penyusun suatu barisan bilangan** ✅  
  <sub>Benar: deret diperoleh dengan menjumlahkan suku-suku barisan</sub>
- C. susunan bilangan yang mengikuti pola tertentu  
  <sub>Salah: mengira deret sama dengan barisan</sub>
- D. hasil kali suku-suku penyusun suatu barisan bilangan  
  <sub>Salah: salah operasi: dikalikan, bukan dijumlahkan</sub>

**Pembahasan:** Penjumlahan suku-suku suatu barisan disebut deret bilangan.
**Acuan:** siswa — siswa hal.68

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas10-b02-b-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: hitung jumlah deret aritmetika*

Diketahui deret: $7 + 11 + 15 + 19 + \dots$ Jumlah 20 suku pertama deret tersebut adalah ....

- A. $1.800$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{2}$</sub>
- B. $830$  
  <sub>Salah: memakai $a$ bukan $2a$ di dalam kurung</sub>
- C. $940$  
  <sub>Salah: memakai $nb$ bukan $(n-1)b$</sub>
- **D. $900$** ✅  
  <sub>Benar: $a=7$, $b=4$, $S_{20}=\frac{20}{2}(2\cdot 7+19\cdot 4)=10\cdot 90$</sub>

**Pembahasan:** $a=7$, $b=4$, $n=20$. $S_{20}=\frac{20}{2}(2\cdot7+19\cdot4)=10\cdot90=900$.
**Acuan:** siswa — siswa hal.71 Contoh 5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas10-b02-b-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: hitung jumlah deret aritmetika*

Diketahui deret: $40 + 36 + 32 + 28 + \dots$ Jumlah 12 suku pertama deret tersebut adalah ....

- A. $744$  
  <sub>Salah: salah tanda: memakai beda $+4$</sub>
- B. $192$  
  <sub>Salah: memakai $nb$ bukan $(n-1)b$</sub>
- **C. $216$** ✅  
  <sub>Benar: $a=40$, $b=-4$, $S_{12}=6(80-44)=6\cdot36$</sub>
- D. $432$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{2}$</sub>

**Pembahasan:** $a=40$, $b=-4$, $n=12$. $S_{12}=\frac{12}{2}(2\cdot40+11\cdot(-4))=6(80-44)=216$.
**Acuan:** siswa — siswa hal.71 Contoh 5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas10-b02-b-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: soal cerita deret geometri*

Banyak pengunjung sebuah situs pada hari pertama adalah 6 orang. Setiap hari banyak pengunjung menjadi 3 kali lipat hari sebelumnya sehingga membentuk barisan geometri. Berapa total pengunjung selama 5 hari pertama?

- **A. $726$ orang** ✅  
  <sub>Benar: $a=6$, $r=3$, $S_5=\frac{6(3^5-1)}{3-1}=\frac{6\cdot242}{2}$</sub>
- B. $729$ orang  
  <sub>Salah: lupa mengurangi 1 pada $r^n-1$ (hasil $\frac{6\cdot243}{2}$)</sub>
- C. $240$ orang  
  <sub>Salah: memakai $n=4$ bukan $n=5$</sub>
- D. $1.452$ orang  
  <sub>Salah: lupa membagi dengan $r-1$</sub>

**Pembahasan:** $S_5=\frac{6(3^5-1)}{3-1}=\frac{6\cdot242}{2}=726$.
**Acuan:** siswa — siswa hal.73 Contoh 6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas10-b02-b-easy-bt01-005
*variasi (konteks) | C2 | 2 langkah | jenis: soal cerita deret geometri*

Penjualan sebuah toko roti pada minggu pertama adalah 30 bungkus. Penjualan setiap minggu membentuk barisan geometri dengan rasio 4. Berapa total penjualan roti hingga minggu kelima?

- A. $10.240$ bungkus  
  <sub>Salah: lupa mengurangi 1 pada $r^n-1$</sub>
- B. $7.680$ bungkus  
  <sub>Salah: hanya menghitung penjualan minggu kelima ($U_5$)</sub>
- **C. $10.230$ bungkus** ✅  
  <sub>Benar: $S_5=\frac{30(4^5-1)}{4-1}=\frac{30\cdot1023}{3}$</sub>
- D. $30.690$ bungkus  
  <sub>Salah: lupa membagi dengan $r-1$</sub>

**Pembahasan:** $S_5=\frac{30(4^5-1)}{4-1}=\frac{30\cdot1023}{3}=10.230$.
**Acuan:** siswa — siswa hal.73 Contoh 6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas10-b02-b-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: soal cerita deret aritmetika*

Rani membagikan stiker kepada sembilan temannya. Teman pertama mendapat 3 stiker, teman kedua 7 stiker, teman ketiga 11 stiker, dan seterusnya dengan pola yang sama hingga teman kesembilan. Berapa stiker yang harus disiapkan Rani?

- A. $136$ stiker  
  <sub>Salah: memakai $n=8$ (hanya delapan teman)</sub>
- **B. $171$ stiker** ✅  
  <sub>Benar: $a=3$, $b=4$, $S_9=\frac{9}{2}(6+8\cdot4)=\frac{9}{2}\cdot38$</sub>
- C. $342$ stiker  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{2}$</sub>
- D. $189$ stiker  
  <sub>Salah: salah suku terakhir: memakai $U_9=3+9\cdot4=39$ sehingga $\frac{9}{2}(3+39)$</sub>

**Pembahasan:** $S_9=\frac{9}{2}(2\cdot3+8\cdot4)=\frac{9}{2}\cdot38=171$.
**Acuan:** pretest — kelas10-b02-p0075-latihan-2-3-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas10-b02-b-easy-bt01-007
*variasi (konteks) | C2 | 2 langkah | jenis: soal cerita deret aritmetika*

Seorang pedagang menyusun kaleng dalam 8 baris. Baris paling atas berisi 5 kaleng, dan setiap baris di bawahnya berisi 3 kaleng lebih banyak daripada baris di atasnya. Berapa banyak kaleng seluruhnya?

- A. $248$ kaleng  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{2}$</sub>
- **B. $124$ kaleng** ✅  
  <sub>Benar: $a=5$, $b=3$, $S_8=\frac{8}{2}(10+7\cdot3)=4\cdot31$</sub>
- C. $136$ kaleng  
  <sub>Salah: memakai $nb$ bukan $(n-1)b$</sub>
- D. $98$ kaleng  
  <sub>Salah: memakai $n=7$ baris</sub>

**Pembahasan:** $S_8=\frac{8}{2}(2\cdot5+7\cdot3)=4\cdot31=124$.
**Acuan:** pretest — kelas10-b02-p0075-latihan-2-3-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas10-b02-b-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: jumlah deret tak hingga*

Tentukan jumlah deret geometri tak hingga $16 + 8 + 4 + 2 + \dots$

- A. $30$  
  <sub>Salah: hanya menjumlahkan keempat suku yang tertulis</sub>
- B. $-16$  
  <sub>Salah: rasio terbalik $r=2$ sehingga $\frac{16}{1-2}$</sub>
- C. $-32$  
  <sub>Salah: memakai $\frac{a}{r-1}$ (pembagi tertukar tanda)</sub>
- **D. $32$** ✅  
  <sub>Benar: $r=\frac{1}{2}$, $|r|<1$ sehingga konvergen, $S_\infty=\frac{16}{1-\frac{1}{2}}=32$</sub>

**Pembahasan:** $r=8/16=1/2$, $|r|<1$. $S_\infty=\frac{16}{1-\frac{1}{2}}=32$.
**Acuan:** siswa — siswa hal.78 Latihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas10-b02-b-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: jumlah deret tak hingga*

Tentukan jumlah deret geometri tak hingga $12 - 6 + 3 - \frac{3}{2} + \dots$

- A. $9$  
  <sub>Salah: hanya menjumlahkan tiga suku pertama</sub>
- B. $24$  
  <sub>Salah: mengabaikan tanda rasio: $\frac{12}{1-\frac{1}{2}}$</sub>
- **C. $8$** ✅  
  <sub>Benar: $r=-\frac{1}{2}$, $|r|<1$, $S_\infty=\frac{12}{1-(-\frac{1}{2})}=\frac{12}{3/2}=8$</sub>
- D. $4$  
  <sub>Salah: rasio terbalik $r=-2$ sehingga $\frac{12}{1+2}$</sub>

**Pembahasan:** $r=-6/12=-1/2$, konvergen. $S_\infty=\frac{12}{1-(-1/2)}=8$.
**Acuan:** siswa — siswa hal.78 Latihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas10-b02-b-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: mencari banyak suku*

Suku pertama dan rasio dari suatu deret geometri berturut-turut adalah 2 dan 4. Tentukan banyak suku jika diketahui jumlah deret bilangan tersebut adalah 682.

- A. $4$  
  <sub>Salah: $S_4=170$, bukan 682 (salah menaksir pangkat)</sub>
- B. $6$  
  <sub>Salah: salah mencocokkan pangkat: mengira $4^n=1.024$ memberi $n=6$</sub>
- **C. $5$** ✅  
  <sub>Benar: $\frac{2(4^n-1)}{3}=682$ sehingga $4^n=1.024=4^5$, jadi $n=5$</sub>
- D. $341$  
  <sub>Salah: mengira $S_n=a\cdot n$ lalu $n=682:2$</sub>

**Pembahasan:** $S_n=\frac{2(4^n-1)}{4-1}=682 \Rightarrow 4^n-1=1.023 \Rightarrow 4^n=1.024=4^5$. Jadi $n=5$.
**Acuan:** siswa — siswa hal.75 Latihan 2.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas10-b02-b-easy-bt01-011
*variasi (konteks) | C2 | 2 langkah | jenis: soal cerita deret aritmetika*

Sebuah perpustakaan mengumpulkan 4.200 buku selama 40 hari. Banyak buku yang terkumpul setiap hari membentuk barisan aritmetika. Pada hari pertama terkumpul 20 buku. Berapa buku yang terkumpul pada hari terakhir?

- **A. $190$ buku** ✅  
  <sub>Benar: $S_{40}=\frac{40}{2}(20+U_{40})=4.200$ sehingga $20+U_{40}=210$ dan $U_{40}=190$</sub>
- B. $210$ buku  
  <sub>Salah: lupa mengurangi suku pertama</sub>
- C. $230$ buku  
  <sub>Salah: menambahkan suku pertama, bukan mengurangi</sub>
- D. $85$ buku  
  <sub>Salah: memakai rata-rata $\frac{4.200}{40}=105$ sebagai $\frac{a+U_n}{1}$ lalu dikurangi $a$</sub>

**Pembahasan:** $4.200=20(20+U_{40})$, $20+U_{40}=210$, $U_{40}=190$.
**Acuan:** siswa — siswa hal.79 Latihan 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas10-b02-b-easy-bt01-012
*orisinal | C2 | 1 langkah | jenis: mengenali jenis deret*

Deret $5 + 10 + 20 + 40 + \dots$ termasuk ....

- A. deret aritmetika dengan beda 5  
  <sub>Salah: memakai selisih suku pertama dan kedua saja; selisih berikutnya 10 dan 20 tidak tetap</sub>
- **B. deret geometri dengan rasio 2** ✅  
  <sub>Benar: $10:5=20:10=40:20=2$, perbandingan tetap</sub>
- C. deret geometri dengan rasio 5  
  <sub>Salah: mengira rasio sama dengan suku pertama</sub>
- D. deret aritmetika dengan beda 2  
  <sub>Salah: mengacaukan rasio dengan beda</sub>

**Pembahasan:** Perbandingan suku berurutan tetap 2, jadi deret geometri dengan rasio 2.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas10-b02-b-easy-bt01-013
*orisinal | C2 | 1 langkah | jenis: hitung jumlah deret aritmetika*

Suatu deret aritmetika memiliki suku pertama 4 dan suku ke-15 sama dengan 60. Jumlah 15 suku pertama deret tersebut adalah ....

- **A. $480$** ✅  
  <sub>Benar: $S_{15}=\frac{15}{2}(4+60)=\frac{15}{2}\cdot64=480$</sub>
- B. $450$  
  <sub>Salah: hanya memakai $U_{15}$ di dalam kurung (lupa $a$)</sub>
- C. $960$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{2}$</sub>
- D. $900$  
  <sub>Salah: memakai $n\cdot U_n$</sub>

**Pembahasan:** $S_n=\frac{n}{2}(a+U_n)$, $S_{15}=\frac{15}{2}(4+60)=480$.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas10-b02-b-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: hitung jumlah deret aritmetika*

Jumlah semua bilangan asli dari 1 sampai 50, yaitu $1 + 2 + 3 + \dots + 50$, adalah ....

- A. $1.225$  
  <sub>Salah: menjumlahkan sampai 49 saja</sub>
- B. $1.250$  
  <sub>Salah: mengalikan 25 dengan 50 (memakai suku terakhir, bukan jumlah $1+50$)</sub>
- **C. $1.275$** ✅  
  <sub>Benar: $S_{50}=\frac{50}{2}(1+50)=25\cdot51=1.275$</sub>
- D. $2.550$  
  <sub>Salah: lupa membagi dua</sub>

**Pembahasan:** Ada 25 pasangan yang masing-masing berjumlah 51, jadi $25\cdot51=1.275$.
**Acuan:** siswa — siswa hal.68

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas10-b02-b-easy-bt01-015
*orisinal | C2 | 1 langkah | jenis: hitung jumlah deret geometri*

Suatu deret geometri memiliki suku pertama 2 dan rasio 3. Jumlah 6 suku pertama deret tersebut adalah ....

- **A. $728$** ✅  
  <sub>Benar: $S_6=\frac{2(3^6-1)}{3-1}=\frac{2\cdot728}{2}=728$</sub>
- B. $1.456$  
  <sub>Salah: lupa membagi dengan $r-1$</sub>
- C. $242$  
  <sub>Salah: memakai $n=5$ bukan $n=6$</sub>
- D. $729$  
  <sub>Salah: lupa mengurangi 1 pada $r^n-1$</sub>

**Pembahasan:** $S_6=\frac{2(729-1)}{2}=728$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas10-b02-b-easy-bt01-016
*orisinal | C1 | 1 langkah | jenis: mengenali rumus deret*

Rumus jumlah $n$ suku pertama deret aritmetika dengan suku pertama $a$ dan beda $b$ adalah ....

- A. $S_n=\frac{n}{2}(a+(n-1)b)$  
  <sub>Salah: memakai $a$ bukan $2a$ (itu hanya $\frac{n}{2}U_n$)</sub>
- B. $S_n=\frac{n}{2}(2a+nb)$  
  <sub>Salah: memakai $nb$ bukan $(n-1)b$</sub>
- C. $S_n=n(2a+(n-1)b)$  
  <sub>Salah: lupa faktor $\frac{1}{2}$</sub>
- **D. $S_n=\frac{n}{2}(2a+(n-1)b)$** ✅  
  <sub>Benar: rumus dari penjumlahan $S_n$ dan urutan terbaliknya</sub>

**Pembahasan:** Rumus: $S_n=\frac{n}{2}(2a+(n-1)b)$.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas10-b02-b-easy-bt01-017
*orisinal | C1 | 1 langkah | jenis: mengenali rumus deret*

Untuk deret geometri dengan suku pertama $a$ dan rasio $r>1$, rumus jumlah $n$ suku pertama adalah ....

- A. $S_n=\frac{a(r^n+1)}{r-1}$  
  <sub>Salah: tanda $-1$ diganti $+1$</sub>
- B. $S_n=\frac{ar^n-1}{r-1}$  
  <sub>Salah: tanda kurung hilang: $a$ tidak ikut dikalikan pada $-1$</sub>
- C. $S_n=\frac{a(r^n-1)}{r+1}$  
  <sub>Salah: penyebut $r-1$ diganti $r+1$</sub>
- **D. $S_n=\frac{a(r^n-1)}{r-1}$** ✅  
  <sub>Benar: rumus pada buku untuk $r\neq1$</sub>

**Pembahasan:** Rumus: $S_n=\frac{a(r^n-1)}{r-1}$ untuk $r\neq1$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas10-b02-b-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: jumlah deret tak hingga*

Jumlah deret geometri tak hingga $24 + 12 + 6 + 3 + \dots$ adalah ....

- A. $45$  
  <sub>Salah: hanya menjumlahkan empat suku yang tertulis</sub>
- **B. $48$** ✅  
  <sub>Benar: $r=\frac{1}{2}$ dan $S_\infty=\frac{24}{1-\frac{1}{2}}=48$</sub>
- C. $-48$  
  <sub>Salah: memakai $\frac{a}{r-1}$</sub>
- D. $16$  
  <sub>Salah: memakai $\frac{a}{1+r}$</sub>

**Pembahasan:** $S_\infty=\frac{a}{1-r}=\frac{24}{1/2}=48$.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas10-b02-b-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: mengenali konvergen atau divergen*

Deret geometri tak hingga yang konvergen adalah ....

- **A. $8 + 4 + 2 + 1 + \dots$** ✅  
  <sub>Benar: rasio $\frac{1}{2}$ dan $|r|<1$</sub>
- B. $2 + 6 + 18 + 54 + \dots$  
  <sub>Salah: rasio 3, $|r|>1$ sehingga divergen</sub>
- C. $3 - 6 + 12 - 24 + \dots$  
  <sub>Salah: rasio $-2$, tanda negatif tidak membuat konvergen karena $|r|=2>1$</sub>
- D. $5 + 10 + 20 + 40 + \dots$  
  <sub>Salah: rasio 2, $|r|>1$ sehingga divergen</sub>

**Pembahasan:** Konvergen bila $|r|<1$: hanya $8+4+2+1+\dots$ (rasio $\frac{1}{2}$).
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas10-b02-b-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: syarat konvergen*

Deret geometri $1 + (m-3) + (m-3)^2 + (m-3)^3 + \dots$ konvergen jika ....

- A. $-1<m<1$  
  <sub>Salah: memakai $|m|<1$ tanpa mengurangi 3</sub>
- B. $-4<m<-2$  
  <sub>Salah: salah tanda saat memindahkan $-3$</sub>
- C. $m<4$  
  <sub>Salah: hanya memakai batas atas $m-3<1$</sub>
- **D. $2<m<4$** ✅  
  <sub>Benar: $r=m-3$ dan $|m-3|<1$ memberi $-1<m-3<1$, jadi $2<m<4$</sub>

**Pembahasan:** $|r|<1 \Rightarrow |m-3|<1 \Rightarrow 2<m<4$.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas10-b02-b-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: jumlah bilangan kelipatan*

Tentukanlah jumlah bilangan kelipatan 7 di antara bilangan 20 dan 150.

- A. $1.750$  
  <sub>Salah: suku terakhir 154 yang sudah melewati 150 (20 suku)</sub>
- B. $1.610$  
  <sub>Salah: suku pertama 14 yang masih di bawah 20 (20 suku)</sub>
- **C. $1.596$** ✅  
  <sub>Benar: kelipatan 7 pertama 21 dan terakhir 147, banyak suku $\frac{147-21}{7}+1=19$, $S_{19}=\frac{19}{2}(21+147)=1.596$</sub>
- D. $1.512$  
  <sub>Salah: banyak suku 18 (lupa menambah 1 pada $\frac{147-21}{7}$)</sub>

**Pembahasan:** Suku pertama $a=21$, beda $b=7$, suku terakhir $147$. $n=\frac{147-21}{7}+1=19$. $S_{19}=\frac{19}{2}(21+147)=19\cdot84=1.596$.
**Acuan:** pretest — kelas10-b02-p0074-latihan-2-3-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas10-b02-b-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: jumlah bilangan kelipatan*

Tentukanlah jumlah bilangan kelipatan 11 di antara bilangan 100 dan 1.000.

- **A. $44.550$** ✅  
  <sub>Benar: kelipatan 11 pertama 110, terakhir 990, banyak suku 81, $S_{81}=\frac{81}{2}(110+990)=44.550$</sub>
- B. $44.649$  
  <sub>Salah: ikut memasukkan 99 yang berada di luar batas 100</sub>
- C. $89.100$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{2}$</sub>
- D. $44.000$  
  <sub>Salah: banyak suku 80 (lupa menambah 1)</sub>

**Pembahasan:** Suku pertama $110$, suku terakhir $990$, beda $11$. $n=\frac{990-110}{11}+1=81$. $S_{81}=\frac{81}{2}(110+990)=81\cdot550=44.550$.
**Acuan:** pretest — kelas10-b02-p0074-latihan-2-3-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas10-b02-b-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: lintasan bola memantul*

Sebuah bola dijatuhkan dari ketinggian 15 meter. Apabila tinggi yang dicapai saat memantul adalah empat perlima kali tinggi sebelumnya, tentukan panjang lintasan yang dilalui bola tersebut hingga berhenti memantul.

- **A. $135$ meter** ✅  
  <sub>Benar: pantulan pertama 12 m dengan $r=\frac{4}{5}$; lintasan $=15+2\cdot\frac{12}{1-\frac{4}{5}}=15+120$</sub>
- B. $150$ meter  
  <sub>Salah: memakai $a=15$ sebagai pantulan pertama sehingga $2\cdot\frac{15}{1/5}$</sub>
- C. $120$ meter  
  <sub>Salah: lupa menambahkan tinggi jatuh awal 15 m</sub>
- D. $75$ meter  
  <sub>Salah: hanya menghitung jatuh dan satu arah naik: $15+60$ (lupa naik-turun)</sub>

**Pembahasan:** Pantulan pertama $15\cdot\frac{4}{5}=12$. Jumlah tinggi semua pantulan $\frac{12}{1-\frac{4}{5}}=60$. Setiap pantulan dilalui naik dan turun, jadi lintasan $=15+2\cdot60=135$ m.
**Acuan:** siswa — siswa hal.80 Latihan 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas10-b02-b-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: keliling bangun bersusun*

Sisi segitiga sama sisi pertama panjangnya 36 cm. Di dalamnya dibuat segitiga sama sisi kedua dengan menghubungkan titik tengah ketiga sisi segitiga pertama. Cara yang sama dilakukan untuk membuat segitiga ketiga, keempat, dan kelima. Berapa total keliling kelima segitiga tersebut?

- A. $104{,}625$ cm  
  <sub>Salah: lupa membagi dengan $1-r$</sub>
- B. $202{,}5$ cm  
  <sub>Salah: hanya menjumlahkan empat segitiga pertama</sub>
- **C. $209{,}25$ cm** ✅  
  <sub>Benar: keliling $108,54,27,\dots$ ($r=\frac{1}{2}$), $S_5=\frac{108(1-\frac{1}{32})}{1-\frac{1}{2}}=209{,}25$</sub>
- D. $212{,}625$ cm  
  <sub>Salah: menjumlahkan enam segitiga, bukan lima</sub>

**Pembahasan:** Keliling pertama $3\cdot36=108$ dan tiap segitiga berikutnya setengah dari sebelumnya. $S_5=\frac{108(1-(\frac12)^5)}{1-\frac12}=216\cdot\frac{31}{32}=209{,}25$.
**Acuan:** siswa — siswa hal.80 Latihan 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas10-b02-b-medium-bt01-005
*variasi (konteks) | C4 | 4 langkah | jenis: bagian bergantian tak hingga*

Dua sahabat, Anto dan Budi, berbagi sebuah pizza dengan cara bergantian. Anto lebih dulu mengambil seperempat bagian pizza. Budi mengambil seperempat dari pizza yang tersisa, kemudian Anto mengambil seperempat dari sisa berikutnya, dan seterusnya tanpa berhenti. Jumlah seluruh bagian pizza yang diambil Anto adalah ....

- **A. $\frac{4}{7}$ bagian** ✅  
  <sub>Benar: bagian Anto $\frac{1}{4}+\frac{9}{64}+\dots$ dengan $r=\left(\frac{3}{4}\right)^2=\frac{9}{16}$, $S_\infty=\frac{1/4}{7/16}=\frac{4}{7}$</sub>
- B. $\frac{1}{2}$ bagian  
  <sub>Salah: mengira kedua orang akhirnya memperoleh bagian sama banyak</sub>
- C. $\frac{3}{7}$ bagian  
  <sub>Salah: tertukar dengan bagian Budi</sub>
- D. $1$ bagian  
  <sub>Salah: menghitung seluruh pizza yang diambil berdua dengan $r=\frac{3}{4}$</sub>

**Pembahasan:** Setelah dua pengambilan, sisa menjadi $\left(\frac{3}{4}\right)^2$. Bagian Anto: $\frac{1}{4},\frac{1}{4}\cdot\frac{9}{16},\dots$ sehingga $r=\frac{9}{16}$ dan $S_\infty=\frac{\frac14}{1-\frac{9}{16}}=\frac{4}{7}$.
**Acuan:** siswa — siswa hal.79 Latihan 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas10-b02-b-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: suku nol barisan aritmetika*

Suku ke-4 suatu barisan aritmetika adalah 42 dan suku ke-9 adalah 12. Tentukan nilai n agar suku ke-n = 0.

- A. $7$  
  <sub>Salah: mengira $U_4=42$ adalah suku pertama: $42:6$</sub>
- **B. $11$** ✅  
  <sub>Benar: $5b=12-42$ sehingga $b=-6$, $a=60$, $60-6(n-1)=0$ memberi $n=11$</sub>
- C. $12$  
  <sub>Salah: salah menghitung $a=U_4-4b=66$ sehingga $66-6(n-1)=0$</sub>
- D. $10$  
  <sub>Salah: memakai $a+nb=0$ (lupa $n-1$)</sub>

**Pembahasan:** $b=\frac{12-42}{9-4}=-6$, $a=42-3(-6)=60$. $U_n=60-6(n-1)=0 \Rightarrow n-1=10 \Rightarrow n=11$.
**Acuan:** siswa — siswa hal.79 Latihan 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas10-b02-b-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: soal cerita deret geometri*

Pertambahan penduduk di suatu desa setiap tahunnya membentuk barisan geometri dengan rasio positif. Pada tahun 2018, penduduk bertambah sebanyak 4 orang, lalu pada tahun 2020 sebanyak 36 orang. Berapa jumlah seluruh pertambahan penduduk dari tahun 2018 sampai tahun 2023?

- A. $484$ orang  
  <sub>Salah: menjumlahkan lima tahun (2018 sampai 2022)</sub>
- B. $2.912$ orang  
  <sub>Salah: lupa membagi dengan $r-1$</sub>
- **C. $1.456$ orang** ✅  
  <sub>Benar: $r^2=9$, $r=3$, $n=6$, $S_6=\frac{4(3^6-1)}{3-1}=1.456$</sub>
- D. $4.372$ orang  
  <sub>Salah: menjumlahkan tujuh suku</sub>

**Pembahasan:** Dari 2018 ke 2020 ada dua langkah: $r^2=\frac{36}{4}=9$, $r=3$. Tahun 2018-2023 ada $6$ suku. $S_6=\frac{4(3^6-1)}{3-1}=2\cdot728=1.456$.
**Acuan:** siswa — siswa hal.79 Latihan 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas10-b02-b-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: syarat konvergen*

Agar deret geometri $6 + 6(2m-7) + 6(2m-7)^2 + \dots$ merupakan deret konvergen, tentukan nilai $m$.

- A. $\frac{7}{2}<m<4$  
  <sub>Salah: hanya memakai $0<r<1$ (mengabaikan rasio negatif)</sub>
- B. $-4<m<-3$  
  <sub>Salah: salah tanda: memakai $|2m+7|<1$</sub>
- **C. $3<m<4$** ✅  
  <sub>Benar: $r=2m-7$, $|2m-7|<1$ sehingga $6<2m<8$, jadi $3<m<4$</sub>
- D. $6<m<8$  
  <sub>Salah: lupa membagi dengan 2 pada $6<2m<8$</sub>

**Pembahasan:** $r=2m-7$. Konvergen bila $-1<2m-7<1 \Rightarrow 6<2m<8 \Rightarrow 3<m<4$.
**Acuan:** siswa — siswa hal.78 Latihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas10-b02-b-medium-bt01-009
*variasi (angka) | C4 | 3 langkah | jenis: syarat konvergen*

Suku pertama suatu deret geometri tak hingga adalah $x$ dan jumlah deret tak hingga tersebut adalah 15. Nilai $x$ berikut yang mungkin adalah ....

- A. $30$  
  <sub>Salah: memberi $r=-1$ sehingga $|r|=1$ (tidak konvergen)</sub>
- **B. $9$** ✅  
  <sub>Benar: $r=1-\frac{x}{15}=\frac{2}{5}$ dan $|r|<1$ sehingga konvergen</sub>
- C. $-5$  
  <sub>Salah: memberi $r=\frac{4}{3}$ sehingga $|r|>1$ (divergen)</sub>
- D. $45$  
  <sub>Salah: memberi $r=-2$ sehingga $|r|>1$ (divergen)</sub>

**Pembahasan:** $S_\infty=\frac{x}{1-r}=15 \Rightarrow r=1-\frac{x}{15}$. Syarat $|r|<1$ memberi $0<x<30$. Hanya $9$ yang memenuhi ($r=\frac{2}{5}$).
**Acuan:** siswa — siswa hal.77 Latihan 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas10-b02-b-medium-bt01-010
*orisinal | C3 | 4 langkah | jenis: menentukan a dan b dari dua jumlah*

Jumlah 4 suku pertama suatu deret aritmetika adalah 44 dan jumlah 8 suku pertama adalah 152. Suku ke-10 deret tersebut adalah ....

- A. $46$  
  <sub>Salah: memakai rumus $S_n=\frac{n}{2}(a+(n-1)b)$ (lupa $2a$) sehingga $a=10$</sub>
- B. $45$  
  <sub>Salah: memakai $a+nb$ (lupa $n-1$)</sub>
- C. $37$  
  <sub>Salah: memakai $a+(n-2)b$ untuk suku ke-10</sub>
- **D. $41$** ✅  
  <sub>Benar: $2a+3b=22$ dan $2a+7b=38$ sehingga $b=4$, $a=5$, $U_{10}=5+9\cdot4=41$</sub>

**Pembahasan:** $S_4=2(2a+3b)=44 \Rightarrow 2a+3b=22$; $S_8=4(2a+7b)=152 \Rightarrow 2a+7b=38$. Selisih: $4b=16$, $b=4$, $a=5$. $U_{10}=5+9\cdot4=41$.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas10-b02-b-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: suku dari rumus jumlah*

Jumlah $n$ suku pertama suatu deret dinyatakan dengan $S_n=3n^2+5n$. Suku ke-8 deret tersebut adalah ....

- A. $182$  
  <sub>Salah: memakai $S_7$ sebagai suku ke-8</sub>
- **B. $50$** ✅  
  <sub>Benar: $U_8=S_8-S_7=232-182=50$</sub>
- C. $232$  
  <sub>Salah: mengira $S_8$ adalah suku ke-8</sub>
- D. $53$  
  <sub>Salah: menurunkan $S_n$ secara aljabar: $U_n=6n+5$</sub>

**Pembahasan:** Suku ke-8 adalah jumlah 8 suku dikurangi jumlah 7 suku. $S_8=3\cdot64+40=232$, $S_7=3\cdot49+35=182$, $U_8=50$.
**Acuan:** siswa — siswa hal.68

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas10-b02-b-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: lintasan ayunan tak hingga*

Sebuah bandul diayunkan dan panjang lintasan pada ayunan pertama adalah 50 cm. Setiap ayunan berikutnya menempuh lintasan sebesar $80\%$ dari ayunan sebelumnya hingga bandul berhenti. Panjang seluruh lintasan bandul adalah ....

- A. $62{,}5$ cm  
  <sub>Salah: memakai $\frac{a}{r}$ bukan $\frac{a}{1-r}$</sub>
- B. $500$ cm  
  <sub>Salah: menggandakan hasil seperti pantulan bola (padahal tiap ayunan sudah satu lintasan)</sub>
- C. $90$ cm  
  <sub>Salah: hanya menjumlahkan dua ayunan pertama: $50+40$</sub>
- **D. $250$ cm** ✅  
  <sub>Benar: $r=\frac{4}{5}$, $S_\infty=\frac{50}{1-\frac{4}{5}}=250$</sub>

**Pembahasan:** $r=80\%=\frac{4}{5}<1$ sehingga konvergen. $S_\infty=\frac{50}{1-\frac45}=250$ cm.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas10-b02-b-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: suku dari jumlah tak hingga*

Suatu deret geometri tak hingga memiliki suku pertama 12 dan jumlah 20. Suku ketiga deret tersebut adalah ....

- A. $\frac{96}{125}$  
  <sub>Salah: memakai $ar^3$ untuk suku ketiga</sub>
- B. $\frac{108}{25}$  
  <sub>Salah: mengira rasio $\frac{12}{20}=\frac{3}{5}$</sub>
- C. $\frac{24}{5}$  
  <sub>Salah: memakai $ar$ (suku kedua)</sub>
- **D. $\frac{48}{25}$** ✅  
  <sub>Benar: $20=\frac{12}{1-r}$ memberi $r=\frac{2}{5}$, $U_3=12\cdot\frac{4}{25}=\frac{48}{25}$</sub>

**Pembahasan:** $S_\infty=\frac{a}{1-r}$: $20=\frac{12}{1-r} \Rightarrow 1-r=\frac{3}{5} \Rightarrow r=\frac{2}{5}$. $U_3=ar^2=12\cdot\frac{4}{25}=\frac{48}{25}$.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas10-b02-b-medium-bt01-014
*orisinal | C4 | 4 langkah | jenis: jumlah suku bernomor genap*

Diketahui deret aritmetika $3 + 7 + 11 + \dots + 99$. Jumlah suku-suku yang bernomor genap (suku ke-2, ke-4, ke-6, dan seterusnya) adalah ....

- A. $636$  
  <sub>Salah: memakai suku terakhir 99 pada deret suku genap</sub>
- B. $663$  
  <sub>Salah: menjumlahkan suku bernomor ganjil</sub>
- C. $1.275$  
  <sub>Salah: menjumlahkan seluruh suku</sub>
- **D. $612$** ✅  
  <sub>Benar: $U_n=4n-1$, $n=25$; suku genap $7,15,\dots,95$ (12 suku), $S=\frac{12}{2}(7+95)=612$</sub>

**Pembahasan:** $U_n=3+4(n-1)=99 \Rightarrow n=25$. Suku genap: $U_2=7$, beda $8$, hingga $U_{24}=95$ (12 suku). $S=6(7+95)=612$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas10-b02-b-medium-bt01-015
*orisinal | C4 | 4 langkah | jenis: selisih jumlah geometri*

Diketahui deret geometri $6 + 18 + 54 + \dots$ Jumlah suku ke-4 sampai suku ke-7 deret tersebut adalah ....

- **A. $6.480$** ✅  
  <sub>Benar: $S_7-S_3=6.558-78=6.480$</sub>
- B. $19.602$  
  <sub>Salah: memakai $S_8-S_3$</sub>
- C. $6.558$  
  <sub>Salah: menghitung $S_7$ saja</sub>
- D. $6.318$  
  <sub>Salah: mengurangkan $S_4$ sehingga suku ke-4 ikut terbuang</sub>

**Pembahasan:** $r=3$. $S_7=\frac{6(3^7-1)}{2}=6.558$, $S_3=\frac{6(3^3-1)}{2}=78$. Suku ke-4 sampai ke-7: $S_7-S_3=6.480$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas10-b02-b-medium-bt01-016
*orisinal | C4 | 4 langkah | jenis: dua suku geometri bertanda berganti*

Suku kedua suatu deret geometri adalah 12 dan suku kelimanya adalah $-96$. Jumlah 6 suku pertama deret tersebut adalah ....

- A. $504$  
  <sub>Salah: memakai $a=U_2\cdot r=-24$</sub>
- B. $378$  
  <sub>Salah: mengabaikan tanda negatif: $r=2$ dan $a=6$</sub>
- **C. $126$** ✅  
  <sub>Benar: $r^3=\frac{-96}{12}=-8$, $r=-2$, $a=-6$, $S_6=\frac{-6((-2)^6-1)}{-2-1}=126$</sub>
- D. $-66$  
  <sub>Salah: memakai $n=5$</sub>

**Pembahasan:** $\frac{U_5}{U_2}=r^3=-8 \Rightarrow r=-2$, $a=\frac{12}{-2}=-6$. $S_6=\frac{-6(64-1)}{-3}=126$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas10-b02-b-medium-bt01-017
*orisinal | C3 | 4 langkah | jenis: cerita n dari jumlah deret aritmetika*

Rina menabung setiap bulan. Pada bulan pertama ia menabung Rp50.000,00 dan setiap bulan berikutnya tabungannya bertambah Rp10.000,00 dari bulan sebelumnya. Jumlah seluruh uang yang ia tabung mencapai Rp1.800.000,00 setelah ... bulan.

- A. $16$  
  <sub>Salah: $S_{16}=2.000.000$, sudah melewati 1.800.000</sub>
- **B. $15$** ✅  
  <sub>Benar: $S_n=\frac{n}{2}(100.000+(n-1)10.000)=5.000n(n+9)=1.800.000$ memberi $n(n+9)=360$, $n=15$</sub>
- C. $14$  
  <sub>Salah: $S_{14}=1.610.000$, belum mencapai 1.800.000</sub>
- D. $36$  
  <sub>Salah: lupa kenaikan tiap bulan: $1.800.000:50.000$</sub>

**Pembahasan:** $S_n=5.000n(n+9)=1.800.000 \Rightarrow n^2+9n-360=0 \Rightarrow (n-15)(n+24)=0$. Karena $n>0$, $n=15$.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas10-b02-b-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: rasio negatif deret tak hingga*

Jumlah suatu deret geometri tak hingga adalah 9 dan rasionya $-\frac{1}{2}$. Suku kedua deret tersebut adalah ....

- **A. $-\frac{27}{4}$** ✅  
  <sub>Benar: $a=9\left(1+\frac12\right)=\frac{27}{2}$, $U_2=ar=-\frac{27}{4}$</sub>
- B. $\frac{27}{4}$  
  <sub>Salah: mengabaikan tanda negatif pada rasio</sub>
- C. $\frac{27}{2}$  
  <sub>Salah: memberikan suku pertama, bukan suku kedua</sub>
- D. $-\frac{9}{4}$  
  <sub>Salah: memakai $a=S(1+r)=\frac{9}{2}$ (tanda $r$ tertukar)</sub>

**Pembahasan:** $S_\infty=\frac{a}{1-r} \Rightarrow 9=\frac{a}{\frac32} \Rightarrow a=\frac{27}{2}$. $U_2=\frac{27}{2}\cdot\left(-\frac12\right)=-\frac{27}{4}$.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas10-b02-b-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: jumlah geometri rasio negatif*

Jumlah 7 suku pertama deret $6 - 12 + 24 - 48 + \dots$ adalah ....

- A. $-126$  
  <sub>Salah: memakai 6 suku, bukan 7</sub>
- B. $-254$  
  <sub>Salah: mengira $(-2)^7=+128$ sehingga $\frac{6\cdot127}{-3}$</sub>
- C. $762$  
  <sub>Salah: memakai $r=2$ (mengabaikan tanda)</sub>
- **D. $258$** ✅  
  <sub>Benar: $r=-2$, $S_7=\frac{6((-2)^7-1)}{-2-1}=\frac{6(-129)}{-3}=258$</sub>

**Pembahasan:** $r=\frac{-12}{6}=-2$. $(-2)^7=-128$. $S_7=\frac{6(-128-1)}{-3}=258$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas10-b02-b-medium-bt01-020
*orisinal | C4 | 4 langkah | jenis: membandingkan dua rencana deret aritmetika*

Dua perusahaan menawarkan gaji kepada Dinda. Perusahaan P: gaji tahun pertama Rp60.000.000,00 dan naik Rp3.000.000,00 setiap tahun. Perusahaan Q: gaji tahun pertama Rp52.000.000,00 dan naik Rp4.500.000,00 setiap tahun. Selama 10 tahun, total gaji yang lebih besar dan selisihnya adalah ....

- A. Perusahaan P lebih besar Rp5.000.000,00  
  <sub>Salah: memakai $nb$ bukan $(n-1)b$ sehingga $750$ juta dan $745$ juta</sub>
- **B. Perusahaan P lebih besar Rp12.500.000,00** ✅  
  <sub>Benar: $S_{10}(P)=5(120+27)=735$ juta, $S_{10}(Q)=5(104+40{,}5)=722{,}5$ juta, selisih 12,5 juta untuk P</sub>
- C. Perusahaan Q lebih besar Rp12.500.000,00  
  <sub>Salah: arah selisih tertukar</sub>
- D. Perusahaan Q lebih besar Rp5.500.000,00  
  <sub>Salah: hanya membandingkan gaji tahun ke-10 ($87$ juta dan $92{,}5$ juta)</sub>

**Pembahasan:** $S_{10}(P)=\frac{10}{2}(2\cdot60+9\cdot3)=735$ juta. $S_{10}(Q)=5(2\cdot52+9\cdot4{,}5)=722{,}5$ juta. P lebih besar $12{,}5$ juta.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas10-b02-b-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi pernyataan konvergensi*

Pernyataan berikut yang benar adalah ....

- **A. Deret $2+\frac{4}{3}+\frac{8}{9}+\dots$ konvergen dengan jumlah $6$** ✅  
  <sub>Benar: $r=\frac{2}{3}$ sehingga $|r|<1$ dan $S_\infty=\frac{2}{1-\frac{2}{3}}=6$</sub>
- B. Deret $5+5+5+\dots$ konvergen dengan jumlah $5$  
  <sub>Salah: rasio $1$ sehingga jumlah terus bertambah (divergen)</sub>
- C. Deret $3+6+12+\dots$ konvergen karena semua sukunya positif  
  <sub>Salah: mengira suku positif cukup untuk konvergen, padahal $r=2$</sub>
- D. Deret $8-12+18-27+\dots$ konvergen karena rasionya negatif  
  <sub>Salah: mengira rasio negatif selalu konvergen, padahal $r=-rac{3}{2}$ dan $|r|>1$</sub>

**Pembahasan:** Syarat konvergen: $|r|<1$. Deret pertama $r=\frac{2}{3}$ (konvergen, $S_\infty=6$). Deret kedua $r=2$, ketiga $r=-\frac{3}{2}$, keempat $r=1$; ketiganya divergen.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas10-b02-b-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal klaim*

Seorang siswa menyatakan: "Untuk setiap deret geometri tak hingga yang konvergen, jumlahnya selalu lebih besar daripada suku pertamanya." Deret yang merupakan contoh penyangkal pernyataan tersebut adalah ....

- A. $12+6+3+\frac{3}{2}+\dots$  
  <sub>Salah: $S_\infty=24>12$, sesuai klaim</sub>
- B. $8+4+2+1+\dots$  
  <sub>Salah: $S_\infty=16>8$, justru sesuai dengan klaim (bukan penyangkal)</sub>
- C. $9+3+1+\frac{1}{3}+\dots$  
  <sub>Salah: $S_\infty=\frac{27}{2}>9$, sesuai klaim</sub>
- **D. $8-4+2-1+\dots$** ✅  
  <sub>Benar: $r=-\frac{1}{2}$, $S_\infty=\frac{8}{1+\frac{1}{2}}=\frac{16}{3}<8$, sehingga jumlahnya lebih kecil daripada suku pertama</sub>

**Pembahasan:** Penyangkal harus konvergen dengan $S_\infty\le a$. Hanya rasio negatif yang mungkin: $8-4+2-\dots$ memberi $S_\infty=\frac{16}{3}<8$. Tiga deret lain berrasio positif sehingga $S_\infty=\frac{a}{1-r}>a$.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas10-b02-b-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: menemukan kesalahan banyak suku*

Seorang siswa menghitung jumlah deret $5+8+11+\dots+101$. Ia menentukan banyak suku dengan $n=\frac{101-5}{3}=32$ lalu memperoleh jumlah $1.696$. Jumlah deret yang benar adalah ....

- A. $1.696$  
  <sub>Salah: hasil siswa: lupa menambah 1 pada banyak suku (32 suku)</sub>
- B. $1.802$  
  <sub>Salah: memakai 34 suku (menambah 1 dua kali)</sub>
- **C. $1.749$** ✅  
  <sub>Benar: banyak suku $n=\frac{101-5}{3}+1=33$ sehingga $S_{33}=\frac{33}{2}(5+101)=1.749$</sub>
- D. $3.498$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{2}$</sub>

**Pembahasan:** Dari $U_n=5+3(n-1)=101$ diperoleh $n=33$. $S_{33}=\frac{33}{2}(5+101)=33\cdot53=1.749$. Siswa lupa bahwa $\frac{101-5}{3}$ menghitung jumlah selisih, bukan jumlah suku.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas10-b02-b-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: tiga bilangan deret aritmetika*

Tiga bilangan bulat positif membentuk deret aritmetika. Jumlah ketiga bilangan itu 21 dan hasil kalinya 280. Bilangan terbesar di antara ketiganya adalah ....

- **A. $10$** ✅  
  <sub>Benar: $3a=21$ sehingga tengah $7$; $7(49-b^2)=280$ memberi $b^2=9$; bilangan $4,7,10$</sub>
- B. $7$  
  <sub>Salah: menjawab bilangan tengah</sub>
- C. $4$  
  <sub>Salah: menjawab bilangan terkecil</sub>
- D. $40$  
  <sub>Salah: menjawab hasil kali bilangan terkecil dan terbesar ($4\cdot10$)</sub>

**Pembahasan:** Misalkan $a-b$, $a$, $a+b$. Jumlah $3a=21 \Rightarrow a=7$. Hasil kali $7(49-b^2)=280 \Rightarrow b^2=9$, $b=\pm3$. Bilangannya $4,7,10$ sehingga yang terbesar $10$.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas10-b02-b-hard-bt01-005
*orisinal | C5 | 5 langkah | jenis: tiga bilangan deret geometri*

Tiga bilangan positif membentuk deret geometri. Jumlah ketiga bilangan itu 26 dan hasil kalinya 216. Selisih bilangan terbesar dan bilangan terkecil adalah ....

- **A. $16$** ✅  
  <sub>Benar: $a^3=216$ sehingga tengah $6$; $\frac{6}{r}+6r=20$ memberi $3r^2-10r+3=0$, $r=3$ atau $\frac{1}{3}$; bilangan $2,6,18$, selisih $16$</sub>
- B. $12$  
  <sub>Salah: selisih bilangan terbesar dan bilangan tengah ($18-6$)</sub>
- C. $4$  
  <sub>Salah: selisih bilangan tengah dan terkecil ($6-2$)</sub>
- D. $20$  
  <sub>Salah: menjumlahkan bilangan terbesar dan terkecil, bukan selisih</sub>

**Pembahasan:** Misalkan $\frac{a}{r}$, $a$, $ar$. Hasil kali $a^3=216 \Rightarrow a=6$. Jumlah: $\frac{6}{r}+6+6r=26 \Rightarrow 3r^2-10r+3=0 \Rightarrow r=3$ atau $\frac{1}{3}$. Bilangannya $2,6,18$ sehingga selisih $18-2=16$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas10-b02-b-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: syarat parameter konvergen (rasio pecahan)*

Deret geometri tak hingga $1+\frac{x}{x+3}+\left(\frac{x}{x+3}\right)^2+\dots$ konvergen untuk semua nilai $x$ yang memenuhi ....

- A. $x<-\frac{3}{2}$  
  <sub>Salah: arah pertidaksamaan terbalik</sub>
- **B. $x>-\frac{3}{2}$** ✅  
  <sub>Benar: $\left|\frac{x}{x+3}\right|<1$ berarti $x^2<(x+3)^2$ sehingga $6x+9>0$, jadi $x>-\frac{3}{2}$</sub>
- C. $x>0$  
  <sub>Salah: hanya memakai $0<r<1$ sehingga mengabaikan rasio negatif (mis. $x=-1$ memberi $r=-\frac{1}{2}$ konvergen)</sub>
- D. $x>-3$  
  <sub>Salah: hanya memastikan penyebut positif; $x=-2$ memberi $r=-2$ sehingga divergen</sub>

**Pembahasan:** Syarat $|r|<1$ dengan $r=\frac{x}{x+3}$: kuadratkan $x^2<(x+3)^2 \Rightarrow 0<6x+9 \Rightarrow x>-\frac{3}{2}$. Uji $x=-1$: $r=-\frac{1}{2}$ konvergen; $x=-2$: $r=-2$ divergen.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas10-b02-b-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: dua deret aritmetika sama jumlahnya*

Deret $P$: $5+11+17+\dots$ dan deret $Q$: $47+49+51+\dots$ keduanya aritmetika. Banyak suku $n$ (bilangan asli) sehingga jumlah $n$ suku pertama kedua deret sama adalah ....

- A. $23$  
  <sub>Salah: menambah 1 pada $n-1=21$ dua kali</sub>
- B. $11$  
  <sub>Salah: membagi 22 dengan 2 karena mengira rumus memuat $\frac{n}{2}$ pada hasil akhir</sub>
- C. $21$  
  <sub>Salah: memakai $n-1=21$ sebagai $n$</sub>
- **D. $22$** ✅  
  <sub>Benar: $\frac{n}{2}(10+6(n-1))=\frac{n}{2}(94+2(n-1))$ memberi $4(n-1)=84$, $n=22$</sub>

**Pembahasan:** $S_n(P)=\frac{n}{2}(10+6(n-1))$ dan $S_n(Q)=\frac{n}{2}(94+2(n-1))$. Samakan dan bagi $\frac{n}{2}$ (karena $n>0$): $10+6(n-1)=94+2(n-1) \Rightarrow 4(n-1)=84 \Rightarrow n=22$. Cek: $S_{22}=1.496$ untuk keduanya.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas10-b02-b-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: jumlah dua deret aritmetika seletak*

Barisan $P$: $2,5,8,\dots$ dan barisan $Q$: $40,36,32,\dots$ keduanya aritmetika. Barisan $R$ dibentuk dengan menjumlahkan suku-suku yang seletak pada $P$ dan $Q$ ($R_1=42$, $R_2=41$, dan seterusnya). Jumlah 20 suku pertama $R$ adalah ....

- **A. $650$** ✅  
  <sub>Benar: $R_n=(2+3(n-1))+(40-4(n-1))=42-(n-1)$ aritmetika dengan $a=42$, $b=-1$; $S_{20}=\frac{20}{2}(84-19)=650$</sub>
- B. $2.170$  
  <sub>Salah: beda $R$ dikira $3+4=7$ (tanda beda $Q$ diabaikan)</sub>
- C. $672$  
  <sub>Salah: menjumlahkan 21 suku, bukan 20</sub>
- D. $1.300$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{2}$</sub>

**Pembahasan:** Beda $R$ adalah $3+(-4)=-1$, suku pertama $2+40=42$. $S_{20}=\frac{20}{2}(2\cdot42+19\cdot(-1))=10\cdot65=650$.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas10-b02-b-hard-bt01-009
*orisinal | C6 | 5 langkah | jenis: merancang deret dengan batas jumlah*

Suatu deret geometri tak hingga memiliki suku pertama 12 dan rasio $\frac{1}{m}$ dengan $m$ bilangan bulat, $m>1$. Nilai $m$ terbesar sehingga jumlah deret tersebut lebih dari $12{,}5$ adalah ....

- A. $25$  
  <sub>Salah: memakai batas tanpa tanda tegas: $m=25$ memberi jumlah tepat $12{,}5$, bukan lebih</sub>
- B. $12$  
  <sub>Salah: membagi batas: menyederhanakan menjadi $m<12{,}5$</sub>
- **C. $24$** ✅  
  <sub>Benar: $S_\infty=\frac{12}{1-\frac{1}{m}}=\frac{12m}{m-1}>12{,}5$ memberi $m<25$, bilangan bulat terbesar $24$</sub>
- D. $26$  
  <sub>Salah: salah arah: $m=26$ memberi $S_\infty=\frac{312}{25}=12{,}48<12{,}5$</sub>

**Pembahasan:** $\frac{12m}{m-1}>12{,}5 \Rightarrow 24m>25m-25 \Rightarrow m<25$. Karena $m$ bulat, $m\le24$. Cek $m=24$: $\frac{288}{23}\approx12{,}52>12{,}5$; $m=25$: tepat $12{,}5$ (tidak memenuhi).
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas10-b02-b-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: rumus $S_n$ yang menghasilkan deret aritmetika*

Rumus jumlah $n$ suku pertama berikut yang menghasilkan deret aritmetika adalah ....

- A. $S_n=2n^2-3n+1$  
  <sub>Salah: $U_1=0$, $U_2=3$, $U_3=7$: beda $3$ lalu $4$ (konstanta merusak suku pertama)</sub>
- **B. $S_n=2n^2-3n$** ✅  
  <sub>Benar: $U_1=-1$, $U_2=3$, $U_3=7$, dan seterusnya dengan beda tetap $4$</sub>
- C. $S_n=3^n-1$  
  <sub>Salah: menghasilkan $2,6,18,\dots$ (geometri, bukan aritmetika)</sub>
- D. $S_n=n^3+n$  
  <sub>Salah: menghasilkan $2,8,20,\dots$ dengan beda tidak tetap</sub>

**Pembahasan:** Hitung $U_n=S_n-S_{n-1}$. Untuk $S_n=2n^2-3n$: $U_n=4n-5$ (beda tetap 4). Untuk $2n^2-3n+1$: $U_1=0$, $U_2=3$, $U_3=7$ (beda berubah). $3^n-1$: $2,6,18$. $n^3+n$: $2,8,20$.
**Acuan:** siswa — siswa hal.68

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas10-b02-b-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: banding dua deret tak hingga*

Deret $P$: $12+3+\frac{3}{4}+\dots$ adalah deret geometri tak hingga. Deret geometri tak hingga $Q$ memiliki suku pertama 9 dan jumlahnya dua kali jumlah deret $P$. Rasio deret $Q$ adalah ....

- A. $\frac{9}{32}$  
  <sub>Salah: mengira $r=1-r$ langsung, yaitu memberi $1-r$ sebagai rasio</sub>
- B. $\frac{41}{32}$  
  <sub>Salah: tanda terbalik: $r=1+\frac{9}{32}$ (rasio lebih dari 1 sehingga divergen)</sub>
- C. $\frac{1}{2}$  
  <sub>Salah: menggandakan rasio $P$ ($2\cdot\frac{1}{4}$)</sub>
- **D. $\frac{23}{32}$** ✅  
  <sub>Benar: $S_P=\frac{12}{1-\frac{1}{4}}=16$, $S_Q=32=\frac{9}{1-r}$ sehingga $1-r=\frac{9}{32}$ dan $r=\frac{23}{32}$</sub>

**Pembahasan:** $S_P=\frac{12}{1-\frac14}=16$ sehingga $S_Q=32$. $\frac{9}{1-r}=32 \Rightarrow 1-r=\frac{9}{32} \Rightarrow r=\frac{23}{32}$ (memenuhi $|r|<1$).
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas10-b02-b-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: banding jumlah geometri dan aritmetika*

Deret aritmetika $4+10+16+\dots$ dan deret geometri $4+8+16+\dots$ dibandingkan jumlah $n$ suku pertamanya. Bilangan asli $n$ terkecil sehingga jumlah deret geometri lebih besar daripada jumlah deret aritmetika adalah ....

- A. $1$  
  <sub>Salah: pada $n=1$ kedua jumlah sama ($4$), belum lebih besar</sub>
- B. $3$  
  <sub>Salah: $S_3$ geometri $=28$ masih lebih kecil dari aritmetika $30$</sub>
- **C. $4$** ✅  
  <sub>Benar: $S_n$ aritmetika $=n(3n+1)$, geometri $=4(2^n-1)$; pada $n=1,2,3$ geometri sama atau lebih kecil ($4,12,28$ lawan $4,14,30$), pada $n=4$: $60>52$</sub>
- D. $5$  
  <sub>Salah: melewatkan $n=4$ yang sudah memenuhi</sub>

**Pembahasan:** Aritmetika: $S_n=\frac{n}{2}(8+6(n-1))=n(3n+1)$. Geometri ($r=2$): $S_n=4(2^n-1)$. $n=1$: $4,4$; $n=2$: $12,14$; $n=3$: $28,30$; $n=4$: $60,52$. Jadi $n=4$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas10-b02-b-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: menemukan kesalahan rasio negatif*

Seorang siswa menghitung jumlah 6 suku pertama deret $243-81+27-9+\dots$ dengan $r=\frac{1}{3}$ sehingga memperoleh $364$. Jumlah 6 suku pertama yang benar adalah ....

- A. $180$  
  <sub>Salah: hanya menjumlahkan 4 suku</sub>
- B. $364$  
  <sub>Salah: hasil siswa: mengabaikan tanda negatif pada rasio</sub>
- C. $183$  
  <sub>Salah: hanya menjumlahkan 5 suku</sub>
- **D. $182$** ✅  
  <sub>Benar: $r=-\frac{1}{3}$ sehingga $S_6=\frac{243\left(1-\frac{1}{729}\right)}{1+\frac{1}{3}}=182$</sub>

**Pembahasan:** Rasio $\frac{-81}{243}=-\frac{1}{3}$. $S_6=\frac{243(1-(-\frac13)^6)}{1-(-\frac13)}=\frac{243\cdot\frac{728}{729}}{\frac43}=182$. Cek: $243-81+27-9+3-1=182$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas10-b02-b-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: nilai maksimum jumlah deret aritmetika*

Suatu deret aritmetika memiliki suku pertama 50 dan beda $-6$. Nilai terbesar yang dapat dicapai oleh jumlah $n$ suku pertama ($n$ bilangan asli) adalah ....

- A. $230$  
  <sub>Salah: $S_{10}$: ikut menjumlahkan suku negatif $U_{10}=-4$</sub>
- **B. $234$** ✅  
  <sub>Benar: $U_n=56-6n>0$ untuk $n\le9$ ($U_9=2$, $U_{10}=-4$); $S_9=\frac{9}{2}(100-48)=234$</sub>
- C. $468$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{2}$</sub>
- D. $232$  
  <sub>Salah: $S_8$: berhenti satu suku terlalu cepat (suku positif $U_9=2$ belum ikut)</sub>

**Pembahasan:** $U_n=50-6(n-1)=56-6n$. Suku positif sampai $n=9$ ($U_9=2$), $U_{10}=-4$. Jumlah maksimum $S_9=\frac{9}{2}(100-48)=234$; $S_8=232$, $S_{10}=230$.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas10-b02-b-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: dua kemungkinan suku pertama dari $S_\infty$ dan $U_2$*

Suatu deret geometri tak hingga konvergen dengan jumlah 9 dan suku kedua 2. Suku pertama terbesar yang mungkin adalah ....

- A. $12$  
  <sub>Salah: memakai $a=S(1+r)$ dengan $r=\frac{1}{3}$ (tanda tertukar)</sub>
- B. $2$  
  <sub>Salah: mengira suku kedua sebagai suku pertama</sub>
- **C. $6$** ✅  
  <sub>Benar: $a=\frac{2}{r}$ sehingga $9r^2-9r+2=0$, $r=\frac{1}{3}$ atau $\frac{2}{3}$; $a=6$ atau $3$ (keduanya konvergen)</sub>
- D. $3$  
  <sub>Salah: mengambil rasio $\frac{2}{3}$ saja (suku pertama yang lebih kecil)</sub>

**Pembahasan:** $\frac{a}{1-r}=9$ dan $ar=2$. Maka $\frac{2}{r(1-r)}=9 \Rightarrow 9r^2-9r+2=0 \Rightarrow (3r-1)(3r-2)=0$. $r=\frac13 \Rightarrow a=6$; $r=\frac23 \Rightarrow a=3$. Keduanya $|r|<1$; yang terbesar $6$.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
