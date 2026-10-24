# Lembar koreksi — kelas11_tl SMA11L-B3 subbab E: Aturan Kosinus

51 soal | easy 20, medium 20, hard 11 | variasi 19, orisinal 32
> **Kapasitas kurang (hard): 11 dari kuota 20** — Aturan Kosinus hanya satu subbab tipis; setelah soal hitung langsung dan variasi acuan habis (Latihan E no.7 ambigu), hanya 11 soal penalaran (C5) yang layak tanpa soal kembar berangka beda.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b03-e-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: panjang sisi dari dua sisi dan sudut apit*

Jika $\angle C = 60^{\circ}$, $a = 5$, dan $b = 8$, panjang $c$ adalah ....

- A. $\sqrt{129}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$ padahal rumus memakai $-2ab\cos$</sub>
- B. $\sqrt{69}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- **C. $7$** ✅  
  <sub>Benar: $c^2 = 25 + 64 - 2(5)(8)\cos 60^{\circ} = 49$</sub>
- D. $\sqrt{89}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>

**Pembahasan:** $c^2 = a^2 + b^2 - 2ab\cos C = 25 + 64 - 40 = 49$, sehingga $c = 7$.
**Acuan:** pretest — kelas11_tl-b03-p0166-latihan-e-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b03-e-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: sisi dari sudut apit tumpul*

Pada suatu segitiga $ABC$ diketahui $\angle C = 120^{\circ}$, $a = 7$, dan $b = 8$. Panjang sisi $c$ sama dengan ....

- **A. $13$** ✅  
  <sub>Benar: $c^2 = 49 + 64 + 56 = 169$</sub>
- B. $\sqrt{57}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$ padahal rumus memakai $-2ab\cos$</sub>
- C. $\sqrt{141}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- D. $\sqrt{113}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>

**Pembahasan:** $\cos 120^{\circ} = -\frac{1}{2}$, sehingga $c^2 = 49 + 64 - 2(7)(8)(-\frac{1}{2}) = 169$ dan $c = 13$.
**Acuan:** pretest — kelas11_tl-b03-p0166-latihan-e-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b03-e-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: sudut dari tiga sisi*

Jika $a = 7$, $b = 5$, dan $c = 8$, besar sudut $A$ adalah ....

- A. $120^{\circ}$  
  <sub>Salah: salah tanda pada pembilang sehingga $\cos = -\frac{1}{2}$</sub>
- **B. $60^{\circ}$** ✅  
  <sub>Benar: $\cos A = \frac{25 + 64 - 49}{80} = \frac{1}{2}$</sub>
- C. $30^{\circ}$  
  <sub>Salah: mengira $\cos = \frac{1}{2}$ untuk sudut $30^{\circ}$ (tertukar dengan sinus)</sub>
- D. $45^{\circ}$  
  <sub>Salah: mengira $\cos = \frac{1}{2}$ sama dengan $\cos 45^{\circ}$</sub>

**Pembahasan:** $\cos A = \frac{b^2 + c^2 - a^2}{2bc} = \frac{25 + 64 - 49}{2(5)(8)} = \frac{40}{80} = \frac{1}{2}$, sehingga $A = 60^{\circ}$.
**Acuan:** pretest — kelas11_tl-b03-p0166-latihan-e-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b03-e-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: sudut tumpul dari tiga sisi*

Segitiga dengan $a = 5$, $b = 19$, dan $c = 16$ memiliki besar sudut $B$ sebesar ....

- A. $135^{\circ}$  
  <sub>Salah: mengira $\cos = -\frac{1}{2}$ sama dengan $\cos 135^{\circ}$</sub>
- B. $60^{\circ}$  
  <sub>Salah: mengabaikan tanda minus pada nilai kosinus</sub>
- **C. $120^{\circ}$** ✅  
  <sub>Benar: $\cos B = -\frac{1}{2}$</sub>
- D. $150^{\circ}$  
  <sub>Salah: mengira $\cos = -\frac{1}{2}$ untuk sudut $150^{\circ}$</sub>

**Pembahasan:** $\cos B = \frac{a^2 + c^2 - b^2}{2ac} = \frac{25 + 256 - 361}{160} = -\frac{1}{2}$, sehingga $B = 120^{\circ}$.
**Acuan:** pretest — kelas11_tl-b03-p0166-latihan-e-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b03-e-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: sudut dari tiga sisi (cerita segitiga)*

Sebuah segitiga KLM memiliki sisi KL, sisi KM, dan sisi LM yang panjangnya secara berturut-turut 15 cm, 7 cm, dan 13 cm. Berapa besar sudut K?

- A. $30^{\circ}$  
  <sub>Salah: mengira $\cos = \frac{1}{2}$ untuk sudut $30^{\circ}$ (tertukar dengan sinus)</sub>
- B. $45^{\circ}$  
  <sub>Salah: mengira $\cos = \frac{1}{2}$ sama dengan $\cos 45^{\circ}$</sub>
- C. $120^{\circ}$  
  <sub>Salah: salah tanda pada pembilang sehingga $\cos = -\frac{1}{2}$</sub>
- **D. $60^{\circ}$** ✅  
  <sub>Benar: $\cos K = \frac{105}{210} = \frac{1}{2}$</sub>

**Pembahasan:** $\cos K = \frac{KL^2 + KM^2 - LM^2}{2(KL)(KM)} = \frac{225 + 49 - 169}{210} = \frac{1}{2}$, sehingga $K = 60^{\circ}$.
**Acuan:** siswa — siswa hal.163 Contoh 3.17

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b03-e-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: sudut di titik tertentu*

Sebuah segitiga XYZ dengan panjang sisi XY, XZ, dan YZ secara berturut-turut adalah 6 cm, 14 cm, dan 10 cm. Berapa besar sudut Y?

- A. $60^{\circ}$  
  <sub>Salah: mengabaikan tanda minus pada nilai kosinus</sub>
- B. $135^{\circ}$  
  <sub>Salah: mengira $\cos = -\frac{1}{2}$ sama dengan $\cos 135^{\circ}$</sub>
- C. $150^{\circ}$  
  <sub>Salah: mengira $\cos = -\frac{1}{2}$ untuk sudut $150^{\circ}$</sub>
- **D. $120^{\circ}$** ✅  
  <sub>Benar: $\cos Y = \frac{36 + 100 - 196}{120} = -\frac{1}{2}$</sub>

**Pembahasan:** Sudut $Y$ diapit $XY = 6$ dan $YZ = 10$, dan berhadapan dengan $XZ = 14$. $\cos Y = \frac{36 + 100 - 196}{2(6)(10)} = -\frac{1}{2}$, sehingga $Y = 120^{\circ}$.
**Acuan:** siswa — siswa hal.163 Mari Mencoba 3.17

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b03-e-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: jarak dua titik dari arah dan kecepatan*

Dika, Eka, dan Fani bermain petak umpet. Dika dan Eka berlari untuk bersembunyi meninggalkan Fani pada waktu yang sama. Dika berlari ke arah 20° dengan kecepatan 3 m/s dan Eka berlari ke arah 140° dengan kecepatan 5 m/s. Setelah 4 detik, mereka berhasil menemukan tempat persembunyian masing-masing. Berapakah jarak tempat persembunyian Dika dengan Eka (dalam meter)?

- A. $4 \sqrt{19}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$ padahal rumus memakai $-2ab\cos$</sub>
- B. $2 \sqrt{166}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- **C. $28$** ✅  
  <sub>Benar: sisi yang diapit 12 m dan 20 m dengan sudut $140^{\circ} - 20^{\circ} = 120^{\circ}$</sub>
- D. $4 \sqrt{34}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>

**Pembahasan:** Jarak tempuh $12$ m dan $20$ m, sudut apit $140^{\circ} - 20^{\circ} = 120^{\circ}$. $d^2 = 144 + 400 - 2(12)(20)(-\frac{1}{2}) = 784$, sehingga $d = 28$ m.
**Acuan:** siswa — siswa hal.165 Mari Mencoba 3.18

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b03-e-easy-bt01-008
*variasi (konteks) | C2 | 2 langkah | jenis: jarak dua kapal dari arah dan kecepatan*

Dua perahu nelayan berangkat dari dermaga yang sama pada waktu yang sama. Perahu M berlayar ke arah 40° dengan kecepatan 20 km/jam dan perahu N berlayar ke arah 100° dengan kecepatan 30 km/jam (arah diukur dari utara searah jarum jam). Setelah 2 jam, jarak kedua perahu adalah ... km.

