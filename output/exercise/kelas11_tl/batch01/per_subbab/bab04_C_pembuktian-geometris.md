# Lembar koreksi — kelas11_tl SMA11L-B4 subbab C: Pembuktian Geometris

48 soal | easy 20, medium 17, hard 11 | variasi 18, orisinal 30
> **Kapasitas kurang (medium): 17 dari kuota 20** — Medium Pembuktian Geometris tipis: acuan teks terbaca habis di easy (Latihan C no.1,2,4, Contoh/MM 4.17 sudah dipakai 2x); Latihan C no.3,5,6 dan Contoh/MM 4.16 bergantung gambar; soal pembuktian panjang tidak bisa jadi pilihan ganda. 17 soal layak tanpa kembar dengan easy.
> **Kapasitas kurang (hard): 11 dari kuota 20** — Hard Pembuktian Geometris sangat tipis: acuan teks terbaca habis di easy/medium dan soal pembuktian terbuka tidak bisa jadi pilihan ganda. 11 soal evaluasi klaim/penyangkal/temuan kesalahan/syarat parameter yang layak tanpa kembar; sisanya hanya hitung langsung sehingga dibuang.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b04-c-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: segitiga siku-siku dari hasil kali titik*

Pada segitiga $PQR$ diketahui $\overrightarrow{PQ} = \langle 4, -2\rangle$ dan $\overrightarrow{PR} = \langle 5, 10\rangle$. Segitiga $PQR$ siku-siku di titik ....

- **A. $P$** ✅  
  <sub>Benar: $\overrightarrow{PQ}\cdot\overrightarrow{PR} = 4\cdot 5 + (-2)\cdot 10 = 0$, jadi kedua sisi di $P$ saling tegak lurus</sub>
- B. $R$  
  <sub>Salah: mengira sudut siku-siku di ujung vektor $\overrightarrow{PR}$</sub>
- C. tidak ada titik sudut yang siku-siku  
  <sub>Salah: salah menghitung hasil kali titik sehingga tidak bernilai nol</sub>
- D. $Q$  
  <sub>Salah: mengira sudut siku-siku di ujung vektor $\overrightarrow{PQ}$ padahal hasil kali titik dihitung di $P$</sub>

**Pembahasan:** $\overrightarrow{PQ}\cdot\overrightarrow{PR} = 20 - 20 = 0$, maka sudut di $P$ siku-siku.
**Acuan:** siswa — siswa hal.210 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b04-c-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: segitiga siku-siku dari hasil kali titik*

Pada segitiga $PQR$ diketahui $\overrightarrow{PQ} = \langle 7, 2\rangle$ dan $\overrightarrow{QR} = \langle -4, 14\rangle$. Pernyataan yang benar tentang $\overrightarrow{PQ}\cdot\overrightarrow{QR}$ dan segitiga $PQR$ adalah ....

- A. hasilnya 0, sehingga siku-siku di $P$  
  <sub>Salah: salah menentukan titik pertemuan kedua vektor</sub>
- **B. hasilnya 0, sehingga siku-siku di $Q$** ✅  
  <sub>Benar: $7\cdot(-4) + 2\cdot 14 = -28 + 28 = 0$; vektor $\overrightarrow{PQ}$ dan $\overrightarrow{QR}$ bertemu di $Q$</sub>
- C. hasilnya 56, sehingga tidak siku-siku  
  <sub>Salah: mengabaikan tanda negatif $-28$ sehingga menjumlahkan 28 + 28</sub>
- D. hasilnya 0, sehingga siku-siku di $R$  
  <sub>Salah: salah menentukan titik pertemuan kedua vektor</sub>

**Pembahasan:** $\overrightarrow{PQ}\cdot\overrightarrow{QR} = -28 + 28 = 0$, sudut antara kedua vektor siku-siku (di $Q$).
**Acuan:** siswa — siswa hal.210 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b04-c-easy-bt01-003
*variasi (konteks) | C1 | 1 langkah | jenis: sifat diagonal belah ketupat*

Pernyataan yang benar mengenai diagonal sebuah belah ketupat yang bukan persegi adalah ....

- **A. saling membagi dua sama panjang dan saling tegak lurus** ✅  
  <sub>Benar: diagonal belah ketupat berpotongan di titik tengah masing-masing dan tegak lurus, tetapi panjangnya berbeda</sub>
- B. saling tegak lurus tetapi tidak saling membagi dua sama panjang  
  <sub>Salah: mencampur dengan sifat diagonal layang-layang</sub>
- C. sama panjang tetapi tidak saling tegak lurus  
  <sub>Salah: mencampur dengan sifat diagonal persegi panjang</sub>
- D. sama panjang dan saling tegak lurus  
  <sub>Salah: mengira diagonal belah ketupat sama panjang (itu sifat persegi)</sub>

**Pembahasan:** Belah ketupat adalah jajargenjang, sehingga diagonalnya saling membagi dua; keempat sisi sama sehingga diagonal tegak lurus; panjang diagonal tidak sama bila bukan persegi.
**Acuan:** siswa — siswa hal.210 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b04-c-easy-bt01-004
*variasi (konteks) | C1 | 1 langkah | jenis: sifat diagonal layang-layang*

Sebuah layang-layang bukan belah ketupat. Sifat diagonalnya yang selalu benar adalah ....

- A. kedua diagonal saling membagi dua sama panjang  
  <sub>Salah: menganggap layang-layang seperti jajargenjang</sub>
- B. kedua diagonal sejajar  
  <sub>Salah: diagonal selalu berpotongan, tidak mungkin sejajar</sub>
- C. kedua diagonal sama panjang  
  <sub>Salah: mengira diagonal layang-layang sama panjang</sub>
- **D. kedua diagonal saling tegak lurus** ✅  
  <sub>Benar: pada layang-layang yang bukan belah ketupat hanya sifat tegak lurus yang selalu berlaku</sub>

**Pembahasan:** Layang-layang: diagonal simetri membagi diagonal lain secara tegak lurus; hanya satu diagonal yang terbagi dua, panjang diagonal berbeda.
**Acuan:** siswa — siswa hal.210 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b04-c-easy-bt01-005
*variasi (konteks) | C2 | 2 langkah | jenis: titik potong diagonal jajargenjang*

Diagonal $AC$ dan $BD$ pada jajargenjang $ABCD$ berpotongan di titik $E$. Jika $A(1, 0)$ dan $E(3, 4)$, koordinat titik $C$ adalah ....

- **A. $(5, 8)$** ✅  
  <sub>Benar: diagonal jajargenjang saling membagi dua sehingga $E$ titik tengah $AC$: $C = 2E - A = (6-1, 8-0)$</sub>
- B. $(2, 4)$  
  <sub>Salah: menghitung $E - A$ saja</sub>
- C. $(4, 4)$  
  <sub>Salah: menjumlahkan $A + E$</sub>
- D. $(6, 8)$  
  <sub>Salah: menghitung $2E$ tanpa mengurangi $A$</sub>

**Pembahasan:** $E$ titik tengah $AC$, maka $C = 2E - A = (5, 8)$.
**Acuan:** siswa — siswa hal.207 Contoh 4.17

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b04-c-easy-bt01-006
*variasi (konteks) | C2 | 1 langkah | jenis: langkah pembuktian diagonal jajargenjang*

Pada jajargenjang $ABCD$, titik $E$ adalah titik tengah $AC$ dan titik $F$ adalah titik tengah $BD$. Agar terbukti bahwa kedua diagonal saling membagi dua sama panjang, kesamaan yang harus ditunjukkan adalah ....

- A. $\overrightarrow{AC} = \overrightarrow{BD}$  
  <sub>Salah: mengira diagonal harus sama sebagai vektor</sub>
- B. $\overrightarrow{AE} = \overrightarrow{BF}$  
  <sub>Salah: membandingkan setengah diagonal yang berbeda</sub>
- **C. $\overrightarrow{AE} = \overrightarrow{AF}$** ✅  
  <sub>Benar: jika $\overrightarrow{AE} = \overrightarrow{AF}$ maka $E = F$, yaitu titik tengah kedua diagonal berimpit</sub>
- D. $\overrightarrow{AE} = \overrightarrow{FD}$  
  <sub>Salah: membandingkan vektor dari titik berbeda</sub>

**Pembahasan:** Dua titik tengah berimpit jika vektor posisinya dari $A$ sama: $\overrightarrow{AE} = \overrightarrow{AF}$.
**Acuan:** siswa — siswa hal.207 Contoh 4.17

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b04-c-easy-bt01-007
*variasi (konteks) | C2 | 2 langkah | jenis: vektor diagonal persegi panjang*

Pada persegi panjang $ABCD$ diketahui $\overrightarrow{AB} = \langle 9, 0\rangle$ dan $\overrightarrow{AD} = \langle 0, 12\rangle$. Vektor $\overrightarrow{BD}$ adalah ....

- A. $\langle 9, -12\rangle$  
  <sub>Salah: arah terbalik, yaitu $\overrightarrow{DB}$</sub>
- B. $\langle 9, 12\rangle$  
  <sub>Salah: menjumlahkan sisi sehingga memperoleh $\overrightarrow{AC}$</sub>
