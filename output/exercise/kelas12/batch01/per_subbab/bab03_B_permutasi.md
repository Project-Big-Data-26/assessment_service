# Lembar koreksi — kelas12 SMA12U-B3 subbab B: Permutasi

60 soal | easy 20, medium 20, hard 20 | variasi 22, orisinal 38

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12-b03-b-easy-bt01-001
*variasi (konteks) | C1 | 1 langkah | jenis: permutasi n dari n objek*

Delapan orang calon ketua regu berdiri berjajar dalam satu barisan untuk berfoto. Banyak susunan barisan yang mungkin adalah ....

- A. 56  
  <sub>Salah: hanya mengalikan dua faktor pertama, $8 \times 7$</sub>
- B. 5.040  
  <sub>Salah: memakai $7!$ karena mengira satu orang tidak ikut diurutkan</sub>
- **C. 40.320** ✅  
  <sub>Benar: delapan objek berbeda disusun seluruhnya sehingga banyaknya $8! = 40.320$</sub>
- D. 362.880  
  <sub>Salah: memakai $9!$ (salah menghitung banyak objek)</sub>

**Pembahasan:** Menyusun 8 orang seluruhnya adalah permutasi 8 dari 8 objek: $8! = 8 \times 7 \times \dots \times 1 = 40.320$.
**Acuan:** pretest — kelas12-b03-p0118-latihan-3-2-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12-b03-b-easy-bt01-002
*variasi (konteks) | C2 | 2 langkah | jenis: permutasi unsur sama*

Putra menyusun seluruh huruf pada kata KEBUMEN sebagai kode rahasia. Banyak susunan huruf berbeda yang dapat dibentuk adalah ....

- A. 1.260  
  <sub>Salah: membagi dengan $2! \times 2!$ padahal hanya satu huruf yang berulang</sub>
- **B. 2.520** ✅  
  <sub>Benar: 7 huruf dengan huruf E muncul 2 kali, sehingga $\frac{7!}{2!} = 2.520$</sub>
- C. 840  
  <sub>Salah: membagi dengan $3!$ seolah E muncul 3 kali</sub>
- D. 5.040  
  <sub>Salah: tidak membagi dengan $2!$ untuk huruf E yang sama</sub>

**Pembahasan:** Huruf K, E, B, U, M, E, N: 7 huruf dengan E dua kali. Banyak susunan $= \frac{7!}{2!} = \frac{5.040}{2} = 2.520$.
**Acuan:** pretest — kelas12-b03-p0119-latihan-3-2-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12-b03-b-easy-bt01-003
*variasi (angka) | C1 | 1 langkah | jenis: permutasi n dari n objek*

Suatu permainan tradisional Egrang beregu terdiri dari 7 orang. Tentukan banyak cara menyusun formasi yang terdiri atas 7 orang tersebut.

- A. 49  
  <sub>Salah: menghitung $7 \times 7$ seolah setiap posisi bebas dipilih ulang</sub>
- **B. 5.040** ✅  
  <sub>Benar: 7 orang disusun seluruhnya sehingga $7! = 5.040$</sub>
- C. 40.320  
  <sub>Salah: memakai $8!$ (kelebihan satu faktor)</sub>
- D. 720  
  <sub>Salah: memakai $6!$ (kurang satu faktor)</sub>

**Pembahasan:** Formasi 7 orang adalah permutasi 7 dari 7 objek: $7! = 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 5.040$.
**Acuan:** siswa — siswa hal.112 Contoh 3.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12-b03-b-easy-bt01-004
*variasi (konteks) | C1 | 1 langkah | jenis: permutasi n dari n objek*

Sebuah penginapan memiliki 5 kamar dan setiap kamar hanya dapat ditempati satu tamu. Pada suatu sore datang 5 tamu bersamaan. Banyak cara petugas menempatkan kelima tamu pada kelima kamar tersebut adalah ....

- **A. 120** ✅  
  <sub>Benar: 5 tamu menempati 5 kamar sehingga $5! = 120$</sub>
- B. 24  
  <sub>Salah: memakai $4!$ (kurang satu faktor)</sub>
- C. 25  
  <sub>Salah: menghitung $5 \times 5$</sub>
- D. 720  
  <sub>Salah: memakai $6!$ (kelebihan satu faktor)</sub>

**Pembahasan:** Menempatkan 5 tamu pada 5 kamar adalah $P(5,5) = 5! = 120$.
**Acuan:** siswa — siswa hal.112 Contoh 3.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12-b03-b-easy-bt01-005
*variasi (konteks) | C2 | 2 langkah | jenis: permutasi unsur sama*

Banyak susunan huruf berbeda yang dapat dibuat dari seluruh huruf pada nama kota PALEMBANG adalah ....

- A. 362.880  
  <sub>Salah: tidak membagi dengan $2!$ untuk huruf A yang sama</sub>
- B. 60.480  
  <sub>Salah: membagi dengan $3!$ seolah A muncul 3 kali</sub>
- **C. 181.440** ✅  
  <sub>Benar: 9 huruf dengan A muncul 2 kali, sehingga $\frac{9!}{2!} = 181.440$</sub>
- D. 90.720  
  <sub>Salah: membagi dengan $2! \times 2!$ padahal hanya A yang berulang</sub>

**Pembahasan:** PALEMBANG memiliki 9 huruf dengan A dua kali. Banyak susunan $= \frac{9!}{2!} = \frac{362.880}{2} = 181.440$.
**Acuan:** pretest — kelas12-b03-p0119-latihan-3-2-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12-b03-b-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: permutasi unsur sama*

Sebuah toko membuat gantungan kunci dari seluruh huruf nama kota SURABAYA dengan susunan berbeda-beda. Banyak susunan huruf berbeda yang mungkin adalah ....

- **A. 6.720** ✅  
  <sub>Benar: 8 huruf dengan A muncul 3 kali, sehingga $\frac{8!}{3!} = 6.720$</sub>
- B. 40.320  
  <sub>Salah: tidak membagi dengan faktorial huruf yang sama</sub>
- C. 3.360  
  <sub>Salah: membagi dengan $3! \times 2!$ padahal hanya A yang berulang</sub>
- D. 20.160  
  <sub>Salah: membagi dengan $2!$ seolah A hanya muncul 2 kali</sub>

**Pembahasan:** SURABAYA memiliki 8 huruf dengan A tiga kali. Banyak susunan $= \frac{8!}{3!} = \frac{40.320}{6} = 6.720$.
**Acuan:** siswa — siswa hal.114 Contoh 3.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12-b03-b-easy-bt01-007
*variasi (konteks) | C1 | 1 langkah | jenis: permutasi siklis*

Tujuh orang peserta rapat duduk mengelilingi sebuah meja bundar. Banyak susunan duduk yang berbeda adalah ....

- A. 120  
  <sub>Salah: memakai $(n-2)!$</sub>
- B. 5.040  
  <sub>Salah: memakai $7!$ seperti susunan berjajar</sub>
- **C. 720** ✅  
  <sub>Benar: permutasi siklis 7 objek $= (7-1)! = 720$</sub>
- D. 2.520  
  <sub>Salah: membagi $7!$ dengan 2, bukan dengan 7</sub>

**Pembahasan:** Permutasi siklis $n$ objek berbeda $= (n-1)!$, sehingga $(7-1)! = 6! = 720$.
**Acuan:** siswa — siswa hal.116 Contoh 3.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12-b03-b-easy-bt01-008
*variasi (konteks) | C1 | 1 langkah | jenis: permutasi siklis*

Lima anggota sebuah keluarga makan malam dengan duduk melingkar pada satu meja makan bundar. Banyak susunan tempat duduk yang berbeda adalah ....

- A. 120  
  <sub>Salah: memakai $5!$ seperti susunan berjajar</sub>
- B. 60  
  <sub>Salah: membagi $5!$ dengan 2, bukan dengan 5</sub>
- C. 6  
  <sub>Salah: memakai $(n-2)! = 3!$</sub>
- **D. 24** ✅  
  <sub>Benar: permutasi siklis 5 objek $= (5-1)! = 24$</sub>

**Pembahasan:** Permutasi siklis 5 objek $= (5-1)! = 4! = 24$.
**Acuan:** siswa — siswa hal.116 Contoh 3.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12-b03-b-easy-bt01-009
*variasi (konteks) | C2 | 2 langkah | jenis: permutasi unsur sama*

Tentukan banyak susunan huruf berbeda yang dapat dibentuk dari seluruh huruf pada kata MATEMATIKA.

- A. 3.628.800  
  <sub>Salah: tidak membagi dengan faktorial huruf yang sama</sub>
- **B. 151.200** ✅  
  <sub>Benar: 10 huruf dengan M 2 kali, A 3 kali, T 2 kali, sehingga $\frac{10!}{2!\,3!\,2!} = 151.200$</sub>
- C. 907.200  
  <sub>Salah: hanya membagi dengan $2! \times 2!$ (huruf A diabaikan)</sub>