- A. $20 \sqrt{13}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>
- B. $20 \sqrt{19}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$ padahal rumus memakai $-2ab\cos$</sub>
- C. $20 \sqrt{10}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- **D. $20 \sqrt{7}$** ✅  
  <sub>Benar: sisi 40 km dan 60 km dengan sudut apit $60^{\circ}$</sub>

**Pembahasan:** Jarak tempuh $40$ km dan $60$ km, sudut apit $100^{\circ} - 40^{\circ} = 60^{\circ}$. $d^2 = 1600 + 3600 - 2(40)(60)\cos 60^{\circ} = 2800$, sehingga $d = 20\sqrt{7}$ km.
**Acuan:** siswa — siswa hal.165 Mari Mencoba 3.18

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b03-e-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: batas nilai kuadrat sisi untuk sudut tumpul*

Diberikan segitiga $ABC$ dengan $b = 5$ dan $c = 12$. Jika $\angle A > 90^{\circ}$, pernyataan yang benar tentang $a^2$ adalah ....

- **A. $169 < a^2 < 289$** ✅  
  <sub>Benar: $\cos A < 0$ sehingga $a^2 > 25 + 144 = 169$, dan $a < 5 + 12$ sehingga $a^2 < 289$</sub>
- B. $a^2 < 49$  
  <sub>Salah: memakai batas $(c-b)^2$ saja sebagai batas atas</sub>
- C. $49 < a^2 < 169$  
  <sub>Salah: terbalik: batas $169$ dipakai untuk sudut lancip, bukan tumpul</sub>
- D. $a^2 > 289$  
  <sub>Salah: mengabaikan ketaksamaan segitiga $a < b + c$</sub>

**Pembahasan:** $a^2 = 169 - 120\cos A$. Untuk $A$ tumpul, $\cos A$ antara $-1$ dan $0$ sehingga $169 < a^2 < 289$.
**Acuan:** siswa — siswa hal.166 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b03-e-easy-bt01-010
*variasi (konteks) | C2 | 1 langkah | jenis: Aturan Kosinus untuk sudut siku-siku*

Pada segitiga $PQR$ diketahui $\angle Q = 90^{\circ}$. Jika aturan kosinus untuk sisi $q$ ditulis $q^2 = p^2 + r^2 - 2pr\cos Q$, bentuk yang benar untuk segitiga ini adalah ....

- A. $q^2 = p^2 - r^2$  
  <sub>Salah: menghilangkan $r^2$ dan mengubah tanda</sub>
- B. $q^2 = p^2 + r^2 + 2pr$  
  <sub>Salah: mengira $\cos 90^{\circ} = -1$</sub>
- **C. $q^2 = p^2 + r^2$** ✅  
  <sub>Benar: $\cos 90^{\circ} = 0$ sehingga suku $2pr\cos Q$ hilang</sub>
- D. $q^2 = p^2 + r^2 - 2pr$  
  <sub>Salah: mengira $\cos 90^{\circ} = 1$</sub>

**Pembahasan:** $\cos 90^{\circ} = 0$, sehingga $q^2 = p^2 + r^2$ (teorema Pythagoras).
**Acuan:** siswa — siswa hal.166 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b03-e-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: memilih rumus Aturan Kosinus*

Pada segitiga $PQR$, sisi $p$, $q$, dan $r$ berturut-turut berhadapan dengan sudut $P$, $Q$, dan $R$. Rumus Aturan Kosinus yang benar adalah ....

- A. $r^2 = p^2 + q^2 - 2pq\cos P$  
  <sub>Salah: memakai sudut yang tidak berhadapan dengan sisi $r$</sub>
- B. $r^2 = p^2 + q^2 - pq\cos R$  
  <sub>Salah: lupa faktor 2</sub>
- C. $r^2 = p^2 + q^2 + 2pq\cos R$  
  <sub>Salah: salah tanda pada suku kosinus</sub>
- **D. $r^2 = p^2 + q^2 - 2pq\cos R$** ✅  
  <sub>Benar: sudut yang dipakai adalah sudut di hadapan sisi $r$, yaitu $R$</sub>

**Pembahasan:** Aturan Kosinus: kuadrat sisi = jumlah kuadrat dua sisi lain dikurangi $2 \times$ hasil kali kedua sisi itu $\times$ kosinus sudut di hadapan sisi pertama.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b03-e-easy-bt01-012
*orisinal | C2 | 2 langkah | jenis: nilai kosinus dari tiga sisi*

Segitiga $ABC$ memiliki sisi $a = 4$, $b = 5$, dan $c = 6$. Nilai $\cos A$ adalah ....

- A. $\frac{9}{16}$  
  <sub>Salah: memakai rumus $\cos B$ (sudut di hadapan sisi $5$)</sub>
- B. $\frac{1}{8}$  
  <sub>Salah: memakai rumus $\cos C$ (sudut di hadapan sisi $6$)</sub>
- C. $-\frac{3}{4}$  
  <sub>Salah: salah tanda pada pembilang: $a^2 - b^2 - c^2$</sub>
- **D. $\frac{3}{4}$** ✅  
  <sub>Benar: $\cos A = \frac{25 + 36 - 16}{60} = \frac{45}{60}$</sub>

**Pembahasan:** $\cos A = \frac{b^2 + c^2 - a^2}{2bc} = \frac{25 + 36 - 16}{2(5)(6)} = \frac{45}{60} = \frac{3}{4}$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b03-e-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: menentukan jenis sudut dari tiga sisi*

Sebuah segitiga memiliki sisi $6$ cm, $7$ cm, dan $10$ cm. Pernyataan yang benar tentang sudut terbesarnya adalah ....

- A. siku-siku, karena $6^2 + 7^2 = 10^2$  
  <sub>Salah: mengira $36 + 49 = 100$</sub>
- **B. tumpul, karena $10^2 > 6^2 + 7^2$** ✅  
  <sub>Benar: $100 > 36 + 49 = 85$ sehingga pembilang $\cos$ negatif</sub>
- C. lancip, karena $6^2 + 7^2 > 10^2$  
  <sub>Salah: mengira $85 > 100$</sub>
- D. tumpul, karena $6^2 + 7^2 > 10^2$  
  <sub>Salah: alasan salah ($85$ tidak lebih besar dari $100$)</sub>

**Pembahasan:** Sudut terbesar berhadapan dengan sisi $10$. $\cos = \frac{36 + 49 - 100}{84} < 0$, sehingga sudutnya tumpul.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b03-e-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: jarak dua titik dari pusat dan sudut*

Titik $P$ dan $Q$ masing-masing berjarak $10$ km dan $16$ km dari pelabuhan $O$. Jika $\angle POQ = 60^{\circ}$, jarak $P$ ke $Q$ adalah ... km.

- **A. $14$** ✅  
  <sub>Benar: $PQ^2 = 100 + 256 - 160 = 196$</sub>
- B. $2 \sqrt{69}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- C. $2 \sqrt{129}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$ padahal rumus memakai $-2ab\cos$</sub>
- D. $2 \sqrt{89}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>

**Pembahasan:** $PQ^2 = 10^2 + 16^2 - 2(10)(16)\cos 60^{\circ} = 356 - 160 = 196$, sehingga $PQ = 14$ km.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b03-e-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: sisi dengan sudut 30 derajat*

Dua batang kayu berukuran $4\sqrt{3}$ m dan $5$ m dipaku pada satu ujungnya sehingga membentuk sudut $30^{\circ}$. Jarak antara kedua ujung bebasnya adalah ... m.

- A. $\sqrt{73}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>
- **B. $\sqrt{13}$** ✅  
  <sub>Benar: $d^2 = 48 + 25 - 2(4\sqrt{3})(5)\cdot\frac{1}{2}\sqrt{3} = 13$</sub>
- C. $\sqrt{43}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- D. $\sqrt{133}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$ padahal rumus memakai $-2ab\cos$</sub>

**Pembahasan:** $d^2 = 48 + 25 - 40\sqrt{3}\cdot\frac{\sqrt{3}}{2} = 73 - 60 = 13$, sehingga $d = \sqrt{13}$ m.
**Acuan:** siswa — siswa hal.163

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b03-e-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: sisi dengan sudut apit 45 derajat*

