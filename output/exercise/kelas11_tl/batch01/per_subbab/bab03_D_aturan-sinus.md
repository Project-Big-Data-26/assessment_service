# Lembar koreksi — kelas11_tl SMA11L-B3 subbab D: Aturan Sinus

41 soal | easy 20, medium 11, hard 10 | variasi 14, orisinal 27
> **Kapasitas kurang (medium): 11 dari kuota 20** — Subbab D (Aturan Sinus) tipis: Rumus Sifat 3.5 hanya gambar, Contoh 3.16 dan Latihan D no.1-2, 6-8 berupa gambar atau teks pecahan rusak, dan acuan variasi pretest/Buku Siswa sudah dipakai di easy. Soal medium layak yang tidak kembar dengan easy hanya tersedia sekitar 11.
> **Kapasitas kurang (hard): 10 dari kuota 20** — Subbab D (Aturan Sinus) tipis dan tanpa soal bergambar: acuan variasi sudah habis di easy/medium, sedangkan penalaran hard yang tidak kembar hanya mencakup kasus ambigu SSA (jumlah segitiga), klaim sinus-sisi, dan batas sinus lewat jari-jari lingkaran luar. Soal layak yang tidak kembar hanya 10.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b03-d-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: sisi dari dua sudut dan satu sisi*

Pada segitiga $ABC$, diketahui $\angle A = 60^\circ$, $\angle B = 30^\circ$, dan $a = 9$. Panjang sisi $b$ adalah ....

- A. $18$  
  <sub>Salah: perbandingan sudut langsung dan terbalik, tanpa memakai sinus</sub>
- **B. $3\sqrt{3}$** ✅  
  <sub>Benar: $\frac{b}{\sin B} = \frac{a}{\sin A}$ sehingga $b = \frac{9 \sin 30^\circ}{\sin 60^\circ} = 3\sqrt{3}$</sub>
- C. $9\sqrt{3}$  
  <sub>Salah: rumus tertukar: memakai $b = a \cdot \frac{\sin A}{\sin B}$</sub>
- D. $\frac{9}{2}$  
  <sub>Salah: memperlakukan sisi sebanding langsung dengan besar sudut ($b = a \cdot \frac{B}{A}$) tanpa sinus</sub>

**Pembahasan:** Aturan Sinus: $b = \frac{a \sin B}{\sin A} = \frac{9 \cdot \frac{1}{2}}{\frac{1}{2}\sqrt{3}} = \frac{9}{\sqrt{3}} = 3\sqrt{3}$.
**Acuan:** pretest — kelas11_tl-b03-p0161-latihan-d-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b03-d-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: sisi dari dua sudut dan satu sisi*

Jika $\angle A = 45^\circ$, $\angle B = 60^\circ$, dan $a = 8$ pada segitiga $ABC$, tentukan panjang $b$.

- A. $\frac{8\sqrt{6}}{3}$  
  <sub>Salah: posisi $\sin A$ dan $\sin B$ tertukar</sub>
- B. $\frac{32}{3}$  
  <sub>Salah: sisi dianggap sebanding dengan besar sudut ($b = a \cdot \frac{B}{A}$)</sub>
- **C. $4\sqrt{6}$** ✅  
  <sub>Benar: $b = \frac{8 \sin 60^\circ}{\sin 45^\circ} = \frac{8 \cdot \frac{\sqrt{3}}{2}}{\frac{\sqrt{2}}{2}} = 4\sqrt{6}$</sub>
- D. $4\sqrt{2}$  
  <sub>Salah: memakai kosinus, bukan sinus, pada perbandingan</sub>

**Pembahasan:** $\frac{b}{\sin B} = \frac{a}{\sin A}$, jadi $b = \frac{8 \sin 60^\circ}{\sin 45^\circ} = \frac{8\sqrt{3}}{\sqrt{2}} = 4\sqrt{6}$.
**Acuan:** pretest — kelas11_tl-b03-p0161-latihan-d-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b03-d-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: sudut dari dua sisi dan satu sudut*

Pada segitiga $ABC$, jika $\angle C = 135^\circ$, $b = 5$, dan $c = 5\sqrt{2}$, maka besar sudut $B$ adalah ....

- A. $150^\circ$  
  <sub>Salah: memilih sudut tumpul dengan $\sin B = \frac{1}{2}$ padahal $C + B$ akan lebih dari $180^\circ$</sub>
- **B. $30^\circ$** ✅  
  <sub>Benar: $\sin B = \frac{b \sin C}{c} = \frac{5 \cdot \frac{\sqrt{2}}{2}}{5\sqrt{2}} = \frac{1}{2}$ dan karena $\angle C$ tumpul, $\angle B$ lancip, yaitu $30^\circ$</sub>
- C. $45^\circ$  
  <sub>Salah: mengira $\sin B = \sin C$ sehingga memilih sudut lancip yang sinusnya sama dengan $\sin 135^\circ$</sub>
- D. $90^\circ$  
  <sub>Salah: membalik $b$ dan $c$: $\sin B = \frac{c \sin C}{b} = 1$</sub>

**Pembahasan:** Aturan Sinus: $\sin B = \frac{b \sin C}{c} = \frac{1}{2}$. Sudut $B = 150^\circ$ ditolak karena $B + C > 180^\circ$, sehingga $B = 30^\circ$.
**Acuan:** pretest — kelas11_tl-b03-p0161-latihan-d-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b03-d-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: sudut dari dua sisi dan satu sudut*

Sebidang tanah berbentuk segitiga $KLM$. Besar sudut di titik $M$ adalah $120^\circ$, panjang $LM = 4$ m, dan panjang $KL = 2\sqrt{6}$ m. Besar sudut di titik $K$ adalah ....

- **A. $45^\circ$** ✅  
  <sub>Benar: $\sin K = \frac{LM \cdot \sin 120^\circ}{KL} = \frac{4 \cdot \frac{\sqrt{3}}{2}}{2\sqrt{6}} = \frac{\sqrt{2}}{2}$, sehingga $K = 45^\circ$</sub>
- B. $60^\circ$  
  <sub>Salah: mengira sudut $K$ sama dengan sudut istimewa berpasangan dengan $\sin 120^\circ = \frac{\sqrt{3}}{2}$</sub>
- C. $135^\circ$  
  <sub>Salah: memilih sudut tumpul dengan sinus sama, padahal jumlah dengan $120^\circ$ melebihi $180^\circ$</sub>
- D. $30^\circ$  
  <sub>Salah: menyederhanakan $\frac{\sqrt{3}}{\sqrt{6}}$ menjadi $\frac{1}{2}$</sub>

**Pembahasan:** Sisi di depan $K$ adalah $LM$, sisi di depan $M$ adalah $KL$. $\sin K = \frac{\sqrt{2}}{2}$, dan $K$ lancip karena $M$ tumpul, jadi $K = 45^\circ$.
**Acuan:** pretest — kelas11_tl-b03-p0161-latihan-d-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b03-d-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: sisi setelah mencari sudut ketiga*

Sebuah segitiga $PQR$ memiliki sisi $PQ$ dengan panjang 12 cm, $\angle P = 30^\circ$ dan $\angle Q = 105^\circ$. Panjang $QR$ adalah ....

- A. $4\sqrt{3}$ cm  
  <sub>Salah: salah menghitung sudut ketiga sebagai $60^\circ$</sub>
- B. $6$ cm  
  <sub>Salah: lupa membagi dengan $\sin R$</sub>
- C. $12\sqrt{2}$ cm  
  <sub>Salah: perbandingan terbalik: memakai $\frac{PQ \sin R}{\sin P}$</sub>