- D. 302.400  
  <sub>Salah: hanya membagi dengan $3! \times 2!$ (salah satu huruf kembar diabaikan)</sub>

**Pembahasan:** MATEMATIKA: 10 huruf, M dua kali, A tiga kali, T dua kali. Banyak susunan $= \frac{10!}{2!\,3!\,2!} = \frac{3.628.800}{24} = 151.200$.
**Acuan:** siswa — siswa hal.114 Contoh 3.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12-b03-b-easy-bt01-010
*variasi (konteks) | C2 | 2 langkah | jenis: permutasi unsur sama*

Berapa banyak susunan huruf berbeda yang dapat dibuat dari huruf-huruf pada kata TERTIB?

- A. 720  
  <sub>Salah: tidak membagi dengan $2!$</sub>
- B. 120  
  <sub>Salah: membagi dengan $3!$ seolah T muncul 3 kali</sub>
- C. 180  
  <sub>Salah: membagi dengan $2! \times 2!$ padahal hanya T yang berulang</sub>
- **D. 360** ✅  
  <sub>Benar: 6 huruf dengan T muncul 2 kali, sehingga $\frac{6!}{2!} = 360$</sub>

**Pembahasan:** TERTIB: 6 huruf dengan T dua kali. Banyak susunan $= \frac{6!}{2!} = \frac{720}{2} = 360$.
**Acuan:** siswa — siswa hal.114 Contoh 3.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12-b03-b-easy-bt01-011
*variasi (konteks) | C2 | 2 langkah | jenis: permutasi unsur sama*

Sebuah penerbit mencetak stiker dari seluruh huruf kata SEMARANG dengan susunan berbeda-beda. Banyak jenis stiker yang dapat dicetak adalah ....

- A. 40.320  
  <sub>Salah: tidak membagi dengan $2!$</sub>
- B. 10.080  
  <sub>Salah: membagi dengan $2! \times 2!$ padahal hanya A yang berulang</sub>
- C. 6.720  
  <sub>Salah: membagi dengan $3!$ seolah A muncul 3 kali</sub>
- **D. 20.160** ✅  
  <sub>Benar: 8 huruf dengan A muncul 2 kali, sehingga $\frac{8!}{2!} = 20.160$</sub>

**Pembahasan:** SEMARANG memiliki 8 huruf dengan A dua kali. Banyak susunan $= \frac{8!}{2!} = \frac{40.320}{2} = 20.160$.
**Acuan:** siswa — siswa hal.114 Contoh 3.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12-b03-b-easy-bt01-012
*variasi (konteks) | C1 | 1 langkah | jenis: permutasi n dari n objek*

Seorang guru menata 9 buku berbeda dalam satu baris pada sebuah rak. Banyak susunan buku yang mungkin adalah ....

- **A. 362.880** ✅  
  <sub>Benar: 9 buku berbeda disusun seluruhnya sehingga $9! = 362.880$</sub>
- B. 40.320  
  <sub>Salah: memakai $8!$ (kurang satu faktor)</sub>
- C. 504  
  <sub>Salah: hanya mengalikan tiga faktor pertama, $9 \times 8 \times 7$</sub>
- D. 81  
  <sub>Salah: menghitung $9 \times 9$</sub>

**Pembahasan:** Menata 9 buku berbeda dalam satu baris adalah $9! = 362.880$.
**Acuan:** pretest — kelas12-b03-p0118-latihan-3-2-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12-b03-b-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: hitung nilai faktorial*

Nilai dari $\frac{8!}{6!}$ adalah ....

- A. 2  
  <sub>Salah: mengurangkan $8 - 6$</sub>
- **B. 56** ✅  
  <sub>Benar: $\frac{8!}{6!} = 8 \times 7 = 56$</sub>
- C. $\frac{4}{3}$  
  <sub>Salah: mencoret faktorialnya secara salah sehingga hanya membagi $8$ dengan $6$</sub>
- D. 336  
  <sub>Salah: mengalikan tiga faktor, $8 \times 7 \times 6$</sub>

**Pembahasan:** $\frac{8!}{6!} = \frac{8 \times 7 \times 6!}{6!} = 8 \times 7 = 56$.
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12-b03-b-easy-bt01-014
*orisinal | C1 | 2 langkah | jenis: hitung nilai faktorial*

Nilai dari $5! + 3!$ adalah ....

- A. 40.320  
  <sub>Salah: menjumlahkan $5 + 3$ terlebih dahulu lalu menghitung $8!$</sub>
- B. 720  
  <sub>Salah: mengalikan $5! \times 3!$ bukan menjumlahkan</sub>
- C. 8  
  <sub>Salah: menjumlahkan $5 + 3$ tanpa faktorial</sub>
- **D. 126** ✅  
  <sub>Benar: $5! = 120$ dan $3! = 6$, sehingga jumlahnya $126$</sub>

**Pembahasan:** $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$, $3! = 6$, jadi $5! + 3! = 126$.
**Acuan:** siswa — siswa hal.112

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12-b03-b-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: hitung nilai P(n,r)*

Nilai dari $P(7,2)$ adalah ....

- A. 14  
  <sub>Salah: mengalikan $n \times r = 7 \times 2$</sub>
- B. 49  
  <sub>Salah: mengalikan $7 \times 7$</sub>
- C. 21  
  <sub>Salah: membagi hasil dengan $2!$, seolah urutan tidak diperhitungkan</sub>
- **D. 42** ✅  
  <sub>Benar: $P(7,2) = \frac{7!}{5!} = 7 \times 6 = 42$</sub>

**Pembahasan:** $P(7,2) = \frac{7!}{(7-2)!} = \frac{7!}{5!} = 7 \times 6 = 42$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12-b03-b-easy-bt01-016
*orisinal | C1 | 1 langkah | jenis: hitung nilai P(n,r)*

Nilai dari $P(9,3)$ adalah ....

- A. 27  
  <sub>Salah: mengalikan $n \times r = 9 \times 3$</sub>
- **B. 504** ✅  
  <sub>Benar: $P(9,3) = \frac{9!}{6!} = 9 \times 8 \times 7 = 504$</sub>
- C. 84  
  <sub>Salah: membagi hasil dengan $3!$, seolah urutan tidak diperhitungkan</sub>
- D. 729  
  <sub>Salah: menghitung $9^3$</sub>

**Pembahasan:** $P(9,3) = \frac{9!}{(9-3)!} = \frac{9!}{6!} = 9 \times 8 \times 7 = 504$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12-b03-b-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: pemodelan permutasi r dari n*

Dari 8 siswa yang bersedia akan dipilih seorang ketua, seorang sekretaris, dan seorang bendahara. Setiap siswa menduduki paling banyak satu jabatan. Banyak susunan pengurus yang mungkin adalah ....

- A. 24  
  <sub>Salah: menjumlahkan/mengalikan $8 \times 3$</sub>
- B. 512  
  <sub>Salah: menghitung $8^3$ (siswa boleh merangkap jabatan)</sub>
- **C. 336** ✅  
  <sub>Benar: $P(8,3) = 8 \times 7 \times 6 = 336$</sub>
- D. 56  
  <sub>Salah: membagi dengan $3!$, seolah jabatan tidak dibedakan</sub>

**Pembahasan:** Jabatan berbeda sehingga urutan diperhitungkan: $P(8,3) = \frac{8!}{5!} = 8 \times 7 \times 6 = 336$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12-b03-b-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: pemodelan permutasi r dari n*

Dua belas siswa bersedia menjadi pengurus kelas. Jabatan ketua dan wakil ketua telah diisi oleh dua siswa di antaranya. Jabatan sekretaris dan bendahara akan diisi oleh siswa yang tersisa, dan setiap siswa menduduki paling banyak satu jabatan. Banyak cara mengisi kedua jabatan tersebut adalah ....

- A. 100  
  <sub>Salah: menghitung $10 \times 10$ (siswa boleh merangkap)</sub>
- B. 45  
  <sub>Salah: membagi dengan $2!$, seolah jabatan tidak dibedakan</sub>
- **C. 90** ✅  
  <sub>Benar: tersisa 10 siswa untuk 2 jabatan berbeda, $P(10,2) = 10 \times 9 = 90$</sub>
- D. 132  
  <sub>Salah: memakai 12 siswa, $12 \times 11$, lupa dua siswa sudah menjabat</sub>

**Pembahasan:** Sisa $12 - 2 = 10$ siswa mengisi 2 jabatan berbeda: $P(10,2) = 10 \times 9 = 90$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12-b03-b-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: rumus permutasi siklis*

Banyak susunan melingkar (permutasi siklis) dari $n$ objek berbeda dinyatakan dengan ....

- **A. $(n-1)!$** ✅  
  <sub>Benar: $n!$ susunan berjajar dibagi $n$ susunan yang sama pada lingkaran, sehingga $\frac{n!}{n} = (n-1)!$</sub>
- B. $(n+1)!$  
  <sub>Salah: salah mengingat tanda pada rumus</sub>
- C. $n!$  
  <sub>Salah: menyamakan dengan susunan berjajar</sub>
