# Lembar koreksi — kelas11_tl SMA11L-B3 subbab C: Identitas Trigonometri

41 soal | easy 20, medium 15, hard 6 | variasi 17, orisinal 24
> **Kapasitas kurang (medium): 15 dari kuota 20** — Subbab C hanya p150-p155: identitas dasar, penjumlahan/pengurangan sudut, dan Latihan C 6 soal. Bukti identitas (Latihan 4b, Contoh 3.13/3.14, Mari Mencoba) berupa gambar sehingga tidak dapat dipakai; acuan siswa/pretest teks sudah banyak terpakai di easy. Soal medium lain akan nyaris kembar atau di luar materi.
> **Kapasitas kurang (hard): 6 dari kuota 20** — Subbab C hanya p150-p155 (identitas dasar, penjumlahan/pengurangan sudut, Latihan C). Bukti identitas bergambar tidak dapat dipakai, dan acuan teks habis di easy dan medium. Soal hard yang layak (evaluasi klaim, syarat domain, temukan kesalahan, rancang identitas) hanya cukup sekitar 6; sisanya menjadi soal kembar atau di luar subbab.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b03-c-easy-bt01-001
*variasi (konteks) | C1 | 1 langkah | jenis: menyederhanakan bentuk sec-tan*

Bentuk paling sederhana dari $\sec^2 t - 1$ adalah ....

- A. $-\tan^2 t$  
  <sub>Salah: tertukar urutan pengurangan sehingga tanda berbalik</sub>
- B. $\sin^2 t$  
  <sub>Salah: mengira sama dengan $1 - \cos^2 t$</sub>
- **C. $\tan^2 t$** ✅  
  <sub>Benar: dari $\tan^2 t + 1 = \sec^2 t$ diperoleh $\sec^2 t - 1 = \tan^2 t$</sub>
- D. $\cot^2 t$  
  <sub>Salah: tertukar tan dan cot</sub>

**Pembahasan:** Identitas Pythagoras: $\tan^2 t + 1 = \sec^2 t$, sehingga $\sec^2 t - 1 = \tan^2 t$.
**Acuan:** pretest — kelas11_tl-b03-p0155-latihan-c-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b03-c-easy-bt01-002
*variasi (konteks) | C2 | 2 langkah | jenis: menjumlahkan identitas Pythagoras*

Untuk $t$ yang membuat semua bentuknya terdefinisi, $\sin^2 t + \cos^2 t + \tan^2 t$ sama dengan ....

- **A. $\sec^2 t$** ✅  
  <sub>Benar: $\sin^2 t + \cos^2 t = 1$, lalu $1 + \tan^2 t = \sec^2 t$</sub>
- B. $1$  
  <sub>Salah: lupa menambahkan suku $\tan^2 t$</sub>
- C. $\csc^2 t$  
  <sub>Salah: tertukar sec dan csc</sub>
- D. $\tan^2 t + 2$  
  <sub>Salah: mengira $\sin^2 t + \cos^2 t = 2$</sub>

**Pembahasan:** $\sin^2 t + \cos^2 t = 1$, sehingga bentuknya menjadi $1 + \tan^2 t = \sec^2 t$.
**Acuan:** pretest — kelas11_tl-b03-p0155-latihan-c-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b03-c-easy-bt01-003
*variasi (angka) | C2 | 1 langkah | jenis: nilai kosinus dari sekan*

Jika $\sec u = -\frac{13}{12}$, maka nilai $\cos u$ adalah ....

- A. $\frac{13}{12}$  
  <sub>Salah: tidak membalik dan tanda tertukar</sub>
- B. $\frac{12}{13}$  
  <sub>Salah: membalik tetapi lupa tanda negatif</sub>
- C. $-\frac{13}{12}$  
  <sub>Salah: tidak membalik pecahan</sub>
- **D. $-\frac{12}{13}$** ✅  
  <sub>Benar: $\cos u = \frac{1}{\sec u}$</sub>

**Pembahasan:** $\cos u = \frac{1}{\sec u} = \frac{1}{-13/12} = -\frac{12}{13}$.
**Acuan:** siswa — siswa hal.155 Latihan C Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b03-c-easy-bt01-004
*variasi (angka) | C2 | 1 langkah | jenis: nilai sinus dari kosekan*

Diketahui $\csc v = -\frac{11}{6}$. Nilai $\sin v$ adalah ....

- **A. $-\frac{6}{11}$** ✅  
  <sub>Benar: $\sin v = \frac{1}{\csc v}$</sub>
- B. $-\frac{11}{6}$  
  <sub>Salah: tidak membalik pecahan</sub>
- C. $\frac{11}{6}$  
  <sub>Salah: tidak membalik dan tanda berubah</sub>
- D. $\frac{6}{11}$  
  <sub>Salah: lupa tanda negatif</sub>

**Pembahasan:** $\sin v = \frac{1}{\csc v} = -\frac{6}{11}$.
**Acuan:** siswa — siswa hal.155 Latihan C Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b03-c-easy-bt01-005
*variasi (konteks) | C2 | 2 langkah | jenis: mengubah identitas Pythagoras*

Dari identitas $\sin^2 t + \cos^2 t = 1$, pernyataan yang benar tentang $\cos t$ adalah ....

- A. $\cos t = \sqrt{1 - \sin^2 t}$  
  <sub>Salah: lupa tanda $\pm$ saat menarik akar</sub>
- **B. $\cos t = \pm\sqrt{1 - \sin^2 t}$** ✅  
  <sub>Benar: $\cos^2 t = 1 - \sin^2 t$ lalu diakarkan, hasilnya dapat positif atau negatif</sub>
- C. $\cos t = \pm(1 - \sin t)$  
  <sub>Salah: menarik akar tiap suku secara terpisah</sub>
- D. $\cos t = 1 - \sin^2 t$  
  <sub>Salah: lupa menarik akar</sub>

**Pembahasan:** $\cos^2 t = 1 - \sin^2 t$, sehingga $\cos t = \pm\sqrt{1 - \sin^2 t}$.
**Acuan:** siswa — siswa hal.155 Latihan C Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b03-c-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: mengubah identitas tan-sec*

Dari identitas $\tan^2 t + 1 = \sec^2 t$, pernyataan yang benar tentang $\sec t$ adalah ....

- A. $\sec t = \sqrt{1 + \tan^2 t}$  
  <sub>Salah: lupa tanda $\pm$</sub>
- B. $\sec t = \pm\sqrt{\tan^2 t - 1}$  
  <sub>Salah: salah tanda di dalam akar</sub>
- C. $\sec t = 1 + \tan t$  
  <sub>Salah: menarik akar tiap suku</sub>