- **D. $6\sqrt{2}$ cm** ✅  
  <sub>Benar: $\angle R = 180^\circ - (30^\circ + 105^\circ) = 45^\circ$, lalu $QR = \frac{12 \sin 30^\circ}{\sin 45^\circ} = 6\sqrt{2}$</sub>

**Pembahasan:** Sudut ketiga $R = 45^\circ$. Aturan Sinus: $\frac{QR}{\sin P} = \frac{PQ}{\sin R}$, sehingga $QR = \frac{12 \cdot \frac{1}{2}}{\frac{\sqrt{2}}{2}} = 6\sqrt{2}$ cm.
**Acuan:** siswa — siswa hal.157 Contoh 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b03-d-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: sisi setelah mencari sudut ketiga*

Pada segitiga $ABC$ diketahui $AB = 14$ cm, $\angle A = 45^\circ$, dan $\angle B = 105^\circ$. Panjang $BC$ adalah ....

- A. $7$ cm  
  <sub>Salah: memakai $AB \sin C$ saja tanpa membagi $\sin A$</sub>
- B. $7\sqrt{2}$ cm  
  <sub>Salah: perbandingan terbalik: $\frac{AB \sin C}{\sin A}$</sub>
- C. $\frac{14\sqrt{6}}{3}$ cm  
  <sub>Salah: salah menghitung sudut $C$ sebagai $60^\circ$</sub>
- **D. $14\sqrt{2}$ cm** ✅  
  <sub>Benar: $\angle C = 180^\circ - (45^\circ + 105^\circ) = 30^\circ$, lalu $BC = \frac{14 \sin 45^\circ}{\sin 30^\circ} = 14\sqrt{2}$</sub>

**Pembahasan:** $C = 30^\circ$. Sisi $BC$ di depan $A$ dan $AB$ di depan $C$: $BC = \frac{AB \sin A}{\sin C} = \frac{14 \cdot \frac{\sqrt{2}}{2}}{\frac{1}{2}} = 14\sqrt{2}$ cm.
**Acuan:** siswa — siswa hal.157 Contoh 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b03-d-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: segitiga dengan dua sudut sama*

Sebuah segitiga $KLM$ dengan panjang $KM = 18$ cm dan $\angle K = \angle L = 45^\circ$. Panjang $KL$ adalah ....

- A. $9\sqrt{2}$ cm  
  <sub>Salah: memakai $KM \sin 45^\circ$ tanpa membagi dengan sinus sudut di depan $KL$</sub>
- B. $36$ cm  
  <sub>Salah: memakai $\sin 30^\circ$ padahal sudut di depan $KM$ adalah $45^\circ$</sub>
- **C. $18\sqrt{2}$ cm** ✅  
  <sub>Benar: $\angle M = 90^\circ$, lalu $KL = \frac{KM \sin 90^\circ}{\sin 45^\circ} = 18\sqrt{2}$</sub>
- D. $18$ cm  
  <sub>Salah: mengira $KL = KM$ karena ada dua sudut sama</sub>

**Pembahasan:** Sudut $M = 180^\circ - 90^\circ = 90^\circ$. $KM$ di depan $L$ dan $KL$ di depan $M$, sehingga $KL = \frac{18 \cdot 1}{\frac{\sqrt{2}}{2}} = 18\sqrt{2}$ cm.
**Acuan:** siswa — siswa hal.158 Mari Mencoba 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b03-d-easy-bt01-008
*variasi (konteks) | C2 | 1 langkah | jenis: hubungan sisi dan sinus*

Pada segitiga $PQR$, panjang sisi $p$ lebih besar daripada panjang sisi $q$. Pernyataan yang pasti benar adalah ....

- A. $\sin P = \sin Q$  
  <sub>Salah: mengira sinus sama karena segitiga sama jenisnya</sub>
- B. $\cos P > \cos Q$  
  <sub>Salah: mengira kosinus ikut membesar, padahal kosinus menurun pada $0^\circ$ sampai $180^\circ$</sub>
- C. $\sin P < \sin Q$  
  <sub>Salah: membalik arah ketidaksamaan</sub>
- **D. $\sin P > \sin Q$** ✅  
  <sub>Benar: karena $\sin P = \frac{p}{2R}$ dan $\sin Q = \frac{q}{2R}$ dengan $p > q$</sub>

**Pembahasan:** Aturan Sinus: $\frac{p}{\sin P} = \frac{q}{\sin Q}$, sehingga $\frac{\sin P}{\sin Q} = \frac{p}{q} > 1$ dan $\sin P > \sin Q$.
**Acuan:** siswa — siswa hal.161 Latihan D Aturan Sinus

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b03-d-easy-bt01-009
*variasi (konteks) | C2 | 1 langkah | jenis: hubungan sisi dan sinus*

Pada segitiga $ABC$, diketahui $\angle A = 40^\circ$ dan $\angle B = 70^\circ$. Hubungan panjang sisi $a$ dan $b$ yang benar adalah ....

- A. $a > b$  
  <sub>Salah: membalik arah ketidaksamaan: mengira sudut kecil berhadapan dengan sisi panjang</sub>
- **B. $a < b$** ✅  
  <sub>Benar: $\sin 40^\circ < \sin 70^\circ$ sehingga $a < b$</sub>
- C. $a = 2b$  
  <sub>Salah: mengira perbandingan sisi sama dengan perbandingan besar sudut ($70 : 40$ dibalik) tanpa sinus</sub>
- D. $a = b$  
  <sub>Salah: mengira sisi sama panjang karena kedua sudut lancip</sub>

**Pembahasan:** $\frac{a}{b} = \frac{\sin 40^\circ}{\sin 70^\circ} < 1$, jadi $a < b$.
**Acuan:** siswa — siswa hal.161 Latihan D Aturan Sinus

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b03-d-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: nilai sinus dari Aturan Sinus*

Diberikan segitiga $ABC$ dengan $\angle A = 30^\circ$, $a = 10$, dan $b = 15$. Nilai $\sin B$ adalah ....

- **A. $\frac{3}{4}$** ✅  
  <sub>Benar: $\sin B = \frac{b \sin A}{a} = \frac{15 \cdot \frac{1}{2}}{10} = \frac{3}{4}$</sub>
- B. $\frac{1}{3}$  
  <sub>Salah: $a$ dan $b$ tertukar: $\sin B = \frac{a \sin A}{b}$</sub>
- C. $\frac{3}{2}$  
  <sub>Salah: lupa mengalikan $\sin A$, hanya $\frac{b}{a}$</sub>
- D. $\frac{3\sqrt{3}}{4}$  
  <sub>Salah: memakai $\cos 30^\circ$ bukan $\sin 30^\circ$</sub>

**Pembahasan:** $\frac{\sin B}{b} = \frac{\sin A}{a}$, sehingga $\sin B = \frac{15 \cdot \sin 30^\circ}{10} = \frac{15}{20} = \frac{3}{4}$.
**Acuan:** siswa — siswa hal.159 Mari Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b03-d-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: mengenali rumus Aturan Sinus*

Pada segitiga $ABC$ dengan panjang sisi $a$, $b$, dan $c$ yang berhadapan dengan sudut $A$, $B$, dan $C$, pernyataan yang benar menurut Aturan Sinus adalah ....

- **A. $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$** ✅  
  <sub>Benar: perbandingan sisi dengan sinus sudut di hadapannya bernilai sama</sub>
- B. $\frac{\sin A}{b} = \frac{\sin B}{c} = \frac{\sin C}{a}$  
  <sub>Salah: pasangan sinus dan sisi bergeser satu huruf</sub>
