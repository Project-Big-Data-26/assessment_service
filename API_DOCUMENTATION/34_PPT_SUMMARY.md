# Ringkasan alur sistem untuk PPT

[Buka animasi](33_ANIMATED_DATA_FLOW.html), lalu pilih tab **Ringkasan untuk PPT**. Materi berikut terdiri dari 12 slide yang siap disalin. Gunakan pesan dan 3-4 poin sebagai isi slide; bagian Mengapa, Catatan pembicara dan Istilah membantu menjelaskan saat presentasi. Rumus dapat dipilih sesuai kedalaman audiens. Angka/contoh merupakan ilustrasi, bukan hasil siswa nyata.

Mulai dari pertanyaan sederhana: bagaimana soal yang baru diekstrak menjadi soal yang dinilai, digunakan siswa, lalu diperbaiki berdasarkan bukti? Dua belas slide ini menceritakan alurnya, menjelaskan alasan setiap pilihan, dan membedakan fungsi yang tersedia dari rancangan berikutnya.

## Slide 1. Mengapa alur ini diperlukan?

**Pesan utama:** Kita menghubungkan isi soal, perkiraan AI dan bukti siswa tanpa kehilangan asal setiap keputusan.

- JSON menyimpan soal beserta sumber, kunci dan medianya.
- LLM dan IndoBERT membantu memberi usulan label isi soal.
- Jawaban siswa dianalisis dengan CTT/IRT untuk pemeriksaan berikutnya.

**Mengapa tahap ini diperlukan:** Perkiraan dari isi soal dan hasil pengerjaan siswa dapat berbeda. Memisahkan bukti tersebut membantu menjelaskan penyebabnya.

**Catatan pembicara:** Ceritakan alur sebagai siklus belajar sistem. Sebelum siswa mengerjakan, kita hanya mempunyai isi soal dan perkiraan tuntutannya. Setelah respons terkumpul, kita dapat melihat bagaimana soal bekerja pada kelompok siswa tertentu. Kedua informasi itu saling melengkapi. Penjelasan ini juga menjaga kita agar tidak menyamakan label AI, label ahli dan parameter IRT.

**Istilah untuk dijelaskan:** **Label** - Kategori yang diberikan untuk menjelaskan isi atau tuntutan soal. Alasan: Membantu menyusun dan mencari soal berdasarkan kebutuhan pembelajaran. **Bukti empiris** - Informasi yang dihitung dari respons siswa yang valid. Alasan: Memeriksa apakah soal berfungsi sesuai tujuan ketika benar-benar dikerjakan.

## Slide 2. Siapkan JSON yang dapat dipercaya

**Pesan utama:** Soal masuk sebagai konten yang lengkap, memiliki versi dan dapat ditelusuri ke sumbernya.

- Periksa teks soal, pilihan jawaban, kunci, solusi dan gambar.
- Simpan kelas siswa, sumber, nomor versi dan sidik isi.
- Soal bermasalah diperiksa lagi sebelum menjadi bahan penilaian.

**Mengapa tahap ini diperlukan:** Model dan penilaian jawaban dapat menghasilkan keluaran yang salah bila isi soal bermasalah. Pemeriksaan sumber mengatasi masalah sejak awal.

**Catatan pembicara:** JSON adalah wadah data, bukan tanda bahwa soal sudah valid. Stem berarti teks pertanyaan; opsi adalah pilihan jawaban; key adalah jawaban yang diverifikasi. Gambar yang diperlukan harus tersedia dan membutuhkan transkripsi terverifikasi untuk model teks. Hash menjadi sidik konten; versi menjelaskan revisi. Jika source JSON, prompt atau byte gambar berubah, penilaian lama yang tidak cocok harus dinilai ulang. Export soal_pretest_db.json tetap candidate bank dan bukan delivery siswa.

**Istilah untuk dijelaskan:** **Stem** - Teks utama pertanyaan yang harus dijawab siswa. Alasan: Menjadi bagian penting input model dan tampilan siswa. **Hash / versi** - Sidik isi dan nomor revisi soal. Alasan: Mengikat label serta respons ke konten yang tepat. **Provenance** - Catatan asal dan proses yang menghasilkan data. Alasan: Membantu menelusuri atau mengulang pemeriksaan.

**Rumus opsional - Identitas isi:**

$$
H=\operatorname{SHA256}(\operatorname{canonicalJSON}(\mathrm{content}))
$$

Simbol: $H$ = Hash konten yang disusun secara deterministik.

Mengapa rumus ini digunakan: Isi yang berubah menghasilkan sidik berbeda sehingga penilaian lama tidak dipakai diam-diam.

## Slide 3. LLM membantu memberi label awal

**Pesan utama:** Gemini memakai pedoman penilaian untuk membuat usulan label sebelum prediksi IndoBERT dibandingkan.