- **D. $\sec t = \pm\sqrt{1 + \tan^2 t}$** ✅  
  <sub>Benar: $\sec^2 t = 1 + \tan^2 t$ lalu diakarkan dengan dua tanda</sub>

**Pembahasan:** $\sec^2 t = 1 + \tan^2 t$, sehingga $\sec t = \pm\sqrt{1 + \tan^2 t}$.
**Acuan:** siswa — siswa hal.155 Latihan C Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b03-c-easy-bt01-007
*variasi (konteks) | C2 | 2 langkah | jenis: contoh penyangkal jumlah sudut*

Persamaan $\cos(x + y) = \cos x + \cos y$ bukan identitas. Pasangan $(x, y)$ yang dapat dipakai sebagai contoh penyangkal adalah ....

- **A. $\left(\frac{\pi}{3}, \frac{\pi}{3}\right)$** ✅  
  <sub>Benar: untuk $x = y = \pi/3$: ruas kiri $\cos(2\pi/3) = -\frac{1}{2}$, ruas kanan $\frac{1}{2} + \frac{1}{2} = 1$ (berbeda)</sub>
- B. $\left(\frac{3\pi}{4}, \frac{\pi}{2}\right)$  
  <sub>Salah: kedua ruas sama ($-\frac{\sqrt{2}}{2}$), bukan penyangkal</sub>
- C. $\left(-\frac{\pi}{4}, \frac{\pi}{2}\right)$  
  <sub>Salah: kedua ruas sama ($\frac{\sqrt{2}}{2}$), bukan penyangkal</sub>
- D. $\left(\frac{7\pi}{4}, \frac{\pi}{2}\right)$  
  <sub>Salah: kedua ruas sama ($\frac{\sqrt{2}}{2}$), bukan penyangkal</sub>

**Pembahasan:** Contoh penyangkal adalah pasangan yang membuat kedua ruas berbeda. Untuk $x = y = \frac{\pi}{3}$ ruas kiri $-\frac{1}{2}$, ruas kanan $1$. Tiga pasangan lain membuat kedua ruas sama sehingga tidak menyangkal.
**Acuan:** siswa — siswa hal.155 Latihan C Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b03-c-easy-bt01-008
*variasi (konteks) | C2 | 2 langkah | jenis: contoh penyangkal sin+cos*

Persamaan $\sin x + \cos x = 1$ bukan identitas. Nilai $x$ yang dapat dipakai sebagai contoh penyangkal adalah ....

- A. $x = \frac{\pi}{2}$  
  <sub>Salah: ruas kiri $1 + 0 = 1$, kedua ruas sama</sub>
- **B. $x = \frac{\pi}{4}$** ✅  
  <sub>Benar: $\sin\frac{\pi}{4} + \cos\frac{\pi}{4} = \sqrt{2} \ne 1$</sub>
- C. $x = 0$  
  <sub>Salah: ruas kiri $0 + 1 = 1$, kedua ruas sama</sub>
- D. $x = 2\pi$  
  <sub>Salah: ruas kiri $0 + 1 = 1$, kedua ruas sama</sub>

**Pembahasan:** Hanya $x = \frac{\pi}{4}$ membuat ruas kiri $\sqrt{2}$ yang tidak sama dengan $1$. Nilai lain membuat kedua ruas sama sehingga bukan penyangkal.
**Acuan:** siswa — siswa hal.155 Latihan C Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b03-c-easy-bt01-009
*variasi (konteks) | C2 | 2 langkah | jenis: menyederhanakan hasil bagi*

Bentuk sederhana dari $\frac{\cos t}{\cot t}$ adalah ....

- A. $\frac{\cos^2 t}{\sin t}$  
  <sub>Salah: mengalikan dengan $\cot t$, bukan membagi</sub>
- **B. $\sin t$** ✅  
  <sub>Benar: $\frac{\cos t}{\cot t} = \cos t \cdot \frac{\sin t}{\cos t}$</sub>
- C. $\csc t$  
  <sub>Salah: membalik hasil</sub>
- D. $\tan t$  
  <sub>Salah: mengira $\cos t$ dibagi $\cot t$ menghasilkan $\tan t$</sub>

**Pembahasan:** $\cot t = \frac{\cos t}{\sin t}$, sehingga $\frac{\cos t}{\cot t} = \cos t \cdot \frac{\sin t}{\cos t} = \sin t$.
**Acuan:** siswa — siswa hal.155 Latihan C Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b03-c-easy-bt01-010
*variasi (konteks) | C2 | 2 langkah | jenis: menyederhanakan hasil bagi*

Untuk $t$ yang membuatnya terdefinisi, $\frac{\tan t}{\sin t}$ sama dengan ....

- A. $\cos t$  
  <sub>Salah: membalik hasil</sub>
- B. $\csc t$  
  <sub>Salah: hanya memperhatikan pembagi $\sin t$</sub>
- **C. $\sec t$** ✅  
  <sub>Benar: $\frac{\tan t}{\sin t} = \frac{\sin t}{\cos t} \cdot \frac{1}{\sin t} = \frac{1}{\cos t}$</sub>
- D. $\cot t$  
  <sub>Salah: mengira hasil bagi tan oleh sin adalah cot</sub>

**Pembahasan:** $\frac{\tan t}{\sin t} = \frac{\sin t}{\cos t}\cdot\frac{1}{\sin t} = \frac{1}{\cos t} = \sec t$.
**Acuan:** siswa — siswa hal.155 Latihan C Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b03-c-easy-bt01-011
*orisinal | C2 | 2 langkah | jenis: nilai kuadrat kosinus*

Jika $\sin t = \frac{8}{17}$, maka nilai $\cos^2 t$ adalah ....

- A. $\frac{15}{17}$  
  <sub>Salah: berhenti di $\cos t$ (lupa pertanyaan $\cos^2 t$)</sub>
- B. $\frac{9}{17}$  
  <sub>Salah: memakai $1 - \sin t$ tanpa mengkuadratkan</sub>
- C. $\frac{353}{289}$  
  <sub>Salah: memakai $1 + \sin^2 t$ sehingga tanda tertukar</sub>
- **D. $\frac{225}{289}$** ✅  
  <sub>Benar: $\cos^2 t = 1 - \left(\frac{8}{17}\right)^2 = \frac{225}{289}$</sub>

**Pembahasan:** $\cos^2 t = 1 - \sin^2 t = 1 - \frac{64}{289} = \frac{225}{289}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b03-c-easy-bt01-012
*orisinal | C2 | 2 langkah | jenis: hasil kali kebalikan*

Untuk $t$ yang membuat semua bentuknya terdefinisi, nilai $\sin t \csc t + \cos t \sec t$ adalah ....

