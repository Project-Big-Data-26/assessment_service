# Lembar koreksi — kelas10 SMA10-B1 subbab C: Fungsi Eksponensial

56 soal | easy 20, medium 20, hard 16 | variasi 20, orisinal 36
> **Kapasitas kurang (hard): 16 dari kuota 20** — Bahan acuan siswa subbab C habis di easy/medium (13 jenis medium sudah memakai hampir semua konsep: fungsi dari data, persentase, waktu target, parameter, tafsir). Hard hanya mencakup penalaran evaluasi klaim, penyangkal, parameter ganda, perbandingan model, dan perancangan; sisanya akan nyaris kembar dengan medium atau di luar materi (transformasi grafik, grafik).

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas10-b01-c-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: nilai fungsi dari cerita*

Seseorang terjangkit virus dan menulari 5 orang lainnya. Pada fase berikutnya, setiap orang yang baru tertular menulari 5 orang lainnya lagi, begitu seterusnya. Banyak orang yang baru tertular pada fase ke-4 adalah ....

- A. $1024$ orang  
  <sub>Salah: menukar basis dan pangkat: $4^{5}$</sub>
- B. $125$ orang  
  <sub>Salah: salah menghitung sebagai fase ke-3: $5^{3}$</sub>
- **C. $625$ orang** ✅  
  <sub>Benar: fase ke-$x$ menghasilkan $5^{x}$ orang, sehingga fase ke-4 adalah $5^{4}=625$</sub>
- D. $20$ orang  
  <sub>Salah: mengalikan $5 \times 4$ alih-alih memangkatkan</sub>

**Pembahasan:** Pola fase 1: $5$, fase 2: $25$, fase 3: $125$, fase 4: $5^{4}=625$.
**Acuan:** siswa — siswa hal.26 Ayo, Bereksplorasi (Eksplorasi 2.3)

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas10-b01-c-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: menyusun model*

Pada awal pengamatan terdapat 40 bakteri pada sebuah inang. Bakteri tersebut membelah menjadi tiga setiap 15 menit. Jika $x$ menyatakan banyak fase pembelahan (setiap 15 menit), model banyak bakteri yang tepat adalah ....

- **A. $f(x) = 40 \cdot 3^{x}$** ✅  
  <sub>Benar: nilai awal 40 dan setiap fase menjadi 3 kali sehingga $f(x)=40\cdot3^{x}$</sub>
- B. $f(x) = 3 \cdot 40^{x}$  
  <sub>Salah: menukar nilai awal dengan bilangan pokok</sub>
- C. $f(x) = 40 + 3x$  
  <sub>Salah: memakai pertambahan tetap (linear) alih-alih pengali tetap</sub>
- D. $f(x) = 40 \cdot x^{3}$  
  <sub>Salah: menukar posisi basis dan pangkat sehingga bukan fungsi eksponensial</sub>

**Pembahasan:** $f(0)=40$, $f(1)=120$, $f(2)=360$, sehingga $f(x)=40\cdot3^{x}$.
**Acuan:** siswa — siswa hal.30 Contoh 3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas10-b01-c-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: nilai fungsi dari cerita*

Pada sebuah media terdapat 6 bakteri. Setiap jam, setiap bakteri membelah menjadi 4 bakteri. Banyak bakteri setelah 3 jam adalah ....

- A. $13824$ bakteri  
  <sub>Salah: memangkatkan hasil kali: $(6\cdot4)^{3}$</sub>
- **B. $384$ bakteri** ✅  
  <sub>Benar: $6\cdot4^{3}=6\cdot64=384$</sub>
- C. $64$ bakteri  
  <sub>Salah: lupa mengalikan dengan banyak bakteri awal</sub>
- D. $72$ bakteri  
  <sub>Salah: mengalikan semua bilangan $6\cdot4\cdot3$</sub>

**Pembahasan:** Model $f(x)=6\cdot4^{x}$, sehingga $f(3)=6\cdot64=384$.
**Acuan:** siswa — siswa hal.33 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas10-b01-c-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: menyusun model*

Sebuah kota berpenduduk 800.000 jiwa. Jumlah penduduknya diprediksi bertambah secara eksponen sebesar 4% setiap tahun. Jika $x$ menyatakan banyak tahun dari sekarang, model jumlah penduduk kota tersebut adalah ....

- A. $f(x) = 800.000\,(0{,}04)^{x}$  
  <sub>Salah: memakai persentase 4% langsung sebagai bilangan pokok</sub>
- B. $f(x) = 800.000\,(4)^{x}$  
  <sub>Salah: memakai 4 sebagai bilangan pokok</sub>
- **C. $f(x) = 800.000\,(1{,}04)^{x}$** ✅  
  <sub>Benar: bertambah 4% berarti faktor pengali per tahun $1+0{,}04=1{,}04$</sub>
- D. $f(x) = 800.000\,(1{,}4)^{x}$  
  <sub>Salah: salah mengubah 4% menjadi 0,4</sub>

**Pembahasan:** Faktor tahunan $1{,}04$, sehingga $f(x)=800.000\,(1{,}04)^{x}$.
**Acuan:** pretest — kelas10-b01-p0033-latihan-22-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas10-b01-c-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: menyusun model*

Massa suatu zat radioaktif mula-mula adalah 2,4 kg. Zat tersebut meluruh 40% setiap jam. Jika $x$ menyatakan banyak jam, model massa zat tersebut adalah ....

- A. $f(x) = 2{,}4\,(1{,}4)^{x}$  
  <sub>Salah: menambah 40% seolah pertumbuhan</sub>
- **B. $f(x) = 2{,}4\,(0{,}6)^{x}$** ✅  
  <sub>Benar: meluruh 40% berarti tersisa 60% sehingga faktor $0{,}6$ per jam</sub>
- C. $f(x) = 2{,}4\,(0{,}4)^{x}$  
  <sub>Salah: memakai tingkat peluruhan sebagai faktor, bukan sisanya</sub>
- D. $f(x) = 2{,}4 - 0{,}4x$  
  <sub>Salah: mengira peluruhan berkurang tetap (linear)</sub>

**Pembahasan:** Sisa tiap jam 60%, jadi $f(x)=2{,}4\,(0{,}6)^{x}$.
**Acuan:** pretest — kelas10-b01-p0036-latihan-23-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas10-b01-c-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: peluruhan dari model cerita*

Dosis obat sebesar 96 mikrogram disuntikkan kepada seorang pasien. Setiap jam, setengah dosis yang ada di dalam tubuh akan luruh dan dikeluarkan. Dosis yang tersisa setelah 3 jam adalah ....

- A. $48$ mikrogram  
  <sub>Salah: hanya menghitung 1 jam</sub>
- B. $32$ mikrogram  
  <sub>Salah: membagi dengan 3 alih-alih membagi dua tiga kali</sub>
- C. $24$ mikrogram  
  <sub>Salah: hanya menghitung 2 jam</sub>
- **D. $12$ mikrogram** ✅  
  <sub>Benar: $96\cdot(\tfrac12)^{3}=96\cdot\tfrac18=12$</sub>

**Pembahasan:** 96 -> 48 -> 24 -> 12 mikrogram.
**Acuan:** siswa — siswa hal.34 Contoh 5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas10-b01-c-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: peluruhan dari model cerita*

Sebanyak 1.000 mg zat disuntikkan ke dalam tubuh pasien. Setiap jam 20% zat yang ada dikeluarkan dari tubuh. Zat yang masih tersisa setelah 2 jam adalah ....

- **A. $640$ mg** ✅  
  <sub>Benar: $1000\cdot(0{,}8)^{2}=640$</sub>