- **C. $\langle -9, 12\rangle$** ✅  
  <sub>Benar: $\overrightarrow{BD} = \overrightarrow{AD} - \overrightarrow{AB} = (0-9, 12-0)$</sub>
- D. $\langle -9, -12\rangle$  
  <sub>Salah: salah tanda kedua komponen</sub>

**Pembahasan:** $\overrightarrow{BD} = \overrightarrow{BA} + \overrightarrow{AD} = \overrightarrow{AD} - \overrightarrow{AB} = \langle -9, 12\rangle$.
**Acuan:** siswa — siswa hal.208 Mari Mencoba 4.17

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b04-c-easy-bt01-008
*variasi (konteks) | C2 | 2 langkah | jenis: panjang setengah diagonal persegi panjang*

Diagonal $AC$ dan $BD$ sebuah persegi panjang berpotongan di titik $E$. Jika panjang $AC = 26$ cm, panjang $BE$ adalah ... cm.

- A. 26  
  <sub>Salah: mengira $BE$ sama dengan seluruh diagonal</sub>
- B. 52  
  <sub>Salah: mengalikan dua panjang diagonal</sub>
- C. 6,5  
  <sub>Salah: membagi dua kali</sub>
- **D. 13** ✅  
  <sub>Benar: $AE = EC = 13$; diagonal sama panjang dan saling membagi dua, sehingga $BE = ED = AE = 13$</sub>

**Pembahasan:** $BD = AC = 26$ dan $E$ titik tengah $BD$, sehingga $BE = 13$.
**Acuan:** siswa — siswa hal.208 Mari Mencoba 4.17

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b04-c-easy-bt01-009
*variasi (konteks) | C2 | 2 langkah | jenis: hasil kali titik diagonal persegi*

Persegi $ABCD$ memiliki titik sudut $A(0, 0)$, $B(5, 0)$, $C(5, 5)$, dan $D(0, 5)$. Nilai $\overrightarrow{AC}\cdot\overrightarrow{BD}$ adalah ....

- A. $-25$  
  <sub>Salah: hanya menghitung hasil kali komponen pertama</sub>
- **B. $0$** ✅  
  <sub>Benar: $\overrightarrow{AC} = \langle 5, 5\rangle$, $\overrightarrow{BD} = \langle -5, 5\rangle$; hasil kali titik $= -25 + 25 = 0$</sub>
- C. $25$  
  <sub>Salah: hanya menghitung hasil kali komponen kedua</sub>
- D. $50$  
  <sub>Salah: mengambil $\|\overrightarrow{AC}\|^2$ bukan hasil kali dengan $\overrightarrow{BD}$</sub>

**Pembahasan:** $\overrightarrow{AC}\cdot\overrightarrow{BD} = 5(-5) + 5(5) = 0$, jadi diagonal persegi saling tegak lurus.
**Acuan:** siswa — siswa hal.210 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b04-c-easy-bt01-010
*variasi (konteks) | C1 | 1 langkah | jenis: sudut perpotongan diagonal persegi*

Diagonal-diagonal persegi $PQRS$ berpotongan di titik $T$. Besar sudut $PTQ$ adalah ....

- A. $60^\circ$  
  <sub>Salah: mengira sudut seperti pada segitiga sama sisi</sub>
- **B. $90^\circ$** ✅  
  <sub>Benar: diagonal persegi saling tegak lurus</sub>
- C. $45^\circ$  
  <sub>Salah: tertukar dengan sudut antara diagonal dan sisi persegi</sub>
- D. $180^\circ$  
  <sub>Salah: mengira kedua diagonal segaris</sub>

**Pembahasan:** Diagonal persegi saling tegak lurus (hasil kali titik nol), sehingga $\angle PTQ = 90^\circ$.
**Acuan:** siswa — siswa hal.210 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b04-c-easy-bt01-011
*orisinal | C2 | 2 langkah | jenis: perbandingan titik pada ruas*

Titik $Q$ terletak pada ruas $PR$ dengan $P(1, 2)$, $R(9, 10)$, dan $PQ : QR = 1 : 3$. Koordinat $Q$ adalah ....

- A. $(5, 6)$  
  <sub>Salah: memakai titik tengah (perbandingan $1 : 1$)</sub>
- B. $(7, 8)$  
  <sub>Salah: perbandingan tertukar menjadi $3 : 1$</sub>
- **C. $(3, 4)$** ✅  
  <sub>Benar: $Q = \frac{3P + 1R}{1+3} = \frac{(3+9,\, 6+10)}{4}$</sub>
- D. $(12, 16)$  
  <sub>Salah: lupa membagi dengan $m + n$</sub>

**Pembahasan:** $\overrightarrow{PQ} = \frac{1}{4}\overrightarrow{PR} = \frac{1}{4}$\langle 8, 8\rangle$ = \langle 2, 2\rangle$, sehingga $Q = (1+2, 2+2) = (3, 4)$.
**Acuan:** siswa — siswa hal.209

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b04-c-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: rumus vektor posisi titik pembagi ruas*

Titik $Q$ berada pada ruas $PR$ dengan $PQ : QR = m : n$. Jika $\mathbf{p}$, $\mathbf{q}$, dan $\mathbf{r}$ berturut-turut vektor posisi $P$, $Q$, dan $R$, maka $\mathbf{q} = ....$

- A. $\frac{m\mathbf{r} + n\mathbf{p}}{m - n}$  
  <sub>Salah: penyebut memakai selisih $m - n$</sub>
- **B. $\frac{m\mathbf{r} + n\mathbf{p}}{m + n}$** ✅  
  <sub>Benar: $\mathbf{q} = \mathbf{p} + \frac{m}{m+n}(\mathbf{r} - \mathbf{p}) = \frac{m\mathbf{r} + n\mathbf{p}}{m+n}$</sub>
- C. $m\mathbf{r} + n\mathbf{p}$  
  <sub>Salah: lupa membagi dengan $m + n$</sub>
- D. $\frac{m\mathbf{p} + n\mathbf{r}}{m + n}$  
  <sub>Salah: perbandingan $m$ dan $n$ tertukar posisinya</sub>

**Pembahasan:** Karena $PQ : PR = m : (m+n)$, $\mathbf{q} = \mathbf{p} + \frac{m}{m+n}(\mathbf{r}-\mathbf{p}) = \frac{m\mathbf{r}+n\mathbf{p}}{m+n}$.
**Acuan:** siswa — siswa hal.209

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b04-c-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: ruas penghubung titik tengah dua sisi segitiga*

Pada segitiga $ABC$, $K$ adalah titik tengah $AB$ dan $L$ adalah titik tengah $AC$. Jika $\overrightarrow{BC} = \langle 8, -6\rangle$, maka $\overrightarrow{KL} = ....$

- A. $\langle 8, -6\rangle$  
  <sub>Salah: mengira $\overrightarrow{KL}$ sama dengan $\overrightarrow{BC}$</sub>
- B. $\langle 16, -12\rangle$  
  <sub>Salah: memakai $2\overrightarrow{BC}$ (tertukar dengan $\overrightarrow{BC} = 2\overrightarrow{KL}$)</sub>
- **C. $\langle 4, -3\rangle$** ✅  
  <sub>Benar: $\overrightarrow{KL} = \frac{1}{2}\overrightarrow{BC}$</sub>
- D. $\langle -4, 3\rangle$  
  <sub>Salah: arah terbalik, yaitu $\overrightarrow{LK}$ atau salah tanda</sub>

**Pembahasan:** $\overrightarrow{KL} = \overrightarrow{AL} - \overrightarrow{AK} = \frac{1}{2}(\overrightarrow{AC} - \overrightarrow{AB}) = \frac{1}{2}\overrightarrow{BC} = \langle 4, -3\rangle$.
**Acuan:** siswa — siswa hal.210

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b04-c-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: vektor garis berat dari titik tengah*

Pada segitiga $PQR$ diketahui $\overrightarrow{PQ} = \langle 6, 2\rangle$ dan $\overrightarrow{PR} = \langle 2, 8\rangle$. Jika $S$ titik tengah $QR$, maka $\overrightarrow{PS} = ....$

- **A. $\langle 4, 5\rangle$** ✅  
  <sub>Benar: $\overrightarrow{PS} = \frac{1}{2}(\overrightarrow{PQ} + \overrightarrow{PR})$</sub>
- B. $\langle 2, -3\rangle$  
  <sub>Salah: memakai $\frac{1}{2}(\overrightarrow{PQ} - \overrightarrow{PR})$</sub>
- C. $\langle -2, 3\rangle$  
  <sub>Salah: memakai $\frac{1}{2}(\overrightarrow{PR} - \overrightarrow{PQ})$, yaitu $\overrightarrow{QS}$</sub>
- D. $\langle 8, 10\rangle$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{2}$</sub>

**Pembahasan:** $\overrightarrow{PS} = \frac{1}{2}($\langle 6, 2\rangle$ + $\langle 2, 8\rangle$) = \langle 4, 5\rangle$.
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b04-c-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: menyatakan vektor titik tengah dalam vektor sisi*

Pada segitiga $PQR$, titik $S$ adalah titik tengah $QR$. Vektor $\overrightarrow{QS}$ dapat dinyatakan sebagai ....