- A. $1$  
  <sub>Salah: hanya menghitung satu pasangan kebalikan</sub>
- B. $0$  
  <sub>Salah: mengurangkan kedua hasil kali</sub>
- **C. $2$** ✅  
  <sub>Benar: $\sin t \csc t = 1$ dan $\cos t \sec t = 1$</sub>
- D. $\sin t + \cos t$  
  <sub>Salah: mencoret csc dan sec saja, bukan pasangannya</sub>

**Pembahasan:** Identitas kebalikan memberi $\sin t \csc t = 1$ dan $\cos t \sec t = 1$, jadi jumlahnya $2$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b03-c-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: identitas hasil bagi*

Diketahui $\sin t = -\frac{5}{13}$ dan $\cos t = \frac{12}{13}$. Nilai $\tan t$ adalah ....

- A. $\frac{5}{12}$  
  <sub>Salah: lupa tanda negatif</sub>
- B. $-\frac{5}{13}$  
  <sub>Salah: hanya menyalin nilai $\sin t$</sub>
- C. $-\frac{12}{5}$  
  <sub>Salah: pembilang dan penyebut tertukar (menghitung $\cot t$)</sub>
- **D. $-\frac{5}{12}$** ✅  
  <sub>Benar: $\tan t = \frac{\sin t}{\cos t}$</sub>

**Pembahasan:** $\tan t = \frac{-5/13}{12/13} = -\frac{5}{12}$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b03-c-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: identitas genap-ganjil*

Diketahui $\sin t = \frac{3}{7}$ dan $\cos t = \frac{2\sqrt{10}}{7}$. Nilai $\sin(-t) + \cos(-t)$ adalah ....

- A. $\frac{3 - 2\sqrt{10}}{7}$  
  <sub>Salah: mengira $\cos(-t) = -\cos t$</sub>
- B. $\frac{2\sqrt{10} + 3}{7}$  
  <sub>Salah: mengira $\sin(-t) = \sin t$</sub>
- **C. $\frac{2\sqrt{10} - 3}{7}$** ✅  
  <sub>Benar: $\sin(-t) = -\frac{3}{7}$ dan $\cos(-t) = \frac{2\sqrt{10}}{7}$</sub>
- D. $-\frac{2\sqrt{10} + 3}{7}$  
  <sub>Salah: memberi tanda negatif pada keduanya</sub>

**Pembahasan:** Sinus fungsi ganjil dan kosinus fungsi genap: $\sin(-t) + \cos(-t) = -\frac{3}{7} + \frac{2\sqrt{10}}{7}$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b03-c-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: mengenali identitas Pythagoras*

Pernyataan berikut yang merupakan identitas Pythagoras adalah ....

- **A. $1 + \cot^2 t = \csc^2 t$** ✅  
  <sub>Benar: salah satu identitas Pythagoras pada Sifat 3.4</sub>
- B. $\sin^2 t - \cos^2 t = 1$  
  <sub>Salah: salah tanda operasi pada $\sin^2 t + \cos^2 t = 1$</sub>
- C. $1 + \cot^2 t = \sec^2 t$  
  <sub>Salah: tertukar csc dan sec</sub>
- D. $1 + \tan^2 t = \csc^2 t$  
  <sub>Salah: tertukar sec dan csc</sub>

**Pembahasan:** Identitas Pythagoras: $\sin^2 t + \cos^2 t = 1$, $\tan^2 t + 1 = \sec^2 t$, dan $1 + \cot^2 t = \csc^2 t$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b03-c-easy-bt01-016
*orisinal | C2 | 1 langkah | jenis: konsep pembuktian dengan grafik*

Grafik kedua ruas suatu persamaan trigonometri digambar pada kalkulator grafik dan tampak berimpit. Pernyataan yang tepat adalah ....

- **A. hasil itu bukti kuat identitas, tetapi belum dapat dianggap sebagai pembuktian** ✅  
  <sub>Benar: buku menyatakan grafik tidak dapat dianggap pembuktian, tetapi menjadi bukti kuat</sub>
- B. hasil itu menunjukkan persamaan tersebut pasti bukan identitas  
  <sub>Salah: menafsirkan grafik berimpit secara terbalik</sub>
- C. hasil itu hanya berlaku untuk sudut lancip saja  
  <sub>Salah: mengira identitas hanya berlaku pada sudut lancip</sub>
- D. hasil itu sudah cukup sebagai pembuktian identitas  
  <sub>Salah: mengira grafik sama dengan pembuktian aljabar</sub>

**Pembahasan:** Grafik yang berimpit adalah bukti kuat, tetapi pembuktian tetap memerlukan manipulasi aljabar.
**Acuan:** siswa — siswa hal.152

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b03-c-easy-bt01-017
*orisinal | C1 | 1 langkah | jenis: rumus jumlah sudut kosinus*

Identitas penjumlahan sudut untuk kosinus adalah $\cos(A + B) = \ldots$

- A. $\cos A \sin B - \sin A \cos B$  
  <sub>Salah: mencampur sin dan cos pada tiap suku</sub>
- **B. $\cos A \cos B - \sin A \sin B$** ✅  
  <sub>Benar: rumus yang ditemukan pada eksplorasi lingkaran satuan</sub>
- C. $\sin A \cos B + \cos A \sin B$  
  <sub>Salah: tertukar dengan rumus $\sin(A + B)$</sub>
- D. $\cos A \cos B + \sin A \sin B$  
  <sub>Salah: tertukar dengan rumus $\cos(A - B)$</sub>

**Pembahasan:** Dari eksplorasi diperoleh $\cos(A + B) = \cos A \cos B - \sin A \sin B$.
**Acuan:** siswa — siswa hal.153

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b03-c-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: nilai sin(A+B) dari data*

Diketahui $\sin A = \frac{3}{5}$, $\cos A = \frac{4}{5}$, $\sin B = \frac{5}{13}$, dan $\cos B = \frac{12}{13}$. Nilai $\sin(A + B)$ adalah ....

- A. $\frac{16}{65}$  
  <sub>Salah: memakai tanda minus pada rumus (seperti $\sin(A - B)$)</sub>
- B. $\frac{33}{65}$  
  <sub>Salah: memakai rumus $\cos(A + B)$</sub>
- C. $\frac{63}{65}$  
  <sub>Salah: memakai rumus $\cos(A - B)$</sub>
- **D. $\frac{56}{65}$** ✅  
  <sub>Benar: $\sin(A+B) = \sin A \cos B + \cos A \sin B = \frac{36}{65} + \frac{20}{65}$</sub>

