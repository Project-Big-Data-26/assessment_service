# Ringkasan untuk PPT — sistem silver AI

Dua belas slide menjelaskan alur silver AI dari JSON, validasi, model, siswa dan CTT/IRT sampai feedback sistem. Tidak ada persetujuan pelabel manusia dalam alur operasional.

## 1. Mengapa alur ini diperlukan?

Kita menghubungkan isi soal, perkiraan AI dan bukti siswa tanpa kehilangan asal setiap keputusan.

- JSON menyimpan soal beserta sumber, kunci dan medianya.
- LLM dan IndoBERT membantu memberi usulan label isi soal.
- Jawaban siswa dianalisis dengan CTT/IRT untuk pemeriksaan berikutnya.

**Alasan:** Perkiraan dari isi soal dan hasil pengerjaan siswa dapat berbeda. Memisahkan bukti tersebut membantu menjelaskan penyebabnya.

**Catatan pembicara:** Ceritakan alur sebagai siklus belajar sistem. Sebelum siswa mengerjakan, kita hanya mempunyai isi soal dan perkiraan tuntutannya. Setelah respons terkumpul, kita dapat melihat bagaimana soal bekerja pada kelompok siswa tertentu. Kedua informasi itu saling melengkapi. Penjelasan ini juga menjaga kita agar tidak menyamakan label AI, label AI dan parameter IRT.

## 2. Siapkan JSON yang dapat dipercaya

Soal masuk sebagai konten yang lengkap, memiliki versi dan dapat ditelusuri ke sumbernya.

- Periksa teks soal, pilihan jawaban, kunci, solusi dan gambar.
- Simpan kelas siswa, sumber, nomor versi dan sidik isi.
- Soal bermasalah diperiksa lagi sebelum menjadi bahan penilaian.

**Alasan:** Model dan penilaian jawaban dapat menghasilkan keluaran yang salah bila isi soal bermasalah. Pemeriksaan sumber mengatasi masalah sejak awal.

**Catatan pembicara:** JSON adalah wadah data, bukan tanda bahwa soal sudah valid. Stem berarti teks pertanyaan; opsi adalah pilihan jawaban; key adalah jawaban yang diverifikasi. Gambar yang diperlukan harus tersedia dan membutuhkan transkripsi terverifikasi untuk model teks. Hash menjadi sidik konten; versi menjelaskan revisi. Jika source JSON, prompt atau byte gambar berubah, penilaian lama yang tidak cocok harus dinilai ulang. Export soal_pretest_db.json tetap candidate bank dan bukan delivery siswa.

## 3. LLM membantu memberi label awal

Gemini memakai pedoman penilaian untuk membuat usulan label sebelum prediksi IndoBERT dibandingkan.

- Soal, kelas dan pedoman penilaian membantu LLM membuat label awal.
- Tiga penilaian tidak melihat prediksi model atau suara penilaian lain.
- Tiga suara sama diterima jika lolos pemeriksaan; kasus lain dinilai kembali.
- Simpan solusi singkat dan bukti; label AI belum menjadi label AI.

**Alasan:** Model memerlukan contoh berlabel untuk belajar. LLM membantu menyiapkan usulan awal, sementara penilaian tanpa melihat prediksi mengurangi pengaruh keputusan model sebelumnya.

**Catatan pembicara:** LLM dibutuhkan untuk menafsirkan langkah penyelesaian dan tuntutan konsep sebelum respons siswa tersedia. Tiga panggilan membantu memperlihatkan konsistensi, tetapi tetap berasal dari satu model Gemini; kesalahan bersama masih mungkin. Karena itu 3/3 bukan confidence terkalibrasi atau silver AI. Silver 2–1, abstain, key conflict atau concern memerlukan adjudikasi terpisah. Hidden chain-of-thought tidak diminta/disimpan; yang ditampilkan adalah solusi minimum, evidence spans, alasan singkat dan difficulty evidence profile.

## 4. IndoBERT mempelajari pola dalam konteks soal

Soal diubah menjadi teks yang susunannya tetap, lalu model membaca konteks dan memberi tiga jenis label.