- B. $40$ mg  
  <sub>Salah: memakai faktor 0,2 sebagai bilangan pokok</sub>
- C. $800$ mg  
  <sub>Salah: hanya menghitung 1 jam</sub>
- D. $600$ mg  
  <sub>Salah: mengurangi 20% dari nilai awal dua kali (peluruhan linear)</sub>

**Pembahasan:** Tersisa 80% tiap jam: $1000\to800\to640$.
**Acuan:** siswa — siswa hal.36 Latihan 2.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas10-b01-c-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: nilai fungsi dari cerita*

Pada suatu media terdapat 12 bakteri yang membelah menjadi dua setiap 20 menit. Banyak bakteri setelah 1 jam adalah ....

- **A. $96$ bakteri** ✅  
  <sub>Benar: 1 jam = 3 fase, sehingga $12\cdot2^{3}=96$</sub>
- B. $24$ bakteri  
  <sub>Salah: menganggap 1 jam hanya 1 fase</sub>
- C. $36$ bakteri  
  <sub>Salah: menjumlahkan $12\cdot3$ alih-alih memangkatkan</sub>
- D. $192$ bakteri  
  <sub>Salah: menghitung 4 fase</sub>

**Pembahasan:** 20 menit per fase, 3 fase: $12\to24\to48\to96$.
**Acuan:** siswa — siswa hal.30 Contoh 3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas10-b01-c-easy-bt01-009
*variasi (konteks) | C2 | 2 langkah | jenis: menyusun model*

Sebuah pesan berantai dikirim oleh 1 orang kepada 6 orang. Pada tahap berikutnya, setiap penerima baru meneruskannya kepada 6 orang lain, dan seterusnya. Jika $x$ adalah nomor tahap, banyak penerima baru pada tahap ke-$x$ dinyatakan dengan ....

- A. $f(x) = 6^{x+1}$  
  <sub>Salah: menggeser pangkat sehingga tahap 1 bernilai 36</sub>
- B. $f(x) = 6x$  
  <sub>Salah: mengira pertambahan tetap 6 tiap tahap</sub>
- **C. $f(x) = 6^{x}$** ✅  
  <sub>Benar: tahap 1: 6, tahap 2: 36, tahap 3: 216, sehingga $6^{x}$</sub>
- D. $f(x) = x^{6}$  
  <sub>Salah: menukar basis dan pangkat</sub>

**Pembahasan:** Tiap tahap dikali 6, jadi $f(x)=6^{x}$.
**Acuan:** siswa — siswa hal.26 Ayo, Bereksplorasi (Eksplorasi 2.3)

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas10-b01-c-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: nilai fungsi dari cerita*

Banyak pengguna sebuah aplikasi saat ini 5.000 orang dan bertambah 20% setiap tahun secara eksponen. Banyak pengguna 3 tahun lagi adalah ....

- A. $8.000$ orang  
  <sub>Salah: menambah 20% dari nilai awal tiga kali (pertumbuhan linear)</sub>
- **B. $8.640$ orang** ✅  
  <sub>Benar: $5000\cdot(1{,}2)^{3}=5000\cdot1{,}728=8640$</sub>
- C. $18.000$ orang  
  <sub>Salah: mengalikan faktor $1{,}2\times3=3{,}6$</sub>
- D. $7.200$ orang  
  <sub>Salah: hanya menghitung 2 tahun</sub>

**Pembahasan:** $5000\to6000\to7200\to8640$.
**Acuan:** pretest — kelas10-b01-p0033-latihan-22-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas10-b01-c-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: pertumbuhan atau peluruhan*

Fungsi berikut yang menyatakan peluruhan eksponensial adalah ....

- A. $f(x) = 7 - 0{,}4x$  
  <sub>Salah: fungsi linear menurun, bukan eksponensial</sub>
- B. $f(x) = 7\cdot1^{x}$  
  <sub>Salah: bilangan pokok 1 menghasilkan fungsi konstan</sub>
- **C. $f(x) = 7\,(0{,}4)^{x}$** ✅  
  <sub>Benar: bilangan pokok $0{,}4$ berada di antara 0 dan 1</sub>
- D. $f(x) = 7\,(2{,}5)^{x}$  
  <sub>Salah: bilangan pokok lebih dari 1 adalah pertumbuhan</sub>

**Pembahasan:** Peluruhan: $f(x)=n\cdot a^{x}$ dengan $0<a<1$.
**Acuan:** siswa — siswa hal.34

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas10-b01-c-easy-bt01-012
*orisinal | C2 | 2 langkah | jenis: pertumbuhan atau peluruhan*

Diberikan $f(x)=\left(\frac{3}{2}\right)^{x}$ dan $g(x)=\left(\frac{2}{3}\right)^{x}$. Pernyataan yang benar adalah ....

- A. $f$ dan $g$ keduanya pertumbuhan eksponensial  
  <sub>Salah: mengabaikan bahwa $\frac{2}{3}<1$</sub>
- **B. $f$ pertumbuhan eksponensial dan $g$ peluruhan eksponensial** ✅  
  <sub>Benar: $\frac{3}{2}>1$ sehingga $f$ tumbuh, $0<\frac{2}{3}<1$ sehingga $g$ meluruh</sub>
- C. $f$ dan $g$ keduanya peluruhan eksponensial  
  <sub>Salah: mengabaikan bahwa $\frac{3}{2}>1$</sub>
- D. $f$ peluruhan eksponensial dan $g$ pertumbuhan eksponensial  
  <sub>Salah: menukar kategori kedua fungsi</sub>

**Pembahasan:** Pertumbuhan jika $a>1$, peluruhan jika $0<a<1$.
**Acuan:** siswa — siswa hal.29

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas10-b01-c-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: syarat bilangan pokok*

Bilangan berikut yang dapat dipakai sebagai bilangan pokok $a$ pada fungsi eksponensial $f(x)=a^{x}$ adalah ....

- A. $0$  
  <sub>Salah: bilangan pokok harus positif</sub>
- **B. $\frac{2}{5}$** ✅  
  <sub>Benar: $\frac{2}{5}>0$ dan tidak sama dengan 1</sub>
- C. $-3$  
  <sub>Salah: bilangan pokok tidak boleh negatif</sub>
- D. $1$  
  <sub>Salah: bilangan pokok tidak boleh 1</sub>

**Pembahasan:** Syarat definisi: $a>0$ dan $a\neq1$.
**Acuan:** siswa — siswa hal.27

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas10-b01-c-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: syarat bilangan pokok*

Jika bilangan pokok $a=1$, fungsi $f(x)=a^{x}$ berubah menjadi ....

- **A. fungsi konstan $f(x)=1$** ✅  
  <sub>Benar: $1^{x}=1$ untuk setiap $x$</sub>
- B. fungsi peluruhan eksponensial  
  <sub>Salah: mengira bilangan pokok 1 membuat nilai turun</sub>
- C. fungsi pertumbuhan eksponensial  
  <sub>Salah: mengira bilangan pokok 1 membuat nilai naik</sub>
- D. fungsi linear $f(x)=x$  
  <sub>Salah: mengira pangkat tetap dipertahankan</sub>

**Pembahasan:** Karena nilainya selalu 1, grafiknya bukan kurva eksponensial; itu sebabnya $a=1$ dikecualikan.
**Acuan:** siswa — siswa hal.27

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas10-b01-c-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: nilai fungsi dari rumus*

Diketahui $f(x)=2\cdot5^{x}$. Nilai $f(2)$ adalah ....

- A. $20$  
  <sub>Salah: menghitung $2\cdot5\cdot2$</sub>
- B. $100$  
  <sub>Salah: mengalikan lebih dulu: $(2\cdot5)^{2}$</sub>
