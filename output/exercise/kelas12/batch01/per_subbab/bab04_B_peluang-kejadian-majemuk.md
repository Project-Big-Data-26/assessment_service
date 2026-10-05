# Lembar koreksi — kelas12 SMA12U-B4 subbab B: Peluang Kejadian Majemuk

60 soal | easy 20, medium 20, hard 20 | variasi 21, orisinal 39

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12-b04-b-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: irisan dan gabungan kejadian dadu*

Sebuah dadu setimbang bersisi enam dilempar satu kali. Kejadian $A$ adalah muncul mata dadu habis dibagi 3 dan kejadian $B$ adalah muncul mata dadu habis dibagi 4. Nilai $P(A \cap B)$ dan $P(A \cup B)$ berturut-turut adalah ....

- A. $P(A \cap B) = \frac{1}{18}$ dan $P(A \cup B) = \frac{4}{9}$  
  <sub>Salah: memakai rumus kejadian saling bebas $P(A)\times P(B)$ padahal kedua kejadian saling lepas</sub>
- **B. $P(A \cap B) = 0$ dan $P(A \cup B) = \frac{1}{2}$** ✅  
  <sub>Benar: $A=\{3,6\}$, $B=\{4\}$ tidak beririsan; $P(A \cup B)=\frac{2}{6}+\frac{1}{6}=\frac{1}{2}$</sub>
- C. $P(A \cap B) = \frac{1}{6}$ dan $P(A \cup B) = \frac{1}{2}$  
  <sub>Salah: menganggap irisan sama dengan peluang $B$</sub>
- D. $P(A \cap B) = 0$ dan $P(A \cup B) = \frac{1}{3}$  
  <sub>Salah: hanya menghitung peluang $A$ pada gabungan</sub>

**Pembahasan:** $A=\{3,6\}$ dan $B=\{4\}$ saling lepas sehingga $A \cap B=\{\}$ dan $P(A \cap B)=0$. Maka $P(A \cup B)=P(A)+P(B)=\frac{2}{6}+\frac{1}{6}=\frac{1}{2}$.
**Acuan:** pretest — kelas12-b04-p0175-latihan-4-2-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12-b04-b-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: peluang bersyarat dua dadu*

Dua dadu setimbang dilemparkan bersamaan. Jika $A$ adalah kejadian muncul dua mata dadu yang hasil kalinya 4 dan $B$ adalah kejadian muncul dua mata dadu berjumlah 5, nilai $P(A|B)$ dan $P(B|A)$ berturut-turut adalah ....

- **A. $P(A|B) = \frac{1}{2}$ dan $P(B|A) = \frac{2}{3}$** ✅  
  <sub>Benar: $A \cap B=\{(1,4),(4,1)\}$, $n(A)=3$, $n(B)=4$; $P(A|B)=\frac{2}{4}$ dan $P(B|A)=\frac{2}{3}$</sub>
- B. $P(A|B) = \frac{1}{18}$ dan $P(B|A) = \frac{1}{18}$  
  <sub>Salah: membagi irisan dengan seluruh ruang sampel 36, bukan dengan kejadian syarat</sub>
- C. $P(A|B) = \frac{2}{7}$ dan $P(B|A) = \frac{2}{7}$  
  <sub>Salah: membagi irisan dengan jumlah $n(A)+n(B)$</sub>
- D. $P(A|B) = \frac{2}{3}$ dan $P(B|A) = \frac{1}{2}$  
  <sub>Salah: kejadian syarat dan kejadian yang dicari tertukar</sub>

**Pembahasan:** $A=\{(1,4),(4,1),(2,2)\}$, $B=\{(1,4),(4,1),(2,3),(3,2)\}$, $A \cap B=\{(1,4),(4,1)\}$. $P(A|B)=\frac{n(A \cap B)}{n(B)}=\frac{2}{4}=\frac{1}{2}$ dan $P(B|A)=\frac{2}{3}$.
**Acuan:** pretest — kelas12-b04-p0182-latihan-4-3-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12-b04-b-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: pengambilan kartu tanpa pengembalian*

Dua kartu dipilih secara acak satu per satu dari tumpukan 40 kartu tanpa pengembalian. Tumpukan itu terdiri dari 4 warna dan setiap warna memiliki kartu bernomor 1 sampai 10. Peluang kartu pertama bernomor 1 dan kartu kedua bernomor 10 adalah ....

- A. $\frac{1}{1560}$  
  <sub>Salah: hanya menghitung satu kartu untuk tiap nomor</sub>
- B. $\frac{1}{100}$  
  <sub>Salah: memakai penyebut 40 pada pengambilan kedua (seperti dengan pengembalian)</sub>
- **C. $\frac{2}{195}$** ✅  
  <sub>Benar: $\frac{4}{40}\times\frac{4}{39}=\frac{2}{195}$</sub>
- D. $\frac{79}{390}$  
  <sub>Salah: menjumlahkan peluang kedua pengambilan, bukan mengalikan</sub>

**Pembahasan:** Pengambilan pertama $P=\frac{4}{40}$. Setelah satu kartu terambil tersisa 39 kartu dan 4 kartu bernomor 10, sehingga peluang kedua $\frac{4}{39}$. Peluang keduanya $=\frac{4}{40}\times\frac{4}{39}=\frac{2}{195}$.
**Acuan:** pretest — kelas12-b04-p0182-latihan-4-3-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12-b04-b-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: gabungan saling lepas dua dadu*

Peluang munculnya mata dadu berjumlah 4 atau 9 jika dua dadu setimbang dilempar secara bersamaan adalah ....

- A. $\frac{1}{108}$  
  <sub>Salah: mengalikan kedua peluang, padahal kejadian 'atau' saling lepas dijumlahkan</sub>
- **B. $\frac{7}{36}$** ✅  
  <sub>Benar: $P(4)=\frac{3}{36}$, $P(9)=\frac{4}{36}$, kedua kejadian saling lepas sehingga jumlahnya $\frac{7}{36}$</sub>
- C. $\frac{1}{6}$  
  <sub>Salah: lupa pasangan (2, 2) pada jumlah 4</sub>
- D. $\frac{7}{72}$  
  <sub>Salah: memakai ruang sampel 72 (36 dijumlahkan dua kali)</sub>

**Pembahasan:** Jumlah 4: (1,3),(3,1),(2,2) = 3 pasangan. Jumlah 9: (3,6),(6,3),(4,5),(5,4) = 4 pasangan. Keduanya tidak dapat terjadi bersamaan, jadi $P=\frac{3}{36}+\frac{4}{36}=\frac{7}{36}$.
**Acuan:** siswa — siswa hal.166 Contoh 4.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12-b04-b-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: pengambilan bola tanpa pengembalian*

Sebuah kotak berisi 5 bola merah dan 3 bola putih. Tiga bola diambil secara acak satu per satu tanpa pengembalian. Peluang bahwa pada pengambilan pertama dan kedua terambil bola merah serta pada pengambilan ketiga terambil bola putih adalah ....

- A. $\frac{5}{14}$  
  <sub>Salah: lupa peluang pengambilan ketiga</sub>
- B. $\frac{15}{112}$  
  <sub>Salah: penyebut pengambilan ketiga tidak dikurangi</sub>
- C. $\frac{75}{512}$  
  <sub>Salah: memakai penyebut 8 terus (seperti dengan pengembalian)</sub>
- **D. $\frac{5}{28}$** ✅  
  <sub>Benar: $\frac{5}{8}\times\frac{4}{7}\times\frac{3}{6}=\frac{5}{28}$</sub>

**Pembahasan:** Pengambilan 1: $\frac{5}{8}$ (merah), pengambilan 2: $\frac{4}{7}$ (merah), pengambilan 3: $\frac{3}{6}$ (putih). Hasil kali $=\frac{60}{336}=\frac{5}{28}$.
**Acuan:** pretest — kelas12-b04-p0183-latihan-4-3-4a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12-b04-b-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: pengambilan bola dengan pengembalian*

Sebuah kantong berisi 3 bola biru dan 7 bola merah. Tiga bola diambil secara acak satu per satu dengan pengembalian. Peluang bahwa pengambilan pertama terambil bola biru serta pengambilan kedua dan ketiga terambil bola merah adalah ....

- A. $\frac{343}{1000}$  
  <sub>Salah: mengira ketiga bola yang terambil berwarna merah</sub>
- B. $\frac{21}{100}$  
  <sub>Salah: hanya menghitung dua pengambilan</sub>
- **C. $\frac{147}{1000}$** ✅  
  <sub>Benar: dengan pengembalian, tiap pengambilan saling bebas: $\frac{3}{10}\times\frac{7}{10}\times\frac{7}{10}=\frac{147}{1000}$</sub>
- D. $\frac{7}{40}$  
  <sub>Salah: memakai cara tanpa pengembalian</sub>

**Pembahasan:** Setiap bola dikembalikan, sehingga isi kantong tetap 10 bola dan kejadian saling bebas. $P=\frac{3}{10}\times\frac{7}{10}\times\frac{7}{10}=\frac{147}{1000}$.
**Acuan:** pretest — kelas12-b04-p0183-latihan-4-3-4b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12-b04-b-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: saling bebas koin dan dadu*

Dua dadu dan sekeping koin dilemparkan secara bersamaan. Jika kemunculan tiap dadu dan koin dianggap seimbang, peluang muncul sisi gambar pada koin dan kedua mata dadu berjumlah 8 adalah ....

- A. $\frac{5}{36}$  
  <sub>Salah: lupa peluang sisi gambar pada koin</sub>
- B. $\frac{23}{36}$  
  <sub>Salah: menjumlahkan peluang, padahal kejadian saling bebas dengan kata 'dan'</sub>
- C. $\frac{1}{72}$  
  <sub>Salah: hanya menghitung pasangan (4, 4) untuk jumlah 8</sub>
- **D. $\frac{5}{72}$** ✅  
  <sub>Benar: $\frac{1}{2}\times\frac{5}{36}=\frac{5}{72}$</sub>

**Pembahasan:** Koin dan dadu saling bebas. $P(\text{gambar})=\frac{1}{2}$. Jumlah 8: (2,6),(6,2),(3,5),(5,3),(4,4) = 5 dari 36. Maka $P=\frac{1}{2}\times\frac{5}{36}=\frac{5}{72}$.
**Acuan:** pretest — kelas12-b04-p0186-uji-kompetensi-bab-4-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12-b04-b-easy-bt01-008
*variasi (konteks) | C2 | 2 langkah | jenis: pengambilan bola dengan pengembalian*

Sebuah kotak memuat 7 kelereng hijau dan 5 kelereng kuning. Dua kelereng diambil berturut-turut secara acak, dan setiap kelereng yang terambil dikembalikan lebih dulu sebelum pengambilan berikutnya. Peluang terambilnya dua kelereng kuning adalah ....