**Pembahasan:** $\sin(A+B) = \frac{3}{5}\cdot\frac{12}{13} + \frac{4}{5}\cdot\frac{5}{13} = \frac{36 + 20}{65} = \frac{56}{65}$.
**Acuan:** siswa — siswa hal.154

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b03-c-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: nilai cos(A-B) dari data*

Diketahui $\sin A = \frac{7}{25}$, $\cos A = \frac{24}{25}$, $\sin B = \frac{3}{5}$, dan $\cos B = \frac{4}{5}$. Nilai $\cos(A - B)$ adalah ....

- A. $\frac{4}{5}$  
  <sub>Salah: memakai rumus $\sin(A + B)$</sub>
- B. $\frac{3}{5}$  
  <sub>Salah: memakai $\cos(A+B)$ (tanda minus pada rumus)</sub>
- **C. $\frac{117}{125}$** ✅  
  <sub>Benar: $\cos(A-B) = \cos A \cos B + \sin A \sin B = \frac{96}{125} + \frac{21}{125}$</sub>
- D. $-\frac{44}{125}$  
  <sub>Salah: memakai rumus $\sin(A - B)$</sub>

**Pembahasan:** $\cos(A-B) = \cos A\cos B + \sin A\sin B = \frac{96}{125} + \frac{21}{125} = \frac{117}{125}$.
**Acuan:** siswa — siswa hal.154

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b03-c-easy-bt01-020
*orisinal | C2 | 1 langkah | jenis: menyederhanakan perkalian tan-cos*

Bentuk sederhana dari $\tan t \cdot \cos t$ adalah ....

- A. $\frac{1}{\sin t}$  
  <sub>Salah: membalik hasil</sub>
- **B. $\sin t$** ✅  
  <sub>Benar: $\tan t \cdot \cos t = \frac{\sin t}{\cos t} \cdot \cos t$</sub>
- C. $\cos t$  
  <sub>Salah: mengira $\tan t$ hilang dan menyisakan $\cos t$</sub>
- D. $\frac{\sin t}{\cos^2 t}$  
  <sub>Salah: membagi dengan $\cos t$, bukan mengalikan</sub>

**Pembahasan:** $\tan t \cdot \cos t = \frac{\sin t}{\cos t}\cdot\cos t = \sin t$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b03-c-medium-bt01-001
*variasi (konteks) | C3 | 2 langkah | jenis: mengalikan identitas Pythagoras*

Untuk $t$ yang membuat semua bentuknya terdefinisi, $(\sec^2 t - 1)\cos^2 t$ sama dengan ....

- A. $\cos^2 t$  
  <sub>Salah: mengira $\tan^2 t \cos^2 t$ sama dengan $\cos^2 t$</sub>
- **B. $\sin^2 t$** ✅  
  <sub>Benar: $\sec^2 t - 1 = \tan^2 t$, lalu $\tan^2 t \cdot \cos^2 t = \sin^2 t$</sub>
- C. $\tan^2 t$  
  <sub>Salah: berhenti setelah $\sec^2 t - 1 = \tan^2 t$ dan lupa mengalikan $\cos^2 t$</sub>
- D. $1$  
  <sub>Salah: mengalikan $\sec^2 t \cos^2 t = 1$ dan mengabaikan pengurangan $1$</sub>

**Pembahasan:** $\sec^2 t - 1 = \tan^2 t = \frac{\sin^2 t}{\cos^2 t}$, sehingga $(\sec^2 t - 1)\cos^2 t = \sin^2 t$.
**Acuan:** pretest — kelas11_tl-b03-p0155-latihan-c-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b03-c-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: dua identitas Pythagoras sekaligus*

Untuk $t$ yang membuat semua bentuknya terdefinisi, $(\sec t - \tan t)(\sec t + \tan t) + \sin^2 t + \cos^2 t$ sama dengan ....

- A. $1$  
  <sub>Salah: lupa menjumlahkan salah satu dari dua bagian yang masing-masing bernilai $1$</sub>
- B. $0$  
  <sub>Salah: mengurangkan kedua bagian</sub>
- **C. $2$** ✅  
  <sub>Benar: hasil kali $= \sec^2 t - \tan^2 t = 1$ dan $\sin^2 t + \cos^2 t = 1$</sub>
- D. $\sec^2 t + 1$  
  <sub>Salah: mengira hasil kali $(\sec t - \tan t)(\sec t + \tan t)$ sama dengan $\sec^2 t$</sub>

**Pembahasan:** $(\sec t - \tan t)(\sec t + \tan t) = \sec^2 t - \tan^2 t = 1$ dan $\sin^2 t + \cos^2 t = 1$, jumlahnya $2$.
**Acuan:** pretest — kelas11_tl-b03-p0155-latihan-c-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b03-c-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: tan dari sec dengan kuadran*

Jika $\sec u = -\frac{17}{8}$ dan $u$ berada di kuadran II, maka nilai $\tan u$ adalah ....

- A. $\frac{15}{8}$  
  <sub>Salah: lupa bahwa $\cos u$ negatif di kuadran II sehingga $\tan u$ ikut negatif</sub>
- B. $-\frac{8}{15}$  
  <sub>Salah: pembilang dan penyebut tertukar (menghitung $\cot u$)</sub>
- **C. $-\frac{15}{8}$** ✅  
  <sub>Benar: $\cos u = -\frac{8}{17}$, $\sin u = \frac{15}{17}$ (positif di kuadran II), $\tan u = \frac{\sin u}{\cos u}$</sub>
- D. $\frac{8}{15}$  
  <sub>Salah: tertukar dan lupa tanda negatif</sub>

**Pembahasan:** $\cos u = \frac{1}{\sec u} = -\frac{8}{17}$; $\sin^2 u = 1 - \frac{64}{289} = \frac{225}{289}$ dan $\sin u > 0$ di kuadran II, jadi $\sin u = \frac{15}{17}$. $\tan u = \frac{15/17}{-8/17} = -\frac{15}{8}$.
**Acuan:** siswa — siswa hal.155 Latihan C Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b03-c-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: cos dari csc dengan tanda tan*

Diketahui $\csc v = -\frac{25}{7}$ dan $\tan v > 0$. Nilai $\cos v$ adalah ....

- A. $-\frac{25}{24}$  
  <sub>Salah: menghitung $\sec v$, bukan $\cos v$</sub>
- **B. $-\frac{24}{25}$** ✅  
  <sub>Benar: $\sin v = -\frac{7}{25}$ dan $\tan v > 0$ berarti $\cos v < 0$ (kuadran III), $\cos^2 v = \frac{576}{625}$</sub>
- C. $\frac{24}{25}$  
  <sub>Salah: lupa memeriksa tanda: $\sin v < 0$ dan $\tan v > 0$ memaksa $\cos v < 0$</sub>