- C. $\frac{a}{\sin B} = \frac{b}{\sin C} = \frac{c}{\sin A}$  
  <sub>Salah: sisi dipasangkan dengan sinus sudut yang bukan di hadapannya</sub>
- D. $\frac{a}{\cos A} = \frac{b}{\cos B} = \frac{c}{\cos C}$  
  <sub>Salah: memakai kosinus, bukan sinus</sub>

**Pembahasan:** Aturan Sinus: sisi dibagi sinus sudut di hadapannya bernilai sama untuk ketiga pasangan.
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b03-d-easy-bt01-012
*orisinal | C2 | 2 langkah | jenis: sisi setelah mencari sudut ketiga*

Pada segitiga $ABC$ diketahui $\angle B = 45^\circ$, $\angle C = 75^\circ$, dan $b = 10$. Panjang sisi $a$ adalah ....

- **A. $5\sqrt{6}$** ✅  
  <sub>Benar: $A = 180^\circ - 45^\circ - 75^\circ = 60^\circ$, lalu $a = \frac{b \sin A}{\sin B} = 5\sqrt{6}$</sub>
- B. $5\sqrt{3}$  
  <sub>Salah: lupa membagi dengan $\sin B$</sub>
- C. $\frac{10\sqrt{6}}{3}$  
  <sub>Salah: perbandingan terbalik: memakai $\frac{b \sin B}{\sin A}$</sub>
- D. $10$  
  <sub>Salah: mengira $a = b$ tanpa menghitung sudut $A$</sub>

**Pembahasan:** $\angle A = 60^\circ$. $\frac{a}{\sin 60^\circ} = \frac{10}{\sin 45^\circ}$, sehingga $a = \frac{10 \cdot \frac{\sqrt{3}}{2}}{\frac{\sqrt{2}}{2}} = 5\sqrt{6}$.
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b03-d-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: jari-jari lingkaran luar*

Pada segitiga $ABC$ diketahui $\angle A = 150^\circ$ dan $a = 9$. Jika $R$ adalah jari-jari lingkaran luar segitiga tersebut, maka $R$ sama dengan ....

- A. $\frac{9}{2}$  
  <sub>Salah: memakai $R = a \sin A$ (salah rumus)</sub>
- B. $18$  
  <sub>Salah: lupa membagi dua: $R = \frac{a}{\sin A}$</sub>
- **C. $9$** ✅  
  <sub>Benar: $\frac{a}{\sin A} = 2R$ sehingga $R = \frac{9}{2 \sin 150^\circ} = \frac{9}{2 \cdot \frac{1}{2}} = 9$</sub>
- D. $\frac{9}{4}$  
  <sub>Salah: mengalikan dengan $\sin A$, bukan membagi: $R = \frac{a \sin A}{2}$</sub>

**Pembahasan:** Aturan Sinus: $\frac{a}{\sin A} = 2R$, jadi $2R = \frac{9}{1/2} = 18$ dan $R = 9$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b03-d-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: sinus dari jari-jari lingkaran luar*

Segitiga $ABC$ memiliki jari-jari lingkaran luar $R = 5$ dan panjang sisi $b = 6$. Nilai $\sin B$ adalah ....

- A. $\frac{6}{5}$  
  <sub>Salah: lupa faktor 2 pada $2R$: $\sin B = \frac{b}{R}$</sub>
- **B. $\frac{3}{5}$** ✅  
  <sub>Benar: $\sin B = \frac{b}{2R} = \frac{6}{10} = \frac{3}{5}$</sub>
- C. $\frac{12}{5}$  
  <sub>Salah: mengalikan $b$ dengan 2, bukan membagi dengan $2R$</sub>
- D. $\frac{5}{3}$  
  <sub>Salah: pecahan terbalik: $\frac{2R}{b}$ bukan $\frac{b}{2R}$</sub>

**Pembahasan:** $\frac{b}{\sin B} = 2R = 10$, sehingga $\sin B = \frac{6}{10} = \frac{3}{5}$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b03-d-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: syarat nilai sinus pada segitiga*

Segitiga $ABC$ memiliki $\angle A = 30^\circ$. Pasangan panjang sisi $a$ dan $b$ yang dapat membentuk segitiga tersebut adalah ....

- A. $a = 5$ dan $b = 11$  
  <sub>Salah: $\sin B = 1{,}1$ lebih dari 1, tidak mungkin</sub>
- **B. $a = 10$ dan $b = 12$** ✅  
  <sub>Benar: hanya pasangan ini yang menghasilkan $\sin B = \frac{b \sin 30^\circ}{a} = 0{,}6 \le 1$</sub>
- C. $a = 4$ dan $b = 9$  
  <sub>Salah: $\sin B = 1{,}125$ lebih dari 1, tidak mungkin; siswa tidak memeriksa nilai maksimum sinus</sub>
- D. $a = 3$ dan $b = 7$  
  <sub>Salah: $\sin B \approx 1{,}17$ lebih dari 1, tidak mungkin</sub>

**Pembahasan:** $\sin B = \frac{b \sin A}{a} = \frac{b}{2a}$. Hanya $a = 10$, $b = 12$ yang memberi $0{,}6$; tiga lainnya lebih dari 1.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b03-d-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: sudut pada segitiga siku-siku*

Pada segitiga $ABC$ diketahui $\angle C = 90^\circ$, $c = 8$, dan $a = 4\sqrt{3}$. Besar sudut $A$ adalah ....

- A. $45^\circ$  
  <sub>Salah: mengira sudut sama karena segitiga siku-siku</sub>
- B. $30^\circ$  
  <sub>Salah: tertukar dengan sudut $B$, atau mengira $\sin A = \frac{1}{2}$</sub>
- C. $120^\circ$  
  <sub>Salah: memilih sudut tumpul dengan $\sin 120^\circ = \frac{\sqrt{3}}{2}$, padahal $A + C$ melebihi $180^\circ$</sub>
- **D. $60^\circ$** ✅  
  <sub>Benar: $\sin A = \frac{a \sin 90^\circ}{c} = \frac{\sqrt{3}}{2}$ dan $A$ lancip sehingga $60^\circ$</sub>

**Pembahasan:** $\frac{a}{\sin A} = \frac{c}{\sin C}$, jadi $\sin A = \frac{4\sqrt{3}}{8} = \frac{\sqrt{3}}{2}$. Karena $C = 90^\circ$, $A$ lancip: $60^\circ$.
**Acuan:** siswa — siswa hal.156

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b03-d-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: soal cerita jarak seberang sungai*

Dua titik pengamat $P$ dan $Q$ berada di tepi sungai dan berjarak 60 m. Dari $P$ dan $Q$ terlihat sebuah pohon $R$ di seberang sungai dengan $\angle QPR = 45^\circ$ dan $\angle PQR = 75^\circ$. Jarak $Q$ ke pohon $R$ adalah ....

- A. $30\sqrt{6}$ m  
  <sub>Salah: perbandingan terbalik: $\frac{PQ \sin R}{\sin P}$</sub>
- B. $30\sqrt{3}$ m  
  <sub>Salah: memakai $\sin 60^\circ$ di pembilang tanpa membagi $\sin 45^\circ$</sub>
- C. $30\sqrt{2}$ m  
  <sub>Salah: lupa membagi dengan $\sin 60^\circ$</sub>
- **D. $20\sqrt{6}$ m** ✅  
  <sub>Benar: $\angle R = 60^\circ$, lalu $QR = \frac{60 \sin 45^\circ}{\sin 60^\circ} = 20\sqrt{6}$ m</sub>