- **A. $\frac{25}{144}$** ✅  
  <sub>Benar: $\frac{5}{12}\times\frac{5}{12}=\frac{25}{144}$</sub>
- B. $\frac{5}{33}$  
  <sub>Salah: memakai cara tanpa pengembalian</sub>
- C. $\frac{25}{132}$  
  <sub>Salah: penyebut dikurangi tetapi pembilang tidak, campuran dua cara</sub>
- D. $\frac{5}{6}$  
  <sub>Salah: menjumlahkan kedua peluang</sub>

**Pembahasan:** Kelereng dikembalikan, jadi tiap pengambilan memiliki peluang kuning $\frac{5}{12}$ dan saling bebas. $P=\left(\frac{5}{12}\right)^2=\frac{25}{144}$.
**Acuan:** pretest — kelas12-b04-p0188-uji-kompetensi-bab-4-9a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12-b04-b-easy-bt01-009
*variasi (konteks) | C2 | 2 langkah | jenis: pengambilan bola tanpa pengembalian*

Sebuah toples berisi 9 permen mint dan 3 permen cokelat. Dua permen diambil berturut-turut secara acak tanpa dikembalikan. Peluang terambilnya dua permen cokelat adalah ....

- A. $\frac{1}{16}$  
  <sub>Salah: memakai cara dengan pengembalian</sub>
- B. $\frac{2}{11}$  
  <sub>Salah: hanya memakai peluang pengambilan kedua</sub>
- **C. $\frac{1}{22}$** ✅  
  <sub>Benar: $\frac{3}{12}\times\frac{2}{11}=\frac{1}{22}$</sub>
- D. $\frac{19}{44}$  
  <sub>Salah: menjumlahkan peluang pertama dan kedua</sub>

**Pembahasan:** Pengambilan pertama cokelat $\frac{3}{12}$; setelah itu tersisa 11 permen dengan 2 cokelat, jadi $\frac{2}{11}$. $P=\frac{3}{12}\times\frac{2}{11}=\frac{1}{22}$.
**Acuan:** pretest — kelas12-b04-p0188-uji-kompetensi-bab-4-9b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12-b04-b-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: frekuensi harapan kejadian majemuk*

Dua buah dadu setimbang dilempar bersama sebanyak 720 kali. Frekuensi harapan muncul mata dadu 2 pada dadu pertama dan mata dadu 6 pada dadu kedua adalah ....

- **A. $20$** ✅  
  <sub>Benar: $P=\frac{1}{6}\times\frac{1}{6}=\frac{1}{36}$ sehingga $Fh=\frac{1}{36}\times 720=20$</sub>
- B. $240$  
  <sub>Salah: menjumlahkan peluang ($\frac{1}{6}+\frac{1}{6}=\frac{1}{3}$) lalu mengalikan dengan 720</sub>
- C. $10$  
  <sub>Salah: membagi 720 dengan 72, bukan dengan 36</sub>
- D. $120$  
  <sub>Salah: hanya memakai peluang satu dadu ($\frac{1}{6}$)</sub>

**Pembahasan:** $P(\text{2 lalu 6})=\frac{1}{6}\times\frac{1}{6}=\frac{1}{36}$. $Fh=P\times n=\frac{1}{36}\times 720=20$.
**Acuan:** siswa — siswa hal.160 Contoh 4.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12-b04-b-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: rumus gabungan data cacah*

Jumlah siswa dalam suatu angkatan adalah 40. Terdapat 25 siswa yang menyukai Sejarah, ada 18 siswa yang menyukai Geografi, dan 8 siswa yang menyukai keduanya. Jika seorang siswa dipilih secara acak, peluang ia menyukai Sejarah atau Geografi adalah ....

- A. $\frac{43}{40}$  
  <sub>Salah: tidak mengurangi irisan, siswa yang menyukai keduanya terhitung dua kali</sub>
- **B. $\frac{7}{8}$** ✅  
  <sub>Benar: $P=\frac{25}{40}+\frac{18}{40}-\frac{8}{40}=\frac{35}{40}=\frac{7}{8}$</sub>
- C. $\frac{27}{40}$  
  <sub>Salah: mengurangi irisan dua kali ($25+18-2\times 8$ lalu salah hitung)</sub>
- D. $\frac{1}{5}$  
  <sub>Salah: hanya menghitung siswa yang menyukai keduanya</sub>

**Pembahasan:** $P(S \cup G)=P(S)+P(G)-P(S \cap G)=\frac{25+18-8}{40}=\frac{35}{40}=\frac{7}{8}$.
**Acuan:** siswa — siswa hal.161 Contoh 4.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12-b04-b-easy-bt01-012
*variasi (konteks) | C2 | 2 langkah | jenis: gabungan dari tabel dua arah*

Banyak siswa menurut kelas dan jenis kelamin:

|Kelas|Putra|Putri|
|---|---|---|
|X|30|20|
|XI|25|25|
|XII|20|30|

Satu siswa dipilih secara acak dari seluruh siswa pada tabel. Peluang terpilih siswa putra atau siswa kelas XII adalah ....

- A. $\frac{1}{6}$  
  <sub>Salah: mengalikan peluang, padahal yang ditanya 'atau'</sub>
- B. $\frac{2}{15}$  
  <sub>Salah: hanya menghitung irisan (putra dan kelas XII)</sub>
- **C. $\frac{7}{10}$** ✅  
  <sub>Benar: $P=\frac{75}{150}+\frac{50}{150}-\frac{20}{150}=\frac{105}{150}=\frac{7}{10}$</sub>
- D. $\frac{5}{6}$  
  <sub>Salah: tidak mengurangi irisan (siswa putra kelas XII terhitung dua kali)</sub>

**Pembahasan:** Total 150 siswa; putra 75, kelas XII 50, putra kelas XII 20. $P=\frac{75+50-20}{150}=\frac{105}{150}=\frac{7}{10}$.
**Acuan:** siswa — siswa hal.180 Contoh 4.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12-b04-b-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: rumus gabungan umum*

Diketahui $P(A)=\frac{7}{20}$, $P(B)=\frac{9}{20}$, dan $P(A \cap B)=\frac{3}{20}$. Nilai $P(A \cup B)$ adalah ....

- A. $\frac{4}{5}$  
  <sub>Salah: tidak mengurangi $P(A \cap B)$</sub>
- **B. $\frac{13}{20}$** ✅  
  <sub>Benar: $P(A \cup B)=\frac{7}{20}+\frac{9}{20}-\frac{3}{20}=\frac{13}{20}$</sub>
- C. $\frac{19}{20}$  
  <sub>Salah: menambahkan irisan, bukan mengurangi</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: mengurangi irisan dua kali</sub>

**Pembahasan:** $P(A \cup B)=P(A)+P(B)-P(A \cap B)=\frac{7+9-3}{20}=\frac{13}{20}$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12-b04-b-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: rumus saling lepas*

Kejadian $A$ dan $B$ saling lepas dengan $P(A)=\frac{2}{5}$ dan $P(B)=\frac{1}{3}$. Nilai $P(A \cup B)$ adalah ....

- **A. $\frac{11}{15}$** ✅  
  <sub>Benar: saling lepas berarti $P(A \cap B)=0$, sehingga $P(A \cup B)=\frac{2}{5}+\frac{1}{3}=\frac{11}{15}$</sub>
- B. $\frac{2}{15}$  
  <sub>Salah: mengalikan kedua peluang (rumus saling bebas)</sub>
- C. $\frac{1}{15}$  
  <sub>Salah: mengurangi kedua peluang</sub>
- D. $\frac{3}{8}$  
  <sub>Salah: menjumlahkan pembilang dan penyebut secara terpisah</sub>

**Pembahasan:** Karena saling lepas, $P(A \cup B)=P(A)+P(B)=\frac{6}{15}+\frac{5}{15}=\frac{11}{15}$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12-b04-b-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: rumus saling bebas*

Kejadian $A$ dan $B$ saling bebas dengan $P(A)=\frac{1}{5}$ dan $P(B)=\frac{3}{10}$. Nilai $P(A \cap B)$ adalah ....

- A. $\frac{1}{2}$  
  <sub>Salah: menjumlahkan kedua peluang</sub>
- B. $\frac{1}{5}$  
  <sub>Salah: mengalikan pembilang dan menjumlahkan penyebut ($\frac{3}{15}$)</sub>
- C. $\frac{1}{10}$  
  <sub>Salah: mengurangi kedua peluang</sub>
- **D. $\frac{3}{50}$** ✅  
  <sub>Benar: saling bebas, sehingga $P(A \cap B)=\frac{1}{5}\times\frac{3}{10}=\frac{3}{50}$</sub>

**Pembahasan:** $P(A \cap B)=P(A)\times P(B)=\frac{1}{5}\times\frac{3}{10}=\frac{3}{50}$.
**Acuan:** siswa — siswa hal.172

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12-b04-b-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: identifikasi saling lepas*

Sebuah dadu setimbang bersisi enam dilempar satu kali. Pasangan kejadian yang saling lepas adalah ....

- **A. muncul bilangan prima dan muncul mata dadu 6** ✅  
  <sub>Benar: bilangan prima $\{2,3,5\}$ dan $\{6\}$ tidak memiliki irisan</sub>
- B. muncul kelipatan 3 dan muncul bilangan genap  
  <sub>Salah: irisannya $\{6\}$, jadi tidak saling lepas</sub>
- C. muncul bilangan ganjil dan muncul bilangan prima  
  <sub>Salah: irisannya $\{3,5\}$, jadi tidak saling lepas</sub>
- D. muncul bilangan genap dan muncul mata dadu lebih dari 3  
  <sub>Salah: irisannya $\{4,6\}$, jadi tidak saling lepas</sub>

**Pembahasan:** Dua kejadian saling lepas bila irisannya kosong. Prima $=\{2,3,5\}$ dan mata 6 $=\{6\}$ tidak beririsan; tiga pasangan lain masing-masing memiliki anggota bersama.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12-b04-b-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: identifikasi saling bebas*

Pasangan kejadian berikut yang saling bebas adalah ....

- A. terambil bola merah pada pengambilan pertama dan bola merah pada pengambilan kedua dari kantong tanpa pengembalian  
  <sub>Salah: pengambilan pertama mengubah isi kantong sehingga peluang kedua berubah</sub>
- B. muncul mata dadu genap dan muncul mata dadu 6 pada satu lemparan dadu yang sama  
  <sub>Salah: kejadian muncul pada lemparan yang sama; mata 6 sudah termasuk genap sehingga saling mempengaruhi</sub>
- **C. muncul sisi gambar pada sebuah koin dan muncul mata dadu 4 pada sebuah dadu yang dilempar bersamaan** ✅  
  <sub>Benar: hasil koin tidak mempengaruhi hasil dadu</sub>
- D. terambil kartu As pada pengambilan pertama dan terambil kartu As pada pengambilan kedua dari 52 kartu tanpa pengembalian  
  <sub>Salah: pengambilan pertama mengubah isi tumpukan sehingga peluang kedua berubah</sub>