- D. $-\frac{7}{24}$  
  <sub>Salah: membagi $\sin v$ dengan $\cos v$ hasil yang salah (bukan $\cos v$)</sub>

**Pembahasan:** $\sin v = \frac{1}{\csc v} = -\frac{7}{25}$. $\cos^2 v = 1 - \frac{49}{625} = \frac{576}{625}$, jadi $\cos v = \pm\frac{24}{25}$. Karena $\sin v < 0$ dan $\tan v > 0$, $\cos v < 0$, sehingga $\cos v = -\frac{24}{25}$.
**Acuan:** siswa — siswa hal.155 Latihan C Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b03-c-medium-bt01-005
*variasi (konteks) | C4 | 3 langkah | jenis: menemukan kesalahan pembuktian*

Dani menyelidiki apakah $\cos t = -\cos(-t)$ merupakan identitas. Langkahnya: (1) $\cos t = -\cos(-t)$ (persamaan yang diberikan); (2) $\cos^2 t = [-\cos(-t)]^2$ (kuadratkan kedua ruas); (3) $\cos^2 t = \cos^2 t$ (sederhanakan, karena $\cos(-t) = \cos t$). Karena kedua ruas akhirnya sama, Dani menyimpulkan bahwa persamaan itu identitas.

Pernyataan yang benar tentang kesimpulan Dani adalah ....

- **A. salah, sebab kuadrat kedua ruas tidak ekuivalen; untuk $t = 0$ ruas kiri $1$ dan ruas kanan $-1$** ✅  
  <sub>Benar: persamaan awal diasumsikan benar dan kuadrat kedua ruas hanya memberi $a^2 = b^2$; untuk $t = 0$, $\cos 0 = 1$ sedangkan $-\cos 0 = -1$</sub>
- B. kesimpulan salah, sebab $\cos(-t) = -\cos t$ sehingga langkah (3) keliru  
  <sub>Salah: mengira kosinus fungsi ganjil seperti sinus</sub>
- C. benar, sebab setelah disederhanakan kedua ruas menjadi sama untuk semua nilai $t$  
  <sub>Salah: mengira kesamaan setelah dikuadratkan membuktikan persamaan awal</sub>
- D. kesimpulan salah, sebab hasil langkah (3) seharusnya $\cos^2 t = -\cos^2 t$  
  <sub>Salah: mengira kuadrat dari bentuk negatif tetap negatif</sub>

**Pembahasan:** Dari $\cos^2 t = \cos^2 t$ tidak dapat disimpulkan $\cos t = -\cos(-t)$, karena $a^2 = b^2$ hanya berarti $a = \pm b$. Untuk $t = 0$: ruas kiri $1$, ruas kanan $-1$, jadi bukan identitas.
**Acuan:** pretest — kelas11_tl-b03-p0155-latihan-c-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b03-c-medium-bt01-006
*variasi (konteks) | C3 | 3 langkah | jenis: menyederhanakan jumlah hasil bagi*

Untuk $t$ yang membuat semua bentuknya terdefinisi, bentuk sederhana dari $\frac{\sin t}{\tan t} + \frac{\cos t}{\cot t}$ adalah ....

- **A. $\sin t + \cos t$** ✅  
  <sub>Benar: $\frac{\sin t}{\tan t} = \cos t$ dan $\frac{\cos t}{\cot t} = \sin t$</sub>
- B. $\frac{1}{\sin t} + \frac{1}{\cos t}$  
  <sub>Salah: membalik kedua hasil sederhana</sub>
- C. $2\cos t$  
  <sub>Salah: mengira kedua suku sama-sama menghasilkan $\cos t$</sub>
- D. $\sin t \cos t$  
  <sub>Salah: mengalikan kedua hasil, bukan menjumlahkan</sub>

**Pembahasan:** $\frac{\sin t}{\tan t} = \sin t \cdot \frac{\cos t}{\sin t} = \cos t$ dan $\frac{\cos t}{\cot t} = \cos t \cdot \frac{\sin t}{\cos t} = \sin t$. Jumlahnya $\sin t + \cos t$.
**Acuan:** siswa — siswa hal.155 Latihan C Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b03-c-medium-bt01-007
*variasi (konteks) | C4 | 3 langkah | jenis: menguji klaim dengan contoh penyangkal*

Karena $\sec^2 t - \tan^2 t = 1$, Rina menyimpulkan bahwa $\sec t - \tan t = 1$ untuk semua $t$ yang terdefinisi. Pernyataan yang benar tentang kesimpulan Rina adalah ....

- A. benar, sebab kedua ruas dapat diakarkan sehingga $\sec t - \tan t = \sqrt{1}$ untuk semua $t$  
  <sub>Salah: mengira akar dari selisih kuadrat sama dengan selisih akar</sub>
- B. salah, sebab seharusnya $\sec t - \tan t = -1$ untuk semua $t$  
  <sub>Salah: mengira hasil akar bernilai negatif</sub>
- C. salah, sebab untuk $t = \frac{\pi}{4}$ diperoleh $\sec t - \tan t = \sqrt{2} + 1$  
  <sub>Salah: salah menghitung selisih dengan menjumlahkan nilai $\sec$ dan $\tan$</sub>
- **D. salah, sebab untuk $t = \frac{\pi}{4}$ diperoleh $\sec t - \tan t = \sqrt{2} - 1 \neq 1$** ✅  
  <sub>Benar: $\sec \frac{\pi}{4} = \sqrt{2}$ dan $\tan \frac{\pi}{4} = 1$, sehingga selisihnya $\sqrt{2} - 1$, bukan $1$</sub>

**Pembahasan:** $\sec^2 t - \tan^2 t = (\sec t - \tan t)(\sec t + \tan t) = 1$, bukan $\sec t - \tan t = 1$. Contoh penyangkal: $t = \frac{\pi}{4}$ memberi $\sqrt{2} - 1 \neq 1$.
**Acuan:** siswa — siswa hal.155 Latihan C Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b03-c-medium-bt01-008
*orisinal | C3 | 3 langkah | jenis: menyederhanakan selisih sec dan sin tan*

Untuk $t$ yang membuat semua bentuknya terdefinisi, bentuk sederhana dari $\sec t - \sin t \tan t$ adalah ....

- **A. $\cos t$** ✅  
  <sub>Benar: $\sec t - \sin t \tan t = \frac{1}{\cos t} - \frac{\sin^2 t}{\cos t} = \frac{1 - \sin^2 t}{\cos t} = \cos t$</sub>