Pada segitiga $ABC$ diketahui $\angle B = 45^{\circ}$, $a = 8$, dan $c = 3\sqrt{2}$. Panjang sisi $b$ adalah ....

- **A. $\sqrt{34}$** ✅  
  <sub>Benar: $b^2 = 64 + 18 - 2(8)(3\sqrt{2})\cdot\frac{\sqrt{2}}{2} = 34$</sub>
- B. $\sqrt{82}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>
- C. $\sqrt{58}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- D. $\sqrt{130}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$ padahal rumus memakai $-2ab\cos$</sub>

**Pembahasan:** $b^2 = a^2 + c^2 - 2ac\cos B = 64 + 18 - 48\sqrt{2}\cdot\frac{\sqrt{2}}{2} = 82 - 48 = 34$, sehingga $b = \sqrt{34}$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b03-e-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: sudut dari bentuk aljabar sisi*

Pada segitiga $ABC$ berlaku $b^2 + c^2 - a^2 = \sqrt{2}\, bc$. Besar sudut $A$ adalah ....

- A. $30^{\circ}$  
  <sub>Salah: mengambil $\cos A = \frac{\sqrt{3}}{2}$ (tertukar nilai istimewa)</sub>
- B. $135^{\circ}$  
  <sub>Salah: salah tanda sehingga $\cos A = -\frac{\sqrt{2}}{2}$</sub>
- **C. $45^{\circ}$** ✅  
  <sub>Benar: $\cos A = \frac{\sqrt{2}\,bc}{2bc} = \frac{\sqrt{2}}{2}$</sub>
- D. $60^{\circ}$  
  <sub>Salah: mengabaikan $\sqrt{2}$ sehingga $\cos A = \frac{1}{2}$</sub>

**Pembahasan:** $\cos A = \frac{b^2 + c^2 - a^2}{2bc} = \frac{\sqrt{2}\,bc}{2bc} = \frac{\sqrt{2}}{2}$, sehingga $A = 45^{\circ}$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b03-e-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: diagonal jajargenjang*

Jajargenjang $ABCD$ memiliki $AB = 3$ cm, $AD = 5$ cm, dan $\angle DAB = 120^{\circ}$. Panjang diagonal yang lebih pendek adalah ... cm.

- **A. $\sqrt{19}$** ✅  
  <sub>Benar: diagonal $AC$ berada di hadapan $\angle ABC = 60^{\circ}$</sub>
- B. $\sqrt{34}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>
- C. $7$  
  <sub>Salah: memilih diagonal $BD$ (di hadapan sudut $120^{\circ}$), yaitu diagonal terpanjang</sub>
- D. $\frac{\sqrt{106}}{2}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos B$</sub>

**Pembahasan:** $\angle ABC = 180^{\circ} - 120^{\circ} = 60^{\circ}$. $AC^2 = 9 + 25 - 2(3)(5)\cos 60^{\circ} = 19$, sehingga $AC = \sqrt{19}$. Diagonal lain $BD = \sqrt{49} = 7$ lebih panjang.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b03-e-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: alas segitiga sama kaki*

Segitiga sama kaki $ABC$ memiliki $AB = AC = 6$ cm dan $\angle A = 120^{\circ}$. Panjang $BC$ adalah ... cm.

- A. $6$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$ padahal rumus memakai $-2ab\cos$</sub>
- **B. $6 \sqrt{3}$** ✅  
  <sub>Benar: $BC^2 = 36 + 36 + 36 = 108$</sub>
- C. $6 \sqrt{2}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>
- D. $3 \sqrt{10}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>

**Pembahasan:** $BC^2 = 36 + 36 - 2(6)(6)\cos 120^{\circ} = 72 + 36 = 108$, sehingga $BC = 6\sqrt{3}$ cm.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b03-e-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: kolam dari dua sisi dan sudut*

Kolam berbentuk segitiga memiliki dua sisi sepanjang $9$ m dan $15$ m yang membentuk sudut $60^{\circ}$. Panjang sisi ketiga kolam tersebut adalah ... m.

- A. $3 \sqrt{34}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>
- **B. $3 \sqrt{19}$** ✅  
  <sub>Benar: $s^2 = 81 + 225 - 135 = 171$</sub>
- C. $21$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$ padahal rumus memakai $-2ab\cos$</sub>
- D. $\frac{3 \sqrt{106}}{2}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>

**Pembahasan:** $s^2 = 9^2 + 15^2 - 2(9)(15)\cos 60^{\circ} = 306 - 135 = 171$, sehingga $s = 3\sqrt{19}$ m.
**Acuan:** siswa — siswa hal.163

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b03-e-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: jarak dua pesawat dengan arah melewati utara*

Dua pesawat terbang meninggalkan bandara pada waktu yang sama dan terbang selama 2 jam. Pesawat A terbang ke arah 340° dengan kecepatan 50 km/jam dan pesawat B terbang ke arah 40° dengan kecepatan 80 km/jam. Berapakah jarak kedua pesawat tersebut setelah 2 jam (dalam km)? (Besar sudut diukur dari arah utara searah putaran jarum jam.)

- A. $20 \sqrt{69}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- B. $20 \sqrt{129}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$</sub>
- C. $20 \sqrt{89}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>
- **D. $140$** ✅  
  <sub>Benar: jarak tempuh 100 km dan 160 km; sudut apit $(40+360)-340 = 60^{\circ}$; $d^2 = 100^2 + 160^2 - 2(100)(160)\cos 60^{\circ} = 19.600$</sub>

**Pembahasan:** Jarak tempuh: $A$ = $50 \times 2 = 100$ km, $B$ = $80 \times 2 = 160$ km. Selisih arah melewati utara: $40^{\circ} + 360^{\circ} - 340^{\circ} = 60^{\circ}$. $d^2 = 10.000 + 25.600 - 16.000 = 19.600$, sehingga $d = 140$ km.
**Acuan:** siswa — siswa hal.164 Contoh 3.18

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b03-e-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: jarak dua drone dari arah dan kecepatan (sudut tumpul)*

Dua drone lepas landas dari lapangan yang sama pada waktu yang sama dan terbang selama 5 detik. Drone P terbang ke arah 110° dengan kecepatan 6 m/s dan drone Q terbang ke arah 230° dengan kecepatan 10 m/s. Berapakah jarak kedua drone setelah 5 detik (dalam m)? (Besar sudut diukur dari arah utara searah putaran jarum jam.)

- A. $5 \sqrt{166}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- **B. $70$** ✅  
  <sub>Benar: jarak tempuh 30 m dan 50 m dengan sudut apit $120^{\circ}$: $d^2 = 900 + 2500 + 1500 = 4900$</sub>
- C. $10 \sqrt{34}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>
- D. $10 \sqrt{19}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$ sehingga suku kosinus dikurangkan</sub>

**Pembahasan:** Jarak tempuh $30$ m dan $50$ m, sudut apit $230^{\circ} - 110^{\circ} = 120^{\circ}$. $d^2 = 900 + 2500 - 2(30)(50)(-\frac{1}{2}) = 4900$, sehingga $d = 70$ m.
**Acuan:** siswa — siswa hal.164 Contoh 3.18

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b03-e-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: sudut dari jari-jari lingkaran bersinggungan*

Seorang insinyur menempatkan tiga pipa sehingga saling bersinggungan di luar. Misalkan pipa dengan pusat A, B, dan C mempunyai jari-jari berturut-turut 4 cm, 6 cm, dan 10 cm. Berapakah besar sudut ABC dalam segitiga ABC (segitiga yang titik sudutnya pusat ketiga pipa)?

- A. $45^{\circ}$  
  <sub>Salah: mengira $\cos = \frac{1}{2}$ sama dengan $\cos 45^{\circ}$</sub>
- B. $120^{\circ}$  
  <sub>Salah: salah tanda pada pembilang sehingga $\cos B = -\frac{1}{2}$</sub>
- **C. $60^{\circ}$** ✅  
  <sub>Benar: $AB = 10$, $BC = 16$, $AC = 14$; $\cos B = \frac{100 + 256 - 196}{320} = \frac{1}{2}$</sub>
- D. $30^{\circ}$  
  <sub>Salah: mengira $\cos = \frac{1}{2}$ untuk sudut $30^{\circ}$ (tertukar dengan sinus)</sub>