**Pembahasan:** Dua kejadian saling bebas bila terjadinya yang satu tidak mempengaruhi peluang yang lain. Koin dan dadu terpisah sehingga saling bebas; ketiga pasangan lain saling mempengaruhi.
**Acuan:** siswa — siswa hal.172

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12-b04-b-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: frekuensi harapan kejadian majemuk*

Tiga koin setimbang dilempar bersamaan sebanyak 400 kali. Frekuensi harapan munculnya sisi gambar pada ketiga koin adalah ....

- A. $200$  
  <sub>Salah: memakai peluang satu koin ($\frac{1}{2}$)</sub>
- B. $100$  
  <sub>Salah: memakai peluang dua koin ($\frac{1}{4}$)</sub>
- C. $150$  
  <sub>Salah: memakai peluang $\frac{3}{8}$, yaitu peluang tepat dua gambar</sub>
- **D. $50$** ✅  
  <sub>Benar: $P=\left(\frac{1}{2}\right)^3=\frac{1}{8}$ sehingga $Fh=\frac{1}{8}\times 400=50$</sub>

**Pembahasan:** Ketiga koin saling bebas, jadi $P=\frac{1}{2}\times\frac{1}{2}\times\frac{1}{2}=\frac{1}{8}$. $Fh=P\times n=\frac{1}{8}\times 400=50$.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12-b04-b-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: peluang bersyarat pengambilan kedua*

Sebuah kotak berisi 7 kelereng hijau dan 3 kelereng kuning. Satu kelereng hijau diambil dan tidak dikembalikan. Jika sebuah kelereng diambil lagi secara acak, peluang terambil kelereng hijau adalah ....

- A. $\frac{7}{9}$  
  <sub>Salah: hanya mengurangi penyebut, pembilang tetap 7</sub>
- B. $\frac{7}{10}$  
  <sub>Salah: lupa bahwa satu kelereng sudah diambil (isi kotak dianggap tetap)</sub>
- C. $\frac{3}{5}$  
  <sub>Salah: hanya mengurangi pembilang, penyebut tetap 10</sub>
- **D. $\frac{2}{3}$** ✅  
  <sub>Benar: setelah satu hijau diambil tersisa 6 hijau dari 9 kelereng, sehingga $\frac{6}{9}=\frac{2}{3}$</sub>

**Pembahasan:** Sisa kelereng: 6 hijau dan 3 kuning, total 9. Peluang hijau kedua $=\frac{6}{9}=\frac{2}{3}$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12-b04-b-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: mencari irisan dari gabungan*

Diketahui $P(A)=\frac{3}{5}$, $P(B)=\frac{1}{2}$, dan $P(A \cup B)=\frac{9}{10}$. Nilai $P(A \cap B)$ adalah ....

- A. $\frac{3}{10}$  
  <sub>Salah: menghitung $P(A \cup B)-P(A)$</sub>
- **B. $\frac{1}{5}$** ✅  
  <sub>Benar: $P(A \cap B)=P(A)+P(B)-P(A \cup B)=\frac{6}{10}+\frac{5}{10}-\frac{9}{10}=\frac{1}{5}$</sub>
- C. $\frac{2}{5}$  
  <sub>Salah: menghitung $P(A \cup B)-P(B)$</sub>
- D. $\frac{11}{10}$  
  <sub>Salah: hanya menjumlahkan $P(A)+P(B)$ tanpa mengurangi $P(A \cup B)$</sub>

**Pembahasan:** Dari $P(A \cup B)=P(A)+P(B)-P(A \cap B)$ diperoleh $P(A \cap B)=\frac{3}{5}+\frac{1}{2}-\frac{9}{10}=\frac{1}{5}$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12-b04-b-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: kombinasi pengambilan sekaligus*

Suatu kotak berisi 7 kelereng merah, 6 kelereng hijau, dan 2 kelereng biru. Tiga kelereng diambil sekaligus secara acak (setiap kelereng berpeluang sama). Peluang terambilnya dua kelereng merah dan satu kelereng hijau adalah ....

- **A. $\frac{18}{65}$** ✅  
  <sub>Benar: $\frac{C(7,2)\times C(6,1)}{C(15,3)}=\frac{21\times 6}{455}=\frac{18}{65}$</sub>
- B. $\frac{6}{65}$  
  <sub>Salah: hanya satu urutan (merah, merah, hijau), lupa ada 3 urutan berbeda</sub>
- C. $\frac{3}{65}$  
  <sub>Salah: hanya menghitung cara memilih dua merah dan mengabaikan pilihan hijau</sub>
- D. $\frac{1}{35}$  
  <sub>Salah: menjumlahkan 7 dan 6, bukan mengalikan banyak cara memilih</sub>

**Pembahasan:** Banyak cara memilih 3 dari 15: $C(15,3)=455$. Dua merah dari 7: $C(7,2)=21$, satu hijau dari 6: $C(6,1)=6$, sehingga $21\times 6=126$ cara. $P=\frac{126}{455}=\frac{18}{65}$.
**Acuan:** pretest — kelas12-b04-p0187-uji-kompetensi-bab-4-7c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12-b04-b-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: kombinasi pengambilan sekaligus*

Sebuah keranjang buah memuat 2 apel, 5 jeruk, dan 6 mangga. Tiga buah dipilih sekaligus secara acak. Peluang bahwa buah yang terpilih terdiri dari satu apel, satu jeruk, dan satu mangga adalah ....

- A. $\frac{60}{2197}$  
  <sub>Salah: memakai penyebut $13^3$ seperti pengambilan dengan pengembalian</sub>
- B. $\frac{5}{143}$  
  <sub>Salah: memakai satu urutan (apel, jeruk, mangga) saja dan lupa 3! urutan</sub>
- **C. $\frac{30}{143}$** ✅  
  <sub>Benar: $\frac{2\times 5\times 6}{C(13,3)}=\frac{60}{286}=\frac{30}{143}$</sub>
- D. $\frac{15}{143}$  
  <sub>Salah: memakai kasus dua mangga dan satu apel, bukan satu dari tiap jenis</sub>

**Pembahasan:** $C(13,3)=286$. Cara memilih satu dari tiap jenis $=2\times 5\times 6=60$. $P=\frac{60}{286}=\frac{30}{143}$.
**Acuan:** pretest — kelas12-b04-p0187-uji-kompetensi-bab-4-7d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12-b04-b-medium-bt01-003
*variasi (angka) | C4 | 4 langkah | jenis: dua tahap dengan pemindahan benda*

Dompet pertama berisi 6 keping uang logam seribu rupiah dan 2 keping uang logam lima ratus rupiah. Dompet kedua berisi 2 keping uang logam seribu rupiah dan 7 keping uang logam lima ratus rupiah. Sekeping uang logam diambil secara acak dari dompet pertama dan dimasukkan ke dompet kedua. Kemudian sekeping uang logam diambil secara acak dari dompet kedua. Peluang bahwa uang logam yang diambil dari dompet kedua adalah uang logam lima ratus rupiah adalah ....

- A. $\frac{7}{9}$  
  <sub>Salah: mengabaikan pemindahan koin dari dompet pertama</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: hanya memakai peluang koin lima ratus dari dompet pertama</sub>
- C. $\frac{21}{40}$  
  <sub>Salah: hanya menghitung kasus koin seribu yang dipindahkan</sub>
- **D. $\frac{29}{40}$** ✅  
  <sub>Benar: $\frac{6}{8}\times\frac{7}{10}+\frac{2}{8}\times\frac{8}{10}=\frac{42}{80}+\frac{16}{80}=\frac{29}{40}$</sub>

**Pembahasan:** Jika koin seribu dipindahkan (peluang $\frac{6}{8}$), dompet kedua berisi 3 seribu dan 7 lima ratus sehingga peluang lima ratus $\frac{7}{10}$. Jika koin lima ratus dipindahkan (peluang $\frac{2}{8}$), dompet kedua berisi 2 seribu dan 8 lima ratus sehingga $\frac{8}{10}$. Jumlahnya $\frac{29}{40}$.
**Acuan:** pretest — kelas12-b04-p0188-uji-kompetensi-bab-4-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12-b04-b-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: dua dadu dalam dua lemparan*

Sepasang dadu setimbang dilemparkan bersama sebanyak dua kali. Peluang munculnya jumlah mata dadu 6 pada salah satu lemparan dan jumlah mata dadu 9 pada lemparan yang lain adalah ....

- A. $\frac{5}{324}$  
  <sub>Salah: hanya satu urutan (6 dulu baru 9), lupa urutan sebaliknya</sub>
- **B. $\frac{5}{162}$** ✅  
  <sub>Benar: $2\times\frac{5}{36}\times\frac{4}{36}=\frac{40}{1296}=\frac{5}{162}$</sub>
- C. $\frac{1}{18}$  
  <sub>Salah: memakai peluang $\frac{1}{6}$ untuk kedua jumlah</sub>
- D. $\frac{1}{4}$  
  <sub>Salah: menjumlahkan kedua peluang, padahal lemparan saling bebas dan dikalikan</sub>

**Pembahasan:** Jumlah 6 ada 5 pasangan, jumlah 9 ada 4 pasangan. Dua urutan: (6 lalu 9) atau (9 lalu 6), saling lepas. $P=\frac{5}{36}\times\frac{4}{36}+\frac{4}{36}\times\frac{5}{36}=\frac{5}{162}$.
**Acuan:** siswa — siswa hal.173 Contoh 4.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12-b04-b-medium-bt01-005
*variasi (konteks) | C3 | 3 langkah | jenis: kartu bridge dengan dua syarat*

Satu kartu dipilih secara acak dari satu set 52 kartu bridge (4 jenis, tiap jenis berisi As, nomor 2 sampai 10, J, Q, dan K; jenis sekop dan keriting berwarna hitam). Peluang terambilnya kartu berwarna hitam yang bernomor lebih dari empat dan kurang dari sembilan adalah ....

- **A. $\frac{2}{13}$** ✅  
  <sub>Benar: kartu bernomor 5, 6, 7, 8 pada dua jenis hitam: $4\times 2=8$ kartu, sehingga $P=\frac{8}{52}=\frac{2}{13}$</sub>
- B. $\frac{21}{26}$  
  <sub>Salah: menjumlahkan peluang kartu hitam dan peluang kartu bernomor 5 sampai 8</sub>
- C. $\frac{3}{13}$  
  <sub>Salah: ikut menghitung nomor 4 dan 9 (batas tidak termasuk)</sub>
- D. $\frac{1}{13}$  
  <sub>Salah: hanya menghitung satu jenis hitam, lupa jenis hitam kedua</sub>

