/* Evidence-backed end of the pipeline; all examples below are illustrative. */
window.FLOW_FEEDBACK_STAGES = [
  {
    id: 'feedback-discrepancy', phase: 'Umpan balik',
    title: 'Bandingkan intended dengan bukti empiris',
    subtitle: 'Setelah siswa menjawab, lihat apakah pengalaman mereka sesuai perkiraan awal',
    status: 'implemented',
    summary: 'Awalnya soal mungkin diperkirakan sulit. Setelah banyak siswa mengerjakannya, ternyata sebagian besar menjawab benar. Sistem menyimpan kedua bukti tersebut agar ahli dapat mencari penyebab perbedaannya sebelum memutuskan perubahan.',
    learning: {
      story: 'Bayangkan soal berlabel Hard dijawab benar oleh 85 dari 100 siswa. Kita sekarang mempunyai perkiraan dari isi soal dan bukti dari pengalaman siswa. Perbedaan ini mengajak ahli memeriksa soal, kunci, distraktor dan kelompok siswanya.',
      terms: [
        {term: 'Intended difficulty', meaning: 'Perkiraan kesulitan dari tuntutan isi soal, relatif terhadap kelas sasaran.', why: 'Menjelaskan tantangan yang direncanakan sebelum respons siswa tersedia.'},
        {term: 'Empirical difficulty', meaning: 'Kesulitan yang terlihat dari respons kelompok siswa pada versi soal tertentu.', why: 'Membantu melihat apakah soal bekerja sesuai tujuan dalam pelaksanaan nyata.'},
        {term: 'Wilson interval', meaning: 'Rentang ketidakpastian untuk proporsi jawaban benar.', why: 'Mencegah kesimpulan terlalu cepat ketika sampel sedikit atau proporsi dekat batas kategori.'}
      ],
      why: 'Label awal dan respons nyata menjawab pertanyaan berbeda. Menyimpannya berdampingan membantu menemukan masalah tanpa kehilangan alasan keputusan sebelumnya.',
      next: 'Jika bukti cukup kuat menunjukkan perbedaan, ahli meninjau penyebabnya dan memilih tindakan.'
    },
    latex: [
      {title: 'Proporsi benar dan ketidakpastiannya', tex: String.raw`\hat p=\frac{x}{n},\qquad [L,U]=\frac{\hat p+\frac{z^2}{2n}\ \pm\ z\sqrt{\frac{\hat p(1-\hat p)}{n}+\frac{z^2}{4n^2}}}{1+\frac{z^2}{n}}`, symbols: [{symbol: 'x', meaning: 'Jumlah respons benar pada item.'}, {symbol: 'n', meaning: 'Jumlah respons valid observed pada item; skip tidak masuk penyebut.'}, {symbol: String.raw`\hat p`, meaning: 'Perkiraan proporsi benar.'}, {symbol: 'z', meaning: '1.96 untuk Wilson CI95.'}, {symbol: 'L,U', meaning: 'Batas bawah dan atas interval.'}], why: 'p memberi ringkasan; interval menunjukkan seberapa kuat bukti itu sebelum dibuat flag review.'},
      {title: 'Flag perbedaan CTT yang stabil', tex: String.raw`\begin{aligned}F&=\mathbf{1}\!\left\{d_i\ne\varnothing\ \land\ d_s\ne\varnothing\ \land\ d_i\ne d_s\right\}\\d_s&=\begin{cases}\mathrm{Easy}&L>0.70\\ \mathrm{Hard}&U<0.30\\ \mathrm{Medium}&L\ge0.30,\ U\le0.70\\ \varnothing&\text{lainnya}\end{cases}\end{aligned}`, symbols: [{symbol: 'F', meaning: 'Flag untuk review; hanya bernilai 1 ketika kedua kategori tersedia dan berbeda.'}, {symbol: 'd_i', meaning: 'Intended difficulty dari penilaian isi; ∅ bila label tidak tersedia.'}, {symbol: 'd_s', meaning: 'Kategori CTT yang stabil dari interval respons; ∅ bila interval melintasi batas kategori atau belum tersedia.'}, {symbol: 'L,U', meaning: 'Batas Wilson CI95 dari rumus sebelumnya.'}], why: 'Seluruh interval harus berada pada satu kategori agar perbedaan tidak sekadar akibat ketidakpastian sampel. Ketika intended atau stable band belum tersedia, flag bernilai 0.'}
    ],
    input: {questionVersionId: 'contoh:v2', intendedDifficulty: 'Hard', ctt: {correctCount: 85, validResponseCount: 100}, irtStatus: 'estimated (status global snapshot.irt.status)', irt: {b: -1.2}},
    process: [
      'CTT menghitung p dan Wilson CI95 dari respons valid per item, termasuk siswa yang tidak memiliki jawaban lengkap untuk seluruh tes.',
      'Band CTT: Easy bila p > easyP; Hard bila p < hardP; sisanya Medium. Flag intended_empirical_disagreement membutuhkan CI seluruhnya berada dalam satu band yang berbeda dari intended.',
      'IRT menyimpan band empiris dari b secara terpisah: Easy bila b < easyB, Hard bila b > hardB, selain itu Medium. Convergence, boundary dan uncertainty tetap diperiksa.',
      'Bandingkan hanya pada questionVersionId, grade, populationId, assessmentFamily, window dan calibration yang sesuai; perbedaan skala membutuhkan linking.'
    ],
    formula: 'p = correctCount / validResponseCount\nCTT stable Easy: WilsonLower > 0.70\nCTT stable Hard: WilsonUpper < 0.30\nCTT stable Medium: WilsonLower ≥ 0.30 dan WilsonUpper ≤ 0.70\nflag = intended tersedia ∧ stableBand tersedia ∧ intended ≠ stableBand\nIRT empirical: b < −1 → Easy; b > 1 → Hard; lainnya Medium',
    example: 'Contoh ilustratif: 85/100 benar memberi p=0.85 dan Wilson CI≈[0.767,0.907]. Karena batas bawah >0.70, band CTT stabil Easy. Intended Hard → flag review. b=−1.2 juga menghasilkan band IRT Easy. Tidak ada penggantian label otomatis.',
    output: {intendedDifficulty: 'Hard', cttEmpiricalDifficulty: 'Easy', irtEmpiricalDifficulty: 'Easy', reviewFlags: ['intended_empirical_disagreement'], labelChanged: false},
    cautions: [
      'CTT flag di kode berasal dari Wilson CI, bukan rumus langsung b mengganti intendedDifficulty.',
      'Bila CI melewati batas band, perbedaan p saja belum menghasilkan flag ini.',
      'p/b tidak menetapkan ulang mathCognitiveDomain atau knowledgeDimension; perbedaan dapat berasal dari kunci, distraktor, populasi atau kualitas konten.'
    ],
    sources: [{path: 'app/psychometrics/analysis.py', symbol: 'analyze_matrix'}, {path: 'app/psychometrics/irt.py', symbol: 'fit_irt'}, {path: 'configs/psychometrics_policy.json', symbol: 'easyP/hardP/easyB/hardB'}]
  },
  {
    id: 'feedback-human-decision', phase: 'Umpan balik',
    title: 'Ahli memutuskan retain, revise, atau quarantine',
    subtitle: 'Ahli memilih mempertahankan, memperbaiki, atau menahan soal',
    status: 'implemented',
    summary: 'Ahli membaca hasil siswa bersama isi soal dan kuncinya. Soal dapat dipertahankan, diminta diperbaiki, atau ditahan sementara. Keputusan dan alasannya disimpan agar langkah berikutnya dapat ditelusuri.',
    learning: {
      story: 'Jika siswa menjawab soal Hard dengan mudah, mungkin perkiraan awal terlalu tinggi, tetapi mungkin juga ada distraktor yang jelas salah. Ahli memeriksa penyebabnya sebelum memilih retain, revise atau quarantine.',
      terms: [
        {term: 'Retain', meaning: 'Mempertahankan versi dan label saat ini berdasarkan hasil review.', why: 'Perbedaan angka tidak selalu berarti soal atau label perlu diubah.'},
        {term: 'Revise / quarantine', meaning: 'Meminta revisi atau menahan versi agar tidak dikirim lagi.', why: 'Menghentikan pemakaian versi yang masih memerlukan pemeriksaan.'},
        {term: 'Immutable decision', meaning: 'Keputusan lama beserta bukti dan pelakunya tetap tercatat.', why: 'Membuat alasan perubahan dapat diaudit dan mencegah riwayat hilang.'}
      ],
      why: 'Statistik menunjukkan gejala. Peninjauan ahli menghubungkan gejala tersebut dengan isi soal dan tujuan pembelajaran.',
      next: 'Jika perlu revisi, operator membuat versi baru yang menjalani pemeriksaan dan anotasi lagi.'
    },
    latex: [
      {title: 'Aturan menahan versi soal', tex: String.raw`\operatorname{held}(v)=\mathbf{1}\!\left\{\operatorname{lastAction}(v)\in\{\mathrm{revise},\mathrm{quarantine}\}\right\}`, symbols: [{symbol: 'v', meaning: 'Versi soal yang sedang diperiksa.'}, {symbol: String.raw`\operatorname{lastAction}(v)`, meaning: 'Tindakan pada keputusan empiris terakhir untuk versi tersebut.'}, {symbol: String.raw`\mathbf{1}\{\cdot\}`, meaning: 'Bernilai 1 bila kondisi benar dan 0 bila salah.'}], why: 'Aturan ini membuat permintaan revisi benar-benar menghentikan delivery baru tanpa menghapus data lama.'}
    ],
    input: {snapshotId: 'contoh-empirical-v1', questionVersionId: 'contoh:v2', action: 'revise', rationale: 'Contoh: bukti menunjukkan distraktor perlu ditinjau.'},
    process: [
      'POST /api/v1/internal/psychometrics/snapshots/{snapshot_id}/decisions memakai expert session, X-CSRF-Token, expertId dan role yang diizinkan.',
      'Pastikan questionVersionId memang terdapat pada snapshot. Simpan snapshotHash, expertId, rationale, decisionId, timestamp dan idempotencyKey.',
      'retain mempertahankan label; revise meminta versi konten baru dan review ahli blind; quarantine menahan delivery.',
      'is_held membaca keputusan terakhir untuk versi itu. Create assessment dan next item memeriksa hold; jawaban item yang sudah terlanjur dikirim dicatat dengan item_held_after_delivery.',
      'Freeze berikutnya mengecualikan versi sumber maupun gold yang held dengan alasan empirical_expert_hold.'
    ],
    formula: 'held(version) = keputusan terakhir(version).action ∈ {revise, quarantine}\naffectsGoldLabels = false\nSatu keputusan immutable per (snapshotId, questionVersionId)',
    example: 'Contoh: ahli memilih revise pada contoh:v2. Versi v2 berhenti menjadi kandidat delivery baru; snapshot dan label v2 tetap tersimpan. Payload keputusan tidak memiliki field label pengganti.',
    output: {affectsGoldLabels: false, nextStep: 'new_content_version_and_blind_expert_review', heldVersion: 'contoh:v2', nextFreezeExclusion: 'empirical_expert_hold'},
    cautions: [
      'Idempotency key dengan isi berbeda ditolak; snapshot/item yang sudah memiliki keputusan tidak ditimpa.',
      'Hold setelah delivery tidak menghapus response event; analisis membersihkan event yang terflag.',
      'Keputusan retain pada snapshot berikutnya dapat memengaruhi status hold terakhir, tetapi tidak membatalkan sejarah keputusan lama.'
    ],
    sources: [{path: 'app/assessment/routes.py', symbol: 'decide'}, {path: 'app/assessment/store.py', symbol: 'decide / _held / next_item / respond'}, {path: 'scripts/freeze_dataset_v2.py', symbol: 'run / empirical_expert_hold'}]
  },
  {
    id: 'feedback-new-version', phase: 'Umpan balik',
    title: 'Siapkan versi baru dan label ahli yang baru',
    subtitle: 'Perbaiki isi, simpan versi baru, lalu minta ahli menilainya kembali',
    status: 'conditional',
    summary: 'Operator memperbaiki bagian soal yang bermasalah dan menyimpan perubahan sebagai versi baru. Tiga ahli menilai versi itu tanpa melihat prediksi model. Label baru berasal dari review tersebut dan tetap memiliki hubungan dengan versi sebelumnya.',
    learning: {
      story: 'Misalnya distraktor pada v2 diperbaiki sehingga lahir v3. Karena siswa akan melihat soal yang berbeda, v3 dinilai kembali. Jika labelnya berubah dari Hard menjadi Medium, riwayat tetap menunjukkan isi dan bukti untuk masing-masing versi.',
      terms: [
        {term: 'Content version / hash', meaning: 'Nomor versi dan sidik isi yang membedakan perubahan soal.', why: 'Menjaga respons dan label tetap terhubung dengan soal yang benar-benar dinilai.'},
        {term: 'Blind review', meaning: 'Reviewer tidak melihat prediksi AI atau suara reviewer lain pada penilaian awal.', why: 'Mengurangi pengaruh keputusan sebelumnya terhadap penilaian baru.'},
        {term: 'Human gold', meaning: 'Label rujukan dari workflow ahli manusia yang telah memenuhi gate konten dan consensus.', why: 'Menjadi sumber terkontrol untuk pilot dan dataset gold, berbeda dari usulan AI.'}
      ],
      why: 'Revisi mengubah objek yang dinilai. Versi dan review baru menjaga label tidak dipindahkan begitu saja dari soal lama.',
      next: 'Versi yang lolos ahli dikumpulkan ke snapshot dataset berikutnya.'
    },
    latex: [
      {title: 'Kapan nomor versi berubah?', tex: String.raw`v_{\mathrm{new}}=\begin{cases}v_{\mathrm{old}}&H_{\mathrm{new}}=H_{\mathrm{old}}\\v_{\mathrm{old}}+1&H_{\mathrm{new}}\ne H_{\mathrm{old}}\end{cases}`, symbols: [{symbol: 'v', meaning: 'Nomor contentVersion.'}, {symbol: 'H', meaning: 'Hash canonical content yang dibandingkan.'}], why: 'Konten identik tidak perlu menjadi revisi palsu; konten berbeda perlu riwayat baru.'},
      {title: 'Consensus label manusia per head', tex: String.raw`d_h=\begin{cases}\operatorname{mode}(y_{1h},y_{2h},y_{3h})&\text{3 vote lengkap dan mayoritas}\ \ge2\\\varnothing&\text{perlu diskusi}\end{cases}`, symbols: [{symbol: 'h', meaning: 'Salah satu dari tiga head label.'}, {symbol: 'y_{rh}', meaning: 'Label reviewer manusia r untuk head h.'}, {symbol: String.raw`\operatorname{mode}`, meaning: 'Label dengan jumlah suara terbanyak.'}], why: 'Aturan ini menjelaskan 3–0/2–1 manusia; kelayakan gold tetap membutuhkan gate konten/key/solution. Silver AI memakai aturan penerimaan berbeda.'}
    ],
    input: {previousQuestionVersionId: 'contoh:v2', amendedContent: {stem: 'Konten hasil revisi operator', options: 'Opsi hasil revisi', answerKey: 'Kunci terverifikasi'}, empiricalSnapshotId: 'contoh-empirical-v1'},
    process: [
      'Operator memperbaiki stem, opsi, key, solusi atau visual bila bukti mengharuskannya. Hitung canonical contentHash dan gunakan contentVersion baru bila hash berubah.',
      'Tiga ahli berbeda menilai versi yang sama secara blind. Repository menghilangkan agentAnswer, agentDifficulty, modelPrediction dan consensus dari payload reviewer.',
      'Gold manusia berbeda dari silver Gemini: tiga vote lengkap 3–0 atau 2–1 menghasilkan label settled; 1–1–1, abstain atau content/key conflict membutuhkan diskusi.',
      'Diskusi melibatkan tiga reviewer asal. Kasus tetap unresolved masuk senior adjudication; bukti tidak cukup menghasilkan quarantine. Label yang sudah settled tidak diganti oleh adjudication.',
      'Catat annotationIds, rubricVersion, evidence dan key/solution terverifikasi; hasil IRT berfungsi sebagai konteks review, bukan label yang dicopy.'
    ],
    formula: 'newContentVersion = oldVersion bila hash sama; oldVersion + 1 bila hash berubah\nGold head: 3/3 sama → unanimous; 2/3 sama → majority; lainnya → discussion_required\nContent eligible: 3 valid + 3 verified + satu key sama + 3 solusi tersedia',
    example: 'Contoh ilustratif: v2 berlabel Hard; setelah revisi distraktor, tiga ahli v3 memilih Medium/Medium/Easy. Gold v3 dapat berlabel Medium bila gate konten/key/solusi juga lolos. Gold v2 tetap Hard dalam snapshot lamanya.',
    output: {old: {questionVersionId: 'contoh:v2', intendedDifficulty: 'Hard'}, candidate: {questionVersionId: 'contoh:v3', intendedDifficulty: 'Medium', provenance: 'human_gold', status: 'gold_ready'}},
    cautions: [
      'Adjudication manusia tidak sama dengan adjudication AI. Silver N=3 hanya menerima 3–0 langsung dan tetap research/advisory.',
      'Revisi konten adalah pekerjaan operator; kode next_content_version hanya helper penghitung versi/hash.',
      'Versi dengan gambar esensial memerlukan transkripsi visual terverifikasi untuk model teks dan delivery pilot.'
    ],
    sources: [{path: 'app/ingestion/pretest_import.py', symbol: 'next_content_version'}, {path: 'app/annotation/consensus.py', symbol: 'build_consensus / apply_adjudication'}, {path: 'app/annotation/repository.py', symbol: 'reviewer_question / submit_discussion / _validate_resolved_labels'}, {path: 'scripts/materialize_consensus.py', symbol: 'run'}]
  },
  {
    id: 'feedback-freeze', phase: 'Umpan balik',
    title: 'Bekukan snapshot dan split versi berikutnya',
    subtitle: 'Kunci data yang lolos dan pisahkan bagian belajar dari bagian pengujian',
    status: 'conditional',
    summary: 'Soal yang lolos review dikumpulkan menjadi satu versi dataset yang tetap. Soal terkait diletakkan dalam kelompok yang sama ketika membagi data belajar dan pengujian. Dengan begitu hasil evaluasi lebih mencerminkan kemampuan model pada soal yang belum dipelajarinya.',
    learning: {
      story: 'Bayangkan model dilatih pada satu soal, lalu diuji pada salinan yang hanya berbeda nama tokoh. Nilai tinggi dapat berasal dari mengingat contoh. Snapshot dan pembagian per keluarga soal membantu menghindari keadaan itu.',
      terms: [
        {term: 'Snapshot / freeze', meaning: 'Salinan dataset versi tertentu yang dikunci bersama hash dan alasan pemilihan.', why: 'Training dan evaluasi dapat diulang dengan data yang sama.'},
        {term: 'Train / validation / test', meaning: 'Data untuk belajar, memilih pengaturan, dan menguji hasil secara terpisah.', why: 'Mencegah model dinilai menggunakan data yang telah memengaruhi pilihannya.'},
        {term: 'Leakage / source family', meaning: 'Kebocoran contoh terkait ke pengujian; source family adalah kelompok soal yang berhubungan.', why: 'Soal terkait harus dipisahkan bersama agar evaluasi tidak terlalu optimistis.'}
      ],
      why: 'Dataset yang jelas asal dan pembagiannya memungkinkan kita menjelaskan apakah peningkatan model berasal dari pembelajaran yang dapat dipercaya.',
      next: 'Training menggunakan bagian train; validation menentukan calibration dan pilihan model.'
    },
    latex: [
      {title: 'Sidik snapshot yang tetap', tex: String.raw`H_{\mathrm{snapshot}}=\operatorname{SHA256}\!\left(\operatorname{canonicalJSON}\!\left(\operatorname{sortedRows}\right)\right) `, symbols: [{symbol: String.raw`H_{\mathrm{snapshot}}`, meaning: 'Sidik dataset untuk memeriksa identitas isinya.'}, {symbol: String.raw`\operatorname{sortedRows}`, meaning: 'Training rows berurutan menurut questionVersionId.'}, {symbol: String.raw`\operatorname{canonicalJSON}`, meaning: 'Serialisasi JSON deterministik yang dipakai sebelum hashing.'}], why: 'Jika isi berubah, hash berubah, sehingga proses tidak dapat diam-diam memakai dataset yang berbeda.'}
    ],
    input: {decisions: 'gold_ready atau adjudicated', questionVersions: 'qualified, non-held', existingSnapshot: 'contoh-gold-v1'},
    process: [
      'freeze_dataset_v2.py membaca keputusan eligible dari MongoDB dan hold dari AssessmentStore bila file store tersedia.',
      'ensure_qualified_content_version mengikat key dan solusi ahli ke contentHash, membuat versi qualified baru bila konten terverifikasi belum mempunyai hash yang sama; provenance sourceQuestionVersionId dipertahankan.',
      'Versi yang held, missing, incomplete/quarantined atau tanpa essential visual transcript masuk exclusionSummary.',
      'Source group, shared stimulus, exact duplicate dan near duplicate dikelompokkan agar tidak bocor antara train/validation/test; target split 70/15/15 adalah pembagian per group.',
      'Data/class support, split integrity dan test-unlock gate tetap diperiksa. Snapshot ID/hash serta splitManifestHash disimpan; output immutable menolak overwrite.'
    ],
    formula: 'trainingRow = teks soal + metadata sesuai serializer + label tiga head dari keputusan ahli\nsnapshotHash = SHA256(canonical JSON rows berurutan)\nIRT response matrix, θ, a, b, c bukan field input training saat ini',
    example: 'Contoh: snapshot gold-v2 memasukkan v3 yang lolos ahli dan mengecualikan v2 yang held. Jika label/class support tidak cukup, snapshot tetap mencatat kegagalan gate dan training normal tidak diteruskan.',
    output: {snapshotId: 'contoh-gold-v2', labelProvenance: 'human_gold', sourceQuestionVersionId: 'contoh:v2', includedVersion: 'contoh:v3', exclusionSummary: {empirical_expert_hold: 1}, snapshotHash: '<SHA256>', splitManifestHash: '<SHA256>'},
    cautions: [
      'Snapshot silver menggunakan builder dan provenance silver tersendiri; tidak berubah menjadi human_gold.',
      '70/15/15 adalah target group split; pembagian aktual dapat berbeda karena kelompok tidak dipecah.',
      'Store hold harus memakai path assessment DB yang sama dengan API/CLI; tanpa file tersebut freeze tidak dapat membaca hold.'
    ],
    sources: [{path: 'scripts/freeze_dataset_v2.py', symbol: 'ensure_qualified_content_version / gold_from_documents / run'}, {path: 'app/training/v2/dataset.py', symbol: 'build_snapshot / deterministic_group_split / validate_split_integrity / save_snapshot'}]
  },
  {
    id: 'feedback-challenger', phase: 'Umpan balik',
    title: 'Latih, kalibrasi, dan kemas challenger',
    subtitle: 'Model belajar dari dataset baru, lalu probabilitasnya diperiksa',
    status: 'conditional',
    summary: 'Setelah label baru disahkan dan dataset dikunci, operator melatih calon model pengganti. Model belajar hubungan antara makna soal dan label rujukannya, kemudian diuji serta dikalibrasi. Inilah jalur hasil siswa dapat memperbaiki model melalui review dan data baru.',
    learning: {
      story: 'Hasil siswa membantu ahli memperbaiki soal atau label. Label yang disahkan menjadi contoh belajar baru. IndoBERT kemudian menyesuaikan bobotnya dari banyak contoh, sehingga satu hasil IRT tidak langsung mengubah prediksi model aktif.',
      terms: [
        {term: 'Challenger', meaning: 'Calon model baru yang akan dibandingkan dengan model sebelumnya.', why: 'Memberi ruang menguji manfaat perubahan sebelum mengaktifkannya.'},
        {term: 'Loss / optimizer', meaning: 'Ukuran kesalahan terhadap label rujukan dan mekanisme untuk menyesuaikan bobot.', why: 'Menjelaskan bagaimana contoh berlabel benar-benar mengubah model saat training.'},
        {term: 'LoRA', meaning: 'Matriks tambahan berukuran kecil yang dilatih pada bagian query/value encoder.', why: 'Mengurangi jumlah parameter trainable saat menyesuaikan IndoBERT.'},
        {term: 'Calibration', meaning: 'Penyesuaian probabilitas berdasarkan validation, lalu pemilihan batas review.', why: 'Membantu confidence lebih sesuai dengan ketepatan yang diamati pada evaluasi.'}
      ],
      why: 'Pembaruan terkontrol menjaga model belajar dari bukti yang sudah diperiksa dan memungkinkan dampaknya diuji sebelum digunakan.',
      next: 'Bandingkan hasil challenger dan periksa syarat aktivasi artifact.'
    },
    latex: [
      {title: 'Apa yang diminimalkan saat belajar?', tex: String.raw`\mathcal{L}=\mathrm{CE}_{\mathrm{cognitive}}+\mathrm{CE}_{\mathrm{knowledge}}+\mathrm{BCEWithLogits}_{\mathrm{ordinal}},\qquad \boldsymbol t=[\mathbf{1}(y>0),\mathbf{1}(y>1)]`, symbols: [{symbol: String.raw`\mathcal{L}`, meaning: 'Jumlah loss tiga head pada training.'}, {symbol: String.raw`\mathrm{CE}`, meaning: 'Cross entropy multiclass dengan class weights dari train.'}, {symbol: String.raw`\mathrm{BCEWithLogits}`, meaning: 'Binary cross entropy untuk dua batas ordinal dengan pos_weight dari train.'}, {symbol: 'y', meaning: 'Indeks intended label: Easy=0, Medium=1, Hard=2.'}, {symbol: String.raw`\boldsymbol t`, meaning: 'Target ordinal: Easy=[0,0], Medium=[1,0], Hard=[1,1].'}], why: 'Masing-masing head belajar targetnya; urutan difficulty dinyatakan melalui dua pertanyaan apakah label melewati suatu batas.'}
    ],
    input: {snapshotId: 'contoh-gold-v2', architecture: 'grade-aware-ordinal-v2', inputRepresentation: 'Dikunci manifest; metadata/solution/kko sesuai eksperimen', operatorCommand: 'python -m app.training.v2.train_lora'},
    process: [
      'Serializer menghasilkan teks dan tokenizer memakai konfigurasi yang sama dengan inference. Head cognitive/knowledge multiclass; difficulty cumulative ordinal menerima embedding grade.',
      'Class weights berasal dari train saja; ordinal target Easy=[0,0], Medium=[1,0], Hard=[1,1]. Update LoRA/head dilakukan dengan optimizer.',
      'Pilih checkpoint yang lolos anti-collapse lalu weakest-head macro-F1 dan mean macro-F1. Validation menentukan temperature dan selective confidence/entropy threshold.',
      'Per-grade calibration hanya berlaku bila support mencukupi. Frozen test tetap mengikuti unlock gate, tanpa digunakan untuk memilih calibration.',
      'Kemas adapter, heads, tokenizer, base-model files, calibration, metrics, architecture dan snapshot/split/checksum dalam direktori versi baru.'
    ],
    formula: 'L = CE_cognitive + CE_knowledge + BCEWithLogits_ordinal\nyOrdinal = [1(y > Easy), 1(y > Medium)]\nθ_model_new diperoleh optimizer pada train; bukan θ_ability siswa',
    example: 'Contoh: label intended pada v3 menjadi target ordinal [1,0] untuk Medium. Bukan memasukkan b=−1.2 ke fitur. bobot model baru baru tersedia setelah training, calibration dan packaging selesai.',
    output: {modelVersion: 'contoh-indobert-v2', datasetSnapshot: 'contoh-gold-v2', architectureVersion: 'grade-aware-ordinal-v2', calibrationVersion: 'versi baru', approvedForProvisional: false, autoRetrained: false},
    cautions: [
      'Jalur silver selalu researchOnly=true, meskipun metrik teknis lolos.',
      'Arsitektur artifact yang ada dapat parallel-v1; jangan menganggap semua diagnostik lama sudah memakai ordinal grade-aware.',
      'Parameter kemampuan θ IRT dan parameter bobot neural network adalah dua objek berbeda.'
    ],
    sources: [{path: 'app/training/v2/train_lora.py', symbol: 'ordinal_difficulty_loss / run_trial / calibration_from_validation / package_artifact'}, {path: 'app/classification/v2/model.py', symbol: 'GradeAwareOrdinalDifficultyHead / ThreeHeadIndoBERT'}]
  },
  {
    id: 'feedback-compare-promote', phase: 'Umpan balik',
    title: 'Bandingkan label lama, label baru, dan prediksi',
    subtitle: 'Tunjukkan apa yang berubah dan apakah model baru memenuhi syarat',
    status: 'conditional',
    summary: 'Label lama, label ahli yang baru dan prediksi model ditampilkan bersama asal serta versinya. Evaluasi memakai contoh yang tetap agar hasil model lama dan baru dapat dibandingkan dengan adil. Model pengganti baru dapat dilayani API setelah seluruh syarat dan persetujuan terpenuhi.',
    learning: {
      story: 'v2 dahulu berlabel Hard; setelah revisi, ahli memberi v3 label Medium. Challenger juga memprediksi Medium. Kesamaan ini perlu dicatat, tetapi peningkatan model diuji lagi pada benchmark yang tetap agar perubahan isi soal tidak disangka sebagai peningkatan model.',
      terms: [
        {term: 'Agreement / confusion', meaning: 'Jumlah label yang sama dan pola pasangan label rujukan dengan prediksi.', why: 'Menunjukkan di kelas mana model cocok atau sering tertukar.'},
        {term: 'Benchmark tetap', meaning: 'Item dan versi pengujian yang sama untuk membandingkan model.', why: 'Memisahkan efek model baru dari efek soal atau populasi yang berubah.'},
        {term: 'Promotion / servable', meaning: 'Pemeriksaan syarat dan persetujuan agar artifact boleh dilayani API.', why: 'Mencegah calon model menjadi aktif hanya karena satu angka atau contoh terlihat bagus.'}
      ],
      why: 'Perbandingan yang adil dan riwayat yang lengkap memungkinkan reviewer menilai manfaat perubahan beserta batasnya.',
      next: 'Jika semua gate terpenuhi, artifact dapat dipertimbangkan untuk aktivasi; integrasi IRT langsung tetap rancangan terpisah.'
    },
    latex: [
      {title: 'Kesamaan label pada comparison offline', tex: String.raw`A_h=\frac{\sum_{i=1}^{N}\mathbf{1}\!\left(\widehat y_{ih}=y_{ih}^{\mathrm{locked}}\right)}{N}`, symbols: [{symbol: 'A_h', meaning: 'Agreement rate untuk head h.'}, {symbol: 'N', meaning: 'Jumlah item yang dibandingkan; berbeda dari jumlah siswa IRT.'}, {symbol: String.raw`\widehat y`, meaning: 'Label prediksi model.'}, {symbol: String.raw`y^{\mathrm{locked}}`, meaning: 'Label blind silver yang sudah dikunci dalam script comparison aktif.'}], why: 'Menunjukkan konsistensi prediksi terhadap rujukan terkunci; agreement terhadap silver tetap bukan akurasi terhadap gold manusia.'},
      {title: 'Syarat artifact dapat dilayani', tex: String.raw`S=A\land\neg R\land D\land C\land P`, symbols: [{symbol: 'S', meaning: 'servable.'}, {symbol: 'A', meaning: 'approvedForProvisional.'}, {symbol: 'R', meaning: 'researchOnly.'}, {symbol: 'D', meaning: 'dataGatesPassed.'}, {symbol: 'C', meaning: 'antiCollapsePassed.'}, {symbol: 'P', meaning: 'promotionGates.passed.'}], why: 'Kualitas data, perilaku model, metrik evaluasi dan approval harus bersama-sama terpenuhi.'}
    ],
    input: {oldLabels: 'snapshot lama', newLabels: 'snapshot baru dengan provenance', incumbentPredictions: 'model versi lama', challengerPredictions: 'model versi baru'},
    process: [
      'Untuk perbandingan model yang adil, pakai item/version dan benchmark tetap, serializer/label map serta scope yang cocok. Label konten v2 dan v3 adalah sejarah revisi, bukan perubahan prediksi pada input identik.',
      'Comparison silver yang tersedia mengharuskan audit lock, SHA256 checkpoint/input match dan timestamp prediksi setelah lock; join per questionId menghasilkan agreement, confusion dan evidence per head.',
      'Agreement = label sama; disagreement tetap reviewRequired. Script comparison tidak memanggil LLM dan tidak menghasilkan gold pengganti.',
      'Promotion memeriksa macro-F1 H1/H2 ≥0.70, H3 ≥0.65; setiap class F1 ≥0.50; ECE ≤0.10; selective accuracy ≥0.80 pada coverage ≥0.70; anti-collapse/baseline dan stabilitas tiga seed.',
      'Manifest servable membutuhkan explicit approval, bukan researchOnly, data gates, anti-collapse dan promotion gates. /v2/classify mengembalikan 503 bila artifact belum servable.'
    ],
    formula: 'changedLabel(h) = oldVersionLabel(h) ≠ newVersionLabel(h), dengan provenance/versi eksplisit\nagreementRate(h) = jumlah label model = label terkunci / jumlah item dibandingkan\nservable = approvedForProvisional ∧ ¬researchOnly ∧ dataGatesPassed ∧ antiCollapsePassed ∧ promotionGates.passed',
    example: 'Contoh ilustratif: intended v2=Hard, gold v3=Medium, challenger memprediksi Medium dengan p=0.78. Gold baru berasal dari review ahli v3; p=0.78 hanya confidence model. Artifact tetap nonservable sampai semua gate dan approval terpenuhi.',
    output: {oldVersion: 'contoh:v2', oldIntendedLabel: 'Hard', newVersion: 'contoh:v3', newHumanLabel: 'Medium', challengerPrediction: 'Medium', historicalLabelsPreserved: true, automaticRelabel: false},
    cautions: [
      'Tabel perbandingan sejarah label/champion vs challenger terpadu masih workflow operator; script aktif khusus locked blind silver versus prediksi, bukan sistem auto-relabel.',
      'Kelas 7–12 pada runtime sekarang out_of_scope/abstain; jangan menganggap label null sebagai prediksi salah biasa.',
      'Tidak ada formula aktif 40% IndoBERT + 60% LLM atau confidence × IRT yang menetapkan label baru.'
    ],
    sources: [{path: 'scripts/compare_blind_labels_to_predictions.py', symbol: 'compare'}, {path: 'app/training/v2/train_lora.py', symbol: 'promotion_gate_failures'}, {path: 'app/classification/v2/artifact.py', symbol: 'ModelManifest.servable'}, {path: 'app/api/v2.py', symbol: 'runtime_or_503'}]
  },
  {
    id: 'feedback-future-irt-features', phase: 'Umpan balik',
    title: 'Rancangan fitur empiris atau pembaruan online',
    subtitle: 'Penggunaan fitur IRT atau tes adaptif perlu pengembangan berikutnya',
    status: 'planned',
    summary: 'Saat ini bukti IRT membantu proses review. Jika kelak ingin memasukkan parameter IRT ke model atau memilih soal berikutnya berdasarkan kemampuan siswa, dibutuhkan schema, model dan evaluasi tambahan. Bagian ini menjelaskan rancangan tersebut dengan status yang jelas.',
    learning: {
      story: 'Setelah bank soal memiliki calibration yang dipercaya, kita dapat merancang pembaruan kemampuan siswa setelah setiap jawaban. Kita juga dapat meneliti apakah fitur empiris membantu classifier. Kedua ide ini membutuhkan layanan dan pengujian baru sebelum menjadi perilaku sistem.',
      terms: [
        {term: 'Fusion fitur', meaning: 'Menggabungkan representasi teks dengan angka empiris yang punya provenance dan missing mask.', why: 'Memungkinkan eksperimen manfaat IRT tanpa menyembunyikan asal atau kekosongan data.'},
        {term: 'Online theta scoring', meaning: 'Memperbarui perkiraan kemampuan siswa dengan parameter item yang sudah dikalibrasi.', why: 'Dapat mendukung pemilihan soal secara bertahap dalam layanan adaptif.'},
        {term: 'CAT / calibration release', meaning: 'Tes adaptif dan izin menggunakan calibration bank item untuk tujuan tertentu.', why: 'Tes adaptif perlu bank, aturan pemilihan/penghentian dan validasi penggunaan yang sesuai.'}
      ],
      why: 'Pengetahuan tentang fitur berikutnya membantu merencanakan sistem sambil menjaga penjelasan kemampuan sekarang tetap akurat.',
      next: 'Tentukan kebutuhan eksperimen, kontrak data dan validasi penggunaan sebelum membangun integrasi.'
    },
    latex: [
      {title: 'Rancangan pembaruan kemampuan per jawaban', tex: String.raw`p_{\mathrm{new}}(\theta)\propto p_{\mathrm{old}}(\theta)\,P_j(\theta)^x\,[1-P_j(\theta)]^{1-x}`, symbols: [{symbol: String.raw`\theta`, meaning: 'Kemampuan laten siswa.'}, {symbol: 'x', meaning: 'Jawaban scored: benar=1 atau salah=0; skip tidak memberi pembaruan likelihood.'}, {symbol: 'P_j', meaning: 'Peluang benar item j dari bank calibration yang telah dilepas.'}, {symbol: String.raw`p_{\mathrm{old}},p_{\mathrm{new}}`, meaning: 'Distribusi kemampuan sebelum dan sesudah evidence baru.'}], why: 'Setiap jawaban menggeser perkiraan secara bertahap. Rumus ini rancangan; runtime online scoring/CAT belum diimplementasikan.'}
    ],
    input: {proposalOnly: true, possibleEmpiricalFeatures: ['a', 'b', 'c', 'bPosteriorSd', 'validResponseCount', 'calibrationSnapshotId', 'populationId', 'timeWindow']},
    process: [
      'Rancang schema dan fusion head tersendiri, missingness indicator serta provenance calibration; jangan mengisi b buatan ketika calibration belum tersedia.',
      'Pisahkan train/test menurut waktu dan family/populasi agar respons atau calibration dari test tidak bocor ke fitur train.',
      'Bandingkan ablation tanpa fitur IRT dengan fusion empiris pada benchmark tetap; intended difficulty dan empirical difficulty dapat memerlukan target/head berbeda.',
      'Online theta scoring membutuhkan bank calibration released, posterior update, content/exposure constraints dan stopping policy. Batch item calibration tidak otomatis menjadi CAT.',
      'Versikan release, monitoring/drift dan rollback. Tentukan kapan calibration lokal dapat digunakan lintas form/populasi melalui linking dan validasi penggunaan.'
    ],
    formula: 'Contoh rancangan saja: hFusion = concat(hCLS, gradeEmbedding, empiricalFeatures, missingMask)\nContoh rancangan saja: posterior_new(θ) ∝ posterior_old(θ) · P(item|θ)^x · [1−P(item|θ)]^(1−x)\nKode aktif: input IRT ke classifier = tidak tersedia; auto-relabel = tidak tersedia',
    example: 'Sekarang request /v2/classify dengan field tambahan b atau theta ditolak kontrak extra="forbid". Pada rancangan berikutnya, schema/model baru harus diuji terlebih dahulu; animasi bagian ini hanya menjelaskan kemungkinan integrasi.',
    output: {status: 'planned_only', currentIrtFeatureInput: false, onlineItemCalibration: false, catEngine: false, automaticRelease: false},
    cautions: [
      'Proposal ini tidak menyatakan fungsi tersebut sudah berjalan di repository.',
      'IRT yang ada tetap batch, local calibration dan research/advisory; tidak ada auto-release calibration.',
      'Profil longitudinal siswa, selector adaptif, CAT, linking/equating, DIF dan UI siswa masih target yang dijelaskan di dokumen 28.'
    ],
    sources: [{path: 'app/classification/v2/contracts.py', symbol: 'V2ClassificationRequest'}, {path: 'app/classification/v2/serializer.py', symbol: 'serialize_question'}, {path: 'API_DOCUMENTATION/28_END_TO_END_PERSONALIZED_ASSESSMENT_FLOW.md', symbol: 'G1–G4 / H3'}]
  }
];