- **A. $\frac{1}{2}(\overrightarrow{PR} - \overrightarrow{PQ})$** ✅  
  <sub>Benar: $\overrightarrow{QS} = \frac{1}{2}\overrightarrow{QR} = \frac{1}{2}(\overrightarrow{QP} + \overrightarrow{PR}) = \frac{1}{2}(\overrightarrow{PR} - \overrightarrow{PQ})$</sub>
- B. $\frac{1}{2}(\overrightarrow{PQ} - \overrightarrow{PR})$  
  <sub>Salah: urutan pengurangan terbalik sehingga arah terbalik</sub>
- C. $\frac{1}{2}(\overrightarrow{PR} + \overrightarrow{PQ})$  
  <sub>Salah: mencampur dengan $\overrightarrow{PS}$; $\overrightarrow{QP}$ diganti $\overrightarrow{PQ}$</sub>
- D. $\overrightarrow{PR} - \overrightarrow{PQ}$  
  <sub>Salah: lupa faktor $\frac{1}{2}$ sehingga memperoleh $\overrightarrow{QR}$</sub>

**Pembahasan:** $\overrightarrow{QS} = \frac{1}{2}\overrightarrow{QR} = \frac{1}{2}(\overrightarrow{PR} - \overrightarrow{PQ})$.
**Acuan:** siswa — siswa hal.207

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b04-c-easy-bt01-016
*orisinal | C1 | 1 langkah | jenis: hasil kali titik pada segitiga siku-siku*

Segitiga $ABC$ siku-siku di $B$. Pernyataan yang benar tentang $\overrightarrow{AB}$ dan $\overrightarrow{BC}$ adalah ....

- A. $\overrightarrow{AB}\cdot\overrightarrow{BC} = \|\overrightarrow{AC}\|^2$  
  <sub>Salah: mencampur dengan hasil $\overrightarrow{AC}\cdot\overrightarrow{AC}$</sub>
- B. $\overrightarrow{AB}\cdot\overrightarrow{BC} = -\|\overrightarrow{AB}\|\|\overrightarrow{BC}\|$  
  <sub>Salah: memakai cos 180 (berlawanan arah)</sub>
- **C. $\overrightarrow{AB}\cdot\overrightarrow{BC} = 0$** ✅  
  <sub>Benar: kedua vektor saling tegak lurus sehingga hasil kali titiknya nol</sub>
- D. $\overrightarrow{AB}\cdot\overrightarrow{BC} = \|\overrightarrow{AB}\|\|\overrightarrow{BC}\|$  
  <sub>Salah: memakai cos 0 (searah) padahal sudutnya siku-siku</sub>

**Pembahasan:** Sudut antara $\overrightarrow{AB}$ dan $\overrightarrow{BC}$ adalah $90^\circ$, cos $90^\circ = 0$, sehingga hasil kali titik 0.
**Acuan:** siswa — siswa hal.208

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b04-c-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: panjang sisi miring dari penjumlahan vektor*

Segitiga $ABC$ siku-siku di $B$ dengan $\overrightarrow{AB} = \langle 5, 0\rangle$ dan $\overrightarrow{BC} = \langle 0, 12\rangle$. Panjang $AC$ adalah ....

- A. $60$  
  <sub>Salah: mengalikan panjang $5 \cdot 12$</sub>
- **B. $13$** ✅  
  <sub>Benar: $\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{BC} = \langle 5, 12\rangle$, panjangnya $\sqrt{25 + 144}$</sub>
- C. $17$  
  <sub>Salah: menjumlahkan panjang $5 + 12$</sub>
- D. $169$  
  <sub>Salah: lupa menarik akar kuadrat</sub>

**Pembahasan:** $\overrightarrow{AC} = \langle 5, 12\rangle$ sehingga $\|\overrightarrow{AC}\| = \sqrt{5^2 + 12^2} = 13$.
**Acuan:** siswa — siswa hal.209

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b04-c-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: titik sudut keempat jajargenjang*

Jajargenjang $ABCD$ memiliki titik $A(1, 1)$, $B(5, 2)$, dan $C(8, 6)$. Koordinat titik $D$ adalah ....

- A. $(12, 7)$  
  <sub>Salah: memakai $B + C - A$ (sisi yang salah)</sub>
- B. $(3, 4)$  
  <sub>Salah: mengira koordinat $D$ sama dengan komponen $\overrightarrow{BC}$</sub>
- C. $(-2, -3)$  
  <sub>Salah: memakai $A + B - C$</sub>
- **D. $(4, 5)$** ✅  
  <sub>Benar: $\overrightarrow{DC} = \overrightarrow{AB} = \langle 4, 1\rangle$, sehingga $D = C - \overrightarrow{AB} = (8-4, 6-1)$</sub>

**Pembahasan:** $D = A + C - B = (1+8-5, 1+6-2) = (4, 5)$.
**Acuan:** siswa — siswa hal.207

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b04-c-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: alasan dua ruas sejajar dengan vektor*

Pada segitiga $ABC$, $K$ dan $L$ berturut-turut titik tengah $AB$ dan $AC$. Alasan yang benar mengapa $KL$ sejajar $BC$ adalah ....

- A. $\overrightarrow{KL} = 2\overrightarrow{BC}$, kelipatan skalar dari $\overrightarrow{BC}$  
  <sub>Salah: salah menurunkan koefisien (terbalik)</sub>
- B. $\overrightarrow{KL}\cdot\overrightarrow{BC} = 0$, hasil kali titiknya nol  
  <sub>Salah: mengira sejajar ditandai hasil kali titik nol (itu tegak lurus)</sub>
- C. $\|\overrightarrow{KL}\| = \|\overrightarrow{BC}\|$, panjangnya sama  
  <sub>Salah: mengira sejajar berarti sama panjang</sub>
- **D. $\overrightarrow{KL} = \frac{1}{2}\overrightarrow{BC}$, kelipatan skalar dari $\overrightarrow{BC}$** ✅  
  <sub>Benar: dua vektor yang satu merupakan kelipatan skalar yang lain pasti sejajar</sub>

**Pembahasan:** $\overrightarrow{KL} = \frac{1}{2}(\overrightarrow{AC} - \overrightarrow{AB}) = \frac{1}{2}\overrightarrow{BC}$; kelipatan skalar berarti sejajar.
**Acuan:** siswa — siswa hal.210

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b04-c-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: jenis segiempat dari vektor sisi*

Pada segiempat $ABCD$ diketahui $\overrightarrow{AB} = \overrightarrow{DC} = \langle 6, 2\rangle$ dan $\overrightarrow{AD} = \langle -1, 3\rangle$. Segiempat $ABCD$ adalah ....

- A. persegi  
  <sub>Salah: mengira semua sisi sama karena siku-siku, padahal $\sqrt{40} \neq \sqrt{10}$</sub>
- B. belah ketupat yang bukan persegi  
  <sub>Salah: mengira sisi berdekatan sama panjang</sub>
- C. jajargenjang yang bukan persegi panjang  
  <sub>Salah: tidak memeriksa hasil kali titik yang bernilai nol</sub>
- **D. persegi panjang yang bukan persegi** ✅  
  <sub>Benar: $\overrightarrow{AB} = \overrightarrow{DC}$ (jajargenjang), $\overrightarrow{AB}\cdot\overrightarrow{AD} = -6 + 6 = 0$ (siku-siku), $\|\overrightarrow{AB}\| = \sqrt{40} \ne \|\overrightarrow{AD}\| = \sqrt{10}$</sub>

**Pembahasan:** Jajargenjang dengan sudut siku-siku dan sisi berdekatan berbeda panjang adalah persegi panjang yang bukan persegi.
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b04-c-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: jenis segitiga menurut sudut dari hasil kali titik*

Pada segitiga $PQR$ diketahui $\overrightarrow{PQ} = \langle -5, 2\rangle$ dan $\overrightarrow{PR} = \langle 4, 7\rangle$. Pernyataan yang benar tentang segitiga $PQR$ adalah ....

- A. siku-siku di $Q$, lancip di $P$ dan $R$  
  <sub>Salah: tidak menghitung hasil kali titik di $Q$ yang bernilai 35</sub>
- B. siku-siku di $P$, lancip di $Q$ dan $R$  
  <sub>Salah: mengira hasil kali titik di $P$ bernilai nol padahal bernilai $-6$</sub>
- C. lancip di ketiga titik sudutnya  
  <sub>Salah: mengabaikan tanda negatif hasil kali titik di $P$</sub>
- **D. tumpul di $P$, lancip di $Q$ dan $R$** ✅  
  <sub>Benar: $-6 < 0$ di $P$ (tumpul); $35 > 0$ di $Q$ dan $71 > 0$ di $R$ (lancip)</sub>

**Pembahasan:** $\overrightarrow{QR} = \langle 9, 5\rangle$. Di $P$: $\overrightarrow{PQ}\cdot\overrightarrow{PR} = -20+14 = -6 < 0$ (tumpul). Di $Q$: $\overrightarrow{QP}\cdot\overrightarrow{QR} = 45-10 = 35 > 0$ (lancip). Di $R$: $\overrightarrow{RP}\cdot\overrightarrow{RQ} = 36+35 = 71 > 0$ (lancip).
**Acuan:** siswa — siswa hal.210 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b04-c-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: parameter agar segitiga siku-siku di titik tertentu*