**Pembahasan:** Syarat: hitam (sekop atau keriting) dan nomor 5, 6, 7, atau 8. Banyak kartu $=2\times 4=8$ dari 52 kartu, jadi $P=\frac{8}{52}=\frac{2}{13}$.
**Acuan:** siswa — siswa hal.179 Contoh 4.11

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12-b04-b-medium-bt01-006
*variasi (konteks) | C3 | 3 langkah | jenis: tabel dua pilihan sekaligus*

Karyawan sebuah perusahaan menurut divisi dan status kepegawaian:

|Divisi|Tetap|Kontrak|
|---|---|---|
|Produksi|36|44|
|Pemasaran|24|16|
|Keuangan|18|12|

Dua karyawan dipilih sekaligus secara acak dari seluruh karyawan pada tabel. Peluang terpilih satu karyawan tetap dan satu karyawan kontrak adalah ....

- A. $\frac{312}{625}$  
  <sub>Salah: memakai cara dengan pengembalian (penyebut 150 terus)</sub>
- B. $\frac{2}{149}$  
  <sub>Salah: menjumlahkan 78 dan 72, bukan mengalikan</sub>
- C. $\frac{936}{3725}$  
  <sub>Salah: hanya satu urutan (tetap dulu, kontrak kemudian), lupa urutan sebaliknya</sub>
- **D. $\frac{1872}{3725}$** ✅  
  <sub>Benar: $\frac{78\times 72}{C(150,2)}=\frac{5.616}{11.175}=\frac{1.872}{3.725}$</sub>

**Pembahasan:** Karyawan tetap $36+24+18=78$ dan kontrak $44+16+12=72$, total 150. $P=\frac{78\times 72}{C(150,2)}=\frac{5.616}{11.175}=\frac{1.872}{3.725}$.
**Acuan:** siswa — siswa hal.180 Contoh 4.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12-b04-b-medium-bt01-007
*variasi (konteks) | C3 | 3 langkah | jenis: tabel pilihan berurutan*

Anggota tiga klub di sebuah sekolah:

|Klub|Putra|Putri|
|---|---|---|
|Seni|14|26|
|Olahraga|30|10|
|Sains|16|24|

Dua anggota dipilih satu per satu secara acak dari seluruh anggota pada tabel tanpa pengembalian. Peluang pilihan pertama anggota putra dan pilihan kedua anggota putra yang lain adalah ....

- **A. $\frac{59}{238}$** ✅  
  <sub>Benar: $\frac{60}{120}\times\frac{59}{119}=\frac{59}{238}$</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: memakai cara dengan pengembalian ($\frac{1}{2}\times\frac{1}{2}$)</sub>
- C. $\frac{59}{240}$  
  <sub>Salah: mengurangi pembilang tetapi penyebut pilihan kedua tidak dikurangi</sub>
- D. $\frac{30}{119}$  
  <sub>Salah: tidak mengurangi pembilang pada pilihan kedua</sub>

**Pembahasan:** Putra $=14+30+16=60$ dari 120 anggota. Pilihan kedua: tersisa 59 putra dari 119 anggota. $P=\frac{60}{120}\times\frac{59}{119}=\frac{59}{238}$.
**Acuan:** siswa — siswa hal.180 Contoh 4.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12-b04-b-medium-bt01-008
*variasi (konteks) | C4 | 3 langkah | jenis: alur percobaan bercabang*

Suatu percobaan dilakukan dengan aturan berikut.

- Pertama dilempar sekeping uang logam setimbang.
- Jika muncul sisi angka, percobaan berhenti.
- Jika muncul sisi gambar, dilempar sebuah dadu setimbang bersisi enam.
- Jika mata dadu yang muncul kelipatan tiga, dadu dilempar sekali lagi lalu percobaan berhenti apa pun hasilnya. Jika bukan kelipatan tiga, percobaan berhenti.

Peluang bahwa banyak seluruh pelemparan (uang logam dan dadu) dalam percobaan itu tepat tiga kali adalah ....

- A. $\frac{1}{3}$  
  <sub>Salah: lupa peluang uang logam muncul gambar</sub>
- B. $\frac{5}{6}$  
  <sub>Salah: menjumlahkan peluang gambar dan peluang dadu kelipatan tiga</sub>
- **C. $\frac{1}{6}$** ✅  
  <sub>Benar: jalurnya hanya: gambar, lalu dadu kelipatan tiga ($\{3,6\}$), lalu dadu lagi. $P=\frac{1}{2}\times\frac{2}{6}=\frac{1}{6}$</sub>
- D. $\frac{1}{18}$  
  <sub>Salah: mengira lemparan dadu kedua juga harus kelipatan tiga</sub>

**Pembahasan:** Tiga pelemparan terjadi hanya bila uang logam gambar ($\frac{1}{2}$) dan dadu pertama kelipatan tiga ($\frac{2}{6}=\frac{1}{3}$); dadu kedua dilempar tanpa syarat. $P=\frac{1}{2}\times\frac{1}{3}=\frac{1}{6}$.
**Acuan:** pretest — kelas12-b04-p0186-uji-kompetensi-bab-4-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12-b04-b-medium-bt01-009
*variasi (konteks) | C4 | 4 langkah | jenis: dua tahap dengan pemindahan benda*

Kantong pertama berisi 7 permen stroberi dan 2 permen jeruk. Kantong kedua berisi 4 permen stroberi dan 5 permen jeruk. Sebuah permen diambil secara acak dari kantong pertama dan dimasukkan ke kantong kedua. Kemudian sebuah permen diambil secara acak dari kantong kedua. Peluang bahwa permen yang diambil dari kantong kedua adalah permen jeruk adalah ....

- A. $\frac{2}{9}$  
  <sub>Salah: hanya memakai peluang permen jeruk dari kantong pertama</sub>
- **B. $\frac{47}{90}$** ✅  
  <sub>Benar: $\frac{7}{9}\times\frac{5}{10}+\frac{2}{9}\times\frac{6}{10}=\frac{35}{90}+\frac{12}{90}=\frac{47}{90}$</sub>
- C. $\frac{7}{18}$  
  <sub>Salah: hanya menghitung kasus permen stroberi yang dipindahkan</sub>
- D. $\frac{5}{9}$  
  <sub>Salah: mengabaikan pemindahan permen dari kantong pertama</sub>

**Pembahasan:** Bila stroberi dipindahkan ($\frac{7}{9}$), kantong kedua berisi 5 stroberi dan 5 jeruk, peluang jeruk $\frac{5}{10}$. Bila jeruk dipindahkan ($\frac{2}{9}$), kantong kedua berisi 4 stroberi dan 6 jeruk, peluang jeruk $\frac{6}{10}$. Jumlahnya $\frac{47}{90}$.
**Acuan:** pretest — kelas12-b04-p0188-uji-kompetensi-bab-4-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12-b04-b-medium-bt01-010
*orisinal | C3 | 2 langkah | jenis: gabungan kejadian saling bebas*

Kejadian $A$ dan $B$ saling bebas. Peluang $A$ terjadi adalah $\frac{2}{5}$ dan peluang $B$ tidak terjadi adalah $\frac{4}{7}$. Nilai $P(A \cup B)$ adalah ....

- A. $\frac{17}{35}$  
  <sub>Salah: mengurangi irisan dua kali</sub>
- B. $\frac{29}{35}$  
  <sub>Salah: menjumlahkan tanpa mengurangi irisan</sub>
- C. $\frac{6}{35}$  
  <sub>Salah: hanya menghitung $P(A\cap B)$</sub>
- **D. $\frac{23}{35}$** ✅  
  <sub>Benar: $P(B)=1-\frac{4}{7}=\frac{3}{7}$ dan $P(A\cap B)=\frac{2}{5}\times\frac{3}{7}=\frac{6}{35}$, sehingga $P(A\cup B)=\frac{14}{35}+\frac{15}{35}-\frac{6}{35}=\frac{23}{35}$</sub>

**Pembahasan:** Saling bebas: $P(A\cap B)=P(A)P(B)=\frac{6}{35}$. $P(A\cup B)=\frac{2}{5}+\frac{3}{7}-\frac{6}{35}=\frac{23}{35}$.
**Acuan:** siswa — siswa hal.172

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12-b04-b-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: peluang tak diketahui pada kejadian saling bebas*

Kejadian $A$ dan $B$ saling bebas dengan $P(A)=\frac{1}{4}$ dan $P(A \cup B)=\frac{1}{2}$. Nilai $P(B)$ adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: menganggap $A$ dan $B$ saling lepas ($P(B)=P(A\cup B)-P(A)$)</sub>
- **B. $\frac{1}{3}$** ✅  
  <sub>Benar: $\frac{1}{4}+P(B)-\frac{1}{4}P(B)=\frac{1}{2}$ sehingga $\frac{3}{4}P(B)=\frac{1}{4}$ dan $P(B)=\frac{1}{3}$</sub>
- C. $\frac{2}{3}$  
  <sub>Salah: lupa mengurangkan $P(A)$ dari ruas kanan sehingga $\frac{3}{4}P(B)=\frac{1}{2}$</sub>
- D. $\frac{1}{5}$  
  <sub>Salah: salah tanda: $\frac{5}{4}P(B)=\frac{1}{4}$</sub>

**Pembahasan:** Saling bebas: $P(A\cup B)=P(A)+P(B)-P(A)P(B)$. $\frac{1}{4}+\frac{3}{4}P(B)=\frac{1}{2}$, $P(B)=\frac{1}{4}\times\frac{4}{3}=\frac{1}{3}$.
**Acuan:** siswa — siswa hal.172

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12-b04-b-medium-bt01-012
*orisinal | C3 | 2 langkah | jenis: peluang bersyarat dari data cacah*

Dalam suatu kelas yang terdiri dari 60 siswa, 35 siswa menyukai basket, 28 siswa menyukai voli, dan 12 siswa menyukai keduanya. Seorang siswa dipilih secara acak. Jika diketahui siswa itu menyukai voli, peluang ia juga menyukai basket adalah ....

- A. $\frac{12}{35}$  
  <sub>Salah: syarat dan kejadian tertukar (membagi dengan banyak penyuka basket)</sub>
- B. $\frac{1}{5}$  
  <sub>Salah: membagi irisan dengan seluruh siswa, bukan dengan penyuka voli</sub>
- **C. $\frac{3}{7}$** ✅  
  <sub>Benar: $P(\text{basket}|\text{voli})=\frac{12}{28}=\frac{3}{7}$</sub>
- D. $\frac{7}{12}$  
  <sub>Salah: memakai peluang menyukai basket tanpa memperhatikan syarat</sub>

**Pembahasan:** Ruang sampel menyempit menjadi 28 siswa penyuka voli, 12 di antaranya menyukai basket. $P=\frac{12}{28}=\frac{3}{7}$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12-b04-b-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: paling sedikit satu tanpa pengembalian*

Sebuah kotak berisi 4 bola merah dan 6 bola putih. Tiga bola diambil satu per satu secara acak tanpa pengembalian. Peluang terambil paling sedikit satu bola merah adalah ....