- Susunan teks mengikuti pilihan input pada versi model.
- Teks dibagi menjadi unit input agar dapat dibaca model.
- Pola dalam konteks soal dipakai untuk tiga jenis label.
- Kata kerja hanya petunjuk; satu kata tidak langsung menetapkan label.

**Alasan:** Kesulitan dan proses berpikir ditentukan oleh keseluruhan tuntutan soal, bukan satu kata kerja.

**Catatan pembicara:** Tokenizer membagi teks menjadi unit yang dikenal model, kemudian encoder membaca hubungan antarbagiannya. [CLS] adalah representasi yang dipakai head klasifikasi. Model mempelajari hubungan dengan label dari banyak contoh training. Representation dapat stem_options, metadata, solution atau kko dan dikunci dalam manifest agar training/inference konsisten. KKO adalah kata kerja operasional yang dideteksi secara leksikal; presence kata hitung tidak otomatis berarti domain atau difficulty tertentu. LoRA menyesuaikan encoder melalui matriks tambahan kecil pada query/value.

## 5. Mengapa ada tiga jenis label?

Proses berpikir, jenis pengetahuan dan tingkat kesulitan menjelaskan tiga sisi berbeda dari soal.

- Proses berpikir: mengingat, menerapkan, atau menalar.
- Pengetahuan: fakta, konsep, prosedur, atau refleksi strategi.
- Kesulitan: mudah, sedang, sulit relatif terhadap kelas siswa.
- Pada pelatihan baru, model mempertimbangkan kelas dan urutan kesulitan.

**Alasan:** Soal prosedural dapat mudah atau sulit. Satu kategori tidak cukup menjelaskan seluruh karakter soal.

**Catatan pembicara:** Head berarti bagian model yang menghasilkan satu jenis label. Kognitif menggambarkan proses berpikir, knowledge menggambarkan jenis pengetahuan, intended difficulty memperkirakan tantangan untuk kelas sasaran. Grade embedding menyediakan representasi kelas agar difficulty head dapat mempertimbangkan tingkat pembelajaran. Default training baru grade-aware-ordinal-v2 menggunakan dua batas terurut. Artifact lama dapat parallel-v1, sehingga arsitektur yang benar dibaca dari manifest. Runtime kini menerima prediksi in-scope untuk grade 1–6; grade 7–12 menghasilkan abstain/out_of_scope.

## 6. Seberapa yakin dan seberapa tersebar?

Confidence melihat peluang terbesar; entropy melihat sebaran seluruh peluang.

- Confidence = peluang label dengan nilai tertinggi.
- Entropy rendah berarti peluang terkonsentrasi; tinggi berarti tersebar.
- Peluang disesuaikan menggunakan data pemeriksaan yang terpisah.
- Batas keyakinan mengatur pemeriksaan; syarat isi atau kelas gagal berarti tidak memberi label.

**Alasan:** Label dengan peluang terbesar saja belum menunjukkan keraguan model. Confidence dan entropy membantu menandai usulan yang perlu diperiksa.

**Catatan pembicara:** Contoh p=[0.80,0.15,0.05] memberi confidence 0.80 dan normalized entropy sekitar 0.558. Dua keluaran ini dihitung setelah probabilitas dikalibrasi; keduanya bukan fitur awal. Temperature menyesuaikan tajamnya distribusi dan dipilih menggunakan validation, bukan test atau skor IRT. Policy confidence-entropy-v1 membutuhkan dua batas yang tersimpan pada manifest; confidence-only-v1 hanya menggunakan confidence untuk gate. Tinggi confidence tidak membuktikan label benar. Input mencapai truncation limit juga menghasilkan review.

## 7. Silver qualified dikerjakan siswa

Snapshot silver langsung terhubung ke delivery setelah pemeriksaan konten dan provenance.

- Registrasi snapshot silver lalu buat assessment dengan grade/track yang cocok.
- Server membuat mapping opsi opaque dan menjaga key/solution privat.
- Jawaban dinilai server; skip tetap null dan retry tetap idempotent.

**Alasan:** Data respons harus terikat pada soal dan kunci versi yang tepat.