- B. $\cos^2 t$  
  <sub>Salah: lupa membagi dengan $\cos t$ setelah $1 - \sin^2 t = \cos^2 t$</sub>
- C. $\sin t$  
  <sub>Salah: mengira $1 - \sin^2 t = \sin^2 t$ lalu membagi sembarang</sub>
- D. $\tan t$  
  <sub>Salah: mengira hasil pengurangan sama dengan $\tan t$ karena ada suku $\tan t$</sub>

**Pembahasan:** $\sec t - \sin t \tan t = \frac{1}{\cos t} - \frac{\sin^2 t}{\cos t} = \frac{\cos^2 t}{\cos t} = \cos t$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b03-c-medium-bt01-009
*orisinal | C4 | 4 langkah | jenis: menjumlahkan pecahan trigonometri*

Untuk $t$ yang membuat semua bentuknya terdefinisi, $\frac{\sin t}{1 + \cos t} + \frac{1 + \cos t}{\sin t}$ sama dengan ....

- A. $2\sec t$  
  <sub>Salah: tertukar csc dan sec setelah menyederhanakan</sub>
- B. $2\sin t$  
  <sub>Salah: membalik hasil $\frac{2}{\sin t}$ menjadi $2\sin t$</sub>
- **C. $2\csc t$** ✅  
  <sub>Benar: $\frac{\sin^2 t + (1 + \cos t)^2}{\sin t(1 + \cos t)} = \frac{2 + 2\cos t}{\sin t(1 + \cos t)} = \frac{2}{\sin t}$</sub>
- D. $\csc t$  
  <sub>Salah: lupa faktor $2$ pada pembilang $2 + 2\cos t$</sub>

**Pembahasan:** Samakan penyebut: $\frac{\sin^2 t + 1 + 2\cos t + \cos^2 t}{\sin t(1 + \cos t)} = \frac{2 + 2\cos t}{\sin t (1 + \cos t)} = \frac{2}{\sin t} = 2\csc t$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b03-c-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: kosinus jumlah sudut dari sinus*

Sudut $A$ dan $B$ keduanya lancip dengan $\sin A = \frac{8}{17}$ dan $\sin B = \frac{3}{5}$. Nilai $\cos(A + B)$ adalah ....

- A. $-\frac{36}{85}$  
  <sub>Salah: tertukar urutan pengurangan: $\sin A \sin B - \cos A \cos B$</sub>
- B. $\frac{84}{85}$  
  <sub>Salah: memakai rumus $\cos(A - B)$ (tanda plus di tengah)</sub>
- C. $\frac{77}{85}$  
  <sub>Salah: memakai rumus $\sin(A + B)$</sub>
- **D. $\frac{36}{85}$** ✅  
  <sub>Benar: $\cos A = \frac{15}{17}$, $\cos B = \frac{4}{5}$ (positif karena lancip), $\cos(A+B) = \cos A \cos B - \sin A \sin B = \frac{60}{85} - \frac{24}{85}$</sub>

**Pembahasan:** $\cos A = \sqrt{1 - \frac{64}{289}} = \frac{15}{17}$ dan $\cos B = \sqrt{1 - \frac{9}{25}} = \frac{4}{5}$. $\cos(A+B) = \frac{15}{17}\cdot\frac{4}{5} - \frac{8}{17}\cdot\frac{3}{5} = \frac{60 - 24}{85} = \frac{36}{85}$.
**Acuan:** siswa — siswa hal.153

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b03-c-medium-bt01-011
*orisinal | C4 | 4 langkah | jenis: sinus selisih sudut dengan kuadran*

Sudut $A$ berada di kuadran II dengan $\sin A = \frac{4}{5}$, sedangkan sudut $B$ berada di kuadran IV dengan $\cos B = \frac{5}{13}$. Nilai $\sin(A - B)$ adalah ....

- A. $\frac{16}{65}$  
  <sub>Salah: tertukar urutan pengurangan pada rumus</sub>
- **B. $-\frac{16}{65}$** ✅  
  <sub>Benar: $\cos A = -\frac{3}{5}$ dan $\sin B = -\frac{12}{13}$, $\sin(A-B) = \sin A \cos B - \cos A \sin B = \frac{20}{65} - \frac{36}{65}$</sub>
- C. $\frac{56}{65}$  
  <sub>Salah: memakai rumus $\sin(A + B)$</sub>
- D. $-\frac{56}{65}$  
  <sub>Salah: memakai rumus $\sin(A+B)$ lalu menukar tanda</sub>

**Pembahasan:** $\cos A = -\frac{3}{5}$ (kuadran II), $\sin B = -\frac{12}{13}$ (kuadran IV). $\sin(A-B) = \frac{4}{5}\cdot\frac{5}{13} - \left(-\frac{3}{5}\right)\left(-\frac{12}{13}\right) = \frac{20}{65} - \frac{36}{65} = -\frac{16}{65}$.
**Acuan:** siswa — siswa hal.154

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b03-c-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: nilai tepat kosinus sudut istimewa*

Dengan menuliskan $\frac{7\pi}{12} = \frac{\pi}{3} + \frac{\pi}{4}$, nilai $\cos\frac{7\pi}{12}$ adalah ....

- A. $-\frac{\sqrt{6} + \sqrt{2}}{4}$  
  <sub>Salah: memakai tanda plus lalu menambah tanda negatif karena sudut di kuadran II</sub>
- B. $\frac{\sqrt{2} + \sqrt{6}}{4}$  
  <sub>Salah: memakai tanda plus pada rumus $\cos(A+B)$</sub>
- **C. $\frac{\sqrt{2} - \sqrt{6}}{4}$** ✅  
  <sub>Benar: $\cos\frac{\pi}{3}\cos\frac{\pi}{4} - \sin\frac{\pi}{3}\sin\frac{\pi}{4} = \frac{\sqrt{2}}{4} - \frac{\sqrt{6}}{4}$</sub>
- D. $\frac{\sqrt{6} - \sqrt{2}}{4}$  
  <sub>Salah: tertukar urutan pengurangan sehingga tanda berbalik</sub>

**Pembahasan:** $\cos\frac{7\pi}{12} = \frac{1}{2}\cdot\frac{\sqrt{2}}{2} - \frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2} = \frac{\sqrt{2} - \sqrt{6}}{4}$.
**Acuan:** siswa — siswa hal.153

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b03-c-medium-bt01-013
*orisinal | C3 | 2 langkah | jenis: mengenali bentuk rumus selisih sudut*

Nilai dari $\cos 80^\circ \cos 20^\circ + \sin 80^\circ \sin 20^\circ$ adalah ....

- A. $\cos 100^\circ$  
  <sub>Salah: memakai rumus $\cos(A + B)$ padahal bentuknya $\cos(A - B)$</sub>