- **A. $\frac{5}{6}$** ✅  
  <sub>Benar: $1-\frac{6}{10}\times\frac{5}{9}\times\frac{4}{8}=1-\frac{1}{6}=\frac{5}{6}$</sub>
- B. $\frac{1}{6}$  
  <sub>Salah: hanya menghitung peluang tidak ada bola merah</sub>
- C. $\frac{1}{2}$  
  <sub>Salah: hanya menghitung peluang tepat satu bola merah</sub>
- D. $\frac{98}{125}$  
  <sub>Salah: memakai cara dengan pengembalian</sub>

**Pembahasan:** Komplemen dari 'paling sedikit satu merah' adalah 'ketiganya putih': $\frac{6}{10}\times\frac{5}{9}\times\frac{4}{8}=\frac{1}{6}$. Jadi $P=1-\frac{1}{6}=\frac{5}{6}$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12-b04-b-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: frekuensi harapan kejadian gabungan*

Dua dadu setimbang dilempar bersamaan sebanyak 900 kali. Frekuensi harapan munculnya jumlah mata dadu 5 atau 8 adalah ....

- A. $100$  
  <sub>Salah: hanya menghitung jumlah 5 ($\frac{4}{36}\times 900$)</sub>
- **B. $225$** ✅  
  <sub>Benar: $P=\frac{4}{36}+\frac{5}{36}=\frac{1}{4}$ sehingga $Fh=\frac{1}{4}\times 900=225$</sub>
- C. $125$  
  <sub>Salah: hanya menghitung jumlah 8 ($\frac{5}{36}\times 900$)</sub>
- D. $25$  
  <sub>Salah: memakai peluang satu pasangan saja ($\frac{1}{36}\times 900$)</sub>

**Pembahasan:** Jumlah 5: 4 pasangan, jumlah 8: 5 pasangan, saling lepas. $P=\frac{9}{36}=\frac{1}{4}$. $Fh=\frac{1}{4}\times 900=225$.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12-b04-b-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: tepat satu dari dua kejadian bebas*

Peluang Ani lulus suatu seleksi adalah $\frac{3}{5}$ dan peluang Budi lulus seleksi yang sama adalah $\frac{2}{3}$. Hasil seleksi keduanya saling bebas. Peluang bahwa tepat satu dari mereka lulus adalah ....

- A. $\frac{13}{15}$  
  <sub>Salah: menghitung peluang paling sedikit satu lulus</sub>
- B. $\frac{2}{15}$  
  <sub>Salah: menghitung peluang keduanya tidak lulus</sub>
- **C. $\frac{7}{15}$** ✅  
  <sub>Benar: $\frac{3}{5}\times\frac{1}{3}+\frac{2}{5}\times\frac{2}{3}=\frac{3}{15}+\frac{4}{15}=\frac{7}{15}$</sub>
- D. $\frac{2}{5}$  
  <sub>Salah: menghitung peluang keduanya lulus</sub>

**Pembahasan:** Tepat satu lulus: (Ani lulus, Budi tidak) atau (Ani tidak, Budi lulus). $P=\frac{3}{5}\times\frac{1}{3}+\frac{2}{5}\times\frac{2}{3}=\frac{7}{15}$.
**Acuan:** siswa — siswa hal.171

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12-b04-b-medium-bt01-016
*orisinal | C4 | 4 langkah | jenis: dua pengambilan berurutan dengan syarat*

Sepuluh kartu diberi nomor 1 sampai 10. Dua kartu diambil satu per satu secara acak tanpa pengembalian. Peluang kartu pertama bernomor genap dan kartu kedua bernomor lebih dari 7 adalah ....

- A. $\frac{3}{20}$  
  <sub>Salah: memakai cara dengan pengembalian</sub>
- B. $\frac{1}{6}$  
  <sub>Salah: menganggap kartu kedua selalu punya 3 pilihan bernomor lebih dari 7</sub>
- C. $\frac{1}{10}$  
  <sub>Salah: hanya menghitung kasus kartu pertama 2, 4, atau 6</sub>
- **D. $\frac{13}{90}$** ✅  
  <sub>Benar: kartu pertama 2, 4, atau 6: $3\times 3=9$ pasangan; kartu pertama 8 atau 10: $2\times 2=4$ pasangan; $P=\frac{13}{90}$</sub>

**Pembahasan:** Pasangan (pertama, kedua): pertama $\in\{2,4,6\}$ dan kedua $\in\{8,9,10\}$ ada 9; pertama $\in\{8,10\}$ dan kedua tinggal 2 pilihan ada 4. Total 13 dari $10\times 9=90$, sehingga $P=\frac{13}{90}$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12-b04-b-medium-bt01-017
*orisinal | C4 | 3 langkah | jenis: peluang dua tahap koin dan kotak*

Sekeping uang logam setimbang dilempar. Jika muncul gambar, sebuah bola diambil secara acak dari kotak I yang berisi 4 bola merah dan 2 bola putih. Jika muncul angka, sebuah bola diambil secara acak dari kotak II yang berisi 3 bola merah dan 7 bola putih. Peluang terambil bola merah adalah ....

- **A. $\frac{29}{60}$** ✅  
  <sub>Benar: $\frac{1}{2}\times\frac{4}{6}+\frac{1}{2}\times\frac{3}{10}=\frac{1}{3}+\frac{3}{20}=\frac{29}{60}$</sub>
- B. $\frac{29}{30}$  
  <sub>Salah: lupa mengalikan dengan peluang uang logam $\frac{1}{2}$</sub>
- C. $\frac{7}{16}$  
  <sub>Salah: menggabungkan semua bola: $\frac{4+3}{6+10}$</sub>
- D. $\frac{1}{3}$  
  <sub>Salah: hanya menghitung jalur kotak I</sub>

**Pembahasan:** Jalur gambar lalu merah: $\frac{1}{2}\times\frac{4}{6}=\frac{1}{3}$. Jalur angka lalu merah: $\frac{1}{2}\times\frac{3}{10}=\frac{3}{20}$. Jumlah $=\frac{29}{60}$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12-b04-b-medium-bt01-018
*orisinal | C4 | 4 langkah | jenis: gabungan dua kejadian pada dua dadu*

Dua dadu setimbang dilempar bersamaan. Kejadian $A$ adalah jumlah kedua mata dadu bilangan prima dan kejadian $B$ adalah selisih kedua mata dadu tepat 1. Peluang $P(A \cup B)$ adalah ....

- A. $\frac{2}{9}$  
  <sub>Salah: hanya menghitung irisan</sub>
- B. $\frac{25}{216}$  
  <sub>Salah: mengalikan $P(A)$ dan $P(B)$ seolah saling bebas</sub>
- **C. $\frac{17}{36}$** ✅  
  <sub>Benar: $n(A)=15$, $n(B)=10$, $n(A\cap B)=8$ sehingga $P(A\cup B)=\frac{15+10-8}{36}=\frac{17}{36}$</sub>
- D. $\frac{25}{36}$  
  <sub>Salah: tidak mengurangi irisan</sub>

**Pembahasan:** $A$: jumlah 2, 3, 5, 7, 11 sebanyak $1+2+4+6+2=15$. $B$: 10 pasangan. $A\cap B$: selisih 1 dengan jumlah prima (3, 5, 7, 11) sebanyak $2+2+2+2=8$. $P=\frac{15+10-8}{36}=\frac{17}{36}$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12-b04-b-medium-bt01-019
*orisinal | C4 | 4 langkah | jenis: uji kebebasan dua kejadian pada dua dadu*

Sebuah dadu merah dan sebuah dadu putih setimbang dilempar bersamaan. Pasangan kejadian berikut yang saling bebas adalah ....

- A. dadu merah muncul genap dan jumlah kedua mata dadu 8  
  <sub>Salah: $P(A\cap B)=\frac{3}{36}\neq\frac{1}{2}\times\frac{5}{36}$</sub>
- B. kedua mata dadu sama dan jumlah kedua mata dadu genap  
  <sub>Salah: $P(A\cap B)=\frac{6}{36}\neq\frac{1}{6}\times\frac{1}{2}$</sub>
- C. dadu merah muncul 6 dan jumlah kedua mata dadu 12  
  <sub>Salah: $P(A\cap B)=\frac{1}{36}\neq\frac{1}{6}\times\frac{1}{36}$</sub>
- **D. dadu merah muncul genap dan jumlah kedua mata dadu ganjil** ✅  
  <sub>Benar: $P(A)=\frac{1}{2}$, $P(B)=\frac{1}{2}$, $P(A\cap B)=\frac{9}{36}=\frac{1}{4}=P(A)P(B)$</sub>

**Pembahasan:** Uji $P(A\cap B)=P(A)P(B)$. Merah genap dan jumlah ganjil: $\frac{1}{4}=\frac{1}{2}\times\frac{1}{2}$ (bebas). Ketiga pasangan lain tidak memenuhi kesamaan itu sehingga tidak saling bebas.
**Acuan:** siswa — siswa hal.172

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12-b04-b-medium-bt01-020
*orisinal | C4 | 3 langkah | jenis: uji kebebasan dari nilai peluang*

Diketahui $P(A)=\frac{1}{2}$, $P(B)=\frac{1}{3}$, dan $P(A \cap B)=\frac{1}{6}$. Pernyataan yang benar adalah ....

- A. $A$ dan $B$ saling bebas dan $P(A \cup B)=\frac{5}{6}$  
  <sub>Salah: lupa mengurangi irisan pada rumus gabungan</sub>
- **B. $A$ dan $B$ saling bebas dan $P(A \cup B)=\frac{2}{3}$** ✅  
  <sub>Benar: $P(A)P(B)=\frac{1}{6}=P(A\cap B)$ sehingga saling bebas; $P(A\cup B)=\frac{1}{2}+\frac{1}{3}-\frac{1}{6}=\frac{2}{3}$</sub>
- C. $A$ dan $B$ tidak saling bebas dan $P(A \cup B)=\frac{2}{3}$  
  <sub>Salah: salah menguji: $P(A)P(B)$ sebenarnya sama dengan $P(A\cap B)$</sub>
- D. $A$ dan $B$ saling lepas dan $P(A \cup B)=\frac{5}{6}$  
  <sub>Salah: irisan tidak nol sehingga tidak saling lepas, dan gabungan hanya dijumlahkan</sub>

**Pembahasan:** $P(A)P(B)=\frac{1}{2}\times\frac{1}{3}=\frac{1}{6}=P(A\cap B)$, jadi saling bebas (dan tidak saling lepas karena irisan tidak nol). $P(A\cup B)=\frac{1}{2}+\frac{1}{3}-\frac{1}{6}=\frac{2}{3}$.
**Acuan:** siswa — siswa hal.172

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12-b04-b-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim batas peluang*

Diketahui $P(A)=0{,}6$ dan $P(B)=0{,}7$. Pernyataan yang pasti benar adalah ....

