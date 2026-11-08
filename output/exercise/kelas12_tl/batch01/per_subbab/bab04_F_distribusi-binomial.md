# Lembar koreksi — kelas12_tl SMA12L-B4 subbab F: Distribusi Binomial

58 soal | easy 20, medium 20, hard 18 | variasi 27, orisinal 31
> **Kapasitas kurang (hard): 18 dari kuota 20** — 10 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b04-f-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: nilai harapan binomial*

Peluang seseorang sembuh dari suatu penyakit setelah menjalani terapi adalah 0,75. Jika terdapat 60 pasien yang menjalani terapi tersebut, nilai harapan banyaknya pasien yang sembuh adalah ....

- A. 50  
  <sub>Salah: Perkiraan kasar tanpa menghitung nilai eksak $60 \times 0,75$.</sub>
- B. 15  
  <sub>Salah: Menghitung nilai harapan pasien yang gagal sembuh ($n \times q = 60 \times 0,25$).</sub>
- C. 40  
  <sub>Salah: Kesalahan perkalian dasar atau mengira $60 \times \frac{2}{3}$ alih-alih $60 \times \frac{3}{4}$.</sub>
- **D. 45** ✅  
  <sub>Benar: Menggunakan rumus nilai harapan distribusi binomial: $E(X) = n \times p = 60 \times 0,75 = 45$.</sub>

**Pembahasan:** Diketahui:
- $n = 60$
- $p = 0,75$

Nilai harapan distribusi binomial dihitung dengan rumus:
$$E(X) = n \cdot p$$
$$E(X) = 60 \times 0,75 = 45$$

Jadi, nilai harapan banyaknya pasien yang sembuh adalah 45.
**Acuan:** siswa — siswa hal.279 Ayo Mencoba 4.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b04-f-easy-bt01-002
*variasi (konteks) | C2 | 2 langkah | jenis: peluang binomial tunggal*

Peluang sebuah bibit tanaman berhasil tumbuh adalah 0,8. Jika seorang petani menanam 4 bibit secara terpisah dan saling bebas, peluang tepat 1 bibit yang tumbuh adalah ....

- A. 0,0320  
  <sub>Salah: Kesalahan hitung nilai eksponen $(0,2)^3$ dianggap $0,01$ sehingga $4 \times 0,8 \times 0,01 = 0,0320$.</sub>
- B. 0,0064  
  <sub>Salah: Lupa mengalikan dengan koefisien kombinasi $\binom{4}{1}$, hanya menghitung $(0,8)^1 \times (0,2)^3 = 0,0064$.</sub>
- **C. 0,0256** ✅  
  <sub>Benar: $P(X = 1) = \binom{4}{1} \times (0,8)^1 \times (0,2)^3 = 4 \times 0,8 \times 0,008 = 0,0256$.</sub>
- D. 0,1024  
  <sub>Salah: Tertukar pangkat antara $p$ dan $q$, menghitung $\binom{4}{1} \times (0,8)^3 \times (0,2)^1 = 4 \times 0,512 \times 0,2 = 0,4096$ lalu salah desimal atau mengalikan $4 \times 0,8 \times 0,2^2$.</sub>

**Pembahasan:** Diketahui:
- $n = 4$
- $p = 0,8$
- $q = 1 - 0,8 = 0,2$
- $x = 1$

Peluang tepat 1 bibit tumbuh:
$$P(X = 1) = \binom{4}{1} p^1 q^{4-1}$$
$$P(X = 1) = 4 \times (0,8)^1 \times (0,2)^3$$
$$P(X = 1) = 4 \times 0,8 \times 0,008 = 0,0256$$

Jadi, peluang tepat 1 bibit yang tumbuh adalah 0,0256.
**Acuan:** pretest — kelas12_tl-b04-p0280-latihan-soal-distribusi-binomial-5b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b04-f-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: peluang pelemparan koin*

Sekeping uang logam seimbang dilemparkan sebanyak 6 kali. Peluang untuk mendapatkan tepat 4 sisi gambar adalah ....

- A. $\frac{20}{64}$  
  <sub>Salah: Menghitung nilai kombinasi untuk $x = 3$, yaitu $\binom{6}{3} = 20$.</sub>
- B. $\frac{6}{64}$  
  <sub>Salah: Menggunakan nilai kombinasi $\binom{6}{1}$ alih-alih $\binom{6}{4}$.</sub>
- **C. $\frac{15}{64}$** ✅  
  <sub>Benar: $P(X = 4) = \binom{6}{4} \left(\frac{1}{2}\right)^4 \left(\frac{1}{2}\right)^2 = 15 \times \frac{1}{64} = \frac{15}{64}$.</sub>
- D. $\frac{15}{32}$  
  <sub>Salah: Salah menghitung pembagi $2^6 = 64$ menjadi $32$.</sub>

**Pembahasan:** Diketahui:
- $n = 6$
- $x = 4$
- $p = \frac{1}{2}$
- $q = \frac{1}{2}$

Perhitungan peluang binomial:
$$P(X = 4) = \binom{6}{4} \left(\frac{1}{2}\right)^4 \left(\frac{1}{2}\right)^{6-4}$$
$$\binom{6}{4} = \frac{6!}{4!2!} = \frac{6 \times 5}{2 \times 1} = 15$$
$$P(X = 4) = 15 \times \left(\frac{1}{2}\right)^6 = 15 \times \frac{1}{64} = \frac{15}{64}$$

Jadi, peluangnya adalah $\frac{15}{64}$.
**Acuan:** siswa — siswa hal.274 Ayo Mencoba 4.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b04-f-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: rumus nilai harapan*

Suatu variabel acak $X$ berdistribusi binomial dengan banyaknya percobaan $n = 50$ dan peluang sukses pada setiap percobaan $p = 0,3$. Nilai harapan $E(X)$ dari variabel acak tersebut adalah ....

- A. 35  
  <sub>Salah: Menghitung $n \cdot q = 50 \times 0,7 = 35$.</sub>
- **B. 15** ✅  
  <sub>Benar: $E(X) = n \cdot p = 50 \times 0,3 = 15$.</sub>
- C. 5  
  <sub>Salah: Kesalahan desimal saat mengalikan $50 \times 0,3$ dianggap 5.</sub>
- D. 10,5  
  <sub>Salah: Menghitung varians $n \cdot p \cdot q = 50 \times 0,3 \times 0,7 = 10,5$ alih-alih nilai harapan.</sub>

**Pembahasan:** Berdasarkan rumus nilai harapan distribusi binomial:
$$E(X) = n \cdot p$$
Diketahui $n = 50$ dan $p = 0,3$, maka:
$$E(X) = 50 \times 0,3 = 15$$

Jadi, nilai harapan $E(X)$ adalah 15.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b04-f-easy-bt01-005
*orisinal | C1 | 1 langkah | jenis: konsep parameter binomial*

Dalam suatu percobaan binomial, peluang terjadinya kejadian berhasil dinyatakan dengan $p = \frac{1}{4}$. Peluang kejadian gagal ($q$) dalam percobaan tersebut bernilai ....

- A. $\frac{1}{4}$  
  <sub>Salah: Menyamakan peluang gagal dengan peluang berhasil.</sub>
- **B. $\frac{3}{4}$** ✅  
  <sub>Benar: $q = 1 - p = 1 - \frac{1}{4} = \frac{3}{4}$.</sub>
- C. $-\frac{1}{4}$  
  <sub>Salah: Salah memahami pengurangan atau lupa menambahkan 1 pada rumus $1 - p$.</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: Mengira setiap percobaan Bernoulli selalu memiliki peluang gagal setara dengan koin ($0,5$).</sub>

**Pembahasan:** Pada percobaan binomial, hanya ada dua kemungkinan hasil: sukses dan gagal. Hubungan antara peluang sukses ($p$) dan peluang gagal ($q$) adalah:
$$q = 1 - p$$
$$q = 1 - \frac{1}{4} = \frac{3}{4}$$

Jadi, peluang kejadian gagal adalah $\frac{3}{4}$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b04-f-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: peluang binomial dadu*

Sebuah dadu seimbang bermata enam dilemparkan sebanyak 4 kali. Peluang mendapatkan sisi mata dadu 6 tepat sebanyak 2 kali adalah ....

- A. $\frac{5}{216}$  
  <sub>Salah: Lupa mengalikan dengan faktor kombinasi $\binom{4}{2} = 6$.</sub>
- B. $\frac{25}{1296}$  
  <sub>Salah: Lupa mengalikan dengan kombinasi dan salah penyederhanaan penyebut.</sub>
- **C. $\frac{25}{216}$** ✅  
  <sub>Benar: $P(X = 2) = \binom{4}{2} \left(\frac{1}{6}\right)^2 \left(\frac{5}{6}\right)^{4-2} = 6 \times \frac{1}{36} \times \frac{25}{36} = \frac{25}{216}$.</sub>
- D. $\frac{5}{36}$  
  <sub>Salah: Keliru menghitung kuadrat dari peluang gagal $(5/6)^2$ menjadi $5/6$.</sub>

**Pembahasan:** Diketahui:
- Peluang sukses (muncul mata dadu 6): $p = \frac{1}{6}$
- Peluang gagal: $q = 1 - \frac{1}{6} = \frac{5}{6}$
- Banyak percobaan: $n = 4$
- Banyak sukses yang diharapkan: $x = 2$

Menggunakan rumus peluang binomial:
$$P(X = x) = \binom{n}{x} p^x q^{n-x}$$
$$P(X = 2) = \binom{4}{2} \left(\frac{1}{6}\right)^2 \left(\frac{5}{6}\right)^2$$
$$\binom{4}{2} = \frac{4 \times 3}{2 \times 1} = 6$$
$$P(X = 2) = 6 \times \frac{1}{36} \times \frac{25}{36} = \frac{1}{6} \times \frac{25}{36} = \frac{25}{216}$$

Jadi, peluangnya adalah $\frac{25}{216}$.
**Acuan:** siswa — siswa hal.273 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b04-f-easy-bt01-007
*variasi (konteks) | C2 | 2 langkah | jenis: peluang binomial tembakan*

Peluang seorang penembak mengenai sasaran tepat adalah 0,6 pada setiap tembakan. Jika ia melepaskan 4 tembakan secara bebas, peluang tepat 3 tembakan mengenai sasaran adalah ....

- **A. 0,3456** ✅  
  <sub>Benar: $P(X = 3) = \binom{4}{3} (0,6)^3 (0,4)^1 = 4 \times 0,216 \times 0,4 = 0,3456$.</sub>
- B. 0,5184  
  <sub>Salah: Tertukar nilai peluang sukses dan peluang gagal, menghitung $\binom{4}{3} (0,4)^3 (0,6)^1$.</sub>
- C. 0,0864  
  <sub>Salah: Lupa mengalikan dengan kombinasi $\binom{4}{3} = 4$, hanya menghitung $(0,6)^3 \times 0,4$.</sub>
- D. 0,2304  
  <sub>Salah: Salah menghitung pangkat, mengalikan $(0,6)^2 \times (0,4)^2 \times 4$.</sub>

**Pembahasan:** Diketahui:
- $n = 4$
- $x = 3$
- $p = 0,6$
- $q = 1 - 0,6 = 0,4$

Peluang binomial:
$$P(X = 3) = \binom{4}{3} (0,6)^3 (0,4)^{4-3}$$
$$\binom{4}{3} = 4$$
$$P(X = 3) = 4 \times 0,216 \times 0,4 = 0,3456$$

Jadi, peluang tepat 3 tembakan mengenai sasaran adalah 0,3456.
**Acuan:** siswa — siswa hal.275 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b04-f-easy-bt01-008
*variasi (konteks) | C2 | 1 langkah | jenis: nilai harapan produksi*

Peluang sebuah produk elektronik yang dihasilkan sebuah pabrik lolos uji kendali mutu adalah 0,95. Jika diambil sampel acak sebanyak 300 produk, nilai harapan banyaknya produk yang lolos uji mutu adalah ....

- **A. 285** ✅  
  <sub>Benar: $E(X) = n \cdot p = 300 \times 0,95 = 285$.</sub>
- B. 295  
  <sub>Salah: Melakukan pengurangan $300 - (100 \times 0,05)$ bukan perkalian langsung.</sub>
- C. 15  
  <sub>Salah: Menghitung nilai harapan produk yang tidak lolos mutu ($300 \times 0,05$).</sub>
- D. 270  
  <sub>Salah: Keliru mengalikan $300 \times 0,90$.</sub>

**Pembahasan:** Diketahui:
- Banyaknya percobaan ($n$) = 300
- Peluang keberhasilan ($p$) = 0,95

Rumus nilai harapan distribusi binomial:
$$E(X) = n \cdot p$$
$$E(X) = 300 \times 0,95 = 285$$

Jadi, nilai harapan produk yang lolos uji mutu adalah 285.
**Acuan:** siswa — siswa hal.279 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b04-f-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: karakteristik distribusi binomial*

Salah satu sifat utama dari percobaan yang berdistribusi binomial (proses Bernoulli) adalah ....

- A. hasil pada percobaan sebelumnya memengaruhi peluang percobaan berikutnya  
  <sub>Salah: Bertentangan dengan sifat saling bebas (independen).</sub>
- **B. peluang keberhasilan pada setiap pengulangan percobaan bernilai tetap** ✅  
  <sub>Benar: Berdasarkan definisi proses Bernoulli, percobaan bersifat saling bebas dan peluang sukses ($p$) konstan pada setiap pengulangan.</sub>
- C. peluang kejadian gagal selalu bernilai sama dengan peluang kejadian berhasil  
  <sub>Salah: Peluang sukses dan gagal tidak harus sama besar ($p$ tidak harus bernilai 0,5).</sub>
- D. setiap percobaan memiliki lebih dari dua kemungkinan hasil yang saling bebas  
  <sub>Salah: Percobaan binomial hanya memiliki tepat dua kemungkinan hasil (sukses dan gagal).</sub>

**Pembahasan:** Karakteristik proses Bernoulli pada distribusi binomial meliputi:
1. Percobaan diulang sebanyak $n$ kali.
2. Setiap percobaan hanya menghasilkan dua kemungkinan: berhasil (sukses) atau gagal.
3. Percobaan bersifat saling bebas (independen).
4. Peluang keberhasilan ($p$) selalu tetap (konstan) pada setiap pengulangan percobaan.

Dengan demikian, pilihan yang tepat adalah peluang keberhasilan pada setiap pengulangan percobaan bernilai tetap.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b04-f-easy-bt01-010
*orisinal | C2 | 2 langkah | jenis: nilai harapan pelemparan dadu*

Sebuah dadu seimbang bermata enam dilemparkan sebanyak 36 kali. Nilai harapan munculnya mata dadu kelipatan 3 adalah ....

- A. 24  
  <sub>Salah: Menghitung nilai harapan kejadian bukan kelipatan 3 ($36 \times 2/3 = 24$).</sub>
- **B. 12** ✅  
  <sub>Benar: $p = \frac{2}{6} = \frac{1}{3}$. $E(X) = n \cdot p = 36 \times \frac{1}{3} = 12$.</sub>
- C. 6  
  <sub>Salah: Hanya menghitung peluang satu mata dadu saja ($p = 1/6$, sehingga $36 \times 1/6 = 6$).</sub>
- D. 18  
  <sub>Salah: Keliru menganggap mata dadu kelipatan 3 memiliki peluang $1/2$ ($36 \times 1/2 = 18$).</sub>

**Pembahasan:** Mata dadu kelipatan 3 pada dadu bermata enam adalah $\{3, 6\}$, berjumlah 2 dari 6 sisi.

1. Peluang sukses muncul mata dadu kelipatan 3:
$$p = \frac{2}{6} = \frac{1}{3}$$

2. Nilai harapan dengan $n = 36$ kali pelemparan:
$$E(X) = n \cdot p = 36 \times \frac{1}{3} = 12$$

Jadi, nilai harapan munculnya mata dadu kelipatan 3 adalah 12.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b04-f-easy-bt01-011
*variasi (angka) | C2 | 1 langkah | jenis: nilai harapan pelemparan koin*

Sekeping uang logam seimbang dilemparkan sebanyak 18 kali. Nilai harapan untuk mendapatkan sisi angka adalah ....

- A. 6  
  <sub>Salah: Membagi jumlah lemparan dengan 3 bukan dikali peluang 1/2.</sub>