**Catatan pembicara:** Delivery tidak menunggu pelabel manusia. Snapshot memakai ai_silver dengan tiga run sukses, kunci/solusi/visual qualified dan checksum. Pilot teks mendukung grade 1–12 serta TL 11–12, tanpa memperluas scope IndoBERT SD.

## 8. Catat segera, hitung pada waktu tertentu

Kita tidak perlu menunggu seluruh siswa masa depan; analisis memakai jawaban yang memenuhi syarat pada batas waktu yang jelas.

- Jawaban disimpan segera; operator memulai analisis pada kumpulan jawaban.
- Pilih satu sesi selesai per siswa dalam rentang waktu analisis.
- Jumlah siswa dihitung dari sampel yang lolos, bukan jumlah akun atau pengiriman.
- Data baru menghasilkan hasil baru; data dan aturan sama memakai hasil tersimpan.

**Alasan:** Siswa terus menambah jawaban. Menyimpan hasil beserta data dan waktunya membuat perhitungan dapat diulang dengan jelas.

**Catatan pembicara:** N_selected adalah unique subjects dengan completed session terpilih. First/last memilih whole session berdasarkan started_at,id setelah filter completed_at [from,to). Event invalid, rapid guesses atau mismatch dikeluarkan; missing tetap NA. N_fit mengecualikan orang dengan observed rate di bawah 70%. Minimum default Rasch=100 orang/5 item, 2PL=300/10, 3PL=1000/20. Masing-masing item juga membutuhkan 50 observed dan minimal 5 benar serta 5 salah; coverage, connected design dan assumption review tetap diperiksa. Belum ada scheduler atau calibration per jawaban otomatis.

## 9. CTT dan IRT menjawab apa?

CTT merangkum jawaban yang terlihat; IRT memodelkan hubungan kemampuan siswa dan karakter soal.

- CTT merangkum jumlah benar, mutu pilihan jawaban dan konsistensi tes.
- IRT menghitung kesulitan, daya pembeda dan peluang dasar sesuai model.
- CTT tetap dihitung ketika syarat data atau asumsi IRT belum terpenuhi.
- Hasil nyata melengkapi perkiraan awal; AI memutuskan perubahan.

**Alasan:** Proporsi benar memberi gambaran cepat. IRT menjelaskan hubungan siswa dengan soal ketika data dan asumsi mendukung.

**Catatan pembicara:** p tinggi berarti item dijawab benar oleh banyak siswa dalam sampel tersebut. b menyatakan posisi difficulty pada skala kemampuan lokal, sehingga p dan b bukan angka yang dibandingkan langsung. CTT corrected item-total/discrimination dan KR-20 menggunakan complete cases untuk score joins; variance item dan total KR-20 sama-sama ddof=1. IRT membutuhkan asumsi unidimensional, local independence dan representative sample. Perbedaan intended/empirical menjadi flag review, bukan perubahan label otomatis. Calibration berbeda populasi, grade, form atau versi belum comparable tanpa linking.

## 10. Bagaimana IRT benar-benar dihitung?

Pola benar-salah dipakai untuk mencari karakter soal, lalu kemampuan siswa diperkirakan bersama ketidakpastiannya.

- Rasch mencari kesulitan; 2PL menambah daya pembeda; 3PL menambah peluang dasar.
- 41 titik bantu mewakili kemungkinan kemampuan ketika perhitungan dilakukan.
- Asumsi awal menahan nilai ekstrem; algoritme mencari parameter yang cocok.
- Hasil memuat kemampuan, ketidakpastian dan pemeriksaan kecocokan model.

**Alasan:** Kemampuan tidak terlihat langsung. Perhitungan mempertimbangkan beberapa kemungkinan dan melaporkan ketidakpastian perkiraannya.

**Catatan pembicara:** Regularized marginal likelihood mempertimbangkan berbagai kemungkinan kemampuan sebelum mengoptimasi item. Gauss-Hermite memakai 41 titik bantu default untuk mendekati integral terhadap N(0,1); jumlah itu adalah konfigurasi numerik. L-BFGS-B mencari parameter dalam bounds. Prior b~N(0,3²), log a~N(0,0.75²), c~Beta(5,17) membantu nilai extreme tetap finite. c bukan 1/jumlah opsi. EAP adalah rata-rata posterior kemampuan; posterior SD menyatakan ketidakpastiannya. Warnings convergence/boundary/local dependence tetap memerlukan review. Ini batch calibration lokal research/advisory, bukan CAT/release otomatis.