**Pembahasan:** Sudut di $R$ adalah $180^\circ - 45^\circ - 75^\circ = 60^\circ$. $QR$ berhadapan dengan $P$: $QR = \frac{60 \cdot \frac{\sqrt{2}}{2}}{\frac{\sqrt{3}}{2}} = 20\sqrt{6}$ m.
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b03-d-easy-bt01-018
*orisinal | C2 | 1 langkah | jenis: perbandingan sisi dan sinus*

Pada segitiga $ABC$, perbandingan panjang sisi $a : b = 2 : 3$. Perbandingan $\sin A : \sin B$ adalah ....

- **A. $2 : 3$** ✅  
  <sub>Benar: $\frac{a}{b} = \frac{\sin A}{\sin B}$</sub>
- B. $5 : 6$  
  <sub>Salah: mengira perbandingan sinus berbeda secara tambahan, bukan sama dengan perbandingan sisi</sub>
- C. $3 : 2$  
  <sub>Salah: perbandingan terbalik</sub>
- D. $4 : 9$  
  <sub>Salah: mengkuadratkan perbandingan</sub>

**Pembahasan:** Dari Aturan Sinus $a : b = \sin A : \sin B$, sehingga perbandingannya sama, yaitu $2 : 3$.
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b03-d-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: sisi dari perbandingan sinus*

Pada segitiga $ABC$ berlaku $\sin A = 2 \sin B$. Jika panjang sisi $a = 10$ cm, maka panjang sisi $b$ adalah ....

- A. $20$ cm  
  <sub>Salah: membalik perbandingan: $b = 2a$</sub>
- B. $2{,}5$ cm  
  <sub>Salah: membagi dua kali: $b = \frac{a}{4}$</sub>
- **C. $5$ cm** ✅  
  <sub>Benar: $\frac{a}{b} = \frac{\sin A}{\sin B} = 2$ sehingga $b = \frac{10}{2} = 5$</sub>
- D. $10$ cm  
  <sub>Salah: mengira $b = a$</sub>

**Pembahasan:** $\frac{a}{\sin A} = \frac{b}{\sin B}$, jadi $b = a \cdot \frac{\sin B}{\sin A} = 10 \cdot \frac{1}{2} = 5$ cm.
**Acuan:** siswa — siswa hal.156

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b03-d-easy-bt01-020
*orisinal | C2 | 1 langkah | jenis: soal cerita taman segitiga*

Sebuah taman berbentuk segitiga $PQR$ dengan $\angle P = 30^\circ$, $\angle Q = 120^\circ$, dan panjang sisi $QR = 14$ m. Panjang sisi $PR$ adalah ....

- A. $28$ m  
  <sub>Salah: mengira $PR = 2 \cdot QR$ karena $\sin 30^\circ = \frac{1}{2}$ tanpa memakai $\sin 120^\circ$</sub>
- B. $7\sqrt{3}$ m  
  <sub>Salah: lupa membagi dengan $\sin 30^\circ$</sub>
- **C. $14\sqrt{3}$ m** ✅  
  <sub>Benar: $PR = \frac{QR \sin Q}{\sin P} = \frac{14 \cdot \frac{\sqrt{3}}{2}}{\frac{1}{2}} = 14\sqrt{3}$ m</sub>
- D. $\frac{14\sqrt{3}}{3}$ m  
  <sub>Salah: perbandingan terbalik: $\frac{QR \sin P}{\sin Q}$</sub>

**Pembahasan:** $PR$ berhadapan dengan $Q$ dan $QR$ berhadapan dengan $P$: $PR = \frac{14 \sin 120^\circ}{\sin 30^\circ} = 14\sqrt{3}$ m.
**Acuan:** siswa — siswa hal.158

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b03-d-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: tinggi tebing dari Aturan Sinus dan tangen*

Dua orang pendaki, Anton ($A$) dan Bobi ($B$), berdiri terpisah sejauh 40 meter di tanah datar dan sama-sama melihat dasar tebing di titik $C$. Anton mengukur $\angle CAB = 45^\circ$ dan Bobi mengukur $\angle ABC = 105^\circ$. Bobi juga mengukur sudut elevasi puncak tebing dari titik $C$ sebesar $60^\circ$ (diukur dari $B$). Tinggi tebing adalah ....

- A. $40 \sqrt{2}$ m  
  <sub>Salah: lupa mengalikan dengan tangen sudut elevasi (berhenti di jarak $BC$)</sub>
- **B. $40 \sqrt{6}$ m** ✅  
  <sub>Benar: $\angle C = 30^\circ$, $BC = \frac{40 \sin 45^\circ}{\sin 30^\circ} = 40\sqrt{2}$ m, tinggi $= BC \tan 60^\circ = 40\sqrt{6}$ m</sub>
- C. $\frac{40 \sqrt{6}}{3}$ m  
  <sub>Salah: memakai $\tan 30^\circ$ padahal sudut elevasinya $60^\circ$</sub>
- D. $20 \sqrt{6}$ m  
  <sub>Salah: perbandingan Aturan Sinus terbalik: $BC = \frac{AB \sin C}{\sin A}$ lalu dikalikan tangen</sub>

**Pembahasan:** Sudut $C = 180^\circ - 45^\circ - 105^\circ = 30^\circ$. $BC$ di depan $A$ dan $AB$ di depan $C$: $BC = 40\sqrt{2}$ m. Tinggi $= BC \tan 60^\circ = 40\sqrt{2}\cdot\sqrt{3} = 40\sqrt{6}$ m.
**Acuan:** siswa — siswa hal.158 Contoh 3.16

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b03-d-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: tinggi tebing dari Aturan Sinus dan tangen*

Dua surveyor, Rini ($A$) dan Tomi ($B$), berdiri sejauh 30 m di lapangan datar untuk mengukur tinggi sebuah menara yang kakinya di titik $C$. Rini mengukur $\angle CAB = 45^\circ$ dan Tomi mengukur $\angle ABC = 75^\circ$. Dari titik $B$, sudut elevasi puncak menara adalah $30^\circ$. Tinggi menara adalah ....

- A. $10 \sqrt{6}$ m  
  <sub>Salah: berhenti di jarak $BC$, lupa mengalikan tangen</sub>
- B. $15 \sqrt{2}$ m  
  <sub>Salah: perbandingan Aturan Sinus terbalik untuk $BC$</sub>
- C. $30 \sqrt{2}$ m  
  <sub>Salah: memakai $\tan 60^\circ$ padahal sudut elevasinya $30^\circ$</sub>
- **D. $10 \sqrt{2}$ m** ✅  
  <sub>Benar: $\angle C = 60^\circ$, $BC = \frac{30 \sin 45^\circ}{\sin 60^\circ} = 10\sqrt{6}$ m, tinggi $= 10\sqrt{6} \tan 30^\circ = 10\sqrt{2}$ m</sub>

**Pembahasan:** Sudut $C = 60^\circ$. $BC = \frac{30 \cdot \frac{\sqrt{2}}{2}}{\frac{\sqrt{3}}{2}} = 10\sqrt{6}$ m. Tinggi $= BC \tan 30^\circ = 10\sqrt{6}\cdot\frac{1}{\sqrt{3}} = 10\sqrt{2}$ m.
**Acuan:** siswa — siswa hal.158 Contoh 3.16

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b03-d-medium-bt01-003
*variasi (angka) | C4 | 3 langkah | jenis: banyak segitiga (kasus ambigu)*

Diberikan segitiga $ABC$ dengan $\angle A = 30^\circ$, $a = 9$, dan $b = 12$. Banyak segitiga $ABC$ berbeda yang dapat dibentuk dengan data tersebut adalah ....