- D. $\frac{n!}{2}$  
  <sub>Salah: membagi dengan 2, bukan dengan $n$</sub>

**Pembahasan:** Terdapat $n$ susunan berjajar yang menjadi satu susunan melingkar, sehingga banyak susunan siklis $= \frac{n!}{n} = (n-1)!$.
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12-b03-b-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: permutasi n dari n objek*

Nilai dari $P(3,3)$ adalah ....

- **A. 6** ✅  
  <sub>Benar: $P(3,3) = \frac{3!}{0!} = 3! = 6$</sub>
- B. 27  
  <sub>Salah: menghitung $3^3$</sub>
- C. 3  
  <sub>Salah: mengira hasilnya sama dengan $n$</sub>
- D. 9  
  <sub>Salah: menghitung $3 \times 3$</sub>

**Pembahasan:** Permutasi $n$ dari $n$ objek adalah $n!$, jadi $P(3,3) = 3! = 3 \times 2 \times 1 = 6$.
**Acuan:** siswa — siswa hal.112

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12-b03-b-medium-bt01-001
*variasi (angka) | C3 | 2 langkah | jenis: pembagian ke kelompok berukuran berbeda*

Sebuah kantor akan mengirim 10 pegawai ke lokasi pelatihan dengan tiga kendaraan berbeda. Kapasitas kendaraan secara berturut-turut adalah 6, 3, dan 1 orang dan semua kursi terisi penuh. Berapa banyak kemungkinan para pegawai dapat terangkut oleh ketiga kendaraan tersebut?

- A. 3.628.800  
  <sub>Salah: menghitung $10!$ tanpa membagi dengan faktorial kapasitas</sub>
- B. 604.800  
  <sub>Salah: hanya membagi dengan $3!$, lupa membagi dengan $6!$</sub>
- C. 5.040  
  <sub>Salah: hanya membagi dengan $6!$, lupa membagi dengan $3!$</sub>
- **D. 840** ✅  
  <sub>Benar: membagi 10 pegawai ke kelompok berukuran 6, 3, dan 1 memberi $\frac{10!}{6!\,3!\,1!} = 840$</sub>

**Pembahasan:** Kendaraan berbeda dan terisi penuh: $\frac{10!}{6!\,3!\,1!} = \frac{3.628.800}{720 \times 6 \times 1} = 840$.
**Acuan:** pretest — kelas12-b03-p0118-latihan-3-2-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12-b03-b-medium-bt01-002
*variasi (konteks) | C3 | 2 langkah | jenis: pembagian ke kelompok berukuran berbeda*

Seorang pelatih bulu tangkis membagi 9 atlet ke tiga lapangan latihan yang diberi nama Lapangan A, B, dan C. Lapangan A dan B masing-masing menampung 4 atlet, sedangkan Lapangan C menampung 1 atlet. Banyak cara pelatih membagi seluruh atlet tersebut adalah ....

- A. 362.880  
  <sub>Salah: menghitung $9!$ tanpa membagi dengan faktorial kapasitas</sub>
- B. 315  
  <sub>Salah: membagi lagi dengan $2!$ karena mengira lapangan berkapasitas sama tidak dibedakan padahal lapangan bernama berbeda</sub>
- **C. 630** ✅  
  <sub>Benar: banyak pembagian $= \frac{9!}{4!\,4!\,1!} = 630$</sub>
- D. 15.120  
  <sub>Salah: hanya membagi dengan satu $4!$, lupa $4!$ yang kedua</sub>

**Pembahasan:** Lapangan berbeda sehingga $\frac{9!}{4!\,4!\,1!} = \frac{362.880}{24 \times 24 \times 1} = 630$.
**Acuan:** pretest — kelas12-b03-p0118-latihan-3-2-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12-b03-b-medium-bt01-003
*variasi (angka) | C4 | 3 langkah | jenis: aturan pengisian dan permutasi*

Sebuah kawasan menetapkan pelat nomor yang diawali dua huruf BK, diikuti tiga angka yang dipilih dari 1, 2, 7, 8, dan 9 dan boleh berulang, serta diakhiri dua huruf berbeda yang dipilih dari huruf P, Q, R, S, T, dan U. Banyak pelat nomor yang dapat dibuat adalah ....

- **A. 3.750** ✅  
  <sub>Benar: $1 \times 5^3 \times P(6,2) = 125 \times 30 = 3.750$</sub>
- B. 4.500  
  <sub>Salah: mengira dua huruf akhir boleh berulang, $6^2 = 36$</sub>
- C. 1.800  
  <sub>Salah: mengira ketiga angka tidak boleh berulang, $5 \times 4 \times 3 = 60$</sub>
- D. 1.875  
  <sub>Salah: memakai kombinasi $C(6,2)=15$ untuk dua huruf akhir, bukan permutasi</sub>

**Pembahasan:** Dua huruf awal tetap (1 cara); tiga angka boleh berulang: $5^3 = 125$; dua huruf akhir berbeda: $P(6,2) = 30$. Total $125 \times 30 = 3.750$.
**Acuan:** pretest — kelas12-b03-p0119-latihan-3-2-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12-b03-b-medium-bt01-004
*variasi (konteks) | C4 | 3 langkah | jenis: aturan pengisian dan permutasi*

Kode anggota sebuah koperasi diawali huruf tetap KS, kemudian tiga digit yang masing-masing dipilih dari 1, 3, 5, dan 7 (digit boleh berulang), dan ditutup tiga huruf berbeda yang dipilih dari M, N, O, P, dan Q. Banyak kode anggota yang dapat dibentuk adalah ....

- A. 8.000  
  <sub>Salah: mengira huruf boleh berulang, $5^3 = 125$</sub>
- B. 640  
  <sub>Salah: memakai kombinasi $C(5,3)=10$ untuk tiga huruf, bukan permutasi</sub>
- **C. 3.840** ✅  
  <sub>Benar: $4^3 \times P(5,3) = 64 \times 60 = 3.840$</sub>
- D. 1.440  
  <sub>Salah: mengira digit tidak boleh berulang, $P(4,3) = 24$</sub>

**Pembahasan:** Tiga digit boleh berulang: $4^3 = 64$; tiga huruf berbeda berurutan: $P(5,3) = 60$. Total $64 \times 60 = 3.840$.
**Acuan:** pretest — kelas12-b03-p0119-latihan-3-2-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12-b03-b-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: aturan pengisian dan permutasi*

Bayu akan membuat kata sandi dua belas karakter. Namanya, yang terdiri dari delapan karakter, ditulis berurutan pada awal atau pada akhir kata sandi, kemudian ditambahkan empat angka berbeda yang dipilih secara acak dari angka 1, 2, 3, 4, 5, 6, 7, dan 8. Banyak cara menyusun kata sandi tersebut adalah ....

- **A. 3.360** ✅  
  <sub>Benar: $2 \times P(8,4) = 2 \times 1.680 = 3.360$</sub>
- B. 8.192  
  <sub>Salah: mengira angka boleh berulang, $2 \times 8^4$</sub>
- C. 1.680  
  <sub>Salah: lupa mengalikan dengan 2 posisi (awal atau akhir) untuk nama</sub>
- D. 140  
  <sub>Salah: memakai kombinasi $C(8,4)=70$ dikali 2 sehingga urutan angka diabaikan</sub>

**Pembahasan:** Nama di awal atau di akhir: 2 cara. Empat angka berbeda berurutan: $P(8,4) = 8 \times 7 \times 6 \times 5 = 1.680$. Total $2 \times 1.680 = 3.360$.
**Acuan:** pretest — kelas12-b03-p0138-uji-kompetensi-bab-3-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12-b03-b-medium-bt01-006
*variasi (konteks) | C3 | 3 langkah | jenis: aturan pengisian dan permutasi*

Sebuah toko daring menerbitkan kode voucher yang memuat kata HEMAT secara berurutan di awal atau di akhir kode, lalu ditambah dua angka berbeda dari 0, 1, 2, ..., 9 yang disusun secara bebas. Banyak kode voucher yang mungkin dibuat adalah ....

- **A. 180** ✅  
  <sub>Benar: $2 \times P(10,2) = 2 \times 90 = 180$</sub>
- B. 45  
  <sub>Salah: memakai kombinasi $C(10,2)$ dan lupa 2 posisi sehingga urutan angka diabaikan</sub>
- C. 90  
  <sub>Salah: lupa mengalikan dengan 2 posisi untuk kata HEMAT</sub>
- D. 200  
  <sub>Salah: mengira kedua angka boleh sama, $2 \times 10^2$</sub>

**Pembahasan:** Kata HEMAT di awal atau akhir: 2 cara; dua angka berbeda berurutan: $P(10,2) = 90$. Total $2 \times 90 = 180$.
**Acuan:** pretest — kelas12-b03-p0138-uji-kompetensi-bab-3-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12-b03-b-medium-bt01-007
*variasi (angka) | C4 | 4 langkah | jenis: bilangan dari angka dengan syarat besar*