- Soal, kelas dan pedoman penilaian membantu LLM membuat label awal.
- Tiga penilaian tidak melihat prediksi model atau suara penilaian lain.
- Tiga suara sama diterima jika lolos pemeriksaan; kasus lain dinilai kembali.
- Simpan solusi singkat dan bukti; label AI belum menjadi label ahli.

**Mengapa tahap ini diperlukan:** Model memerlukan contoh berlabel untuk belajar. LLM membantu menyiapkan usulan awal, sementara penilaian tanpa melihat prediksi mengurangi pengaruh keputusan model sebelumnya.

**Catatan pembicara:** LLM dibutuhkan untuk menafsirkan langkah penyelesaian dan tuntutan konsep sebelum respons siswa tersedia. Tiga panggilan membantu memperlihatkan konsistensi, tetapi tetap berasal dari satu model Gemini; kesalahan bersama masih mungkin. Karena itu 3/3 bukan confidence terkalibrasi atau gold manusia. Silver 2–1, abstain, key conflict atau concern memerlukan adjudikasi terpisah. Hidden chain-of-thought tidak diminta/disimpan; yang ditampilkan adalah solusi minimum, evidence spans, alasan singkat dan difficulty evidence profile.

**Istilah untuk dijelaskan:** **Blind** - Penilaian awal tidak melihat prediksi IndoBERT, vote lain atau estimasi difficulty agen. Alasan: Mengurangi anchoring pada jawaban yang sudah ada. **Silver label** - Usulan label penelitian yang dibuat AI. Alasan: Menyediakan data awal dengan provenance yang tetap jelas. **Adjudikasi AI** - Penilaian terpisah untuk kasus yang belum dapat diterima langsung. Alasan: Menyelesaikan ketidakcocokan tanpa menyamarkannya sebagai vote bulat.

## Slide 4. IndoBERT mempelajari pola dalam konteks soal

**Pesan utama:** Soal diubah menjadi teks yang susunannya tetap, lalu model membaca konteks dan memberi tiga jenis label.

- Susunan teks mengikuti pilihan input pada versi model.
- Teks dibagi menjadi unit input agar dapat dibaca model.
- Pola dalam konteks soal dipakai untuk tiga jenis label.
- Kata kerja hanya petunjuk; satu kata tidak langsung menetapkan label.

**Mengapa tahap ini diperlukan:** Kesulitan dan proses berpikir ditentukan oleh keseluruhan tuntutan soal, bukan satu kata kerja.

**Catatan pembicara:** Tokenizer membagi teks menjadi unit yang dikenal model, kemudian encoder membaca hubungan antarbagiannya. [CLS] adalah representasi yang dipakai head klasifikasi. Model mempelajari hubungan dengan label dari banyak contoh training. Representation dapat stem_options, metadata, solution atau kko dan dikunci dalam manifest agar training/inference konsisten. KKO adalah kata kerja operasional yang dideteksi secara leksikal; presence kata hitung tidak otomatis berarti domain atau difficulty tertentu. LoRA menyesuaikan encoder melalui matriks tambahan kecil pada query/value.

**Istilah untuk dijelaskan:** **Encoder / [CLS]** - Pembaca konteks teks dan representasi yang dipakai untuk klasifikasi. Alasan: Memungkinkan model menggunakan hubungan antara soal, opsi dan metadata. **KKO** - Kata kerja operasional yang dideteksi sebagai fitur opsional. Alasan: Memberi petunjuk leksikal tanpa menggantikan penilaian tuntutan soal. **LoRA** - Adapter dengan matriks rank kecil yang dilatih saat fine-tuning. Alasan: Mengurangi jumlah parameter yang perlu disesuaikan.

**Rumus opsional - Penyesuaian bobot LoRA:**

$$
W'=W+\frac{\alpha}{r}BA
$$

Simbol: $W$ = Bobot dasar yang dibekukan pada jalur LoRA. $A,B$ = Matriks adapter yang dipelajari. $r$ = Rank adapter. $\alpha$ = Faktor skala adapter.

Mengapa rumus ini digunakan: Perubahan dipelajari melalui adapter kecil; head klasifikasi juga dilatih.

## Slide 5. Mengapa ada tiga jenis label?

**Pesan utama:** Proses berpikir, jenis pengetahuan dan tingkat kesulitan menjelaskan tiga sisi berbeda dari soal.

- Proses berpikir: mengingat, menerapkan, atau menalar.
- Pengetahuan: fakta, konsep, prosedur, atau refleksi strategi.
- Kesulitan: mudah, sedang, sulit relatif terhadap kelas siswa.
- Pada pelatihan baru, model mempertimbangkan kelas dan urutan kesulitan.

**Mengapa tahap ini diperlukan:** Soal prosedural dapat mudah atau sulit. Satu kategori tidak cukup menjelaskan seluruh karakter soal.