- **B. $\frac{1}{2}$** ✅  
  <sub>Benar: bentuk itu sama dengan $\cos(80^\circ - 20^\circ) = \cos 60^\circ$</sub>
- C. $-\frac{1}{2}$  
  <sub>Salah: salah tanda saat menghitung nilai $\cos 60^\circ$</sub>
- D. $\frac{\sqrt{3}}{2}$  
  <sub>Salah: mengira hasilnya $\sin 60^\circ$ atau salah mengambil nilai $\cos 30^\circ$</sub>

**Pembahasan:** $\cos A \cos B + \sin A \sin B = \cos(A - B)$, sehingga nilainya $\cos 60^\circ = \frac{1}{2}$.
**Acuan:** siswa — siswa hal.154

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b03-c-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: kuadrat jumlah dan hasil kali sin cos*

Jika $\sin t + \cos t = \frac{1}{2}$, maka nilai $\sin t \cos t$ adalah ....

- A. $\frac{1}{8}$  
  <sub>Salah: lupa suku $\sin^2 t + \cos^2 t = 1$ sehingga langsung $2\sin t \cos t = \frac{1}{4}$</sub>
- B. $-\frac{3}{4}$  
  <sub>Salah: lupa membagi dengan $2$ dari suku $2\sin t \cos t$</sub>
- C. $\frac{3}{8}$  
  <sub>Salah: salah tanda saat memindahkan $1$ ke ruas kanan</sub>
- **D. $-\frac{3}{8}$** ✅  
  <sub>Benar: $(\sin t + \cos t)^2 = 1 + 2\sin t \cos t = \frac{1}{4}$, sehingga $\sin t \cos t = -\frac{3}{8}$</sub>

**Pembahasan:** Kuadratkan: $\sin^2 t + 2\sin t\cos t + \cos^2 t = \frac{1}{4}$, yaitu $1 + 2\sin t \cos t = \frac{1}{4}$. Maka $\sin t \cos t = \frac{1}{2}\left(\frac{1}{4} - 1\right) = -\frac{3}{8}$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b03-c-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: sistem dari sec dan tan*

Jika $\sec t + \tan t = 2$, maka nilai $\tan t$ adalah ....

- A. $\frac{3}{2}$  
  <sub>Salah: lupa membagi dengan $2$ setelah mengurangkan kedua persamaan</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: mengira $\sec t - \tan t = \frac{1}{2}$ lalu langsung membagi dengan $2$</sub>
- C. $\frac{5}{4}$  
  <sub>Salah: menghitung $\sec t$, bukan $\tan t$</sub>
- **D. $\frac{3}{4}$** ✅  
  <sub>Benar: $(\sec t - \tan t)(\sec t + \tan t) = 1$ sehingga $\sec t - \tan t = \frac{1}{2}$; eliminasi: $\tan t = \frac{2 - 1/2}{2}$</sub>

**Pembahasan:** Dari $\sec^2 t - \tan^2 t = 1$: $\sec t - \tan t = \frac{1}{2}$. Kurangkan dengan $\sec t + \tan t = 2$: $2\tan t = 2 - \frac{1}{2} = \frac{3}{2}$, jadi $\tan t = \frac{3}{4}$ (dan $\sec t = \frac{5}{4}$).
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [hard] kelas11_tl-b03-c-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: memilih identitas di antara persamaan mirip*

Di antara kesamaan berikut, yang berlaku untuk semua $t$ real (identitas) adalah ....

- **A. $\sin^4 t - \cos^4 t = \sin^2 t - \cos^2 t$** ✅  
  <sub>Benar: $\sin^4 t - \cos^4 t = (\sin^2 t - \cos^2 t)(\sin^2 t + \cos^2 t) = \sin^2 t - \cos^2 t$</sub>
- B. $\cos^4 t - \sin^4 t = 1 - 2\cos^2 t$  
  <sub>Salah: tertukar tanda; yang benar $\cos^4 t - \sin^4 t = 2\cos^2 t - 1$</sub>
- C. $\sin^4 t + \cos^4 t = 1$  
  <sub>Salah: mengira pangkat empat berperilaku seperti pangkat dua; untuk $t = \frac{\pi}{4}$ ruas kiri $\frac{1}{2}$</sub>
- D. $(\sin t + \cos t)^2 = 1 + \sin t\cos t$  
  <sub>Salah: lupa suku silang bernilai $2\sin t\cos t$; untuk $t = \frac{\pi}{4}$ ruas kiri $2$ dan ruas kanan $\frac{3}{2}$</sub>

**Pembahasan:** Faktorkan selisih kuadrat lalu pakai identitas Pythagoras untuk pilihan pertama. Pilihan lain gugur: $t=\frac{\pi}{4}$ memberi $\frac{1}{2}\neq 1$, kemudian $\cos^4 t-\sin^4 t=\cos^2 t-\sin^2 t = 2\cos^2 t-1$, dan $2\neq\frac{3}{2}$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas11_tl-b03-c-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: menemukan langkah pembuktian yang salah*

Bima membuktikan $\tan^2 t - \sin^2 t = \tan^2 t\sin^2 t$ dengan langkah berikut.

(1) $\tan^2 t - \sin^2 t = \dfrac{\sin^2 t}{\cos^2 t} - \sin^2 t$

(2) $= \sin^2 t\left(\dfrac{1}{\cos^2 t} - 1\right)$

(3) $= \sin^2 t\left(\dfrac{1}{\cos t} - 1\right)^2$

(4) $= \sin^2 t\tan^2 t$

Kesalahan yang pertama kali muncul terdapat pada langkah ....

- A. (4)  
  <sub>Salah: langkah ini juga tidak sah dari (3), tetapi bukan kesalahan pertama; akibat dari (3)</sub>
- **B. (3)** ✅  
  <sub>Benar: $\left(\frac{1}{\cos t} - 1\right)^2 \neq \frac{1}{\cos^2 t} - 1$; yang benar adalah $\sec^2 t - 1 = \tan^2 t$</sub>
- C. (2)  
  <sub>Salah: langkah ini sah, hanya memfaktorkan $\sin^2 t$</sub>
- D. (1)  
  <sub>Salah: langkah ini sah, hanya mengganti $\tan t$ dengan $\frac{\sin t}{\cos t}$</sub>

**Pembahasan:** Langkah (1) dan (2) sah. Pada (3) kuadrat dipindahkan ke luar sehingga $\frac{1}{\cos^2 t} - 1$ diganti $\left(\frac{1}{\cos t} - 1\right)^2$, padahal tidak senilai (uji $t = \frac{\pi}{3}$: $3$ lawan $1$). Seharusnya $\sec^2 t - 1 = \tan^2 t$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas11_tl-b03-c-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: merancang ruas pasangan identitas*

