# Lembar koreksi — kelas10 SMA10-B7 subbab C: Aturan Perkalian

60 soal | easy 20, medium 20, hard 20 | variasi 20, orisinal 40

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas10-b07-c-easy-bt01-001
*variasi (konteks) | C1 | 1 langkah | jenis: konsep/rumus*

Dewi melempar sebuah koin setimbang dan mengambil satu kartu dari seperangkat kartu bridge lengkap (52 kartu). Ia ingin tahu peluang bahwa koin menunjukkan angka dan kartu yang terambil adalah As.

Manakah penulisan berikut yang paling tepat menyatakan peluang yang ingin ditentukan Dewi?

- A. $P(\text{koin angka}) - P(\text{kartu As})$  
  <sub>Salah: mengurangkan dua peluang, tidak ada dasarnya</sub>
- B. $P(\text{koin angka}) + P(\text{kartu As})$  
  <sub>Salah: menjumlahkan dua peluang padahal kedua kejadian harus terjadi bersama</sub>
- **C. $P(\text{koin angka dan kartu As})$** ✅  
  <sub>Benar: kata hubung "dan" berarti kedua kejadian harus terjadi bersama</sub>
- D. $P(\text{koin angka atau kartu As})$  
  <sub>Salah: mengira kata "dan" sama dengan "atau"</sub>

**Pembahasan:** Kedua kejadian harus terjadi bersama, jadi ditulis $P(\text{koin angka dan kartu As})$.
**Acuan:** pretest — kelas10-b07-p0276-latihan-7-5-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas10-b07-c-easy-bt01-002
*variasi (konteks) | C2 | 2 langkah | jenis: alasan dan peluang*

Sebuah koin setimbang dan sebuah dadu setimbang dilempar bersamaan. Ratna menang jika koin menunjukkan gambar dan dadu menunjukkan mata kelipatan 3.

Pernyataan manakah yang benar tentang alasan aturan perkalian dapat dipakai dan peluang Ratna menang?

- A. Hasil koin dan dadu tidak saling bebas; peluangnya $\frac{1}{6}$  
  <sub>Salah: alasan keliru: koin dan dadu tidak saling memengaruhi</sub>
- B. Hasil koin dan dadu saling bebas; peluangnya $\frac{5}{6}$  
  <sub>Salah: menjumlahkan $\frac{1}{2} + \frac{2}{6}$ alih-alih mengalikan</sub>
- C. Hasil koin dan dadu saling bebas; peluangnya $\frac{1}{3}$  
  <sub>Salah: hanya menghitung peluang dadu dan lupa peluang koin</sub>
- **D. Hasil koin dan dadu saling bebas; peluangnya $\frac{1}{6}$** ✅  
  <sub>Benar: koin dan dadu tidak saling memengaruhi sehingga $P = \frac{1}{2} \times \frac{2}{6} = \frac{1}{6}$</sub>

**Pembahasan:** Koin dan dadu tidak saling memengaruhi. $P(\text{gambar dan kelipatan 3}) = \frac{1}{2} \times \frac{2}{6} = \frac{1}{6}$.
**Acuan:** pretest — kelas10-b07-p0276-latihan-7-5-1b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas10-b07-c-easy-bt01-003
*variasi (angka) | C2 | 1 langkah | jenis: hitung P(A dan B) dari peluang diketahui*

Sani dan Oka sedang bermain bola basket. Peluang bagi Sani untuk memasukkan bola dalam keranjang adalah 0,6, sedangkan untuk Oka 0,7. Keberhasilan atau kegagalan Sani dan Oka memasukkan bola saling bebas. Sani dan Oka masing-masing melemparkan bola sekali.

Peluang bahwa keduanya memasukkan bola dalam keranjang adalah ....

- A. 0,18  
  <sub>Salah: mengira Oka gagal memasukkan bola</sub>
- B. 0,88  
  <sub>Salah: memakai aturan "atau" ($P(A) + P(B) - P(A \text{ dan } B)$)</sub>
- **C. 0,42** ✅  
  <sub>Benar: kejadian saling bebas sehingga $0,6 \times 0,7 = 0,42$</sub>
- D. 0,12  
  <sub>Salah: menghitung peluang keduanya gagal</sub>

**Pembahasan:** $P(\text{keduanya masuk}) = 0,6 \times 0,7 = 0,42$.
**Acuan:** pretest — kelas10-b07-p0276-latihan-7-5-2a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas10-b07-c-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: hitung P(A dan B) dari peluang diketahui*

Dito dan Eka masing-masing menendang penalti satu kali. Peluang Dito mencetak gol adalah 0,9, sedangkan peluang Eka mencetak gol adalah 0,4. Keberhasilan atau kegagalan keduanya saling bebas.

Peluang bahwa Dito mencetak gol, tetapi Eka tidak, adalah ....

- A. 0,36  
  <sub>Salah: menghitung peluang keduanya mencetak gol</sub>
- B. 0,04  
  <sub>Salah: tertukar: Dito gagal dan Eka mencetak gol</sub>
- **C. 0,54** ✅  
  <sub>Benar: peluang Eka gagal $1 - 0,4 = 0,6$, lalu $0,9 \times 0,6 = 0,54$</sub>
- D. 0,06  
  <sub>Salah: menghitung peluang keduanya gagal</sub>

**Pembahasan:** $P = 0,9 \times (1 - 0,4) = 0,9 \times 0,6 = 0,54$.
**Acuan:** pretest — kelas10-b07-p0276-latihan-7-5-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas10-b07-c-easy-bt01-005
*variasi (konteks) | C2 | 2 langkah | jenis: percobaan berulang dengan pengembalian*

Sebuah kotak berisi 10 kartu bernomor 1 sampai 10. Satu kartu diambil secara acak, dicatat nomornya, lalu dikembalikan ke dalam kotak. Setelah itu satu kartu diambil lagi.

Peluang bahwa kedua kartu bernomor kelipatan 3 adalah ....

- A. $\frac{3}{5}$  
  <sub>Salah: menjumlahkan $\frac{3}{10} + \frac{3}{10}$</sub>
- **B. $\frac{9}{100}$** ✅  
  <sub>Benar: kartu dikembalikan sehingga saling bebas; kelipatan 3 ada 3 (3, 6, 9): $\frac{3}{10} \times \frac{3}{10} = \frac{9}{100}$</sub>
- C. $\frac{3}{100}$  
  <sub>Salah: mengalikan $\frac{3}{10}$ dengan $\frac{1}{10}$</sub>
- D. $\frac{3}{10}$  
  <sub>Salah: hanya menghitung peluang satu pengambilan</sub>

**Pembahasan:** Kelipatan 3: 3, 6, 9 (tiga kartu). $P = \frac{3}{10} \times \frac{3}{10} = \frac{9}{100}$.
**Acuan:** pretest — kelas10-b07-p0276-latihan-7-5-3b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas10-b07-c-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: percobaan berulang dengan pengembalian*

Sebuah roda putar setimbang memiliki 8 sektor sama besar yang diberi nomor 1 sampai 8. Roda diputar dua kali.

Peluang bahwa nomor yang muncul pada kedua putaran berbeda adalah ....

- A. $\frac{1}{64}$  
  <sub>Salah: mengalikan $\frac{1}{8} \times \frac{1}{8}$ (peluang nomor tertentu muncul dua kali)</sub>
- **B. $\frac{7}{8}$** ✅  
  <sub>Benar: putaran pertama bebas; putaran kedua harus beda: $1 \times \frac{7}{8}$</sub>
- C. $\frac{49}{64}$  
  <sub>Salah: mengalikan $\frac{7}{8} \times \frac{7}{8}$ padahal nomor pertama bebas</sub>
- D. $\frac{1}{8}$  
  <sub>Salah: menghitung peluang kedua nomor sama</sub>

**Pembahasan:** Nomor pertama apa saja (peluang 1), nomor kedua harus berbeda ($\frac{7}{8}$). $P = \frac{7}{8}$.
**Acuan:** pretest — kelas10-b07-p0277-latihan-7-5-3d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas10-b07-c-easy-bt01-007
*variasi (angka) | C2 | 1 langkah | jenis: pengambilan bola dengan pengembalian*

Sebuah tas berisi 20 bola dengan warna sebagai berikut: delapan bola merah dan selebihnya berwarna biru. Sebuah bola diambil secara acak dari dalam tas. Bola tersebut kemudian dikembalikan ke dalam tas, dan bola kedua diambil.

Peluang bahwa bola pertama biru dan bola kedua merah adalah ....

- A. $\frac{9}{25}$  
  <sub>Salah: tertukar: kedua bola biru</sub>
- B. $\frac{4}{25}$  
  <sub>Salah: tertukar: kedua bola merah</sub>
- C. $\frac{24}{95}$  
  <sub>Salah: memakai pengambilan tanpa pengembalian ($\frac{12}{20} \times \frac{8}{19}$)</sub>
- **D. $\frac{6}{25}$** ✅  
  <sub>Benar: dengan pengembalian: $\frac{12}{20} \times \frac{8}{20} = \frac{96}{400} = \frac{6}{25}$</sub>

**Pembahasan:** Bola biru ada 12. $P = \frac{12}{20} \times \frac{8}{20} = \frac{6}{25}$.
**Acuan:** pretest — kelas10-b07-p0277-latihan-7-5-4b3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas10-b07-c-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: pengambilan bola dengan pengembalian*

Sebuah kantong berisi 15 kelereng: enam kelereng hijau dan selebihnya kuning. Sebuah kelereng diambil secara acak, dicatat warnanya, lalu dikembalikan ke dalam kantong. Kelereng kedua kemudian diambil.

Peluang bahwa kedua kelereng yang terambil berwarna sama adalah ....

- A. $\frac{12}{25}$  
  <sub>Salah: menghitung peluang warna berbeda</sub>
- **B. $\frac{13}{25}$** ✅  
  <sub>Benar: $\left(\frac{6}{15}\right)^2 + \left(\frac{9}{15}\right)^2 = \frac{4}{25} + \frac{9}{25} = \frac{13}{25}$</sub>
- C. $\frac{4}{25}$  
  <sub>Salah: hanya menghitung kedua hijau</sub>
- D. $\frac{9}{25}$  
  <sub>Salah: hanya menghitung kedua kuning</sub>