**Pembahasan:** Dua pipa yang bersinggungan di luar berjarak pusat sama dengan jumlah jari-jarinya: $AB = 4 + 6 = 10$, $BC = 6 + 10 = 16$, $AC = 4 + 10 = 14$. $\cos B = \frac{AB^2 + BC^2 - AC^2}{2(AB)(BC)} = \frac{100 + 256 - 196}{320} = \frac{1}{2}$, sehingga $B = 60^{\circ}$.
**Acuan:** siswa — siswa hal.166 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b03-e-medium-bt01-004
*variasi (konteks) | C4 | 3 langkah | jenis: sudut dari jari-jari bola bersinggungan*

Tiga bola besi saling bersinggungan di luar di atas sebuah meja. Bola P, Q, dan R mempunyai jari-jari berturut-turut 1 dm, 5 dm, dan 9 dm. Berapakah besar sudut QPR pada segitiga yang titik sudutnya pusat ketiga bola?

- A. $135^{\circ}$  
  <sub>Salah: mengira $\cos = -\frac{1}{2}$ sama dengan $\cos 135^{\circ}$</sub>
- B. $150^{\circ}$  
  <sub>Salah: mengira $\cos = -\frac{1}{2}$ untuk sudut $150^{\circ}$</sub>
- **C. $120^{\circ}$** ✅  
  <sub>Benar: $PQ = 6$, $PR = 10$, $QR = 14$; $\cos P = \frac{36 + 100 - 196}{120} = -\frac{1}{2}$</sub>
- D. $60^{\circ}$  
  <sub>Salah: mengabaikan tanda minus pada nilai kosinus</sub>

**Pembahasan:** $PQ = 1 + 5 = 6$, $PR = 1 + 9 = 10$, $QR = 5 + 9 = 14$. $\cos P = \frac{36 + 100 - 196}{2(6)(10)} = -\frac{1}{2}$, sehingga $P = 120^{\circ}$.
**Acuan:** siswa — siswa hal.166 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b03-e-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: sisi dari sudut apit 45 derajat dengan sisi bentuk akar*

Jika $\angle C = 45^{\circ}$, $a = 5$, dan $b = 2\sqrt{2}$, panjang $c$ adalah ....

- A. $\sqrt{23}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- B. $\sqrt{53}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$</sub>
- C. $\sqrt{33}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>
- **D. $\sqrt{13}$** ✅  
  <sub>Benar: $c^2 = 25 + 8 - 2(5)(2\sqrt{2})\cdot\frac{\sqrt{2}}{2} = 33 - 20 = 13$</sub>

**Pembahasan:** $c^2 = a^2 + b^2 - 2ab\cos C = 25 + 8 - 20\sqrt{2}\cdot\frac{\sqrt{2}}{2} = 33 - 20 = 13$, sehingga $c = \sqrt{13}$.
**Acuan:** pretest — kelas11_tl-b03-p0166-latihan-e-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b03-e-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: sisi dari sudut apit 30 derajat dengan sisi bentuk akar*

Jika $\angle C = 30^{\circ}$, $a = 6$, dan $b = 5\sqrt{3}$, panjang $c$ adalah ....

- A. $\sqrt{201}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$</sub>
- B. $\sqrt{111}$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>
- C. $\sqrt{66}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- **D. $\sqrt{21}$** ✅  
  <sub>Benar: $c^2 = 36 + 75 - 2(6)(5\sqrt{3})\cdot\frac{\sqrt{3}}{2} = 111 - 90 = 21$</sub>

**Pembahasan:** $c^2 = 36 + 75 - 60\sqrt{3}\cdot\frac{\sqrt{3}}{2} = 111 - 90 = 21$, sehingga $c = \sqrt{21}$.
**Acuan:** pretest — kelas11_tl-b03-p0166-latihan-e-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b03-e-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: sudut dari tiga sisi bentuk akar (45 derajat)*

Jika $a = 5$, $b = \sqrt{17}$, dan $c = 4\sqrt{2}$, besar sudut $B$ adalah ....

- A. $60^{\circ}$  
  <sub>Salah: mengira $\cos B = \frac{1}{2}$ setelah salah merasionalkan $\frac{1}{\sqrt{2}}$</sub>
- **B. $45^{\circ}$** ✅  
  <sub>Benar: $\cos B = \frac{25 + 32 - 17}{2(5)(4\sqrt{2})} = \frac{40}{40\sqrt{2}} = \frac{\sqrt{2}}{2}$</sub>
- C. $135^{\circ}$  
  <sub>Salah: salah tanda pada pembilang sehingga $\cos B = -\frac{\sqrt{2}}{2}$</sub>
- D. $30^{\circ}$  
  <sub>Salah: mengambil $\cos B = \frac{\sqrt{3}}{2}$ (tertukar nilai istimewa)</sub>

**Pembahasan:** $\cos B = \frac{a^2 + c^2 - b^2}{2ac} = \frac{25 + 32 - 17}{40\sqrt{2}} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$, sehingga $B = 45^{\circ}$.
**Acuan:** pretest — kelas11_tl-b03-p0166-latihan-e-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b03-e-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: sudut tumpul dari tiga sisi bentuk akar (150 derajat)*

Jika $a = 2$, $b = 7$, dan $c = 3\sqrt{3}$, besar sudut $B$ adalah ....

- **A. $150^{\circ}$** ✅  
  <sub>Benar: $\cos B = \frac{4 + 27 - 49}{2(2)(3\sqrt{3})} = \frac{-18}{12\sqrt{3}} = -\frac{\sqrt{3}}{2}$</sub>
- B. $135^{\circ}$  
  <sub>Salah: mengira $\cos B = -\frac{\sqrt{2}}{2}$</sub>
- C. $120^{\circ}$  
  <sub>Salah: mengira $\cos B = -\frac{1}{2}$</sub>
- D. $30^{\circ}$  
  <sub>Salah: mengabaikan tanda minus pada nilai kosinus</sub>

**Pembahasan:** $\cos B = \frac{a^2 + c^2 - b^2}{2ac} = \frac{4 + 27 - 49}{12\sqrt{3}} = -\frac{3}{2\sqrt{3}} = -\frac{\sqrt{3}}{2}$, sehingga $B = 150^{\circ}$.
**Acuan:** pretest — kelas11_tl-b03-p0166-latihan-e-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b03-e-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: sudut di titik tertentu dengan sisi bentuk akar*

Sebuah segitiga PQR dengan panjang sisi PQ, PR, dan QR secara berturut-turut adalah 8 cm, 4 cm, dan $4\sqrt{3}$ cm. Berapa besar sudut Q?

- A. $90^{\circ}$  
  <sub>Salah: mengira segitiga siku-siku di $Q$ (menerapkan Pythagoras $PQ^2 + QR^2 = PR^2$ tanpa dicek)</sub>
- B. $60^{\circ}$  
  <sub>Salah: mengira $\cos Q = \frac{1}{2}$ (tertukar nilai istimewa)</sub>
- **C. $30^{\circ}$** ✅  
  <sub>Benar: $\cos Q = \frac{64 + 48 - 16}{2(8)(4\sqrt{3})} = \frac{96}{64\sqrt{3}} = \frac{\sqrt{3}}{2}$</sub>
- D. $150^{\circ}$  
  <sub>Salah: salah tanda pada pembilang sehingga $\cos Q = -\frac{\sqrt{3}}{2}$</sub>

**Pembahasan:** Sudut $Q$ diapit $PQ = 8$ dan $QR = 4\sqrt{3}$, berhadapan dengan $PR = 4$. $\cos Q = \frac{PQ^2 + QR^2 - PR^2}{2(PQ)(QR)} = \frac{64 + 48 - 16}{64\sqrt{3}} = \frac{\sqrt{3}}{2}$, sehingga $Q = 30^{\circ}$.
**Acuan:** siswa — siswa hal.163 Mari Mencoba 3.17

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b03-e-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: sudut jajargenjang dari diagonal*

Jajargenjang $ABCD$ memiliki $AB = 5$ cm, $AD = 8$ cm, dan diagonal $BD = 7$ cm. Besar $\angle ABC$ adalah ....

- A. $150^{\circ}$  
  <sub>Salah: mengurangkan $30^{\circ}$ dari $180^{\circ}$ setelah salah menentukan $\angle DAB$</sub>
- **B. $120^{\circ}$** ✅  
  <sub>Benar: $\cos A = \frac{25 + 64 - 49}{80} = \frac{1}{2}$ sehingga $\angle DAB = 60^{\circ}$ dan $\angle ABC = 180^{\circ} - 60^{\circ}$</sub>