Sebuah bank menerbitkan kartu undian dengan nomor berupa bilangan lima angka yang disusun dari angka 2, 4, 4, 7, dan 9. Banyak kartu dengan nomor lebih besar daripada 47000 adalah ....

- A. 24  
  <sub>Salah: hanya menghitung angka pertama 9 dan 7, lupa kasus angka pertama 4</sub>
- B. 30  
  <sub>Salah: lupa kasus angka pertama 4 dan kedua 7</sub>
- **C. 36** ✅  
  <sub>Benar: kasus angka pertama 9: 12, angka pertama 7: 12, angka pertama 4 dan kedua 9: 6, angka pertama 4 dan kedua 7: 6, total $36$</sub>
- D. 48  
  <sub>Salah: menganggap semua nomor berawalan 4 memenuhi sehingga $12+12+24$</sub>

**Pembahasan:** Angka pertama 9: $\frac{4!}{2!} = 12$. Angka pertama 7: $12$. Angka pertama 4: sisa 2, 4, 7, 9; kedua 9: $3! = 6$; kedua 7: $3! = 6$; kedua 4 atau 2 menghasilkan nomor di bawah 47000. Total $12 + 12 + 6 + 6 = 36$.
**Acuan:** pretest — kelas12-b03-p0138-uji-kompetensi-bab-3-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12-b03-b-medium-bt01-008
*variasi (konteks) | C4 | 4 langkah | jenis: bilangan dari angka dengan syarat besar*

Sebuah toko buku membuat voucher belanja dengan nomor seri berupa bilangan lima angka yang disusun dari angka 1, 3, 3, 5, dan 8 (setiap angka dipakai tepat sekali). Banyak voucher dengan nomor seri kurang dari 53000 adalah ....

- A. 42  
  <sub>Salah: memakai $3!$ pada kasus angka pertama 5 dan kedua 1 (lupa angka 3 kembar), sehingga $12+24+6$</sub>
- **B. 39** ✅  
  <sub>Benar: angka pertama 1: 12, angka pertama 3: 24, angka pertama 5 dan kedua 1: 3, total $39$</sub>
- C. 48  
  <sub>Salah: menghitung angka pertama 1 sebagai $4! = 24$ tanpa membagi $2!$ dan lupa kasus angka pertama 5</sub>
- D. 36  
  <sub>Salah: lupa kasus angka pertama 5 dan kedua 1, hanya $12 + 24$</sub>

**Pembahasan:** Angka pertama 1: sisa 3, 3, 5, 8 sehingga $\frac{4!}{2!} = 12$. Angka pertama 3: sisa 1, 3, 5, 8 sehingga $4! = 24$. Angka pertama 5: kedua harus 1 (sisa 3, 3, 8) sehingga $\frac{3!}{2!} = 3$; kedua 3 menghasilkan nomor di atas 53000. Total $12 + 24 + 3 = 39$.
**Acuan:** pretest — kelas12-b03-p0138-uji-kompetensi-bab-3-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12-b03-b-medium-bt01-009
*variasi (konteks) | C4 | 4 langkah | jenis: permutasi siklis dengan syarat*

Enam pengurus OSIS putra dan empat pengurus OSIS putri akan duduk melingkar mengelilingi meja rapat bundar. Banyak cara duduk jika tidak ada dua putri yang duduk berdampingan adalah ....

- A. 362.880  
  <sub>Salah: menghitung duduk bebas $(10-1)!$ tanpa syarat</sub>
- B. 1.800  
  <sub>Salah: memakai kombinasi $C(6,4) = 15$ untuk celah putri, $120 \times 15$</sub>
- C. 259.200  
  <sub>Salah: mengatur putra seperti berjajar, $6! \times P(6,4)$</sub>
- **D. 43.200** ✅  
  <sub>Benar: $(6-1)! \times P(6,4) = 120 \times 360 = 43.200$</sub>

**Pembahasan:** Putra duduk siklis: $5! = 120$. Terbentuk 6 celah di antara putra; empat putri menempati 4 dari 6 celah secara berurutan: $P(6,4) = 360$. Total $120 \times 360 = 43.200$.
**Acuan:** siswa — siswa hal.116 Contoh 3.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12-b03-b-medium-bt01-010
*variasi (konteks) | C4 | 4 langkah | jenis: permutasi siklis dengan syarat*

Lima siswa putra dan dua siswa putri duduk melingkar pada sebuah meja makan bundar dalam suatu perjamuan. Banyak susunan duduk apabila kedua siswa putri tidak duduk berdampingan adalah ....

- A. 240  
  <sub>Salah: memakai kombinasi $C(5,2) = 10$ untuk celah putri, $24 \times 10$</sub>
- **B. 480** ✅  
  <sub>Benar: $(5-1)! \times P(5,2) = 24 \times 20 = 480$</sub>
- C. 2.400  
  <sub>Salah: mengatur putra seperti berjajar, $5! \times P(5,2)$</sub>
- D. 720  
  <sub>Salah: menghitung duduk bebas $(7-1)!$ tanpa syarat</sub>

**Pembahasan:** Putra duduk siklis: $4! = 24$. Terbentuk 5 celah; dua putri menempati 2 celah berbeda secara berurutan: $P(5,2) = 20$. Total $24 \times 20 = 480$.
**Acuan:** siswa — siswa hal.116 Contoh 3.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12-b03-b-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: unsur harus berdampingan (berjajar)*

Delapan orang berdiri berjajar dalam satu barisan untuk berfoto. Dua di antaranya, Amir dan Bayu, harus selalu berdampingan. Banyak susunan barisan yang mungkin adalah ....

- A. 1.440  
  <sub>Salah: menyusun hanya 6 objek (satu objek terlewat) lalu mengalikan $2!$, yaitu $2 \times 6!$</sub>
- B. 40.320  
  <sub>Salah: menghitung $8!$ tanpa syarat berdampingan</sub>
- **C. 10.080** ✅  
  <sub>Benar: blok Amir-Bayu dan 6 orang lain menjadi 7 objek: $7! \times 2! = 10.080$</sub>
- D. 5.040  
  <sub>Salah: lupa susunan di dalam blok, hanya $7!$</sub>

**Pembahasan:** Gabungkan Amir dan Bayu menjadi satu blok sehingga ada $7$ objek: $7! = 5.040$. Di dalam blok ada $2! = 2$ susunan. Total $5.040 \times 2 = 10.080$.
**Acuan:** siswa — siswa hal.119

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12-b03-b-medium-bt01-012
*orisinal | C4 | 4 langkah | jenis: unsur tidak boleh berdampingan (berjajar)*

Tujuh orang duduk berjajar pada satu baris kursi. Dua di antaranya, Citra dan Dodi, tidak boleh duduk berdampingan. Banyak susunan duduk yang mungkin adalah ....

- A. 1.440  
  <sub>Salah: hanya menghitung susunan saat Citra dan Dodi berdampingan</sub>
- B. 5.040  
  <sub>Salah: menghitung $7!$ tanpa syarat</sub>
- **C. 3.600** ✅  
  <sub>Benar: $7! - 2 \times 6! = 5.040 - 1.440 = 3.600$</sub>
- D. 4.320  
  <sub>Salah: mengurangi $7! - 6!$ (lupa susunan di dalam blok $2!$)</sub>

**Pembahasan:** Semua susunan: $7! = 5.040$. Citra dan Dodi berdampingan: $2 \times 6! = 1.440$. Tidak berdampingan: $5.040 - 1.440 = 3.600$.
**Acuan:** siswa — siswa hal.118

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12-b03-b-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: huruf kata dengan syarat posisi*

Seluruh huruf pada kata SEMESTER disusun menjadi susunan berbeda yang diawali huruf E. Banyak susunan yang mungkin adalah ....

- **A. 1.260** ✅  
  <sub>Benar: huruf pertama E, sisa 7 huruf dengan S 2 kali dan E 2 kali: $\frac{7!}{2!\,2!} = 1.260$</sub>
- B. 2.520  
  <sub>Salah: hanya membagi dengan $2!$, lupa huruf S yang juga berulang</sub>
- C. 840  
  <sub>Salah: membagi dengan $3!$ untuk sisa huruf, padahal E tinggal 2 buah (S juga 2 kali)</sub>
- D. 6.720  
  <sub>Salah: menghitung semua susunan $\frac{8!}{3!}$ tanpa syarat huruf pertama</sub>

**Pembahasan:** SEMESTER: S 2 kali, E 3 kali, M, T, R. Setelah E menempati posisi pertama, sisa 7 huruf dengan S dua kali dan E dua kali: $\frac{7!}{2!\,2!} = \frac{5.040}{4} = 1.260$.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12-b03-b-medium-bt01-014
*orisinal | C4 | 4 langkah | jenis: huruf kata dengan syarat tidak berdampingan*

Seluruh huruf pada kata BANANA disusun menjadi susunan berbeda sehingga kedua huruf N tidak berdampingan. Banyak susunan yang mungkin adalah ....

- A. 20  
  <sub>Salah: hanya menghitung susunan saat kedua N berdampingan</sub>