- B. 12  
  <sub>Salah: Mengalikan dengan 2/3 bukan 1/2.</sub>
- C. 18  
  <sub>Salah: Menganggap nilai harapan sama dengan jumlah percobaan n.</sub>
- **D. 9** ✅  
  <sub>Benar: $E(X) = n \times p = 18 \times \frac{1}{2} = 9$.</sub>

**Pembahasan:** Pada pelemparan uang logam seimbang, peluang munculnya sisi angka pada setiap pelemparan adalah $p = \frac{1}{2}$. Banyaknya pelemparan adalah $n = 18$.
Nilai harapan variabel acak binomial dirumuskan dengan:
$$E(X) = n \cdot p = 18 \cdot \frac{1}{2} = 9$$
Jadi, nilai harapan munculnya sisi angka adalah 9.
**Acuan:** siswa — siswa hal.278 Ayo Mencoba 4.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b04-f-easy-bt01-012
*variasi (konteks) | C2 | 2 langkah | jenis: peluang binomial cacat produk*

Peluang sebuah lampu LED rusak dalam suatu proses produksi adalah $0,1$. Jika diambil sampel $3$ lampu LED secara acak dan saling bebas, peluang diperoleh tepat $1$ lampu LED yang rusak adalah ....

- A. 0,027  
  <sub>Salah: Menggunakan p^3 bukannya p^1 * q^2.</sub>
- B. 0,081  
  <sub>Salah: Lupa mengalikan dengan koefisien kombinasi C(3, 1).</sub>
- C. 0,270  
  <sub>Salah: Salah menghitung pangkat peluang gagal menjadi 3 x 0,1 x 0,9.</sub>
- **D. 0,243** ✅  
  <sub>Benar: $P(X = 1) = \binom{3}{1} (0,1)^1 (0,9)^2 = 3 \times 0,1 \times 0,81 = 0,243$.</sub>

**Pembahasan:** Diketahui:
- $n = 3$
- $x = 1$
- $p = 0,1$ (peluang rusak)
- $q = 1 - p = 1 - 0,1 = 0,9$

Rumus distribusi binomial:
$$P(X = x) = \binom{n}{x} p^x q^{n-x}$$
$$P(X = 1) = \binom{3}{1} (0,1)^1 (0,9)^{3-1} = 3 \times 0,1 \times 0,81 = 0,243$$
Jadi, peluang tepat 1 lampu rusak adalah 0,243.
**Acuan:** siswa — siswa hal.280 Latihan Soal Distribusi Binomial

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b04-f-easy-bt01-013
*variasi (konteks) | C2 | 2 langkah | jenis: peluang binomial pemanah*

Peluang seorang pemanah mengenai sasaran tepat di tengah adalah $0,8$ pada setiap tembakan. Jika pemanah tersebut melepaskan $3$ tembakan secara bebas, peluang ia mengenai sasaran tepat di tengah tepat $1$ kali adalah ....

- **A. 0,096** ✅  
  <sub>Benar: $P(X = 1) = \binom{3}{1} (0,8)^1 (0,2)^2 = 3 \times 0,8 \times 0,04 = 0,096$.</sub>
- B. 0,384  
  <sub>Salah: Tertukar antara pangkat sukses dan pangkat gagal C(3,1) * (0,8)^2 * (0,2)^1.</sub>
- C. 0,032  
  <sub>Salah: Lupa mengalikan dengan koefisien kombinasi C(3, 1) = 3.</sub>
- D. 0,064  
  <sub>Salah: Hanya menghitung q^3 yaitu (0,2)^3.</sub>

**Pembahasan:** Diketahui:
- $n = 3$
- $x = 1$
- $p = 0,8$
- $q = 1 - 0,8 = 0,2$

Peluang tepat 1 kali berhasil:
$$P(X = 1) = \binom{3}{1} (0,8)^1 (0,2)^2 = 3 \times 0,8 \times 0,04 = 0,096$$
Jadi, peluangnya adalah 0,096.
**Acuan:** pretest — kelas12_tl-b04-p0280-latihan-soal-distribusi-binomial-5b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b04-f-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: perhitungan parameter peluang*

Suatu variabel acak $X$ berdistribusi binomial memiliki nilai harapan $E(X) = 24$. Jika percobaan dilakukan sebanyak $n = 40$ kali, peluang keberhasilan $p$ pada setiap percobaan adalah ....

- A. 0,75  
  <sub>Salah: Salah membagi pecahan.</sub>
- B. 0,16  
  <sub>Salah: Mengurangkan n - E(X) lalu dibagi 100.</sub>
- **C. 0,6** ✅  
  <sub>Benar: $p = \frac{E(X)}{n} = \frac{24}{40} = 0,6$.</sub>
- D. 0,4  
  <sub>Salah: Menghitung peluang kegagalan q = 1 - p bukannya p.</sub>

**Pembahasan:** Rumus nilai harapan distribusi binomial:
$$E(X) = n \cdot p$$
Maka:
$$24 = 40 \cdot p \implies p = \frac{24}{40} = 0,6$$
Jadi, peluang keberhasilan pada setiap percobaan adalah 0,6.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b04-f-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: konsep peluang proses Bernoulli*

Dalam suatu percobaan binomial (proses Bernoulli) yang dilakukan sebanyak $n$ kali secara saling bebas, peluang terjadinya keberhasilan pada percobaan ke-1 adalah $p$. Peluang terjadinya keberhasilan pada percobaan ke-5 adalah ....

- A. $\frac{p}{5}$  
  <sub>Salah: Mengira peluang terbagi oleh nomor urutan percobaan.</sub>
- **B. $p$** ✅  
  <sub>Benar: Peluang keberhasilan pada setiap pengulangan percobaan Bernoulli selalu tetap sama yaitu p.</sub>
- C. $p^5$  
  <sub>Salah: Mengira peluang dipangkatkan urutan percobaan.</sub>
- D. $5p$  
  <sub>Salah: Mengira peluang dikalikan dengan indeks urutan percobaan.</sub>

**Pembahasan:** Salah satu sifat utama dari proses Bernoulli pada distribusi binomial adalah bahwa setiap pengulangan percobaan bersifat bebas dan peluang keberhasilan ($p$) pada setiap pengulangan tetap sama.
Oleh karena itu, pada percobaan ke-5 peluang keberhasilannya tetap sebesar $p$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b04-f-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: peluang muncul gambar*

Tentukan peluang untuk mendapatkan tepat 1 sisi gambar dalam 5 kali pelemparan sekeping uang logam seimbang.

- A. $\frac{10}{32}$  
  <sub>Salah: Menggunakan kombinasi $\binom{5}{2}$ bukan $\binom{5}{1}$.</sub>
- B. $\frac{1}{5}$  
  <sub>Salah: Membuat rasio sederhana 1 kejadian dari 5 pelemparan.</sub>
- C. $\frac{1}{32}$  
  <sub>Salah: Lupa mengalikan dengan koefisien kombinasi $\binom{5}{1}$.</sub>
- **D. $\frac{5}{32}$** ✅  
  <sub>Benar: $b(1; 5, 0{,}5) = \binom{5}{1} \left(\frac{1}{2}\right)^1 \left(\frac{1}{2}\right)^4 = 5 \times \frac{1}{32} = \frac{5}{32}$.</sub>

**Pembahasan:** Pada sekeping uang logam seimbang, peluang sisi gambar adalah $p = \frac{1}{2}$ dan $q = \frac{1}{2}$. Banyak pelemparan $n = 5$ dan sukses $x = 1$.
$$P(X = 1) = \binom{5}{1} \left(\frac{1}{2}\right)^1 \left(\frac{1}{2}\right)^{5-1} = 5 \cdot \left(\frac{1}{2}\right)^5 = \frac{5}{32}$$
Jadi, peluang mendapatkan tepat 1 sisi gambar adalah $\frac{5}{32}$.
**Acuan:** siswa — siswa hal.274 Ayo Mencoba 4.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b04-f-easy-bt01-017
*variasi (konteks) | C2 | 2 langkah | jenis: peluang kejadian sukses*

Peluang sebuah paket sampai tepat waktu adalah $0,8$. Jika seorang kurir mengantar $3$ paket yang proses pengirimannya saling bebas, peluang tepat $2$ paket sampai tepat waktu adalah ....

- A. 0,512  
  <sub>Salah: Menghitung peluang ketiga-tiganya tepat waktu $(0{,}8)^3 = 0{,}512$.</sub>
- B. 0,128  
  <sub>Salah: Lupa mengalikan dengan kombinasi $\binom{3}{2} = 3$ sehingga hanya $(0{,}8)^2 (0{,}2) = 0{,}128$.</sub>
- **C. 0,384** ✅  
  <sub>Benar: $P(X = 2) = \binom{3}{2} (0{,}8)^2 (0{,}2)^1 = 3 \times 0{,}64 \times 0{,}2 = 0{,}384$.</sub>
- D. 0,480  
  <sub>Salah: Salah menghitung $(0{,}8)^2 = 0{,}8 \times 2 = 1{,}6$ lalu dikalikan nilai lain.</sub>

**Pembahasan:** Diketahui $n = 3$, $p = 0{,}8$, $q = 1 - 0{,}8 = 0{,}2$, dan $x = 2$.
$$P(X = 2) = \binom{3}{2} (0{,}8)^2 (0{,}2)^{3-2} = 3 \cdot 0{,}64 \cdot 0{,}2 = 0{,}384$$
Jadi, peluang tepat 2 paket sampai tepat waktu adalah 0,384.
**Acuan:** siswa — siswa hal.280 Latihan Soal Distribusi Binomial

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b04-f-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: formulasi fungsi binomial*

Jika suatu variabel acak binomial $X$ menyatakan banyaknya keberhasilan dalam $n$ percobaan saling bebas dengan peluang sukses $p$ dan peluang gagal $q = 1 - p$, bentuk fungsi distribusi peluang binomial $b(x; n, p)$ untuk $x$ keberhasilan adalah ....

- A. $n \cdot p^x q^{n-x}$  
  <sub>Salah: Mengganti faktor kombinasi $\binom{n}{x}$ dengan perkalian langsung $n$.</sub>
- B. $\binom{n}{x} p^{n-x} q^x$  
  <sub>Salah: Pangkat peluang sukses $p$ dan peluang gagal $q$ saling tertukar.</sub>
- C. $\binom{n}{x} (p \cdot q)^{n-x}$  
  <sub>Salah: Mengalikan peluang $p$ dan $q$ di dalam satu pangkat bersama.</sub>
- **D. $\binom{n}{x} p^x q^{n-x}$** ✅  
  <sub>Benar: Sesuai Definisi 4.6 pada buku siswa, $b(x; n, p) = \binom{n}{x} p^x q^{n-x}$.</sub>

**Pembahasan:** Berdasarkan definisi fungsi distribusi binomial, jika $X$ menyatakan banyaknya sukses dalam $n$ percobaan bebas dengan peluang sukses $p$ dan gagal $q = 1 - p$, fungsi peluangnya adalah:
$$b(x; n, p) = \binom{n}{x} p^x q^{n-x}, \quad \text{untuk } x = 0, 1, 2, \dots, n$$
Jadi, bentuk yang benar adalah $\binom{n}{x} p^x q^{n-x}$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b04-f-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: penentuan ukuran sampel*

Suatu variabel acak binomial $X$ memiliki nilai harapan $E(X) = 20$. Jika peluang terjadinya keberhasilan pada setiap percobaan adalah $p = 0{,}4$, banyak percobaan $n$ yang dilakukan adalah ....

- **A. 50** ✅  
  <sub>Benar: $n = \frac{E(X)}{p} = \frac{20}{0{,}4} = 50$.</sub>
- B. 8  
  <sub>Salah: Salah melakukan operasi dengan mengalikan $E(X) \times p = 20 \times 0{,}4 = 8$.</sub>
- C. 80  
  <sub>Salah: Keliru membagi 20 dengan kuadrat peluang atau salah meletakkan tanda koma desimal.</sub>
- D. 40  
  <sub>Salah: Membagi 20 dengan 0,5 bukannya 0,4.</sub>

**Pembahasan:** Rumus nilai harapan untuk distribusi binomial adalah:
$$E(X) = n \cdot p$$
Diketahui $E(X) = 20$ dan $p = 0{,}4$. Maka banyak percobaan $n$ adalah:
$$n = \frac{E(X)}{p} = \frac{20}{0{,}4} = 50$$
Jadi, banyak percobaan yang dilakukan adalah 50.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b04-f-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: nilai harapan koin*

Berapa nilai harapan untuk mendapatkan 5 sisi angka dalam 10 kali pelemparan sekeping uang logam seimbang?

- **A. 5** ✅  
  <sub>Benar: Peluang muncul sisi angka pada sekeping uang logam seimbang adalah $p = \frac{1}{2}$. Nilai harapan dihitung dengan rumus $E(X) = n \cdot p = 10 \cdot \frac{1}{2} = 5$.</sub>
- B. 0,5  
  <sub>Salah: Siswa hanya menuliskan peluang sukses ($p$) per lemparan tanpa mengalikannya dengan banyak percobaan.</sub>
- C. 10  
  <sub>Salah: Siswa menganggap nilai harapan sama dengan total banyaknya percobaan ($n$).</sub>
- D. 2,5  
  <sub>Salah: Siswa keliru mengalikan $n$ dengan kuadrat peluang ($n \cdot p^2 = 10 \cdot 0,25$).</sub>

**Pembahasan:** Diketahui:
- Peluang muncul sisi angka pada uang logam seimbang: $p = \frac{1}{2}$
- Banyaknya lemparan: $n = 10$

Nilai harapan variabel acak binomial ditentukan dengan rumus:
$$E(X) = n \cdot p$$
$$E(X) = 10 \cdot \frac{1}{2} = 5$$

Jadi, nilai harapan untuk mendapatkan sisi angka adalah 5.
**Acuan:** siswa — siswa hal.278 Ayo Mencoba 4.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b04-f-medium-bt01-001
*variasi (angka) | C3 | 2 langkah | jenis: peluang kumulatif binomial*

Peluang seorang siswa menyelesaikan studi pada sebuah sekolah kejuruan adalah $0{,}8$. Jika dipilih sampel acak sebanyak $4$ siswa di sekolah tersebut, tentukan peluang paling sedikit satu siswa menyelesaikan studi.

- **A. $0{,}9984$** ✅  
  <sub>Benar: Peluang komplemen (tidak ada siswa yang menyelesaikan studi) adalah $P(X = 0) = (1 - 0{,}8)^4 = (0{,}2)^4 = 0{,}0016$. Maka $P(X \ge 1) = 1 - P(X = 0) = 1 - 0{,}0016 = 0{,}9984$.</sub>
- B. $0{,}9968$  
  <sub>Salah: Salah menghitung nilai $(0{,}2)^4$ menjadi $0{,}0032$ sehingga hasil pengurangannya $1 - 0{,}0032 = 0{,}9968$.</sub>
- C. $0{,}4096$  
  <sub>Salah: Hanya menghitung peluang semua siswa menyelesaikan studi, yaitu $(0{,}8)^4 = 0{,}4096$.</sub>
- D. $0{,}0016$  
  <sub>Salah: Menghitung peluang kejadian komplemen $P(X = 0)$ tanpa mengurangkannya dari $1$.</sub>

**Pembahasan:** Diketahui $n = 4$, $p = 0{,}8$, dan $q = 1 - 0{,}8 = 0{,}2$. Peluang paling sedikit satu siswa menyelesaikan studi dinyatakan sebagai $P(X \ge 1) = 1 - P(X = 0)$. Peluang tidak ada yang menyelesaikan studi adalah $P(X = 0) = \binom{4}{0} (0{,}8)^0 (0{,}2)^4 = 1 \times 1 \times 0{,}0016 = 0{,}0016$. Dengan demikian, $P(X \ge 1) = 1 - 0{,}0016 = 0{,}9984$.
**Acuan:** pretest — kelas12_tl-b04-p0280-latihan-soal-distribusi-binomial-5c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b04-f-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: peluang binomial dadu*

Sepasang dadu seimbang dilemparkan bersama-sama sebanyak $4$ kali. Peluang memperoleh jumlah mata dadu sama dengan $10$ tepat sebanyak $2$ kali pelemparan adalah ....