- C. $60^{\circ}$  
  <sub>Salah: menjawab $\angle DAB$, bukan $\angle ABC$</sub>
- D. $30^{\circ}$  
  <sub>Salah: mengira $\cos = \frac{1}{2}$ untuk sudut $30^{\circ}$</sub>

**Pembahasan:** $BD$ berhadapan dengan $\angle A$. $\cos A = \frac{AB^2 + AD^2 - BD^2}{2(AB)(AD)} = \frac{1}{2}$, $A = 60^{\circ}$. Sudut berdekatan pada jajargenjang berjumlah $180^{\circ}$, sehingga $\angle ABC = 120^{\circ}$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b03-e-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: hasil kali dua sisi dari jumlah sisi dan sudut*

Pada segitiga $ABC$ diketahui $\angle A = 60^{\circ}$, $a = 7$, dan $b + c = 11$. Nilai $bc$ adalah ....

- **A. $24$** ✅  
  <sub>Benar: $49 = b^2 + c^2 - bc = (b + c)^2 - 3bc = 121 - 3bc$, sehingga $bc = 24$</sub>
- B. $36$  
  <sub>Salah: menulis $a^2 = (b + c)^2 - 2bc$ (suku kosinus diabaikan)</sub>
- C. $18$  
  <sub>Salah: menghitung $2bc\cos 60^{\circ}$ sebagai $2bc$ sehingga $4bc = 72$</sub>
- D. $72$  
  <sub>Salah: lupa membagi $3$ pada $3bc = 72$</sub>

**Pembahasan:** $a^2 = b^2 + c^2 - 2bc\cos 60^{\circ} = b^2 + c^2 - bc = (b+c)^2 - 3bc$. Maka $49 = 121 - 3bc$ dan $bc = 24$ (mis. $b = 3$, $c = 8$).
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b03-e-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: sudut terbesar dari perbandingan sisi*

Perbandingan panjang sisi-sisi suatu segitiga adalah $3 : 5 : 7$. Besar sudut terbesar segitiga tersebut adalah ....

- A. $150^{\circ}$  
  <sub>Salah: mengira $\cos = -\frac{1}{2}$ untuk sudut $150^{\circ}$</sub>
- B. $60^{\circ}$  
  <sub>Salah: mengabaikan tanda minus pada nilai kosinus</sub>
- **C. $120^{\circ}$** ✅  
  <sub>Benar: $\cos = \frac{9k^2 + 25k^2 - 49k^2}{30k^2} = -\frac{1}{2}$</sub>
- D. $90^{\circ}$  
  <sub>Salah: mengira segitiga siku-siku padahal $3^2 + 5^2 = 34 \neq 49$</sub>

**Pembahasan:** Sudut terbesar berhadapan dengan sisi $7k$. $\cos = \frac{(3k)^2 + (5k)^2 - (7k)^2}{2(3k)(5k)} = \frac{-15k^2}{30k^2} = -\frac{1}{2}$, sehingga sudutnya $120^{\circ}$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b03-e-medium-bt01-013
*orisinal | C4 | 4 langkah | jenis: menyusun persamaan dari sudut terbesar dan sisi aljabar*

Sisi-sisi sebuah segitiga panjangnya $x$, $x + 2$, dan $x + 4$ (dalam cm). Jika sudut terbesar segitiga itu $120^{\circ}$, panjang sisi terpendek adalah ... cm.

- **A. $3$** ✅  
  <sub>Benar: $(x+4)^2 = x^2 + (x+2)^2 + x(x+2)$ menjadi $x^2 - x - 6 = 0$, sehingga $x = 3$ (akar $-2$ ditolak)</sub>
- B. $-2$  
  <sub>Salah: memakai tanda $-2ab\cos$ dengan $\cos 120^{\circ}$ dihitung $+\frac{1}{2}$ lalu tidak menolak nilai negatif</sub>
- C. $7$  
  <sub>Salah: memilih sisi terpanjang $x + 4$ sebagai jawaban</sub>
- D. $5$  
  <sub>Salah: memilih sisi tengah $x + 2$ sebagai jawaban</sub>

**Pembahasan:** Sisi terpanjang $x + 4$ di hadapan sudut $120^{\circ}$: $(x+4)^2 = x^2 + (x+2)^2 - 2x(x+2)(-\frac{1}{2})$. Diperoleh $x^2 - x - 6 = 0$, $(x - 3)(x + 2) = 0$. Panjang tidak boleh negatif, jadi $x = 3$ (sisi $3, 5, 7$).
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b03-e-medium-bt01-014
*orisinal | C4 | 4 langkah | jenis: banyak sisi bulat agar segitiga lancip*

Dua sisi sebuah segitiga panjangnya $5$ cm dan $7$ cm. Jika panjang sisi ketiga $c$ adalah bilangan bulat dan ketiga sudut segitiga itu lancip, banyak nilai $c$ yang mungkin adalah ....

- **A. $4$** ✅  
  <sub>Benar: $c^2 < 5^2 + 7^2 = 74$ dan $7^2 < 5^2 + c^2$ (jadi $c^2 > 24$), sehingga $c = 5, 6, 7, 8$</sub>
- B. $7$  
  <sub>Salah: hanya memakai syarat $c^2 > 24$ (menghitung $c = 5, \ldots, 11$)</sub>
- C. $9$  
  <sub>Salah: hanya memakai ketaksamaan segitiga ($c = 3, \ldots, 11$)</sub>
- D. $6$  
  <sub>Salah: hanya memakai syarat $c^2 < 74$ (menghitung $c = 3, \ldots, 8$)</sub>

**Pembahasan:** Sudut terbesar lancip bila kuadrat sisi terpanjang kurang dari jumlah kuadrat dua sisi lain. Bila $c$ terpanjang: $c^2 < 74$, sehingga $c \le 8$. Bila $7$ terpanjang: $49 < 25 + c^2$, sehingga $c \ge 5$. Nilai: $5, 6, 7, 8$ (4 nilai).
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b03-e-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: banyak sisi bulat agar sudut tumpul*

Pada segitiga $ABC$ diketahui $b = 8$ dan $c = 15$ (dalam cm). Jika $\angle A$ tumpul dan $a$ bilangan bulat, banyak nilai $a$ yang mungkin adalah ....

- A. $6$  
  <sub>Salah: memasukkan $a = 17$ (memakai $a^2 \ge 289$, padahal $a = 17$ memberi sudut siku-siku)</sub>
- B. $4$  
  <sub>Salah: memakai batas atas $a < 22$ (menghilangkan $a = 22$)</sub>
- C. $15$  
  <sub>Salah: hanya memakai ketaksamaan segitiga $7 < a < 23$</sub>
- **D. $5$** ✅  
  <sub>Benar: $a^2 > 64 + 225 = 289$ sehingga $a > 17$, dan $a < 8 + 15 = 23$; nilai $a = 18, \ldots, 22$</sub>

**Pembahasan:** $\angle A$ tumpul bila $\cos A < 0$, yaitu $a^2 > b^2 + c^2 = 289$, jadi $a > 17$. Ketaksamaan segitiga: $a < 23$. Bilangan bulat: $18, 19, 20, 21, 22$ (5 nilai).
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b03-e-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: jarak dari titik awal pada lintasan berbelok*

Seorang pejalan berangkat dari titik $A$, berjalan $8$ km ke titik $B$ pada arah $30^{\circ}$, lalu berjalan $15$ km ke titik $C$ pada arah $150^{\circ}$ (arah diukur dari utara searah putaran jarum jam). Jarak $A$ ke $C$ adalah ... km.

- A. $\sqrt{229}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- B. $17$  
  <sub>Salah: mengabaikan suku kosinus (seperti Pythagoras)</sub>
- C. $\sqrt{409}$  
  <sub>Salah: memakai sudut belokan $120^{\circ}$ sebagai sudut dalam segitiga</sub>
- **D. $13$** ✅  
  <sub>Benar: sudut dalam di $B$ adalah $180^{\circ} - (150^{\circ} - 30^{\circ}) = 60^{\circ}$; $AC^2 = 64 + 225 - 120 = 169$</sub>