## 11. Feedback otomatis dan validasi ulang AI

Bukti siswa memicu tindakan sistem tanpa menimpa label awal.

- Sampel lemah meminta tambahan respons.
- Kandidat masalah kualitas ditahan untuk AI review.
- Konten berubah menghasilkan versi baru, blind validation baru dan snapshot silver baru.

**Alasan:** Kesulitan empiris dan label isi soal memiliki dasar yang berbeda.

**Catatan pembicara:** Screen menyimpan keputusan sistem secara otomatis. GET decisions memberi audit; POST keputusan manual sudah dihapus. IRT tidak menimpa domain, knowledge atau intended difficulty dan tidak memicu retraining otomatis.

## 12. Apa yang tersedia dan apa berikutnya?

Bagian utama tersedia untuk penelitian dan uji coba, sementara beberapa kemampuan masih perlu dibangun.

- Delivery silver dan feedback otomatis tersedia; data serta kredensial tetap diperlukan.
- IRT batch menunggu data/bukti asumsi dan tidak dikalibrasi setiap jawaban.
- CAT, mastery topik, equating dan pembaruan model online masih rancangan.

**Alasan:** Menjelaskan batas implementasi membantu pembaca memahami hasil sekarang dan merencanakan pengembangan berikutnya.

**Catatan pembicara:** Gate konten, split, model dan IRT tetap berlaku. Persetujuan pelabel manusia dihapus. Operator mengelola pekerjaan sistem dan service integration; label berasal dari AI. Migrasi tidak menciptakan respons siswa atau melatih model baru.

## Glosarium

| Istilah | Arti |
|---|---|
| Silver | Usulan label dari AI untuk penelitian. |
| Silver AI | Label awal dari blind N=3/adjudikasi AI yang memenuhi qualification. |
| Blind review | Penilaian awal tidak melihat prediksi atau keputusan lain. |
| Evidence / solusi minimum | Bukti singkat dan langkah minimum untuk memverifikasi jawaban. |
| Content hash / version | Sidik dan nomor revisi konten. |
| Serializer / tokenizer | Penyusun teks tetap dan pengubah teks menjadi unit input model. |
| Encoder / head | Pembaca konteks dan penghasil satu jenis label. |
| KKO | Kata kerja operasional yang dideteksi secara leksikal. |
| LoRA | Adapter rank kecil untuk penyesuaian model. |
| Ordinal / grade embedding | Urutan kategori difficulty dan vektor kelas sasaran. |
| Confidence | Peluang tertinggi setelah calibration. |
| Entropy | Ukuran sebaran peluang di semua kategori. |
| Temperature | Parameter calibration yang dipilih dari validation. |
| CTT / Wilson interval | Ringkasan skor sampel dan rentang ketidakpastian proporsi benar. |
| IRT / a,b,c | Model peluang respons dengan slope, difficulty dan lower asymptote. |
| Theta / EAP / posterior SD | Kemampuan laten, rata-rata posterior dan ketidakpastiannya. |
| Gauss-Hermite 41 | Titik/bobot numerik default untuk mendekati integral kemampuan. |
| Prior / regularization | Asumsi tambahan yang menahan estimasi ekstrem. |
| NA / missing | Respons tidak observed atau explicit skip. |
| N_selected / N_fit | Subject unik sesi terpilih dan orang yang lolos batas missing. |
| Snapshot / lineage | Versi data/hasil yang tetap dan rantai asal perubahannya. |
| Hold / challenger | Penahanan versi item dan calon model pengganti. |
| Gate / calibration release | Syarat penggunaan artifact atau calibration untuk tujuan tertentu. |
| CAT / linking | Tes adaptif dan penghubungan skala calibration. |

Rumus dan contoh interaktif tersedia pada [33 animasi](33_ANIMATED_DATA_FLOW.html). [Integrasi API](36_SILVER_OPERATIONAL_INTEGRATION.md).