**Catatan pembicara:** Head berarti bagian model yang menghasilkan satu jenis label. Kognitif menggambarkan proses berpikir, knowledge menggambarkan jenis pengetahuan, intended difficulty memperkirakan tantangan untuk kelas sasaran. Grade embedding menyediakan representasi kelas agar difficulty head dapat mempertimbangkan tingkat pembelajaran. Default training baru grade-aware-ordinal-v2 menggunakan dua batas terurut. Artifact lama dapat parallel-v1, sehingga arsitektur yang benar dibaca dari manifest. Runtime kini menerima prediksi in-scope untuk grade 1–6; grade 7–12 menghasilkan abstain/out_of_scope.

**Istilah untuk dijelaskan:** **Head** - Bagian model yang memetakan representasi encoder menjadi label tertentu. Alasan: Memungkinkan satu encoder mendukung tiga tugas yang berbeda. **Ordinal** - Kategori dengan urutan, seperti Easy < Medium < Hard. Alasan: Memakai struktur urutan saat difficulty dipelajari. **Grade embedding** - Vektor yang merepresentasikan kelas siswa pada difficulty head. Alasan: Kesulitan soal perlu dipertimbangkan relatif terhadap kelas sasaran.

**Rumus opsional - Peluang pada urutan kesulitan:**

$$
\begin{aligned}q_k&=\sigma(s-\tau_k),\quad \tau_1>\tau_0\\p_E&=1-q_0\\p_M&=q_0-q_1\\p_H&=q_1\end{aligned}
$$

Simbol: $s$ = Skor dari representasi encoder dan grade embedding. $\tau_0,\tau_1$ = Cutpoints terurut yang dipelajari. $\sigma$ = Sigmoid. $p_E,p_M,p_H$ = Peluang Easy, Medium dan Hard sebelum calibration.

Mengapa rumus ini digunakan: Dua batas menjaga hubungan urut tiga kategori difficulty.

## Slide 6. Seberapa yakin dan seberapa tersebar?

**Pesan utama:** Confidence melihat peluang terbesar; entropy melihat sebaran seluruh peluang.

- Confidence = peluang label dengan nilai tertinggi.
- Entropy rendah berarti peluang terkonsentrasi; tinggi berarti tersebar.
- Peluang disesuaikan menggunakan data pemeriksaan yang terpisah.
- Batas keyakinan mengatur pemeriksaan; syarat isi atau kelas gagal berarti tidak memberi label.

**Mengapa tahap ini diperlukan:** Label dengan peluang terbesar saja belum menunjukkan keraguan model. Confidence dan entropy membantu menandai usulan yang perlu diperiksa.

**Catatan pembicara:** Contoh p=[0.80,0.15,0.05] memberi confidence 0.80 dan normalized entropy sekitar 0.558. Dua keluaran ini dihitung setelah probabilitas dikalibrasi; keduanya bukan fitur awal. Temperature menyesuaikan tajamnya distribusi dan dipilih menggunakan validation, bukan test atau skor IRT. Policy confidence-entropy-v1 membutuhkan dua batas yang tersimpan pada manifest; confidence-only-v1 hanya menggunakan confidence untuk gate. Tinggi confidence tidak membuktikan label benar. Input mencapai truncation limit juga menghasilkan review.

**Istilah untuk dijelaskan:** **Confidence** - Nilai peluang tertinggi setelah calibration. Alasan: Menunjukkan kekuatan usulan label utama. **Normalized entropy** - Ringkasan sebaran peluang dengan rentang 0–1. Alasan: Menunjukkan apakah model membagi peluang ke banyak label. **Temperature** - Parameter calibration yang mengubah ketajaman distribusi. Alasan: Membantu probabilitas sesuai dengan ketepatan pada validation.

**Rumus opsional - Penyesuaian peluang dan ringkasan keyakinan:**

$$
\begin{aligned}p_k&=\frac{\exp(z_k/T)}{\sum_{\ell=1}^{K}\exp(z_\ell/T)}\\C&=\max_k p_k\\H_{\mathrm{norm}}&=-\frac{\sum_{k=1}^{K}p_k\ln p_k}{\ln K}\end{aligned}
$$

Simbol: $z_k$ = Logit head multiclass; log raw probability untuk head ordinal. $T$ = Temperature dari validation. $K$ = Jumlah kategori pada head: 3 atau 4. $C$ = Calibrated confidence. $H_{\mathrm{norm}}$ = Normalized entropy.

Mengapa rumus ini digunakan: Calibration diterapkan dulu, kemudian dua ringkasan digunakan sesuai policy artifact.

## Slide 7. Soal disahkan, lalu dikerjakan siswa

**Pesan utama:** Uji coba mengirim soal yang disahkan ahli dan menilai jawaban menggunakan kunci di server.