**Pembahasan:** Arah kembali dari $B$ ke $A$ adalah $210^{\circ}$, arah $B$ ke $C$ adalah $150^{\circ}$, sehingga $\angle ABC = 60^{\circ}$. $AC^2 = 8^2 + 15^2 - 2(8)(15)\cos 60^{\circ} = 289 - 120 = 169$, sehingga $AC = 13$ km.
**Acuan:** siswa — siswa hal.163

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b03-e-medium-bt01-017
*orisinal | C4 | 4 langkah | jenis: sudut segi empat lewat dua segitiga*

Pada segi empat $ABCD$ diketahui $AB = 5$ cm, $BC = 8$ cm, $\angle ABC = 60^{\circ}$, $CD = 5$ cm, dan $AD = 3$ cm. Besar $\angle ADC$ adalah ....

- A. $60^{\circ}$  
  <sub>Salah: mengabaikan tanda minus pada nilai kosinus</sub>
- **B. $120^{\circ}$** ✅  
  <sub>Benar: $AC^2 = 25 + 64 - 40 = 49$ sehingga $AC = 7$; $\cos D = \frac{9 + 25 - 49}{30} = -\frac{1}{2}$</sub>
- C. $135^{\circ}$  
  <sub>Salah: mengira $\cos = -\frac{1}{2}$ sama dengan $\cos 135^{\circ}$</sub>
- D. $150^{\circ}$  
  <sub>Salah: mengira $\cos = -\frac{1}{2}$ untuk sudut $150^{\circ}$</sub>

**Pembahasan:** Diagonal $AC$ dari $\triangle ABC$: $AC^2 = 25 + 64 - 2(5)(8)\cos 60^{\circ} = 49$, $AC = 7$. Pada $\triangle ACD$: $\cos D = \frac{AD^2 + CD^2 - AC^2}{2(AD)(CD)} = \frac{9 + 25 - 49}{30} = -\frac{1}{2}$, sehingga $\angle ADC = 120^{\circ}$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b03-e-medium-bt01-018
*orisinal | C4 | 3 langkah | jenis: menemukan kesalahan langkah hitung*

Rina menghitung sisi $c$ pada segitiga $ABC$ dengan $\angle C = 120^{\circ}$, $a = 6$, dan $b = 10$. Langkahnya: $c^2 = 6^2 + 10^2 - 2(6)(10)\cos 120^{\circ} = 136 - 120\cdot\frac{1}{2} = 76$, sehingga $c = \sqrt{76}$. Kesalahan Rina terletak pada ....

- **A. nilai $\cos 120^{\circ}$ yang seharusnya $-\frac{1}{2}$, sehingga $c^2 = 196$** ✅  
  <sub>Benar: $\cos 120^{\circ} = -\frac{1}{2}$, bukan $\frac{1}{2}$, sehingga suku $-2ab\cos C$ bernilai $+60$</sub>
- B. rumus yang seharusnya $c^2 = a^2 + b^2 + 2ab\cos C$  
  <sub>Salah: rumus Aturan Kosinus yang dikutip sudah benar, tanda minus tidak perlu diganti</sub>
- C. faktor $2$ yang seharusnya tidak ada pada suku $2ab\cos C$  
  <sub>Salah: faktor $2$ memang ada pada rumus</sub>
- D. besar sudut $C$ yang seharusnya $60^{\circ}$  
  <sub>Salah: sudut $C = 120^{\circ}$ diberikan pada soal</sub>

**Pembahasan:** Rumus dan substitusi awal benar, tetapi $\cos 120^{\circ} = -\frac{1}{2}$. Seharusnya $c^2 = 36 + 100 - 120\cdot(-\frac{1}{2}) = 196$ sehingga $c = 14$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b03-e-medium-bt01-019
*orisinal | C4 | 3 langkah | jenis: panjang ruas garis dari titik pada sisi segitiga*

Pada segitiga $ABC$ diketahui $AB = 8$ cm, $BC = 10$ cm, dan $\angle B = 60^{\circ}$. Titik $D$ terletak pada $BC$ dengan $BD = 3$ cm. Panjang $AD$ adalah ... cm.

- A. $\sqrt{61}$  
  <sub>Salah: lupa faktor 2 pada suku $2ab\cos$</sub>
- B. $2\sqrt{21}$  
  <sub>Salah: memakai $BC = 10$ (menghitung $AC$), bukan $BD = 3$</sub>
- **C. $7$** ✅  
  <sub>Benar: pada $\triangle ABD$: $AD^2 = 64 + 9 - 2(8)(3)\cos 60^{\circ} = 49$</sub>
- D. $\sqrt{97}$  
  <sub>Salah: salah tanda: memakai $+2ab\cos$</sub>

**Pembahasan:** $\angle ABD = \angle ABC = 60^{\circ}$ karena $D$ pada $BC$. $AD^2 = AB^2 + BD^2 - 2(AB)(BD)\cos 60^{\circ} = 64 + 9 - 24 = 49$, sehingga $AD = 7$ cm.
**Acuan:** siswa — siswa hal.163

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b03-e-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: waktu agar jarak tertentu tercapai*

Dua pelari berangkat bersamaan dari titik $O$ pada lintasan lurus yang membentuk sudut $120^{\circ}$. Pelari pertama berlari dengan kecepatan $3$ m/s dan pelari kedua $5$ m/s. Setelah ... detik, jarak kedua pelari tepat $84$ m.

- A. $10{,}5$  
  <sub>Salah: memakai $d = (3 + 5)t$ (menjumlahkan kecepatan seolah sejalan)</sub>
- **B. $12$** ✅  
  <sub>Benar: $d^2 = (3t)^2 + (5t)^2 - 2(3t)(5t)\cos 120^{\circ} = 49t^2$ sehingga $d = 7t = 84$ dan $t = 12$</sub>
- C. $144$  
  <sub>Salah: lupa menarik akar: $t^2 = 144$ dianggap $t$</sub>
- D. $42$  
  <sub>Salah: memakai $d = (5 - 3)t$</sub>

**Pembahasan:** Jarak tempuh $3t$ dan $5t$ dengan sudut apit $120^{\circ}$: $d^2 = 9t^2 + 25t^2 + 15t^2 = 49t^2$, sehingga $d = 7t$. Dari $7t = 84$ diperoleh $t = 12$ detik.
**Acuan:** siswa — siswa hal.163

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b03-e-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal klaim jenis segitiga*

Seorang siswa mengklaim: "Jika $a^2 + b^2 > c^2$ pada suatu segitiga dengan sisi $a$, $b$, $c$, maka segitiga itu pasti lancip." Segitiga yang merupakan contoh penyangkal klaim tersebut adalah segitiga dengan ....

- A. $a = 6$, $b = 7$, $c = 8$  
  <sub>Salah: premis terpenuhi tetapi ketiga sudutnya lancip (64 < 85, 49 < 100, 36 < 113), bukan penyangkal</sub>
- B. $a = 5$, $b = 6$, $c = 10$  
  <sub>Salah: premis tidak terpenuhi ($25 + 36 = 61 < 100$); segitiga tumpul tetapi tidak menyangkal klaim</sub>
- **C. $a = 4$, $b = 8$, $c = 5$** ✅  
  <sub>Benar: $4^2 + 8^2 = 80 > 25 = 5^2$ (premis terpenuhi), tetapi $b^2 = 64 > 4^2 + 5^2 = 41$ sehingga sudut $B$ tumpul; jadi bukan lancip</sub>
- D. $a = 5$, $b = 12$, $c = 13$  
  <sub>Salah: premis tidak terpenuhi ($25 + 144 = 169$ sama dengan $c^2$), segitiga siku-siku; bukan penyangkal</sub>

**Pembahasan:** Penyangkal harus memenuhi premis $a^2 + b^2 > c^2$ namun tidak lancip. Hanya $a=4, b=8, c=5$: $80 > 25$ tetapi $\cos B = \frac{16 + 25 - 64}{40} < 0$, jadi $B$ tumpul. Syarat $a^2+b^2>c^2$ hanya menjamin sudut $C$ lancip.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b03-e-hard-bt01-002
*orisinal | C5 | 5 langkah | jenis: banyak nilai bulat agar segitiga tumpul (dua kasus)*

Dua sisi sebuah segitiga panjangnya $6$ cm dan $9$ cm, sedangkan sisi ketiga $k$ cm dengan $k$ bilangan bulat. Banyak nilai $k$ sehingga segitiga tersebut ada dan tumpul adalah ....

- A. $11$  
  <sub>Salah: menghitung semua $k$ yang membentuk segitiga ($3 < k < 15$) tanpa syarat tumpul</sub>