- B. 60  
  <sub>Salah: menghitung semua susunan tanpa syarat N tidak berdampingan</sub>
- C. 30  
  <sub>Salah: membagi semua susunan dengan 2 untuk syarat N, bukan mengurangi susunan berdampingan</sub>
- **D. 40** ✅  
  <sub>Benar: $\frac{6!}{3!\,2!} - \frac{5!}{3!} = 60 - 20 = 40$</sub>

**Pembahasan:** BANANA: 6 huruf, A 3 kali, N 2 kali: $\frac{6!}{3!\,2!} = 60$. Kedua N berdampingan dianggap satu blok sehingga 5 objek dengan A 3 kali: $\frac{5!}{3!} = 20$. Tidak berdampingan: $60 - 20 = 40$.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12-b03-b-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: permutasi siklis dengan syarat*

Tujuh orang tamu duduk mengelilingi sebuah meja bundar. Dua di antaranya, Eka dan Feri, harus selalu duduk berdampingan. Banyak susunan duduk yang berbeda adalah ....

- **A. 240** ✅  
  <sub>Benar: blok Eka-Feri dan 5 tamu lain menjadi 6 objek siklis: $(6-1)! \times 2! = 240$</sub>
- B. 120  
  <sub>Salah: lupa susunan di dalam blok, hanya $(6-1)!$</sub>
- C. 720  
  <sub>Salah: menghitung duduk bebas $(7-1)!$ tanpa syarat berdampingan</sub>
- D. 1.440  
  <sub>Salah: memakai $6!$ untuk 6 objek seperti berjajar, $6! \times 2$</sub>

**Pembahasan:** Gabungkan Eka dan Feri menjadi satu blok sehingga ada 6 objek yang duduk melingkar: $(6-1)! = 120$. Susunan di dalam blok $2! = 2$. Total $120 \times 2 = 240$.
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12-b03-b-medium-bt01-016
*orisinal | C4 | 4 langkah | jenis: permutasi siklis dengan syarat*

Empat pasang suami istri duduk mengelilingi meja bundar pada suatu acara makan malam. Setiap pasangan harus duduk berdampingan. Banyak susunan duduk yang berbeda adalah ....

- A. 384  
  <sub>Salah: memakai $4!$ untuk susunan blok seperti berjajar, $4! \times 2^4$</sub>
- **B. 96** ✅  
  <sub>Benar: 4 blok siklis: $(4-1)! = 6$, tiap blok $2!$: $6 \times 2^4 = 96$</sub>
- C. 6  
  <sub>Salah: hanya menghitung $(4-1)!$ untuk susunan blok, lupa susunan dalam pasangan</sub>
- D. 48  
  <sub>Salah: membagi hasil dengan 2 karena mengira susunan cermin dianggap sama, $\frac{6 \times 2^4}{2}$</sub>

**Pembahasan:** Empat pasangan menjadi 4 blok yang disusun siklis: $(4-1)! = 6$. Setiap pasangan dapat bertukar tempat dalam $2!$ cara, sehingga $2^4 = 16$. Total $6 \times 16 = 96$.
**Acuan:** siswa — siswa hal.117

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12-b03-b-medium-bt01-017
*orisinal | C4 | 4 langkah | jenis: penjumlahan dua kasus pada bilangan*

Dari angka 0, 1, 2, 3, 4, 5, dan 6 akan dibentuk bilangan tiga angka yang genap dan tidak memuat angka berulang. Banyak bilangan yang dapat dibentuk adalah ....

- A. 30  
  <sub>Salah: hanya menghitung bilangan dengan satuan 0</sub>
- **B. 105** ✅  
  <sub>Benar: satuan 0: $P(6,2) = 30$; satuan 2, 4, atau 6: $3 \times 5 \times 5 = 75$; total $105$</sub>
- C. 75  
  <sub>Salah: hanya menghitung bilangan dengan satuan 2, 4, 6, lupa satuan 0</sub>
- D. 120  
  <sub>Salah: mengira angka ratusan boleh 0 pada kasus satuan 2, 4, 6, sehingga $30 + 3 \times 30$</sub>

**Pembahasan:** Kasus satuan 0: ratusan dan puluhan dari 6 angka sisa, $P(6,2) = 30$. Kasus satuan 2, 4, atau 6 (3 pilihan): ratusan bukan 0 dan bukan satuan (5 pilihan), puluhan dari 5 angka sisa (5 pilihan): $3 \times 5 \times 5 = 75$. Total $30 + 75 = 105$.
**Acuan:** siswa — siswa hal.119

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12-b03-b-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: persamaan permutasi*

Diketahui $n$ bilangan asli dengan $n \geq 2$ dan $P(n,2) = 90$. Nilai $n$ adalah ....

- A. 45  
  <sub>Salah: menganggap $P(n,2) = 2n$ sehingga $n = 45$</sub>
- **B. 10** ✅  
  <sub>Benar: $P(n,2) = n(n-1) = 90 = 10 \times 9$ sehingga $n = 10$</sub>
- C. 9  
  <sub>Salah: mengambil faktor yang lebih kecil dari pasangan $10 \times 9$</sub>
- D. 91  
  <sub>Salah: menganggap $n - 1 = 90$ dan mengabaikan faktor $n$</sub>

**Pembahasan:** $P(n,2) = \frac{n!}{(n-2)!} = n(n-1) = 90$. Karena $10 \times 9 = 90$, diperoleh $n^2 - n - 90 = 0$, $(n-10)(n+9) = 0$, dan $n$ bilangan asli sehingga $n = 10$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12-b03-b-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: persamaan permutasi*

Diketahui $n$ bilangan asli dengan $n \geq 3$ dan $P(n,3) = 6 \times P(n,2)$. Nilai $n$ adalah ....

- A. 7  
  <sub>Salah: menyederhanakan menjadi $n - 1 = 6$</sub>
- B. 6  
  <sub>Salah: mengira $n = 6$ dari angka pengali, lupa $n - 2 = 6$</sub>
- C. 12  
  <sub>Salah: menyelesaikan $n - 2 = 6$ menjadi $n = 6 \times 2$</sub>
- **D. 8** ✅  
  <sub>Benar: $n(n-1)(n-2) = 6\,n(n-1)$ sehingga $n - 2 = 6$ dan $n = 8$</sub>

**Pembahasan:** $P(n,3) = n(n-1)(n-2)$ dan $P(n,2) = n(n-1)$. Persamaan menjadi $n(n-1)(n-2) = 6\,n(n-1)$. Karena $n \geq 3$, kedua ruas dapat dibagi $n(n-1)$ sehingga $n - 2 = 6$ dan $n = 8$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12-b03-b-medium-bt01-020
*orisinal | C4 | 3 langkah | jenis: pemodelan permutasi r dari n dengan syarat*

Dari 7 siswa yang bersedia akan dipilih seorang ketua, seorang sekretaris, dan seorang bendahara. Setiap siswa menduduki paling banyak satu jabatan dan Dina tidak bersedia menjadi ketua (tetapi boleh memegang jabatan lain). Banyak susunan pengurus yang mungkin adalah ....

- A. 210  
  <sub>Salah: menghitung $P(7,3)$ tanpa syarat Dina tidak menjadi ketua</sub>
- B. 30  
  <sub>Salah: hanya menghitung susunan sekretaris dan bendahara setelah ketua dipilih</sub>
- C. 252  
  <sub>Salah: mengira sekretaris dan bendahara dipilih dari 7 siswa, $6 \times 7 \times 6$</sub>
- **D. 180** ✅  
  <sub>Benar: ketua dipilih dari 6 siswa selain Dina, lalu $P(6,2) = 30$ untuk dua jabatan lain: $6 \times 30 = 180$</sub>

**Pembahasan:** Ketua dipilih dari 6 siswa selain Dina: 6 cara. Sekretaris dan bendahara dipilih dari 6 siswa yang tersisa (termasuk Dina): $P(6,2) = 30$. Total $6 \times 30 = 180$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12-b03-b-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi penyelesaian siswa*

Budi menghitung banyak susunan huruf berbeda dari seluruh huruf pada kata STATISTIKA (S dua kali, T tiga kali, A dua kali, I dua kali, dan K satu kali) dengan cara $\frac{10!}{2!\,2!\,2!} = 453.600$. Banyak susunan huruf berbeda yang benar adalah ....

- A. 151.200  
  <sub>Salah: membagi dengan $2!\,3!\,2!$ saja, lupa $2!$ untuk huruf I</sub>
- **B. 75.600** ✅  
  <sub>Benar: ada empat huruf yang berulang sehingga penyebutnya $2!\,3!\,2!\,2! = 48$ dan $\frac{10!}{48} = 75.600$</sub>
- C. 226.800  
  <sub>Salah: menganggap huruf T hanya berulang dua kali sehingga memakai $2!\,2!\,2!\,2!$</sub>
- D. 453.600  
  <sub>Salah: hasil Budi: lupa membagi dengan $3!$ untuk huruf T</sub>