- Soal memakai label ahli, kunci/solusi terverifikasi dan izin untuk digunakan.
- Urutan pilihan diacak, lalu tetap sama saat siswa memuat ulang.
- Server mencatat benar=1, salah=0, dilewati=belum ada skor.
- Kepemilikan sesi dan pencegahan data ganda menjaga respons peserta.

**Mengapa tahap ini diperlukan:** Analisis hasil siswa memerlukan soal yang tepat, penilaian konsisten dan jawaban yang tidak terhitung dua kali.

**Catatan pembicara:** Gold berasal dari workflow tiga ahli manusia, bukan tiga panggilan Gemini. Untuk gold, vote lengkap 3–0 atau 2–1 dapat settled jika gate konten/key/solution lolos. Pilot sekarang fixed-form dan text-only; gambar esensial memerlukan transkripsi terverifikasi. Siswa tidak menerima kunci, solusi atau reasoning LLM. Receipt respons juga tidak menampilkan correctness saat pilot. Server memetakan public option ID ke opsi privat dan menghitung skor. Explicit skip tetap null; sesi complete memerlukan seluruh item answered atau skipped.

**Istilah untuk dijelaskan:** **Human gold** - Label dan konten rujukan yang disahkan melalui workflow ahli. Alasan: Menjadi sumber yang diizinkan untuk pilot sekarang. **Server scoring** - Penilaian jawaban menggunakan kunci versi di server. Alasan: Menjaga jawaban dan nilai terikat pada item yang benar. **NA / idempotency** - Missing score dan aturan agar pengiriman ulang tidak membuat data ganda. Alasan: Menghindari skip menjadi salah serta siswa terhitung berulang.

**Rumus opsional - Skor matriks respons:**

$$
x_{ij}=\begin{cases}1&\text{jawaban benar}\\0&\text{jawaban salah}\\\mathrm{NA}&\text{skip atau missing}\end{cases}
$$

Simbol: $i$ = Siswa/subject yang dipilih untuk analisis. $j$ = Versi item yang dianalisis.

Mengapa rumus ini digunakan: Missing menyatakan ketiadaan evidence; tidak dianggap jawaban salah.

## Slide 8. Catat segera, hitung pada waktu tertentu

**Pesan utama:** Kita tidak perlu menunggu seluruh siswa masa depan; analisis memakai jawaban yang memenuhi syarat pada batas waktu yang jelas.

- Jawaban disimpan segera; operator memulai analisis pada kumpulan jawaban.
- Pilih satu sesi selesai per siswa dalam rentang waktu analisis.
- Jumlah siswa dihitung dari sampel yang lolos, bukan jumlah akun atau pengiriman.
- Data baru menghasilkan hasil baru; data dan aturan sama memakai hasil tersimpan.

**Mengapa tahap ini diperlukan:** Siswa terus menambah jawaban. Menyimpan hasil beserta data dan waktunya membuat perhitungan dapat diulang dengan jelas.

**Catatan pembicara:** N_selected adalah unique subjects dengan completed session terpilih. First/last memilih whole session berdasarkan started_at,id setelah filter completed_at [from,to). Event invalid, rapid guesses atau mismatch dikeluarkan; missing tetap NA. N_fit mengecualikan orang dengan observed rate di bawah 70%. Minimum default Rasch=100 orang/5 item, 2PL=300/10, 3PL=1000/20. Masing-masing item juga membutuhkan 50 observed dan minimal 5 benar serta 5 salah; coverage, connected design dan assumption review tetap diperiksa. Belum ada scheduler atau calibration per jawaban otomatis.

**Istilah untuk dijelaskan:** **Snapshot** - Hasil analisis dari data/window/policy tertentu yang disimpan tetap. Alasan: Memisahkan evidence lama dari jawaban yang datang setelah cutoff. **N_selected / N_fit** - Jumlah subject sesi terpilih dan jumlah yang lolos batas missing untuk fit. Alasan: Menggunakan sampel eligible daripada semua peserta terdaftar. **Cutoff window** - Rentang completion time yang menentukan cohort analisis. Alasan: Memberi batas yang jelas ketika siswa terus masuk.

**Rumus opsional - Jumlah orang yang dapat di-fit:**

$$
N_{\mathrm{fit}}=\sum_{i=1}^{N_{\mathrm{selected}}}\mathbf{1}\!\left(\frac{\sum_{j=1}^{J}m_{ij}}{J}\ge0.70\right) 
$$

Simbol: $m_{ij}$ = 1 jika respons item observed valid, 0 jika missing/skip. $J$ = Jumlah versi item. $N_{\mathrm{selected}}$ = Jumlah subject unik yang dipilih setelah whole-session selection.

Mengapa rumus ini digunakan: Fit tidak bergantung pada total siswa yang akan datang; gate memakai evidence yang sudah tersedia.

## Slide 9. CTT dan IRT menjawab apa?