- A. $\frac{121}{20736}$  
  <sub>Salah: Lupa mengalikan dengan koefisien kombinasi $\binom{4}{2} = 6$.</sub>
- B. $\frac{11}{288}$  
  <sub>Salah: Salah menghitung pemangkatan peluang gagal, menganggap $q^2 = \frac{11}{144}$ alih-alih $\frac{121}{144}$.</sub>
- **C. $\frac{121}{3456}$** ✅  
  <sub>Benar: Pasangan mata dadu berjumlah $10$ adalah $(4,6), (5,5), (6,4)$, berjumlah $3$ dari $36$ titik sampel sehingga $p = \frac{1}{12}$ dan $q = \frac{11}{12}$. Peluang tepat $2$ kali adalah $\binom{4}{2} \left(\frac{1}{12}\right)^2 \left(\frac{11}{12}\right)^2 = 6 \times \frac{1}{144} \times \frac{121}{144} = \frac{121}{3456}$.</sub>
- D. $\frac{121}{1728}$  
  <sub>Salah: Menggunakan koefisien permutasi $4$ alih-alih kombinasi $\binom{4}{2} = 6$ sehingga menghasilkan $\frac{4 \times 121}{20736} = \frac{121}{5184}$, atau salah menyederhanakan pecahan.</sub>

**Pembahasan:** Jumlah mata dadu $10$ muncul pada pasangan $(4,6), (5,5), (6,4)$, sehingga ada $3$ kemungkinan dari total $36$ kemungkinan. Peluang sukses satu kali lemparan adalah $p = \frac{3}{36} = \frac{1}{12}$, dan peluang gagal $q = 1 - \frac{1}{12} = \frac{11}{12}$. Percobaan diulang sebanyak $n = 4$ kali. Peluang sukses tepat $x = 2$ kali adalah $P(X = 2) = \binom{4}{2} \left(\frac{1}{12}\right)^2 \left(\frac{11}{12}\right)^2 = 6 \times \frac{1}{144} \times \frac{121}{144} = \frac{6 \times 121}{20736} = \frac{726}{20736} = \frac{121}{3456}$.
**Acuan:** pretest — kelas12_tl-b04-p0280-latihan-soal-distribusi-binomial-6a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b04-f-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: peluang binomial kumulatif*

Seorang penjaga gawang mampu menepis tendangan penalti dengan peluang $\frac{1}{3}$. Dalam suatu sesi latihan, ia menghadapi $4$ kali tendangan penalti yang saling bebas. Peluang penjaga gawang tersebut menepis paling banyak $1$ tendangan adalah ....

- A. $\frac{16}{81}$  
  <sub>Salah: Hanya menghitung peluang menepis $0$ tendangan ($P(X = 0)$).</sub>
- B. $\frac{8}{27}$  
  <sub>Salah: Salah menjumlahkan atau lupa mengalikan kombinasi $\binom{4}{1}$ pada suku kedua sehingga didapat $\frac{16}{81} + \frac{8}{81} = \frac{24}{81} = \frac{8}{27}$.</sub>
- C. $\frac{32}{81}$  
  <sub>Salah: Hanya menghitung peluang menepis tepat $1$ tendangan ($P(X = 1)$), mengabaikan $P(X = 0)$.</sub>
- **D. $\frac{16}{27}$** ✅  
  <sub>Benar: $P(X \le 1) = P(X = 0) + P(X = 1) = \binom{4}{0}\left(\frac{1}{3}\right)^0\left(\frac{2}{3}\right)^4 + \binom{4}{1}\left(\frac{1}{3}\right)^1\left(\frac{2}{3}\right)^3 = \frac{16}{81} + \frac{32}{81} = \frac{48}{81} = \frac{16}{27}$.</sub>

**Pembahasan:** Diketahui $n = 4$, $p = \frac{1}{3}$, dan $q = 1 - \frac{1}{3} = \frac{2}{3}$. Kejadian menepis paling banyak $1$ tendangan berarti $X = 0$ atau $X = 1$. Hitung masing-masing peluang: $P(X = 0) = \binom{4}{0} \left(\frac{1}{3}\right)^0 \left(\frac{2}{3}\right)^4 = 1 \times 1 \times \frac{16}{81} = \frac{16}{81}$. $P(X = 1) = \binom{4}{1} \left(\frac{1}{3}\right)^1 \left(\frac{2}{3}\right)^3 = 4 \times \frac{1}{3} \times \frac{8}{27} = \frac{32}{81}$. Jumlahkan: $P(X \le 1) = \frac{16}{81} + \frac{32}{81} = \frac{48}{81} = \frac{16}{27}$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b04-f-medium-bt01-004
*orisinal | C4 | 3 langkah | jenis: parameter distribusi binomial*

Suatu variabel acak $X$ berdistribusi binomial dengan $n$ percobaan saling bebas dan peluang keberhasilan $p$. Diketahui nilai harapan $E(X) = 2$ dan peluang tidak memperoleh keberhasilan sama sekali adalah $P(X = 0) = \frac{1}{16}$. Jika $n$ merupakan bilangan bulat positif, nilai peluang keberhasilan $p$ adalah ....

- A. $0{,}4$  
  <sub>Salah: Menebak nilai $n = 5$ sehingga $p = \frac{2}{5} = 0{,}4$, namun $(0{,}6)^5 \ne \frac{1}{16}$.</sub>
- B. $0{,}75$  
  <sub>Salah: Tertukar antara nilai peluang sukses $p$ dengan $1 - (\text{nilai lain})$ tanpa mencocokkan nilai harapan.</sub>
- C. $0{,}25$  
  <sub>Salah: Mengira $1-p = \frac{1}{16}$ atau salah membagi nilai harapan dengan kuadrat banyaknya percobaan.</sub>
- **D. $0{,}5$** ✅  
  <sub>Benar: Diketahui $E(X) = np = 2$ dan $P(X=0) = (1-p)^n = \frac{1}{16}$. Jika $1-p = \frac{1}{2}$, maka $p = 0{,}5$, yang menghasilkan $\left(\frac{1}{2}\right)^n = \frac{1}{16} \implies n = 4$. Cek nilai harapan: $np = 4 \times 0{,}5 = 2$ (konsisten).</sub>

**Pembahasan:** Dari rumus nilai harapan: $E(X) = n \cdot p = 2$. Peluang untuk $X = 0$: $P(X = 0) = \binom{n}{0} p^0 (1 - p)^n = (1 - p)^n = \frac{1}{16} = \left(\frac{1}{2}\right)^4$. Karena $n$ bilangan bulat positif dan $0 < p < 1$, bentuk perpangkatan yang memenuhi bersamaan dengan $n \cdot p = 2$ adalah $1 - p = \frac{1}{2}$ dan $n = 4$. Maka didapat $p = 1 - \frac{1}{2} = 0{,}5$. Kita periksa: $n \cdot p = 4 \times 0{,}5 = 2$ (terbukti benar).
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b04-f-medium-bt01-005
*orisinal | C3 | 3 langkah | jenis: perbandingan peluang binomial*

Sebuah dadu seimbang bermata enam dilemparkan sebanyak $5$ kali secara saling bebas. Peluang munculnya mata dadu bilangan prima sebanyak $3$ kali adalah ... kali peluang munculnya mata dadu bilangan prima sebanyak $4$ kali.

- A. $\frac{5}{2}$  
  <sub>Salah: Salah menghitung nilai kombinasi $\binom{5}{3}$ menjadi $25$ atau salah menyederhanakan rasio.</sub>
- B. $4$  
  <sub>Salah: Membandingkan langsung nilai $x_2$ dengan $1$ alih-alih rasio kombinasi $\frac{\binom{5}{3}}{\binom{5}{4}}$.</sub>
- **C. $2$** ✅  
  <sub>Benar: Peluang mata dadu prima $\{2, 3, 5\}$ adalah $p = \frac{3}{6} = \frac{1}{2}$, sehingga $q = \frac{1}{2}$. Peluang $X=3$ adalah $\binom{5}{3} \left(\frac{1}{2}\right)^5 = \frac{10}{32}$. Peluang $X=4$ adalah $\binom{5}{4} \left(\frac{1}{2}\right)^5 = \frac{5}{32}$. Rasio keduanya adalah $\frac{10/32}{5/32} = \frac{10}{5} = 2$.</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: Terbalik dalam menghitung perbandingan, membagi peluang $X=4$ dengan peluang $X=3$.</sub>

**Pembahasan:** Mata dadu bernomor prima pada dadu enam sisi adalah $2, 3, 5$, sehingga peluang munculnya mata dadu prima pada setiap pelemparan adalah $p = \frac{3}{6} = \frac{1}{2}$ dan $q = 1 - \frac{1}{2} = \frac{1}{2}$. Banyaknya pelemparan $n = 5$. Peluang muncul $3$ kali prima: $P(X = 3) = \binom{5}{3} \left(\frac{1}{2}\right)^3 \left(\frac{1}{2}\right)^2 = 10 \times \frac{1}{32} = \frac{10}{32}$. Peluang muncul $4$ kali prima: $P(X = 4) = \binom{5}{4} \left(\frac{1}{2}\right)^4 \left(\frac{1}{2}\right)^1 = 5 \times \frac{1}{32} = \frac{5}{32}$. Perbandingan nilai keduanya adalah $\frac{P(X = 3)}{P(X = 4)} = \frac{10/32}{5/32} = \frac{10}{5} = 2$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b04-f-medium-bt01-006
*variasi (konteks) | C3 | 2 langkah | jenis: peluang binomial sukses tepat x*

Peluang sebutir benih jagung gagal berkecambah adalah $0{,}3$. Seorang petani menanam $5$ butir benih jagung secara terpisah dan saling bebas. Peluang tepat $2$ butir benih gagal berkecambah adalah ....

- **A. 0,3087** ✅  
  <sub>Benar: Peluang sukses (gagal berkecambah) $p = 0{,}3$, $q = 1 - 0{,}3 = 0{,}7$, dengan $n = 5$ dan $x = 2$. $P(X = 2) = \binom{5}{2} (0{,}3)^2 (0{,}7)^3 = 10 \times 0{,}09 \times 0{,}343 = 0{,}3087$.</sub>
- B. 0,1323  
  <sub>Salah: Lupa mengalikan dengan koefisien kombinasi $\binom{5}{2} = 10$, sehingga hanya menghitung $p^2 q^3 = 0{,}09 \times 0{,}343 = 0{,}03087$ lalu salah menempatkan desimal.</sub>
- C. 0,4410  
  <sub>Salah: Tertukar pangkat antara $p$ dan $q$, menghitung $10 \times (0{,}3)^3 \times (0{,}7)^2 = 10 \times 0{,}027 \times 0{,}49 = 0{,}1323$ atau salah hitung perkalian desimal.</sub>
- D. 0,3600  
  <sub>Salah: Mengabaikan komponen binomial dan hanya menghitung kombinasi dikali kuadrat $p$: $10 \times (0{,}3)^2 \times 0{,}4$.</sub>

**Pembahasan:** Diketahui:
- Peluang sukses (benih gagal berkecambah): $p = 0{,}3$
- Peluang gagal: $q = 1 - 0{,}3 = 0{,}7$
- Banyak percobaan: $n = 5$
- Banyak kejadian sukses yang diinginkan: $x = 2$

Rumus distribusi binomial:
$$P(X = x) = \binom{n}{x} p^x q^{n-x}$$

Substitusi nilai-nilai ke dalam rumus:
$$\begin{aligned} P(X = 2) &= \binom{5}{2} (0{,}3)^2 (0{,}7)^{5-2} \\ &= \frac{5!}{2!(5-2)!} \times 0{,}09 \times (0{,}7)^3 \\ &= 10 \times 0{,}09 \times 0{,}343 \\ &= 0{,}3087 \end{aligned}$$

Jadi, peluang tepat $2$ butir benih gagal berkecambah adalah $0{,}3087$.
**Acuan:** siswa — siswa hal.280 Latihan Soal Distribusi Binomial

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b04-f-medium-bt01-007
*variasi (angka) | C3 | 2 langkah | jenis: peluang binomial sukses tepat satu*

Peluang sebuah barang elektronik lolos uji kelayakan adalah $0{,}7$. Jika dipilih $5$ barang secara acak dan saling bebas untuk diuji, peluang bahwa hanya satu barang yang lolos uji kelayakan adalah ....

- A. 0,05670  
  <sub>Salah: Salah menghitung nilai kombinasi menjadi $\binom{5}{1} = 10$ sehingga menghasilkan $10 \times 0{,}00567 = 0{,}0567$.</sub>
- B. 0,09720  
  <sub>Salah: Tertukar antara peluang sukses dan peluang gagal, yaitu menghitung $\binom{5}{1} (0{,}3)^1 (0{,}7)^4 = 5 \times 0{,}3 \times 0{,}2401$.</sub>
- **C. 0,02835** ✅  
  <sub>Benar: Parameter $n = 5$, $x = 1$, $p = 0{,}7$, $q = 0{,}3$. $P(X = 1) = \binom{5}{1} (0{,}7)^1 (0{,}3)^4 = 5 \times 0{,}7 \times 0{,}0081 = 0{,}02835$.</sub>
- D. 0,00567  
  <sub>Salah: Lupa mengalikan dengan faktor kombinasi $\binom{5}{1} = 5$, sehingga hanya menghitung $(0{,}7) \times (0{,}3)^4 = 0{,}00567$.</sub>

**Pembahasan:** Berdasarkan permasalahan:
- Peluang sukses $p = 0{,}7$
- Peluang gagal $q = 1 - 0{,}7 = 0{,}3$
- Banyak barang diuji $n = 5$
- Banyak keberhasilan $x = 1$

Peluang tepat satu barang lolos dihitung menggunakan rumus distribusi binomial:
$$\begin{aligned} P(X = 1) &= \binom{5}{1} (0{,}7)^1 (0{,}3)^{5-1} \\ &= 5 \times 0{,}7 \times (0{,}3)^4 \\ &= 3{,}5 \times 0{,}0081 \\ &= 0{,}02835 \end{aligned}$$

Jadi, peluang bahwa hanya satu barang yang lolos uji kelayakan adalah $0{,}02835$.
**Acuan:** pretest — kelas12_tl-b04-p0280-latihan-soal-distribusi-binomial-5b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b04-f-medium-bt01-008
*variasi (konteks) | C3 | 2 langkah | jenis: peluang binomial nol sukses*

Sebuah survei menemukan bahwa $1$ dari $4$ nasabah bank memilih bertransaksi langsung di kantor cabang. Jika dipilih $4$ nasabah secara acak dan saling bebas, peluang bahwa tidak ada satu pun dari nasabah tersebut yang memilih bertransaksi langsung di kantor cabang adalah ....

- **A. $\frac{81}{256}$** ✅  
  <sub>Benar: Peluang sukses $p = \frac{1}{4}$, peluang gagal $q = \frac{3}{4}$, $n = 4$, $x = 0$. $P(X = 0) = \binom{4}{0} \left(\frac{1}{4}\right)^0 \left(\frac{3}{4}\right)^4 = 1 \times 1 \times \frac{81}{256} = \frac{81}{256}$.</sub>
- B. $\frac{1}{256}$  
  <sub>Salah: Menghitung peluang semua nasabah bertransaksi di cabang, yaitu $P(X = 4) = (\frac{1}{4})^4 = \frac{1}{256}$.</sub>
- C. $\frac{27}{64}$  
  <sub>Salah: Salah menghitung pangkat kegagalan sebagai $q^3 = (\frac{3}{4})^3 = \frac{27}{64}$.</sub>
- D. $\frac{175}{256}$  
  <sub>Salah: Menghitung komplemen $1 - P(X=0) = 1 - \frac{81}{256} = \frac{175}{256}$.</sub>

**Pembahasan:** Dari soal diperoleh:
- Peluang sukses memilih di cabang: $p = \frac{1}{4}$
- Peluang gagal: $q = 1 - \frac{1}{4} = \frac{3}{4}$
- Banyak nasabah: $n = 4$
- Banyak nasabah yang diinginkan: $x = 0$

Peluang tidak ada yang memilih bertransaksi di kantor cabang:
$$\begin{aligned} P(X = 0) &= \binom{4}{0} \left(\frac{1}{4}\right)^0 \left(\frac{3}{4}\right)^4 \\ &= 1 \times 1 \times \frac{81}{256} \\ &= \frac{81}{256} \end{aligned}$$