**Pembahasan:** Huruf berulang: S (2), T (3), A (2), I (2), K (1). Banyak susunan $= \frac{10!}{2!\,3!\,2!\,2!} = \frac{3.628.800}{48} = 75.600$. Hitungan Budi melewatkan $3!$ untuk huruf T.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12-b03-b-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: tidak berdampingan beberapa unsur (celah)*

Tujuh orang berdiri berjajar dalam satu barisan. Tiga di antaranya, yaitu Aldi, Beni, dan Cica, tidak boleh ada dua orang yang berdiri berdampingan (artinya di antara dua dari ketiganya selalu ada orang lain). Banyak susunan barisan yang mungkin adalah ....

- **A. 1.440** ✅  
  <sub>Benar: empat orang lain disusun $4! = 24$; terbentuk 5 celah; Aldi, Beni, Cica menempati 3 celah berbeda secara berurutan $P(5,3) = 60$; total $24 \times 60 = 1.440$</sub>
- B. 3.000  
  <sub>Salah: mengira ketiga orang boleh memilih celah yang sama, $4! \times 5^3$</sub>
- C. 720  
  <sub>Salah: mengurangi $7! - 3 \times 2 \times 6!$ tanpa menambah kembali irisan ketiga pasangan</sub>
- D. 240  
  <sub>Salah: memakai kombinasi $C(5,3) = 10$ untuk celah, sehingga urutan ketiga orang diabaikan</sub>

**Pembahasan:** Susun 4 orang lain: $4! = 24$. Ada 5 celah (dua ujung dan tiga tengah). Tiga orang bersyarat menempati tiga celah berbeda dan urutannya penting: $P(5,3) = 60$. Total $24 \times 60 = 1.440$.
**Acuan:** siswa — siswa hal.118

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12-b03-b-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim dan contoh penyangkal*

Seorang siswa mengklaim bahwa untuk setiap bilangan asli $n$ dan $r$ dengan $1 \leq r < n$ selalu berlaku $P(n,r) < n!$. Pasangan $(n, r)$ berikut yang merupakan contoh penyangkal klaim tersebut adalah ....

- A. $(n,r) = (6,4)$  
  <sub>Salah: $P(6,4) = 360 < 720$, justru mendukung klaim</sub>
- B. $(n,r) = (5,2)$  
  <sub>Salah: $P(5,2) = 20 < 120$, justru mendukung klaim</sub>
- **C. $(n,r) = (7,6)$** ✅  
  <sub>Benar: $P(7,6) = \frac{7!}{1!} = 5.040 = 7!$ sehingga $P(7,6)$ tidak kurang dari $7!$</sub>
- D. $(n,r) = (8,5)$  
  <sub>Salah: $P(8,5) = 6.720 < 40.320$, justru mendukung klaim</sub>

**Pembahasan:** $P(n,r) = \frac{n!}{(n-r)!}$. Untuk $r = n-1$ penyebutnya $1! = 1$ sehingga $P(n,n-1) = n!$, bukan lebih kecil. Maka $(7,6)$ menyangkal klaim: $P(7,6) = 5.040 = 7!$. Tiga pasangan lain menghasilkan $P(n,r) < n!$.
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12-b03-b-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: pertumbuhan faktorial*

Panitia ingin tamu duduk mengelilingi sebuah meja bundar dengan lebih dari 100.000 susunan duduk berbeda. Banyak tamu paling sedikit yang diperlukan adalah ....

- **A. 10** ✅  
  <sub>Benar: $(n-1)! > 100.000$; $8! = 40.320$ belum cukup, $9! = 362.880$ cukup, sehingga $n - 1 = 9$ dan $n = 10$</sub>
- B. 8  
  <sub>Salah: mengira $8!$ sudah lebih dari 100.000 padahal nilainya 40.320</sub>
- C. 11  
  <sub>Salah: menggeser satu terlalu jauh: mengira perlu $(n-1) = 10$</sub>
- D. 9  
  <sub>Salah: memakai $n! > 100.000$ (karena $9! = 362.880$) dan lupa susunan melingkar $(n-1)!$</sub>

**Pembahasan:** Susunan melingkar $n$ orang $= (n-1)!$. Dengan $8! = 40.320 < 100.000 < 362.880 = 9!$ diperoleh $n-1 = 9$ sehingga $n = 10$ (sepuluh tamu menghasilkan $9! = 362.880$; sembilan tamu hanya $8! = 40.320$).
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12-b03-b-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: persamaan permutasi dengan parameter*

Diketahui $n$ bilangan asli dengan $n \geq 3$ dan $P(n+1,3) = 4 \times P(n,3)$. Nilai $n$ adalah ....

- **A. 3** ✅  
  <sub>Benar: $(n+1)n(n-1) = 4\,n(n-1)(n-2)$ sehingga $n+1 = 4(n-2)$ dan $n = 3$</sub>
- B. 4  
  <sub>Salah: mengambil $n + 1 = 4$ sebagai nilai $n$</sub>
- C. 9  
  <sub>Salah: mendapat $3n = 9$ lalu mengambil 9 tanpa membagi 3</sub>
- D. 1  
  <sub>Salah: menulis $4(n-2)$ sebagai $4n - 2$ sehingga $n + 1 = 4n - 2$ dan $n = 1$</sub>

**Pembahasan:** $P(n+1,3) = (n+1)n(n-1)$ dan $P(n,3) = n(n-1)(n-2)$. Bagi kedua ruas dengan $n(n-1)$ (tidak nol karena $n \geq 3$): $n + 1 = 4(n-2) = 4n - 8$ sehingga $3n = 9$ dan $n = 3$. Cek: $P(4,3) = 24 = 4 \times P(3,3) = 4 \times 6$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12-b03-b-hard-bt01-006
*orisinal | C5 | 5 langkah | jenis: permutasi siklis dengan dua syarat*

Delapan orang duduk mengelilingi sebuah meja bundar. Dua di antaranya, Andra dan Bima, harus duduk berdampingan, sedangkan Citra tidak boleh duduk bersebelahan dengan Andra maupun Bima. Banyak susunan duduk yang berbeda adalah ....

- A. 480  
  <sub>Salah: hanya menghitung susunan saat Citra bersebelahan dengan blok</sub>
- **B. 960** ✅  
  <sub>Benar: blok Andra-Bima dengan 6 orang lain: $6! \times 2 = 1.440$; Citra bersebelahan dengan blok: $2 \times 5! \times 2 = 480$; $1.440 - 480 = 960$</sub>
- C. 1.200  
  <sub>Salah: mengurangi hanya satu sisi blok ($2 \times 5!$ saja), lupa susunan dalam blok $2!$ pada kasus Citra bersebelahan</sub>
- D. 1.440  
  <sub>Salah: hanya memenuhi syarat berdampingan, lupa syarat Citra</sub>

**Pembahasan:** Anggap Andra-Bima satu blok: 7 objek melingkar $(7-1)! = 720$, dikali $2!$ susunan dalam blok = 1.440. Dengan blok sebagai acuan, 6 orang lain menempati 6 kursi berjajar; Citra di salah satu dari 2 kursi ujung (bersebelahan dengan blok): $2 \times 5! = 240$, dikali $2!$ = 480. Yang memenuhi: $1.440 - 480 = 960$.
**Acuan:** siswa — siswa hal.117

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12-b03-b-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: permutasi siklis dengan dua syarat*

Lima laki-laki dan lima perempuan duduk mengelilingi meja bundar dengan tempat duduk selang-seling (tidak ada dua orang berjenis kelamin sama yang bersebelahan). Di antara mereka ada pasangan Pak Ali dan Bu Sari yang tidak ingin duduk bersebelahan. Banyak susunan duduk yang berbeda adalah ....

- A. 1.152  
  <sub>Salah: hanya menghitung susunan saat Bu Sari duduk di samping Pak Ali, $24 \times 2 \times 4!$</sub>
- **B. 1.728** ✅  
  <sub>Benar: laki-laki siklis $4! = 24$; perempuan pada 5 celah $5! = 120$ dan Bu Sari tidak pada 2 celah di samping Pak Ali: $120 - 2 \times 4! = 72$; total $24 \times 72 = 1.728$</sub>
- C. 1.440  
  <sub>Salah: membagi 2.880 dengan 2 untuk syarat pasangan</sub>
- D. 2.880  
  <sub>Salah: hanya selang-seling, lupa syarat Pak Ali dan Bu Sari</sub>

**Pembahasan:** Tempatkan 5 laki-laki melingkar: $(5-1)! = 24$. Perempuan mengisi 5 celah di antara mereka: $5! = 120$. Bu Sari bersebelahan dengan Pak Ali bila menempati salah satu dari 2 celah di samping Pak Ali: $2 \times 4! = 48$. Susunan perempuan yang sah $= 120 - 48 = 72$. Total $24 \times 72 = 1.728$.
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12-b03-b-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: evaluasi penyelesaian siswa*

Dari huruf A, B, C, D, E, F, dan G akan disusun kode empat huruf berbeda yang memuat huruf A atau huruf B (boleh keduanya). Dina menghitung: kode memuat A ada $4 \times P(6,3) = 480$, kode memuat B ada 480, sehingga totalnya 960. Perhitungan Dina keliru karena ada kode yang terhitung dua kali. Banyak kode yang benar adalah ....