Agar $\dfrac{\cos t}{1 - \sin t} = \ldots$ menjadi identitas untuk semua $t$ yang membuat kedua ruasnya terdefinisi, bentuk yang tepat untuk mengisi titik-titik adalah ....

- A. $\dfrac{1 - \sin t}{\cos t}$  
  <sub>Salah: tanda sekawan tertukar; ini kebalikan dari bentuk yang benar</sub>
- **B. $\dfrac{1 + \sin t}{\cos t}$** ✅  
  <sub>Benar: kalikan pembilang dan penyebut dengan sekawan $1 + \sin t$: $\frac{\cos t(1+\sin t)}{1-\sin^2 t} = \frac{\cos t(1+\sin t)}{\cos^2 t}$</sub>
- C. $\dfrac{1 + \cos t}{\sin t}$  
  <sub>Salah: tertukar peran $\sin$ dan $\cos$; untuk $t=\frac{\pi}{3}$ bentuk ini bernilai $\sqrt{3}$, sedangkan ruas kiri $2+\sqrt{3}\neq\sqrt{3}$</sub>
- D. $\dfrac{\cos t}{1 + \cos t}$  
  <sub>Salah: hanya mengganti $\sin$ dengan $\cos$ di penyebut</sub>

**Pembahasan:** Kalikan dengan $\frac{1+\sin t}{1+\sin t}$ dan gunakan $1-\sin^2 t=\cos^2 t$ sehingga diperoleh $\frac{1+\sin t}{\cos t}$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas11_tl-b03-c-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: syarat berlakunya akar identitas Pythagoras*

Dari $\sin^2 t + \cos^2 t = 1$, Eka menulis $\sqrt{1 - \sin^2 t} = \cos t$. Himpunan semua $t$ real yang membuat kesamaan itu benar adalah $t$ dengan ....

- A. $\sin t \ge 0$  
  <sub>Salah: mengira tanda ditentukan $\sin t$; untuk $t = -\frac{\pi}{4}$ kesamaan tetap benar</sub>
- B. $\cos t > 0$  
  <sub>Salah: titik batas $t = \frac{\pi}{2}$ terlewat: kedua ruas bernilai $0$ sehingga kesamaan berlaku</sub>
- **C. $\cos t \ge 0$** ✅  
  <sub>Benar: $\sqrt{1-\sin^2 t}=\sqrt{\cos^2 t}=|\cos t|$, yang sama dengan $\cos t$ tepat bila $\cos t \ge 0$ (termasuk $\cos t = 0$)</sub>
- D. semua bilangan real $t$  
  <sub>Salah: melupakan bahwa akar tidak negatif; untuk $t = \frac{2\pi}{3}$ ruas kiri $\frac{1}{2}$ dan ruas kanan $-\frac{1}{2}$</sub>

**Pembahasan:** Akar kuadrat bernilai tidak negatif, jadi $\sqrt{\cos^2 t}=|\cos t|$. Kesamaan $|\cos t|=\cos t$ benar tepat bila $\cos t\ge 0$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas11_tl-b03-c-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: syarat domain agar identitas berlaku*

Identitas $\dfrac{\sin t}{1 - \cos t} = \dfrac{1 + \cos t}{\sin t}$ berlaku untuk semua $t$ yang kedua ruasnya terdefinisi. Himpunan $t$ tersebut adalah semua bilangan real kecuali ... dengan $k$ bilangan bulat.

- **A. $t = k\pi$** ✅  
  <sub>Benar: ruas kiri tak terdefinisi bila $\cos t=1$ ($t=2k\pi$), ruas kanan tak terdefinisi bila $\sin t=0$ ($t=k\pi$); gabungannya $t=k\pi$</sub>
- B. $t = (2k+1)\pi$  
  <sub>Salah: hanya memeriksa penyebut ruas kanan pada sudut ganjil; di $t=2k\pi$ ruas kiri tak terdefinisi</sub>
- C. $t = \dfrac{\pi}{2} + k\pi$  
  <sub>Salah: mengira syarat berasal dari $\cos t = 0$ padahal tidak ada $\cos t$ di penyebut</sub>
- D. $t = 2k\pi$  
  <sub>Salah: hanya memeriksa penyebut ruas kiri; di $t=\pi$ ruas kanan tak terdefinisi</sub>

**Pembahasan:** Penyebut ruas kiri nol bila $t=2k\pi$; penyebut ruas kanan nol bila $t=k\pi$. Kedua ruas terdefinisi bila $t\ne k\pi$. Di titik lain kesamaan terbukti dengan $\sin^2 t=(1-\cos t)(1+\cos t)$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b03-c-hard-bt01-006
*orisinal | C5 | 5 langkah | jenis: menilai kemungkinan nilai dari identitas*

Untuk suatu sudut $t$, misalkan $s = \sin t + \cos t$ dan $p = \sin t\cos t$. Pasangan $(s, p)$ berikut yang benar-benar dapat terjadi untuk suatu $t$ real adalah ....

- A. $\left(\dfrac{7}{5}, \dfrac{6}{25}\right)$  
  <sub>Salah: melanggar $s^2 = 1 + 2p$: $\frac{49}{25}\neq\frac{37}{25}$</sub>
- B. $\left(\dfrac{8}{5}, \dfrac{39}{50}\right)$  
  <sub>Salah: memenuhi $s^2=1+2p$ tetapi $p>\frac{1}{2}$ mustahil; $\sin t,\cos t$ tidak real</sub>
- C. $\left(\dfrac{3}{2}, \dfrac{5}{8}\right)$  
  <sub>Salah: memenuhi $s^2=1+2p$ tetapi $p>\frac{1}{2}$ mustahil; $\sin t,\cos t$ tidak real</sub>
- **D. $\left(\dfrac{7}{5}, \dfrac{12}{25}\right)$** ✅  
  <sub>Benar: $s^2=1+2p$ terpenuhi ($\frac{49}{25}=1+\frac{24}{25}$), dan $\sin t=\frac{4}{5}$, $\cos t=\frac{3}{5}$ memberi pasangan itu</sub>

**Pembahasan:** Dari $(\sin t+\cos t)^2=1+2\sin t\cos t$ diperoleh $s^2=1+2p$. Selain itu $\sin t$ dan $\cos t$ adalah akar $x^2-sx+p=0$ yang harus real, yaitu $s^2\ge 4p$, sehingga $p\le\frac{1}{2}$. Hanya $(\frac{7}{5},\frac{12}{25})$ memenuhi keduanya.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