- **A. 2 segitiga** ✅  
  <sub>Benar: $\sin B = \frac{b \sin A}{a} = \frac{2}{3}$, ada $B \approx 41,8^\circ$ (lancip) dan $B \approx 138,2^\circ$ (tumpul); keduanya memenuhi $A + B < 180^\circ$</sub>
- B. 1 segitiga  
  <sub>Salah: hanya memakai sudut $B$ lancip dan lupa sudut tumpul dengan sinus yang sama</sub>
- C. 0 segitiga  
  <sub>Salah: mengira $\sin B$ lebih dari 1 seperti pada kasus Paulina</sub>
- D. 3 segitiga  
  <sub>Salah: menghitung sudut lancip, tumpul, dan $90^\circ$ sekaligus</sub>

**Pembahasan:** $\sin B = \frac{12 \cdot \frac{1}{2}}{9} = \frac{2}{3} < 1$. Sudut $B_1 \approx 41,8^\circ$ dan $B_2 = 180^\circ - B_1 \approx 138,2^\circ$. Untuk $B_2$: $30^\circ + 138,2^\circ = 168,2^\circ < 180^\circ$, sehingga ada dua segitiga.
**Acuan:** siswa — siswa hal.159 Mari Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b03-d-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: kasus $\sin B = 1$ lalu sudut ketiga*

Diberikan segitiga $ABC$ dengan $\angle A = 30^\circ$, $a = 6$, dan $b = 12$. Besar sudut $C$ adalah ....

- A. $90^\circ$  
  <sub>Salah: memberikan sudut $B$, bukan sudut $C$</sub>
- B. $120^\circ$  
  <sub>Salah: memakai $B = 30^\circ$ sehingga $C = 180^\circ - 30^\circ - 30^\circ$</sub>
- **C. $60^\circ$** ✅  
  <sub>Benar: $\sin B = \frac{12 \cdot \frac{1}{2}}{6} = 1$ sehingga $B = 90^\circ$ dan $C = 180^\circ - 30^\circ - 90^\circ = 60^\circ$</sub>
- D. $30^\circ$  
  <sub>Salah: mengira $C = A$ karena segitiga dianggap sama kaki</sub>

**Pembahasan:** $\frac{\sin B}{12} = \frac{\sin 30^\circ}{6}$ sehingga $\sin B = 1$ dan $B = 90^\circ$. Maka $C = 180^\circ - 30^\circ - 90^\circ = 60^\circ$.
**Acuan:** siswa — siswa hal.159 Mari Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b03-d-medium-bt01-005
*orisinal | C4 | 4 langkah | jenis: perbandingan sisi dari perbandingan sudut*

Besar sudut-sudut $A$, $B$, dan $C$ pada segitiga $ABC$ berbanding $1 : 2 : 3$. Jika keliling segitiga tersebut 24 cm, panjang sisi terpanjang adalah ....

- A. $12 - 4 \sqrt{3}$ cm  
  <sub>Salah: memberi panjang sisi terpendek ($a$), bukan sisi terpanjang</sub>
- B. $12$ cm  
  <sub>Salah: mengira sisi sebanding dengan sudut ($c = \frac{3}{6} \cdot 24$), bukan dengan sinus sudut</sub>
- C. $-12 + 12 \sqrt{3}$ cm  
  <sub>Salah: memberi panjang sisi tengah ($b$), bukan sisi terpanjang</sub>
- **D. $24 - 8 \sqrt{3}$ cm** ✅  
  <sub>Benar: sudut $30^\circ, 60^\circ, 90^\circ$ sehingga $a : b : c = \frac{1}{2} : \frac{\sqrt{3}}{2} : 1 = 1 : \sqrt{3} : 2$; $c = \frac{2 \cdot 24}{3 + \sqrt{3}} = 24 - 8\sqrt{3}$ cm</sub>

**Pembahasan:** $A = 30^\circ$, $B = 60^\circ$, $C = 90^\circ$. Sisi sebanding dengan $\sin A : \sin B : \sin C = 1 : \sqrt{3} : 2$. Jumlah bagian $3 + \sqrt{3}$, maka $c = \frac{2}{3+\sqrt{3}} \cdot 24 = 24 - 8\sqrt{3}$ cm.
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b03-d-medium-bt01-006
*orisinal | C3 | 3 langkah | jenis: jari-jari lingkaran luar setelah mencari sudut*

Pada segitiga $ABC$ diketahui $\angle B = 45^\circ$, $\angle C = 75^\circ$, dan $a = 6$. Jika $R$ adalah jari-jari lingkaran luar segitiga tersebut, maka $R$ sama dengan ....

- A. $3 \sqrt{2}$  
  <sub>Salah: memakai $\sin B$ padahal $a$ berhadapan dengan sudut $A$</sub>
- **B. $2 \sqrt{3}$** ✅  
  <sub>Benar: $A = 180^\circ - 45^\circ - 75^\circ = 60^\circ$, $2R = \frac{6}{\sin 60^\circ} = 4\sqrt{3}$ sehingga $R = 2\sqrt{3}$</sub>
- C. $4 \sqrt{3}$  
  <sub>Salah: lupa membagi dua: $R = \frac{a}{\sin A}$</sub>
- D. $6$  
  <sub>Salah: memakai $\cos A$ sebagai pengganti $\sin A$</sub>

**Pembahasan:** $A = 60^\circ$. Aturan Sinus: $\frac{a}{\sin A} = 2R$, jadi $2R = \frac{6}{\sqrt{3}/2} = 4\sqrt{3}$ dan $R = 2\sqrt{3}$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b03-d-medium-bt01-007
*orisinal | C3 | 3 langkah | jenis: soal cerita keliling dengan sudut sama*

Dua pos jaga $A$ dan $B$ berjarak 60 m. Sebuah menara $C$ terlihat dari kedua pos dengan $\angle CAB = \angle CBA = 30^\circ$. Jika seorang petugas berjalan mengelilingi segitiga $ABC$ satu kali, jarak yang ditempuhnya adalah ....

- A. $20 \sqrt{3} + 60$ m  
  <sub>Salah: hanya menambahkan satu kaki ($AC$) ke $AB$</sub>
- B. $60 + 120 \sqrt{3}$ m  
  <sub>Salah: perbandingan terbalik: kaki $= \frac{AB \sin C}{\sin A} = 60\sqrt{3}$</sub>
- **C. $60 + 40 \sqrt{3}$ m** ✅  
  <sub>Benar: $\angle C = 120^\circ$, $AC = BC = \frac{60 \sin 30^\circ}{\sin 120^\circ} = 20\sqrt{3}$ m, keliling $= 60 + 40\sqrt{3}$ m</sub>
- D. $120$ m  
  <sub>Salah: mengira $AC = BC = AB$ (segitiga sama sisi)</sub>

**Pembahasan:** $\angle C = 120^\circ$. $\frac{AC}{\sin 30^\circ} = \frac{60}{\sin 120^\circ}$ sehingga $AC = BC = 20\sqrt{3}$ m. Keliling $= 60 + 20\sqrt{3} + 20\sqrt{3} = 60 + 40\sqrt{3}$ m.
**Acuan:** siswa — siswa hal.158

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b03-d-medium-bt01-008
*orisinal | C3 | 3 langkah | jenis: sinus sudut dan jari-jari lingkaran luar*

Pada segitiga $ABC$ diketahui $\sin A = \frac{2}{5}$, $\sin B = \frac{3}{5}$, dan $a = 8$. Jika $R$ adalah jari-jari lingkaran luar segitiga tersebut, nilai $b + R$ adalah ....

