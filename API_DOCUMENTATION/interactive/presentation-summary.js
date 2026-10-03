/* Indonesian presentation copy. Formula cards are rendered by the main page. */
window.FLOW_PRESENTATION = {
  intro: 'Mulai dari pertanyaan sederhana: bagaimana soal yang baru diekstrak menjadi soal yang dinilai, digunakan siswa, lalu diperbaiki berdasarkan bukti? Dua belas slide ini menceritakan alurnya, menjelaskan alasan setiap pilihan, dan membedakan fungsi yang tersedia dari rancangan berikutnya.',
  conclusion: 'AI membantu menilai isi soal; jawaban siswa menunjukkan bagaimana soal bekerja saat digunakan. Ahli meninjau hasilnya, lalu perbaikan disimpan sebagai versi soal dan data baru untuk pelatihan model. Jawaban dicatat segera, sedangkan parameter soal IRT dihitung pada kumpulan jawaban pada waktu tertentu setelah data dan asumsi diperiksa.',
  slides: [
    {
      id: 'ppt-purpose', title: '1. Mengapa alur ini diperlukan?',
      message: 'Kita menghubungkan isi soal, perkiraan AI dan bukti siswa tanpa kehilangan asal setiap keputusan.',
      bullets: [
        'JSON menyimpan soal beserta sumber, kunci dan medianya.',
        'LLM dan IndoBERT membantu memberi usulan label isi soal.',
        'Jawaban siswa dianalisis dengan CTT/IRT untuk pemeriksaan berikutnya.'
      ],
      why: 'Perkiraan dari isi soal dan hasil pengerjaan siswa dapat berbeda. Memisahkan bukti tersebut membantu menjelaskan penyebabnya.',
      speakerNotes: 'Ceritakan alur sebagai siklus belajar sistem. Sebelum siswa mengerjakan, kita hanya mempunyai isi soal dan perkiraan tuntutannya. Setelah respons terkumpul, kita dapat melihat bagaimana soal bekerja pada kelompok siswa tertentu. Kedua informasi itu saling melengkapi. Penjelasan ini juga menjaga kita agar tidak menyamakan label AI, label ahli dan parameter IRT.',
      terms: [
        {term: 'Label', meaning: 'Kategori yang diberikan untuk menjelaskan isi atau tuntutan soal.', why: 'Membantu menyusun dan mencari soal berdasarkan kebutuhan pembelajaran.'},
        {term: 'Bukti empiris', meaning: 'Informasi yang dihitung dari respons siswa yang valid.', why: 'Memeriksa apakah soal berfungsi sesuai tujuan ketika benar-benar dikerjakan.'}
      ],
      latex: []
    },
    {
      id: 'ppt-json', title: '2. Siapkan JSON yang dapat dipercaya',
      message: 'Soal masuk sebagai konten yang lengkap, memiliki versi dan dapat ditelusuri ke sumbernya.',
      bullets: [
        'Periksa teks soal, pilihan jawaban, kunci, solusi dan gambar.',
        'Simpan kelas siswa, sumber, nomor versi dan sidik isi.',
        'Soal bermasalah diperiksa lagi sebelum menjadi bahan penilaian.'
      ],
      why: 'Model dan penilaian jawaban dapat menghasilkan keluaran yang salah bila isi soal bermasalah. Pemeriksaan sumber mengatasi masalah sejak awal.',
      speakerNotes: 'JSON adalah wadah data, bukan tanda bahwa soal sudah valid. Stem berarti teks pertanyaan; opsi adalah pilihan jawaban; key adalah jawaban yang diverifikasi. Gambar yang diperlukan harus tersedia dan membutuhkan transkripsi terverifikasi untuk model teks. Hash menjadi sidik konten; versi menjelaskan revisi. Jika source JSON, prompt atau byte gambar berubah, penilaian lama yang tidak cocok harus dinilai ulang. Export soal_pretest_db.json tetap candidate bank dan bukan delivery siswa.',
      terms: [
        {term: 'Stem', meaning: 'Teks utama pertanyaan yang harus dijawab siswa.', why: 'Menjadi bagian penting input model dan tampilan siswa.'},
        {term: 'Hash / versi', meaning: 'Sidik isi dan nomor revisi soal.', why: 'Mengikat label serta respons ke konten yang tepat.'},
        {term: 'Provenance', meaning: 'Catatan asal dan proses yang menghasilkan data.', why: 'Membantu menelusuri atau mengulang pemeriksaan.'}
      ],
      latex: [
        {title: 'Identitas isi', tex: String.raw`H=\operatorname{SHA256}(\operatorname{canonicalJSON}(\mathrm{content}))`, symbols: [{symbol: 'H', meaning: 'Hash konten yang disusun secara deterministik.'}], why: 'Isi yang berubah menghasilkan sidik berbeda sehingga penilaian lama tidak dipakai diam-diam.'}
      ]
    },
    {
      id: 'ppt-llm', title: '3. LLM membantu memberi label awal',
      message: 'Gemini memakai pedoman penilaian untuk membuat usulan label sebelum prediksi IndoBERT dibandingkan.',
      bullets: [
        'Soal, kelas dan pedoman penilaian membantu LLM membuat label awal.',
        'Tiga penilaian tidak melihat prediksi model atau suara penilaian lain.',
        'Tiga suara sama diterima jika lolos pemeriksaan; kasus lain dinilai kembali.',
        'Simpan solusi singkat dan bukti; label AI belum menjadi label ahli.'
      ],
      why: 'Model memerlukan contoh berlabel untuk belajar. LLM membantu menyiapkan usulan awal, sementara penilaian tanpa melihat prediksi mengurangi pengaruh keputusan model sebelumnya.',
      speakerNotes: 'LLM dibutuhkan untuk menafsirkan langkah penyelesaian dan tuntutan konsep sebelum respons siswa tersedia. Tiga panggilan membantu memperlihatkan konsistensi, tetapi tetap berasal dari satu model Gemini; kesalahan bersama masih mungkin. Karena itu 3/3 bukan confidence terkalibrasi atau gold manusia. Silver 2–1, abstain, key conflict atau concern memerlukan adjudikasi terpisah. Hidden chain-of-thought tidak diminta/disimpan; yang ditampilkan adalah solusi minimum, evidence spans, alasan singkat dan difficulty evidence profile.',
      terms: [
        {term: 'Blind', meaning: 'Penilaian awal tidak melihat prediksi IndoBERT, vote lain atau estimasi difficulty agen.', why: 'Mengurangi anchoring pada jawaban yang sudah ada.'},
        {term: 'Silver label', meaning: 'Usulan label penelitian yang dibuat AI.', why: 'Menyediakan data awal dengan provenance yang tetap jelas.'},
        {term: 'Adjudikasi AI', meaning: 'Penilaian terpisah untuk kasus yang belum dapat diterima langsung.', why: 'Menyelesaikan ketidakcocokan tanpa menyamarkannya sebagai vote bulat.'}
      ],
      latex: []
    },
    {
      id: 'ppt-semantic', title: '4. IndoBERT mempelajari pola dalam konteks soal',
      message: 'Soal diubah menjadi teks yang susunannya tetap, lalu model membaca konteks dan memberi tiga jenis label.',
      bullets: [
        'Susunan teks mengikuti pilihan input pada versi model.',
        'Teks dibagi menjadi unit input agar dapat dibaca model.',
        'Pola dalam konteks soal dipakai untuk tiga jenis label.',
        'Kata kerja hanya petunjuk; satu kata tidak langsung menetapkan label.'
      ],
      why: 'Kesulitan dan proses berpikir ditentukan oleh keseluruhan tuntutan soal, bukan satu kata kerja.',
      speakerNotes: 'Tokenizer membagi teks menjadi unit yang dikenal model, kemudian encoder membaca hubungan antarbagiannya. [CLS] adalah representasi yang dipakai head klasifikasi. Model mempelajari hubungan dengan label dari banyak contoh training. Representation dapat stem_options, metadata, solution atau kko dan dikunci dalam manifest agar training/inference konsisten. KKO adalah kata kerja operasional yang dideteksi secara leksikal; presence kata hitung tidak otomatis berarti domain atau difficulty tertentu. LoRA menyesuaikan encoder melalui matriks tambahan kecil pada query/value.',
      terms: [
        {term: 'Encoder / [CLS]', meaning: 'Pembaca konteks teks dan representasi yang dipakai untuk klasifikasi.', why: 'Memungkinkan model menggunakan hubungan antara soal, opsi dan metadata.'},
        {term: 'KKO', meaning: 'Kata kerja operasional yang dideteksi sebagai fitur opsional.', why: 'Memberi petunjuk leksikal tanpa menggantikan penilaian tuntutan soal.'},
        {term: 'LoRA', meaning: 'Adapter dengan matriks rank kecil yang dilatih saat fine-tuning.', why: 'Mengurangi jumlah parameter yang perlu disesuaikan.'}
      ],
      latex: [
        {title: 'Penyesuaian bobot LoRA', tex: String.raw`W'=W+\frac{\alpha}{r}BA`, symbols: [{symbol: 'W', meaning: 'Bobot dasar yang dibekukan pada jalur LoRA.'}, {symbol: 'A,B', meaning: 'Matriks adapter yang dipelajari.'}, {symbol: 'r', meaning: 'Rank adapter.'}, {symbol: String.raw`\alpha`, meaning: 'Faktor skala adapter.'}], why: 'Perubahan dipelajari melalui adapter kecil; head klasifikasi juga dilatih.'}
      ]
    },
    {
      id: 'ppt-heads', title: '5. Mengapa ada tiga jenis label?',
      message: 'Proses berpikir, jenis pengetahuan dan tingkat kesulitan menjelaskan tiga sisi berbeda dari soal.',
      bullets: [
        'Proses berpikir: mengingat, menerapkan, atau menalar.',
        'Pengetahuan: fakta, konsep, prosedur, atau refleksi strategi.',
        'Kesulitan: mudah, sedang, sulit relatif terhadap kelas siswa.',
        'Pada pelatihan baru, model mempertimbangkan kelas dan urutan kesulitan.'
      ],
      why: 'Soal prosedural dapat mudah atau sulit. Satu kategori tidak cukup menjelaskan seluruh karakter soal.',
      speakerNotes: 'Head berarti bagian model yang menghasilkan satu jenis label. Kognitif menggambarkan proses berpikir, knowledge menggambarkan jenis pengetahuan, intended difficulty memperkirakan tantangan untuk kelas sasaran. Grade embedding menyediakan representasi kelas agar difficulty head dapat mempertimbangkan tingkat pembelajaran. Default training baru grade-aware-ordinal-v2 menggunakan dua batas terurut. Artifact lama dapat parallel-v1, sehingga arsitektur yang benar dibaca dari manifest. Runtime kini menerima prediksi in-scope untuk grade 1–6; grade 7–12 menghasilkan abstain/out_of_scope.',
      terms: [
        {term: 'Head', meaning: 'Bagian model yang memetakan representasi encoder menjadi label tertentu.', why: 'Memungkinkan satu encoder mendukung tiga tugas yang berbeda.'},
        {term: 'Ordinal', meaning: 'Kategori dengan urutan, seperti Easy < Medium < Hard.', why: 'Memakai struktur urutan saat difficulty dipelajari.'},
        {term: 'Grade embedding', meaning: 'Vektor yang merepresentasikan kelas siswa pada difficulty head.', why: 'Kesulitan soal perlu dipertimbangkan relatif terhadap kelas sasaran.'}
      ],
      latex: [
        {title: 'Peluang pada urutan kesulitan', tex: String.raw`\begin{aligned}q_k&=\sigma(s-\tau_k),\quad \tau_1>\tau_0\\p_E&=1-q_0\\p_M&=q_0-q_1\\p_H&=q_1\end{aligned}`, symbols: [{symbol: 's', meaning: 'Skor dari representasi encoder dan grade embedding.'}, {symbol: String.raw`\tau_0,\tau_1`, meaning: 'Cutpoints terurut yang dipelajari.'}, {symbol: String.raw`\sigma`, meaning: 'Sigmoid.'}, {symbol: 'p_E,p_M,p_H', meaning: 'Peluang Easy, Medium dan Hard sebelum calibration.'}], why: 'Dua batas menjaga hubungan urut tiga kategori difficulty.'}
      ]
    },
    {
      id: 'ppt-confidence', title: '6. Seberapa yakin dan seberapa tersebar?',
      message: 'Confidence melihat peluang terbesar; entropy melihat sebaran seluruh peluang.',
      bullets: [
        'Confidence = peluang label dengan nilai tertinggi.',
        'Entropy rendah berarti peluang terkonsentrasi; tinggi berarti tersebar.',
        'Peluang disesuaikan menggunakan data pemeriksaan yang terpisah.',
        'Batas keyakinan mengatur pemeriksaan; syarat isi atau kelas gagal berarti tidak memberi label.'
      ],
      why: 'Label dengan peluang terbesar saja belum menunjukkan keraguan model. Confidence dan entropy membantu menandai usulan yang perlu diperiksa.',
      speakerNotes: 'Contoh p=[0.80,0.15,0.05] memberi confidence 0.80 dan normalized entropy sekitar 0.558. Dua keluaran ini dihitung setelah probabilitas dikalibrasi; keduanya bukan fitur awal. Temperature menyesuaikan tajamnya distribusi dan dipilih menggunakan validation, bukan test atau skor IRT. Policy confidence-entropy-v1 membutuhkan dua batas yang tersimpan pada manifest; confidence-only-v1 hanya menggunakan confidence untuk gate. Tinggi confidence tidak membuktikan label benar. Input mencapai truncation limit juga menghasilkan review.',
      terms: [
        {term: 'Confidence', meaning: 'Nilai peluang tertinggi setelah calibration.', why: 'Menunjukkan kekuatan usulan label utama.'},
        {term: 'Normalized entropy', meaning: 'Ringkasan sebaran peluang dengan rentang 0–1.', why: 'Menunjukkan apakah model membagi peluang ke banyak label.'},
        {term: 'Temperature', meaning: 'Parameter calibration yang mengubah ketajaman distribusi.', why: 'Membantu probabilitas sesuai dengan ketepatan pada validation.'}
      ],
      latex: [
        {title: 'Penyesuaian peluang dan ringkasan keyakinan', tex: String.raw`\begin{aligned}p_k&=\frac{\exp(z_k/T)}{\sum_{\ell=1}^{K}\exp(z_\ell/T)}\\C&=\max_k p_k\\H_{\mathrm{norm}}&=-\frac{\sum_{k=1}^{K}p_k\ln p_k}{\ln K}\end{aligned}`, symbols: [{symbol: 'z_k', meaning: 'Logit head multiclass; log raw probability untuk head ordinal.'}, {symbol: 'T', meaning: 'Temperature dari validation.'}, {symbol: 'K', meaning: 'Jumlah kategori pada head: 3 atau 4.'}, {symbol: 'C', meaning: 'Calibrated confidence.'}, {symbol: String.raw`H_{\mathrm{norm}}`, meaning: 'Normalized entropy.'}], why: 'Calibration diterapkan dulu, kemudian dua ringkasan digunakan sesuai policy artifact.'}
      ]
    },
    {
      id: 'ppt-student', title: '7. Soal disahkan, lalu dikerjakan siswa',
      message: 'Uji coba mengirim soal yang disahkan ahli dan menilai jawaban menggunakan kunci di server.',
      bullets: [
        'Soal memakai label ahli, kunci/solusi terverifikasi dan izin untuk digunakan.',
        'Urutan pilihan diacak, lalu tetap sama saat siswa memuat ulang.',
        'Server mencatat benar=1, salah=0, dilewati=belum ada skor.',
        'Kepemilikan sesi dan pencegahan data ganda menjaga respons peserta.'
      ],
      why: 'Analisis hasil siswa memerlukan soal yang tepat, penilaian konsisten dan jawaban yang tidak terhitung dua kali.',
      speakerNotes: 'Gold berasal dari workflow tiga ahli manusia, bukan tiga panggilan Gemini. Untuk gold, vote lengkap 3–0 atau 2–1 dapat settled jika gate konten/key/solution lolos. Pilot sekarang fixed-form dan text-only; gambar esensial memerlukan transkripsi terverifikasi. Siswa tidak menerima kunci, solusi atau reasoning LLM. Receipt respons juga tidak menampilkan correctness saat pilot. Server memetakan public option ID ke opsi privat dan menghitung skor. Explicit skip tetap null; sesi complete memerlukan seluruh item answered atau skipped.',
      terms: [
        {term: 'Human gold', meaning: 'Label dan konten rujukan yang disahkan melalui workflow ahli.', why: 'Menjadi sumber yang diizinkan untuk pilot sekarang.'},
        {term: 'Server scoring', meaning: 'Penilaian jawaban menggunakan kunci versi di server.', why: 'Menjaga jawaban dan nilai terikat pada item yang benar.'},
        {term: 'NA / idempotency', meaning: 'Missing score dan aturan agar pengiriman ulang tidak membuat data ganda.', why: 'Menghindari skip menjadi salah serta siswa terhitung berulang.'}
      ],
      latex: [
        {title: 'Skor matriks respons', tex: String.raw`x_{ij}=\begin{cases}1&\text{jawaban benar}\\0&\text{jawaban salah}\\\mathrm{NA}&\text{skip atau missing}\end{cases}`, symbols: [{symbol: 'i', meaning: 'Siswa/subject yang dipilih untuk analisis.'}, {symbol: 'j', meaning: 'Versi item yang dianalisis.'}], why: 'Missing menyatakan ketiadaan evidence; tidak dianggap jawaban salah.'}
      ]
    },
    {
      id: 'ppt-realtime', title: '8. Catat segera, hitung pada waktu tertentu',
      message: 'Kita tidak perlu menunggu seluruh siswa masa depan; analisis memakai jawaban yang memenuhi syarat pada batas waktu yang jelas.',
      bullets: [
        'Jawaban disimpan segera; operator memulai analisis pada kumpulan jawaban.',
        'Pilih satu sesi selesai per siswa dalam rentang waktu analisis.',
        'Jumlah siswa dihitung dari sampel yang lolos, bukan jumlah akun atau pengiriman.',
        'Data baru menghasilkan hasil baru; data dan aturan sama memakai hasil tersimpan.'
      ],
      why: 'Siswa terus menambah jawaban. Menyimpan hasil beserta data dan waktunya membuat perhitungan dapat diulang dengan jelas.',
      speakerNotes: 'N_selected adalah unique subjects dengan completed session terpilih. First/last memilih whole session berdasarkan started_at,id setelah filter completed_at [from,to). Event invalid, rapid guesses atau mismatch dikeluarkan; missing tetap NA. N_fit mengecualikan orang dengan observed rate di bawah 70%. Minimum default Rasch=100 orang/5 item, 2PL=300/10, 3PL=1000/20. Masing-masing item juga membutuhkan 50 observed dan minimal 5 benar serta 5 salah; coverage, connected design dan assumption review tetap diperiksa. Belum ada scheduler atau calibration per jawaban otomatis.',
      terms: [
        {term: 'Snapshot', meaning: 'Hasil analisis dari data/window/policy tertentu yang disimpan tetap.', why: 'Memisahkan evidence lama dari jawaban yang datang setelah cutoff.'},
        {term: 'N_selected / N_fit', meaning: 'Jumlah subject sesi terpilih dan jumlah yang lolos batas missing untuk fit.', why: 'Menggunakan sampel eligible daripada semua peserta terdaftar.'},
        {term: 'Cutoff window', meaning: 'Rentang completion time yang menentukan cohort analisis.', why: 'Memberi batas yang jelas ketika siswa terus masuk.'}
      ],
      latex: [
        {title: 'Jumlah orang yang dapat di-fit', tex: String.raw`N_{\mathrm{fit}}=\sum_{i=1}^{N_{\mathrm{selected}}}\mathbf{1}\!\left(\frac{\sum_{j=1}^{J}m_{ij}}{J}\ge0.70\right) `, symbols: [{symbol: 'm_{ij}', meaning: '1 jika respons item observed valid, 0 jika missing/skip.'}, {symbol: 'J', meaning: 'Jumlah versi item.'}, {symbol: String.raw`N_{\mathrm{selected}}`, meaning: 'Jumlah subject unik yang dipilih setelah whole-session selection.'}], why: 'Fit tidak bergantung pada total siswa yang akan datang; gate memakai evidence yang sudah tersedia.'}
      ]
    },
    {
      id: 'ppt-ctt-irt', title: '9. CTT dan IRT menjawab apa?',
      message: 'CTT merangkum jawaban yang terlihat; IRT memodelkan hubungan kemampuan siswa dan karakter soal.',
      bullets: [
        'CTT merangkum jumlah benar, mutu pilihan jawaban dan konsistensi tes.',
        'IRT menghitung kesulitan, daya pembeda dan peluang dasar sesuai model.',
        'CTT tetap dihitung ketika syarat data atau asumsi IRT belum terpenuhi.',
        'Hasil nyata melengkapi perkiraan awal; ahli memutuskan perubahan.'
      ],
      why: 'Proporsi benar memberi gambaran cepat. IRT menjelaskan hubungan siswa dengan soal ketika data dan asumsi mendukung.',
      speakerNotes: 'p tinggi berarti item dijawab benar oleh banyak siswa dalam sampel tersebut. b menyatakan posisi difficulty pada skala kemampuan lokal, sehingga p dan b bukan angka yang dibandingkan langsung. CTT corrected item-total/discrimination dan KR-20 menggunakan complete cases untuk score joins; variance item dan total KR-20 sama-sama ddof=1. IRT membutuhkan asumsi unidimensional, local independence dan representative sample. Perbedaan intended/empirical menjadi flag review, bukan perubahan label otomatis. Calibration berbeda populasi, grade, form atau versi belum comparable tanpa linking.',
      terms: [
        {term: 'CTT', meaning: 'Classical Test Theory: ringkasan skor dan kualitas item dari sampel.', why: 'Memberi pengamatan langsung dan tetap berguna sebelum IRT siap.'},
        {term: 'IRT', meaning: 'Item Response Theory: model probabilitas jawaban berdasarkan kemampuan dan item.', why: 'Memisahkan parameter item dan perkiraan kemampuan pada skala model.'},
        {term: 'Intended / empirical', meaning: 'Tuntutan isi yang direncanakan dan kesulitan dari pengalaman sampel.', why: 'Menghindari penafsiran bahwa satu hasil respons langsung menetapkan label isi.'}
      ],
      latex: [
        {title: 'Ringkasan jawaban dan model peluang', tex: String.raw`\begin{aligned}\hat p_j&=\frac{\text{benar}_j}{\text{observed valid}_j}\\P_j(\theta)&=c_j+(1-c_j)\\&\quad\cdot\sigma\!\left[a_j(\theta-b_j)\right]\end{aligned}`, symbols: [{symbol: String.raw`\hat p_j`, meaning: 'Proporsi benar observed pada item j.'}, {symbol: String.raw`\theta`, meaning: 'Kemampuan laten siswa pada calibration lokal.'}, {symbol: 'a_j', meaning: 'Discrimination/slope.'}, {symbol: 'b_j', meaning: 'Lokasi difficulty item.'}, {symbol: 'c_j', meaning: 'Lower asymptote; diestimasi pada 3PL.'}], why: 'Persamaan memperlihatkan perbedaan antara ringkasan sampel dan model peluang.'}
      ]
    },
    {
      id: 'ppt-irt-fit', title: '10. Bagaimana IRT benar-benar dihitung?',
      message: 'Pola benar-salah dipakai untuk mencari karakter soal, lalu kemampuan siswa diperkirakan bersama ketidakpastiannya.',
      bullets: [
        'Rasch mencari kesulitan; 2PL menambah daya pembeda; 3PL menambah peluang dasar.',
        '41 titik bantu mewakili kemungkinan kemampuan ketika perhitungan dilakukan.',
        'Asumsi awal menahan nilai ekstrem; algoritme mencari parameter yang cocok.',
        'Hasil memuat kemampuan, ketidakpastian dan pemeriksaan kecocokan model.'
      ],
      why: 'Kemampuan tidak terlihat langsung. Perhitungan mempertimbangkan beberapa kemungkinan dan melaporkan ketidakpastian perkiraannya.',
      speakerNotes: 'Regularized marginal likelihood mempertimbangkan berbagai kemungkinan kemampuan sebelum mengoptimasi item. Gauss-Hermite memakai 41 titik bantu default untuk mendekati integral terhadap N(0,1); jumlah itu adalah konfigurasi numerik. L-BFGS-B mencari parameter dalam bounds. Prior b~N(0,3²), log a~N(0,0.75²), c~Beta(5,17) membantu nilai extreme tetap finite. c bukan 1/jumlah opsi. EAP adalah rata-rata posterior kemampuan; posterior SD menyatakan ketidakpastiannya. Warnings convergence/boundary/local dependence tetap memerlukan review. Ini batch calibration lokal research/advisory, bukan CAT/release otomatis.',
      terms: [
        {term: 'Marginal likelihood / Gauss-Hermite', meaning: 'Pencocokan item dengan merata-ratakan peluang atas kemampuan; integrasinya didekati titik numerik.', why: 'Kemampuan laten tidak harus dianggap satu nilai pasti ketika item di-fit.'},
        {term: 'Regularization / prior', meaning: 'Asumsi tambahan yang menahan parameter ekstrem saat evidence terbatas.', why: 'Menjaga estimasi lebih stabil; tidak menggantikan gate sampel dan asumsi.'},
        {term: 'EAP / posterior SD', meaning: 'Rata-rata dan simpangan baku distribusi kemampuan setelah respons diamati.', why: 'Menampilkan perkiraan siswa beserta tingkat ketidakpastiannya.'}
      ],
      latex: [
        {title: 'Peluang respons dengan kemampuan diperhitungkan', tex: String.raw`\begin{aligned}\ell_{ij}(\theta)&=P_j(\theta)^{x_{ij}}\\&\quad\cdot[1-P_j(\theta)]^{1-x_{ij}}\\L_i&=\int\phi(\theta)\prod_{j\in O_i}\ell_{ij}(\theta)\,d\theta\\&\approx\sum_{q=1}^{41}w_q\prod_{j\in O_i}\ell_{ij}(\theta_q)\end{aligned}`, symbols: [{symbol: String.raw`\ell_{ij}`, meaning: 'Kontribusi likelihood respons siswa i pada item j.'}, {symbol: 'x_{ij}', meaning: 'Respons observed: benar=1 atau salah=0.'}, {symbol: 'O_i', meaning: 'Item observed siswa i; missing tidak memberi likelihood.'}, {symbol: String.raw`\phi`, meaning: 'Densitas kemampuan N(0,1).'}, {symbol: String.raw`\theta_q,w_q`, meaning: 'Titik dan bobot Gauss-Hermite yang disesuaikan untuk N(0,1).'}], why: 'Integrasi mengakomodasi kemampuan yang belum diketahui; quadrature membuatnya dapat dihitung.'},
        {title: 'Perkiraan kemampuan dan ketidakpastian', tex: String.raw`\begin{aligned}\widehat\theta_i^{\mathrm{EAP}}&=\sum_q\pi_{iq}\theta_q\\\mathrm{SD}_i&=\sqrt{\sum_q\pi_{iq}\theta_q^2-(\widehat\theta_i^{\mathrm{EAP}})^2}\end{aligned}`, symbols: [{symbol: String.raw`\pi_{iq}`, meaning: 'Bobot posterior siswa i pada titik kemampuan q setelah respons diamati.'}, {symbol: String.raw`\widehat\theta_i^{\mathrm{EAP}}`, meaning: 'Rata-rata posterior kemampuan.'}, {symbol: String.raw`\mathrm{SD}_i`, meaning: 'Ketidakpastian posterior kemampuan.'}], why: 'Satu nilai EAP saja belum menunjukkan seberapa kuat evidence siswa.'}
      ]
    },
    {
      id: 'ppt-feedback', title: '11. Bagaimana hasil siswa memperbaiki model?',
      message: 'Ahli meninjau hasil siswa, lalu perbaikan masuk melalui versi soal dan data belajar yang baru.',
      bullets: [
        'Bandingkan perkiraan awal dengan hasil siswa pada soal dan kelompok yang sesuai.',
        'Ahli memilih mempertahankan, memperbaiki, atau menahan soal.',
        'Soal yang diperbaiki dinilai ulang dan disimpan sebagai data versi baru.',
        'Latih calon model pengganti dan periksa hasilnya sebelum diaktifkan.'
      ],
      why: 'IRT menunjukkan pola jawaban. Pemeriksaan ahli menghubungkan pola itu dengan mutu soal dan label yang dipelajari IndoBERT.',
      speakerNotes: 'Contoh: intended v2 Hard, CTT stabil Easy, b=-1.2. Sistem memberikan alasan review; label lama tidak ditimpa. Ahli mungkin memperbaiki distraktor dan memberi v3 label Medium setelah blind review. Gold baru berasal dari ahli, sedangkan confidence model hanya usulan. Keputusan empiris menyimpan affectsGoldLabels=false. Raw response matrix, theta dan a/b/c tidak menjadi fitur serializer/training aktif. Tidak ada formula 40% IndoBERT+60% LLM atau confidence×IRT untuk menentukan label baru. Perbandingan model adil memakai benchmark item/version yang tetap.',
      terms: [
        {term: 'Hold', meaning: 'Status yang menahan delivery baru dan mengecualikan versi dari freeze berikutnya.', why: 'Perintah revisi memengaruhi penggunaan item tanpa menghapus sejarahnya.'},
        {term: 'Lineage', meaning: 'Rantai asal dari versi lama ke keputusan, revisi, dataset dan model baru.', why: 'Reviewer dapat menjelaskan mengapa label atau model berubah.'},
        {term: 'Challenger', meaning: 'Calon model pengganti yang dilatih dan dibandingkan dahulu.', why: 'Perubahan sistem dinilai sebelum diaktifkan.'}
      ],
      latex: []
    },
    {
      id: 'ppt-boundary', title: '12. Apa yang tersedia dan apa berikutnya?',
      message: 'Bagian utama tersedia untuk penelitian dan uji coba, sementara beberapa kemampuan masih perlu dibangun.',
      bullets: [
        'Tersedia: label AI/ahli, pelatihan model, paket soal tetap dan analisis CTT/IRT.',
        'Model aktif memerlukan data memadai, hasil evaluasi dan persetujuan.',
        'Berikutnya: fitur IRT ke model, profil siswa dan tes adaptif.',
        'Label AI tetap untuk penelitian; IndoBERT sekarang tidak memberi prediksi kelas 7–12.'
      ],
      why: 'Menjelaskan batas implementasi membantu pembaca memahami hasil sekarang dan merencanakan pengembangan berikutnya.',
      speakerNotes: 'Kode tersedia belum berarti data nyata, provider, gold atau artifact final sudah tersedia. Calibration IRT masih lokal dan research/advisory. Tidak ada auto-release, auto-relabel, auto-retrain atau calibration item per jawaban. Untuk CAT diperlukan bank calibration released, online theta scoring, content/exposure constraints dan stopping policy. Fitur IRT ke model memerlukan schema dan fusion head baru, temporal/population split serta ablation. Approval artifact classifier adalah gate terpisah dari gate IRT. Silver tidak dapat menjadi servable hanya karena metrik teknisnya tinggi.',
      terms: [
        {term: 'Gate / servable', meaning: 'Syarat data/model/evaluasi/persetujuan agar artifact dapat dilayani API.', why: 'Mencegah penggunaan calon model sebelum syaratnya terpenuhi.'},
        {term: 'CAT', meaning: 'Tes adaptif yang memilih item berdasarkan evidence kemampuan dan aturan tes.', why: 'Memerlukan bank serta operasi tambahan di luar batch IRT.'},
        {term: 'Linking / release', meaning: 'Penghubungan skala dan izin memakai calibration untuk tujuan tertentu.', why: 'Hasil lokal tidak langsung comparable atau layak digunakan di semua konteks.'}
      ],
      latex: [
        {title: 'Gate artifact classifier', tex: String.raw`\mathrm{servable}=A\land\neg R\land D\land C\land P`, symbols: [{symbol: 'A', meaning: 'approvedForProvisional.'}, {symbol: 'R', meaning: 'researchOnly.'}, {symbol: 'D', meaning: 'dataGatesPassed.'}, {symbol: 'C', meaning: 'antiCollapsePassed.'}, {symbol: 'P', meaning: 'promotionGates.passed.'}], why: 'Metrik yang baik perlu disertai data yang memenuhi syarat, perilaku model sehat dan approval.'}
      ]
    }
  ],
  decisions: [
    {method: 'Pemeriksaan sumber dan versi', meaning: 'Konten, key, solusi dan media diperiksa serta diikat ke hash/versi.', why: 'Mencegah kesalahan konten menyebar ke label, scoring dan calibration.', limit: 'Hash mendeteksi perubahan; hash sendiri tidak membuktikan isi benar.'},
    {method: 'Blind Gemini N=3', meaning: 'Tiga run memberi silver labels sebelum prediksi model dibandingkan.', why: 'Memperlihatkan konsistensi dan mengurangi anchoring pada IndoBERT.', limit: 'Satu model dapat salah bersama; silver bukan gold ahli atau calibrated confidence.'},
    {method: 'Konteks soal + tiga jenis label', meaning: 'Representasi teks bersama menghasilkan tiga aspek label berbeda.', why: 'Tuntutan konsep, proses berpikir dan difficulty tidak ditentukan oleh satu KKO.', limit: 'Kualitas data, truncation, grade scope dan manifest artifact tetap membatasi hasil.'},
    {method: 'Temperature + confidence/entropy', meaning: 'Probabilitas dikalibrasi, lalu ringkasannya dipakai menurut routing policy.', why: 'Usulan meragukan dapat ditandai untuk review.', limit: 'Threshold dipilih dari validation; confidence tinggi belum membuktikan kebenaran.'},
    {method: 'Human gold sebelum pilot', meaning: 'Versi item memiliki keputusan ahli serta key/solution terverifikasi.', why: 'Respons siswa membutuhkan item dan scoring yang dapat dipertanggungjawabkan.', limit: 'Silver delivery adapter belum tersedia; pilot saat ini fixed-form/text-only.'},
    {method: 'Whole-session snapshot batch', meaning: 'Pilih satu completed session per subject pada cutoff/window yang jelas.', why: 'N tidak mengganda akibat repeated attempts dan hasil dapat diulang.', limit: 'Belum ada scheduler otomatis atau CAT; first/last mengikuti started_at,id setelah filter completion window.'},
    {method: 'Gate, regularization dan EAP', meaning: 'Periksa data/asumsi, fit item dengan prior, ringkas kemampuan dengan uncertainty.', why: 'Memperhitungkan evidence terbatas dan kemampuan laten yang belum pasti.', limit: 'IRT tetap calibration lokal research/advisory; warning atau prior tidak menggantikan validasi.'},
    {method: 'Review → versi → freeze → retrain', meaning: 'Bukti empiris memengaruhi contoh belajar setelah diperiksa ahli.', why: 'Menjaga perubahan label serta model dapat dilacak dan diuji.', limit: 'Tidak ada auto-relabel, auto-retrain, direct IRT feature atau release otomatis.'}
  ],
  glossary: [
    {term: 'Silver', meaning: 'Usulan label dari AI untuk penelitian.', why: 'Menyediakan rujukan awal sambil menjaga provenance AI.'},
    {term: 'Human gold', meaning: 'Label rujukan dari workflow ahli yang memenuhi gate.', why: 'Memberi sumber terkontrol untuk pilot dan training gold.'},
    {term: 'Blind review', meaning: 'Penilaian awal tidak melihat prediksi atau keputusan lain.', why: 'Mengurangi anchoring.'},
    {term: 'Evidence / solusi minimum', meaning: 'Bukti singkat dan langkah minimum untuk memverifikasi jawaban.', why: 'Membuat penilaian dapat diperiksa tanpa meminta hidden CoT.'},
    {term: 'Content hash / version', meaning: 'Sidik dan nomor revisi konten.', why: 'Mengikat respons serta label ke soal yang tepat.'},
    {term: 'Serializer / tokenizer', meaning: 'Penyusun teks tetap dan pengubah teks menjadi unit input model.', why: 'Menjaga input training/inference konsisten.'},
    {term: 'Encoder / head', meaning: 'Pembaca konteks dan penghasil satu jenis label.', why: 'Memisahkan representasi makna dari tugas klasifikasi.'},
    {term: 'KKO', meaning: 'Kata kerja operasional yang dideteksi secara leksikal.', why: 'Petunjuk opsional; tidak menjadi aturan penetapan label.'},
    {term: 'LoRA', meaning: 'Adapter rank kecil untuk penyesuaian model.', why: 'Mengurangi parameter trainable.'},
    {term: 'Ordinal / grade embedding', meaning: 'Urutan kategori difficulty dan vektor kelas sasaran.', why: 'Kesulitan relatif kelas serta urutan kategori perlu dimodelkan.'},
    {term: 'Confidence', meaning: 'Peluang tertinggi setelah calibration.', why: 'Merangkum kekuatan usulan label.'},
    {term: 'Entropy', meaning: 'Ukuran sebaran peluang di semua kategori.', why: 'Memperlihatkan keraguan yang tidak terlihat dari argmax saja.'},
    {term: 'Temperature', meaning: 'Parameter calibration yang dipilih dari validation.', why: 'Menyesuaikan ketajaman distribusi probabilitas.'},
    {term: 'CTT / Wilson interval', meaning: 'Ringkasan skor sampel dan rentang ketidakpastian proporsi benar.', why: 'Menyediakan pengamatan item sebelum atau bersama IRT.'},
    {term: 'IRT / a,b,c', meaning: 'Model peluang respons dengan slope, difficulty dan lower asymptote.', why: 'Memodelkan hubungan item dengan kemampuan pada skala lokal.'},
    {term: 'Theta / EAP / posterior SD', meaning: 'Kemampuan laten, rata-rata posterior dan ketidakpastiannya.', why: 'Skor siswa perlu disertai kekuatan evidence.'},
    {term: 'Gauss-Hermite 41', meaning: 'Titik/bobot numerik default untuk mendekati integral kemampuan.', why: 'Membuat marginal likelihood dapat dihitung.'},
    {term: 'Prior / regularization', meaning: 'Asumsi tambahan yang menahan estimasi ekstrem.', why: 'Membantu kestabilan numerik saat evidence terbatas.'},
    {term: 'NA / missing', meaning: 'Respons tidak observed atau explicit skip.', why: 'Ketiadaan evidence tidak sama dengan salah.'},
    {term: 'N_selected / N_fit', meaning: 'Subject unik sesi terpilih dan orang yang lolos batas missing.', why: 'Jumlah sampel IRT harus berasal dari evidence eligible.'},
    {term: 'Snapshot / lineage', meaning: 'Versi data/hasil yang tetap dan rantai asal perubahannya.', why: 'Hasil dapat diulang dan keputusan dapat diaudit.'},
    {term: 'Hold / challenger', meaning: 'Penahanan versi item dan calon model pengganti.', why: 'Memberi ruang perbaikan serta evaluasi sebelum penggunaan.'},
    {term: 'Gate / calibration release', meaning: 'Syarat penggunaan artifact atau calibration untuk tujuan tertentu.', why: 'Hasil penelitian tidak otomatis menjadi layanan yang aktif.'},
    {term: 'CAT / linking', meaning: 'Tes adaptif dan penghubungan skala calibration.', why: 'Operasi adaptif dan perbandingan lintas form/populasi membutuhkan kemampuan tambahan.'}
  ]
};