- A. $A$ dan $B$ pasti saling bebas  
  <sub>Salah: keterbebasan tidak ditentukan oleh $P(A)$ dan $P(B)$ saja; irisan tidak diketahui</sub>
- **B. $A$ dan $B$ tidak mungkin saling lepas** ✅  
  <sub>Benar: jika saling lepas maka $P(A \cup B)=0{,}6+0{,}7=1{,}3>1$, mustahil; jadi irisan tidak kosong ($P(A \cap B)\geq 0{,}3$)</sub>
- C. $P(A \cap B)$ dapat bernilai $0{,}2$  
  <sub>Salah: $P(A \cap B)=P(A)+P(B)-P(A \cup B)\geq 1{,}3-1=0{,}3$, jadi $0{,}2$ tidak mungkin</sub>
- D. $P(A \cup B)=1{,}3$  
  <sub>Salah: lupa mengurangi irisan; peluang tidak pernah lebih dari 1</sub>

**Pembahasan:** $P(A \cap B)=P(A)+P(B)-P(A \cup B)\geq 0{,}6+0{,}7-1=0{,}3>0$, sehingga $A$ dan $B$ pasti beririsan dan tidak saling lepas. Pernyataan lain salah: irisan tidak mungkin $0{,}2$, gabungan tidak boleh $1{,}3$, dan keterbebasan tidak dapat dipastikan.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12-b04-b-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: syarat parameter kejadian saling lepas*

Kejadian $A$ dan $B$ saling lepas dengan $P(A)=2x$ dan $P(B)=3x-\frac{1}{10}$. Nilai $x$ terbesar yang masih mungkin adalah ....

- A. $\frac{1}{2}$  
  <sub>Salah: hanya memakai syarat $P(A)\leq 1$</sub>
- **B. $\frac{11}{50}$** ✅  
  <sub>Benar: saling lepas: $P(A \cup B)=5x-\frac{1}{10}\leq 1$ sehingga $x\leq\frac{11}{50}$; syarat $P(A)\leq 1$ dan $P(B)\leq 1$ lebih longgar</sub>
- C. $\frac{1}{5}$  
  <sub>Salah: lupa suku $-\frac{1}{10}$ sehingga memakai $5x\leq 1$</sub>
- D. $\frac{11}{30}$  
  <sub>Salah: hanya memakai syarat $P(B)\leq 1$ dan mengabaikan syarat gabungan</sub>

**Pembahasan:** $P(A \cup B)=P(A)+P(B)=5x-\frac{1}{10}$ dan harus $\leq 1$, jadi $x\leq\frac{11}{10}\times\frac{1}{5}=\frac{11}{50}$. Syarat $2x\leq 1$ memberi $x\leq\frac{1}{2}$ dan $3x-\frac{1}{10}\leq 1$ memberi $x\leq\frac{11}{30}$, keduanya lebih longgar. Nilai terbesar $x=\frac{11}{50}$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12-b04-b-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: syarat parameter kejadian saling bebas*

Kejadian $A$ dan $B$ saling bebas dengan $P(A)=x$, $P(B)=2x$, dan $P(A \cup B)=\frac{18}{25}$. Nilai $x$ yang memenuhi sehingga kedua peluang berada di antara 0 dan 1 adalah ....

- A. $\frac{6}{5}$  
  <sub>Salah: akar kedua persamaan kuadrat yang membuat $P(A)>1$</sub>
- B. $\frac{3}{5}$  
  <sub>Salah: salah menyebut nilai $P(B)$ sebagai $x$</sub>
- **C. $\frac{3}{10}$** ✅  
  <sub>Benar: $3x-2x^2=\frac{18}{25}$ memberi $x=\frac{3}{10}$ atau $x=\frac{6}{5}$; $x=\frac{6}{5}$ membuat peluang lebih dari 1</sub>
- D. $\frac{6}{25}$  
  <sub>Salah: menganggap saling lepas: $3x=\frac{18}{25}$</sub>

**Pembahasan:** Saling bebas: $P(A \cup B)=x+2x-2x^2=\frac{18}{25}$, yaitu $50x^2-75x+18=0$ atau $(10x-3)(5x-6)=0$. Jadi $x=\frac{3}{10}$ atau $x=\frac{6}{5}$. Karena $P(A)=x\leq 1$, hanya $x=\frac{3}{10}$ yang berlaku (cek: $0{,}3+0{,}6-0{,}18=0{,}72$).
**Acuan:** siswa — siswa hal.172

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12-b04-b-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan lupa irisan*

Dari satu set 52 kartu bridge yang dikocok, satu kartu diambil secara acak. Rani menghitung peluang terambil kartu As atau kartu hati dengan $\frac{4}{52}+\frac{13}{52}=\frac{17}{52}$. Pernyataan yang benar tentang hitungan Rani adalah ....

- A. As hati belum terhitung; peluang yang benar $\frac{9}{26}$  
  <sub>Salah: irisan ditambahkan padahal harus dikurangkan</sub>
- B. kedua kejadian saling bebas sehingga dikalikan; peluangnya $\frac{1}{52}$  
  <sub>Salah: perkalian untuk 'dan', bukan 'atau', dan kejadian ini bukan dua pengambilan</sub>
- **C. As hati terhitung dua kali; peluang yang benar $\frac{4}{13}$** ✅  
  <sub>Benar: kartu As hati termasuk As dan termasuk hati sehingga irisan $\frac{1}{52}$ harus dikurangkan: $\frac{17-1}{52}=\frac{4}{13}$</sub>
- D. penyebut harus 51 karena ada dua kejadian; peluangnya $\frac{1}{3}$  
  <sub>Salah: mengira satu kartu sudah diambil sehingga penyebut menjadi 51</sub>

**Pembahasan:** Kejadian As dan hati tidak saling lepas karena As hati ada pada keduanya. $P(\text{As} \cup \text{hati})=\frac{4}{52}+\frac{13}{52}-\frac{1}{52}=\frac{16}{52}=\frac{4}{13}$. Hitungan Rani lupa mengurangi irisan.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12-b04-b-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan tanpa pengembalian*

Dua kartu diambil satu per satu secara acak tanpa pengembalian dari 52 kartu bridge. Doni menghitung peluang keduanya kartu As dengan $\frac{4}{52}\times\frac{4}{52}=\frac{1}{169}$. Pernyataan yang benar tentang hitungan Doni adalah ....

- A. kedua pengambilan seharusnya dijumlahkan; peluangnya $\frac{2}{13}$  
  <sub>Salah: menjumlahkan padahal yang diminta kedua-duanya terjadi ('dan')</sub>
- B. hanya penyebut kedua yang menjadi 51; peluangnya $\frac{4}{663}$  
  <sub>Salah: pembilang kedua juga berkurang karena satu As sudah terambil</sub>
- C. hanya pembilang kedua yang menjadi 3; peluangnya $\frac{3}{676}$  
  <sub>Salah: penyebut kedua juga berkurang karena satu kartu sudah terambil</sub>
- **D. pembilang dan penyebut kedua seharusnya 3 dan 51; peluang yang benar $\frac{1}{221}$** ✅  
  <sub>Benar: setelah satu As terambil tersisa 3 As dari 51 kartu: $\frac{4}{52}\times\frac{3}{51}=\frac{1}{221}$</sub>

**Pembahasan:** Tanpa pengembalian, pengambilan kedua bergantung pada pengambilan pertama. $P=\frac{4}{52}\times\frac{3}{51}=\frac{12}{2652}=\frac{1}{221}$. Doni memperlakukan pengambilan seperti dengan pengembalian.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12-b04-b-hard-bt01-006
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan menganggap saling lepas*

Sebuah dadu setimbang dilempar satu kali. Sinta menghitung peluang muncul mata dadu genap atau prima dengan $\frac{3}{6}+\frac{3}{6}=1$ karena menganggap kedua kejadian saling lepas. Pernyataan yang benar adalah ....

- **A. kedua kejadian beririsan di mata 2; peluang yang benar $\frac{5}{6}$** ✅  
  <sub>Benar: genap $=\{2,4,6\}$ dan prima $=\{2,3,5\}$ beririsan di $\{2\}$ sehingga $\frac{3}{6}+\frac{3}{6}-\frac{1}{6}=\frac{5}{6}$</sub>
- B. tidak ada kesalahan; peluangnya $1$  
  <sub>Salah: mata 2 terhitung dua kali sehingga hasil 1 terlalu besar</sub>
- C. kedua kejadian saling bebas sehingga dikalikan; peluangnya $\frac{1}{4}$  
  <sub>Salah: memakai rumus saling bebas untuk 'atau' pada satu lemparan</sub>
- D. kedua kejadian beririsan di mata 2; peluangnya $\frac{2}{3}$  
  <sub>Salah: irisan dikurangkan dua kali</sub>

**Pembahasan:** Mata 2 adalah genap sekaligus prima, jadi kedua kejadian tidak saling lepas. $P=\frac{3}{6}+\frac{3}{6}-\frac{1}{6}=\frac{5}{6}$, yaitu semua mata kecuali 1.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12-b04-b-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: contoh penyangkal klaim*

Andi mengklaim: "Dua kejadian yang tidak saling lepas pasti tidak saling bebas." Pada pelemparan sebuah dadu setimbang, pasangan kejadian yang menyangkal klaim Andi adalah ....

- **A. muncul mata dadu kurang dari 4 dan muncul mata dadu bukan 3 dan bukan 6** ✅  
  <sub>Benar: irisannya $\{1,2\}$ tidak kosong, tetapi $P(A \cap B)=\frac{1}{3}=\frac{1}{2}\times\frac{2}{3}=P(A)P(B)$ sehingga saling bebas</sub>
- B. muncul mata dadu kurang dari 3 dan muncul mata dadu lebih dari 1  
  <sub>Salah: tidak saling lepas dan $\frac{1}{6}\neq\frac{1}{3}\times\frac{5}{6}$, sehingga mendukung klaim</sub>
- C. muncul mata dadu genap dan muncul mata dadu ganjil  
  <sub>Salah: saling lepas, sehingga bukan contoh dari kasus yang diklaim</sub>
- D. muncul mata dadu genap dan muncul bilangan prima  
  <sub>Salah: tidak saling lepas dan $\frac{1}{6}\neq\frac{1}{2}\times\frac{1}{2}$, sehingga justru mendukung klaim</sub>

**Pembahasan:** Penyangkal harus tidak saling lepas (irisan tidak kosong) tetapi saling bebas. $A=\{1,2,3\}$, $B=\{1,2,4,5\}$: $A \cap B=\{1,2\}$, $P(A \cap B)=\frac{2}{6}=\frac{1}{3}$ dan $P(A)P(B)=\frac{1}{2}\times\frac{2}{3}=\frac{1}{3}$. Pasangan lain tidak memenuhi keduanya.
**Acuan:** siswa — siswa hal.172

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12-b04-b-hard-bt01-008
*orisinal | C5 | 3 langkah | jenis: saling lepas lawan saling bebas*