**Pembahasan:** Hijau-hijau $\frac{4}{25}$, kuning-kuning $\frac{9}{25}$. Jumlahnya $\frac{13}{25}$.
**Acuan:** pretest — kelas10-b07-p0277-latihan-7-5-4b4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas10-b07-c-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: pengambilan bola dengan pengembalian*

Sebuah kotak berisi 10 lampu, 3 di antaranya rusak. Sebuah lampu diambil secara acak, dicatat kondisinya, lalu dikembalikan ke dalam kotak. Setelah itu lampu kedua diambil.

Peluang bahwa setidaknya satu lampu yang terambil rusak adalah ....

- **A. $\frac{51}{100}$** ✅  
  <sub>Benar: $1 - \left(\frac{7}{10}\right)^2 = 1 - \frac{49}{100} = \frac{51}{100}$</sub>
- B. $\frac{3}{5}$  
  <sub>Salah: menjumlahkan $\frac{3}{10} + \frac{3}{10}$</sub>
- C. $\frac{49}{100}$  
  <sub>Salah: menghitung peluang kedua lampu tidak rusak</sub>
- D. $\frac{9}{100}$  
  <sub>Salah: hanya menghitung kedua lampu rusak</sub>

**Pembahasan:** Peluang tidak ada yang rusak $\left(\frac{7}{10}\right)^2 = \frac{49}{100}$. Setidaknya satu rusak: $1 - \frac{49}{100} = \frac{51}{100}$.
**Acuan:** pretest — kelas10-b07-p0277-latihan-7-5-4b7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas10-b07-c-easy-bt01-010
*variasi (konteks) | C1 | 1 langkah | jenis: percobaan berulang dengan pengembalian*

Sebuah koin setimbang dilempar tiga kali.

Peluang bahwa ketiga lemparan menunjukkan gambar adalah ....

- **A. $\frac{1}{8}$** ✅  
  <sub>Benar: lemparan saling bebas: $\frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{8}$</sub>
- B. $\frac{1}{16}$  
  <sub>Salah: mengalikan empat kali $\frac{1}{2}$</sub>
- C. $\frac{1}{2}$  
  <sub>Salah: hanya menghitung satu lemparan</sub>
- D. $\frac{1}{4}$  
  <sub>Salah: hanya mengalikan dua lemparan</sub>

**Pembahasan:** $P = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{8}$.
**Acuan:** siswa — siswa hal.276 Latihan 7.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas10-b07-c-easy-bt01-011
*variasi (konteks) | C2 | 2 langkah | jenis: pengambilan bola dengan pengembalian*

Sebuah toples berisi 9 permen: 4 permen cokelat dan 5 permen mint. Satu permen diambil secara acak, dilihat jenisnya, lalu dikembalikan ke dalam toples. Setelah itu satu permen diambil lagi.

Peluang bahwa kedua permen yang terambil berbeda jenis adalah ....

- **A. $\frac{40}{81}$** ✅  
  <sub>Benar: $2 \times \frac{4}{9} \times \frac{5}{9} = \frac{40}{81}$ (cokelat-mint atau mint-cokelat)</sub>
- B. $\frac{5}{9}$  
  <sub>Salah: memakai pengambilan tanpa pengembalian ($\frac{5}{8}$ pada pengambilan kedua)</sub>
- C. $\frac{20}{81}$  
  <sub>Salah: hanya menghitung satu urutan (cokelat lalu mint)</sub>
- D. $\frac{41}{81}$  
  <sub>Salah: menghitung peluang kedua permen sama jenis</sub>

**Pembahasan:** Dua urutan: cokelat-mint dan mint-cokelat, masing-masing $\frac{20}{81}$. Jumlah $\frac{40}{81}$.
**Acuan:** siswa — siswa hal.277 Latihan 7.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas10-b07-c-easy-bt01-012
*variasi (konteks) | C2 | 2 langkah | jenis: pengambilan bola dengan pengembalian*

Sebuah kotak undian berisi 20 kertas: 5 kertas berhadiah dan selebihnya kosong. Satu kertas diambil secara acak, dicatat, lalu dikembalikan ke dalam kotak. Satu kertas kemudian diambil lagi.

Peluang bahwa kedua kertas yang terambil tidak berhadiah adalah ....

- A. $\frac{1}{16}$  
  <sub>Salah: menghitung peluang kedua kertas berhadiah</sub>
- B. $\frac{3}{8}$  
  <sub>Salah: menghitung peluang tepat satu kertas berhadiah</sub>
- **C. $\frac{9}{16}$** ✅  
  <sub>Benar: $\frac{15}{20} \times \frac{15}{20} = \frac{3}{4} \times \frac{3}{4} = \frac{9}{16}$</sub>
- D. $\frac{3}{4}$  
  <sub>Salah: hanya menghitung satu pengambilan</sub>

**Pembahasan:** $P = \left(\frac{15}{20}\right)^2 = \frac{9}{16}$.
**Acuan:** siswa — siswa hal.277 Latihan 7.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas10-b07-c-easy-bt01-013
*orisinal | C2 | 1 langkah | jenis: konsep/rumus*

Perhatikan beberapa pasangan kejadian pada pilihan jawaban berikut (koin dan dadu setimbang, kartu bridge lengkap).

Pasangan kejadian manakah yang saling bebas?

- A. Satu kartu diambil dari kartu bridge lengkap: kartu hati dan kartu merah  
  <sub>Salah: kartu hati pasti merah, jadi kejadian pertama memengaruhi kejadian kedua</sub>
- B. Dua bola diambil berturut-turut tanpa pengembalian dari tas berisi 4 bola merah dan 6 bola biru: bola pertama merah dan bola kedua merah  
  <sub>Salah: bola tidak dikembalikan sehingga peluang bola kedua berubah</sub>
- C. Sebuah dadu dilempar satu kali: muncul mata genap dan muncul mata 6  
  <sub>Salah: kedua kejadian berasal dari satu lemparan; mata genap memengaruhi peluang mata 6</sub>
- **D. Koin menunjukkan angka dan dadu menunjukkan mata 4** ✅  
  <sub>Benar: hasil koin tidak memengaruhi peluang hasil dadu, sehingga saling bebas</sub>

**Pembahasan:** Hanya pasangan koin dan dadu yang kejadiannya tidak saling memengaruhi; pada pilihan lain, kejadian pertama memengaruhi peluang kejadian kedua.
**Acuan:** siswa — siswa hal.274

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas10-b07-c-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: hitung P(A dan B) dari peluang diketahui*

Kejadian $A$ dan $B$ saling bebas dengan $P(A) = \frac{2}{5}$ dan $P(B) = \frac{3}{4}$.

Nilai $P(A \text{ dan } B)$ adalah ....

- A. $\frac{8}{15}$  
  <sub>Salah: membagi $P(A)$ dengan $P(B)$</sub>
- B. $\frac{1}{10}$  
  <sub>Salah: memakai $P(B)$ komplemen ($\frac{2}{5} \times \frac{1}{4}$)</sub>
- C. $\frac{17}{20}$  
  <sub>Salah: memakai rumus "atau" ($P(A) + P(B) - P(A) P(B)$)</sub>
- **D. $\frac{3}{10}$** ✅  
  <sub>Benar: $\frac{2}{5} \times \frac{3}{4} = \frac{6}{20} = \frac{3}{10}$</sub>

**Pembahasan:** Karena saling bebas, $P(A \text{ dan } B) = P(A) \times P(B) = \frac{3}{10}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas10-b07-c-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: dua percobaan berbeda bersamaan*

Dua dadu setimbang, satu merah dan satu putih, dilempar bersamaan.

Peluang bahwa dadu merah menunjukkan mata ganjil dan dadu putih menunjukkan mata 6 adalah ....

- A. $\frac{2}{3}$  
  <sub>Salah: menjumlahkan $\frac{1}{2} + \frac{1}{6}$</sub>
- B. $\frac{1}{6}$  
  <sub>Salah: hanya memakai peluang dadu putih</sub>
- **C. $\frac{1}{12}$** ✅  
  <sub>Benar: $P(\text{merah ganjil}) = \frac{3}{6}$ dan $P(\text{putih 6}) = \frac{1}{6}$, sehingga $\frac{1}{2} \times \frac{1}{6} = \frac{1}{12}$</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: hanya memakai peluang dadu merah</sub>

**Pembahasan:** Dua dadu dilempar bersamaan tetap saling bebas, jadi $\frac{1}{2} \times \frac{1}{6} = \frac{1}{12}$.
**Acuan:** siswa — siswa hal.276

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas10-b07-c-easy-bt01-016
*orisinal | C2 | 1 langkah | jenis: konsep/rumus*

Dari sebuah tas berisi bola merah dan bola biru, satu bola diambil dan tidak dikembalikan, kemudian satu bola lain diambil.

Mengapa kejadian "bola pertama merah" dan "bola kedua merah" tidak dapat dikalikan begitu saja sebagai kejadian saling bebas?

- A. Karena kedua bola yang terambil pasti berwarna sama  
  <sub>Salah: warna bola kedua tidak pasti sama dengan bola pertama</sub>
- **B. Karena bola pertama tidak dikembalikan, peluang pengambilan kedua berubah** ✅  
  <sub>Benar: tanpa pengembalian, isi tas berubah sehingga pengambilan kedua dipengaruhi pengambilan pertama</sub>
- C. Karena peluang bola kedua selalu sama dengan nol setelah bola pertama merah  
  <sub>Salah: peluang bola kedua tidak nol, hanya berubah</sub>
- D. Karena aturan perkalian hanya berlaku untuk dadu dan koin  
  <sub>Salah: aturan perkalian berlaku untuk semua kejadian saling bebas, termasuk bola dengan pengembalian</sub>

**Pembahasan:** Bola pertama tidak dikembalikan, jadi jumlah bola berkurang dan peluang pengambilan kedua berubah.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas10-b07-c-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: percobaan berulang dengan pengembalian*

Sepasang dadu setimbang dilempar sebanyak tiga kali. Peluang mendapatkan angka yang sama (dobel) pada sekali lemparan sepasang dadu adalah $\frac{1}{6}$.

Peluang mendapatkan dobel pada ketiga lemparan adalah ....

- A. $\frac{1}{6}$  
  <sub>Salah: memakai peluang satu lemparan saja</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: menjumlahkan $\frac{1}{6}$ sebanyak tiga kali</sub>
- C. $\frac{1}{36}$  
  <sub>Salah: hanya mengalikan dua lemparan</sub>