Pada segitiga $PQR$ diketahui $\overrightarrow{PQ} = \langle 8, 2\rangle$ dan $\overrightarrow{PR} = \langle k, 10\rangle$. Segitiga $PQR$ siku-siku di $Q$ untuk nilai $k$ sama dengan ....

- A. $k = 0$  
  <sub>Salah: membagi $-16$ dengan 2 (komponen kedua $\overrightarrow{PQ}$), bukan dengan 8</sub>
- B. $k = 10$  
  <sub>Salah: salah tanda saat memindahkan 16 sehingga $k - 8 = 2$</sub>
- **C. $k = 6$** ✅  
  <sub>Benar: $\overrightarrow{QR} = \overrightarrow{PR} - \overrightarrow{PQ} = \langle k-8, 8\rangle$; siku-siku di $Q$ berarti $\overrightarrow{PQ}\cdot\overrightarrow{QR} = 8(k-8)+16 = 0$</sub>
- D. $k = -\frac{5}{2}$  
  <sub>Salah: menyamakan $\overrightarrow{PQ}\cdot\overrightarrow{PR} = 0$, yaitu siku-siku di $P$</sub>

**Pembahasan:** $\overrightarrow{QR} = \langle k-8, 8\rangle$. $8(k-8)+2\cdot 8 = 0 \Rightarrow 8k = 48 \Rightarrow k = 6$.
**Acuan:** siswa — siswa hal.210 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b04-c-medium-bt01-003
*variasi (konteks) | C4 | 3 langkah | jenis: sifat diagonal layang-layang dari koordinat*

Segiempat $ABCD$ dengan $A(0, 0)$, $B(3, 1)$, $C(5, 5)$, dan $D(1, 3)$ adalah layang-layang yang bukan belah ketupat. Pernyataan yang benar tentang diagonal $AC$ dan $BD$ adalah ....

- A. saling tegak lurus; $BD$ membagi $AC$ menjadi dua sama panjang, tetapi $AC$ tidak membagi $BD$ menjadi dua sama panjang  
  <sub>Salah: peran kedua diagonal tertukar</sub>
- **B. saling tegak lurus; $AC$ membagi $BD$ menjadi dua sama panjang, tetapi $BD$ tidak membagi $AC$ menjadi dua sama panjang** ✅  
  <sub>Benar: $\overrightarrow{AC}\cdot\overrightarrow{BD} = \langle 5, 5\rangle\cdot\langle -2, 2\rangle = 0$; titik tengah $BD$ adalah $(2, 2)$ yang terletak pada $AC$, sedangkan titik tengah $AC$ adalah $(2,5;\ 2,5)$ bukan titik potong</sub>
- C. tidak saling tegak lurus, tetapi saling membagi dua sama panjang  
  <sub>Salah: salah menghitung hasil kali titik dan mencampur sifat jajargenjang</sub>
- D. saling tegak lurus dan saling membagi dua sama panjang  
  <sub>Salah: menganggap layang-layang seperti jajargenjang; titik tengah $AC$ ternyata $(2,5;\ 2,5)$ bukan $(2, 2)$</sub>

**Pembahasan:** Hasil kali titik $\overrightarrow{AC}\cdot\overrightarrow{BD} = -10+10 = 0$. Titik tengah $BD$ = $(2, 2)$ ada pada $AC$, tetapi bukan titik tengah $AC$ yaitu $(2,5;\ 2,5)$.
**Acuan:** siswa — siswa hal.210 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b04-c-medium-bt01-004
*variasi (konteks) | C3 | 3 langkah | jenis: titik sudut jajargenjang dari titik potong diagonal*

Pada jajargenjang $ABCD$ diketahui $A(2, -1)$, $B(6, 2)$, dan kedua diagonalnya berpotongan di $E(5, 4)$. Koordinat titik $D$ adalah ....

- A. $(9, 7)$  
  <sub>Salah: memakai $B + E - A$ yang bukan hubungan titik tengah</sub>
- **B. $(4, 6)$** ✅  
  <sub>Benar: diagonal jajargenjang saling membagi dua sehingga $E$ titik tengah $BD$: $D = 2E - B = (10-6,\ 8-2)$</sub>
- C. $(8, 9)$  
  <sub>Salah: menghitung $2E - A$, yaitu titik $C$</sub>
- D. $(-1, 2)$  
  <sub>Salah: menghitung $E - B$ saja</sub>

**Pembahasan:** $E$ titik tengah $BD$ sehingga $D = 2E - B = (4, 6)$.
**Acuan:** siswa — siswa hal.207 Contoh 4.17

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b04-c-medium-bt01-005
*variasi (konteks) | C3 | 3 langkah | jenis: panjang diagonal persegi panjang dari titik potong diagonal*

Diagonal-diagonal persegi panjang $ABCD$ berpotongan di titik $E$. Jika $A(-4, 3)$ dan $E(3, 27)$, panjang diagonal $BD$ adalah ....

- A. $25$  
  <sub>Salah: menghitung $AE$ saja, lupa menggandakan</sub>
- B. $100$  
  <sub>Salah: menggandakan dua kali</sub>
- **C. $50$** ✅  
  <sub>Benar: $\overrightarrow{AE} = \langle 7, 24\rangle$ sehingga $AE = 25$; $E$ titik tengah $AC$ dan $BD = AC = 2AE$</sub>
- D. $62$  
  <sub>Salah: menjumlahkan komponen $7 + 24$ lalu menggandakan</sub>

**Pembahasan:** $AE=\sqrt{49+576}=25$, $AC=50$, dan $BD=AC=50$ pada persegi panjang.
**Acuan:** siswa — siswa hal.208 Mari Mencoba 4.17

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b04-c-medium-bt01-006
*variasi (konteks) | C3 | 4 langkah | jenis: titik sudut persegi dari diagonal*

Persegi $ABCD$ dengan titik-titik sudut berurutan berlawanan arah jarum jam memiliki $A(1, 1)$ dan $C(7, 5)$. Koordinat titik $D$ adalah ....

- A. $(6, 0)$  
  <sub>Salah: menukar $B$ dan $D$ (memutar ke arah sebaliknya)</sub>
- **B. $(2, 6)$** ✅  
  <sub>Benar: diagonal persegi saling membagi dua, tegak lurus, dan sama panjang: $E=(4,3)$, setengah diagonal $\langle 3, 2\rangle$ diputar $90^\circ$ menjadi $\langle -2, 3\rangle$, sehingga $D = E + \langle -2, 3\rangle$</sub>
- C. $(1, 5)$  
  <sub>Salah: memakai $E + \langle -3, 2\rangle$, tanda komponen rotasi salah</sub>
- D. $(6, 6)$  
  <sub>Salah: memakai $E + \langle 2, 3\rangle$, lupa tanda negatif saat memutar</sub>

**Pembahasan:** $E=(4,3)$, $\overrightarrow{EC}=\langle 3,2\rangle$, tegak lurus dan sama panjang: $\langle -2,3\rangle$. $D=(4-2,\ 3+3)=(2,6)$, $B=(6,0)$.
**Acuan:** siswa — siswa hal.210 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b04-c-medium-bt01-007
*variasi (konteks) | C3 | 3 langkah | jenis: vektor titik tengah diagonal jajargenjang*

Pada jajargenjang $ABCD$, titik $F$ adalah titik tengah diagonal $BD$. Vektor $\overrightarrow{AF}$ dinyatakan dalam $\overrightarrow{AB}$ dan $\overrightarrow{AD}$ adalah ....

- A. $\overrightarrow{AB} + \overrightarrow{AD}$  
  <sub>Salah: lupa faktor $\frac{1}{2}$, hasilnya $\overrightarrow{AC}$</sub>
- B. $\overrightarrow{AB} + \frac{1}{2}\overrightarrow{AD}$  
  <sub>Salah: mengira $\overrightarrow{BF} = \frac{1}{2}\overrightarrow{AD}$ padahal $\overrightarrow{BF} = \frac{1}{2}\overrightarrow{BD}$</sub>
- **C. $\frac{1}{2}(\overrightarrow{AB} + \overrightarrow{AD})$** ✅  
  <sub>Benar: $\overrightarrow{AF} = \overrightarrow{AB} + \frac{1}{2}\overrightarrow{BD} = \overrightarrow{AB} + \frac{1}{2}(\overrightarrow{AD} - \overrightarrow{AB}) = \frac{1}{2}(\overrightarrow{AB} + \overrightarrow{AD})$</sub>
- D. $\frac{1}{2}(\overrightarrow{AB} - \overrightarrow{AD})$  
  <sub>Salah: memakai $\overrightarrow{DB}$ atau salah tanda sehingga bukan vektor ke titik tengah</sub>

**Pembahasan:** $\overrightarrow{BD}=\overrightarrow{AD}-\overrightarrow{AB}$, sehingga $\overrightarrow{AF}=\frac{1}{2}(\overrightarrow{AB}+\overrightarrow{AD})$ (sama dengan $\overrightarrow{AE}$, titik tengah $AC$).
**Acuan:** siswa — siswa hal.207 Contoh 4.17

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b04-c-medium-bt01-008
*variasi (konteks) | C3 | 3 langkah | jenis: sifat diagonal belah ketupat dari vektor sisi*