- C. $25$  
  <sub>Salah: lupa mengalikan dengan 2</sub>
- **D. $50$** ✅  
  <sub>Benar: $2\cdot5^{2}=2\cdot25=50$</sub>

**Pembahasan:** $f(2)=2\cdot5^{2}=50$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas10-b01-c-easy-bt01-016
*orisinal | C2 | 1 langkah | jenis: nilai awal dan titik*

Sebuah populasi dimodelkan dengan $f(x)=250\,(0{,}8)^{x}$ dengan $x$ menyatakan banyak hari. Populasi awal (saat $x=0$) adalah ....

- A. $0{,}8$  
  <sub>Salah: mengira bilangan pokok adalah nilai awal</sub>
- B. $1$  
  <sub>Salah: mengira pangkat nol menghasilkan seluruh fungsi bernilai 1</sub>
- C. $200$  
  <sub>Salah: menghitung $250\cdot0{,}8$ (nilai untuk $x=1$)</sub>
- **D. $250$** ✅  
  <sub>Benar: $f(0)=250\cdot(0{,}8)^{0}=250$</sub>

**Pembahasan:** $(0{,}8)^{0}=1$, jadi $f(0)=250$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas10-b01-c-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: nilai awal dan titik*

Grafik fungsi $f(x)=6\cdot3^{x}$ memotong sumbu-$y$ di titik ....

- A. $(0, 18)$  
  <sub>Salah: memakai $f(1)$ sebagai nilai di sumbu-$y$</sub>
- B. $(6, 0)$  
  <sub>Salah: menukar absis dan ordinat</sub>
- C. $(0, 1)$  
  <sub>Salah: mengira $a^{0}=1$ tanpa mengalikan 6</sub>
- **D. $(0, 6)$** ✅  
  <sub>Benar: $f(0)=6\cdot3^{0}=6$</sub>

**Pembahasan:** Sumbu-$y$ saat $x=0$: $f(0)=6$, titiknya $(0,6)$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas10-b01-c-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: fungsi dari tabel*

| $x$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| $f(x)$ | 5 | 15 | 45 | 135 |

Perhatikan tabel berikut. Fungsi eksponensial yang sesuai dengan tabel adalah ....

- A. $f(x) = 3\cdot5^{x}$  
  <sub>Salah: menukar nilai awal dan rasio</sub>
- B. $f(x) = 5 + 10x$  
  <sub>Salah: memakai pertambahan tetap, tidak cocok untuk $f(2)=45$</sub>
- **C. $f(x) = 5\cdot3^{x}$** ✅  
  <sub>Benar: $f(0)=5$ dan rasio tiap kenaikan $x$ adalah $15/5=3$</sub>
- D. $f(x) = 15^{x}$  
  <sub>Salah: tidak sesuai karena $f(0)=1$, bukan 5</sub>

**Pembahasan:** Rasio 3 dan nilai awal 5 memberi $f(x)=5\cdot3^{x}$; cek $f(3)=135$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas10-b01-c-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: fungsi dari tabel*

| $x$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| $f(x)$ | 64 | 32 | 16 | 8 |

Perhatikan tabel berikut. Fungsi eksponensial yang sesuai dengan tabel adalah ....

- A. $f(x) = 64 - 32x$  
  <sub>Salah: memakai pengurangan tetap, tidak cocok untuk $f(2)=16$</sub>
- B. $f(x) = 64\cdot2^{x}$  
  <sub>Salah: menukar rasio $\frac12$ dengan 2 (pertumbuhan)</sub>
- C. $f(x) = \frac{1}{2}\cdot64^{x}$  
  <sub>Salah: menukar nilai awal dan rasio</sub>
- **D. $f(x) = 64\left(\frac{1}{2}\right)^{x}$** ✅  
  <sub>Benar: $f(0)=64$ dan rasio tiap kenaikan $x$ adalah $\frac{32}{64}=\frac12$</sub>

**Pembahasan:** Nilai awal 64, rasio $\frac12$, cek $f(3)=8$.
**Acuan:** siswa — siswa hal.35

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas10-b01-c-easy-bt01-020
*orisinal | C2 | 1 langkah | jenis: tafsir faktor pertumbuhan*

Banyak ikan di sebuah kolam dimodelkan dengan $f(x)=75\cdot4^{x}$ dengan $x$ menyatakan banyak tahun. Setiap tahun, banyak ikan menjadi ... kali banyak ikan tahun sebelumnya.

- **A. $4$** ✅  
  <sub>Benar: bilangan pokok 4 adalah pengali tiap tahun</sub>
- B. $75$  
  <sub>Salah: mengira nilai awal adalah pengali</sub>
- C. $300$  
  <sub>Salah: mengalikan $75\cdot4$</sub>
- D. $79$  
  <sub>Salah: menjumlahkan 75 dan 4</sub>

**Pembahasan:** $f(x+1)/f(x)=4$, jadi menjadi 4 kali lipat.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas10-b01-c-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: fungsi dari dua data*

Sebuah koloni bakteri membelah dengan faktor pengali tetap setiap jam. Pada akhir jam ke-1 terdapat 600 bakteri dan pada akhir jam ke-3 terdapat 5.400 bakteri. Banyak bakteri pada akhir jam ke-6 adalah ....

- **A. $145.800$ bakteri** ✅  
  <sub>Benar: $a^{2}=5400/600=9$ sehingga $a=3$ dan $n=600/3=200$; $f(6)=200\cdot3^{6}=145.800$</sub>
- B. $437.400$ bakteri  
  <sub>Salah: menganggap 600 sebagai nilai awal: $600\cdot3^{6}$</sub>
- C. $12.600$ bakteri  
  <sub>Salah: memakai pertambahan tetap (linear) $2.400$ per jam</sub>
- D. $48.600$ bakteri  
  <sub>Salah: menghitung untuk jam ke-5, yaitu $600\cdot3^{4}$</sub>

**Pembahasan:** Dari $f(1)=600$ dan $f(3)=5400$: $a^{2}=9$, $a=3$, $n=200$. Jadi $f(6)=200\cdot729=145.800$.
**Acuan:** siswa — siswa hal.32 Contoh 4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas10-b01-c-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: fungsi dari dua data*

Populasi lalat buah di sebuah laboratorium bertambah menurut faktor pengali tetap tiap hari. Pada hari ke-2 tercatat 80 ekor dan pada hari ke-4 tercatat 1.280 ekor. Populasi lalat buah pada hari ke-5 adalah ....

- A. $20.480$ ekor  
  <sub>Salah: memakai faktor 16 (untuk 2 hari) sebagai faktor satu hari</sub>
- B. $1.880$ ekor  
  <sub>Salah: memakai pertambahan tetap $600$ ekor per hari (linear)</sub>
- **C. $5.120$ ekor** ✅  
  <sub>Benar: $a^{2}=1280/80=16$ sehingga $a=4$; hari ke-5 adalah $1280\cdot4=5120$</sub>
- D. $2.560$ ekor  
  <sub>Salah: memakai faktor pengali 2 alih-alih 4</sub>

**Pembahasan:** Faktor harian $a=4$ sehingga hari ke-5 adalah $1280\cdot4=5120$.
**Acuan:** siswa — siswa hal.32 Contoh 4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas10-b01-c-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: pertumbuhan majemuk*

Pada tahun 2021 jumlah kasus suatu penyakit di sebuah provinsi adalah 40.000 jiwa. Jumlah kasus diprediksi meningkat secara eksponen sebesar 25% setiap tahun. Jumlah kasus pada tahun 2024 adalah ....

- A. $70.000$ jiwa  
  <sub>Salah: menambah 25% dari nilai awal tiga kali (pertumbuhan linear)</sub>