Jadi, peluangnya adalah $\frac{81}{256}$.
**Acuan:** siswa — siswa hal.280 Latihan Soal Distribusi Binomial

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b04-f-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: rekonstruksi peluang sukses dari rasio binomial*

Suatu variabel acak $X$ berdistribusi binomial dengan $n = 3$ percobaan bebas dan peluang sukses $p$ (dengan $0 < p < 1$). Jika diketahui $P(X = 1) = 2 \cdot P(X = 2)$, maka nilai $p$ adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: Salah menyelesaikan aljabar pada tahap akhir dengan membagi $1$ dengan $4$ bukan $3$.</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: Mengabaikan koefisien pengali $2$ dan menganggap kedua peluang bernilai sama sehingga $p = 1-p$.</sub>
- **C. $\frac{1}{3}$** ✅  
  <sub>Benar: $P(X = 1) = 3p(1-p)^2$ dan $P(X = 2) = 3p^2(1-p)$. Persamaan $3p(1-p)^2 = 2 \cdot 3p^2(1-p)$ menghasilkan $1-p = 2p$, sehingga $3p = 1 \implies p = \frac{1}{3}$.</sub>
- D. $\frac{2}{3}$  
  <sub>Salah: Tertukar antara nilai $p$ dan $q$ saat menyelesaikan persamaan linear $1-p = 2p$.</sub>

**Pembahasan:** Rumus peluang binomial untuk $n = 3$:
$$P(X = x) = \binom{3}{x} p^x (1-p)^{3-x}$$

Untuk $x = 1$:
$$P(X = 1) = \binom{3}{1} p^1 (1-p)^2 = 3p(1-p)^2$$

Untuk $x = 2$:
$$P(X = 2) = \binom{3}{2} p^2 (1-p)^1 = 3p^2(1-p)$$

Diketahui $P(X = 1) = 2 \cdot P(X = 2)$, maka:
$$3p(1-p)^2 = 2 \cdot 3p^2(1-p)$$

Karena $0 < p < 1$, kita dapat membagi kedua ruas dengan $3p(1-p)$:
$$\begin{aligned} 1 - p &= 2p \\ 1 &= 3p \\ p &= \frac{1}{3} \end{aligned}$$

Jadi, nilai peluang sukses $p$ adalah $\frac{1}{3}$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b04-f-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: nilai harapan dari rasio peluang ekstrem*

Variabel acak $X$ berdistribusi binomial dengan banyaknya percobaan $n = 4$ dan peluang sukses $p$. Jika rasio peluang semua percobaan sukses terhadap peluang tidak ada percobaan yang sukses adalah $P(X = 4) : P(X = 0) = 16 : 1$, nilai harapan $E(X)$ dari variabel acak tersebut adalah ....

- A. $\frac{8}{5}$  
  <sub>Salah: Salah menyelesaikan persamaan rasio menjadi $\frac{p}{1-p} = 4$ sehingga memperoleh $p = \frac{4}{5}$ lalu menghitung $E(X)$.</sub>
- **B. $\frac{8}{3}$** ✅  
  <sub>Benar: $P(X = 4) = p^4$ dan $P(X = 0) = (1-p)^4$. Rasio $\frac{p^4}{(1-p)^4} = 16 \implies \frac{p}{1-p} = 2 \implies p = \frac{2}{3}$. Nilai harapan $E(X) = n \cdot p = 4 \times \frac{2}{3} = \frac{8}{3}$.</sub>
- C. $\frac{4}{3}$  
  <sub>Salah: Tertukar menghitung nilai harapan menggunakan peluang gagal $q = \frac{1}{3}$, sehingga $4 \times \frac{1}{3} = \frac{4}{3}$.</sub>
- D. $2$  
  <sub>Salah: Menyimpulkan rasio $16:1$ berakar menjadi $p = \frac{1}{2}$, lalu menghitung $E(X) = 4 \times \frac{1}{2} = 2$.</sub>

**Pembahasan:** Rumus fungsi peluang binomial:
$$P(X = x) = \binom{n}{x} p^x (1-p)^{n-x}$$

Untuk $n = 4$:
$$P(X = 4) = \binom{4}{4} p^4 (1-p)^0 = p^4$$
$$P(X = 0) = \binom{4}{0} p^0 (1-p)^4 = (1-p)^4$$

Diketahui perbandingan:
$$\frac{P(X = 4)}{P(X = 0)} = \frac{p^4}{(1-p)^4} = 16$$

Menarik akar pangkat empat dari kedua ruas (karena $0 < p < 1$):
$$\begin{aligned} \frac{p}{1-p} &= 2 \\ p &= 2(1-p) \\ p &= 2 - 2p \\ 3p &= 2 \\ p &= \frac{2}{3} \end{aligned}$$

Menghitung nilai harapan $E(X)$:
$$E(X) = n \cdot p = 4 \times \frac{2}{3} = \frac{8}{3}$$

Jadi, nilai harapan $E(X)$ adalah $\frac{8}{3}$.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b04-f-medium-bt01-011
*variasi (angka) | C3 | 2 langkah | jenis: peluang dan nilai harapan binomial*

Peluang keberhasilan seorang pemain bola basket dalam melakukan lemparan bebas adalah $0{,}6$. Jika ia diberikan kesempatan melakukan $3$ kali lemparan bebas secara bebas dan saling lepas, peluang ia berhasil memasukkan tepat $2$ kali lemparan dan nilai harapannya berturut-turut adalah ....

- **A. $0{,}432$ dan $1{,}8$** ✅  
  <sub>Benar: $n = 3$, $p = 0{,}6$, dan $q = 1 - 0{,}6 = 0{,}4$. Peluang tepat 2 kali: $P(X = 2) = \binom{3}{2} (0{,}6)^2 (0{,}4)^1 = 3 \times 0{,}36 \times 0{,}4 = 0{,}432$. Nilai harapan: $E(X) = n \cdot p = 3 \times 0{,}6 = 1{,}8$.</sub>
- B. $0{,}144$ dan $1{,}8$  
  <sub>Salah: Lupa mengalikan dengan faktor kombinasi $\binom{3}{2} = 3$ pada peluang sehingga didapat $0{,}36 \times 0{,}4 = 0{,}144$.</sub>
- C. $0{,}432$ dan $1{,}2$  
  <sub>Salah: Salah menghitung nilai harapan dengan rumus $n \cdot q = 3 \times 0{,}4 = 1{,}2$ (menggunakan peluang gagal).</sub>
- D. $0{,}288$ dan $1{,}8$  
  <sub>Salah: Tertukar pangkat sukses dan gagal: menghitung $\binom{3}{2} (0{,}6)^1 (0{,}4)^2 = 3 \times 0{,}6 \times 0{,}16 = 0{,}288$.</sub>

**Pembahasan:** Diketahui:
- Peluang sukses $p = 0{,}6$
- Peluang gagal $q = 1 - 0{,}6 = 0{,}4$
- Banyak percobaan $n = 3$

1. Peluang tepat $2$ kali berhasil:
$$P(X = 2) = \binom{3}{2} p^2 q^{3-2} = 3 \times (0{,}6)^2 \times (0{,}4)^1 = 3 \times 0{,}36 \times 0{,}4 = 0{,}432$$

2. Nilai harapan banyaknya keberhasilan:
$$E(X) = n \cdot p = 3 \times 0{,}6 = 1{,}8$$

Jadi, peluang tepat $2$ kali lemparan masuk dan nilai harapannya berturut-turut adalah $0{,}432$ dan $1{,}8$.
**Acuan:** siswa — siswa hal.279 Latihan Soal Distribusi Binomial

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b04-f-medium-bt01-012
*variasi (konteks) | C3 | 2 langkah | jenis: peluang binomial komplemen*

Peluang sebuah mesin pemotong rumput menyala dalam satu kali tarikan tali starter adalah $0{,}7$. Jika tali starter ditarik sebanyak $3$ kali secara saling bebas, peluang mesin tersebut menyala paling sedikit satu kali adalah ....

- A. $0{,}657$  
  <sub>Salah: Mengurangkan peluang semua sukses dari $1$, yaitu $1 - (0{,}7)^3 = 1 - 0{,}343 = 0{,}657$.</sub>
- **B. $0{,}973$** ✅  
  <sub>Benar: Kejadian paling sedikit satu kali menyala merupakan komplemen dari mesin tidak pernah menyala sama sekali ($X = 0$). Dengan $n = 3$, $p = 0{,}7$, dan $q = 0{,}3$, diperoleh $P(X \ge 1) = 1 - P(X = 0) = 1 - \binom{3}{0}(0{,}7)^0(0{,}3)^3 = 1 - 0{,}027 = 0{,}973$.</sub>
- C. $0{,}027$  
  <sub>Salah: Hanya menghitung peluang tidak menyala sama sekali $P(X = 0) = (0{,}3)^3 = 0{,}027$ tanpa mengurangkannya dari $1$.</sub>
- D. $0{,}343$  
  <sub>Salah: Hanya menghitung peluang selalu menyala pada semua tarikan $P(X = 3) = (0{,}7)^3 = 0{,}343$.</sub>

**Pembahasan:** Misalkan $X$ adalah banyak tarikan yang berhasil menyalakan mesin dari $n = 3$ tarikan.
Peluang berhasil $p = 0{,}7$ dan peluang gagal $q = 1 - 0{,}7 = 0{,}3$.

Peluang mesin menyala paling sedikit satu kali adalah $P(X \ge 1)$.
Menggunakan sifat komplemen:
$$P(X \ge 1) = 1 - P(X = 0)$$
$$P(X = 0) = \binom{3}{0} (0{,}7)^0 (0{,}3)^3 = 1 \times 1 \times 0{,}027 = 0{,}027$$
Maka:
$$P(X \ge 1) = 1 - 0{,}027 = 0{,}973$$

Jadi, peluang mesin menyala paling sedikit satu kali adalah $0{,}973$.
**Acuan:** pretest — kelas12_tl-b04-p0280-latihan-soal-distribusi-binomial-5c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b04-f-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: analisis parameter dari rasio binomial*

Suatu variabel acak $X$ berdistribusi binomial dengan banyaknya percobaan $n = 4$ dan peluang sukses $p$ (dengan $0 < p < 1$). Jika diketahui $P(X = 3) = 4 \cdot P(X = 4)$, maka nilai harapan $E(X)$ dari variabel acak tersebut adalah ....

- A. $\frac{8}{3}$  
  <sub>Salah: Salah mengalikan nilai $p = \frac{2}{3}$ dari kesalahan aljabar sehingga $E(X) = 4 \times \frac{2}{3} = \frac{8}{3}$.</sub>
- B. $1$  
  <sub>Salah: Keliru menyederhanakan $1 - p = 4p$ sehingga didapat $p = 0{,}2$, lalu $E(X) = 4 \times 0{,}2 = 0{,}8 \approx 1$ atau salah bagi koefisien.</sub>
- C. $\frac{4}{3}$  
  <sub>Salah: Salah menyelesaikan persamaan menjadi $1 - p = 2p \implies p = \frac{1}{3}$, sehingga $E(X) = 4 \times \frac{1}{3} = \frac{4}{3}$.</sub>
- **D. $2$** ✅  
  <sub>Benar: $P(X = 3) = \binom{4}{3} p^3 (1-p) = 4p^3(1-p)$ dan $P(X = 4) = \binom{4}{4} p^4 = p^4$. Persamaan $4p^3(1-p) = 4p^4 \implies 1 - p = p \implies 2p = 1 \implies p = 0{,}5$. Nilai harapan $E(X) = n \cdot p = 4 \times 0{,}5 = 2$.</sub>

**Pembahasan:** Rumus fungsi distribusi binomial untuk $n = 4$:
$$P(X = x) = \binom{4}{x} p^x (1 - p)^{4-x}$$

Berdasarkan yang diketahui:
$$P(X = 3) = \binom{4}{3} p^3 (1 - p)^{4-3} = 4p^3(1 - p)$$
$$P(X = 4) = \binom{4}{4} p^4 (1 - p)^0 = p^4$$

Substitusikan ke persamaan $P(X = 3) = 4 \cdot P(X = 4)$:
$$4p^3(1 - p) = 4(p^4)$$
Bagi kedua ruas dengan $4p^3$ (karena $p \ne 0$):
$$1 - p = p$$
$$2p = 1 \implies p = 0{,}5$$

Nilai harapan $E(X)$:
$$E(X) = n \cdot p = 4 \times 0{,}5 = 2$$

Jadi, nilai harapan $E(X)$ adalah $2$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b04-f-medium-bt01-014
*orisinal | C3 | 2 langkah | jenis: peluang binomial koin tak seimbang*

Sebuah uang logam tidak seimbang dirancang sedemikian rupa sehingga peluang munculnya sisi angka adalah dua kali peluang munculnya sisi gambar pada setiap pelemparan. Jika uang logam tersebut dilemparkan sebanyak $3$ kali secara saling bebas, peluang diperoleh tepat satu kali sisi gambar adalah ....

- A. $\frac{2}{9}$  
  <sub>Salah: Lupa mengalikan dengan koefisien kombinasi $\binom{3}{1} = 3$ sehingga menghasilkan $\frac{1}{3} \cdot \frac{4}{9} = \frac{4}{27}$ yang lalu salah disederhanakan, atau menghitung $\binom{3}{1} \left(\frac{1}{3}\right)^2 \left(\frac{2}{3}\right)^1 = \frac{2}{9}$ (peluang tepat dua gambar).</sub>
- B. $\frac{1}{3}$  
  <sub>Salah: Mengira peluang mendapatkan tepat 1 gambar sama langsung dengan nilai peluang sukses tunggal $p = \frac{1}{3}$.</sub>
- C. $\frac{3}{8}$  
  <sub>Salah: Menggunakan peluang uang logam seimbang ($p = \frac{1}{2}$) sehingga menghitung $\binom{3}{1}\left(\frac{1}{2}\right)^3 = \frac{3}{8}$.</sub>
- **D. $\frac{4}{9}$** ✅  
  <sub>Benar: P(A) = 2 P(G) dan P(A) + P(G) = 1 $\implies$ P(G) = $\frac{1}{3}$, P(A) = $\frac{2}{3}$. Dengan $n = 3$ dan sukses adalah sisi gambar ($p = \frac{1}{3}$): $P(X = 1) = \binom{3}{1} \left(\frac{1}{3}\right)^1 \left(\frac{2}{3}\right)^2 = 3 \cdot \frac{1}{3} \cdot \frac{4}{9} = \frac{4}{9}$.</sub>

**Pembahasan:** Misalkan $P(G)$ adalah peluang muncul sisi gambar dan $P(A)$ adalah peluang muncul sisi angka.
Diketahui $P(A) = 2 \cdot P(G)$.
Karena $P(A) + P(G) = 1$, maka:
$$2P(G) + P(G) = 1 \implies 3P(G) = 1 \implies P(G) = \frac{1}{3}$$
Sehingga peluang sisi angka adalah $P(A) = \frac{2}{3}$.

Misalkan $X$ adalah banyak sisi gambar yang muncul dari $n = 3$ lemparan.
Dengan $p = P(G) = \frac{1}{3}$ dan $q = P(A) = \frac{2}{3}$:
$$P(X = 1) = \binom{3}{1} p^1 q^{3-1} = 3 \times \left(\frac{1}{3}\right)^1 \times \left(\frac{2}{3}\right)^2 = 3 \times \frac{1}{3} \times \frac{4}{9} = \frac{4}{9}$$

Jadi, peluang diperoleh tepat satu kali sisi gambar adalah $\frac{4}{9}$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b04-f-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: rekonstruksi n dari nilai harapan*

Variabel acak $X$ berdistribusi binomial dengan banyak percobaan $n$ dan peluang keberhasilan $p = 0{,}75$. Jika nilai harapan dari $X$ adalah $E(X) = 3$, maka peluang terjadinya tepat dua kali keberhasilan, yaitu $P(X = 2)$, adalah ....

- A. $\frac{27}{64}$  
  <sub>Salah: Salah menghitung penyebut $(4^4 = 256)$ menjadi $4^3 = 64$ sehingga diperoleh $\frac{27}{64}$.</sub>