- B. $4$  
  <sub>Salah: hanya meninjau kasus $k$ sebagai sisi terpanjang</sub>
- **C. $7$** ✅  
  <sub>Benar: tumpul di sudut hadapan $k$: $k^2 > 117$ dan $k < 15$ memberi $k = 11, 12, 13, 14$ (4 nilai); tumpul di sudut hadapan 9: $81 > 36 + k^2$ dan $k > 3$ memberi $k = 4, 5, 6$ (3 nilai); total 7</sub>
- D. $3$  
  <sub>Salah: hanya meninjau kasus sisi 9 sebagai sisi terpanjang</sub>

**Pembahasan:** Syarat ada: $3 < k < 15$. Tumpul bila sisi terpanjang kuadratnya melebihi jumlah kuadrat dua sisi lain. Kasus $k$ terpanjang: $k^2 > 6^2 + 9^2 = 117$ sehingga $k = 11..14$. Kasus 9 terpanjang: $9^2 > 6^2 + k^2$ sehingga $k^2 < 45$, $k = 4,5,6$. Total $4 + 3 = 7$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b03-e-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: merancang segitiga memenuhi dua syarat*

Seorang perancang ingin membuat bingkai segitiga yang sisi ketiganya berukuran bilangan bulat (dalam cm) dan segitiganya tumpul. Rancangan dua sisi dan sudut apit yang memenuhi kedua syarat itu adalah ....

- **A. dua sisi $3$ dan $5$ dengan sudut apit $120^{\circ}$** ✅  
  <sub>Benar: $c^2 = 9 + 25 - 30\cos 120^{\circ} = 49$ sehingga $c = 7$ (bulat) dan sudut apit $120^{\circ}$ tumpul</sub>
- B. dua sisi $5$ dan $8$ dengan sudut apit $60^{\circ}$  
  <sub>Salah: sisi ketiga $7$ bulat, tetapi $49 < 25 + 64$ dan seluruh sudut lancip (hanya memenuhi satu syarat)</sub>
- C. dua sisi $6$ dan $8$ dengan sudut apit $90^{\circ}$  
  <sub>Salah: sisi ketiga $10$ bulat, tetapi sudut apitnya siku-siku, bukan tumpul</sub>
- D. dua sisi $4$ dan $6$ dengan sudut apit $120^{\circ}$  
  <sub>Salah: segitiga tumpul tetapi $c^2 = 16 + 36 + 24 = 76$ sehingga $c = 2\sqrt{19}$ tidak bulat</sub>

**Pembahasan:** Hitung sisi ketiga tiap rancangan dengan $c^2 = p^2 + q^2 - 2pq\cos\theta$ lalu uji jenis segitiga. Hanya rancangan $3$, $5$, $120^{\circ}$ yang memberi $c = 7$ dan tumpul.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b03-e-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: memilih metode (aturan sinus atau kosinus) dari data*

Pada segitiga $ABC$, empat kelompok data berikut diketahui (sisi dalam cm). Kelompok data yang membuat aturan sinus tidak dapat langsung dipakai dan penyelesaian harus dimulai dengan aturan kosinus adalah ....

- A. $\angle A = 30^{\circ}$, $\angle B = 70^{\circ}$, dan $c = 12$  
  <sub>Salah: sudut $C = 80^{\circ}$ langsung diperoleh dan $c$ berhadapan dengannya sehingga aturan sinus dipakai; aturan kosinus tidak bisa karena hanya satu sisi diketahui</sub>
- B. $a = 9$, $b = 6$, dan $\angle A = 50^{\circ}$  
  <sub>Salah: ada pasangan $a$ dan $\angle A$ berhadapan sehingga aturan sinus langsung bisa dipakai</sub>
- **C. $a = 9$, $b = 6$, dan $\angle C = 50^{\circ}$** ✅  
  <sub>Benar: sudut $C$ diketahui tetapi sisi $c$ yang berhadapan dengannya tidak, dan tidak ada pasangan sisi-sudut berhadapan yang lengkap; dua sisi mengapit sudut $C$ sehingga aturan kosinus langsung dipakai untuk $c$</sub>
- D. $\angle A = 40^{\circ}$, $\angle B = 65^{\circ}$, dan $a = 8$  
  <sub>Salah: ada pasangan $a$ dan $\angle A$ berhadapan sehingga aturan sinus langsung bisa dipakai</sub>

**Pembahasan:** Aturan sinus butuh satu pasangan sisi dan sudut berhadapan yang lengkap. Pada $a=9$, $b=6$, $C=50^{\circ}$ tidak ada pasangan itu, namun dua sisi dan sudut apitnya ada, sehingga $c^2 = a^2 + b^2 - 2ab\cos C$ dipakai lebih dulu.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b03-e-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: menemukan kesalahan: faktor 2 pada aturan kosinus*

Dina menghitung sisi $a$ pada segitiga $ABC$ dengan $b = 6$, $c = 10$, dan $\angle A = 60^{\circ}$. Langkahnya: $a^2 = 6^2 + 10^2 - 6 \cdot 10 \cdot \cos 60^{\circ} = 136 - 30 = 106$, sehingga $a = \sqrt{106}$. Pernyataan yang benar tentang pekerjaan Dina adalah ....

- A. Dina salah tanda; seharusnya $a^2 = 136 + 60$ sehingga $a = 14$  
  <sub>Salah: mengira suku $2bc\cos A$ ditambah, padahal dikurangi</sub>
- B. Dina salah memakai kosinus; seharusnya $a = \sqrt{136 - 60\sqrt{3}}$  
  <sub>Salah: mengira $\sin 60^{\circ}$ yang dipakai pada aturan kosinus</sub>
- C. Pekerjaan Dina sudah benar sehingga $a = \sqrt{106}$  
  <sub>Salah: menganggap rumus tanpa faktor 2 benar</sub>
- **D. Dina lupa faktor $2$ pada suku $2bc\cos A$; seharusnya $a = 2\sqrt{19}$** ✅  
  <sub>Benar: suku ketiga seharusnya $2 \cdot 6 \cdot 10 \cdot \frac{1}{2} = 60$, sehingga $a^2 = 136 - 60 = 76$ dan $a = 2\sqrt{19}$</sub>

**Pembahasan:** Aturan kosinus: $a^2 = b^2 + c^2 - 2bc\cos A = 36 + 100 - 120 \cdot \frac{1}{2} = 76$, jadi $a = 2\sqrt{19}$. Dina kehilangan faktor $2$ sehingga mendapat $\sqrt{106}$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b03-e-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: evaluasi hasil aturan sinus (sudut ganda)*

Rudi menentukan sudut terbesar $\theta$ (di hadapan sisi terpanjang) pada segitiga bersisi $11$, $24$, dan $31$ cm. Dengan aturan sinus ia mendapat $\sin\theta = \frac{\sqrt{3}}{2}$, lalu menyimpulkan $\theta = 60^{\circ}$ karena kalkulatornya menampilkan nilai itu. Pernyataan yang benar tentang kesimpulan Rudi adalah ....

- **A. Tidak tepat; $\theta = 120^{\circ}$ karena $\cos\theta = -\frac{1}{2}$** ✅  
  <sub>Benar: $\cos\theta = \frac{11^2 + 24^2 - 31^2}{2 \cdot 11 \cdot 24} = -\frac{1}{2}$ sehingga $\theta = 120^{\circ}$ (tumpul), yang juga memenuhi $\sin\theta = \frac{\sqrt{3}}{2}$</sub>
- B. Tidak tepat; $\theta = 30^{\circ}$ karena $\cos\theta = \frac{1}{2}$  
  <sub>Salah: salah tanda pada pembilang kosinus dan salah sudut</sub>
- C. Tidak tepat; $\theta = 150^{\circ}$ karena $\cos\theta = -\frac{\sqrt{3}}{2}$  
  <sub>Salah: salah menghitung nilai kosinus (menukar nilai sinus dan kosinus)</sub>
- D. Tepat; $\theta = 60^{\circ}$ karena sudut terbesar pasti lancip  
  <sub>Salah: mengabaikan bahwa $\sin\theta$ sama untuk $\theta$ dan $180^{\circ} - \theta$</sub>

**Pembahasan:** $\sin\theta=\frac{\sqrt3}{2}$ dipenuhi oleh $60^{\circ}$ dan $120^{\circ}$. Aturan kosinus: $\cos\theta=\frac{121+576-961}{528}=-\frac12$, sehingga $\theta=120^{\circ}$ (kuadrat sisi terpanjang $961 > 697$).
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b03-e-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: menentukan jenis segitiga dari dua syarat aljabar*