Pada segiempat $ABCD$ yang merupakan belah ketupat diketahui $\overrightarrow{AB} = \langle 5, 12\rangle$ dan $\overrightarrow{AD} = \langle 12, 5\rangle$. Pernyataan yang benar tentang diagonalnya adalah ....

- **A. $\overrightarrow{AC}\cdot\overrightarrow{BD} = 0$ dan $AC$ lebih panjang daripada $BD$** ✅  
  <sub>Benar: $\overrightarrow{AC}=\langle 17, 17\rangle$, $\overrightarrow{BD}=\langle 7, -7\rangle$; hasil kali titik $119-119=0$; $AC=17\sqrt{2} > BD=7\sqrt{2}$</sub>
- B. $\overrightarrow{AC}\cdot\overrightarrow{BD} = 238$ sehingga tidak tegak lurus  
  <sub>Salah: memakai $\overrightarrow{BD} = \langle 7, 7\rangle$ (salah tanda saat mengurangkan)</sub>
- C. $\overrightarrow{AC}\cdot\overrightarrow{BD} = 0$ dan $AC = BD$  
  <sub>Salah: mengira diagonal belah ketupat sama panjang (sifat persegi)</sub>
- D. $\overrightarrow{AC}\cdot\overrightarrow{BD} = 0$ dan $AC$ lebih pendek daripada $BD$  
  <sub>Salah: membandingkan panjang diagonal secara terbalik</sub>

**Pembahasan:** $\overrightarrow{AC}\cdot\overrightarrow{BD}=0$ menunjukkan diagonal belah ketupat tegak lurus; panjangnya $17\sqrt{2}$ dan $7\sqrt{2}$.
**Acuan:** siswa — siswa hal.210 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b04-c-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: ujung ruas dari perbandingan*

Titik $Q(7, 5)$ terletak pada ruas $PR$ dengan $P(1, 2)$ dan $PQ : QR = 3 : 2$. Koordinat titik $R$ adalah ....

- **A. $(11, 7)$** ✅  
  <sub>Benar: $PQ : PR = 3 : 5$ sehingga $\overrightarrow{PR} = \frac{5}{3}\langle 6, 3\rangle = \langle 10, 5\rangle$ dan $R = (1+10,\ 2+5)$</sub>
- B. $(17, 10)$  
  <sub>Salah: menambahkan $\overrightarrow{PR}$ utuh ke titik $Q$ bukan ke titik $P$</sub>
- C. $(9, 6)$  
  <sub>Salah: mengambil $\overrightarrow{QR} = \frac{1}{3}\overrightarrow{PQ}$ dari satu bagian saja</sub>
- D. $(13, 8)$  
  <sub>Salah: mengira $Q$ titik tengah $PR$ ($R = 2Q - P$)</sub>

**Pembahasan:** Dari $PQ:QR=3:2$, $\overrightarrow{QR}=\frac{2}{3}\overrightarrow{PQ}=\langle 4,2\rangle$, jadi $R=(7+4,\ 5+2)=(11,7)$.
**Acuan:** siswa — siswa hal.209

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b04-c-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: vektor titik berat dari garis berat*

Pada segitiga $PQR$ diketahui $\overrightarrow{PQ} = \langle 6, 3\rangle$ dan $\overrightarrow{PR} = \langle 3, 9\rangle$. Titik $S$ adalah titik tengah $QR$ dan titik berat $G$ terletak pada $PS$ dengan $PG : GS = 2 : 1$. Vektor $\overrightarrow{PG}$ adalah ....

- A. $\langle 9, 12\rangle$  
  <sub>Salah: memakai $2\overrightarrow{PS}$ bukan $\frac{2}{3}\overrightarrow{PS}$</sub>
- B. $\langle \frac{3}{2}, 2\rangle$  
  <sub>Salah: memakai $\frac{1}{3}\overrightarrow{PS}$, perbandingan tertukar menjadi $1 : 2$</sub>
- **C. $\langle 3, 4\rangle$** ✅  
  <sub>Benar: $\overrightarrow{PS}=\frac{1}{2}(\overrightarrow{PQ}+\overrightarrow{PR})=\langle \frac{9}{2}, 6\rangle$ dan $\overrightarrow{PG}=\frac{2}{3}\overrightarrow{PS}=\langle 3, 4\rangle$</sub>
- D. $\langle \frac{9}{2}, 6\rangle$  
  <sub>Salah: berhenti di $\overrightarrow{PS}$ (lupa mengambil $\frac{2}{3}$-nya)</sub>

**Pembahasan:** $\overrightarrow{PS}=\langle \frac{9}{2}, 6\rangle$; $PG:PS = 2:3$ sehingga $\overrightarrow{PG}=\langle 3, 4\rangle$.
**Acuan:** siswa — siswa hal.207

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b04-c-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: parameter agar tiga titik segaris*

Titik $A(-1, 2)$, $B(3, -4)$, dan $C(k, 8)$ terletak pada satu garis lurus. Nilai $k$ adalah ....

- A. $8$  
  <sub>Salah: memakai syarat hasil kali titik nol (tegak lurus), bukan sejajar</sub>
- **B. $-5$** ✅  
  <sub>Benar: $\overrightarrow{AB}=\langle 4, -6\rangle$, $\overrightarrow{AC}=\langle k+1, 6\rangle = t\overrightarrow{AB}$ dengan $t=-1$, sehingga $k+1=-4$</sub>
- C. $3$  
  <sub>Salah: salah tanda faktor skalar ($t = 1$ bukan $t = -1$)</sub>
- D. $-4$  
  <sub>Salah: lupa menambahkan 1 karena $\overrightarrow{AC}$ komponen pertama $k + 1$</sub>

**Pembahasan:** Segaris berarti $\overrightarrow{AC}$ kelipatan $\overrightarrow{AB}$: $6 = -6t \Rightarrow t=-1 \Rightarrow k+1=-4 \Rightarrow k=-5$.
**Acuan:** siswa — siswa hal.210

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b04-c-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: panjang ruas penghubung titik tengah dari koordinat*

Pada segitiga $ABC$ dengan $A(2, 6)$, $B(-2, 0)$, dan $C(8, 2)$, titik $K$ dan $L$ berturut-turut titik tengah $AB$ dan $AC$. Panjang $KL$ adalah ....

- **A. $\sqrt{26}$** ✅  
  <sub>Benar: $K=(0,3)$, $L=(5,4)$, $\overrightarrow{KL}=\langle 5, 1\rangle$ sehingga $KL=\sqrt{25+1}$</sub>
- B. $26$  
  <sub>Salah: lupa menarik akar kuadrat</sub>
- C. $2\sqrt{26}$  
  <sub>Salah: menghitung panjang $BC$ yang dua kali $KL$</sub>
- D. $\sqrt{6}$  
  <sub>Salah: menjumlahkan komponen $5 + 1$ sebelum diakarkan</sub>

**Pembahasan:** $KL=\sqrt{26}$ dan $BC = 2\sqrt{26}$, sesuai $\overrightarrow{KL}=\frac{1}{2}\overrightarrow{BC}$.
**Acuan:** siswa — siswa hal.210

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b04-c-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: hasil kali titik garis berat dan sisi*

Pada segitiga $PQR$ diketahui $|\overrightarrow{PQ}| = 7$ dan $|\overrightarrow{PR}| = 11$. Titik $S$ adalah titik tengah $QR$. Nilai $\overrightarrow{PS}\cdot\overrightarrow{QR}$ adalah ....

- A. $2$  
  <sub>Salah: menghitung $\frac{1}{2}(11-7)$, selisih panjang bukan selisih kuadrat</sub>
- B. $72$  
  <sub>Salah: lupa faktor $\frac{1}{2}$ pada $\overrightarrow{PS}$</sub>
- C. $-36$  
  <sub>Salah: memakai $\overrightarrow{PQ}-\overrightarrow{PR}$ sehingga arah $\overrightarrow{QR}$ terbalik</sub>
- **D. $36$** ✅  
  <sub>Benar: $\overrightarrow{PS}\cdot\overrightarrow{QR}=\frac{1}{2}(\overrightarrow{PQ}+\overrightarrow{PR})\cdot(\overrightarrow{PR}-\overrightarrow{PQ})=\frac{1}{2}(|\overrightarrow{PR}|^2-|\overrightarrow{PQ}|^2)=\frac{1}{2}(121-49)$</sub>

**Pembahasan:** Hasil kali titik $(\mathbf{a}+\mathbf{b})\cdot(\mathbf{b}-\mathbf{a}) = |\mathbf{b}|^2-|\mathbf{a}|^2$, dikali $\frac{1}{2}$: $\frac{1}{2}(121-49)=36$.
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b04-c-medium-bt01-014
*orisinal | C4 | 4 langkah | jenis: jenis segiempat dari diagonalnya*

Segiempat $ABCD$ memiliki titik sudut $A(-1, 0)$, $B(4, 1)$, $C(5, 6)$, dan $D(0, 5)$. Segiempat $ABCD$ adalah ....

- A. persegi panjang yang bukan persegi  
  <sub>Salah: mengira diagonal saling membagi dua berarti sudut siku-siku di sisi; diagonal persegi panjang harus sama panjang</sub>