- A. 480  
  <sub>Salah: hanya menghitung kode yang memuat A</sub>
- B. 960  
  <sub>Salah: hasil Dina: tidak mengurangi kode yang memuat A dan B sekaligus</sub>
- **C. 720** ✅  
  <sub>Benar: kode yang memuat A dan B sekaligus ada $4 \times 3 \times P(5,2) = 240$ dan terhitung dua kali, sehingga $960 - 240 = 720$</sub>
- D. 240  
  <sub>Salah: hanya menghitung kode yang memuat A dan B sekaligus</sub>

**Pembahasan:** Kode yang memuat A dan B sekaligus terhitung di kedua kelompok: pilih posisi A (4) dan B (3), dua posisi lain dari 5 huruf: $P(5,2) = 20$, jadi $4 \times 3 \times 20 = 240$. Total benar $= 480 + 480 - 240 = 720$. Cek: $P(7,4) - P(5,4) = 840 - 120 = 720$.
**Acuan:** siswa — siswa hal.118

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12-b03-b-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: evaluasi klaim dan contoh penyangkal*

Huruf-huruf pada kata MISSISSIPPI terdiri atas M satu kali, I empat kali, S empat kali, dan P dua kali. Pernyataan yang benar tentang susunan huruf berbeda dari seluruh huruf kata tersebut adalah ....

- A. Banyak seluruh susunan adalah $\frac{11!}{4!+4!+2!} = 1.330.560$  
  <sub>Salah: mengganti hasil kali faktorial pada penyebut dengan jumlah</sub>
- B. Banyak susunan yang keempat huruf S-nya berdampingan adalah $\frac{8!}{4!\,2!} \times 4! = 20.160$  
  <sub>Salah: mengalikan $4!$ untuk susunan di dalam blok padahal huruf S identik</sub>
- C. Banyak susunan yang diawali huruf M adalah $\frac{11!}{4!\,4!\,2!} = 34.650$  
  <sub>Salah: memakai 11 huruf padahal setelah M tinggal 10 huruf</sub>
- **D. Banyak susunan yang kedua huruf P-nya berdampingan adalah $\frac{10!}{4!\,4!} = 6.300$** ✅  
  <sub>Benar: blok P bersama M, 4 I, dan 4 S membentuk 10 objek sehingga $\frac{10!}{4!\,4!} = 6.300$</sub>

**Pembahasan:** Kedua P berdampingan dijadikan satu blok (identik, tanpa susunan dalam): objek menjadi blok P, M, 4 I, 4 S = 10 objek sehingga $\frac{10!}{4!\,4!} = 6.300$. Pernyataan lain keliru: seluruh susunan $\frac{11!}{4!\,4!\,2!} = 34.650$; diawali M: $\frac{10!}{4!\,4!\,2!} = 3.150$; empat S berdampingan: $\frac{8!}{4!\,2!} = 840$.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12-b03-b-hard-bt01-010
*orisinal | C5 | 3 langkah | jenis: syarat urutan relatif*

Delapan orang berdiri berjajar dalam satu barisan. Salah satunya, Tomi, harus berdiri di antara Ani dan Beno (Tomi berada di tengah antara keduanya, tidak harus berdampingan, dan Ani boleh berada di kiri maupun di kanan Tomi). Banyak susunan barisan yang mungkin adalah ....

- **A. 13.440** ✅  
  <sub>Benar: urutan Ani-Tomi-Beno atau Beno-Tomi-Ani: $2 \times \frac{8!}{3!} = 13.440$</sub>
- B. 40.320  
  <sub>Salah: menghitung $8!$ tanpa syarat Tomi di tengah</sub>
- C. 20.160  
  <sub>Salah: mengira Tomi di antara kedua orang itu berpeluang setengah</sub>
- D. 6.720  
  <sub>Salah: hanya menghitung satu arah (Ani di kiri Beno)</sub>

**Pembahasan:** Tiga orang itu menempati tiga posisi dalam urutan tertentu. Jika ketiganya dianggap objek sama pada 8 posisi, ada $\frac{8!}{3!} = 6.720$ cara. Urutan Ani-Tomi-Beno dan Beno-Tomi-Ani: $2 \times 6.720 = 13.440$.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12-b03-b-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: tidak berdampingan dengan unsur sama*

Seluruh huruf pada kata MATEMATIKA disusun menjadi susunan berbeda sehingga tidak ada dua huruf vokal (A, E, I) yang berdampingan. Banyak susunan yang mungkin adalah ....

- A. 21.600  
  <sub>Salah: menganggap ketiga huruf A berbeda, $30 \times P(6,5) / 6 \times 6$ tanpa membagi $3!$</sub>
- B. 180  
  <sub>Salah: lupa menyusun vokal pada celah, hanya $30 \times 6$</sub>
- **C. 3.600** ✅  
  <sub>Benar: konsonan M, M, T, T, K: $\frac{5!}{2!\,2!} = 30$; vokal A, A, A, E, I pada 5 dari 6 celah: $\frac{P(6,5)}{3!} = 120$; total $30 \times 120 = 3.600$</sub>
- D. 600  
  <sub>Salah: memilih 5 dari 6 celah hanya satu cara (celah terpilih diabaikan), $30 \times \frac{5!}{3!}$</sub>

**Pembahasan:** Kata memuat 5 konsonan (M, M, T, T, K) dan 5 vokal (A, A, A, E, I). Konsonan: $\frac{5!}{2!\,2!} = 30$ susunan, membentuk 6 celah. Lima vokal menempati 5 celah berbeda: $P(6,5) = 720$ penempatan bila semua vokal berbeda; karena A kembar tiga, dibagi $3!$: $120$. Total $30 \times 120 = 3.600$.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12-b03-b-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: pemodelan jabatan dengan dua syarat*

Dari 9 orang akan dipilih ketua, wakil ketua, sekretaris, dan bendahara (setiap orang paling banyak satu jabatan). Andi hanya bersedia terpilih bila menjadi ketua, sedangkan Budi dan Cici tidak bersedia terpilih bersama-sama dalam pengurus yang sama (salah satu boleh terpilih). Banyak susunan pengurus yang mungkin adalah ....

- A. 2.016  
  <sub>Salah: mengabaikan syarat Budi dan Cici, $P(8,3) + P(8,4)$</sub>
- B. 1.980  
  <sub>Salah: menerapkan syarat Budi-Cici hanya saat Andi ketua, lupa pada kasus Andi tidak terpilih</sub>
- C. 1.320  
  <sub>Salah: hanya menghitung kasus Andi tidak terpilih</sub>
- **D. 1.620** ✅  
  <sub>Benar: Andi ketua: $P(8,3) - 6 \times 6 = 300$; Andi tidak terpilih: $P(8,4) - P(4,2) \times P(6,2) = 1.320$; total $1.620$</sub>

**Pembahasan:** Kasus 1 (Andi ketua): tiga jabatan lain dari 8 orang, $P(8,3) = 336$; yang memuat Budi dan Cici sekaligus $P(3,2) \times 6 = 36$; sah $300$. Kasus 2 (Andi tidak terpilih): empat jabatan dari 8 orang, $P(8,4) = 1.680$; yang memuat Budi dan Cici $P(4,2) \times P(6,2) = 360$; sah $1.320$. Total $300 + 1.320 = 1.620$.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12-b03-b-hard-bt01-013
*orisinal | C6 | 3 langkah | jenis: merancang komposisi huruf*

Sebuah kode terdiri atas 7 huruf yang seluruhnya dipakai. Agar banyak susunan huruf berbeda dari kode tersebut tepat 420, komposisi huruf yang benar adalah ....

- A. dua huruf masing-masing muncul 3 kali dan satu huruf lain muncul satu kali  
  <sub>Salah: $\frac{7!}{3!\,3!} = 140$, bukan 420</sub>
- B. satu huruf muncul 4 kali dan tiga huruf lainnya berbeda masing-masing satu kali  
  <sub>Salah: $\frac{7!}{4!} = 210$, bukan 420</sub>
- C. tiga huruf masing-masing muncul 2 kali dan satu huruf lain muncul satu kali  
  <sub>Salah: $\frac{7!}{2!\,2!\,2!} = 630$, bukan 420</sub>
- **D. satu huruf muncul 2 kali, satu huruf lain muncul 3 kali, dan dua huruf lainnya berbeda masing-masing satu kali** ✅  
  <sub>Benar: $\frac{7!}{2!\,3!} = 420$</sub>

**Pembahasan:** $\frac{7!}{2!\,3!} = \frac{5.040}{12} = 420$. Tiga komposisi lain menghasilkan 210, 630, dan 140.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12-b03-b-hard-bt01-014
*orisinal | C5 | 3 langkah | jenis: persamaan permutasi dengan parameter*

Banyak bilangan asli $n$ dengan $n \geq 2$ yang memenuhi $P(n,2) < 100$ adalah ....