- **D. $\frac{1}{216}$** ✅  
  <sub>Benar: lemparan saling bebas: $\left(\frac{1}{6}\right)^3 = \frac{1}{216}$</sub>

**Pembahasan:** $P = \frac{1}{6} \times \frac{1}{6} \times \frac{1}{6} = \frac{1}{216}$.
**Acuan:** siswa — siswa hal.274

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas10-b07-c-easy-bt01-018
*orisinal | C2 | 1 langkah | jenis: mencari peluang yang belum diketahui*

Kejadian $A$ dan $B$ saling bebas, dengan $P(A) = 0,4$ dan $P(A \text{ dan } B) = 0,28$.

Nilai $P(B)$ adalah ....

- **A. 0,7** ✅  
  <sub>Benar: $P(B) = \frac{0,28}{0,4} = 0,7$</sub>
- B. 0,12  
  <sub>Salah: mengurangkan $0,4 - 0,28$</sub>
- C. 0,68  
  <sub>Salah: menjumlahkan $0,4 + 0,28$</sub>
- D. 0,112  
  <sub>Salah: mengalikan $0,4 \times 0,28$</sub>

**Pembahasan:** $P(A \text{ dan } B) = P(A) \times P(B)$, sehingga $P(B) = 0,28 : 0,4 = 0,7$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas10-b07-c-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: hitung P(A dan B) dari peluang diketahui*

Peluang Aldo lulus seleksi adalah 0,8 dan peluang Bima lulus seleksi adalah 0,5. Hasil seleksi keduanya saling bebas.

Peluang bahwa Aldo dan Bima keduanya tidak lulus adalah ....

- A. 0,4  
  <sub>Salah: menghitung peluang keduanya lulus</sub>
- **B. 0,1** ✅  
  <sub>Benar: $(1 - 0,8) \times (1 - 0,5) = 0,2 \times 0,5 = 0,1$</sub>
- C. 0,16  
  <sub>Salah: mengalikan peluang lulus Aldo dengan peluang tidak lulusnya sendiri</sub>
- D. 0,7  
  <sub>Salah: menjumlahkan $0,2 + 0,5$</sub>

**Pembahasan:** Aldo tidak lulus 0,2 dan Bima tidak lulus 0,5. Peluang keduanya $0,2 \times 0,5 = 0,1$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas10-b07-c-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: konsep/rumus*

Misalkan $A$ dan $B$ adalah dua kejadian yang saling bebas.

Rumus yang benar untuk peluang terjadinya $A$ dan $B$ bersama-sama adalah ....

- **A. $P(A \text{ dan } B) = P(A) \times P(B)$** ✅  
  <sub>Benar: aturan perkalian untuk kejadian saling bebas</sub>
- B. $P(A \text{ dan } B) = P(A) - P(B)$  
  <sub>Salah: mengurangkan dua peluang</sub>
- C. $P(A \text{ dan } B) = P(A) + P(B)$  
  <sub>Salah: mencampur aturan perkalian dengan penjumlahan</sub>
- D. $P(A \text{ dan } B) = \frac{P(A)}{P(B)}$  
  <sub>Salah: membagi dua peluang</sub>

**Pembahasan:** Untuk kejadian saling bebas, $P(A \text{ dan } B) = P(A) \times P(B)$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas10-b07-c-medium-bt01-001
*variasi (konteks) | C3 | 3 langkah | jenis: dua lemparan sepasang dadu*

Rafi memainkan permainan papan yang memakai sepasang dadu setimbang. Pada giliran pertama ia harus mendapatkan kedua dadu bermata sama, dan pada giliran kedua ia harus mendapatkan jumlah mata sembilan. Hasil kedua giliran saling bebas.

Peluang Rafi berhasil pada kedua giliran tersebut adalah ....

- **A. $\frac{1}{54}$** ✅  
  <sub>Benar: $P(\text{dobel}) = \frac{6}{36} = \frac{1}{6}$, $P(\text{jumlah 9}) = \frac{4}{36} = \frac{1}{9}$, lalu $\frac{1}{6} \times \frac{1}{9} = \frac{1}{54}$</sub>
- B. $\frac{1}{36}$  
  <sub>Salah: mengira peluang jumlah sembilan sama dengan peluang dobel ($\frac{1}{6}$)</sub>
- C. $\frac{5}{18}$  
  <sub>Salah: menjumlahkan $\frac{1}{6} + \frac{1}{9}$ alih-alih mengalikan</sub>
- D. $\frac{1}{9}$  
  <sub>Salah: hanya memakai peluang giliran kedua</sub>

**Pembahasan:** Dobel: 6 dari 36 hasil, jumlah 9: (3,6), (4,5), (5,4), (6,3) = 4 dari 36. $P = \frac{1}{6} \times \frac{1}{9} = \frac{1}{54}$.
**Acuan:** siswa — siswa hal.276 Latihan 7.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas10-b07-c-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: dua lemparan sepasang dadu*

Sebuah mesin permainan di pasar malam melempar sepasang dadu setimbang sebanyak dua kali secara terpisah. Hadiah diberikan jika lemparan pertama berjumlah empat dan lemparan kedua menghasilkan angka dobel.

Peluang pengunjung mendapatkan hadiah adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: menjumlahkan $\frac{1}{12} + \frac{1}{6}$</sub>
- B. $\frac{1}{36}$  
  <sub>Salah: mengira peluang jumlah empat sama dengan $\frac{1}{6}$</sub>
- C. $\frac{1}{12}$  
  <sub>Salah: hanya memakai peluang lemparan pertama</sub>
- **D. $\frac{1}{72}$** ✅  
  <sub>Benar: $P(\text{jumlah 4}) = \frac{3}{36} = \frac{1}{12}$, $P(\text{dobel}) = \frac{1}{6}$, sehingga $\frac{1}{12} \times \frac{1}{6} = \frac{1}{72}$</sub>

**Pembahasan:** Jumlah 4: (1,3), (2,2), (3,1) = 3 dari 36. $P = \frac{1}{12} \times \frac{1}{6} = \frac{1}{72}$.
**Acuan:** siswa — siswa hal.276 Latihan 7.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas10-b07-c-medium-bt01-003
*variasi (konteks) | C3 | 2 langkah | jenis: percobaan berulang dengan pengembalian*

Sebuah roda putar setimbang memiliki 9 sektor sama besar yang diberi nomor 1 sampai 9. Roda diputar tiga kali dan hasil tiap putaran saling bebas.

Peluang bahwa ketiga nomor yang muncul semuanya genap adalah ....

- A. $\frac{125}{729}$  
  <sub>Salah: menghitung ketiganya ganjil (5 nomor ganjil)</sub>
- B. $\frac{16}{81}$  
  <sub>Salah: hanya mengalikan dua putaran</sub>
- C. $\frac{4}{9}$  
  <sub>Salah: hanya menghitung satu putaran</sub>
- **D. $\frac{64}{729}$** ✅  
  <sub>Benar: nomor genap ada 4 (2, 4, 6, 8): $\left(\frac{4}{9}\right)^3 = \frac{64}{729}$</sub>

**Pembahasan:** Genap: 2, 4, 6, 8 (4 nomor). $P = \left(\frac{4}{9}\right)^3 = \frac{64}{729}$.
**Acuan:** pretest — kelas10-b07-p0276-latihan-7-5-3b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas10-b07-c-medium-bt01-004
*variasi (konteks) | C4 | 3 langkah | jenis: percobaan berulang dengan pengembalian*

Sebuah kotak berisi 6 kartu bernomor 1 sampai 6. Satu kartu diambil secara acak, dicatat nomornya, lalu dikembalikan. Proses yang sama diulang sehingga terdapat tiga pengambilan, dan semua pengambilan saling bebas.

Peluang bahwa ketiga nomor yang tercatat semuanya berbeda adalah ....

- A. $\frac{125}{216}$  
  <sub>Salah: mengalikan $\frac{5}{6}$ tiga kali seolah tiap pengambilan harus beda dari satu nomor tertentu</sub>
- B. $\frac{5}{6}$  
  <sub>Salah: hanya memperhatikan syarat untuk pengambilan kedua</sub>
- C. $\frac{1}{36}$  
  <sub>Salah: menghitung peluang ketiga nomor sama</sub>
- **D. $\frac{5}{9}$** ✅  
  <sub>Benar: pengambilan pertama bebas ($1$), kedua harus beda ($\frac{5}{6}$), ketiga harus beda dari keduanya ($\frac{4}{6}$): $\frac{5}{6} \times \frac{4}{6} = \frac{5}{9}$</sub>

**Pembahasan:** Nomor pertama bebas, nomor kedua 5 pilihan dari 6, nomor ketiga 4 pilihan dari 6. $P = 1 \times \frac{5}{6} \times \frac{4}{6} = \frac{20}{36} = \frac{5}{9}$.
**Acuan:** pretest — kelas10-b07-p0277-latihan-7-5-3d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas10-b07-c-medium-bt01-005
*variasi (angka) | C3 | 2 langkah | jenis: pengambilan bola dengan pengembalian*

Sebuah tas berisi 15 bola dengan warna sebagai berikut: tujuh bola merah dan selebihnya berwarna biru. Sebuah bola diambil secara acak dari dalam tas. Bola tersebut kemudian dikembalikan ke dalam tas, dan bola kedua diambil.

Peluang bahwa bola pertama biru dan bola kedua merah adalah ....

- A. $\frac{112}{225}$  
  <sub>Salah: menghitung kedua urutan (biru-merah dan merah-biru)</sub>
- **B. $\frac{56}{225}$** ✅  
  <sub>Benar: bola biru ada 8; dengan pengembalian: $\frac{8}{15} \times \frac{7}{15} = \frac{56}{225}$</sub>
- C. $\frac{4}{15}$  
  <sub>Salah: memakai pengambilan tanpa pengembalian ($\frac{8}{15} \times \frac{7}{14}$)</sub>
- D. $\frac{49}{225}$  
  <sub>Salah: mengira bola biru ada 7, jadi memakai $\frac{7}{15} \times \frac{7}{15}$</sub>

**Pembahasan:** Biru: $15 - 7 = 8$. $P = \frac{8}{15} \times \frac{7}{15} = \frac{56}{225}$.
**Acuan:** pretest — kelas10-b07-p0277-latihan-7-5-4b3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas10-b07-c-medium-bt01-006
*variasi (konteks) | C4 | 4 langkah | jenis: pengambilan bola dengan pengembalian*