Pada segitiga $ABC$ dengan sisi $a$, $b$, $c$ berlaku $a^2 = b^2 + c^2 - bc$ dan $b + c = 2a$. Segitiga $ABC$ pasti ....

- A. sama kaki dengan sudut puncak $120^{\circ}$  
  <sub>Salah: mengira $\cos A = -\frac{1}{2}$ karena ada tanda minus pada rumus</sub>
- B. siku-siku di $A$  
  <sub>Salah: mengira $a^2 = b^2 + c^2$ meski ada suku $-bc$</sub>
- C. sama kaki dengan $b = c \neq a$  
  <sub>Salah: menduga $b = c$ tanpa memeriksa nilai $a$; padahal $a = b = c$</sub>
- **D. sama sisi** ✅  
  <sub>Benar: $\cos A = \frac{1}{2}$ sehingga $A = 60^{\circ}$; dari $b + c = 2a$ dan $a^2 = (b+c)^2 - 3bc$ diperoleh $bc = a^2$ sehingga $b = c = a$</sub>

**Pembahasan:** $a^2 = b^2 + c^2 - 2bc\cos A$ dibandingkan dengan $a^2 = b^2 + c^2 - bc$ memberi $\cos A = \frac12$. Substitusi $b + c = 2a$: $a^2 = 4a^2 - 3bc$ sehingga $bc = a^2$. Maka $b$ dan $c$ akar $t^2 - 2at + a^2 = 0$, yaitu $b = c = a$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b03-e-hard-bt01-008
*orisinal | C5 | 6 langkah | jenis: banyak segitiga dari dua sisi dan sudut tak apit*

Pada segitiga $ABC$ diketahui $\angle A = 30^{\circ}$, $b = 8$, dan $a$ bilangan bulat positif. Dengan aturan kosinus $a^2 = b^2 + c^2 - 2bc\cos A$ sebagai persamaan dalam $c$, banyak nilai $a$ sehingga terdapat tepat dua segitiga $ABC$ yang berbeda adalah ....

- A. $4$  
  <sub>Salah: ikut menghitung $a = 4$ (diskriminan nol, hanya satu segitiga siku-siku)</sub>
- **B. $3$** ✅  
  <sub>Benar: $c^2 - 8\sqrt{3}c + 64 - a^2 = 0$ punya dua akar positif berbeda bila diskriminan $4a^2 - 64 > 0$ dan $64 - a^2 > 0$, yaitu $4 < a < 8$ sehingga $a = 5, 6, 7$</sub>
- C. $2$  
  <sub>Salah: salah batas: mengira $a = 7$ tidak memberi dua segitiga</sub>
- D. $5$  
  <sub>Salah: ikut menghitung $a = 4$ dan $a = 8$ yang masing-masing hanya memberi satu segitiga</sub>

**Pembahasan:** Persamaan kuadrat $c^2 - 8\sqrt{3}c + (64 - a^2) = 0$ memiliki diskriminan $192 - 4(64 - a^2) = 4a^2 - 64$ dan hasil kali akar $64 - a^2$. Dua akar positif berbeda butuh $a > 4$ dan $a < 8$. Nilai bulatnya $5, 6, 7$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b03-e-hard-bt01-009
*orisinal | C5 | 6 langkah | jenis: jumlah nilai parameter agar segitiga lancip (sisi aljabar)*

Sisi-sisi sebuah segitiga panjangnya $10$, $x$, dan $x + 4$ (dalam cm) dengan $x$ bilangan bulat positif. Jumlah semua nilai $x$ sehingga segitiga tersebut ada dan ketiga sudutnya lancip adalah ....

- **A. $45$** ✅  
  <sub>Benar: ada bila $x > 3$; lancip bila $(x+4)^2 < 100 + x^2$ ($x < 10{,}5$) dan $100 < x^2 + (x+4)^2$ ($x > -2 + \sqrt{46} \approx 4{,}78$); jadi $x = 5, \dots, 10$ dan jumlahnya $45$</sub>
- B. $56$  
  <sub>Salah: memasukkan $x = 11$ yang memberi sisi $10, 11, 15$ dan sudut tumpul</sub>
- C. $49$  
  <sub>Salah: hanya memakai syarat ada segitiga ($x = 4, \dots, 10$) padahal $x = 4$ memberi sudut tumpul</sub>
- D. $35$  
  <sub>Salah: membatasi $x < 10$ sehingga $x = 10$ (sisi $10, 10, 14$ yang lancip) tertinggal</sub>

**Pembahasan:** Untuk tiap $x$ uji sisi terpanjang. $x=4$: sisi $10,4,8$, $100 > 80$ tumpul. $x = 5..10$ lancip (misal $x=10$: $196 < 200$). $x = 11$: $225 > 221$ tumpul. Jumlah $5+6+7+8+9+10 = 45$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b03-e-hard-bt01-010
*orisinal | C5 | 3 langkah | jenis: mengevaluasi kelayakan data ukur dengan nilai kosinus*

Empat kelompok pengukur melaporkan panjang sisi sebuah lahan segitiga (dalam meter). Jika aturan kosinus dipakai untuk menghitung ketiga sudutnya, hasil pengukuran yang menghasilkan nilai kosinus kurang dari $-1$ sehingga datanya tidak mungkin adalah ....

- A. $6$, $10$, dan $15$  
  <sub>Salah: $\cos$ sudut terbesar $= -\frac{89}{120}$, masih dalam $[-1, 1]$ sehingga data mungkin</sub>
- **B. $6$, $7$, dan $15$** ✅  
  <sub>Benar: $\cos C = \frac{6^2 + 7^2 - 15^2}{2 \cdot 6 \cdot 7} = -\frac{140}{84} = -\frac{5}{3} < -1$, tidak ada sudut seperti itu</sub>
- C. $8$, $9$, dan $16$  
  <sub>Salah: $\cos$ sudut terbesar $= -\frac{37}{48}$, masih dalam $[-1, 1]$ sehingga data mungkin</sub>
- D. $5$, $7$, dan $10$  
  <sub>Salah: $\cos$ sudut terbesar $= -\frac{13}{35}$, masih dalam $[-1, 1]$ sehingga data mungkin</sub>

**Pembahasan:** Hitung kosinus sudut di hadapan sisi terpanjang. Hanya $6,7,15$ menghasilkan $-\frac{5}{3} < -1$ (karena $6 + 7 < 15$). Pada tiga data lain nilainya antara $-1$ dan $0$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b03-e-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: kesalahan penalaran: sisi uji bukan terpanjang*

Budi menyelidiki jenis segitiga bersisi $7$ cm, $9$ cm, dan $12$ cm. Ia menulis: "Karena $9^2 = 81 < 7^2 + 12^2 = 193$, maka sudut di hadapan sisi $9$ lancip, sehingga segitiga ini lancip." Pernyataan yang benar tentang kesimpulan Budi adalah ....

- A. Keliru; segitiga siku-siku karena $12^2$ hampir sama dengan $7^2 + 9^2$  
  <sub>Salah: menganggap selisih kecil berarti siku-siku, padahal 144 tidak sama dengan 130</sub>
- B. Benar; ketiga sudut lancip karena $9^2 < 7^2 + 12^2$  
  <sub>Salah: menyimpulkan semua sudut dari satu sudut saja</sub>
- C. Keliru; harus menguji sisi terpendek $7$, dan $7^2 < 9^2 + 12^2$ sehingga segitiga lancip  
  <sub>Salah: menguji sisi terpendek yang tidak menentukan sehingga kesimpulan tetap keliru</sub>
- **D. Keliru; sudut di hadapan sisi terpanjang tumpul karena $12^2 = 144 > 7^2 + 9^2 = 130$** ✅  
  <sub>Benar: sudut di hadapan sisi $9$ memang lancip, tetapi jenis segitiga ditentukan sudut terbesar (hadapan sisi $12$), dan $144 > 130$ sehingga sudutnya tumpul</sub>

**Pembahasan:** Segitiga lancip hanya bila sudut terbesar lancip. Sudut terbesar ada di hadapan sisi $12$: $\cos = \frac{49 + 81 - 144}{126} = -\frac{1}{9} < 0$, tumpul. Budi menguji sisi yang bukan terpanjang.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