- **B. $78.125$ jiwa** ✅  
  <sub>Benar: $40.000\cdot(1{,}25)^{3}=40.000\cdot1{,}953125=78.125$</sub>
- C. $150.000$ jiwa  
  <sub>Salah: mengalikan faktor $1{,}25\times3=3{,}75$</sub>
- D. $62.500$ jiwa  
  <sub>Salah: hanya menghitung 2 tahun</sub>

**Pembahasan:** Dari 2021 ke 2024 ada 3 tahun: $40.000\to50.000\to62.500\to78.125$.
**Acuan:** siswa — siswa hal.33 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas10-b01-c-medium-bt01-004
*variasi (konteks) | C3 | 3 langkah | jenis: pertumbuhan majemuk*

Harga sebuah rumah saat ini Rp500.000.000 dan diperkirakan naik secara eksponen 10% setiap tahun. Kenaikan harga rumah tersebut setelah 3 tahun dari sekarang adalah ....

- **A. Rp165.500.000** ✅  
  <sub>Benar: $500\,\text{juta}\cdot(1{,}1)^{3}=665{,}5\,\text{juta}$, selisih terhadap harga awal $165{,}5$ juta</sub>
- B. Rp105.000.000  
  <sub>Salah: hanya menghitung kenaikan 2 tahun</sub>
- C. Rp665.500.000  
  <sub>Salah: menjawab harga akhir, bukan kenaikannya</sub>
- D. Rp150.000.000  
  <sub>Salah: menambah 10% dari harga awal tiga kali (linear)</sub>

**Pembahasan:** Harga: $500\to550\to605\to665{,}5$ juta; kenaikan $=665{,}5-500=165{,}5$ juta.
**Acuan:** siswa — siswa hal.33 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas10-b01-c-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: peluruhan majemuk*

Massa suatu zat radioaktif adalah 5 kg. Tingkat peluruhan zat tersebut adalah 20% setiap jam. Massa zat radioaktif tersebut 3 jam kemudian adalah ....

- A. $3{,}2$ kg  
  <sub>Salah: hanya menghitung 2 jam</sub>
- B. $0{,}04$ kg  
  <sub>Salah: memakai faktor $0{,}2$ sebagai bilangan pokok</sub>
- **C. $2{,}56$ kg** ✅  
  <sub>Benar: $5\cdot(0{,}8)^{3}=5\cdot0{,}512=2{,}56$</sub>
- D. $2$ kg  
  <sub>Salah: mengurangi 20% dari massa awal tiga kali (peluruhan linear)</sub>

**Pembahasan:** Faktor sisa $0{,}8$: $5\to4\to3{,}2\to2{,}56$ kg.
**Acuan:** siswa — siswa hal.36 Latihan 2.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas10-b01-c-medium-bt01-006
*variasi (konteks) | C3 | 3 langkah | jenis: peluruhan majemuk*

Sebuah mobil dibeli seharga Rp160.000.000 dan nilainya menyusut secara eksponen 25% setiap tahun. Besar penyusutan nilai mobil tersebut setelah 3 tahun adalah ....

- A. Rp40.000.000  
  <sub>Salah: hanya menghitung penyusutan tahun pertama</sub>
- **B. Rp92.500.000** ✅  
  <sub>Benar: nilai setelah 3 tahun $160\cdot(0{,}75)^{3}=67{,}5$ juta, sehingga penyusutan $160-67{,}5=92{,}5$ juta</sub>
- C. Rp67.500.000  
  <sub>Salah: menjawab nilai akhir, bukan penyusutannya</sub>
- D. Rp120.000.000  
  <sub>Salah: mengurangi 25% dari nilai awal tiga kali (linear)</sub>

**Pembahasan:** Nilai: $160\to120\to90\to67{,}5$ juta; penyusutan total $92{,}5$ juta.
**Acuan:** siswa — siswa hal.36 Latihan 2.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas10-b01-c-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: waktu mencapai target*

Dosis obat sebesar 300 mikrogram disuntikkan kepada seorang pasien. Setiap jam, setengah dosis yang ada di dalam tubuh akan luruh dan dikeluarkan. Paling sedikit berapa jam diperlukan agar dosis yang tersisa kurang dari 5 mikrogram?

- A. $7$ jam  
  <sub>Salah: benar kurang dari 5 mikrogram tetapi bukan yang paling sedikit</sub>
- **B. $6$ jam** ✅  
  <sub>Benar: $300\cdot(\tfrac12)^{x}<5$ berarti $2^{x}>60$; $2^{5}=32$ belum cukup, $2^{6}=64$ cukup</sub>
- C. $5$ jam  
  <sub>Salah: memilih $2^{5}=32$ padahal dosis masih $9{,}375$ mikrogram</sub>
- D. $4$ jam  
  <sub>Salah: dosis masih $18{,}75$ mikrogram</sub>

**Pembahasan:** Dosis: 150, 75, 37,5, 18,75, 9,375, 4,6875. Pertama kali kurang dari 5 pada jam ke-6.
**Acuan:** siswa — siswa hal.35 Ayo, Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas10-b01-c-medium-bt01-008
*variasi (konteks) | C3 | 3 langkah | jenis: waktu mencapai target*

Sebuah koloni ragi berjumlah 5 sel pada awal pengamatan dan menjadi dua kali lipat setiap jam. Paling sedikit berapa jam diperlukan agar jumlah sel lebih dari 1.000?

- **A. $8$ jam** ✅  
  <sub>Benar: $5\cdot2^{x}>1000$ berarti $2^{x}>200$; $2^{7}=128$ belum cukup, $2^{8}=256$ cukup</sub>
- B. $7$ jam  
  <sub>Salah: jumlah sel baru $640$, belum melebihi 1.000</sub>
- C. $6$ jam  
  <sub>Salah: jumlah sel baru $320$</sub>
- D. $9$ jam  
  <sub>Salah: memang lebih dari 1.000 tetapi bukan yang paling sedikit</sub>

**Pembahasan:** Jumlah sel: 10, 20, 40, 80, 160, 320, 640, 1.280. Terpenuhi pada jam ke-8.
**Acuan:** siswa — siswa hal.35 Ayo, Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas10-b01-c-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: jumlah beberapa model*

Tiga koloni bakteri masing-masing berawal dari 6, 18, dan 54 sel. Setiap jam, jumlah sel pada tiap koloni menjadi tiga kali lipat. Jumlah seluruh sel dari ketiga koloni setelah 2 jam adalah ....

- A. $234$ sel  
  <sub>Salah: hanya menghitung 1 jam</sub>
- B. $156$ sel  
  <sub>Salah: mengalikan dengan 2 alih-alih $3^{2}$</sub>
- C. $468$ sel  
  <sub>Salah: mengalikan dengan $3\cdot2=6$ alih-alih memangkatkan</sub>
- **D. $702$ sel** ✅  
  <sub>Benar: model $f(x)=n\cdot3^{x}$, sehingga $(6+18+54)\cdot3^{2}=78\cdot9=702$</sub>

**Pembahasan:** Jumlah awal $78$, pada $x=2$ menjadi $78\cdot9=702$.
**Acuan:** siswa — siswa hal.31 Ayo, Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas10-b01-c-medium-bt01-010
*variasi (angka) | C3 | 4 langkah | jenis: selisih nilai fungsi*

Sebuah koloni berawal dari 5 bakteri. Setiap 10 menit, tiap bakteri membelah menjadi tiga. Pertambahan banyak bakteri antara menit ke-30 dan menit ke-50 adalah ....

- A. $405$ bakteri  
  <sub>Salah: menghitung nilai untuk fase 4 saja</sub>
- B. $216$ bakteri  
  <sub>Salah: lupa mengalikan dengan 5 bakteri awal</sub>