**Pesan utama:** CTT merangkum jawaban yang terlihat; IRT memodelkan hubungan kemampuan siswa dan karakter soal.

- CTT merangkum jumlah benar, mutu pilihan jawaban dan konsistensi tes.
- IRT menghitung kesulitan, daya pembeda dan peluang dasar sesuai model.
- CTT tetap dihitung ketika syarat data atau asumsi IRT belum terpenuhi.
- Hasil nyata melengkapi perkiraan awal; ahli memutuskan perubahan.

**Mengapa tahap ini diperlukan:** Proporsi benar memberi gambaran cepat. IRT menjelaskan hubungan siswa dengan soal ketika data dan asumsi mendukung.

**Catatan pembicara:** p tinggi berarti item dijawab benar oleh banyak siswa dalam sampel tersebut. b menyatakan posisi difficulty pada skala kemampuan lokal, sehingga p dan b bukan angka yang dibandingkan langsung. CTT corrected item-total/discrimination dan KR-20 menggunakan complete cases untuk score joins; variance item dan total KR-20 sama-sama ddof=1. IRT membutuhkan asumsi unidimensional, local independence dan representative sample. Perbedaan intended/empirical menjadi flag review, bukan perubahan label otomatis. Calibration berbeda populasi, grade, form atau versi belum comparable tanpa linking.

**Istilah untuk dijelaskan:** **CTT** - Classical Test Theory: ringkasan skor dan kualitas item dari sampel. Alasan: Memberi pengamatan langsung dan tetap berguna sebelum IRT siap. **IRT** - Item Response Theory: model probabilitas jawaban berdasarkan kemampuan dan item. Alasan: Memisahkan parameter item dan perkiraan kemampuan pada skala model. **Intended / empirical** - Tuntutan isi yang direncanakan dan kesulitan dari pengalaman sampel. Alasan: Menghindari penafsiran bahwa satu hasil respons langsung menetapkan label isi.

**Rumus opsional - Ringkasan jawaban dan model peluang:**

$$
\begin{aligned}\hat p_j&=\frac{\text{benar}_j}{\text{observed valid}_j}\\P_j(\theta)&=c_j+(1-c_j)\\&\quad\cdot\sigma\!\left[a_j(\theta-b_j)\right]\end{aligned}
$$

Simbol: $\hat p_j$ = Proporsi benar observed pada item j. $\theta$ = Kemampuan laten siswa pada calibration lokal. $a_j$ = Discrimination/slope. $b_j$ = Lokasi difficulty item. $c_j$ = Lower asymptote; diestimasi pada 3PL.

Mengapa rumus ini digunakan: Persamaan memperlihatkan perbedaan antara ringkasan sampel dan model peluang.

## Slide 10. Bagaimana IRT benar-benar dihitung?

**Pesan utama:** Pola benar-salah dipakai untuk mencari karakter soal, lalu kemampuan siswa diperkirakan bersama ketidakpastiannya.

- Rasch mencari kesulitan; 2PL menambah daya pembeda; 3PL menambah peluang dasar.
- 41 titik bantu mewakili kemungkinan kemampuan ketika perhitungan dilakukan.
- Asumsi awal menahan nilai ekstrem; algoritme mencari parameter yang cocok.
- Hasil memuat kemampuan, ketidakpastian dan pemeriksaan kecocokan model.

**Mengapa tahap ini diperlukan:** Kemampuan tidak terlihat langsung. Perhitungan mempertimbangkan beberapa kemungkinan dan melaporkan ketidakpastian perkiraannya.

**Catatan pembicara:** Regularized marginal likelihood mempertimbangkan berbagai kemungkinan kemampuan sebelum mengoptimasi item. Gauss-Hermite memakai 41 titik bantu default untuk mendekati integral terhadap N(0,1); jumlah itu adalah konfigurasi numerik. L-BFGS-B mencari parameter dalam bounds. Prior b~N(0,3²), log a~N(0,0.75²), c~Beta(5,17) membantu nilai extreme tetap finite. c bukan 1/jumlah opsi. EAP adalah rata-rata posterior kemampuan; posterior SD menyatakan ketidakpastiannya. Warnings convergence/boundary/local dependence tetap memerlukan review. Ini batch calibration lokal research/advisory, bukan CAT/release otomatis.

**Istilah untuk dijelaskan:** **Marginal likelihood / Gauss-Hermite** - Pencocokan item dengan merata-ratakan peluang atas kemampuan; integrasinya didekati titik numerik. Alasan: Kemampuan laten tidak harus dianggap satu nilai pasti ketika item di-fit. **Regularization / prior** - Asumsi tambahan yang menahan parameter ekstrem saat evidence terbatas. Alasan: Menjaga estimasi lebih stabil; tidak menggantikan gate sampel dan asumsi. **EAP / posterior SD** - Rata-rata dan simpangan baku distribusi kemampuan setelah respons diamati. Alasan: Menampilkan perkiraan siswa beserta tingkat ketidakpastiannya.