- A. $\frac{46}{3}$  
  <sub>Salah: perbandingan terbalik untuk $b$: $b = \frac{16}{3}$, lalu ditambah $R = 10$</sub>
- B. $20$  
  <sub>Salah: menghitung $a + b = 8 + 12$ tanpa jari-jari</sub>
- C. $32$  
  <sub>Salah: memakai $2R = 20$ sebagai $R$: $12 + 20$</sub>
- **D. $22$** ✅  
  <sub>Benar: $2R = \frac{8}{2/5} = 20$ sehingga $R = 10$; $b = 20 \cdot \frac{3}{5} = 12$; $b + R = 22$</sub>

**Pembahasan:** $\frac{a}{\sin A} = 2R = 20$, jadi $R = 10$. $b = 2R \sin B = 12$. Maka $b + R = 22$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b03-d-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: keliling segitiga sama kaki*

Segitiga $PQR$ sama kaki dengan $PQ = PR$, $\angle P = 120^\circ$, dan $QR = 12\sqrt{3}$ cm. Keliling segitiga $PQR$ adalah ....

- **A. $12 \sqrt{3} + 24$ cm** ✅  
  <sub>Benar: $\angle Q = \angle R = 30^\circ$, $PQ = \frac{12\sqrt{3} \sin 30^\circ}{\sin 120^\circ} = 12$ cm, keliling $= 24 + 12\sqrt{3}$ cm</sub>
- B. $12 \sqrt{3} + 72$ cm  
  <sub>Salah: perbandingan terbalik: kaki $= \frac{QR \sin P}{\sin Q} = 36$</sub>
- C. $12 + 12 \sqrt{3}$ cm  
  <sub>Salah: hanya menjumlahkan satu kaki dan alas</sub>
- D. $24 \sqrt{3}$ cm  
  <sub>Salah: memakai kaki $= 6\sqrt{3}$ (lupa membagi dengan $\sin 120^\circ$)</sub>

**Pembahasan:** Sudut alas $= \frac{180^\circ - 120^\circ}{2} = 30^\circ$. $PQ = \frac{QR \sin R}{\sin P} = 12$ cm. Keliling $= 12 + 12 + 12\sqrt{3} = 24 + 12\sqrt{3}$ cm.
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b03-d-medium-bt01-010
*orisinal | C4 | 4 langkah | jenis: nilai terbesar pada kasus dua kemungkinan sudut*

Diberikan segitiga $ABC$ dengan $\angle A = 30^\circ$, $a = 5$, dan $b = 5\sqrt{3}$. Nilai terbesar yang mungkin untuk panjang sisi $c$ adalah ....

- A. $5\sqrt{3}$  
  <sub>Salah: mengira $c = b$</sub>
- B. $5$  
  <sub>Salah: hanya memakai $B = 120^\circ$, padahal $c = 5$ adalah nilai terkecil</sub>
- **C. $10$** ✅  
  <sub>Benar: $\sin B = \frac{\sqrt{3}}{2}$ sehingga $B = 60^\circ$ ($C = 90^\circ$, $c = 10$) atau $B = 120^\circ$ ($C = 30^\circ$, $c = 5$); terbesar $10$</sub>
- D. $10\sqrt{3}$  
  <sub>Salah: memakai $\frac{b}{\sin A} = 10\sqrt{3}$ (yaitu $2R$) sebagai $c$</sub>

**Pembahasan:** $B = 60^\circ$: $C = 90^\circ$, $c = \frac{5 \cdot 1}{1/2} = 10$. $B = 120^\circ$: $C = 30^\circ$, $c = 5$. Nilai terbesar adalah $10$.
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b03-d-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: syarat keberadaan segitiga (parameter)*

Diberikan segitiga $ABC$ dengan $\angle A = 30^\circ$ dan $b = 14$. Jika panjang sisi $a$ adalah bilangan bulat, nilai terkecil $a$ agar segitiga tersebut ada adalah ....

- **A. $7$** ✅  
  <sub>Benar: $\sin B = \frac{14 \cdot \frac{1}{2}}{a} = \frac{7}{a} \le 1$ sehingga $a \ge 7$; $a = 7$ memberi $B = 90^\circ$ yang masih valid</sub>
- B. $6$  
  <sub>Salah: tidak memeriksa: $a = 6$ memberi $\sin B = \frac{7}{6} > 1$</sub>
- C. $14$  
  <sub>Salah: mengira $a$ harus sama dengan $b$</sub>
- D. $8$  
  <sub>Salah: memakai syarat $\sin B < 1$ (batas $<$ bukan $\le$)</sub>

**Pembahasan:** $\sin B = \frac{b \sin A}{a} = \frac{7}{a}$. Syarat segitiga ada: $\sin B \le 1$, jadi $a \ge 7$. Bilangan bulat terkecil adalah $7$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [hard] kelas11_tl-b03-d-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: syarat dua segitiga (pilih panjang sisi)*

Pada segitiga $ABC$ diketahui $\angle A = 45^\circ$ dan $b = 8\sqrt{2}$. Nilai $a$ yang menghasilkan tepat dua segitiga berbeda adalah ....

- **A. $a = 10$** ✅  
  <sub>Benar: $\sin B = \frac{b \sin A}{a} = \frac{8}{a}$. Untuk $a = 10$: $\sin B = 0{,}8$, $B$ lancip maupun tumpul memenuhi $A + B < 180^\circ$ sehingga dua segitiga</sub>
- B. $a = 8\sqrt{2}$  
  <sub>Salah: $a = b$ sehingga $B = 45^\circ$ atau $135^\circ$, tetapi $45^\circ + 135^\circ = 180^\circ$ ditolak, jadi satu segitiga</sub>
- C. $a = 8$  
  <sub>Salah: $\sin B = 1$, $B = 90^\circ$ hanya satu sudut sehingga satu segitiga (siku-siku)</sub>
- D. $a = 6$  
  <sub>Salah: $\sin B = \frac{8}{6} > 1$ sehingga tidak ada segitiga; siswa mengira $a$ kecil selalu memberi dua sudut</sub>

**Pembahasan:** Dua segitiga terjadi bila $b \sin A < a < b$, yaitu $8 < a < 8\sqrt{2} \approx 11{,}3$. Dari pilihan hanya $a = 10$ di dalam selang itu.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [hard] kelas11_tl-b03-d-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: banyak nilai bulat untuk dua segitiga*

Pada segitiga $ABC$ diketahui $\angle A = 30^\circ$ dan $b = 18$. Jika $a$ adalah bilangan bulat, banyak nilai $a$ yang menghasilkan tepat dua segitiga berbeda adalah ....

- A. $10$  
  <sub>Salah: ikut menghitung kedua batas $a = 9$ dan $a = 18$, padahal masing-masing hanya memberi satu segitiga</sub>
- B. $9$  
  <sub>Salah: ikut menghitung salah satu batas ($a = 9$ memberi $B = 90^\circ$, hanya satu segitiga)</sub>
- **C. $8$** ✅  
  <sub>Benar: syarat dua segitiga: $b \sin A < a < b$ atau $9 < a < 18$; bilangan bulatnya $10, 11, \dots, 17$ yaitu $8$ nilai</sub>
- D. $7$  
  <sub>Salah: menghitung $18 - 9 - 1 - 1$, membuang satu nilai bulat yang sebenarnya memenuhi</sub>