- **B. $\frac{27}{128}$** ✅  
  <sub>Benar: $E(X) = n \cdot p \implies 3 = n \times \frac{3}{4} \implies n = 4$. Maka $P(X = 2) = \binom{4}{2} \left(\frac{3}{4}\right)^2 \left(\frac{1}{4}\right)^2 = 6 \times \frac{9}{16} \times \frac{1}{16} = \frac{54}{256} = \frac{27}{128}$.</sub>
- C. $\frac{9}{64}$  
  <sub>Salah: Menggunakan nilai $n = 3$ karena langsung menyamakan $n$ dengan nilai $E(X) = 3$, lalu menghitung $\binom{3}{2}\left(\frac{3}{4}\right)^2\left(\frac{1}{4}\right) = 3 \times \frac{9}{16} \times \frac{1}{4} = \frac{27}{64}$, atau kombinasi hitungan salah lainnya yang menghasilkan $\frac{9}{64}$.</sub>
- D. $\frac{9}{128}$  
  <sub>Salah: Lupa mengalikan koefisien kombinasi $\binom{4}{2} = 6$, atau hanya mengalikan dengan $2$ sehingga $\frac{18}{256} = \frac{9}{128}$.</sub>

**Pembahasan:** Langkah 1: Tentukan banyak percobaan $n$.
Diketahui nilai harapan $E(X) = n \cdot p$.
$$3 = n \times 0{,}75$$
$$3 = n \times \frac{3}{4} \implies n = \frac{3 \times 4}{3} = 4$$

Langkah 2: Hitung $P(X = 2)$.
Dengan $n = 4$, $p = \frac{3}{4}$, dan $q = 1 - \frac{3}{4} = \frac{1}{4}$:
$$P(X = 2) = \binom{4}{2} p^2 q^{4-2} = \binom{4}{2} \left(\frac{3}{4}\right)^2 \left(\frac{1}{4}\right)^2$$
$$\binom{4}{2} = \frac{4 \times 3}{2 \times 1} = 6$$
$$P(X = 2) = 6 \times \frac{9}{16} \times \frac{1}{16} = \frac{54}{256} = \frac{27}{128}$$

Jadi, peluang terjadinya tepat dua kali keberhasilan adalah $\frac{27}{128}$.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b04-f-medium-bt01-016
*variasi (angka) | C3 | 2 langkah | jenis: peluang kejadian binomial spesifik*

Peluang seorang bayi belum divaksinasi campak adalah $0{,}3$. Suatu hari terdapat $5$ bayi di sebuah posyandu. Peluang bahwa tepat $3$ dari $5$ bayi tersebut belum divaksinasi campak adalah ....

- **A. $0{,}1323$** ✅  
  <sub>Benar: Dihitung dari $P(X = 3) = \binom{5}{3} (0{,}3)^3 (0{,}7)^2 = 10 \times 0{,}027 \times 0{,}49 = 0{,}1323$.</sub>
- B. $0{,}3087$  
  <sub>Salah: Tertukar menghitung peluang untuk $2$ bayi belum divaksinasi yaitu $\binom{5}{2} (0{,}3)^2 (0{,}7)^3$.</sub>
- C. $0{,}0132$  
  <sub>Salah: Lupa mengalikan dengan koefisien kombinasi $\binom{5}{3} = 10$.</sub>
- D. $0{,}2646$  
  <sub>Salah: Salah menghitung nilai kombinasi $\binom{5}{3}$ menjadi $20$ bukannya $10$.</sub>

**Pembahasan:** Diketahui:
- Peluang sukses (belum divaksinasi): $p = 0{,}3$
- Peluang gagal: $q = 1 - 0{,}3 = 0{,}7$
- Banyaknya percobaan: $n = 5$
- Banyaknya kejadian sukses yang diharapkan: $x = 3$

Rumus fungsi distribusi binomial:
$$P(X = x) = \binom{n}{x} p^x q^{n-x}$$

Substitusi nilai-nilai ke dalam rumus:
$$P(X = 3) = \binom{5}{3} (0{,}3)^3 (0{,}7)^{5-3}$$
$$P(X = 3) = \frac{5!}{3!(5-3)!} \times 0{,}027 \times (0{,}7)^2$$
$$P(X = 3) = 10 \times 0{,}027 \times 0{,}49 = 0{,}1323$$

Jadi, peluang tepat $3$ dari $5$ bayi belum divaksinasi campak adalah $0{,}1323$.
**Acuan:** siswa — siswa hal.280 Latihan Soal Distribusi Binomial

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b04-f-medium-bt01-017
*variasi (konteks) | C3 | 3 langkah | jenis: peluang binomial pelanggaran*

Sebuah penelitian di jalan tol mendapati bahwa satu dari empat kendaraan melanggar batas kecepatan maksimal. Jika dipilih secara acak $6$ kendaraan yang melintas secara saling bebas, berapakah peluang tepat $2$ kendaraan yang melanggar batas kecepatan maksimal?

- A. $\frac{135}{4096}$  
  <sub>Salah: Salah memangkatkan nilai peluang gagal $(3/4)^4$ dihitung sebagai $3^3 / 4^4 = 27 / 256$.</sub>
- **B. $\frac{1215}{4096}$** ✅  
  <sub>Benar: Dihitung dari $P(X = 2) = \binom{6}{2} \left(\frac{1}{4}\right)^2 \left(\frac{3}{4}\right)^4 = 15 \times \frac{1}{16} \times \frac{81}{256} = \frac{1215}{4096}$.</sub>
- C. $\frac{1215}{2048}$  
  <sub>Salah: Salah menghitung hasil perkalian penyebut $16 \times 256$ menjadi $2048$.</sub>
- D. $\frac{405}{4096}$  
  <sub>Salah: Salah menghitung kombinasi $\binom{6}{2}$ menjadi $5$ bukannya $15$.</sub>

**Pembahasan:** Dari informasi soal didapatkan:
- Peluang kendaraan melanggar: $p = \frac{1}{4}$
- Peluang kendaraan tidak melanggar: $q = 1 - \frac{1}{4} = \frac{3}{4}$
- Jumlah kendaraan yang diamati: $n = 6$
- Jumlah kendaraan melanggar yang diinginkan: $x = 2$

Menggunakan rumus peluang binomial:
$$P(X = x) = \binom{n}{x} p^x q^{n-x}$$
$$P(X = 2) = \binom{6}{2} \left(\frac{1}{4}\right)^2 \left(\frac{3}{4}\right)^{6-2}$$
$$P(X = 2) = \frac{6 \times 5}{2 \times 1} \times \frac{1}{16} \times \left(\frac{3}{4}\right)^4$$
$$P(X = 2) = 15 \times \frac{1}{16} \times \frac{81}{256} = \frac{1215}{4096}$$

Jadi, peluang tepat $2$ kendaraan melanggar adalah $\frac{1215}{4096}$.
**Acuan:** siswa — siswa hal.280 Latihan Soal Distribusi Binomial

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b04-f-medium-bt01-018
*variasi (angka) | C3 | 2 langkah | jenis: peluang binomial sukses sebagian*

Peluang seorang siswa lulus dalam seleksi masuk perguruan tinggi adalah $0{,}8$. Misalkan terdapat $4$ siswa dari sekolah yang sama mengikuti seleksi tersebut secara saling bebas. Peluang bahwa tepat $2$ siswa yang lulus seleksi adalah ....

- A. $0{,}1024$  
  <sub>Salah: Salah menggunakan nilai kombinasi $\binom{4}{1} = 4$ bukannya $\binom{4}{2} = 6$.</sub>
- **B. $0{,}1536$** ✅  
  <sub>Benar: Dihitung dari $P(X = 2) = \binom{4}{2} (0{,}8)^2 (0{,}2)^2 = 6 \times 0{,}64 \times 0{,}04 = 0{,}1536$.</sub>
- C. $0{,}4096$  
  <sub>Salah: Menghitung peluang untuk $3$ siswa yang lulus yaitu $\binom{4}{3} (0{,}8)^3 (0{,}2)^1$.</sub>
- D. $0{,}0256$  
  <sub>Salah: Lupa mengalikan dengan faktor kombinasi $\binom{4}{2} = 6$, hanya menghitung $(0{,}8)^2 (0{,}2)^2$.</sub>

**Pembahasan:** Diketahui:
- Peluang lulus: $p = 0{,}8$
- Peluang tidak lulus: $q = 1 - 0{,}8 = 0{,}2$
- Banyaknya siswa: $n = 4$
- Banyaknya siswa lulus yang diharapkan: $x = 2$

Peluang binomial:
$$P(X = 2) = \binom{4}{2} (0{,}8)^2 (0{,}2)^{4-2}$$
$$P(X = 2) = \frac{4 \times 3}{2 \times 1} \times 0{,}64 \times (0{,}2)^2$$
$$P(X = 2) = 6 \times 0{,}64 \times 0{,}04 = 0{,}1536$$

Jadi, peluang tepat $2$ siswa lulus seleksi adalah $0{,}1536$.
**Acuan:** pretest — kelas12_tl-b04-p0280-latihan-soal-distribusi-binomial-5b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b04-f-medium-bt01-019
*orisinal | C4 | 3 langkah | jenis: sistem parameter binomial*

Suatu variabel acak $X$ berdistribusi binomial dengan $n$ percobaan saling bebas dan peluang sukses $p$. Diketahui nilai harapan $E(X) = 1{,}6$ dan peluang tidak ada percobaan yang berhasil adalah $P(X = 0) = 0{,}1296$. Nilai dari banyaknya percobaan $n$ adalah ....

- A. $8$  
  <sub>Salah: Salah menentukan nilai $p$ menjadi $0{,}2$ sehingga menghitung $n = 1{,}6 / 0{,}2 = 8$.</sub>
- B. $5$  
  <sub>Salah: Salah membagi nilai harapan dengan menganggap $p = 0{,}32$ sehingga $1{,}6 / 0{,}32 = 5$.</sub>
- C. $6$  
  <sub>Salah: Terkecoh angka desimal $0{,}6$ pada $(1-p)$ dan mengira banyaknya percobaan adalah $6$.</sub>
- **D. $4$** ✅  
  <sub>Benar: Dari $P(X=0) = (1-p)^n = 0{,}1296 = (0{,}6)^4$, didapat $1-p = 0{,}6 \implies p = 0{,}4$. Karena $E(X) = np = 1{,}6$, maka $n = 1{,}6 / 0{,}4 = 4$.</sub>

**Pembahasan:** 1. Berdasarkan rumus peluang distribusi binomial:
$$P(X = 0) = \binom{n}{0} p^0 (1-p)^{n-0} = (1-p)^n$$
Diketahui $P(X = 0) = 0{,}1296$. Perhatikan bahwa $0{,}1296 = \frac{1296}{10000} = \left(\frac{6}{10}\right)^4 = (0{,}6)^4$.
Maka diperoleh hubungan:
$$(1-p)^n = (0{,}6)^4$$
Sehingga $1 - p = 0{,}6$ dan $n = 4$, yang menghasilkan $p = 0{,}4$.

2. Verifikasi dengan rumus nilai harapan:
$$E(X) = n \cdot p = 4 \cdot 0{,}4 = 1{,}6$$
Nilai ini sesuai dengan informasi pada soal.

Jadi, banyaknya percobaan $n$ adalah $4$.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b04-f-medium-bt01-020
*orisinal | C4 | 2 langkah | jenis: rasio peluang berurutan*

Suatu variabel acak $X$ berdistribusi binomial dengan banyaknya percobaan $n = 5$ dan peluang sukses pada setiap percobaan adalah $p = \frac{1}{3}$. Nilai perbandingan peluang $\frac{P(X = 3)}{P(X = 2)}$ adalah ....

- A. $\frac{2}{3}$  
  <sub>Salah: Mengambil nilai peluang gagal $q$ bukannya rasio $p/q$.</sub>
- B. $\frac{1}{3}$  
  <sub>Salah: Hanya mengambil nilai peluang sukses $p$.</sub>
- **C. $\frac{1}{2}$** ✅  
  <sub>Benar: Rasio $\frac{\binom{5}{3} p^3 q^2}{\binom{5}{2} p^2 q^3} = \frac{10 p^3 q^2}{10 p^2 q^3} = \frac{p}{q} = \frac{1/3}{2/3} = \frac{1}{2}$.</sub>
- D. $2$  
  <sub>Salah: Terbalik menghitung rasio $\frac{P(X = 2)}{P(X = 3)} = \frac{q}{p} = 2$.</sub>

**Pembahasan:** Diketahui:
- $n = 5$
- $p = \frac{1}{3}$
- $q = 1 - p = 1 - \frac{1}{3} = \frac{2}{3}$

Tuliskan rumus peluang untuk $X = 3$ dan $X = 2$:
$$P(X = 3) = \binom{5}{3} p^3 q^{5-3} = 10 p^3 q^2$$
$$P(X = 2) = \binom{5}{2} p^2 q^{5-2} = 10 p^2 q^3$$

Bandingkan kedua nilai tersebut:
$$\frac{P(X = 3)}{P(X = 2)} = \frac{10 p^3 q^2}{10 p^2 q^3} = \frac{p}{q}$$

Substitusikan nilai $p$ dan $q$:
$$\frac{p}{q} = \frac{\frac{1}{3}}{\frac{2}{3}} = \frac{1}{2}$$

Jadi, nilai perbandingan $\frac{P(X = 3)}{P(X = 2)}$ adalah $\frac{1}{2}$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b04-f-hard-bt01-001
*variasi (konteks) | C5 | 5 langkah | jenis: evaluasi klaim binomial*

Sebuah mesin produksi menghasilkan barang dengan peluang cacat sebesar $0{,}5$ pada setiap unit secara saling bebas. Seorang pengawas mutu mengambil sampel $6$ unit barang secara acak dan menyatakan klaim bahwa 'peluang menemukan paling sedikit $4$ unit barang cacat melebihi $0{,}35$'. Nilai peluang sesungguhnya dan kesimpulan terhadap klaim tersebut adalah ....

- A. $\frac{21}{32}$ dan klaim benar  
  <sub>Salah: Menghitung komplemen secara terbalik $1 - P(X \ge 4) = \frac{42}{64} = \frac{21}{32}$.</sub>
- **B. $\frac{11}{32}$ dan klaim salah** ✅  
  <sub>Benar: $P(X \ge 4) = \frac{\binom{6}{4} + \binom{6}{5} + \binom{6}{6}}{2^6} = \frac{15 + 6 + 1}{64} = \frac{22}{64} = \frac{11}{32} = 0{,}34375$. Karena $0{,}34375 < 0{,}35$, klaim tersebut salah.</sub>
- C. $\frac{11}{32}$ dan klaim benar  
  <sub>Salah: Benar menghitung nilai peluang $\frac{11}{32} = 0{,}34375$, namun salah membandingkan desimal dan menganggap $0{,}34375 > 0{,}35$.</sub>
- D. $\frac{7}{32}$ dan klaim salah  
  <sub>Salah: Hanya menjumlahkan kasus $X=5$ dan $X=6$, lupa menyertakan $X=4$.</sub>

**Pembahasan:** Langkah 1: Identifikasi parameter binomial:
$n = 6$, $p = 0{,}5 = \frac{1}{2}$, $q = 1 - p = \frac{1}{2}$.

Langkah 2: Menghitung peluang masing-masing titik untuk $X \ge 4$:
$$P(X = 4) = \binom{6}{4}\left(\frac{1}{2}\right)^6 = \frac{15}{64}$$
$$P(X = 5) = \binom{6}{5}\left(\frac{1}{2}\right)^6 = \frac{6}{64}$$
$$P(X = 6) = \binom{6}{6}\left(\frac{1}{2}\right)^6 = \frac{1}{64}$$

Langkah 3: Menjumlahkan peluang:
$$P(X \ge 4) = \frac{15 + 6 + 1}{64} = \frac{22}{64} = \frac{11}{32}$$

Langkah 4: Konversi ke desimal:
$$\frac{11}{32} = 0{,}34375$$

Langkah 5: Evaluasi klaim:
Karena $0{,}34375 < 0{,}35$, maka klaim pengawas bahwa peluang melebihi $0{,}35$ adalah salah.
**Acuan:** siswa — siswa hal.271 Ayo Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b04-f-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: penentuan parameter binomial*

Suatu variabel acak $X$ berdistribusi binomial dengan $n = 5$ percobaan saling bebas dan peluang sukses $p$ (dengan $0 < p < 1$). Jika diketahui peluang terjadinya $2$ kali sukses sama dengan peluang terjadinya $3$ kali sukses ($P(X = 2) = P(X = 3)$), maka nilai harapan $E(X)$ adalah ....