Sebuah kantong berisi 10 kelereng: 5 kelereng merah, 3 kelereng biru, dan 2 kelereng hijau. Sebuah kelereng diambil secara acak, dicatat warnanya, lalu dikembalikan ke dalam kantong. Kelereng kedua kemudian diambil.

Peluang bahwa kedua kelereng yang terambil berwarna sama adalah ....

- A. $\frac{31}{50}$  
  <sub>Salah: menghitung peluang kedua kelereng berbeda warna</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: hanya menghitung kedua merah</sub>
- **C. $\frac{19}{50}$** ✅  
  <sub>Benar: $\left(\frac{5}{10}\right)^2 + \left(\frac{3}{10}\right)^2 + \left(\frac{2}{10}\right)^2 = \frac{25 + 9 + 4}{100} = \frac{19}{50}$</sub>
- D. $\frac{14}{45}$  
  <sub>Salah: memakai pengambilan tanpa pengembalian ($\frac{5}{10} \times \frac{4}{9} + \dots$)</sub>

**Pembahasan:** Merah-merah $\frac{25}{100}$, biru-biru $\frac{9}{100}$, hijau-hijau $\frac{4}{100}$. Jumlahnya $\frac{38}{100} = \frac{19}{50}$.
**Acuan:** pretest — kelas10-b07-p0277-latihan-7-5-4b4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas10-b07-c-medium-bt01-007
*variasi (angka) | C4 | 3 langkah | jenis: pengambilan bola dengan pengembalian*

Sebuah kotak berisi 9 lampu, 4 di antaranya rusak. Sebuah lampu diambil secara acak, dicatat kondisinya, lalu dikembalikan ke dalam kotak. Proses ini dilakukan sebanyak tiga kali.

Peluang bahwa setidaknya satu lampu yang terambil rusak adalah ....

- **A. $\frac{604}{729}$** ✅  
  <sub>Benar: $1 - \left(\frac{5}{9}\right)^3 = 1 - \frac{125}{729} = \frac{604}{729}$</sub>
- B. $\frac{125}{729}$  
  <sub>Salah: menghitung peluang ketiga lampu tidak rusak</sub>
- C. $\frac{4}{9}$  
  <sub>Salah: hanya menghitung satu pengambilan</sub>
- D. $\frac{64}{729}$  
  <sub>Salah: hanya menghitung ketiga lampu rusak</sub>

**Pembahasan:** Tidak ada yang rusak: $\left(\frac{5}{9}\right)^3 = \frac{125}{729}$. Setidaknya satu rusak: $1 - \frac{125}{729} = \frac{604}{729}$.
**Acuan:** pretest — kelas10-b07-p0277-latihan-7-5-4b7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas10-b07-c-medium-bt01-008
*variasi (angka) | C3 | 2 langkah | jenis: hitung P(A dan B) dari peluang diketahui*

Gea dan Hadi sedang bermain lempar cincin. Peluang bagi Gea untuk mengenai sasaran adalah 0,45, sedangkan untuk Hadi 0,7. Keberhasilan atau kegagalan Gea dan Hadi saling bebas. Gea dan Hadi masing-masing melempar cincin sekali.

Peluang bahwa Gea mengenai sasaran, tetapi Hadi tidak, adalah ....

- A. 0,385  
  <sub>Salah: peran tertukar: Gea gagal dan Hadi mengenai sasaran</sub>
- **B. 0,135** ✅  
  <sub>Benar: peluang Hadi gagal $1 - 0,7 = 0,3$, lalu $0,45 \times 0,3 = 0,135$</sub>
- C. 0,315  
  <sub>Salah: lupa mengambil komplemen: $0,45 \times 0,7$</sub>
- D. 0,75  
  <sub>Salah: menjumlahkan $0,45 + 0,3$ alih-alih mengalikan</sub>

**Pembahasan:** $P = 0,45 \times (1 - 0,7) = 0,45 \times 0,3 = 0,135$.
**Acuan:** pretest — kelas10-b07-p0276-latihan-7-5-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas10-b07-c-medium-bt01-009
*orisinal | C3 | 2 langkah | jenis: tanpa pengembalian*

Sebuah tas berisi 6 bola merah dan 4 bola biru yang identik kecuali warnanya. Dua bola diambil satu per satu secara acak tanpa pengembalian.

Peluang bahwa kedua bola yang terambil berwarna merah adalah ....

- **A. $\frac{1}{3}$** ✅  
  <sub>Benar: pengambilan pertama $\frac{6}{10}$, kedua tersisa 5 merah dari 9 bola: $\frac{6}{10} \times \frac{5}{9} = \frac{1}{3}$</sub>
- B. $\frac{9}{25}$  
  <sub>Salah: memakai pengambilan dengan pengembalian ($\frac{6}{10} \times \frac{6}{10}$)</sub>
- C. $\frac{4}{15}$  
  <sub>Salah: menghitung bola pertama merah dan bola kedua biru</sub>
- D. $\frac{2}{5}$  
  <sub>Salah: mengurangi penyebut tetapi lupa mengurangi banyak bola merah</sub>

**Pembahasan:** Setelah satu bola merah diambil, tersisa 5 merah dari 9 bola. $P = \frac{6}{10} \times \frac{5}{9} = \frac{30}{90} = \frac{1}{3}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas10-b07-c-medium-bt01-010
*orisinal | C4 | 4 langkah | jenis: tanpa pengembalian*

Sebuah tas berisi 5 bola merah dan 3 bola biru. Dua bola diambil satu per satu secara acak. Skema I: bola pertama dikembalikan sebelum bola kedua diambil. Skema II: bola pertama tidak dikembalikan.

Peluang kedua bola merah pada Skema I dikurangi peluang kedua bola merah pada Skema II adalah ....

- **A. $\frac{15}{448}$** ✅  
  <sub>Benar: Skema I: $\frac{5}{8} \times \frac{5}{8} = \frac{25}{64}$; Skema II: $\frac{5}{8} \times \frac{4}{7} = \frac{5}{14}$; selisih $\frac{25}{64} - \frac{5}{14} = \frac{15}{448}$</sub>
- B. $\frac{5}{64}$  
  <sub>Salah: pada Skema II mengurangi banyak bola merah tetapi lupa mengurangi penyebut</sub>
- C. $-\frac{15}{448}$  
  <sub>Salah: urutan pengurangan tertukar (Skema II dikurangi Skema I)</sub>
- D. $\frac{25}{448}$  
  <sub>Salah: pada Skema II lupa mengurangi banyak bola merah, lalu urutan pengurangan tertukar</sub>

**Pembahasan:** Skema I $\frac{25}{64}$, Skema II $\frac{5}{8} \times \frac{4}{7} = \frac{5}{14}$. Selisih: $\frac{175 - 160}{448} = \frac{15}{448}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas10-b07-c-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: hitung P(A dan B) dari peluang diketahui*

Tiga kejadian $A$, $B$, dan $C$ saling bebas dengan $P(A) = 0,5$, $P(B) = 0,8$, dan $P(C) = 0,25$.

Peluang bahwa $A$ dan $B$ terjadi tetapi $C$ tidak terjadi adalah ....

- A. 0,025  
  <sub>Salah: mengambil komplemen untuk $B$ saja: $A$ dan $C$ terjadi, $B$ tidak</sub>
- B. 0,075  
  <sub>Salah: salah mengambil komplemen: hanya $A$ terjadi, $B$ dan $C$ tidak</sub>
- C. 0,1  
  <sub>Salah: lupa komplemen: menghitung ketiganya terjadi</sub>
- **D. 0,3** ✅  
  <sub>Benar: $P(C \text{ tidak terjadi}) = 0,75$, sehingga $0,5 \times 0,8 \times 0,75 = 0,3$</sub>

**Pembahasan:** $P = P(A) \times P(B) \times (1 - P(C)) = 0,5 \times 0,8 \times 0,75 = 0,3$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas10-b07-c-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: mencari peluang yang belum diketahui*

Kejadian $A$ dan $B$ saling bebas dengan $P(A) = 0,6$ dan $P(A \text{ dan } B) = 0,24$.

Peluang bahwa $A$ terjadi tetapi $B$ tidak terjadi adalah ....

- A. 0,16  
  <sub>Salah: peran tertukar: $A$ tidak terjadi dan $B$ terjadi</sub>
- B. 0,24  
  <sub>Salah: mengira sama dengan $P(A \text{ dan } B)$</sub>
- **C. 0,36** ✅  
  <sub>Benar: $P(B) = \frac{0,24}{0,6} = 0,4$; $P(B \text{ tidak terjadi}) = 0,6$; $0,6 \times 0,6 = 0,36$</sub>
- D. 0,84  
  <sub>Salah: menjumlahkan $0,6 + 0,24$</sub>

**Pembahasan:** $P(B) = 0,24 : 0,6 = 0,4$. $P(A \text{ dan bukan } B) = 0,6 \times (1 - 0,4) = 0,36$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas10-b07-c-medium-bt01-013
*orisinal | C3 | 2 langkah | jenis: konsep/rumus*

Dua kejadian $A$ dan $B$ dikatakan saling bebas jika $P(A \text{ dan } B) = P(A) \times P(B)$.

Pasangan nilai manakah yang mungkin terjadi pada dua kejadian yang saling bebas?

- A. $P(A) = 0,4$, $P(B) = 0,5$, $P(A \text{ dan } B) = 0,25$  
  <sub>Salah: $0,4 \times 0,5 = 0,2$, bukan $0,25$ (keliru memakai $0,5 \times 0,5$)</sub>
- **B. $P(A) = 0,5$, $P(B) = 0,6$, $P(A \text{ dan } B) = 0,3$** ✅  
  <sub>Benar: $0,5 \times 0,6 = 0,3$ sehingga memenuhi aturan perkalian</sub>
- C. $P(A) = 0,5$, $P(B) = 0,6$, $P(A \text{ dan } B) = 0,2$  
  <sub>Salah: $0,5 \times 0,6 = 0,3$, bukan $0,2$</sub>
- D. $P(A) = 0,3$, $P(B) = 0,4$, $P(A \text{ dan } B) = 0,7$  
  <sub>Salah: menjumlahkan $0,3 + 0,4$ alih-alih mengalikan</sub>