Kejadian $A$ dan $B$ saling lepas dengan $P(A)>0$ dan $P(B)>0$. Pernyataan yang pasti benar adalah ....

- **A. $A$ dan $B$ tidak saling bebas** ✅  
  <sub>Benar: saling lepas berarti $P(A \cap B)=0$, sedangkan $P(A)P(B)>0$; keduanya tidak sama</sub>
- B. $P(A \cup B)=P(A)\times P(B)$  
  <sub>Salah: kejadian saling lepas dijumlahkan, bukan dikalikan</sub>
- C. $P(A \cap B)=P(A)\times P(B)$  
  <sub>Salah: itu syarat saling bebas; di sini $P(A \cap B)=0$ sedangkan hasil kali positif</sub>
- D. $P(A|B)=P(A)$  
  <sub>Salah: sebenarnya $P(A|B)=0$ karena $B$ terjadi berarti $A$ tidak terjadi</sub>

**Pembahasan:** Saling lepas: $P(A \cap B)=0$. Saling bebas menuntut $P(A \cap B)=P(A)P(B)>0$. Keduanya bertentangan, jadi kejadian saling lepas dengan peluang positif tidak mungkin saling bebas. Juga $P(A|B)=\frac{0}{P(B)}=0\neq P(A)$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12-b04-b-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim dengan lawan tanpa pengembalian*

Sebuah kantong berisi $N$ bola dengan $N\geq 2$, terdiri dari $r$ bola merah dan sisanya putih dengan $1\leq r\leq N-1$. Dua bola diambil satu per satu secara acak; peluang keduanya merah adalah $p_1$ bila dengan pengembalian dan $p_2$ bila tanpa pengembalian. Pernyataan yang benar adalah ....

- **A. $p_2<p_1$ untuk setiap nilai $r$ dan $N$ tersebut** ✅  
  <sub>Benar: $p_1=\frac{r}{N}\times\frac{r}{N}$ dan $p_2=\frac{r}{N}\times\frac{r-1}{N-1}$; karena $\frac{r-1}{N-1}<\frac{r}{N}$ untuk $r<N$, maka $p_2<p_1$</sub>
- B. $p_2<p_1$ hanya jika $r>\frac{N}{2}$  
  <sub>Salah: perbandingan itu berlaku untuk semua $r$ dengan $r<N$, tidak bergantung pada setengah $N$</sub>
- C. $p_2>p_1$ untuk setiap nilai $r$ dan $N$ tersebut  
  <sub>Salah: arahnya terbalik: tanpa pengembalian peluang bola merah kedua selalu menyusut</sub>
- D. $p_2=p_1$ untuk setiap nilai $r$ dan $N$ tersebut  
  <sub>Salah: kedua cara hanya sama bila $r=N$, yang dikecualikan</sub>

**Pembahasan:** $\frac{r-1}{N-1}<\frac{r}{N}\iff N(r-1)<r(N-1)\iff -N<-r\iff r<N$. Syarat terakhir selalu dipenuhi, sehingga $p_2<p_1$ untuk semua $r$ dan $N$ pada syarat soal. Contoh: $N=10, r=5$ memberi $p_1=\frac{1}{4}$ dan $p_2=\frac{2}{9}$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12-b04-b-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: uji kebebasan dari tabel dua arah*

Banyak siswa menurut jenis kelamin dan peminatan olahraga:

|Jenis kelamin|Basket|Voli|Renang|
|---|---|---|---|
|Putra|20|12|8|
|Putri|20|18|22|

Seorang siswa dipilih secara acak dari 100 siswa pada tabel berikut. Pasangan kejadian yang saling bebas adalah ....

- A. terpilih siswa putra dan terpilih siswa peminat basket  
  <sub>Salah: $\frac{20}{100}\neq\frac{40}{100}\times\frac{40}{100}=\frac{16}{100}$</sub>
- B. terpilih siswa putra dan terpilih siswa peminat renang  
  <sub>Salah: $\frac{8}{100}\neq\frac{40}{100}\times\frac{30}{100}=\frac{12}{100}$</sub>
- **C. terpilih siswa putra dan terpilih siswa peminat voli** ✅  
  <sub>Benar: $P(\text{putra})=\frac{40}{100}$, $P(\text{voli})=\frac{30}{100}$, $P(\text{putra} \cap \text{voli})=\frac{12}{100}=\frac{40}{100}\times\frac{30}{100}$</sub>
- D. terpilih siswa putri dan terpilih siswa peminat renang  
  <sub>Salah: $\frac{22}{100}\neq\frac{60}{100}\times\frac{30}{100}=\frac{18}{100}$</sub>

**Pembahasan:** Uji $P(A \cap B)=P(A)P(B)$. Putra dan voli: $\frac{12}{100}=0{,}4\times 0{,}3$ (bebas). Putra dan basket: $0{,}20\neq 0{,}16$. Putra dan renang: $0{,}08\neq 0{,}12$. Putri dan renang: $0{,}22\neq 0{,}18$.
**Acuan:** siswa — siswa hal.172

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12-b04-b-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: peluang bersyarat bertingkat dua kotak*

Sebuah dadu setimbang dilempar. Jika muncul mata 1 atau 2, sebuah bola diambil secara acak dari kotak I yang berisi 5 bola merah dan 3 bola putih. Jika muncul mata lainnya, sebuah bola diambil secara acak dari kotak II yang berisi 2 bola merah dan 6 bola putih. Jika diketahui bola yang terambil berwarna merah, peluang bola itu berasal dari kotak I adalah ....

- **A. $\frac{5}{9}$** ✅  
  <sub>Benar: $P(\text{merah})=\frac{1}{3}\times\frac{5}{8}+\frac{2}{3}\times\frac{2}{8}=\frac{3}{8}$ dan $P(\text{I} \cap \text{merah})=\frac{5}{24}$, sehingga $\frac{5/24}{3/8}=\frac{5}{9}$</sub>
- B. $\frac{5}{8}$  
  <sub>Salah: memakai peluang bola merah pada kotak I tanpa membalik syarat</sub>
- C. $\frac{5}{24}$  
  <sub>Salah: hanya menghitung $P(\text{I} \cap \text{merah})$ dan lupa membagi dengan $P(\text{merah})$</sub>
- D. $\frac{1}{3}$  
  <sub>Salah: hanya memakai peluang memilih kotak I dan mengabaikan informasi bola merah</sub>

**Pembahasan:** $P(\text{I} \cap \text{merah})=\frac{2}{6}\times\frac{5}{8}=\frac{5}{24}$; $P(\text{II} \cap \text{merah})=\frac{4}{6}\times\frac{2}{8}=\frac{1}{6}=\frac{4}{24}$. $P(\text{merah})=\frac{9}{24}=\frac{3}{8}$. $P(\text{I}|\text{merah})=\frac{5/24}{9/24}=\frac{5}{9}$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12-b04-b-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: peluang bersyarat bertingkat tiga pengambilan*

Sebuah kotak berisi 5 bola merah dan 4 bola putih. Tiga bola diambil satu per satu secara acak tanpa pengembalian. Jika diketahui bola ketiga berwarna putih, peluang bola pertama dan kedua keduanya merah adalah ....

- A. $\frac{5}{18}$  
  <sub>Salah: hanya menghitung dua pengambilan pertama dan mengabaikan syarat bola ketiga putih</sub>
- B. $\frac{10}{63}$  
  <sub>Salah: hanya menghitung peluang urutan merah, merah, putih tanpa membagi dengan peluang syarat</sub>
- C. $\frac{4}{9}$  
  <sub>Salah: memakai peluang syarat (bola ketiga putih) sebagai jawaban</sub>
- **D. $\frac{5}{14}$** ✅  
  <sub>Benar: $P(\text{MMP})=\frac{5}{9}\times\frac{4}{8}\times\frac{4}{7}=\frac{10}{63}$ dan $P(\text{bola ketiga putih})=\frac{4}{9}$, sehingga $\frac{10/63}{4/9}=\frac{5}{14}$</sub>

**Pembahasan:** Peluang bola ketiga putih $=\frac{4}{9}$ (tiap posisi setara). $P(\text{MMP})=\frac{5}{9}\times\frac{4}{8}\times\frac{4}{7}=\frac{80}{504}=\frac{10}{63}$. $P(\text{MM}|\text{P ketiga})=\frac{10}{63}\div\frac{4}{9}=\frac{10}{63}\times\frac{9}{4}=\frac{5}{14}$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12-b04-b-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: peluang bersyarat dua dadu*

Dua dadu setimbang dilempar bersamaan. Jika diketahui paling sedikit satu dadu menunjukkan mata 6, peluang jumlah kedua mata dadu paling sedikit 10 adalah ....

- A. $\frac{5}{36}$  
  <sub>Salah: membagi dengan seluruh ruang sampel 36, bukan dengan 11 pasangan syarat</sub>
- B. $\frac{11}{36}$  
  <sub>Salah: memakai peluang syarat (paling sedikit satu mata 6) sebagai jawaban</sub>
- **C. $\frac{5}{11}$** ✅  
  <sub>Benar: ruang sampel menyempit ke 11 pasangan yang memuat 6; di antaranya (4,6),(6,4),(5,6),(6,5),(6,6) berjumlah $\geq 10$, sehingga $\frac{5}{11}$</sub>
- D. $\frac{1}{6}$  
  <sub>Salah: memakai peluang jumlah paling sedikit 10 tanpa syarat ($\frac{6}{36}$)</sub>

**Pembahasan:** Syarat: paling sedikit satu 6, ada $36-25=11$ pasangan. Yang berjumlah $\geq 10$: (4,6), (6,4), (5,6), (6,5), (6,6) = 5 pasangan. $P=\frac{5}{11}$. Bandingkan $\frac{6}{36}$ tanpa syarat, karena pasangan (5,5) tidak memuat 6.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12-b04-b-hard-bt01-014
*orisinal | C6 | 5 langkah | jenis: rancang skema permainan adil*

Sebuah kantong berisi 3 bola merah dan $n$ bola putih, dengan $n$ bilangan asli. Dua bola diambil sekaligus secara acak. Ani menang jika kedua bola sewarna dan Budi menang jika berbeda warna. Permainan adil bila peluang menang keduanya sama. Nilai $n$ terbesar yang membuat permainan adil adalah ....

- A. $1$  
  <sub>Salah: akar yang lebih kecil dari persamaan; soal meminta $n$ terbesar</sub>
- B. $7$  
  <sub>Salah: mengambil jumlah kedua akar persamaan sebagai jawaban</sub>
- C. $3$  
  <sub>Salah: mengira permainan adil bila jumlah bola putih sama dengan jumlah bola merah</sub>
- **D. $6$** ✅  
  <sub>Benar: $\frac{C(3,2)+C(n,2)}{C(n+3,2)}=\frac{1}{2}$ menjadi $n^2-7n+6=0$ sehingga $n=1$ atau $n=6$; $n$ terbesar adalah 6</sub>