**Rumus opsional - Peluang respons dengan kemampuan diperhitungkan:**

$$
\begin{aligned}\ell_{ij}(\theta)&=P_j(\theta)^{x_{ij}}\\&\quad\cdot[1-P_j(\theta)]^{1-x_{ij}}\\L_i&=\int\phi(\theta)\prod_{j\in O_i}\ell_{ij}(\theta)\,d\theta\\&\approx\sum_{q=1}^{41}w_q\prod_{j\in O_i}\ell_{ij}(\theta_q)\end{aligned}
$$

Simbol: $\ell_{ij}$ = Kontribusi likelihood respons siswa i pada item j. $x_{ij}$ = Respons observed: benar=1 atau salah=0. $O_i$ = Item observed siswa i; missing tidak memberi likelihood. $\phi$ = Densitas kemampuan N(0,1). $\theta_q,w_q$ = Titik dan bobot Gauss-Hermite yang disesuaikan untuk N(0,1).

Mengapa rumus ini digunakan: Integrasi mengakomodasi kemampuan yang belum diketahui; quadrature membuatnya dapat dihitung.

**Rumus opsional - Perkiraan kemampuan dan ketidakpastian:**

$$
\begin{aligned}\widehat\theta_i^{\mathrm{EAP}}&=\sum_q\pi_{iq}\theta_q\\\mathrm{SD}_i&=\sqrt{\sum_q\pi_{iq}\theta_q^2-(\widehat\theta_i^{\mathrm{EAP}})^2}\end{aligned}
$$

Simbol: $\pi_{iq}$ = Bobot posterior siswa i pada titik kemampuan q setelah respons diamati. $\widehat\theta_i^{\mathrm{EAP}}$ = Rata-rata posterior kemampuan. $\mathrm{SD}_i$ = Ketidakpastian posterior kemampuan.

Mengapa rumus ini digunakan: Satu nilai EAP saja belum menunjukkan seberapa kuat evidence siswa.

## Slide 11. Bagaimana hasil siswa memperbaiki model?

**Pesan utama:** Ahli meninjau hasil siswa, lalu perbaikan masuk melalui versi soal dan data belajar yang baru.

- Bandingkan perkiraan awal dengan hasil siswa pada soal dan kelompok yang sesuai.
- Ahli memilih mempertahankan, memperbaiki, atau menahan soal.
- Soal yang diperbaiki dinilai ulang dan disimpan sebagai data versi baru.
- Latih calon model pengganti dan periksa hasilnya sebelum diaktifkan.

**Mengapa tahap ini diperlukan:** IRT menunjukkan pola jawaban. Pemeriksaan ahli menghubungkan pola itu dengan mutu soal dan label yang dipelajari IndoBERT.

**Catatan pembicara:** Contoh: intended v2 Hard, CTT stabil Easy, b=-1.2. Sistem memberikan alasan review; label lama tidak ditimpa. Ahli mungkin memperbaiki distraktor dan memberi v3 label Medium setelah blind review. Gold baru berasal dari ahli, sedangkan confidence model hanya usulan. Keputusan empiris menyimpan affectsGoldLabels=false. Raw response matrix, theta dan a/b/c tidak menjadi fitur serializer/training aktif. Tidak ada formula 40% IndoBERT+60% LLM atau confidence×IRT untuk menentukan label baru. Perbandingan model adil memakai benchmark item/version yang tetap.

**Istilah untuk dijelaskan:** **Hold** - Status yang menahan delivery baru dan mengecualikan versi dari freeze berikutnya. Alasan: Perintah revisi memengaruhi penggunaan item tanpa menghapus sejarahnya. **Lineage** - Rantai asal dari versi lama ke keputusan, revisi, dataset dan model baru. Alasan: Reviewer dapat menjelaskan mengapa label atau model berubah. **Challenger** - Calon model pengganti yang dilatih dan dibandingkan dahulu. Alasan: Perubahan sistem dinilai sebelum diaktifkan.

## Slide 12. Apa yang tersedia dan apa berikutnya?

**Pesan utama:** Bagian utama tersedia untuk penelitian dan uji coba, sementara beberapa kemampuan masih perlu dibangun.

- Tersedia: label AI/ahli, pelatihan model, paket soal tetap dan analisis CTT/IRT.
- Model aktif memerlukan data memadai, hasil evaluasi dan persetujuan.
- Berikutnya: fitur IRT ke model, profil siswa dan tes adaptif.
- Label AI tetap untuk penelitian; IndoBERT sekarang tidak memberi prediksi kelas 7–12.

**Mengapa tahap ini diperlukan:** Menjelaskan batas implementasi membantu pembaca memahami hasil sekarang dan merencanakan pengembangan berikutnya.