- B. layang-layang yang bukan belah ketupat  
  <sub>Salah: hanya memeriksa diagonal tegak lurus tanpa memeriksa bahwa kedua diagonal saling membagi dua</sub>
- **C. belah ketupat yang bukan persegi** ✅  
  <sub>Benar: titik tengah $AC$ dan $BD$ sama $(2, 3)$ (jajargenjang), $\overrightarrow{AC}\cdot\overrightarrow{BD}=\langle 6,6\rangle\cdot\langle -4,4\rangle=0$ (tegak lurus), panjang diagonal $6\sqrt{2}\ne 4\sqrt{2}$</sub>
- D. persegi  
  <sub>Salah: mengira diagonal tegak lurus dan saling membagi dua sudah cukup menjadi persegi, padahal panjang diagonal berbeda</sub>

**Pembahasan:** Diagonal saling membagi dua (jajargenjang) dan tegak lurus, jadi belah ketupat. Panjang diagonal $6\sqrt{2}$ dan $4\sqrt{2}$ berbeda, jadi bukan persegi.
**Acuan:** siswa — siswa hal.207

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b04-c-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: panjang AC dari AC = AB + BC dan hasil kali titik*

Pada segitiga $ABC$ diketahui $|\overrightarrow{AB}| = 5$, $|\overrightarrow{BC}| = 7$, dan $\overrightarrow{AB}\cdot\overrightarrow{BC} = -10$. Panjang $AC$ adalah ....

- A. $8$  
  <sub>Salah: lupa faktor 2 pada suku $2\,\overrightarrow{AB}\cdot\overrightarrow{BC}$ sehingga $74 - 10 = 64$</sub>
- B. $\sqrt{94}$  
  <sub>Salah: salah tanda suku hasil kali titik ($+20$)</sub>
- C. $\sqrt{74}$  
  <sub>Salah: memakai $|AC|^2 = |AB|^2 + |BC|^2$ (rumus Pythagoras) padahal tidak siku-siku</sub>
- **D. $3\sqrt{6}$** ✅  
  <sub>Benar: $\overrightarrow{AC}=\overrightarrow{AB}+\overrightarrow{BC}$, sehingga $|\overrightarrow{AC}|^2 = 25 + 49 + 2(-10) = 54$</sub>

**Pembahasan:** $|\overrightarrow{AC}|^2=(\overrightarrow{AB}+\overrightarrow{BC})\cdot(\overrightarrow{AB}+\overrightarrow{BC})=25+2(-10)+49=54$.
**Acuan:** siswa — siswa hal.209

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b04-c-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: sudut keliling pada diameter dengan hasil kali titik*

Pada lingkaran berpusat di $O(0, 0)$ berjari-jari 13, $AB$ adalah diameter dengan $A(-13, 0)$ dan $B(13, 0)$, serta titik $C(5, 12)$ terletak pada lingkaran. Pernyataan yang benar adalah ....

- **A. $\overrightarrow{AC}\cdot\overrightarrow{BC} = 0$ sehingga $\angle ACB = 90^\circ$** ✅  
  <sub>Benar: $\overrightarrow{AC}=\langle 18, 12\rangle$, $\overrightarrow{BC}=\langle -8, 12\rangle$, hasil kali titik $-144+144=0$</sub>
- B. $\overrightarrow{AC}\cdot\overrightarrow{BC} = 288$ sehingga $\angle ACB$ lancip  
  <sub>Salah: salah tanda saat mengalikan $12\cdot 12$ dan $18\cdot(-8)$ (menjumlahkan 144 + 144)</sub>
- C. $\overrightarrow{AC}\cdot\overrightarrow{BC} = 0$ sehingga $AC$ sejajar $BC$  
  <sub>Salah: mengira hasil kali titik nol berarti sejajar (itu tegak lurus)</sub>
- D. $\overrightarrow{AC}\cdot\overrightarrow{BC} = -288$ sehingga $\angle ACB$ tumpul  
  <sub>Salah: menghitung $-144 - 144$ karena salah tanda komponen</sub>

**Pembahasan:** Hasil kali titik $-144+144=0$ menunjukkan $AC \perp BC$, sesuai sudut keliling pada diameter.
**Acuan:** siswa — siswa hal.210

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b04-c-medium-bt01-017
*orisinal | C3 | 3 langkah | jenis: vektor penghubung titik tengah sisi segiempat*

Pada segiempat sembarang $ABCD$, titik $K$, $L$, $M$, dan $N$ berturut-turut titik tengah $AB$, $BC$, $CD$, dan $DA$. Jika $\overrightarrow{AC} = \langle 8, -6\rangle$ dan $\overrightarrow{BD} = \langle -10, 4\rangle$, maka $\overrightarrow{LM}$ adalah ....

- A. $\langle -10, 4\rangle$  
  <sub>Salah: lupa faktor $\frac{1}{2}$ sehingga memperoleh $\overrightarrow{BD}$</sub>
- B. $\langle 4, -3\rangle$  
  <sub>Salah: memakai $\frac{1}{2}\overrightarrow{AC}$ (diagonal yang salah)</sub>
- C. $\langle 5, -2\rangle$  
  <sub>Salah: arah terbalik, yaitu $\frac{1}{2}\overrightarrow{DB}$</sub>
- **D. $\langle -5, 2\rangle$** ✅  
  <sub>Benar: $\overrightarrow{LM} = \overrightarrow{M} - \overrightarrow{L} = \frac{1}{2}(\overrightarrow{D} - \overrightarrow{B}) = \frac{1}{2}\overrightarrow{BD}$</sub>

**Pembahasan:** $L=\frac{B+C}{2}$, $M=\frac{C+D}{2}$, sehingga $\overrightarrow{LM}=\frac{D-B}{2}=\frac{1}{2}\langle -10, 4\rangle=\langle -5, 2\rangle$.
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas11_tl-b04-c-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal klaim geometri*

Seorang siswa mengklaim: "Jika kedua diagonal sebuah segiempat saling tegak lurus, maka segiempat itu pasti belah ketupat." Titik-titik sudut segiempat $ABCD$ ditulis berurutan. Segiempat yang menjadi contoh penyangkal klaim tersebut adalah ....

- A. $A(0, 0)$, $B(6, 0)$, $C(6, 4)$, $D(0, 4)$  
  <sub>Salah: persegi panjang tidak punya diagonal tegak lurus, premis klaim tidak terpenuhi sehingga bukan penyangkal</sub>
- B. $A(0, 0)$, $B(12, 5)$, $C(24, 0)$, $D(12, -5)$  
  <sub>Salah: diagonalnya tegak lurus dan memang belah ketupat (semua sisi 13), sehingga mendukung klaim, bukan menyangkalnya</sub>
- C. $A(0, 0)$, $B(5, 0)$, $C(7, 3)$, $D(2, 3)$  
  <sub>Salah: jajargenjang biasa dengan diagonal tidak tegak lurus ($-12\neq 0$), premis tidak terpenuhi</sub>
- **D. $A(0, 0)$, $B(2, 2)$, $C(6, 0)$, $D(2, -2)$** ✅  
  <sub>Benar: $\overrightarrow{AC}\cdot\overrightarrow{BD}=\langle 6,0\rangle\cdot\langle 0,-4\rangle=0$ (tegak lurus), tetapi $|AB|^2=8\neq 20=|BC|^2$ sehingga bukan belah ketupat</sub>

**Pembahasan:** Penyangkal harus memenuhi premis (diagonal tegak lurus) tetapi gagal pada kesimpulan (bukan belah ketupat). Hitung $\overrightarrow{AC}\cdot\overrightarrow{BD}$ dan panjang sisi tiap pilihan: hanya layang-layang yang memenuhi keduanya.
**Acuan:** siswa — siswa hal.210

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas11_tl-b04-c-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal klaim geometri*

Seorang siswa mengklaim: "Jika kedua diagonal sebuah segiempat sama panjang, maka segiempat itu pasti persegi panjang." Titik-titik sudut segiempat $ABCD$ ditulis berurutan. Segiempat yang menjadi contoh penyangkal klaim tersebut adalah ....

- **A. $A(0, 0)$, $B(10, 0)$, $C(8, 4)$, $D(2, 4)$** ✅  
  <sub>Benar: $|AC|^2=|BD|^2=80$ sehingga diagonal sama panjang, tetapi $\overrightarrow{AB}\cdot\overrightarrow{AD}=\langle 10,0\rangle\cdot\langle 2,4\rangle=20\neq 0$ sehingga bukan persegi panjang (trapesium sama kaki)</sub>
- B. $A(0, 0)$, $B(8, 0)$, $C(8, 5)$, $D(0, 5)$  
  <sub>Salah: persegi panjang: diagonal sama panjang dan memang persegi panjang, mendukung klaim</sub>
- C. $A(0, 0)$, $B(6, 0)$, $C(8, 3)$, $D(2, 3)$  
  <sub>Salah: jajargenjang biasa: diagonal $\sqrt{73}$ dan $5$ tidak sama, premis tidak terpenuhi</sub>
- D. $A(0, 0)$, $B(3, 4)$, $C(0, 8)$, $D(-3, 4)$  
  <sub>Salah: belah ketupat: diagonal 8 dan 6 tidak sama panjang, premis tidak terpenuhi</sub>