- A. $3{,}0$  
  <sub>Salah: Mengira nilai harapan sama dengan nilai $x$ kedua yang diketahui yaitu $x = 3$.</sub>
- **B. $2{,}5$** ✅  
  <sub>Benar: $\binom{5}{2} p^2 (1-p)^3 = \binom{5}{3} p^3 (1-p)^2 \implies 10(1-p) = 10p \implies 1 - p = p \implies p = 0{,}5$. Maka $E(X) = n \cdot p = 5 \cdot 0{,}5 = 2{,}5$.</sub>
- C. $2{,}0$  
  <sub>Salah: Mengira nilai harapan sama dengan nilai $x$ pertama yang diketahui yaitu $x = 2$.</sub>
- D. $1{,}5$  
  <sub>Salah: Salah menyelesaikan persamaan menjadi $1 - p = 2p \implies p = \frac{1}{3}$, sehingga $E(X) = \frac{5}{3} \approx 1{,}67$ lalu dibulatkan salah.</sub>

**Pembahasan:** Langkah 1: Tuliskan rumus peluang binomial untuk kedua kondisi:
$$P(X = 2) = \binom{5}{2} p^2 (1 - p)^{5 - 2} = 10 p^2 (1 - p)^3$$
$$P(X = 3) = \binom{5}{3} p^3 (1 - p)^{5 - 3} = 10 p^3 (1 - p)^2$$

Langkah 2: Samakan kedua persamaan sesuai yang diketahui:
$$10 p^2 (1 - p)^3 = 10 p^3 (1 - p)^2$$

Langkah 3: Karena $0 < p < 1$, bagi kedua ruas dengan $10 p^2 (1 - p)^2$:
$$1 - p = p \implies 2p = 1 \implies p = 0{,}5$$

Langkah 4: Hitung nilai harapan:
$$E(X) = n \cdot p = 5 \cdot 0{,}5 = 2{,}5$$
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b04-f-hard-bt01-003
*orisinal | C6 | 5 langkah | jenis: rekonstruksi nilai harapan dari parameter*

Dalam suatu eksperimen binomial dengan peluang sukses pada setiap percobaan $p = \frac{1}{3}$, diketahui bahwa peluang mendapatkan tepat satu kali sukses bernilai tiga kali dari peluang tidak pernah sukses sama sekali. Nilai harapan banyaknya sukses dalam eksperimen tersebut adalah ....

- **A. $2$** ✅  
  <sub>Benar: $P(X=1) = 3 P(X=0) \implies n\left(\frac{1}{3}\right)\left(\frac{2}{3}\right)^{n-1} = 3\left(\frac{2}{3}\right)^n \implies n\left(\frac{1}{3}\right) = 3\left(\frac{2}{3}\right) = 2 \implies n = 6$. Nilai harapan $E(X) = np = 6 \times \frac{1}{3} = 2$.</sub>
- B. $3$  
  <sub>Salah: Menganggap nilai $n = 9$ karena salah membagi konstanta $3$, sehingga $E(X) = 9 \times \frac{1}{3} = 3$.</sub>
- C. $1$  
  <sub>Salah: Salah menyelesaikan persamaan menjadi $n = 3$, sehingga $E(X) = 3 \times \frac{1}{3} = 1$.</sub>
- D. $6$  
  <sub>Salah: Menjawab banyaknya percobaan $n = 6$ bukan nilai harapannya $E(X)$.</sub>

**Pembahasan:** Langkah 1: Identifikasi peluang sukses dan gagal:
$p = \frac{1}{3}$, $q = 1 - \frac{1}{3} = \frac{2}{3}$.

Langkah 2: Tuliskan formula $P(X = 0)$ dan $P(X = 1)$:
$$P(X = 0) = \binom{n}{0}\left(\frac{1}{3}\right)^0\left(\frac{2}{3}\right)^n = \left(\frac{2}{3}\right)^n$$
$$P(X = 1) = \binom{n}{1}\left(\frac{1}{3}\right)^1\left(\frac{2}{3}\right)^{n - 1} = n \cdot \frac{1}{3} \cdot \left(\frac{2}{3}\right)^{n - 1}$$

Langkah 3: Masukkan ke hubungan yang diketahui $P(X = 1) = 3 \cdot P(X = 0)$:
$$n \cdot \frac{1}{3} \cdot \left(\frac{2}{3}\right)^{n - 1} = 3 \cdot \left(\frac{2}{3}\right)^n$$

Langkah 4: Bagi kedua ruas dengan $\left(\frac{2}{3}\right)^{n - 1}$:
$$\frac{n}{3} = 3 \cdot \frac{2}{3} = 2 \implies n = 6$$

Langkah 5: Hitung nilai harapan:
$$E(X) = n \cdot p = 6 \cdot \frac{1}{3} = 2$$
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b04-f-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: analisis batas kelulusan binomial*

Sebuah ujian singkat terdiri atas $4$ soal pilihan ganda. Setiap soal memiliki $4$ opsi pilihan jawaban dengan tepat $1$ jawaban benar. Seseorang mengerjakan ujian tersebut dengan menebak seluruh jawaban secara acak dan saling bebas. Jika syarat kelulusan adalah menjawab dengan benar paling sedikit $3$ soal, maka peluang orang tersebut tidak lulus adalah ....

- A. $\frac{244}{256}$  
  <sub>Salah: Lupa memperhitungkan kasus $X=4$ saat menghitung peluang lulus sehingga mengurangkan $1 - \frac{12}{256}$.</sub>
- **B. $\frac{243}{256}$** ✅  
  <sub>Benar: Peluang lulus adalah $P(X \ge 3) = P(X=3) + P(X=4) = \binom{4}{3}\left(\frac{1}{4}\right)^3\left(\frac{3}{4}\right)^1 + \binom{4}{4}\left(\frac{1}{4}\right)^4 = \frac{12}{256} + \frac{1}{256} = \frac{13}{256}$. Peluang tidak lulus adalah komplemennya: $1 - \frac{13}{256} = \frac{243}{256}$.</sub>
- C. $\frac{13}{256}$  
  <sub>Salah: Menghitung peluang lulus $P(X \ge 3)$ bukan peluang tidak lulus.</sub>
- D. $\frac{189}{256}$  
  <sub>Salah: Salah menghitung nilai kombinasi $\binom{4}{3}$ menjadi $1$ sehingga memperoleh peluang lulus $\frac{4}{256}$.</sub>

**Pembahasan:** Langkah 1: Menentukan parameter binomial:
$n = 4$, $p = \frac{1}{4}$, $q = 1 - \frac{1}{4} = \frac{3}{4}$.

Langkah 2: Menghitung peluang lulus $P(\text{Lulus}) = P(X \ge 3) = P(X = 3) + P(X = 4)$:
$$P(X = 3) = \binom{4}{3}\left(\frac{1}{4}\right)^3\left(\frac{3}{4}\right)^1 = 4 \cdot \frac{1}{64} \cdot \frac{3}{4} = \frac{12}{256}$$
$$P(X = 4) = \binom{4}{4}\left(\frac{1}{4}\right)^4\left(\frac{3}{4}\right)^0 = 1 \cdot \frac{1}{256} \cdot 1 = \frac{1}{256}$$

Langkah 3: Menjumlahkan peluang lulus:
$$P(\text{Lulus}) = \frac{12 + 1}{256} = \frac{13}{256}$$

Langkah 4: Menghitung peluang tidak lulus menggunakan komplemen:
$$P(\text{Tidak Lulus}) = 1 - P(\text{Lulus}) = 1 - \frac{13}{256} = \frac{243}{256}$$
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b04-f-hard-bt01-005
*variasi (angka) | C5 | 5 langkah | jenis: evaluasi peluang kumulatif majemuk*

Tentukan peluang mendapatkan paling sedikit 5 sisi gambar pada 7 kali pelemparan sekeping uang logam seimbang.

- A. $\frac{7}{32}$  
  <sub>Salah: Hanya menghitung P(X = 5) + P(X = 7) = 22/128 = 11/64 atau salah menjumlahkan koefisien kombinasi menjadi 28/128 = 7/32.</sub>
- B. $\frac{99}{128}$  
  <sub>Salah: Menghitung komplemen 1 - 29/128, yaitu peluang mendapatkan paling banyak 4 sisi gambar.</sub>
- **C. $\frac{29}{128}$** ✅  
  <sub>Benar: Peluang gambar p = 1/2, q = 1/2. P(X >= 5) = P(X=5) + P(X=6) + P(X=7) = (C(7,5) + C(7,6) + C(7,7)) / 128 = (21 + 7 + 1) / 128 = 29/128.</sub>
- D. $\frac{21}{128}$  
  <sub>Salah: Hanya menghitung peluang tepat 5 sisi gambar P(X = 5).</sub>

**Pembahasan:** Pelemparan uang logam seimbang sebanyak $n = 7$ kali memiliki peluang muncul gambar $p = \frac{1}{2}$ dan $q = 1 - p = \frac{1}{2}$.
Kejadian mendapatkan paling sedikit $5$ sisi gambar berarti $X \ge 5$, yaitu $X = 5$, $X = 6$, atau $X = 7$.
1. $P(X = 5) = \binom{7}{5} \left(\frac{1}{2}\right)^5 \left(\frac{1}{2}\right)^2 = 21 \cdot \frac{1}{128} = \frac{21}{128}$
2. $P(X = 6) = \binom{7}{6} \left(\frac{1}{2}\right)^6 \left(\frac{1}{2}\right)^1 = 7 \cdot \frac{1}{128} = \frac{7}{128}$
3. $P(X = 7) = \binom{7}{7} \left(\frac{1}{2}\right)^7 \left(\frac{1}{2}\right)^0 = 1 \cdot \frac{1}{128} = \frac{1}{128}$
Jumlahkan seluruh peluang:
$P(X \ge 5) = \frac{21 + 7 + 1}{128} = \frac{29}{128}$.
**Acuan:** siswa — siswa hal.271 Ayo Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b04-f-hard-bt01-006
*orisinal | C5 | 6 langkah | jenis: komparasi model binomial*

Dua orang siswa, Ahmad dan Budi, melakukan eksperimen peluang. Ahmad melempar $4$ keping uang logam seimbang secara bersamaan dan menang jika memperoleh paling sedikit $3$ sisi gambar. Budi melempar $3$ buah dadu seimbang bersisi enam secara bersamaan dan menang jika memperoleh paling sedikit $2$ mata dadu bernilai genap. Selisih peluang kemenangan Budi terhadap peluang kemenangan Ahmad adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: Mengabaikan kasus kejadian semua dadu genap pada perhitungan peluang kemenangan Budi sehingga diperoleh 3/8 - 5/16 = 1/16 atau salah membagi pecahan.</sub>
- **B. $\frac{3}{16}$** ✅  
  <sub>Benar: Peluang Ahmad menang = P(X >= 3) = (C(4,3)+C(4,4))/16 = 5/16. Peluang Budi menang = P(Y >= 2) = (C(3,2)+C(3,3))/8 = 4/8 = 8/16. Selisih = 8/16 - 5/16 = 3/16.</sub>
- C. $\frac{1}{16}$  
  <sub>Salah: Salah menghitung peluang Ahmad menang menjadi (C(4,2)+C(4,4))/16 = 7/16 sehingga selisihnya 8/16 - 7/16 = 1/16.</sub>
- D. $\frac{5}{16}$  
  <sub>Salah: Hanya menghitung nilai peluang kemenangan Ahmad tanpa mencari selisihnya.</sub>

**Pembahasan:** Untuk Ahmad:
Banyak koin $n = 4$, peluang sisi gambar $p = \frac{1}{2}$.
Ahmad menang jika $X \ge 3$:
$P(X \ge 3) = P(X = 3) + P(X = 4) = \binom{4}{3}\left(\frac{1}{2}\right)^4 + \binom{4}{4}\left(\frac{1}{2}\right)^4 = \frac{4 + 1}{16} = \frac{5}{16}$.

Untuk Budi:
Banyak dadu $n = 3$, peluang mata dadu genap $\{2, 4, 6\}$ adalah $p = \frac{3}{6} = \frac{1}{2}$.
Budi menang jika $Y \ge 2$:
$P(Y \ge 2) = P(Y = 2) + P(Y = 3) = \binom{3}{2}\left(\frac{1}{2}\right)^3 + \binom{3}{3}\left(\frac{1}{2}\right)^3 = \frac{3 + 1}{8} = \frac{4}{8} = \frac{8}{16}$.

Selisih peluang kemenangan Budi terhadap Ahmad:
$P(Y \ge 2) - P(X \ge 3) = \frac{8}{16} - \frac{5}{16} = \frac{3}{16}$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b04-f-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: analisis batas parameter binomial*

Sebuah sistem pengamanan bekerja dengan mengaktifkan $3$ sensor pendeteksi bahaya yang beroperasi secara saling bebas. Setiap sensor memiliki peluang yang sama sebesar $p$ untuk berhasil mendeteksi bahaya. Sistem pengamanan akan menyalakan alarm jika sedikitnya $2$ sensor berhasil mendeteksi bahaya. Nilai peluang keberhasilan setiap sensor ($p$) terkecil agar peluang alarm berbunyi tidak kurang dari $0{,}5$ adalah ....

- **A. $0{,}5$** ✅  
  <sub>Benar: P(X >= 2) = 3p^2(1-p) + p^3 = 3p^2 - 2p^3 >= 0,5 <=> 4p^3 - 6p^2 + 1 <= 0 <=> (2p - 1)(2p^2 - 2p - 1) <= 0. Untuk 0 <= p <= 1, solusi minimum adalah p = 0,5.</sub>
- B. $0{,}33$  
  <sub>Salah: Mengira nilai p minimum diperoleh dari rasio 1 dibagi banyak sensor (1/3).</sub>
- C. $0{,}67$  
  <sub>Salah: Mengira peluang per sensor harus sama dengan ambang batas minimal sensor yang bekerja yaitu 2/3.</sub>
- D. $0{,}75$  
  <sub>Salah: Salah melakukan pemfaktoran pertidaksamaan polinomial pangkat 3.</sub>

**Pembahasan:** Banyaknya sensor $n = 3$, peluang tiap sensor berhasil adalah $p$, dan gagal $1 - p$.
Alarm menyala jika sedikitnya $2$ sensor berhasil ($X \ge 2$):
$P(X \ge 2) = P(X = 2) + P(X = 3)$
$P(X \ge 2) = \binom{3}{2} p^2 (1 - p) + \binom{3}{3} p^3 = 3p^2(1 - p) + p^3 = 3p^2 - 2p^3$.

Syarat agar $P(X \ge 2) \ge 0{,}5$:
$3p^2 - 2p^3 \ge \frac{1}{2}$
$6p^2 - 4p^3 \ge 1$
$4p^3 - 6p^2 + 1 \le 0$

Faktorkan suku banyak tersebut:
Substitusi $p = \frac{1}{2}$: $4\left(\frac{1}{8}\right) - 6\left(\frac{1}{4}\right) + 1 = \frac{1}{2} - \frac{3}{2} + 1 = 0$.
Diperoleh pemfaktoran $(2p - 1)(2p^2 - 2p - 1) \le 0$.
Akar dari $2p^2 - 2p - 1 = 0$ adalah $p = \frac{2 \pm \sqrt{12}}{4} = \frac{1 \pm \sqrt{3}}{2}$, yang berada di luar rentang $0 < p < 1$.
Karena pada interval $[0{,}5; 1]$ nilai $4p^3 - 6p^2 + 1 \le 0$, maka nilai terkecil $p$ yang memenuhi adalah $0{,}5$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b04-f-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: rekonstruksi parameter dari ekspektasi*

Suatu variabel acak $X$ berdistribusi binomial dengan $n$ percobaan saling bebas dan peluang berhasil $p$ pada setiap percobaan (dengan $0 < p < 1$). Diketahui bahwa nilai harapan $E(X) = 3$ dan peluang memperoleh tepat satu keberhasilan adalah $4$ kali peluang tidak memperoleh keberhasilan sama sekali ($P(X = 1) = 4 \cdot P(X = 0)$). Banyaknya percobaan $n$ yang dilakukan adalah ....

- A. $16$  
  <sub>Salah: Mengalikan kuadrat nilai harapan dengan faktor rasio peluang (4 * 4 = 16).</sub>