**Pembahasan:** $\sin B = \frac{9}{a}$. Untuk $a = 9$: $B = 90^\circ$ (satu). Untuk $9 < a < 18$: $\sin B < 1$ dan $a < b$ sehingga $B$ lancip dan tumpul sama-sama valid (dua). Untuk $a = 18$: $B = 30^\circ$ atau $150^\circ$, tetapi $30^\circ + 150^\circ = 180^\circ$ ditolak (satu). Jadi $a = 10, \dots, 17$ ada $8$ nilai.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [hard] kelas11_tl-b03-d-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan: sudut A tumpul*

Rani mengerjakan soal berikut. Pada segitiga $ABC$ diketahui $\angle A = 120^\circ$, $a = 6\sqrt{3}$, dan $b = 6$. Ia menulis $\sin B = \frac{b \sin A}{a} = \frac{1}{2}$, lalu menyimpulkan ada dua segitiga karena $B = 30^\circ$ atau $B = 150^\circ$. Kesimpulan yang benar mengenai data tersebut adalah ....

- A. Hanya satu segitiga, dengan $B = 30^\circ$ dan $C = 60^\circ$  
  <sub>Salah: salah menghitung $C$: $120^\circ + 30^\circ + 60^\circ = 210^\circ$, bukan $180^\circ$</sub>
- B. Dua segitiga, dengan $B = 30^\circ$ atau $B = 150^\circ$  
  <sub>Salah: mengulang kesalahan Rani: tidak memeriksa jumlah sudut untuk $B = 150^\circ$</sub>
- C. Tidak ada segitiga, karena $\angle A$ tumpul  
  <sub>Salah: mengira sudut tumpul membuat segitiga mustahil; padahal $B$ lancip masih memenuhi</sub>
- **D. Hanya satu segitiga, dengan $B = 30^\circ$ dan $C = 30^\circ$** ✅  
  <sub>Benar: $B = 150^\circ$ ditolak karena $A + B = 270^\circ > 180^\circ$; $B = 30^\circ$ memberi $C = 180^\circ - 120^\circ - 30^\circ = 30^\circ$</sub>

**Pembahasan:** Kesalahan Rani: sudut $B$ dengan $\sin B = \frac{1}{2}$ memang bisa $30^\circ$ atau $150^\circ$, tetapi karena $\angle A = 120^\circ$ tumpul, $B$ harus lancip. Jadi hanya $B = 30^\circ$, $C = 30^\circ$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [hard] kelas11_tl-b03-d-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: banyak sudut bulat untuk dua segitiga*

Pada segitiga $ABC$ diketahui $a = 6$ dan $b = 12$, sedangkan besar $\angle A$ adalah bilangan bulat dalam derajat. Banyak nilai $\angle A$ yang menghasilkan tepat dua segitiga berbeda adalah ....

- A. $30$  
  <sub>Salah: ikut menghitung $A = 30^\circ$, padahal $\sin B = 1$ hanya memberi satu segitiga</sub>
- B. $28$  
  <sub>Salah: memulai dari $A = 2^\circ$ atau salah menghitung banyak bilangan bulat pada $1$ sampai $29$</sub>
- **C. $29$** ✅  
  <sub>Benar: $\sin B = 2 \sin A$. Dua segitiga bila $\sin B < 1$ dan $A$ lancip (karena $a < b$), yaitu $\sin A < \frac{1}{2}$ atau $1^\circ \le A \le 29^\circ$: $29$ nilai</sub>
- D. $58$  
  <sub>Salah: ikut menghitung $151^\circ$ sampai $179^\circ$ yang juga berlaku $\sin A < \frac{1}{2}$, padahal $a < b$ menuntut $A < B$ sehingga $A$ lancip</sub>

**Pembahasan:** Karena $a < b$ maka $A < B$, jadi $A$ harus lancip. Syarat $\sin B = 2\sin A < 1$ memberi $A < 30^\circ$. Untuk $A = 1^\circ, \dots, 29^\circ$ sudut $B$ lancip dan tumpul sama-sama valid: $29$ nilai. $A = 30^\circ$ memberi satu segitiga.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [hard] kelas11_tl-b03-d-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: menilai contoh penyangkal*

Klaim: "pada setiap segitiga, sudut yang lebih besar memiliki nilai sinus yang lebih besar." Rina mengajukan sudut $A = 150^\circ$ dan $B = 60^\circ$ sebagai contoh penyangkal karena $\sin 150^\circ < \sin 60^\circ$. Penilaian yang benar adalah ....

- **A. Contoh itu tidak sah karena $150^\circ + 60^\circ > 180^\circ$, sehingga tidak ada segitiga dengan kedua sudut itu** ✅  
  <sub>Benar: dalam segitiga $A + B < 180^\circ$; dengan $A > B$ berlaku $a > b$ sehingga $\sin A > \sin B$. Pasangan $150^\circ$ dan $60^\circ$ bukan sudut segitiga</sub>
- B. Contoh itu sah karena $\sin 150^\circ < \sin 60^\circ$, sehingga klaim salah  
  <sub>Salah: hanya membandingkan nilai sinus tanpa memeriksa apakah kedua sudut dapat berada pada satu segitiga</sub>
- C. Klaim salah karena sinus sudut tumpul selalu lebih kecil daripada sinus sudut lancip  
  <sub>Salah: generalisasi keliru: $\sin 100^\circ > \sin 30^\circ$ walau $100^\circ$ tumpul</sub>
- D. Contoh itu tidak sah karena $\sin 150^\circ > \sin 60^\circ$  
  <sub>Salah: salah nilai: $\sin 150^\circ = \frac{1}{2}$ lebih kecil dari $\sin 60^\circ = \frac{\sqrt{3}}{2}$</sub>

**Pembahasan:** $\frac{a}{\sin A} = \frac{b}{\sin B}$ dan sisi lebih panjang berhadapan dengan sudut lebih besar, sehingga pada segitiga $A > B$ memberi $\sin A > \sin B$. Contoh Rina tidak dapat membentuk segitiga ($150^\circ + 60^\circ = 210^\circ$), jadi tidak menyangkal klaim.
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas11_tl-b03-d-hard-bt01-006
*orisinal | C5 | 5 langkah | jenis: bandingkan dua cara kasus ambigu*

Pada segitiga $ABC$ diketahui $\angle A = 45^\circ$, $a = 8$, dan $b = 4\sqrt{6}$. Dina berpendapat hanya ada satu segitiga karena $B$ pasti lancip, sedangkan Eko berpendapat $B$ bisa lancip atau tumpul. Penilaian yang benar adalah ....

- A. Dina benar: hanya $c = 4\sqrt{3} + 4$, karena $B$ selalu lancip bila $A$ lancip  
  <sub>Salah: anggapan keliru: sudut lancip $A$ tidak memaksa $B$ lancip</sub>
- B. Keduanya salah: tidak ada segitiga karena $\sin B > 1$  
  <sub>Salah: $\sin B = \frac{\sqrt{3}}{2} < 1$, bukan lebih dari 1</sub>
- **C. Eko benar: $B = 60^\circ$ atau $120^\circ$ sama-sama valid, sehingga $c = 4\sqrt{3} + 4$ atau $c = 4\sqrt{3} - 4$** ✅  
  <sub>Benar: $\sin B = \frac{\sqrt{3}}{2}$; $B = 60^\circ$ memberi $C = 75^\circ$, $B = 120^\circ$ memberi $C = 15^\circ$ (jumlah $45^\circ + 120^\circ = 165^\circ < 180^\circ$); $c = \frac{8 \sin C}{\sin 45^\circ}$</sub>
- D. Dina benar: $B = 120^\circ$ ditolak karena $45^\circ + 120^\circ > 180^\circ$  
  <sub>Salah: salah menjumlahkan: $45^\circ + 120^\circ = 165^\circ < 180^\circ$</sub>