**Pembahasan:** Penyangkal memenuhi premis (diagonal sama panjang) tetapi bukan persegi panjang. Hitung $|AC|^2$ dan $|BD|^2$ tiap pilihan lalu uji $\overrightarrow{AB}\cdot\overrightarrow{AD}$ pada yang diagonalnya sama.
**Acuan:** siswa — siswa hal.208

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas11_tl-b04-c-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: evaluasi klaim tentang sifat diagonal*

Pernyataan yang benar tentang segiempat dan diagonalnya adalah ....

- A. Segiempat yang kedua diagonalnya saling membagi dua sama panjang pasti persegi panjang  
  <sub>Salah: segiempat demikian adalah jajargenjang, dan jajargenjang biasa bukan persegi panjang</sub>
- **B. Jajargenjang yang kedua diagonalnya saling tegak lurus pasti belah ketupat** ✅  
  <sub>Benar: pada jajargenjang $\overrightarrow{AC}\cdot\overrightarrow{BD}=(\overrightarrow{AB}+\overrightarrow{AD})\cdot(\overrightarrow{AD}-\overrightarrow{AB})=|AD|^2-|AB|^2$; bernilai 0 hanya bila $|AB|=|AD|$</sub>
- C. Layang-layang yang kedua diagonalnya sama panjang pasti persegi  
  <sub>Salah: layang-layang dengan diagonal 4 dan 4 yang sisinya $\sqrt{5}$ dan $\sqrt{13}$ bukan persegi</sub>
- D. Jajargenjang yang kedua diagonalnya sama panjang pasti belah ketupat  
  <sub>Salah: persegi panjang berukuran $6\times 4$ berdiagonal sama tetapi bukan belah ketupat</sub>

**Pembahasan:** Pernyataan benar harus dibuktikan umum. Untuk jajargenjang, $\overrightarrow{AC}\cdot\overrightarrow{BD}=|AD|^2-|AB|^2$, jadi diagonal tegak lurus setara dengan $|AB|=|AD|$ (belah ketupat). Tiga pernyataan lain runtuh oleh contoh penyangkal: persegi panjang $6\times 4$, layang-layang berdiagonal 4 dan 4, serta jajargenjang biasa.
**Acuan:** siswa — siswa hal.210

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b04-c-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: merancang titik dari dua syarat*

Persegi panjang $ABCD$ dengan titik sudut berurutan memiliki $A(2, 1)$ dan $B(9, 3)$. Panjang $AD$ sama dengan dua kali panjang $AB$, dan ordinat titik $D$ lebih besar daripada ordinat titik $A$. Koordinat titik $C$ adalah ....

- **A. $(5, 17)$** ✅  
  <sub>Benar: $\overrightarrow{AB}=\langle 7,2\rangle$, $\overrightarrow{AD}\perp\overrightarrow{AB}$ sehingga $\overrightarrow{AD}=k\langle -2,7\rangle$; $|AD|=2|AB|$ memberi $k=\pm 2$; ordinat $D$ lebih besar memilih $k=2$, $D(-2,15)$, $C=B+\overrightarrow{AD}=(5,17)$</sub>
- B. $(13, -11)$  
  <sub>Salah: memakai $k=-2$ sehingga $D$ berada di bawah $A$, melanggar syarat ordinat $D>$ ordinat $A$</sub>
- C. $(-2, 15)$  
  <sub>Salah: mengira koordinat $D$ sebagai koordinat $C$</sub>
- D. $(7, 10)$  
  <sub>Salah: memakai $k=1$ (panjang $AD$ sama dengan $AB$), mengabaikan syarat dua kali</sub>

**Pembahasan:** Vektor tegak lurus $\langle 7,2\rangle$ adalah $\langle -2,7\rangle$. Syarat panjang memberi $k=\pm 2$, syarat orientasi memilih $k=2$. Titik $C=B+\overrightarrow{AD}=(9-4,3+14)=(5,17)$.
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b04-c-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: menemukan kesalahan pada pembuktian vektor*

Pada segitiga $ABC$, $K$ titik tengah $AB$ dan $L$ titik tengah $AC$. Seorang siswa membuktikan $\overrightarrow{KL}=\frac{1}{2}\overrightarrow{BC}$ dengan langkah berikut.

- Langkah 1: $\overrightarrow{KL}=\overrightarrow{KA}+\overrightarrow{AL}$
- Langkah 2: $\overrightarrow{KA}=\frac{1}{2}\overrightarrow{BA}$ dan $\overrightarrow{AL}=\frac{1}{2}\overrightarrow{AC}$
- Langkah 3: $\overrightarrow{KL}=\frac{1}{2}\left(\overrightarrow{BA}+\overrightarrow{AC}\right)$
- Langkah 4: $\overrightarrow{BA}+\overrightarrow{AC}=\overrightarrow{CB}$, sehingga $\overrightarrow{KL}=\frac{1}{2}\overrightarrow{CB}$

Satu-satunya langkah yang mengandung kesalahan adalah ....

- **A. Langkah 4** ✅  
  <sub>Benar: $\overrightarrow{BA}+\overrightarrow{AC}=\overrightarrow{BC}$ (dari $B$ ke $A$ lalu ke $C$), bukan $\overrightarrow{CB}$; hasil yang benar $\overrightarrow{KL}=\frac{1}{2}\overrightarrow{BC}$</sub>
- B. Langkah 3  
  <sub>Salah: benar: substitusi langkah 2 lalu faktorkan $\frac{1}{2}$</sub>
- C. Langkah 1  
  <sub>Salah: benar: dari $K$ ke $A$ lalu ke $L$ sama dengan $K$ ke $L$</sub>
- D. Langkah 2  
  <sub>Salah: benar: $K$ titik tengah $AB$ sehingga $\overrightarrow{KA}=\frac{1}{2}\overrightarrow{BA}$</sub>

**Pembahasan:** Cek arah tiap vektor. Langkah 1-3 benar. Pada langkah 4, $\overrightarrow{BA}+\overrightarrow{AC}$ berawal di $B$ dan berakhir di $C$, yaitu $\overrightarrow{BC}$, bukan $\overrightarrow{CB}$.
**Acuan:** siswa — siswa hal.207

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b04-c-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: menemukan kesalahan pada pembuktian vektor*

Titik $Q$ pada ruas $PR$ dengan $PQ : QR = m : n$. Misalkan $\mathbf{p}$, $\mathbf{q}$, $\mathbf{r}$ vektor posisi $P$, $Q$, $R$. Seorang siswa menurunkan $\mathbf{q}$ dengan langkah berikut.

- Langkah 1: $\overrightarrow{PR}=\mathbf{r}-\mathbf{p}$
- Langkah 2: $\overrightarrow{PQ}=\frac{n}{m+n}\overrightarrow{PR}$
- Langkah 3: $\mathbf{q}=\mathbf{p}+\overrightarrow{PQ}$
- Langkah 4: $\mathbf{q}=\mathbf{p}+\frac{n}{m+n}(\mathbf{r}-\mathbf{p})=\frac{m\mathbf{p}+n\mathbf{r}}{m+n}$

Langkah pertama yang mengandung kesalahan adalah ....

- A. Langkah 3  
  <sub>Salah: benar: $\overrightarrow{OQ}=\overrightarrow{OP}+\overrightarrow{PQ}$</sub>
- **B. Langkah 2** ✅  
  <sub>Benar: $PQ : PR = m : (m+n)$ sehingga $\overrightarrow{PQ}=\frac{m}{m+n}\overrightarrow{PR}$, bukan $\frac{n}{m+n}$</sub>
- C. Langkah 4  
  <sub>Salah: pengerjaan aljabarnya benar mengikuti langkah 2; kesalahan sudah terjadi lebih awal pada langkah 2</sub>
- D. Langkah 1  
  <sub>Salah: benar: $\overrightarrow{PR}=\overrightarrow{OR}-\overrightarrow{OP}=\mathbf{r}-\mathbf{p}$</sub>

**Pembahasan:** Karena $PQ : QR = m : n$, panjang $PQ$ adalah $\frac{m}{m+n}$ dari $PR$. Langkah 2 menukar $m$ dan $n$. Langkah 4 hanyalah aljabar yang benar dari langkah 2, tetapi hasilnya $\frac{m\mathbf{p}+n\mathbf{r}}{m+n}$ keliru; seharusnya $\frac{n\mathbf{p}+m\mathbf{r}}{m+n}$.
**Acuan:** siswa — siswa hal.209

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b04-c-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: menyimpulkan jenis segiempat dari titik tengah sisi*

Pada segiempat sembarang $ABCD$, titik $K$, $L$, $M$, dan $N$ berturut-turut adalah titik tengah $AB$, $BC$, $CD$, dan $DA$. Jika diagonal $AC$ dan $BD$ saling tegak lurus (panjangnya tidak diketahui), segiempat $KLMN$ pasti merupakan ....

- A. persegi, untuk setiap segiempat $ABCD$ yang diagonalnya tegak lurus  
  <sub>Salah: sisi $\frac{1}{2}|AC|$ dan $\frac{1}{2}|BD|$ sama hanya bila $|AC|=|BD|$, tidak dijamin</sub>