**Pembahasan:** Peluang sewarna $=\frac{3+\frac{n(n-1)}{2}}{\frac{(n+3)(n+2)}{2}}=\frac{6+n^2-n}{(n+3)(n+2)}=\frac{1}{2}$, sehingga $12+2n^2-2n=n^2+5n+6$ atau $n^2-7n+6=0$, yaitu $(n-1)(n-6)=0$. Cek $n=6$: $\frac{3+15}{36}=\frac{1}{2}$. $n$ terbesar $=6$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12-b04-b-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: bandingkan dua skema undian*

Dari 10 kartu undian terdapat 4 kartu hadiah. Peserta mengambil dua kartu secara acak satu per satu dan menang bila keduanya kartu hadiah. Pada skema X kartu pertama dikembalikan sebelum pengambilan kedua, sedangkan pada skema Y tidak dikembalikan. Pernyataan yang benar adalah ....

- A. peluang menang kedua skema sama besar  
  <sub>Salah: mengira pengembalian tidak mempengaruhi peluang pengambilan kedua</sub>
- B. peluang menang skema X lebih besar daripada skema Y dengan selisih $\frac{1}{25}$  
  <sub>Salah: menghitung skema Y sebagai $\frac{4}{10}\times\frac{3}{10}$ (penyebut kedua tidak dikurangi)</sub>
- C. peluang menang skema Y lebih besar daripada skema X dengan selisih $\frac{2}{75}$  
  <sub>Salah: membalik arah: tanpa pengembalian kartu hadiah berkurang sehingga peluang justru mengecil</sub>
- **D. peluang menang skema X lebih besar daripada skema Y dengan selisih $\frac{2}{75}$** ✅  
  <sub>Benar: X: $\frac{4}{10}\times\frac{4}{10}=\frac{4}{25}$; Y: $\frac{4}{10}\times\frac{3}{9}=\frac{2}{15}$; selisih $\frac{12-10}{75}=\frac{2}{75}$</sub>

**Pembahasan:** Skema X (saling bebas): $\frac{4}{25}=\frac{12}{75}$. Skema Y (tergantung pengambilan pertama): $\frac{4}{10}\times\frac{3}{9}=\frac{2}{15}=\frac{10}{75}$. X lebih besar dengan selisih $\frac{2}{75}$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12-b04-b-hard-bt01-016
*orisinal | C6 | 6 langkah | jenis: bandingkan dua skema kelulusan tiga tes*

Peluang seorang peserta lulus tes 1, tes 2, dan tes 3 berturut-turut adalah $\frac{1}{2}$, $\frac{2}{3}$, dan $\frac{3}{4}$, dan hasil ketiga tes saling bebas. Aturan P: peserta diterima jika lulus paling sedikit dua dari tiga tes. Aturan Q: peserta diterima jika lulus tes 1 dan lulus paling sedikit satu dari tes 2 atau tes 3. Pernyataan yang benar adalah ....

- A. peluang diterima aturan Q lebih besar daripada aturan P dengan selisih $\frac{1}{4}$  
  <sub>Salah: arah terbalik: aturan P lebih longgar sehingga peluangnya lebih besar</sub>
- **B. peluang diterima aturan P lebih besar daripada aturan Q dengan selisih $\frac{1}{4}$** ✅  
  <sub>Benar: $P=\frac{17}{24}$ dan $Q=\frac{1}{2}\times\left(1-\frac{1}{3}\times\frac{1}{4}\right)=\frac{11}{24}$; selisih $\frac{6}{24}=\frac{1}{4}$</sub>
- C. peluang diterima kedua aturan sama besar  
  <sub>Salah: hanya menghitung kasus tepat dua tes lulus pada aturan P ($\frac{11}{24}$) sehingga tampak sama dengan Q</sub>
- D. peluang diterima aturan P lebih besar daripada aturan Q dengan selisih $\frac{1}{8}$  
  <sub>Salah: aturan Q dihitung $\frac{1}{3}+\frac{1}{4}=\frac{7}{12}$ (tes 3 tidak dikalikan peluang lulus tes 1)</sub>

**Pembahasan:** Aturan P: tepat dua lulus $\frac{11}{24}$ ditambah ketiganya lulus $\frac{1}{4}$ $=\frac{17}{24}$. Aturan Q: $P(\text{tes 1})\times(1-P(\text{tes 2 gagal})P(\text{tes 3 gagal}))=\frac{1}{2}\times\frac{11}{12}=\frac{11}{24}$. Selisih $\frac{6}{24}=\frac{1}{4}$.
**Acuan:** siswa — siswa hal.172

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12-b04-b-hard-bt01-017
*orisinal | C6 | 4 langkah | jenis: rancang banyak percobaan frekuensi harapan*

Dua dadu setimbang dilempar bersamaan sebanyak $n$ kali. Agar frekuensi harapan munculnya jumlah mata dadu 7 atau 11 paling sedikit 100, banyak lemparan $n$ paling sedikit adalah ....

- A. $600$  
  <sub>Salah: hanya menghitung jumlah 7 ($\frac{6}{36}$)</sub>
- B. $1.800$  
  <sub>Salah: hanya menghitung jumlah 11 ($\frac{2}{36}$)</sub>
- C. $400$  
  <sub>Salah: memakai peluang $\frac{1}{4}$ untuk kejadian 7 atau 11</sub>
- **D. $450$** ✅  
  <sub>Benar: $P=\frac{6}{36}+\frac{2}{36}=\frac{2}{9}$; $\frac{2}{9}n\geq 100$ sehingga $n\geq 450$</sub>

**Pembahasan:** Jumlah 7: 6 pasangan, jumlah 11: 2 pasangan, saling lepas, $P=\frac{8}{36}=\frac{2}{9}$. Frekuensi harapan $\frac{2}{9}n\geq 100\Rightarrow n\geq 450$. Cek: $n=450$ memberi tepat 100, $n=449$ memberi kurang dari 100.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12-b04-b-hard-bt01-018
*orisinal | C6 | 5 langkah | jenis: rancang banyak percobaan peluang komplemen*

Sebuah dadu setimbang dilempar $n$ kali, tiap lemparan saling bebas. Banyak lemparan $n$ terkecil agar peluang muncul mata 6 paling sedikit satu kali lebih dari $0{,}9$ adalah ....

- A. $12$  
  <sub>Salah: pembulatan ke bawah: $\left(\frac{5}{6}\right)^{12}\approx 0{,}112$ masih lebih dari $0{,}1$</sub>
- **B. $13$** ✅  
  <sub>Benar: $1-\left(\frac{5}{6}\right)^n>0{,}9$ berarti $\left(\frac{5}{6}\right)^n<0{,}1$; $n=12$ memberi $0{,}112$ (belum), $n=13$ memberi $0{,}0935$ (memenuhi)</sub>
- C. $14$  
  <sub>Salah: memenuhi syarat tetapi bukan yang terkecil</sub>
- D. $6$  
  <sub>Salah: memakai $\frac{n}{6}\geq 0{,}9$ seolah peluang bertambah $\frac{1}{6}$ tiap lemparan</sub>

**Pembahasan:** Komplemen dari paling sedikit satu 6 adalah tidak ada 6 sama sekali: $\left(\frac{5}{6}\right)^n$. Perlu $\left(\frac{5}{6}\right)^n<0{,}1$. $\left(\frac{5}{6}\right)^{12}\approx 0{,}1122$ dan $\left(\frac{5}{6}\right)^{13}\approx 0{,}0935$. Jadi $n$ terkecil $=13$.
**Acuan:** siswa — siswa hal.171

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12-b04-b-hard-bt01-019
*orisinal | C5 | 4 langkah | jenis: bandingkan pengambilan berurutan dan sekaligus*

Sebuah kotak berisi 4 bola merah dan 6 bola putih. Misalkan $a$ adalah peluang pada pengambilan dua bola satu per satu tanpa pengembalian bahwa bola pertama merah dan bola kedua putih, dan $b$ adalah peluang bahwa dua bola yang diambil sekaligus terdiri atas satu merah dan satu putih. Hubungan yang benar adalah ....

- A. $b=a$  
  <sub>Salah: lupa bahwa satu merah satu putih juga dapat terjadi dengan urutan putih lalu merah</sub>
- **B. $b=2a$** ✅  
  <sub>Benar: $a=\frac{4}{10}\times\frac{6}{9}=\frac{4}{15}$ dan $b=\frac{4\times 6}{C(10,2)}=\frac{8}{15}$, sehingga $b=2a$ (dua urutan: merah-putih dan putih-merah)</sub>
- C. $b=\frac{a}{2}$  
  <sub>Salah: membalik hubungan: kejadian sekaligus mencakup dua urutan sehingga lebih besar</sub>
- D. $b=\frac{3a}{2}$  
  <sub>Salah: menghitung banyak urutan sebagai 3 padahal hanya ada 2 urutan</sub>

**Pembahasan:** $a=\frac{4}{10}\times\frac{6}{9}=\frac{24}{90}=\frac{4}{15}$. Sekaligus: $b=\frac{C(4,1)C(6,1)}{C(10,2)}=\frac{24}{45}=\frac{8}{15}$. Karena (merah, putih) dan (putih, merah) saling lepas dan sama peluangnya, $b=2a$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12-b04-b-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: syarat parameter pengambilan tanpa pengembalian*

Sebuah kantong berisi $n$ bola merah dan 4 bola putih, dengan $n$ bilangan asli. Dua bola diambil satu per satu secara acak tanpa pengembalian. Jika peluang kedua bola merah adalah $\frac{1}{3}$, nilai $n$ adalah ....

- A. $12$  
  <sub>Salah: mengambil konstanta persamaan $2n^2-10n-12=0$ sebagai nilai $n$</sub>
- B. $5$  
  <sub>Salah: memakai cara dengan pengembalian $\left(\frac{n}{n+4}\right)^2=\frac{1}{3}$ lalu membulatkan</sub>
- **C. $6$** ✅  
  <sub>Benar: $\frac{n}{n+4}\times\frac{n-1}{n+3}=\frac{1}{3}$ menjadi $n^2-5n-6=0$ sehingga $n=6$ (akar $-1$ tidak berlaku)</sub>
- D. $8$  
  <sub>Salah: salah memfaktorkan $n^2-5n-6=0$ menjadi $(n-8)(n+3)=0$</sub>

**Pembahasan:** Tanpa pengembalian: $\frac{n(n-1)}{(n+4)(n+3)}=\frac{1}{3}\Rightarrow 3n^2-3n=n^2+7n+12\Rightarrow n^2-5n-6=0\Rightarrow (n-6)(n+1)=0$. Karena $n$ bilangan asli, $n=6$. Cek: $\frac{6}{10}\times\frac{5}{9}=\frac{1}{3}$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