- **C. $1.080$ bakteri** ✅  
  <sub>Benar: menit ke-30 adalah fase 3: $5\cdot3^{3}=135$; menit ke-50 adalah fase 5: $5\cdot3^{5}=1215$; selisih $1080$</sub>
- D. $1.215$ bakteri  
  <sub>Salah: menjawab banyak bakteri menit ke-50, bukan selisihnya</sub>

**Pembahasan:** $f(x)=5\cdot3^{x}$; $f(5)-f(3)=1215-135=1080$.
**Acuan:** siswa — siswa hal.33 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas10-b01-c-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: fungsi dari dua data*

Diketahui $f(x)=n\cdot a^{x}$ dengan $a>0$. Jika $f(1)=6$ dan $f(3)=54$, nilai $f(4)$ adalah ....

- A. $486$  
  <sub>Salah: memakai $a=9$ sebagai faktor satu langkah: $54\cdot9$</sub>
- B. $108$  
  <sub>Salah: menganggap nilai hanya naik dua kali dari $f(3)$</sub>
- C. $78$  
  <sub>Salah: memakai pertambahan tetap $24$ per langkah (linear)</sub>
- **D. $162$** ✅  
  <sub>Benar: $a^{2}=54/6=9$ sehingga $a=3$, $n=2$; $f(4)=2\cdot3^{4}=162$</sub>

**Pembahasan:** $f(3)/f(1)=a^{2}=9$, $a=3$; $n=6/3=2$; $f(4)=2\cdot81=162$.
**Acuan:** siswa — siswa hal.32

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas10-b01-c-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: fungsi dari tabel*

| $x$ | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| $f(x)$ | 36 | 108 | 324 | 972 |

Perhatikan tabel berikut. Fungsi eksponensial $f(x)=n\cdot a^{x}$ yang sesuai dengan tabel adalah ....

- A. $f(x) = 12\cdot3^{x}$  
  <sub>Salah: menghitung $n=36/3$, lupa memangkatkan $a$ dengan 2</sub>
- B. $f(x) = 3\cdot4^{x}$  
  <sub>Salah: menukar nilai awal dan bilangan pokok</sub>
- **C. $f(x) = 4\cdot3^{x}$** ✅  
  <sub>Benar: rasio $108/36=3$ sehingga $a=3$; dari $f(2)=n\cdot9=36$ diperoleh $n=4$</sub>
- D. $f(x) = 36\cdot3^{x}$  
  <sub>Salah: memakai nilai $f(2)$ sebagai nilai awal</sub>

**Pembahasan:** Cek: $4\cdot27=108$, $4\cdot81=324$, $4\cdot243=972$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas10-b01-c-medium-bt01-013
*orisinal | C3 | 4 langkah | jenis: waktu mencapai target*

Populasi jamur pada awal pengamatan adalah 4 satuan dan menjadi tiga kali lipat setiap 3 hari. Populasi jamur tepat 324 satuan setelah ... hari.

- A. $4$  
  <sub>Salah: tidak mengubah banyak fase menjadi hari</sub>
- B. $27$  
  <sub>Salah: membagi 81 dengan 3 lalu menganggapnya hari</sub>
- C. $81$  
  <sub>Salah: menganggap $3^{x}=81$ memberi $x=81$</sub>
- **D. $12$** ✅  
  <sub>Benar: $4\cdot3^{x}=324$ berarti $3^{x}=81=3^{4}$, $x=4$ fase; $4\times3=12$ hari</sub>

**Pembahasan:** $3^{x}=81$ memberi $x=4$ fase; tiap fase 3 hari sehingga 12 hari.
**Acuan:** siswa — siswa hal.29

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas10-b01-c-medium-bt01-014
*orisinal | C3 | 4 langkah | jenis: waktu mencapai target*

Massa suatu zat adalah 1.600 gram dan massanya menjadi setengah kali setiap 3 jam. Massa zat tersebut tepat 25 gram setelah ... jam.

- A. $64$  
  <sub>Salah: menganggap $2^{x}=64$ memberi $x=64$</sub>
- B. $6$  
  <sub>Salah: tidak mengubah banyak fase menjadi jam</sub>
- **C. $18$** ✅  
  <sub>Benar: $(\tfrac12)^{x}=25/1600=\tfrac1{64}$ sehingga $x=6$ fase; $6\times3=18$ jam</sub>
- D. $12$  
  <sub>Salah: mengira $2^{4}=64$ sehingga 4 fase</sub>

**Pembahasan:** $2^{x}=64$ sehingga $x=6$ fase, atau $18$ jam.
**Acuan:** siswa — siswa hal.34

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas10-b01-c-medium-bt01-015
*orisinal | C4 | 4 langkah | jenis: perbandingan dua model*

Banyak sel koloni A dimodelkan $A(x)=200\cdot2^{x}$ dan koloni B dimodelkan $B(x)=50\cdot4^{x}$ dengan $x$ banyak jam. Kedua koloni sama banyak pada $x=$ ....

- A. $4$  
  <sub>Salah: menganggap hasil $2^{x}=4$ sebagai nilai $x$</sub>
- B. $1$  
  <sub>Salah: pada $x=1$ nilainya $400$ untuk A dan $200$ untuk B</sub>
- C. $3$  
  <sub>Salah: pada $x=3$ nilainya $1600$ untuk A dan $3200$ untuk B</sub>
- **D. $2$** ✅  
  <sub>Benar: $50\cdot4^{x}=200\cdot2^{x}$ berarti $\frac{4^{x}}{2^{x}}=2^{x}=4$ sehingga $x=2$</sub>

**Pembahasan:** Pada $x=2$: $A=800$ dan $B=50\cdot16=800$.
**Acuan:** siswa — siswa hal.27

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas10-b01-c-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: persentase dari data*

Nilai sebuah investasi Rp5.000.000 menjadi Rp7.200.000 setelah 2 tahun. Jika pertumbuhannya eksponen dengan persentase tetap setiap tahun, persentase pertumbuhan tahunannya adalah ....

- A. $44\%$  
  <sub>Salah: memakai kenaikan total 2 tahun sebagai kenaikan tahunan</sub>
- B. $22\%$  
  <sub>Salah: membagi kenaikan total $44\%$ dengan 2 (pertumbuhan linear)</sub>
- C. $120\%$  
  <sub>Salah: menjawab faktor $1{,}2$ sebagai persentase tanpa mengurangi 1</sub>
- **D. $20\%$** ✅  
  <sub>Benar: $a^{2}=7,2/5=1{,}44$ sehingga $a=1{,}2$, yaitu naik $20\%$ per tahun</sub>

**Pembahasan:** Faktor tahunan $\sqrt{1{,}44}=1{,}2$ sehingga pertumbuhan $20\%$ per tahun.
**Acuan:** siswa — siswa hal.33

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas10-b01-c-medium-bt01-017
*orisinal | C3 | 3 langkah | jenis: nilai fungsi eksponen negatif*

Diketahui $f(x)=81\left(\frac{1}{3}\right)^{x}$. Nilai $f(2)+f(-1)$ adalah ....

- **A. $252$** ✅  
  <sub>Benar: $f(2)=81\cdot\frac19=9$, $f(-1)=81\cdot3=243$, jumlahnya $252$</sub>
- B. $-18$  
  <sub>Salah: mengira $\left(\frac13\right)^{-1}=-\frac13$ sehingga $f(-1)=-27$</sub>
- C. $243$  
  <sub>Salah: hanya menghitung $f(-1)$</sub>
- D. $36$  
  <sub>Salah: mengira $\left(\frac13\right)^{-1}=\frac13$ sehingga $f(-1)=27$</sub>