- A. 8  
  <sub>Salah: mulai dari $n = 3$, mengira $n$ harus lebih dari 2</sub>
- B. 10  
  <sub>Salah: ikut menghitung $n = 1$ padahal $P(1,2)$ tidak terdefinisi</sub>
- **C. 9** ✅  
  <sub>Benar: $n(n-1) < 100$ dipenuhi $n = 2, 3, \ldots, 10$ ($10 \times 9 = 90$), sedangkan $n = 11$ memberi 110; ada 9 nilai</sub>
- D. 11  
  <sub>Salah: mengira $11 \times 10 = 90$ sehingga $n = 11$ ikut dihitung</sub>

**Pembahasan:** $P(n,2) = n(n-1)$. $10 \times 9 = 90 < 100$ dan $11 \times 10 = 110 > 100$. Karena $n \geq 2$, nilai $n$ adalah $2, 3, \ldots, 10$, yaitu 9 nilai.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12-b03-b-hard-bt01-015
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim dan contoh penyangkal*

Pernyataan yang benar tentang banyak susunan 8 orang yang duduk mengelilingi meja bundar dan banyak susunan 7 orang yang berdiri berjajar adalah ....

- **A. keduanya sama banyak, yaitu 5.040** ✅  
  <sub>Benar: melingkar 8 orang $(8-1)! = 5.040$ dan berjajar 7 orang $7! = 5.040$</sub>
- B. susunan melingkar 8 orang sama dengan susunan berjajar 8 orang, yaitu 40.320  
  <sub>Salah: memakai $8!$ untuk melingkar dan lupa $(8-1)!$</sub>
- C. susunan melingkar 8 orang adalah setengah dari susunan berjajar 8 orang, yaitu 20.160  
  <sub>Salah: membagi $8!$ dengan 2 padahal pembaginya 8</sub>
- D. susunan melingkar 8 orang adalah 720, lebih sedikit dari susunan berjajar 7 orang  
  <sub>Salah: memakai $(7-1)!$ seolah melingkar 7 orang</sub>

**Pembahasan:** Melingkar 8 orang: $(8-1)! = 7! = 5.040$. Berjajar 7 orang: $7! = 5.040$. Jadi keduanya sama; pernyataan lain keliru.
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12-b03-b-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: kata dengan huruf awal dan akhir sama*

Seluruh huruf pada kata PENDIDIKAN disusun menjadi susunan berbeda dengan huruf pertama dan huruf terakhir sama. Banyak susunan yang mungkin adalah ....

- A. 60.480  
  <sub>Salah: membagi hanya dengan $2!$, lupa pasangan huruf kembar kedua pada sisa huruf</sub>
- B. 120.960  
  <sub>Salah: menghitung $3 \times 8!$ tanpa membagi unsur sama pada 8 huruf sisa</sub>
- **C. 30.240** ✅  
  <sub>Benar: huruf yang dapat berada di kedua ujung hanya N, D, atau I; tiap kasus $\frac{8!}{2!\,2!} = 10.080$; total $3 \times 10.080 = 30.240$</sub>
- D. 10.080  
  <sub>Salah: hanya menghitung satu huruf (mis. N) di kedua ujung</sub>

**Pembahasan:** Huruf PENDIDIKAN: P, E, N (2), D (2), I (2), K, A. Huruf awal = akhir hanya mungkin untuk N, D, atau I. Misal N di kedua ujung: sisa P, E, D, D, I, I, K, A (8 huruf) dengan D dan I kembar: $\frac{8!}{2!\,2!} = 10.080$. Kasus D dan I juga 10.080. Total $30.240$.
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12-b03-b-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: bilangan dengan syarat posisi saling bergantung*

Dari angka 1, 2, 3, 4, 5, 6, dan 7 akan dibentuk bilangan empat angka tanpa angka berulang. Banyak bilangan genap yang angka ribuannya lebih kecil daripada angka ratusannya adalah ....

- A. 210  
  <sub>Salah: membagi $P(7,4)$ dengan 4 untuk dua syarat sekaligus</sub>
- B. 420  
  <sub>Salah: mengabaikan syarat genap, $\frac{P(7,4)}{2}$</sub>
- C. 360  
  <sub>Salah: mengabaikan syarat ribuan < ratusan, $3 \times P(6,3)$</sub>
- **D. 180** ✅  
  <sub>Benar: satuan 2, 4, atau 6 (3 cara); tiga angka depan dari 6 angka sisa $P(6,3) = 120$, separuhnya memenuhi ribuan < ratusan: $3 \times 60 = 180$</sub>

**Pembahasan:** Satuan harus genap: 3 pilihan. Tiga angka depan diambil dari 6 angka sisa dan disusun: $P(6,3) = 120$. Untuk setiap pilihan dua angka pada posisi ribuan dan ratusan, tepat satu dari dua urutan memenuhi ribuan < ratusan, sehingga separuh: 60. Total $3 \times 60 = 180$.
**Acuan:** siswa — siswa hal.119

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12-b03-b-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: tidak berdampingan dengan unsur sama*

Seluruh huruf pada kode AABBC disusun menjadi susunan berbeda sehingga tidak ada dua huruf yang sama yang berdampingan (kedua A tidak berdampingan dan kedua B tidak berdampingan). Banyak susunan yang mungkin adalah ....

- A. 30  
  <sub>Salah: menghitung semua susunan tanpa syarat</sub>
- B. 6  
  <sub>Salah: mengurangi dua kasus tanpa menambahkan kembali irisan yang terhitung dua kali, $30 - 12 - 12$</sub>
- C. 18  
  <sub>Salah: hanya mengurangi susunan saat A berdampingan, lupa syarat B</sub>
- **D. 12** ✅  
  <sub>Benar: semua $\frac{5!}{2!\,2!} = 30$; A berdampingan $\frac{4!}{2!} = 12$; B berdampingan 12; keduanya berdampingan $3! = 6$; $30 - 12 - 12 + 6 = 12$</sub>

**Pembahasan:** Semua: 30. Kedua A berdampingan (blok AA, B, B, C): $\frac{4!}{2!} = 12$. Kedua B berdampingan: 12. Kedua-duanya berdampingan (AA, BB, C): $3! = 6$. Tidak ada yang berdampingan: $30 - (12 + 12 - 6) = 12$.
**Acuan:** siswa — siswa hal.118

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12-b03-b-hard-bt01-019
*orisinal | C5 | 3 langkah | jenis: perbandingan nilai $P(n,r)$*

Banyak bilangan asli $r$ dengan $1 \leq r \leq 6$ yang memenuhi $P(6,r) > 300$ adalah ....

- A. 6  
  <sub>Salah: menganggap semua nilai $r$ memenuhi</sub>
- **B. 3** ✅  
  <sub>Benar: $P(6,r) = 6, 30, 120, 360, 720, 720$ untuk $r = 1, \ldots, 6$; yang lebih dari 300 adalah $r = 4, 5, 6$</sub>
- C. 2  
  <sub>Salah: mengira $P(6,6)$ lebih kecil dari $P(6,5)$ sehingga hanya $r = 4, 5$</sub>
- D. 4  
  <sub>Salah: ikut menghitung $r = 3$ dengan menganggap $P(6,3) = 180$</sub>

**Pembahasan:** $P(6,1) = 6$, $P(6,2) = 30$, $P(6,3) = 120$, $P(6,4) = 360$, $P(6,5) = 720$, $P(6,6) = 720$. Nilai yang lebih dari 300: $r = 4, 5, 6$, yaitu 3 nilai.
**Acuan:** siswa — siswa hal.110

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12-b03-b-hard-bt01-020
*orisinal | C5 | 4 langkah | jenis: berdampingan dengan syarat posisi*

Delapan orang berdiri berjajar dalam satu barisan. Dua di antaranya, Edo dan Fani, harus selalu berdampingan, sedangkan Gita tidak boleh berdiri di ujung kiri maupun ujung kanan barisan. Banyak susunan barisan yang mungkin adalah ....

- A. 2.880  
  <sub>Salah: hanya menghitung susunan saat Gita berada di salah satu ujung</sub>
- **B. 7.200** ✅  
  <sub>Benar: berdampingan: $7! \times 2 = 10.080$; Gita di salah satu ujung: $2 \times (6! \times 2) = 2.880$; $10.080 - 2.880 = 7.200$</sub>
- C. 10.080  
  <sub>Salah: hanya memenuhi syarat berdampingan, lupa syarat Gita</sub>
- D. 8.640  
  <sub>Salah: hanya mengurangi satu ujung ($10.080 - 1.440$), lupa ujung yang lain</sub>

**Pembahasan:** Edo-Fani dijadikan blok: 7 objek, $7! = 5.040$, dikali $2!$ = 10.080. Gita di ujung kiri: 6 objek lain disusun $6! = 720$, dikali $2!$ = 1.440; ujung kanan juga 1.440, total 2.880. Yang memenuhi: $10.080 - 2.880 = 7.200$.
**Acuan:** siswa — siswa hal.119

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