**Pembahasan:** $\sin B = \frac{4\sqrt{6} \cdot \frac{\sqrt{2}}{2}}{8} = \frac{\sqrt{3}}{2}$. Kasus $B = 60^\circ$: $C = 75^\circ$, $c = 4\sqrt{3} + 4$. Kasus $B = 120^\circ$: $C = 15^\circ$, $c = 4\sqrt{3} - 4$. Eko benar.
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas11_tl-b03-d-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim perbandingan sinus*

Pada segitiga $ABC$ berlaku $\sin A : \sin B : \sin C = 3 : 4 : 5$. Andi menyimpulkan bahwa besar sudutnya juga berbanding $3 : 4 : 5$ sehingga $C = \frac{5}{12} \cdot 180^\circ = 75^\circ$. Penilaian yang benar adalah ....

- A. Salah, sebab sudut berbanding terbalik dengan sinus sehingga $C$ sudut terkecil, yaitu $45^\circ$  
  <sub>Salah: sisi terpanjang $c$ berhadapan dengan sudut terbesar, bukan terkecil</sub>
- **B. Salah, sebab sisi berbanding $3 : 4 : 5$ sehingga $C = 90^\circ$** ✅  
  <sub>Benar: Aturan Sinus: $a : b : c = \sin A : \sin B : \sin C = 3 : 4 : 5$. Karena $3^2 + 4^2 = 5^2$, segitiga siku-siku di $C$</sub>
- C. Salah, sebab $C = 120^\circ$ karena bagian sinus terbesar  
  <sub>Salah: tidak memeriksa: dengan sisi $3 : 4 : 5$ kosinus $C$ bernilai $0$, bukan negatif</sub>
- D. Benar, $C = 75^\circ$ karena nilai sinus sebanding dengan besar sudut  
  <sub>Salah: mengira sinus sebanding dengan sudut; yang sebanding dengan sinus adalah sisi</sub>

**Pembahasan:** Sisi sebanding dengan sinus sudut di hadapannya, bukan dengan sudutnya. Maka $a : b : c = 3 : 4 : 5$. Hukum kosinus atau kebalikan Pythagoras: $3^2 + 4^2 = 5^2$, jadi $C = 90^\circ$ (dan $\sin C = 1$).
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas11_tl-b03-d-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: pilih data yang menjamin tepat satu segitiga*

Data $(\angle A, a, b)$ berikut dipakai untuk membentuk segitiga $ABC$. Data yang menghasilkan tepat satu segitiga adalah ....

- A. $\angle A = 45^\circ$, $a = 5$, $b = 10$  
  <sub>Salah: $\sin B = \sqrt{2} > 1$ sehingga tidak ada segitiga</sub>
- **B. $\angle A = 30^\circ$, $a = 5$, $b = 10$** ✅  
  <sub>Benar: $\sin B = \frac{10 \cdot \frac{1}{2}}{5} = 1$ sehingga $B = 90^\circ$ saja, $C = 60^\circ$: tepat satu segitiga</sub>
- C. $\angle A = 120^\circ$, $a = 6$, $b = 8$  
  <sub>Salah: $\angle A$ tumpul menuntut $a > b$; di sini $a < b$ sehingga tidak ada segitiga ($\sin B = \frac{2\sqrt{3}}{3} > 1$)</sub>
- D. $\angle A = 60^\circ$, $a = 7$, $b = 8$  
  <sub>Salah: $\sin B = \frac{4\sqrt{3}}{7} \approx 0{,}99 < 1$ dan $a < b$ sehingga dua segitiga ($B$ lancip dan tumpul)</sub>

**Pembahasan:** Opsi benar: $\sin B = 1$ (batas), satu segitiga siku-siku. $60^\circ, 7, 8$: dua segitiga. $45^\circ, 5, 10$: $\sin B > 1$ (nol). $120^\circ, 6, 8$: $\sin B > 1$ (nol).
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas11_tl-b03-d-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: evaluasi pernyataan jari-jari lingkaran luar*

Sebuah segitiga memiliki jari-jari lingkaran luar $R = 5$. Pernyataan yang benar tentang panjang sisi-sisinya adalah ....

- A. Bila ada sisi $5$, sudut di hadapannya pasti $30^\circ$  
  <sub>Salah: $\sin A = \frac{1}{2}$ juga dipenuhi $A = 150^\circ$ (mis. sudut $150^\circ, 10^\circ, 20^\circ$)</sub>
- **B. Tiap sisi paling panjang $10$, dan $10$ hanya bila sudut di hadapannya $90^\circ$** ✅  
  <sub>Benar: $a = 2R \sin A = 10 \sin A \le 10$ dan sama dengan $10$ hanya jika $\sin A = 1$, yaitu $A = 90^\circ$</sub>
- C. Sisi terpanjangnya pasti tepat $10$  
  <sub>Salah: penyangkal: segitiga sama sisi ($A = 60^\circ$) memiliki sisi $10 \sin 60^\circ = 5\sqrt{3} \approx 8{,}7$</sub>
- D. Ada segitiga dengan sisi $12$ asalkan sudut di hadapannya tumpul  
  <sub>Salah: $\sin A = \frac{12}{10} > 1$ mustahil untuk sudut apa pun</sub>

**Pembahasan:** Dari $\frac{a}{\sin A} = 2R = 10$, $a = 10 \sin A \le 10$. Sisi $12$ mustahil, sisi terpanjang tidak harus $10$ (sama sisi: $5\sqrt{3}$), dan $a = 5$ bisa berhadapan dengan $30^\circ$ atau $150^\circ$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b03-d-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: evaluasi pernyataan umum banyak segitiga (SSA)*

Dari data $\angle A$, sisi $a$ (di hadapan $A$), dan sisi $b$ akan dibentuk segitiga $ABC$. Pernyataan yang benar adalah ....

- A. Jika $\angle A$ lancip dan $a = b \sin A$, maka tidak ada segitiga  
  <sub>Salah: $\sin B = 1$ sehingga $B = 90^\circ$ dan terbentuk satu segitiga siku-siku, mis. $A = 30^\circ$, $a = 5$, $b = 10$</sub>
- B. Jika $\angle A$ lancip dan $a < b$, maka selalu terbentuk dua segitiga  
  <sub>Salah: penyangkal: $A = 30^\circ$, $a = 3$, $b = 10$ memberi $\sin B = \frac{5}{3} > 1$ (tidak ada segitiga)</sub>
- C. Jika $\angle A$ tumpul dan $a > b$, maka terbentuk dua segitiga  
  <sub>Salah: $B$ harus lancip sehingga hanya satu segitiga, mis. $A = 120^\circ$, $a = 9$, $b = 8$</sub>
- **D. Jika $\angle A$ lancip dan $a \ge b$, maka terbentuk tepat satu segitiga** ✅  
  <sub>Benar: $a \ge b$ berarti $A \ge B$, jadi $B$ lancip dan $\sin B = \frac{b \sin A}{a} \le \sin A < 1$; sudut tumpul $180^\circ - B$ ditolak karena jumlahnya dengan $A$ melebihi $180^\circ$</sub>

**Pembahasan:** Pernyataan benar sesuai: $a \ge b$ dan $A$ lancip selalu memberi satu segitiga. Tiga lainnya ditolak dengan contoh penyangkal: $(30^\circ, 3, 10)$ nol segitiga, $(120^\circ, 9, 8)$ satu segitiga, $(30^\circ, 5, 10)$ satu segitiga.
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