- **B. persegi panjang, tetapi belum tentu persegi** ✅  
  <sub>Benar: $\overrightarrow{KL}=\frac{1}{2}\overrightarrow{AC}=\overrightarrow{NM}$ dan $\overrightarrow{LM}=\frac{1}{2}\overrightarrow{BD}=\overrightarrow{KN}$ sehingga $KLMN$ jajargenjang; $AC\perp BD$ membuat sisi bersebelahan tegak lurus; sisinya $\frac{1}{2}|AC|$ dan $\frac{1}{2}|BD|$ belum tentu sama</sub>
- C. jajargenjang yang bukan persegi panjang  
  <sub>Salah: sudut $KLM$ siku-siku karena $\overrightarrow{LK}\perp\overrightarrow{LM}$, jadi pasti persegi panjang</sub>
- D. belah ketupat yang bukan persegi  
  <sub>Salah: sudutnya pasti siku-siku, sedangkan belah ketupat yang bukan persegi tidak bersudut siku-siku</sub>

**Pembahasan:** Ruas yang menghubungkan titik tengah dua sisi segiempat sejajar dengan satu diagonal dan setengah panjangnya. Maka $KLMN$ jajargenjang dengan sisi sejajar $AC$ dan $BD$. Karena $AC\perp BD$, sudutnya siku-siku. Sama panjang sisi hanya bila diagonalnya sama panjang, jadi bukan persegi pasti.
**Acuan:** siswa — siswa hal.210

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b04-c-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: syarat parameter agar segiempat khusus*

Segiempat $ABCD$ memiliki $A(0, 0)$, $B(5, k)$, $C(12, 0)$, dan $D(5, -3)$ dengan $k>0$. Titik $K$, $L$, $M$, dan $N$ berturut-turut titik tengah $AB$, $BC$, $CD$, dan $DA$. Nilai $k$ agar $KLMN$ berbentuk persegi adalah ....

- A. $12$  
  <sub>Salah: menyamakan $k$ dengan $|AC|$ tanpa menambah ordinat $D$ ($|BD|=k+3$)</sub>
- B. $15$  
  <sub>Salah: mengira $|BD|=k-3$ atau menjumlahkan $12+3$</sub>
- C. $3$  
  <sub>Salah: menyamakan $|BD|$ dengan $\frac{1}{2}|AC|=6$ sehingga $k=3$</sub>
- **D. $9$** ✅  
  <sub>Benar: $KLMN$ persegi bila $AC\perp BD$ (selalu, sebab $AC$ mendatar dan $BD$ tegak) dan $|AC|=|BD|$: $12=k+3$ sehingga $k=9$</sub>

**Pembahasan:** Sisi $KLMN$ sejajar diagonal dan berukuran setengahnya. Persegi memerlukan diagonal $AC$, $BD$ tegak lurus dan sama panjang. $AC=\langle 12,0\rangle$, $BD=\langle 0,-3-k\rangle$ tegak lurus; $|BD|=k+3=12$ memberi $k=9$.
**Acuan:** siswa — siswa hal.210

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b04-c-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: syarat parameter agar segiempat khusus*

Segiempat $ABCD$ memiliki $A(0, 0)$, $B(8, 0)$, $C(8+p, 6)$, dan $D(p, 6)$ dengan $p\geq 0$. Pernyataan yang benar adalah ....

- A. persegi panjang untuk $p=0$, belah ketupat untuk $p=8$, dan tidak ada $p$ yang membuatnya persegi  
  <sub>Salah: memakai panjang diagonal 10 padahal syaratnya $|AD|=|AB|$ yaitu $p^2+36=64$</sub>
- B. persegi panjang untuk $p=0$, belah ketupat dan persegi sama-sama untuk $p=2\sqrt{7}$  
  <sub>Salah: sisi sama panjang saja menghasilkan belah ketupat; untuk persegi sudutnya harus siku-siku, sedangkan $8p\neq 0$</sub>
- **C. persegi panjang untuk $p=0$, belah ketupat untuk $p=2\sqrt{7}$, dan tidak ada $p$ yang membuatnya persegi** ✅  
  <sub>Benar: $\overrightarrow{AB}=\overrightarrow{DC}$ sehingga jajargenjang; persegi panjang bila $\overrightarrow{AB}\cdot\overrightarrow{AD}=8p=0$; belah ketupat bila $p^2+36=64$; kedua syarat tidak bisa dipenuhi bersamaan</sub>
- D. persegi panjang untuk $p=0$, belah ketupat untuk $p=2\sqrt{7}$, dan persegi untuk $p=0$  
  <sub>Salah: untuk $p=0$ sisi $AB=8$ dan $AD=6$ tidak sama, hanya persegi panjang</sub>

**Pembahasan:** $\overrightarrow{AB}=\overrightarrow{DC}=\langle 8,0\rangle$ sehingga jajargenjang. Persegi panjang: $\overrightarrow{AB}\cdot\overrightarrow{AD}=8p=0$, jadi $p=0$. Belah ketupat: $|AD|^2=p^2+36=64$, jadi $p=2\sqrt{7}$ ($p\geq 0$). Dua syarat itu tidak bertemu, jadi persegi tidak mungkin.
**Acuan:** siswa — siswa hal.207

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b04-c-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: menggeneralisasi bukti sudut pada diameter*

Lingkaran berpusat di $O(0, 0)$ berjari-jari $13$, dengan $AB$ diameter, $A(-13, 0)$ dan $B(13, 0)$. Titik $C$ berada di salah satu posisi berikut (bukan pada sumbu $x$). Titik $C$ yang membuat $\angle ACB$ lancip adalah ....

- A. $(5, 12)$  
  <sub>Salah: titik pada lingkaran ($25+144=169$) membuat hasil kali titik 0, sudut siku-siku</sub>
- B. $(-4, 10)$  
  <sub>Salah: $16+100=116<169$, di dalam lingkaran, sudut tumpul</sub>
- **C. $(14, 3)$** ✅  
  <sub>Benar: $\overrightarrow{CA}\cdot\overrightarrow{CB}=|OC|^2-13^2$; untuk $C(14,3)$ nilainya $205-169=36>0$ sehingga sudut lancip</sub>
- D. $(6, -11)$  
  <sub>Salah: $36+121=157<169$, di dalam lingkaran, sudut tumpul</sub>

**Pembahasan:** $\overrightarrow{CA}\cdot\overrightarrow{CB}=(-13-x)(13-x)+y^2=x^2+y^2-169$. Lancip bila hasilnya positif, yaitu $C$ di luar lingkaran. Hanya $(14,3)$ dengan $14^2+3^2=205>169$.
**Acuan:** siswa — siswa hal.210

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b04-c-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: membandingkan dua pendekatan penyelesaian*

Pada trapesium $ABCD$ dengan $AB\parallel DC$, $K$ adalah titik tengah $AD$ dan $L$ titik tengah $BC$. Diketahui $\overrightarrow{AB}=\langle 12, 0\rangle$ dan $\overrightarrow{DC}=\langle 4, 0\rangle$.

- Siswa I: $\overrightarrow{KL}=\frac{1}{2}\left(\overrightarrow{AB}+\overrightarrow{DC}\right)$
- Siswa II: $\overrightarrow{KL}=\frac{1}{2}\left(\overrightarrow{AB}-\overrightarrow{DC}\right)$

Pernyataan yang benar adalah ....

- A. Siswa II benar dan $|KL|=4$  
  <sub>Salah: mengurangkan padahal $\overrightarrow{DC}$ searah dengan $\overrightarrow{AB}$; selisih bukan panjang ruas tengah</sub>
- B. Keduanya salah dan $|KL|=6$  
  <sub>Salah: Siswa I benar; 6 tidak sesuai karena $|KL|=\frac{12+4}{2}=8$</sub>
- **C. Siswa I benar dan $|KL|=8$** ✅  
  <sub>Benar: $\overrightarrow{KL}=\overrightarrow{KA}+\overrightarrow{AB}+\overrightarrow{BL}$ dan $\overrightarrow{KL}=\overrightarrow{KD}+\overrightarrow{DC}+\overrightarrow{CL}$; jumlahkan, suku $\overrightarrow{KA}+\overrightarrow{KD}=\mathbf{0}$ dan $\overrightarrow{BL}+\overrightarrow{CL}=\mathbf{0}$, sehingga $2\overrightarrow{KL}=\overrightarrow{AB}+\overrightarrow{DC}$ dan $|KL|=\frac{12+4}{2}=8$</sub>
- D. Keduanya benar karena menghasilkan panjang yang sama  
  <sub>Salah: hasilnya 8 dan 4, tidak sama</sub>

**Pembahasan:** Dengan koordinat $A(0,0)$, $B(12,0)$, $D(3,5)$, $C(7,5)$: $K\left(\frac{3}{2}, \frac{5}{2}\right)$ dan $L\left(\frac{19}{2}, \frac{5}{2}\right)$ sehingga $\overrightarrow{KL}=\langle 8,0\rangle=\frac{1}{2}(\overrightarrow{AB}+\overrightarrow{DC})$. Rumus Siswa II keliru karena $\overrightarrow{AB}$ dan $\overrightarrow{DC}$ searah.
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