**Catatan pembicara:** Kode tersedia belum berarti data nyata, provider, gold atau artifact final sudah tersedia. Calibration IRT masih lokal dan research/advisory. Tidak ada auto-release, auto-relabel, auto-retrain atau calibration item per jawaban. Untuk CAT diperlukan bank calibration released, online theta scoring, content/exposure constraints dan stopping policy. Fitur IRT ke model memerlukan schema dan fusion head baru, temporal/population split serta ablation. Approval artifact classifier adalah gate terpisah dari gate IRT. Silver tidak dapat menjadi servable hanya karena metrik teknisnya tinggi.

**Istilah untuk dijelaskan:** **Gate / servable** - Syarat data/model/evaluasi/persetujuan agar artifact dapat dilayani API. Alasan: Mencegah penggunaan calon model sebelum syaratnya terpenuhi. **CAT** - Tes adaptif yang memilih item berdasarkan evidence kemampuan dan aturan tes. Alasan: Memerlukan bank serta operasi tambahan di luar batch IRT. **Linking / release** - Penghubungan skala dan izin memakai calibration untuk tujuan tertentu. Alasan: Hasil lokal tidak langsung comparable atau layak digunakan di semua konteks.

**Rumus opsional - Gate artifact classifier:**

$$
\mathrm{servable}=A\land\neg R\land D\land C\land P
$$

Simbol: $A$ = approvedForProvisional. $R$ = researchOnly. $D$ = dataGatesPassed. $C$ = antiCollapsePassed. $P$ = promotionGates.passed.

Mengapa rumus ini digunakan: Metrik yang baik perlu disertai data yang memenuhi syarat, perilaku model sehat dan approval.

## Alasan pilihan metode

| Pilihan | Artinya | Mengapa digunakan | Batas |
|---|---|---|---|
| Pemeriksaan sumber dan versi | Konten, key, solusi dan media diperiksa serta diikat ke hash/versi. | Mencegah kesalahan konten menyebar ke label, scoring dan calibration. | Hash mendeteksi perubahan; hash sendiri tidak membuktikan isi benar. |
| Blind Gemini N=3 | Tiga run memberi silver labels sebelum prediksi model dibandingkan. | Memperlihatkan konsistensi dan mengurangi anchoring pada IndoBERT. | Satu model dapat salah bersama; silver bukan gold ahli atau calibrated confidence. |
| Konteks soal + tiga jenis label | Representasi teks bersama menghasilkan tiga aspek label berbeda. | Tuntutan konsep, proses berpikir dan difficulty tidak ditentukan oleh satu KKO. | Kualitas data, truncation, grade scope dan manifest artifact tetap membatasi hasil. |
| Temperature + confidence/entropy | Probabilitas dikalibrasi, lalu ringkasannya dipakai menurut routing policy. | Usulan meragukan dapat ditandai untuk review. | Threshold dipilih dari validation; confidence tinggi belum membuktikan kebenaran. |
| Human gold sebelum pilot | Versi item memiliki keputusan ahli serta key/solution terverifikasi. | Respons siswa membutuhkan item dan scoring yang dapat dipertanggungjawabkan. | Silver delivery adapter belum tersedia; pilot saat ini fixed-form/text-only. |
| Whole-session snapshot batch | Pilih satu completed session per subject pada cutoff/window yang jelas. | N tidak mengganda akibat repeated attempts dan hasil dapat diulang. | Belum ada scheduler otomatis atau CAT; first/last mengikuti started_at,id setelah filter completion window. |
| Gate, regularization dan EAP | Periksa data/asumsi, fit item dengan prior, ringkas kemampuan dengan uncertainty. | Memperhitungkan evidence terbatas dan kemampuan laten yang belum pasti. | IRT tetap calibration lokal research/advisory; warning atau prior tidak menggantikan validasi. |
| Review → versi → freeze → retrain | Bukti empiris memengaruhi contoh belajar setelah diperiksa ahli. | Menjaga perubahan label serta model dapat dilacak dan diuji. | Tidak ada auto-relabel, auto-retrain, direct IRT feature atau release otomatis. |

## Glosarium singkat