**Pembahasan:** Kejadian bebas harus memenuhi $P(A \text{ dan } B) = P(A) \times P(B)$. Hanya $0,5 \times 0,6 = 0,3$ yang cocok.
**Acuan:** siswa — siswa hal.274

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas10-b07-c-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: dua percobaan berbeda bersamaan*

Dua dadu setimbang, satu biru dan satu kuning, dilempar bersamaan.

Peluang bahwa dadu biru menunjukkan mata lebih dari 4 dan dadu kuning menunjukkan mata bilangan prima adalah ....

- A. $\frac{1}{9}$  
  <sub>Salah: menganggap prima hanya 2 dan 3 sehingga peluang kuning $\frac{1}{3}$</sub>
- B. $\frac{1}{3}$  
  <sub>Salah: hanya memakai peluang dadu biru</sub>
- **C. $\frac{1}{6}$** ✅  
  <sub>Benar: biru lebih dari 4: mata 5 dan 6 ($\frac{2}{6}$); kuning prima: 2, 3, 5 ($\frac{3}{6}$); $\frac{1}{3} \times \frac{1}{2} = \frac{1}{6}$</sub>
- D. $\frac{5}{6}$  
  <sub>Salah: menjumlahkan $\frac{1}{3} + \frac{1}{2}$</sub>

**Pembahasan:** Dua dadu dilempar bersamaan tetap saling bebas. $P = \frac{2}{6} \times \frac{3}{6} = \frac{1}{6}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas10-b07-c-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: dua percobaan berbeda bersamaan*

Sebuah koin setimbang dilempar, sebuah dadu setimbang dilempar, dan satu kartu diambil secara acak dari seperangkat kartu bridge lengkap (52 kartu, 4 di antaranya As). Ketiga percobaan saling bebas.

Peluang bahwa koin menunjukkan angka, dadu menunjukkan mata bilangan prima, dan kartu yang terambil adalah As adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: lupa menyertakan peluang kartu As</sub>
- **B. $\frac{1}{52}$** ✅  
  <sub>Benar: $\frac{1}{2} \times \frac{3}{6} \times \frac{4}{52} = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{13} = \frac{1}{52}$</sub>
- C. $\frac{1}{13}$  
  <sub>Salah: hanya memakai peluang kartu As</sub>
- D. $\frac{1}{26}$  
  <sub>Salah: lupa menyertakan peluang dadu prima</sub>

**Pembahasan:** Angka $\frac{1}{2}$, prima (2, 3, 5) $\frac{1}{2}$, As $\frac{1}{13}$. $P = \frac{1}{52}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas10-b07-c-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: tanpa pengembalian*

Sebuah tas berisi 5 bola merah dan 7 bola biru. Dua bola diambil satu per satu secara acak tanpa pengembalian. Dani menghitung peluang kedua bola merah dengan cara $\frac{5}{12} \times \frac{5}{12} = \frac{25}{144}$.

Pernyataan manakah yang benar tentang hitungan Dani?

- A. Salah, karena kedua peluang harus dijumlahkan sehingga hasil yang benar $\frac{5}{6}$  
  <sub>Salah: mengganti aturan perkalian dengan penjumlahan</sub>
- B. Salah, karena peluang bola kedua merah $\frac{4}{12}$ sehingga hasil yang benar $\frac{5}{36}$  
  <sub>Salah: mengurangi banyak bola merah tetapi lupa mengurangi banyak bola seluruhnya</sub>
- **C. Salah, karena bola tidak dikembalikan sehingga peluang bola kedua merah $\frac{4}{11}$ dan hasil yang benar $\frac{5}{33}$** ✅  
  <sub>Benar: setelah satu bola merah diambil tersisa 4 merah dari 11 bola: $\frac{5}{12} \times \frac{4}{11} = \frac{5}{33}$</sub>
- D. Benar, karena kedua pengambilan saling bebas sehingga hasilnya $\frac{25}{144}$  
  <sub>Salah: mengira tanpa pengembalian tetap saling bebas</sub>

**Pembahasan:** Tanpa pengembalian, isi tas berubah. $P = \frac{5}{12} \times \frac{4}{11} = \frac{20}{132} = \frac{5}{33}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas10-b07-c-medium-bt01-017
*orisinal | C4 | 4 langkah | jenis: hitung P(A dan B) dari peluang diketahui*

Peluang Ani tiba tepat waktu di sekolah pada hari Senin adalah 0,9 dan pada hari Selasa adalah 0,8. Ketepatan waktunya pada kedua hari saling bebas.

Peluang bahwa Ani terlambat tepat pada satu dari kedua hari itu adalah ....

- A. 0,18  
  <sub>Salah: hanya menghitung satu kasus (terlambat pada hari Selasa)</sub>
- B. 0,72  
  <sub>Salah: menghitung peluang tepat waktu pada kedua hari</sub>
- C. 0,02  
  <sub>Salah: menghitung peluang terlambat pada kedua hari</sub>
- **D. 0,26** ✅  
  <sub>Benar: Senin terlambat dan Selasa tepat: $0,1 \times 0,8 = 0,08$; Senin tepat dan Selasa terlambat: $0,9 \times 0,2 = 0,18$; jumlah $0,26$</sub>

**Pembahasan:** Dua kasus yang saling lepas: $0,1 \times 0,8 = 0,08$ dan $0,9 \times 0,2 = 0,18$. Jumlahnya $0,26$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas10-b07-c-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: peluang setidaknya satu kejadian*

Peluang Wira lolos seleksi tahap tulis adalah 0,6 dan peluang Yuni lolos seleksi tahap tulis adalah 0,5. Hasil seleksi keduanya saling bebas.

Peluang bahwa setidaknya satu dari mereka lolos adalah ....

- A. 0,3  
  <sub>Salah: hanya menghitung keduanya lolos ($0,6 \times 0,5$)</sub>
- **B. 0,8** ✅  
  <sub>Benar: keduanya gagal: $0,4 \times 0,5 = 0,2$; setidaknya satu lolos: $1 - 0,2 = 0,8$</sub>
- C. 0,2  
  <sub>Salah: hanya menghitung keduanya gagal, lupa dikurangkan dari 1</sub>
- D. 0,5  
  <sub>Salah: menghitung peluang tepat satu yang lolos ($0,6 \times 0,5 + 0,4 \times 0,5$), bukan setidaknya satu</sub>

**Pembahasan:** Keduanya tidak lolos: $0,4 \times 0,5 = 0,2$. Setidaknya satu lolos: $1 - 0,2 = 0,8$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas10-b07-c-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: pengambilan bola dengan pengembalian*

Sebuah kotak berisi 20 kartu bernomor 1 sampai 20. Satu kartu diambil secara acak, dicatat nomornya, lalu dikembalikan. Setelah itu satu kartu diambil lagi.

Peluang bahwa kartu pertama bernomor bilangan prima dan kartu kedua bernomor kuadrat sempurna (1, 4, 9, 16) adalah ....

- A. $\frac{7}{100}$  
  <sub>Salah: mengira bilangan prima hanya 7 (terlewat 19)</sub>
- B. $\frac{1}{10}$  
  <sub>Salah: menganggap kuadrat sempurna ada 5 kartu</sub>
- **C. $\frac{2}{25}$** ✅  
  <sub>Benar: prima: 2, 3, 5, 7, 11, 13, 17, 19 (8 kartu); $\frac{8}{20} \times \frac{4}{20} = \frac{32}{400} = \frac{2}{25}$</sub>
- D. $\frac{3}{5}$  
  <sub>Salah: menjumlahkan $\frac{8}{20} + \frac{4}{20}$</sub>

**Pembahasan:** Prima ada 8 dan kuadrat sempurna ada 4. $P = \frac{8}{20} \times \frac{4}{20} = \frac{2}{25}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas10-b07-c-medium-bt01-020
*orisinal | C4 | 3 langkah | jenis: mencari data yang belum diketahui*

Sebuah tas berisi 4 bola merah dan sejumlah $n$ bola biru. Sebuah bola diambil secara acak, dicatat warnanya, lalu dikembalikan ke dalam tas, kemudian bola kedua diambil. Peluang kedua bola yang terambil berwarna merah adalah $\frac{1}{9}$.

Banyak bola biru di dalam tas adalah ....

- **A. 8 bola** ✅  
  <sub>Benar: $\left(\frac{4}{4+n}\right)^2 = \frac{1}{9}$ sehingga $\frac{4}{4+n} = \frac{1}{3}$, $4 + n = 12$, $n = 8$</sub>
- B. 5 bola  
  <sub>Salah: mengira penyebut peluang adalah 9, sehingga $n = 9 - 4$</sub>
- C. 12 bola  
  <sub>Salah: mengira $4 + n = 12$ adalah banyak bola biru, padahal itu seluruh bola</sub>
- D. 32 bola  
  <sub>Salah: lupa mengkuadratkan: $\frac{4}{4+n} = \frac{1}{9}$ sehingga $n = 32$</sub>

**Pembahasan:** $\left(\frac{4}{4+n}\right)^2 = \frac{1}{9}$, jadi $\frac{4}{4+n} = \frac{1}{3}$ dan $n = 8$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas10-b07-c-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim*

Diketahui $A$ dan $B$ dua kejadian yang saling bebas dengan $P(A) = 0,3$ dan $P(B) = 0,4$. Wulan berkata, "Karena saling bebas dan tidak saling memengaruhi, kejadian $A$ dan $B$ tidak mungkin terjadi bersamaan." Pernyataan yang benar tentang klaim Wulan adalah ....

- **A. Klaim salah; $P(A \text{ dan } B) = 0,3 \times 0,4 = 0,12 > 0$ sehingga keduanya dapat terjadi bersamaan** ✅  
  <sub>Benar: kejadian bebas memenuhi $P(A \text{ dan } B) = P(A) \times P(B) = 0,12$, bukan 0</sub>
- B. Klaim benar; $P(A \text{ dan } B) = 0$ sebab kejadian yang tidak saling memengaruhi tidak beririsan  
  <sub>Salah: mencampuradukkan saling bebas dengan tidak dapat terjadi bersamaan</sub>
- C. Klaim benar; karena $P(A) + P(B) = 0,7 < 1$ keduanya pasti tidak dapat terjadi bersamaan  
  <sub>Salah: menjumlahkan peluang dan mengira jumlah kurang dari 1 berarti tidak beririsan</sub>