**Pembahasan:** $\left(\frac13\right)^{-1}=3$, jadi $f(-1)=243$; $f(2)=9$; jumlah $252$.
**Acuan:** siswa — siswa hal.27

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas10-b01-c-medium-bt01-018
*orisinal | C4 | 3 langkah | jenis: syarat parameter*

Fungsi $f(x)=(2k-5)^{x}$ merupakan fungsi pertumbuhan eksponensial. Bilangan bulat $k$ terkecil yang memenuhi adalah ....

- **A. $4$** ✅  
  <sub>Benar: pertumbuhan jika $2k-5>1$ sehingga $k>3$; bilangan bulat terkecil $4$</sub>
- B. $5$  
  <sub>Salah: memenuhi tetapi bukan yang terkecil</sub>
- C. $3$  
  <sub>Salah: pada $k=3$ bilangan pokok $1$ sehingga fungsi konstan</sub>
- D. $2$  
  <sub>Salah: pada $k=2$ bilangan pokok $-1$ sehingga bukan fungsi eksponensial</sub>

**Pembahasan:** $2k-5>1\Rightarrow k>3$, sehingga $k=4$ (bilangan pokok $3$).
**Acuan:** siswa — siswa hal.29

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas10-b01-c-medium-bt01-019
*orisinal | C4 | 4 langkah | jenis: tafsir model*

Nilai sebuah mesin (dalam juta rupiah) dimodelkan dengan $f(x)=240\,(0{,}85)^{x}$ dengan $x$ banyak tahun sejak dibeli. Pernyataan yang benar adalah ....

- A. nilai mesin naik $15\%$ setiap tahun dan setelah 2 tahun bernilai Rp317,4 juta  
  <sub>Salah: mengira bilangan pokok $0{,}85$ menunjukkan kenaikan</sub>
- **B. nilai mesin turun $15\%$ setiap tahun dan setelah 2 tahun bernilai Rp173,4 juta** ✅  
  <sub>Benar: $0{,}85=1-0{,}15$ sehingga turun $15\%$ per tahun; $f(2)=240\cdot0{,}7225=173{,}4$</sub>
- C. nilai mesin turun $15\%$ setiap tahun dan setelah 2 tahun bernilai Rp168 juta  
  <sub>Salah: memakai penurunan tetap $36$ juta per tahun (linear)</sub>
- D. nilai mesin turun $85\%$ setiap tahun dan setelah 2 tahun bernilai Rp5,4 juta  
  <sub>Salah: menyamakan faktor $0{,}85$ dengan penurunan $85\%$</sub>

**Pembahasan:** Faktor $0{,}85$ berarti tersisa $85\%$ atau turun $15\%$; $f(2)=240\cdot0{,}7225=173{,}4$ juta.
**Acuan:** siswa — siswa hal.34

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas10-b01-c-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: peluruhan berulang (pantulan)*

Sebuah bola dijatuhkan dari ketinggian 5 meter. Setiap kali memantul, bola mencapai $\frac{2}{5}$ dari tinggi pantulan sebelumnya (pantulan pertama mencapai $\frac{2}{5}$ dari 5 meter). Tinggi pantulan ke-3 adalah ....

- A. $1{,}2$ meter  
  <sub>Salah: menghitung $3\cdot\frac25$ (mengalikan banyak pantulan)</sub>
- **B. $0{,}32$ meter** ✅  
  <sub>Benar: $5\cdot\left(\frac25\right)^{3}=5\cdot\frac{8}{125}=0{,}32$</sub>
- C. $0{,}8$ meter  
  <sub>Salah: menghitung pantulan ke-2</sub>
- D. $0{,}064$ meter  
  <sub>Salah: memangkatkan $\frac25$ tanpa mengalikan tinggi awal 5</sub>

**Pembahasan:** Tinggi: $2\to0{,}8\to0{,}32$ meter.
**Acuan:** siswa — siswa hal.36

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas10-b01-c-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim peluruhan*

Seorang siswa menyatakan, "Zat yang meluruh $20\%$ setiap tahun secara eksponen akan habis setelah $5$ tahun karena $5\times20\%=100\%$." Pernyataan yang benar mengenai klaim tersebut adalah ....

- **A. klaim keliru: zat tidak habis, setelah 5 tahun tersisa sekitar $32{,}8\%$ dari massa awal** ✅  
  <sub>Benar: faktor sisa tiap tahun $0{,}8$ sehingga setelah 5 tahun $0{,}8^{5}=0{,}32768\approx32{,}8\%$; peluruhan eksponen tidak pernah mencapai nol</sub>
- B. klaim keliru: setelah 5 tahun tersisa sekitar $20\%$ dari massa awal  
  <sub>Salah: memakai persentase peluruhan $20\%$ sebagai persentase sisa</sub>
- C. klaim benar: zat habis tepat setelah 5 tahun karena persentase penurunan dijumlahkan  
  <sub>Salah: menjumlahkan persentase seolah peluruhan linear</sub>
- D. klaim keliru: setelah 5 tahun tersisa sekitar $67{,}2\%$ dari massa awal  
  <sub>Salah: menjawab banyaknya yang meluruh ($100\%-32{,}8\%$), bukan yang tersisa</sub>

**Pembahasan:** Sisa $=0{,}8^{5}=0{,}32768$, yaitu sekitar $32{,}8\%$ dari massa awal. Peluruhan eksponen tidak membuat zat habis dalam waktu terbatas.
**Acuan:** siswa — siswa hal.34

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas10-b01-c-hard-bt01-002
*orisinal | C5 | 5 langkah | jenis: evaluasi klaim waktu berlipat*

Nilai sebuah aset naik secara eksponen $10\%$ setiap tahun. Seorang analis menyatakan nilai aset tersebut menjadi dua kali lipat setelah $10$ tahun karena $10\times10\%=100\%$. Banyak tahun paling sedikit agar nilai aset lebih dari dua kali nilai awal adalah ....

- A. $9$ tahun  
  <sub>Salah: memenuhi lebih dari dua kali, tetapi bukan yang paling sedikit</sub>
- **B. $8$ tahun** ✅  
  <sub>Benar: $1{,}1^{7}\approx1{,}95<2$ dan $1{,}1^{8}\approx2{,}14>2$, sehingga paling sedikit 8 tahun</sub>
- C. $7$ tahun  
  <sub>Salah: $1{,}1^{7}\approx1{,}95$ masih kurang dari 2</sub>
- D. $10$ tahun  
  <sub>Salah: mempercayai klaim penjumlahan persentase (linear)</sub>

**Pembahasan:** Faktor: $1{,}1^{6}\approx1{,}77$; $1{,}1^{7}\approx1{,}95$; $1{,}1^{8}\approx2{,}14$. Jadi 8 tahun, bukan 10 tahun.
**Acuan:** siswa — siswa hal.29

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas10-b01-c-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan fase*

Sebuah koloni berawal dari $6$ bakteri dan menjadi tiga kali lipat setiap $2$ jam. Dina menghitung banyak bakteri setelah $8$ jam dengan $6\cdot3^{8}=39.366$. Banyak bakteri setelah $8$ jam yang benar adalah ....

- A. $72$ bakteri  
  <sub>Salah: mengalikan $6\cdot3\cdot4$ alih-alih memangkatkan</sub>
- B. $39.366$ bakteri  
  <sub>Salah: memakai banyak jam sebagai pangkat (kesalahan Dina)</sub>
- C. $54$ bakteri  
  <sub>Salah: mengira $8$ jam hanya $2$ fase</sub>
- **D. $486$ bakteri** ✅  
  <sub>Benar: $8$ jam $=4$ fase (tiap 2 jam), sehingga $6\cdot3^{4}=486$</sub>