| Istilah | Artinya | Mengapa penting |
|---|---|---|
| Silver | Usulan label dari AI untuk penelitian. | Menyediakan rujukan awal sambil menjaga provenance AI. |
| Human gold | Label rujukan dari workflow ahli yang memenuhi gate. | Memberi sumber terkontrol untuk pilot dan training gold. |
| Blind review | Penilaian awal tidak melihat prediksi atau keputusan lain. | Mengurangi anchoring. |
| Evidence / solusi minimum | Bukti singkat dan langkah minimum untuk memverifikasi jawaban. | Membuat penilaian dapat diperiksa tanpa meminta hidden CoT. |
| Content hash / version | Sidik dan nomor revisi konten. | Mengikat respons serta label ke soal yang tepat. |
| Serializer / tokenizer | Penyusun teks tetap dan pengubah teks menjadi unit input model. | Menjaga input training/inference konsisten. |
| Encoder / head | Pembaca konteks dan penghasil satu jenis label. | Memisahkan representasi makna dari tugas klasifikasi. |
| KKO | Kata kerja operasional yang dideteksi secara leksikal. | Petunjuk opsional; tidak menjadi aturan penetapan label. |
| LoRA | Adapter rank kecil untuk penyesuaian model. | Mengurangi parameter trainable. |
| Ordinal / grade embedding | Urutan kategori difficulty dan vektor kelas sasaran. | Kesulitan relatif kelas serta urutan kategori perlu dimodelkan. |
| Confidence | Peluang tertinggi setelah calibration. | Merangkum kekuatan usulan label. |
| Entropy | Ukuran sebaran peluang di semua kategori. | Memperlihatkan keraguan yang tidak terlihat dari argmax saja. |
| Temperature | Parameter calibration yang dipilih dari validation. | Menyesuaikan ketajaman distribusi probabilitas. |
| CTT / Wilson interval | Ringkasan skor sampel dan rentang ketidakpastian proporsi benar. | Menyediakan pengamatan item sebelum atau bersama IRT. |
| IRT / a,b,c | Model peluang respons dengan slope, difficulty dan lower asymptote. | Memodelkan hubungan item dengan kemampuan pada skala lokal. |
| Theta / EAP / posterior SD | Kemampuan laten, rata-rata posterior dan ketidakpastiannya. | Skor siswa perlu disertai kekuatan evidence. |
| Gauss-Hermite 41 | Titik/bobot numerik default untuk mendekati integral kemampuan. | Membuat marginal likelihood dapat dihitung. |
| Prior / regularization | Asumsi tambahan yang menahan estimasi ekstrem. | Membantu kestabilan numerik saat evidence terbatas. |
| NA / missing | Respons tidak observed atau explicit skip. | Ketiadaan evidence tidak sama dengan salah. |
| N_selected / N_fit | Subject unik sesi terpilih dan orang yang lolos batas missing. | Jumlah sampel IRT harus berasal dari evidence eligible. |
| Snapshot / lineage | Versi data/hasil yang tetap dan rantai asal perubahannya. | Hasil dapat diulang dan keputusan dapat diaudit. |
| Hold / challenger | Penahanan versi item dan calon model pengganti. | Memberi ruang perbaikan serta evaluasi sebelum penggunaan. |
| Gate / calibration release | Syarat penggunaan artifact atau calibration untuk tujuan tertentu. | Hasil penelitian tidak otomatis menjadi layanan yang aktif. |
| CAT / linking | Tes adaptif dan penghubungan skala calibration. | Operasi adaptif dan perbandingan lintas form/populasi membutuhkan kemampuan tambahan. |

## Kalimat penutup presentasi

AI membantu menilai isi soal; jawaban siswa menunjukkan bagaimana soal bekerja saat digunakan. Ahli meninjau hasilnya, lalu perbaikan disimpan sebagai versi soal dan data baru untuk pelatihan model. Jawaban dicatat segera, sedangkan parameter soal IRT dihitung pada kumpulan jawaban pada waktu tertentu setelah data dan asumsi diperiksa.

## Rujukan untuk pemeriksaan teknis

- [Panduan lengkap animasi](33_ANIMATED_DATA_FLOW.md), [detail model/LLM](24_INDOBERT_FINETUNING_LLM_REASONING_DETAIL.md), [training grade-aware](25_GRADE_AWARE_ORDINAL_PIPELINE.md), [runbook CTT/IRT](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md) dan [topology serta integrasi target](28_END_TO_END_PERSONALIZED_ASSESSMENT_FLOW.md).
- [Serializer](../app/classification/v2/serializer.py), [model/LoRA/ordinal head](../app/classification/v2/model.py), [confidence/entropy](../app/classification/v2/runtime.py), [calibration](../app/classification/v2/calibration.py) dan [training/promotion](../app/training/v2/train_lora.py).
- [Blind LLM](../app/llm/silver.py), [consensus manusia](../app/annotation/consensus.py), [delivery/screening/hold](../app/assessment/store.py), [cleaning/CTT/readiness](../app/psychometrics/analysis.py), [IRT/EAP/quadrature](../app/psychometrics/irt.py) dan [policy numerik](../configs/psychometrics_policy.json).

Konten tab dan dokumen ini menggunakan data yang sama dari [presentation-summary.js](interactive/presentation-summary.js). Status implementasi mengikuti repository saat dokumentasi dibuat; artifact, scope, calibration dan data yang digunakan tetap harus dibaca melalui manifest masing-masing versi.