- B. $9$  
  <sub>Salah: Salah menghitung nilai p menjadi 1/3 sehingga memperoleh n = 3 / (1/3) = 9.</sub>
- C. $15$  
  <sub>Salah: Salah menyelesaikan persamaan aljabar 3/(1-p) = 4 menjadi p = 1/5 sehingga n = 3/(1/5) = 15.</sub>
- **D. $12$** ✅  
  <sub>Benar: P(X=1)/P(X=0) = (n*p*(1-p)^(n-1))/(1-p)^n = np/(1-p) = 4. Karena np = E(X) = 3, maka 3/(1-p) = 4 => 1-p = 3/4 => p = 1/4. Maka n = E(X)/p = 3/(1/4) = 12.</sub>

**Pembahasan:** Rumus fungsi distribusi binomial:
$P(X = x) = \binom{n}{x} p^x (1 - p)^{n - x}$

Maka:
$P(X = 0) = (1 - p)^n$
$P(X = 1) = \binom{n}{1} p^1 (1 - p)^{n - 1} = n p (1 - p)^{n - 1}$

Dari informasi $P(X = 1) = 4 \cdot P(X = 0)$:
$\frac{P(X = 1)}{P(X = 0)} = \frac{n p (1 - p)^{n - 1}}{(1 - p)^n} = \frac{n p}{1 - p} = 4$

Diketahui nilai harapan $E(X) = n p = 3$. Substitusikan ke persamaan:
$\frac{3}{1 - p} = 4$
$1 - p = \frac{3}{4} \implies p = 1 - \frac{3}{4} = \frac{1}{4}$

Banyaknya percobaan $n$:
$n = \frac{E(X)}{p} = \frac{3}{\frac{1}{4}} = 12$.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b04-f-hard-bt01-009
*variasi (konteks) | C5 | 4 langkah | jenis: analisis ketahanan sistem binomial*

Peluang sebuah mesin pemindai dokumen berhasil mendeteksi berkas cacat secara tepat adalah $0{,}7$. Dalam suatu pengujian mutu, dipilih $4$ berkas cacat untuk dipindai secara saling bebas. Peluang bahwa paling sedikit $3$ berkas berhasil dideteksi dengan tepat oleh mesin tersebut adalah ....

- **A. $0{,}6517$** ✅  
  <sub>Benar: $P(X \ge 3) = P(X=3) + P(X=4) = \binom{4}{3}(0{,}7)^3(0{,}3)^1 + \binom{4}{4}(0{,}7)^4(0{,}3)^0 = 4(0{,}343)(0{,}3) + 0{,}2401 = 0{,}4116 + 0{,}2401 = 0{,}6517$.</sub>
- B. $0{,}3483$  
  <sub>Salah: Menghitung komplemen secara keliru sebagai $1 - 0{,}6517$.</sub>
- C. $0{,}4116$  
  <sub>Salah: Hanya menghitung peluang tepat $3$ berkas berhasil terdeteksi ($P(X = 3)$).</sub>
- D. $0{,}2401$  
  <sub>Salah: Hanya menghitung peluang seluruh berkas ($4$ berkas) berhasil terdeteksi ($P(X = 4)$).</sub>

**Pembahasan:** Langkah 1: Tentukan parameter distribusi binomial: $n = 4$, $p = 0{,}7$, dan $q = 1 - 0{,}7 = 0{,}3$.
Langkah 2: Kejadian paling sedikit $3$ berkas terdeteksi berarti $X \ge 3$, yaitu $X = 3$ atau $X = 4$.
Langkah 3: Hitung probabilitas masing-masing kejadian:
$P(X = 3) = \binom{4}{3} (0{,}7)^3 (0{,}3)^1 = 4 \times 0{,}343 \times 0{,}3 = 0{,}4116$
$P(X = 4) = \binom{4}{4} (0{,}7)^4 (0{,}3)^0 = 1 \times 0{,}2401 \times 1 = 0{,}2401$
Langkah 4: Jumlahkan kedua probabilitas:
$P(X \ge 3) = 0{,}4116 + 0{,}2401 = 0{,}6517$.
**Acuan:** pretest — kelas12_tl-b04-p0280-latihan-soal-distribusi-binomial-5c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b04-f-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: rekonstruksi nilai harapan binomial*

Suatu variabel acak $X$ berdistribusi binomial dengan banyaknya percobaan $n = 6$ dan peluang sukses pada setiap percobaan $p$ (dengan $0 < p < 1$). Jika diketahui peluang terjadinya tepat $1$ kali sukses sama dengan peluang terjadinya tepat $2$ kali sukses, nilai harapan $E(X)$ dari variabel acak tersebut adalah ....

- A. $\frac{2}{7}$  
  <sub>Salah: Hanya menghitung nilai parameter peluang sukses $p$, lupa mengalikan dengan $n$ untuk mencari nilai harapan.</sub>
- B. $\frac{15}{7}$  
  <sub>Salah: Keliru menggunakan koefisien kombinasi pada pembilang nilai harapan.</sub>
- **C. $\frac{12}{7}$** ✅  
  <sub>Benar: Persamaan $P(X = 1) = P(X = 2)$ menghasilkan $6p(1-p)^5 = 15p^2(1-p)^4$. Penyederhanaan menghasilkan $2(1-p) = 5p \implies 7p = 2 \implies p = \frac{2}{7}$. Nilai harapan $E(X) = n p = 6 \times \frac{2}{7} = \frac{12}{7}$.</sub>
- D. $4$  
  <sub>Salah: Salah menyelesaikan persamaan linear $2(1-p) = 5p$ menjadi $2 = 3p \implies p = \frac{2}{3}$ sehingga $E(X) = 6 \times \frac{2}{3} = 4$.</sub>

**Pembahasan:** Langkah 1: Tuliskan rumus peluang binomial untuk $X = 1$ dan $X = 2$ dengan $n = 6$:
$P(X = 1) = \binom{6}{1} p^1 (1-p)^5 = 6p(1-p)^5$
$P(X = 2) = \binom{6}{2} p^2 (1-p)^4 = 15p^2(1-p)^4$
Langkah 2: Samakan kedua nilai peluang sesuai yang diketahui pada soal:
$6p(1-p)^5 = 15p^2(1-p)^4$
Langkah 3: Karena $0 < p < 1$, bagi kedua ruas dengan $3p(1-p)^4$:
$2(1-p) = 5p$
Langkah 4: Selesaikan persamaan untuk memperoleh $p$:
$2 - 2p = 5p \implies 7p = 2 \implies p = \frac{2}{7}$
Langkah 5: Hitung nilai harapan $E(X)$:
$E(X) = n \cdot p = 6 \cdot \frac{2}{7} = \frac{12}{7}$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b04-f-hard-bt01-011
*variasi (konteks) | C5 | 4 langkah | jenis: penentuan nilai harapan dari kumulatif*

Seorang teknisi menguji $5$ unit perangkat sensor yang bekerja secara saling bebas. Setiap perangkat memiliki peluang keberhasilan fungsi yang sama sebesar $p$. Jika peluang paling sedikit satu perangkat berfungsi dengan baik adalah $\frac{242}{243}$, nilai harapan banyaknya perangkat yang berfungsi dengan baik adalah ....

- A. $\frac{8}{3}$  
  <sub>Salah: Siswa keliru menghitung nilai $n = 4$ padahal terdapat $5$ unit perangkat yang diuji.</sub>
- B. $\frac{5}{2}$  
  <sub>Salah: Siswa mengasumsikan peluang keberhasilan setiap perangkat netral ($p = 0{,}5$) tanpa memanfaatkan informasi peluang kumulatif.</sub>
- **C. $\frac{10}{3}$** ✅  
  <sub>Benar: Peluang paling sedikit 1 berfungsi adalah $P(X \ge 1) = 1 - P(X = 0) = 1 - (1 - p)^5 = \frac{242}{243}$. Diperoleh $(1 - p)^5 = \frac{1}{243} = \left(\frac{1}{3}\right)^5$, sehingga $1 - p = \frac{1}{3}$ atau $p = \frac{2}{3}$. Maka nilai harapan $E(X) = n \cdot p = 5 \cdot \frac{2}{3} = \frac{10}{3}$.</sub>
- D. $\frac{5}{3}$  
  <sub>Salah: Siswa keliru mengalikan $n$ dengan peluang kegagalan $q = \frac{1}{3}$, bukan peluang sukses $p$.</sub>

**Pembahasan:** Misalkan $X$ menyatakan banyaknya perangkat yang berfungsi dengan baik, maka $X \sim B(5, p)$.
Diketahui:
$$P(X \ge 1) = \frac{242}{243}$$
$$1 - P(X = 0) = \frac{242}{243}$$
$$1 - \binom{5}{0} p^0 (1-p)^5 = \frac{242}{243}$$
$$(1-p)^5 = 1 - \frac{242}{243} = \frac{1}{243}$$
$$1 - p = \frac{1}{3} \implies p = 1 - \frac{1}{3} = \frac{2}{3}$$
Nilai harapan banyaknya perangkat yang berfungsi baik adalah:
$$E(X) = n \cdot p = 5 \cdot \frac{2}{3} = \frac{10}{3}$$
**Acuan:** pretest — kelas12_tl-b04-p0280-latihan-soal-distribusi-binomial-5c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b04-f-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: analisis fungsi skor linier binomial*

Sebuah ujian singkat memuat $4$ butir soal pilihan ganda dengan $5$ opsi jawaban (tepat $1$ opsi benar per soal). Seorang siswa menjawab seluruh soal murni dengan cara menebak secara acak dan bebas. Aturan penilaian memberikan skor $+4$ untuk setiap jawaban benar dan denda skor $-1$ untuk setiap jawaban salah (tidak ada soal yang dikosongkan). Jika $Y$ adalah skor total yang diperoleh siswa tersebut, nilai harapan skor $E(Y)$ dan peluang siswa memperoleh skor total lebih dari $0$ berturut-turut adalah ....

- **A. $0$ dan $\frac{369}{625}$** ✅  
  <sub>Benar: Banyaknya jawaban benar $X \sim B(4, \frac{1}{5})$. Skor $Y = 4X - 1(4 - X) = 5X - 4$. Nilai harapan $E(X) = 4 \cdot \frac{1}{5} = \frac{4}{5}$, sehingga $E(Y) = 5E(X) - 4 = 5(\frac{4}{5}) - 4 = 0$. Syarat skor $Y > 0 \iff 5X - 4 > 0 \iff X > \frac{4}{5} \iff X \ge 1$. Peluang $P(X \ge 1) = 1 - P(X = 0) = 1 - (\frac{4}{5})^4 = 1 - \frac{256}{625} = \frac{369}{625}$.</sub>
- B. $\frac{4}{5}$ dan $\frac{369}{625}$  
  <sub>Salah: Siswa keliru menganggap nilai harapan skor total sama dengan nilai harapan banyak soal benar $E(X) = \frac{4}{5}$.</sub>
- C. $0$ dan $\frac{1}{5}$  
  <sub>Salah: Siswa salah mengira bahwa peluang memperoleh skor positif hanya diwakili oleh peluang menebak satu soal dengan benar.</sub>
- D. $0$ dan $\frac{256}{625}$  
  <sub>Salah: Siswa menghitung peluang mendapatkan skor tidak positif $P(X = 0) = \left(\frac{4}{5}\right)^4 = \frac{256}{625}$.</sub>

**Pembahasan:** Misalkan $X$ adalah banyaknya jawaban benar. Karena setiap soal memiliki 5 opsi dan ditebak acak, maka $X \sim B\left(4, \frac{1}{5}\right)$.
Banyaknya jawaban salah adalah $4 - X$.
Fungsi skor total $Y$ adalah:
$$Y = 4X - 1(4 - X) = 5X - 4$$
1. Menghitung nilai harapan $E(Y)$:
$$E(X) = n \cdot p = 4 \cdot \frac{1}{5} = \frac{4}{5}$$
$$E(Y) = E(5X - 4) = 5 \cdot E(X) - 4 = 5 \left(\frac{4}{5}\right) - 4 = 4 - 4 = 0$$
2. Menghitung peluang $P(Y > 0)$:
$$Y > 0 \iff 5X - 4 > 0 \iff X > \frac{4}{5}$$
Karena $X$ bilangan cacah, $X > \frac{4}{5}$ setara dengan $X \ge 1$.
$$P(Y > 0) = P(X \ge 1) = 1 - P(X = 0)$$
$$P(X = 0) = \binom{4}{0} \left(\frac{1}{5}\right)^0 \left(\frac{4}{5}\right)^4 = 1 \times 1 \times \frac{256}{625} = \frac{256}{625}$$
$$P(Y > 0) = 1 - \frac{256}{625} = \frac{369}{625}$$
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b04-f-hard-bt01-013
*variasi (konteks) | C5 | 5 langkah | jenis: komparasi keandalan sistem binomial*

Sebuah perangkat kendali dapat dirancang dengan dua konfigurasi sistem yang bekerja secara independen:
- Sistem A menggunakan $4$ komponen dengan peluang masing-masing komponen berfungsi normal sebesar $0{,}8$. Sistem A akan berfungsi jika minimal $3$ komponen bekerja normal.
- Sistem B menggunakan $3$ komponen berkualitas tinggi dengan peluang masing-masing komponen berfungsi normal sebesar $0{,}9$. Sistem B akan berfungsi jika minimal $2$ komponen bekerja normal.

Berdasarkan evaluasi keandalan menggunakan distribusi binomial, sistem manakah yang memiliki peluang berfungsi lebih tinggi dan berapakah selisih peluang di antara kedua konfigurasi tersebut?

- A. Sistem A, dengan selisih peluang sebesar $0{,}1528$  
  <sub>Salah: Tertukar dalam membandingkan nilai akhir $0{,}8192$ dan $0{,}972$ sehingga keliru menyimpulkan Sistem A lebih besar.</sub>
- B. Sistem B, dengan selisih peluang sebesar $0{,}0704$  
  <sub>Salah: Hanya menghitung peluang tepat memenuhi batas minimum ($P(X=3) = 0{,}4096$ dan $P(Y=2) = 0{,}243$) atau salah mengurangi komponen peluang sempurna.</sub>
- C. Sistem B, dengan selisih peluang sebesar $0{,}1704$  
  <sub>Salah: Kesalahan aritmetika saat menghitung $P(X=4)$ sebagai $(0{,}8)^4 = 0{,}392$ bukan $0{,}4096$.</sub>
- **D. Sistem B, dengan selisih peluang sebesar $0{,}1528$** ✅  
  <sub>Benar: Peluang beroperasinya Sistem A adalah $P(X \ge 3) = P(X=3) + P(X=4) = \binom{4}{3}(0{,}8)^3(0{,}2)^1 + \binom{4}{4}(0{,}8)^4 = 4(0{,}512)(0{,}2) + 0{,}4096 = 0{,}4096 + 0{,}4096 = 0{,}8192$. Peluang beroperasinya Sistem B adalah $P(Y \ge 2) = P(Y=2) + P(Y=3) = \binom{3}{2}(0{,}9)^2(0{,}1)^1 + \binom{3}{3}(0{,}9)^3 = 3(0{,}81)(0{,}1) + 0{,}729 = 0{,}243 + 0{,}729 = 0{,}972$. Dengan demikian, Sistem B memiliki keandalan lebih tinggi dengan selisih peluang $0{,}972 - 0{,}8192 = 0{,}1528$.</sub>

**Pembahasan:** Langkah 1 (Peluang Sistem A):
Variabel acak $X \sim \text{Binomial}(n=4, p=0{,}8)$. Sistem A berfungsi jika $X \ge 3$.
$P(X = 3) = \binom{4}{3}(0{,}8)^3(0{,}2)^1 = 4(0{,}512)(0{,}2) = 0{,}4096$
$P(X = 4) = \binom{4}{4}(0{,}8)^4(0{,}2)^0 = 1(0{,}4096)(1) = 0{,}4096$
$P(X \ge 3) = 0{,}4096 + 0{,}4096 = 0{,}8192$.