**Pembahasan:** Kesalahan Dina: pangkat harus banyak fase, yaitu $8/2=4$. Jadi $6\cdot3^{4}=6\cdot81=486$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas10-b01-c-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: bandingkan pertumbuhan dan peluruhan*

Dua tabungan masing-masing berawal Rp1.000.000. Tabungan P bertambah $5\%$ per tahun secara eksponen, sedangkan nilai tabungan Q menyusut $5\%$ per tahun secara eksponen. Selisih nilai P dan Q setelah $3$ tahun adalah ....

- A. Rp157.625  
  <sub>Salah: hanya menghitung pertambahan P, lupa memperhitungkan Q</sub>
- B. Rp300.000  
  <sub>Salah: memakai perubahan linear $\pm5\%$ dari nilai awal tiap tahun</sub>
- **C. Rp300.250** ✅  
  <sub>Benar: $P=1.000.000\cdot1{,}05^{3}=1.157.625$; $Q=1.000.000\cdot0{,}95^{3}=857.375$; selisih $300.250$</sub>
- D. Rp200.000  
  <sub>Salah: hanya menghitung selisih setelah 2 tahun</sub>

**Pembahasan:** $1{,}05^{3}=1{,}157625$ dan $0{,}95^{3}=0{,}857375$; selisih $0{,}30025$ dikali satu juta $=300.250$.
**Acuan:** siswa — siswa hal.34

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas10-b01-c-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal*

Klaim: "Jika $a>b>0$, maka $a^{x}>b^{x}$ untuk setiap bilangan bulat $x$." Pasangan $(a,b,x)$ yang merupakan contoh penyangkal klaim tersebut adalah ....

- A. $(a,b,x)=(5,3,2)$  
  <sub>Salah: $25>9$, klaim berlaku sehingga bukan penyangkal</sub>
- B. $(a,b,x)=(3,2,1)$  
  <sub>Salah: $3>2$, klaim berlaku sehingga bukan penyangkal</sub>
- C. $(a,b,x)=\left(\frac12,\frac13,2\right)$  
  <sub>Salah: $\frac14>\frac19$, klaim berlaku sehingga bukan penyangkal</sub>
- **D. $(a,b,x)=(4,2,-1)$** ✅  
  <sub>Benar: $4^{-1}=\frac14<\frac12=2^{-1}$ padahal $4>2$, sehingga klaim tidak berlaku</sub>

**Pembahasan:** Untuk pangkat negatif urutan berbalik: $4^{-1}=\frac14$ lebih kecil dari $2^{-1}=\frac12$. Ketiga pasangan lain memenuhi klaim.
**Acuan:** siswa — siswa hal.27

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas10-b01-c-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: syarat parameter dua fungsi*

Fungsi $f(x)=\left(\frac{m+1}{4}\right)^{x}$ merupakan fungsi peluruhan eksponensial dan fungsi $g(x)=(7-3m)^{x}$ merupakan fungsi pertumbuhan eksponensial. Banyak bilangan bulat $m$ yang memenuhi kedua syarat tersebut adalah ....

- **A. $2$** ✅  
  <sub>Benar: $0<\frac{m+1}{4}<1$ memberi $-1<m<3$; $7-3m>1$ memberi $m<2$; bilangan bulat: $m=0$ dan $m=1$</sub>
- B. $4$  
  <sub>Salah: memasukkan $m=-1$ dan $m=3$ yang membuat $a=0$ dan $a=1$</sub>
- C. $3$  
  <sub>Salah: hanya memakai syarat $f$ sehingga $m=0,1,2$ (pada $m=2$, $g$ konstan)</sub>
- D. $1$  
  <sub>Salah: mengira $m>0$ dan $m<1$</sub>

**Pembahasan:** Untuk $f$: $-1<m<3$. Untuk $g$: $m<2$. Irisan bilangan bulat: $0$ dan $1$. Pada $m=2$, $g(x)=1^{x}$ konstan.
**Acuan:** siswa — siswa hal.29

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas10-b01-c-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: eksponen versus linear*

Tabungan A bertambah tetap Rp200 ribu tiap bulan dari awal Rp1.000 ribu. Tabungan B berawal Rp1.000 ribu dan bertambah $20\%$ tiap bulan secara eksponen. Bilangan asli $x$ terkecil sehingga tabungan B pada bulan ke-$x$ lebih banyak dari tabungan A adalah ....

- A. $3$  
  <sub>Salah: benar B lebih banyak, tetapi bukan yang terkecil</sub>
- **B. $2$** ✅  
  <sub>Benar: $x=1$: A $=1.200$ dan B $=1.200$ (sama); $x=2$: A $=1.400$ dan B $=1.440$</sub>
- C. $5$  
  <sub>Salah: benar B lebih banyak, tetapi bukan yang terkecil</sub>
- D. $1$  
  <sub>Salah: pada bulan ke-1 keduanya sama, bukan lebih banyak</sub>

**Pembahasan:** A: $1.000+200x$, B: $1.000\cdot1{,}2^{x}$. Bulan 1: 1.200 vs 1.200. Bulan 2: 1.400 vs 1.440. Jadi $x=2$.
**Acuan:** siswa — siswa hal.27

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas10-b01-c-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: basis dari nilai fungsi negatif*

Diketahui $f(x)=n\cdot a^{x}$ dengan $a>0$. Jika $f(-1)=12$ dan $f(1)=3$, nilai $f(3)$ adalah ....

- A. $6$  
  <sub>Salah: menjawab nilai awal $n$</sub>
- **B. $\frac34$** ✅  
  <sub>Benar: $f(-1)\cdot f(1)=n^{2}=36$ sehingga $n=6$; dari $n\cdot a=3$ diperoleh $a=\frac12$; $f(3)=6\cdot\frac18=\frac34$</sub>
- C. $12$  
  <sub>Salah: mengira $a=2$ sehingga $n=\frac32$ dan $f(3)=12$</sub>
- D. $\frac38$  
  <sub>Salah: mengira $f(3)=f(1)\cdot a^{3}$ (pangkat dihitung dari 1, bukan 2 langkah)</sub>

**Pembahasan:** $f(-1)=\frac{n}{a}=12$ dan $f(1)=na=3$. Perkalian: $n^{2}=36$, $n=6$, $a=\frac12$. $f(3)=6\cdot\frac18=\frac34$.
**Acuan:** siswa — siswa hal.27

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas10-b01-c-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: persentase lebih dari 100%*

Sebuah koloni berawal dari $10$ ekor dan bertambah $200\%$ dari jumlah sebelumnya setiap hari secara eksponen. Banyak ekor setelah $3$ hari adalah ....

- A. $810$ ekor  
  <sub>Salah: memakai pangkat $4$ ($10\cdot3^{4}$)</sub>
- B. $80$ ekor  
  <sub>Salah: memakai faktor $2$ dari $200\%$ sehingga $10\cdot2^{3}$</sub>
- **C. $270$ ekor** ✅  
  <sub>Benar: bertambah $200\%$ berarti menjadi $100\%+200\%=300\%$ atau faktor $3$; $10\cdot3^{3}=270$</sub>
- D. $70$ ekor  
  <sub>Salah: menambah $20$ ekor tiga kali (linear)</sub>

**Pembahasan:** Faktor tiap hari $1+2=3$. Jumlah: $10\to30\to90\to270$.
**Acuan:** siswa — siswa hal.33

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas10-b01-c-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: dua peluruhan beda periode*

Zat X bermassa $960$ gram dan massanya tersisa setengah kali setiap $2$ jam. Zat Y bermassa $1.280$ gram dan massanya tersisa $\frac34$ kali setiap $3$ jam. Setelah $12$ jam, massa Y lebih banyak dari massa X sebesar ....