- D. Klaim benar; $P(A \text{ dan } B) = 0,12$ terlalu kecil sehingga dianggap tidak mungkin terjadi  
  <sub>Salah: menganggap peluang kecil sama dengan mustahil</sub>

**Pembahasan:** Untuk kejadian bebas, $P(A \text{ dan } B) = 0,3 \times 0,4 = 0,12$. Karena lebih dari 0, kedua kejadian dapat terjadi bersamaan. Jadi bebas tidak sama dengan tidak dapat terjadi bersamaan.
**Acuan:** siswa — siswa hal.274

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas10-b07-c-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal*

Bima berkata, "Untuk setiap dua kejadian $A$ dan $B$ berlaku $P(A \text{ dan } B) = P(A) \times P(B)$." Semua kartu bernomor 1 sampai 5 pada situasi berikut diambil secara acak. Situasi manakah yang menjadi contoh penyangkal klaim Bima?

- A. Dua kartu bernomor 1 sampai 5 diambil satu per satu dengan pengembalian; $A$: kartu pertama ganjil, $B$: kartu kedua ganjil  
  <sub>Salah: pada pengambilan dengan pengembalian kejadian bebas sehingga rumus berlaku: $\frac{9}{25}$</sub>
- B. Sebuah dadu setimbang dilempar dua kali; $A$: lemparan pertama genap, $B$: lemparan kedua lebih dari 4  
  <sub>Salah: lemparan dadu saling bebas, hasil $\frac{1}{6} = \frac{1}{2} \times \frac{1}{3}$</sub>
- C. Sebuah koin setimbang dilempar dua kali; $A$: lemparan pertama angka, $B$: lemparan kedua gambar  
  <sub>Salah: lemparan koin saling bebas, hasil $\frac{1}{4} = \frac{1}{2} \times \frac{1}{2}$</sub>
- **D. Dua kartu bernomor 1 sampai 5 diambil satu per satu tanpa pengembalian; $A$: kartu pertama ganjil, $B$: kartu kedua ganjil** ✅  
  <sub>Benar: $P(A) = P(B) = \frac{3}{5}$ tetapi $P(A \text{ dan } B) = \frac{3}{5} \times \frac{2}{4} = \frac{3}{10} \neq \frac{9}{25}$</sub>

**Pembahasan:** Hanya pengambilan tanpa pengembalian yang tidak bebas: $P(A \text{ dan } B) = \frac{3}{5} \times \frac{2}{4} = \frac{3}{10}$, sedangkan $P(A) \times P(B) = \frac{9}{25}$. Tiga situasi lain bebas sehingga rumus berlaku.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas10-b07-c-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: bandingkan skema*

Empat skema undian mengambil dua bola satu per satu secara acak dan menang jika kedua bola merah. Skema I: tas berisi 5 merah dan 5 biru, dengan pengembalian. Skema II: tas berisi 5 merah dan 3 biru, tanpa pengembalian. Skema III: tas berisi 6 merah dan 4 biru, dengan pengembalian. Skema IV: tas berisi 7 merah dan 5 biru, tanpa pengembalian. Skema yang peluang menangnya terbesar adalah ....

- A. Skema IV  
  <sub>Salah: memilih tas terbesar tanpa menghitung; peluangnya $\frac{7}{22}$</sub>
- B. Skema I  
  <sub>Salah: memilih komposisi seimbang saja; peluangnya hanya $\frac{1}{4}$</sub>
- **C. Skema III** ✅  
  <sub>Benar: peluangnya $\frac{9}{25} = 0,36$; skema II $\frac{5}{14} \approx 0,357$, skema I $\frac{1}{4}$, skema IV $\frac{7}{22} \approx 0,318$</sub>
- D. Skema II  
  <sub>Salah: mengira tanpa pengembalian selalu lebih besar karena bola berkurang; padahal $\frac{5}{14} < \frac{9}{25}$</sub>

**Pembahasan:** I: $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$. II: $\frac{5}{8} \times \frac{4}{7} = \frac{5}{14}$. III: $\frac{3}{5} \times \frac{3}{5} = \frac{9}{25}$. IV: $\frac{7}{12} \times \frac{6}{11} = \frac{7}{22}$. Karena $\frac{9}{25} = \frac{126}{350} > \frac{125}{350} = \frac{5}{14}$, skema III terbesar.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas10-b07-c-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan*

Andi menghitung peluang mengambil tiga kartu berturut-turut dari satu set 52 kartu bridge (tanpa pengembalian) dan ketiganya As: $P = \frac{4}{52} \times \frac{3}{52} \times \frac{2}{52}$. Penilaian yang benar atas hitungan Andi adalah ....

- A. Salah: peluang ketiganya seharusnya dijumlahkan sehingga hasilnya $\frac{9}{52}$  
  <sub>Salah: mengganti perkalian menjadi penjumlahan</sub>
- B. Benar, karena tiap pengambilan memakai aturan perkalian  
  <sub>Salah: mengira aturan perkalian tanpa menyesuaikan banyak kartu yang tersisa</sub>
- C. Salah: penyebutnya 52, 51, 50 tetapi pembilangnya 4, 4, 4 sehingga hasilnya $\frac{64}{132.600} = \frac{8}{16.575}$  
  <sub>Salah: tidak mengurangi jumlah As yang tersisa</sub>
- **D. Salah: penyebutnya seharusnya 52, 51, 50 sehingga hasil benar $\frac{24}{132.600} = \frac{1}{5.525}$** ✅  
  <sub>Benar: tiap kartu tidak dikembalikan, jadi jumlah kartu berkurang satu pada tiap pengambilan</sub>

**Pembahasan:** Setelah satu As terambil tersisa 3 As dari 51 kartu, lalu 2 As dari 50 kartu: $\frac{4}{52} \times \frac{3}{51} \times \frac{2}{50} = \frac{24}{132.600} = \frac{1}{5.525}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas10-b07-c-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim*

Sepasang dadu setimbang (merah dan putih) dilempar bersamaan. $A$: jumlah kedua mata paling sedikit 10; $B$: dadu merah menunjukkan mata 6. Sari berkata, "Dadu tidak saling memengaruhi, jadi $A$ dan $B$ pasti saling bebas." Pernyataan yang benar adalah ....

- A. Klaim benar; dadu tidak saling memengaruhi sehingga semua kejadian dari kedua dadu saling bebas  
  <sub>Salah: menyamaratakan kebebasan kedua dadu dengan kebebasan setiap pasangan kejadian</sub>
- **B. Klaim salah; $P(A \text{ dan } B) = \frac{1}{12}$, padahal $P(A) \times P(B) = \frac{1}{36}$** ✅  
  <sub>Benar: $A \text{ dan } B$ = $\{(6,4),(6,5),(6,6)\}$ sehingga $\frac{3}{36} = \frac{1}{12}$, sedangkan $P(A) = P(B) = \frac{1}{6}$</sub>
- C. Klaim benar; $P(A \text{ dan } B) = \frac{1}{12}$ sama dengan $P(A) + P(B)$ dikali $\frac{1}{4}$  
  <sub>Salah: membuat kesamaan keliru untuk membenarkan klaim</sub>
- D. Klaim salah; $P(A \text{ dan } B) = \frac{1}{6}$, padahal $P(A) \times P(B) = \frac{1}{36}$  
  <sub>Salah: menganggap $P(A \text{ dan } B)$ sama dengan $P(B)$ saja</sub>

**Pembahasan:** $P(A) = \frac{6}{36} = \frac{1}{6}$ dan $P(B) = \frac{1}{6}$. Irisan $\{(6,4),(6,5),(6,6)\}$ berpeluang $\frac{1}{12} \neq \frac{1}{36}$, sehingga $A$ dan $B$ tidak bebas meskipun dadunya terpisah.
**Acuan:** siswa — siswa hal.274

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas10-b07-c-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: rancang kejadian atau skema*

Sebuah tas berisi 10 bola yang hanya berwarna merah atau biru. Dua bola diambil satu per satu secara acak dengan pengembalian. Panitia ingin peluang kedua bola berbeda warna tepat $0,42$. Komposisi isi tas yang memenuhi adalah ....

- A. 4 bola merah dan 6 bola biru  
  <sub>Salah: peluang beda warna menjadi $2 \times 0,4 \times 0,6 = 0,48$</sub>
- B. 5 bola merah dan 5 bola biru  
  <sub>Salah: peluang beda warna menjadi $2 \times 0,5 \times 0,5 = 0,50$</sub>
- **C. 3 bola merah dan 7 bola biru** ✅  
  <sub>Benar: peluang beda warna $2 \times \frac{3}{10} \times \frac{7}{10} = 0,42$</sub>
- D. 2 bola merah dan 8 bola biru  
  <sub>Salah: peluang beda warna menjadi $2 \times 0,2 \times 0,8 = 0,32$</sub>

**Pembahasan:** Beda warna = merah lalu biru atau biru lalu merah: $2 \times \frac{m}{10} \times \frac{10-m}{10}$. Untuk $m = 3$ hasilnya $0,42$; opsi lain menghasilkan $0,32$, $0,48$, dan $0,50$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas10-b07-c-hard-bt01-007
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim*

Satu kartu diambil secara acak dari 52 kartu bridge. $H$: kartu berjenis hati; $S$: kartu As. Tono berkata, "Hanya ada satu kartu yang hati sekaligus As, jadi $H$ dan $S$ pasti tidak saling bebas." Pernyataan yang benar tentang klaim Tono adalah ....

- A. Klaim benar; $P(H \text{ dan } S) = \frac{1}{52}$ sedangkan $P(H) \times P(S) = \frac{1}{4} + \frac{1}{13} = \frac{17}{52}$  
  <sub>Salah: menjumlahkan peluang, bukan mengalikannya</sub>
- **B. Klaim salah; $P(H \text{ dan } S) = \frac{1}{52} = \frac{1}{4} \times \frac{1}{13}$** ✅  
  <sub>Benar: $P(H) = \frac{1}{4}$, $P(S) = \frac{1}{13}$, dan $P(H \text{ dan } S) = \frac{1}{52}$ sama dengan hasil kalinya</sub>
- C. Klaim benar; $P(H \text{ dan } S) = \frac{1}{52}$ lebih kecil daripada $P(H) \times P(S)$  
  <sub>Salah: salah membandingkan: kedua nilai sama-sama $\frac{1}{52}$</sub>