Langkah 2 (Peluang Sistem B):
Variabel acak $Y \sim \text{Binomial}(n=3, p=0{,}9)$. Sistem B berfungsi jika $Y \ge 2$.
$P(Y = 2) = \binom{3}{2}(0{,}9)^2(0{,}1)^1 = 3(0{,}81)(0{,}1) = 0{,}243$
$P(Y = 3) = \binom{3}{3}(0{,}9)^3(0{,}1)^0 = 1(0{,}729)(1) = 0{,}729$
$P(Y \ge 2) = 0{,}243 + 0{,}729 = 0{,}972$.

Langkah 3 (Komparasi dan Selisih):
Karena $0{,}972 > 0{,}8192$, maka Sistem B memiliki peluang berfungsi lebih tinggi.
Selisih peluangnya adalah:
$P(Y \ge 2) - P(X \ge 3) = 0{,}972 - 0{,}8192 = 0{,}1528$.
**Acuan:** pretest — kelas12_tl-b04-p0280-latihan-soal-distribusi-binomial-5b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b04-f-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: penentuan parameter rasio peluang*

Suatu variabel acak $X$ berdistribusi binomial dengan banyaknya percobaan $n = 5$ dan peluang sukses pada setiap percobaan $p$ (dengan $0 < p < 1$). Jika diketahui bahwa peluang memperoleh tepat $3$ kali sukses bernilai dua kali lipat dari peluang memperoleh tepat $2$ kali sukses, yaitu $P(X = 3) = 2 \cdot P(X = 2)$, maka nilai dari $P(X \ge 4)$ adalah ....

- A. $\frac{11}{243}$  
  <sub>Salah: Tertukar saat menyelesaikan perbandingan aljabar sehingga memperoleh $p = \frac{1}{3}$, lalu menghitung $P(X \ge 4) = \frac{10 + 1}{243} = \frac{11}{243}$.</sub>
- B. $\frac{80}{243}$  
  <sub>Salah: Hanya menghitung nilai $P(X = 4)$ dan lupa menambahkan $P(X = 5)$ untuk kondisi $P(X \ge 4)$.</sub>
- C. $\frac{131}{243}$  
  <sub>Salah: Keliru menganggap koefisien kombinasi $\binom{5}{4}$ adalah $10$ sehingga menghitung $(10 \times 16 + 32)/243$.</sub>
- **D. $\frac{112}{243}$** ✅  
  <sub>Benar: Dari $P(X = 3) = 2 \cdot P(X = 2)$, diperoleh $\binom{5}{3} p^3 (1-p)^2 = 2 \binom{5}{2} p^2 (1-p)^3$. Karena $\binom{5}{3} = \binom{5}{2} = 10$, persamaan tereduksi menjadi $p = 2(1-p) \implies 3p = 2 \implies p = \frac{2}{3}$. Maka $P(X \ge 4) = P(X = 4) + P(X = 5) = \binom{5}{4}\left(\frac{2}{3}\right)^4\left(\frac{1}{3}\right)^1 + \binom{5}{5}\left(\frac{2}{3}\right)^5 = 5\left(\frac{16}{243}\right) + \frac{32}{243} = \frac{80 + 32}{243} = \frac{112}{243}$.</sub>

**Pembahasan:** Langkah 1: Gunakan rumus fungsi peluang binomial $b(x; n, p) = \binom{n}{x} p^x (1-p)^{n-x}$.
$P(X = 3) = \binom{5}{3} p^3 (1-p)^2 = 10 p^3 (1-p)^2$
$P(X = 2) = \binom{5}{2} p^2 (1-p)^3 = 10 p^2 (1-p)^3$

Langkah 2: Substitusikan ke dalam persamaan $P(X = 3) = 2 \cdot P(X = 2)$:
$10 p^3 (1-p)^2 = 2 \cdot 10 p^2 (1-p)^3$
Bagi kedua ruas dengan $10 p^2 (1-p)^2$ (karena $0 < p < 1$):
$p = 2(1 - p)$
$p = 2 - 2p \implies 3p = 2 \implies p = \frac{2}{3}$
Maka $q = 1 - p = \frac{1}{3}$.

Langkah 3: Hitung $P(X = 4)$:
$P(X = 4) = \binom{5}{4} \left(\frac{2}{3}\right)^4 \left(\frac{1}{3}\right)^1 = 5 \cdot \frac{16}{81} \cdot \frac{1}{3} = \frac{80}{243}$.

Langkah 4: Hitung $P(X = 5)$:
$P(X = 5) = \binom{5}{5} \left(\frac{2}{3}\right)^5 \left(\frac{1}{3}\right)^0 = 1 \cdot \frac{32}{243} \cdot 1 = \frac{32}{243}$.

Langkah 5: Jumlahkan untuk mendapatkan $P(X \ge 4)$:
$P(X \ge 4) = P(X = 4) + P(X = 5) = \frac{80}{243} + \frac{32}{243} = \frac{112}{243}$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b04-f-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: perancangan kapasitas batas binomial*

Dalam suatu sistem pemantauan lalu lintas data jaringan, setiap paket data yang lewat memiliki peluang independen $p = 0{,}2$ memicu alarm peringatan palsu. Suatu siklus pemeriksaan dinyatakan aman jika peluang munculnya paling sedikit satu alarm peringatan palsu tidak melebihi $0{,}6$. Berapakah banyak paket data maksimum ($n$) yang boleh diperiksa dalam satu siklus agar sistem tetap memenuhi kriteria aman tersebut?

- A. $3$  
  <sub>Salah: Berhenti menghitung terlalu awal karena mengira $(0{,}8)^4$ sudah kurang dari $0{,}4$.</sub>
- B. $2$  
  <sub>Salah: Salah menggunakan pendekatan linier ekspektasi $n \cdot p \le 0{,}6 \implies n \le 3$, lalu mengurangi satu karena ragu.</sub>
- **C. $4$** ✅  
  <sub>Benar: Peluang muncul paling sedikit satu peringatan palsu adalah $P(X \ge 1) = 1 - P(X = 0) = 1 - (1 - 0{,}2)^n = 1 - (0{,}8)^n$. Syarat aman adalah $P(X \ge 1) \le 0{,}6 \iff 1 - (0{,}8)^n \le 0{,}6 \iff (0{,}8)^n \ge 0{,}4$. Evaluasi nilai $(0{,}8)^n$: untuk $n=1$, $(0{,}8)^1 = 0{,}8$; untuk $n=2$, $(0{,}8)^2 = 0{,}64$; untuk $n=3$, $(0{,}8)^3 = 0{,}512$; untuk $n=4$, $(0{,}8)^4 = 0{,}4096 \ge 0{,}4$; untuk $n=5$, $(0{,}8)^5 = 0{,}32768 < 0{,}4$. Jadi nilai $n$ maksimum adalah $4$.</sub>
- D. $5$  
  <sub>Salah: Memilih nilai pertama saat peluang melebihi batas $0{,}6$ bukannya nilai maksimum yang masih memenuhi syarat tidak melebihi $0{,}6$.</sub>

**Pembahasan:** Langkah 1: Definisikan variabel acak $X$ sebagai banyaknya alarm palsu yang muncul dari $n$ paket data, sehingga $X \sim \text{Binomial}(n, p=0{,}2)$. Peluang komplemen (tidak ada alarm palsu sama sekali) adalah $P(X = 0) = (1 - 0{,}2)^n = (0{,}8)^n$.

Langkah 2: Tuliskan peluang terjadinya paling sedikit satu alarm palsu:
$P(X \ge 1) = 1 - P(X = 0) = 1 - (0{,}8)^n$.

Langkah 3: Terapkan syarat bahwa peluang ini tidak boleh melebihi $0{,}6$:
$1 - (0{,}8)^n \le 0{,}6$
$-(0{,}8)^n \le -0{,}4$
$(0{,}8)^n \ge 0{,}4$.

Langkah 4: Evaluasi nilai $(0{,}8)^n$ untuk $n$ bilangan bulat positif:
- $n = 1 \implies (0{,}8)^1 = 0{,}8 \ge 0{,}4$ (memenuhi, $P(X \ge 1) = 0{,}20$)
- $n = 2 \implies (0{,}8)^2 = 0{,}64 \ge 0{,}4$ (memenuhi, $P(X \ge 1) = 0{,}36$)
- $n = 3 \implies (0{,}8)^3 = 0{,}512 \ge 0{,}4$ (memenuhi, $P(X \ge 1) = 0{,}488$)
- $n = 4 \implies (0{,}8)^4 = 0{,}4096 \ge 0{,}4$ (memenuhi, $P(X \ge 1) = 0{,}5904 \le 0{,}6$)
- $n = 5 \implies (0{,}8)^5 = 0{,}32768 < 0{,}4$ (tidak memenuhi, $P(X \ge 1) = 0{,}67232 > 0{,}6$)

Dengan demikian, banyak paket data maksimum yang boleh diperiksa adalah $n = 4$.
**Acuan:** siswa — siswa hal.270

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b04-f-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: optimasi fungsi peluang binomial*

Dalam suatu eksperimen binomial dengan variabel acak $X \sim B(4, p)$ di mana $p \in (0, 1)$, seorang pengamat ingin mengetahui kondisi ketika peluang mendapatkan tepat $2$ kali sukses mencapai nilai paling maksimum. Nilai peluang maksimum $P(X = 2)$ tersebut adalah ....

- A. $\frac{5}{16}$  
  <sub>Salah: Menggunakan nilai $p = \frac{1}{4}$ atau salah menjumlahkan pangkat pada ekspresi peluang.</sub>
- **B. $\frac{3}{8}$** ✅  
  <sub>Benar: Peluang $P(X=2) = 6p^2(1-p)^2$ mencapai nilai maksimum saat $p = \frac{1}{2}$, yang menghasilkan nilai peluang $\frac{3}{8}$.</sub>
- C. $\frac{1}{2}$  
  <sub>Salah: Mengira nilai peluang maksimum sama dengan nilai parameter $p = \frac{1}{2}$ yang memaksimumkannya.</sub>
- D. $\frac{1}{4}$  
  <sub>Salah: Salah menghitung koefisien binomial $\binom{4}{2}$ menjadi $4$ alih-alih $6$.</sub>

**Pembahasan:** Berdasarkan definisi fungsi distribusi binomial, peluang terjadinya tepat $2$ kali sukses dari $n = 4$ percobaan adalah:
$P(X = 2) = \binom{4}{2} p^2 (1 - p)^{4-2} = 6 p^2 (1 - p)^2 = 6 [p(1 - p)]^2$

Untuk memaksimumkan fungsi tersebut terhadap $p \in (0, 1)$, kita tinjau fungsi kuadrat $f(p) = p(1 - p) = p - p^2$.
Fungsi kuadrat ini terbuka ke bawah dan mencapai puncak maksimum saat:
$p = -\frac{b}{2a} = -\frac{1}{2(-1)} = \frac{1}{2}$

Karena $p = \frac{1}{2}$ memaksimumkan $f(p)$, maka $[f(p)]^2$ juga mencapai nilai maksimum pada $p = \frac{1}{2}$.
Nilai peluang maksimumnya adalah:
$P(X = 2) = 6 \left(\frac{1}{2}\right)^2 \left(1 - \frac{1}{2}\right)^2 = 6 \cdot \frac{1}{4} \cdot \frac{1}{4} = \frac{6}{16} = \frac{3}{8}$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b04-f-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: rekonstruksi linear nilai harapan binomial*

Dua variabel acak binomial independen $X$ dan $Y$ masing-masing memenuhi $X \sim B(n, p)$ dan $Y \sim B(2n, 1-p)$, dengan $n$ bilangan bulat positif dan $0 < p < 1$. Jika diketahui peluang tidak diperoleh kesuksesan sama sekali pada $X$ adalah $P(X = 0) = \left(\frac{2}{3}\right)^n$ dan selisih nilai harapan keduanya adalah $E(Y) - E(X) = 6$, maka nilai dari $E(X + Y)$ adalah ....

- **A. $10$** ✅  
  <sub>Benar: Menemukan $p = \frac{1}{3}$ dari peluang nol sukses, menyelesaikan $n = 6$ dari selisih nilai harapan, dan menghitung $E(X+Y) = 2 + 8 = 10$.</sub>
- B. $12$  
  <sub>Salah: Keliru menganggap kedua variabel memiliki banyak percobaan yang sama yaitu $2n$.</sub>
- C. $6$  
  <sub>Salah: Mengira nilai harapan jumlah sama dengan nilai selisih $E(Y) - E(X)$.</sub>
- D. $8$  
  <sub>Salah: Hanya menghitung nilai harapan $E(Y)$ tanpa menambahkan $E(X)$.</sub>

**Pembahasan:** Langkah 1: Tentukan nilai parameter $p$.
Diketahui $P(X = 0) = \binom{n}{0} p^0 (1 - p)^n = (1 - p)^n$.
Karena $(1 - p)^n = \left(\frac{2}{3}\right)^n$, maka:
$1 - p = \frac{2}{3} \implies p = 1 - \frac{2}{3} = \frac{1}{3}$

Langkah 2: Tentukan rumus nilai harapan masing-masing variabel.
$E(X) = n \cdot p = \frac{n}{3}$
$E(Y) = 2n \cdot (1 - p) = 2n \cdot \frac{2}{3} = \frac{4n}{3}$

Langkah 3: Gunakan informasi selisih nilai harapan untuk mencari $n$.
$E(Y) - E(X) = 6$
$\frac{4n}{3} - \frac{n}{3} = 6 \implies \frac{3n}{3} = 6 \implies n = 6$

Langkah 4: Hitung nilai dari $E(X + Y)$.
$E(X) = \frac{6}{3} = 2$
$E(Y) = \frac{4(6)}{3} = 8$
$E(X + Y) = E(X) + E(Y) = 2 + 8 = 10$.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b04-f-hard-bt01-018
*orisinal | C5 | 3 langkah | jenis: analisis ambang batas keputusan binomial*

Sebuah sistem pengamanan darurat dilengkapi dengan $5$ sensor gas independen. Pada saat terjadi kebocoran gas, setiap sensor memiliki peluang mendeteksi bahaya sebesar $0{,}6$. Sistem lama membunyikan alarm jika paling sedikit $3$ sensor mendeteksi gas. Pihak teknisi ingin mengubah ambang batas aktivasi sehingga alarm hanya berbunyi jika paling sedikit $4$ sensor mendeteksi gas. Penurunan peluang berbunyinya alarm setelah perubahan ambang batas tersebut dilakukan adalah ....

- A. $0{,}2304$  
  <sub>Salah: Keliru menghitung selisih sebagai nilai peluang tepat $4$ sensor mendeteksi gas $P(X=4)$.</sub>
- B. $0{,}33696$  
  <sub>Salah: Menghitung peluang alarm berbunyi pada sistem baru $P(X \ge 4)$ bukan selisih penurunannya.</sub>
- C. $0{,}68256$  
  <sub>Salah: Menghitung peluang alarm berbunyi pada sistem lama $P(X \ge 3)$ bukan penurunannya.</sub>
- **D. $0{,}3456$** ✅  
  <sub>Benar: Penurunan peluang ekuivalen tepat dengan $P(X = 3)$, yaitu $\binom{5}{3} (0{,}6)^3 (0{,}4)^2 = 0{,}3456$.</sub>

**Pembahasan:** Misalkan $X$ adalah banyaknya sensor yang berhasil mendeteksi gas, maka $X \sim B(5;\, 0{,}6)$ dengan $q = 1 - 0{,}6 = 0{,}4$.

Peluang alarm berbunyi pada sistem lama: $P_{\text{lama}} = P(X \ge 3) = P(X = 3) + P(X = 4) + P(X = 5)$.
Peluang alarm berbunyi pada sistem baru: $P_{\text{baru}} = P(X \ge 4) = P(X = 4) + P(X = 5)$.

Penurunan peluang berbunyinya alarm adalah:
$\Delta P = P_{\text{lama}} - P_{\text{baru}} = [P(X = 3) + P(X = 4) + P(X = 5)] - [P(X = 4) + P(X = 5)] = P(X = 3)$

Maka kita cukup menghitung peluang tepat $3$ sensor mendeteksi gas:
$P(X = 3) = \binom{5}{3} (0{,}6)^3 (0{,}4)^{5-3}$
$P(X = 3) = 10 \cdot (0{,}216) \cdot (0{,}16)$
$P(X = 3) = 10 \cdot 0{,}03456 = 0{,}3456$.

Jadi, penurunan peluang berbunyinya alarm adalah $0{,}3456$.
**Acuan:** siswa — siswa hal.272

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