- A. $345$ gram  
  <sub>Salah: memakai 4 fase untuk X ($960/16=60$), selisih $405-60$</sub>
- B. $405$ gram  
  <sub>Salah: menjawab massa Y saja</sub>
- C. $525$ gram  
  <sub>Salah: memakai 3 fase untuk Y ($540$), selisih $540-15$</sub>
- **D. $390$ gram** ✅  
  <sub>Benar: X: $12/2=6$ fase, $960\cdot\left(\frac12\right)^{6}=15$; Y: $12/3=4$ fase, $1280\cdot\left(\frac34\right)^{4}=405$; selisih $390$</sub>

**Pembahasan:** X: $960/64=15$ gram. Y: $1280\cdot\frac{81}{256}=405$ gram. Selisih $405-15=390$ gram.
**Acuan:** siswa — siswa hal.34

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas10-b01-c-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: naik lalu turun persentase sama*

Harga sebuah barang Rp2.500.000. Selama $2$ tahun pertama harganya naik $20\%$ per tahun secara eksponen, kemudian selama $2$ tahun berikutnya turun $20\%$ per tahun secara eksponen. Harga barang setelah $4$ tahun adalah ....

- A. Rp2.500.000  
  <sub>Salah: mengira kenaikan dan penurunan $20\%$ saling meniadakan</sub>
- B. Rp2.100.000  
  <sub>Salah: mengira naik $40\%$ lalu turun $40\%$ dari nilai awal ($0{,}84$)</sub>
- C. Rp3.600.000  
  <sub>Salah: hanya menghitung kenaikan 2 tahun pertama</sub>
- **D. Rp2.304.000** ✅  
  <sub>Benar: $2.500.000\cdot1{,}2^{2}\cdot0{,}8^{2}=2.500.000\cdot1{,}44\cdot0{,}64=2.304.000$</sub>

**Pembahasan:** Setelah 2 tahun naik: $3.600.000$. Dua tahun turun: $3.600.000\cdot0{,}64=2.304.000$.
**Acuan:** siswa — siswa hal.33

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas10-b01-c-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: nilai awal dari nilai akhir*

Populasi serangga di sebuah kebun sekarang $8.640$ ekor. Populasi tersebut tumbuh secara eksponen $20\%$ per tahun. Populasi serangga $3$ tahun yang lalu adalah ....

- A. $6.000$ ekor  
  <sub>Salah: hanya membagi untuk 2 tahun ($1{,}2^{2}=1{,}44$)</sub>
- **B. $5.000$ ekor** ✅  
  <sub>Benar: $8.640\div1{,}2^{3}=8.640\div1{,}728=5.000$</sub>
- C. $5.400$ ekor  
  <sub>Salah: membagi $8.640$ dengan $1{,}6$ (menganggap kenaikan $20\%$ linear tiga tahun)</sub>
- D. $7.200$ ekor  
  <sub>Salah: hanya membagi untuk 1 tahun</sub>

**Pembahasan:** $n\cdot1{,}2^{3}=8.640$ sehingga $n=8.640/1{,}728=5.000$.
**Acuan:** siswa — siswa hal.29

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas10-b01-c-hard-bt01-013
*orisinal | C6 | 5 langkah | jenis: merancang model dengan titik potong*

Diketahui $f(x)=5\cdot2^{x}$. Agar grafik $g(x)=k\left(\frac12\right)^{x}$ berpotongan dengan grafik $f$ tepat di titik berabsis $x=2$, nilai $k$ yang harus dipilih adalah ....

- **A. $80$** ✅  
  <sub>Benar: $f(2)=20$; $g(2)=k\cdot\frac14=20$ sehingga $k=80$</sub>
- B. $20$  
  <sub>Salah: mengira $g(2)=k$ sehingga $k=f(2)$</sub>
- C. $5$  
  <sub>Salah: memakai nilai awal $f$ sebagai $k$</sub>
- D. $40$  
  <sub>Salah: mengira $\left(\frac12\right)^{2}=\frac12$ sehingga $k=40$</sub>

**Pembahasan:** Titik berabsis 2: $5\cdot4=20$. $k\cdot\frac14=20$ memberi $k=80$.
**Acuan:** siswa — siswa hal.27

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas10-b01-c-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: temukan data tidak konsisten*

| $x$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| $f(x)$ | 5 | 10 | 20 | 35 |

Sebuah tabel pengamatan memuat data yang seharusnya mengikuti fungsi eksponensial $f(x)=n\cdot a^{x}$. Data pada $x=0,1,2$ dicatat dengan benar, sedangkan data pada $x=3$ salah catat. Nilai $f(3)$ yang seharusnya adalah ....

- **A. $40$** ✅  
  <sub>Benar: rasio $10/5=20/10=2$ sehingga $a=2$; $f(3)=20\cdot2=40$</sub>
- B. $35$  
  <sub>Salah: memakai nilai salah catat pada tabel</sub>
- C. $80$  
  <sub>Salah: mengira $f(3)=f(2)\cdot a^{2}$ dengan $a=2$</sub>
- D. $30$  
  <sub>Salah: menambah $10$ (beda tetap, linear)</sub>

**Pembahasan:** Rasio $a=2$. Maka $f(3)=20\cdot2=40$; nilai $35$ bukan hasil model eksponensial.
**Acuan:** siswa — siswa hal.27

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas10-b01-c-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: hubungan dua fungsi timbal balik*

Diketahui $f(x)=3^{x}$ dan $g(x)=\left(\frac13\right)^{x}$. Pernyataan yang benar adalah ....

- A. $g(-2)=\frac19$ dan $f(-2)=9$  
  <sub>Salah: menukar hasil kedua fungsi</sub>
- B. $g(-2)=-9$ dan $f(-2)=-\frac19$  
  <sub>Salah: menganggap pangkat negatif menghasilkan nilai negatif</sub>
- **C. $g(-2)=9$ dan $f(-2)=\frac19$** ✅  
  <sub>Benar: $g(-2)=\left(\frac13\right)^{-2}=3^{2}=9$ dan $f(-2)=3^{-2}=\frac19$</sub>
- D. $g(-2)=9$ dan $f(-2)=-6$  
  <sub>Salah: mengira $3^{-2}=3\cdot(-2)$</sub>

**Pembahasan:** $g(x)=f(-x)$: $g(-2)=f(2)=9$, dan $f(-2)=\frac{1}{3^{2}}=\frac19$.
**Acuan:** siswa — siswa hal.29

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas10-b01-c-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: bandingkan nilai awal dan laju*

Koloni A berjumlah $1.000$ sel dan bertambah $10\%$ per jam secara eksponen. Koloni B berjumlah $100$ sel dan menjadi dua kali lipat setiap jam. Banyak jam paling sedikit agar koloni B lebih banyak dari koloni A adalah ....

- A. $3$ jam  
  <sub>Salah: A masih $1.331$ sedangkan B baru $800$</sub>
- B. $5$ jam  
  <sub>Salah: benar B lebih banyak, tetapi bukan yang paling sedikit</sub>
- **C. $4$ jam** ✅  
  <sub>Benar: jam ke-3: A $=1.331$, B $=800$; jam ke-4: A $\approx1.464$, B $=1.600$</sub>
- D. $10$ jam  
  <sub>Salah: membandingkan nilai awal $1.000$ dan $100$ sebagai rasio</sub>

**Pembahasan:** A: $1.000\cdot1{,}1^{x}$; B: $100\cdot2^{x}$. $x=3$: 1.331 vs 800. $x=4$: 1.464,1 vs 1.600. Jadi 4 jam.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