- D. Klaim benar; kedua kejadian dapat terjadi bersamaan sehingga pasti tidak bebas  
  <sub>Salah: mengira dapat terjadi bersamaan berarti tidak bebas</sub>

**Pembahasan:** $P(H) = \frac{13}{52} = \frac{1}{4}$, $P(S) = \frac{4}{52} = \frac{1}{13}$, $P(H \text{ dan } S) = \frac{1}{52}$. Karena $\frac{1}{4} \times \frac{1}{13} = \frac{1}{52}$, $H$ dan $S$ saling bebas.
**Acuan:** siswa — siswa hal.274

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas10-b07-c-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: bandingkan skema*

Dalam kotak undian ada 6 kertas, 2 di antaranya berhadiah. Dua orang mengambil satu kertas masing-masing secara bergantian. Skema P: kertas dikembalikan setelah pengambilan pertama. Skema Q: kertas tidak dikembalikan. Peluang tepat satu dari kedua orang mendapat hadiah dibandingkan pada kedua skema. Pernyataan yang benar adalah ....

- **A. Skema Q lebih besar, dengan selisih $\frac{4}{45}$** ✅  
  <sub>Benar: P: $\frac{4}{9} = \frac{20}{45}$, Q: $\frac{8}{15} = \frac{24}{45}$, selisih $\frac{4}{45}$</sub>
- B. Kedua skema sama besar karena banyak kertas berhadiah sama  
  <sub>Salah: mengira aturan pengembalian tidak memengaruhi peluang</sub>
- C. Skema P lebih besar, dengan selisih $\frac{4}{45}$  
  <sub>Salah: membalik arah perbandingan</sub>
- D. Skema Q lebih besar, dengan selisih $\frac{8}{45}$  
  <sub>Salah: salah hitung selisih dengan menghitung satu urutan saja pada salah satu skema</sub>

**Pembahasan:** P: $2 \times \frac{2}{6} \times \frac{4}{6} = \frac{4}{9}$. Q: $2 \times \frac{2}{6} \times \frac{4}{5} = \frac{8}{15}$. Selisihnya $\frac{24}{45} - \frac{20}{45} = \frac{4}{45}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas10-b07-c-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: contoh penyangkal*

Sepasang dadu setimbang (merah dan putih) dilempar bersamaan. Rudi berkata, "Jika $P(A) = P(B) = \frac{1}{2}$, maka pasti $P(A \text{ dan } B) = \frac{1}{4}$." Pasangan kejadian manakah yang menjadi contoh penyangkal klaim Rudi?

- A. $A$: dadu merah kurang dari 4; $B$: dadu putih lebih dari 3  
  <sub>Salah: bebas sehingga $\frac{1}{4}$; bukan penyangkal</sub>
- B. $A$: dadu merah lebih dari 3; $B$: jumlah kedua mata genap  
  <sub>Salah: irisan berpeluang $\frac{9}{36} = \frac{1}{4}$; bukan penyangkal</sub>
- **C. $A$: dadu merah genap; $B$: dadu merah lebih dari 3** ✅  
  <sub>Benar: keduanya berpeluang $\frac{1}{2}$ tetapi irisannya $\{4,6\}$ berpeluang $\frac{1}{3} \neq \frac{1}{4}$</sub>
- D. $A$: dadu merah genap; $B$: dadu putih ganjil  
  <sub>Salah: bebas sehingga $\frac{1}{4}$; bukan penyangkal</sub>

**Pembahasan:** Pada opsi $A$: merah genap dan $B$: merah lebih dari 3, kejadian bergantung pada dadu yang sama: irisan $\{4,6\}$ sehingga $\frac{2}{6} = \frac{1}{3}$. Tiga pasangan lain memberi tepat $\frac{1}{4}$.
**Acuan:** siswa — siswa hal.274

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas10-b07-c-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan*

Sepasang dadu setimbang dilempar dua kali. Budi menghitung peluang tepat satu dari kedua lemparan menghasilkan angka dobel: $\frac{1}{6} \times \frac{5}{6} = \frac{5}{36}$. Penilaian yang benar atas hitungan Budi adalah ....

- A. Salah: seharusnya $\frac{5}{36} + \frac{1}{36} = \frac{1}{6}$  
  <sub>Salah: menjumlahkan dengan peluang dobel dua kali, bukan menghitung dua urutan</sub>
- **B. Salah: ada dua urutan (dobel lalu tidak dobel, atau tidak dobel lalu dobel); hasil benar $\frac{5}{18}$** ✅  
  <sub>Benar: $2 \times \frac{1}{6} \times \frac{5}{6} = \frac{10}{36} = \frac{5}{18}$</sub>
- C. Salah: seharusnya $\frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$  
  <sub>Salah: menghitung peluang dobel dua kali</sub>
- D. Benar, karena tepat satu dobel hanya terjadi pada satu urutan  
  <sub>Salah: tidak menyadari dobel dapat muncul pada lemparan pertama maupun kedua</sub>

**Pembahasan:** Dua urutan yang saling berbeda: (dobel, tidak dobel) dan (tidak dobel, dobel), masing-masing $\frac{5}{36}$. Jumlahnya $\frac{10}{36} = \frac{5}{18}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas10-b07-c-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: rancang kejadian atau skema*

Dua pemain mengambil dua bola satu per satu secara acak. Pemain X menang jika kedua bola berwarna sama, pemain Y menang jika berbeda warna. Rancangan manakah yang membuat permainan adil (peluang X menang sama dengan peluang Y menang)?

- A. Tas berisi 3 bola merah dan 3 bola biru, tanpa pengembalian  
  <sub>Salah: peluang sama $\frac{2}{5}$ dan beda $\frac{3}{5}$</sub>
- **B. Tas berisi 2 bola merah dan 2 bola biru, dengan pengembalian** ✅  
  <sub>Benar: $P(\text{sama}) = \frac{2}{4} \times \frac{2}{4} + \frac{2}{4} \times \frac{2}{4} = \frac{1}{2} = P(\text{beda})$</sub>
- C. Tas berisi 3 bola merah dan 1 bola biru, dengan pengembalian  
  <sub>Salah: peluang sama $\frac{5}{8}$ dan beda $\frac{3}{8}$</sub>
- D. Tas berisi 2 bola merah dan 2 bola biru, tanpa pengembalian  
  <sub>Salah: peluang sama hanya $\frac{1}{3}$ dan beda $\frac{2}{3}$</sub>

**Pembahasan:** Adil bila $P(\text{sama}) = \frac{1}{2}$. Opsi 1: $\frac{1}{2}$. Opsi 2: $2 \times \frac{2}{4} \times \frac{1}{3} = \frac{1}{3}$. Opsi 3: $\frac{9+1}{16} = \frac{5}{8}$. Opsi 4: $\frac{3 \cdot 2 + 3 \cdot 2}{6 \cdot 5} = \frac{2}{5}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas10-b07-c-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: bandingkan skema*

Skema P: sebuah dadu setimbang dilempar 4 kali; menang jika setidaknya satu kali muncul mata 6. Skema Q: sepasang dadu setimbang dilempar 3 kali; menang jika setidaknya satu kali muncul angka dobel. Pernyataan yang benar adalah ....

- **A. Skema P lebih besar, yaitu $\frac{671}{1.296}$ dibanding $\frac{91}{216}$** ✅  
  <sub>Benar: $P_P = 1 - (\frac{5}{6})^4 = \frac{671}{1.296}$ dan $P_Q = 1 - (\frac{5}{6})^3 = \frac{91}{216} = \frac{546}{1.296}$</sub>
- B. Skema P lebih besar, yaitu $\frac{2}{3}$ dibanding $\frac{1}{2}$  
  <sub>Salah: menjumlahkan $4 \times \frac{1}{6}$ dan $3 \times \frac{1}{6}$ padahal kejadiannya tidak saling lepas</sub>
- C. Skema Q lebih besar, yaitu $\frac{125}{216}$ dibanding $\frac{625}{1.296}$  
  <sub>Salah: lupa komplemen sehingga menghitung peluang tidak ada kejadian sama sekali</sub>
- D. Kedua skema sama besar karena peluang tiap lemparan sama-sama $\frac{1}{6}$  
  <sub>Salah: mengabaikan perbedaan banyak lemparan</sub>

**Pembahasan:** Peluang dobel pada sepasang dadu $\frac{6}{36} = \frac{1}{6}$, sama dengan peluang mata 6 pada satu dadu. P: $1 - (\frac{5}{6})^4 = \frac{671}{1.296}$. Q: $1 - (\frac{5}{6})^3 = \frac{91}{216} = \frac{546}{1.296}$. Jadi P lebih besar.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas10-b07-c-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: rancang kejadian atau skema*

Dalam kotak ada 10 kertas, sebagian berhadiah. Seorang peserta mengambil satu kertas secara acak, mencatatnya, mengembalikannya, lalu mengambil lagi. Panitia ingin peluang peserta mendapat tepat satu hadiah dari kedua pengambilan sebesar mungkin. Dari opsi berikut, banyak kertas berhadiah yang harus dipasang adalah ....

- A. 1 kertas  
  <sub>Salah: peluangnya hanya $2 \times 0,1 \times 0,9 = 0,18$</sub>
- **B. 5 kertas** ✅  
  <sub>Benar: peluang tepat satu hadiah $2 \times 0,5 \times 0,5 = 0,50$, tertinggi di antara opsi</sub>
- C. 3 kertas  
  <sub>Salah: peluangnya $2 \times 0,3 \times 0,7 = 0,42$</sub>
- D. 8 kertas  
  <sub>Salah: peluangnya $2 \times 0,8 \times 0,2 = 0,32$; mengira makin banyak hadiah makin besar peluang</sub>

**Pembahasan:** Dengan $k$ kertas berhadiah, $P = 2 \times \frac{k}{10} \times \frac{10-k}{10}$. Untuk $k = 1, 3, 5, 8$ diperoleh $0,18$; $0,42$; $0,50$; $0,32$. Maksimum di $k = 5$.
**Acuan:** siswa — siswa hal.277

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas10-b07-c-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: uji kebebasan dari data*

Sebanyak 100 siswa disurvei. Sebanyak 60 siswa suka basket, 50 siswa suka voli, dan 40 siswa suka renang. Siswa yang suka basket dan voli ada 30 orang, sedangkan yang suka basket dan renang ada 20 orang. Seorang siswa dipilih secara acak dari 100 siswa itu. Pernyataan yang benar adalah ....

- A. Suka basket dan suka voli saling bebas, begitu pula suka basket dan suka renang  
  <sub>Salah: tidak menguji hasil kali pada pasangan basket dan renang</sub>
- B. Suka basket dan suka voli tidak saling bebas, tetapi suka basket dan suka renang saling bebas  
  <sub>Salah: menukar hasil pengujian kedua pasangan</sub>
- C. Kedua pasangan kejadian tidak saling bebas  
  <sub>Salah: tidak menguji hasil kali pada pasangan basket dan voli</sub>
- **D. Suka basket dan suka voli saling bebas, tetapi suka basket dan suka renang tidak saling bebas** ✅  
  <sub>Benar: $0,6 \times 0,5 = 0,3 = P(\text{basket dan voli})$, tetapi $0,6 \times 0,4 = 0,24 \neq 0,2$</sub>

**Pembahasan:** Basket dan voli: $P = \frac{30}{100} = 0,3$ dan $0,6 \times 0,5 = 0,3$ sehingga bebas. Basket dan renang: $P = 0,2$, sedangkan $0,6 \times 0,4 = 0,24$ sehingga tidak bebas.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas10-b07-c-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim*

Kejadian $A$ dan $B$ saling bebas dengan $P(A) = 0,7$ dan $P(B) = 0,4$. Rina menyatakan, "$P(A \text{ dan bukan } B) = 0,42$ dan $P(\text{bukan } A \text{ dan bukan } B) = 0,18$." Penilaian yang benar atas pernyataan Rina adalah ....

- A. Hanya yang kedua benar; yang pertama seharusnya $0,7 \times 0,4 = 0,28$  
  <sub>Salah: memakai $P(B)$, bukan $P(\text{bukan } B)$, pada hitungan pertama</sub>
- B. Keduanya salah, karena $A$ dan bukan $B$ tidak saling bebas sehingga tidak dapat dikalikan  
  <sub>Salah: mengira komplemen merusak kebebasan</sub>
- C. Hanya yang pertama benar; yang kedua seharusnya $0,3 \times 0,4 = 0,12$  
  <sub>Salah: memakai $P(B)$, bukan $P(\text{bukan } B)$, pada faktor kedua</sub>
- **D. Keduanya benar, karena $0,7 \times 0,6 = 0,42$ dan $0,3 \times 0,6 = 0,18$** ✅  
  <sub>Benar: bila $A$ dan $B$ bebas, komplemen $B$ pun bebas dari $A$ dan dari komplemen $A$</sub>

**Pembahasan:** $P(\text{bukan } B) = 0,6$ dan $P(\text{bukan } A) = 0,3$. Karena $A$, $B$ bebas, $P(A \text{ dan bukan } B) = 0,7 \times 0,6 = 0,42$ dan $P(\text{bukan } A \text{ dan bukan } B) = 0,3 \times 0,6 = 0,18$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas10-b07-c-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: peluang bertingkat tiga pengambilan*

Tas berisi 4 bola merah dan 5 bola biru. Tiga bola diambil satu per satu secara acak tanpa pengembalian. Urutan warna MMB berarti merah, merah, biru; demikian pula MBM dan BMM. Pernyataan yang benar tentang ketiga urutan itu adalah ....

- A. Urutan BMM paling besar karena bola biru lebih banyak diambil lebih dulu  
  <sub>Salah: hanya melihat faktor pertama</sub>
- B. Urutan MMB paling besar karena dua bola merah diambil lebih dulu  
  <sub>Salah: mengira urutan menentukan peluang padahal pembilang dan penyebut hanya tersusun ulang</sub>
- C. Ketiga urutan berpeluang sama, yaitu $\frac{80}{729}$  
  <sub>Salah: memakai perhitungan dengan pengembalian</sub>
- **D. Ketiga urutan berpeluang sama, yaitu $\frac{5}{42}$** ✅  
  <sub>Benar: $\frac{4}{9} \times \frac{3}{8} \times \frac{5}{7} = \frac{4}{9} \times \frac{5}{8} \times \frac{3}{7} = \frac{5}{9} \times \frac{4}{8} \times \frac{3}{7} = \frac{5}{42}$</sub>

**Pembahasan:** Pembilang selalu $4 \times 3 \times 5$ dan penyebut $9 \times 8 \times 7$ untuk ketiga urutan, hanya susunan faktornya berbeda: $\frac{60}{504} = \frac{5}{42}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas10-b07-c-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: rancang kejadian atau skema*

Sebuah dadu setimbang dilempar sekali. $A$: muncul mata genap. Kejadian $B$ manakah yang saling bebas dengan $A$?

- A. $B$: muncul mata 4, 5, atau 6  
  <sub>Salah: $P(A \text{ dan } B) = \frac{1}{3}$ tetapi $P(A) \times P(B) = \frac{1}{4}$</sub>
- B. $B$: muncul mata 1, 2, atau 3  
  <sub>Salah: $P(A \text{ dan } B) = \frac{1}{6}$ tetapi $P(A) \times P(B) = \frac{1}{4}$</sub>
- **C. $B$: muncul mata 1 atau 2** ✅  
  <sub>Benar: $P(A \text{ dan } B) = P(\{2\}) = \frac{1}{6} = \frac{1}{2} \times \frac{1}{3} = P(A) \times P(B)$</sub>
- D. $B$: muncul mata 2 atau 4  
  <sub>Salah: $P(A \text{ dan } B) = \frac{1}{3}$ tetapi $P(A) \times P(B) = \frac{1}{6}$</sub>

**Pembahasan:** $A = \{2,4,6\}$, $P(A) = \frac{1}{2}$. Hanya $B = \{1,2\}$ yang memenuhi $P(A \text{ dan } B) = P(A) \times P(B)$.
**Acuan:** siswa — siswa hal.274

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas10-b07-c-hard-bt01-018
*orisinal | C5 | 5 langkah | jenis: bandingkan skema*

Peluang pemanah A mengenai sasaran pada tiap tembakan adalah $0,6$ dan pemanah B adalah $0,7$; semua tembakan saling bebas. Tim berhasil jika semua tembakan pada skemanya mengenai sasaran. Skema I: A menembak sekali dan B menembak sekali. Skema II: A menembak dua kali. Skema III: B menembak dua kali. Skema IV: A menembak sekali dan B menembak dua kali. Pernyataan yang benar adalah ....

- **A. Peluang terbesar pada Skema III ($0,49$) dan terkecil pada Skema IV ($0,294$)** ✅  
  <sub>Benar: I: $0,42$; II: $0,36$; III: $0,49$; IV: $0,6 \times 0,49 = 0,294$</sub>
- B. Peluang terbesar pada Skema I ($0,42$) dan terkecil pada Skema IV ($0,294$)  
  <sub>Salah: mengira skema yang memakai kedua pemanah selalu terbesar</sub>
- C. Peluang terbesar pada Skema III ($0,49$) dan terkecil pada Skema II ($0,36$)  
  <sub>Salah: tidak menghitung skema IV yang lebih kecil lagi</sub>
- D. Peluang terbesar pada Skema I ($0,42$) dan terkecil pada Skema II ($0,36$)  
  <sub>Salah: mengabaikan skema III dan IV</sub>

**Pembahasan:** I: $0,6 \times 0,7 = 0,42$. II: $0,6^2 = 0,36$. III: $0,7^2 = 0,49$. IV: $0,6 \times 0,7^2 = 0,294$. Terbesar III, terkecil IV.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas10-b07-c-hard-bt01-019
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim*

Tas berisi 3 bola merah dan 5 bola biru. Dua bola diambil satu per satu secara acak tanpa pengembalian. Rani berkata, "Peluang bola pertama merah dan bola kedua biru sama dengan peluang bola pertama biru dan bola kedua merah." Pernyataan yang benar adalah ....

- A. Klaim benar; keduanya bernilai $\frac{15}{64}$  
  <sub>Salah: lupa mengurangi banyak bola pada pengambilan kedua</sub>
- B. Klaim salah; peluang biru lalu merah lebih besar karena bola biru lebih banyak  
  <sub>Salah: hanya melihat faktor pertama</sub>
- **C. Klaim benar; keduanya bernilai $\frac{15}{56}$** ✅  
  <sub>Benar: $\frac{3}{8} \times \frac{5}{7} = \frac{5}{8} \times \frac{3}{7} = \frac{15}{56}$</sub>
- D. Klaim salah; peluang merah lalu biru lebih kecil karena $\frac{3}{8} < \frac{5}{8}$  
  <sub>Salah: membandingkan faktor pertama saja</sub>

**Pembahasan:** Merah lalu biru: $\frac{3}{8} \times \frac{5}{7} = \frac{15}{56}$. Biru lalu merah: $\frac{5}{8} \times \frac{3}{7} = \frac{15}{56}$. Faktor yang sama hanya tersusun ulang.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas10-b07-c-hard-bt01-020
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan*

Tiga koin setimbang dilempar. Dewi menghitung peluang setidaknya satu koin menunjukkan angka dengan menjumlahkan: $\frac{1}{2} + \frac{1}{2} + \frac{1}{2} = \frac{3}{2}$. Penilaian yang benar atas hitungan Dewi adalah ....

- **A. Salah: peluang tidak mungkin lebih dari 1; hasil benar $1 - (\frac{1}{2})^3 = \frac{7}{8}$** ✅  
  <sub>Benar: kejadian tidak saling lepas tidak boleh dijumlahkan; komplemennya semua gambar $(\frac{1}{2})^3 = \frac{1}{8}$</sub>
- B. Salah: hasil benar $(\frac{1}{2})^3 = \frac{1}{8}$  
  <sub>Salah: menghitung peluang semua gambar, bukan setidaknya satu angka</sub>
- C. Benar, karena peluang boleh lebih dari 1 asalkan lemparannya saling bebas  
  <sub>Salah: tidak tahu bahwa peluang paling besar 1</sub>
- D. Salah: hasil benar $\frac{3}{8}$  
  <sub>Salah: menghitung peluang tepat satu angka</sub>

**Pembahasan:** Penjumlahan menghasilkan $\frac{3}{2} > 1$, tidak mungkin. Gunakan komplemen: tidak ada angka sama sekali berpeluang $(\frac{1}{2})^3 = \frac{1}{8}$, sehingga hasilnya $1 - \frac{1}{8} = \frac{7}{8}$.
**Acuan:** siswa — siswa hal.277

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
