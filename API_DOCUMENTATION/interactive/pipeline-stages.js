/* Rubric v8 / prompt v10. Documentation only: no provider or student requests. */
(function () {
  'use strict';
  const stages = [];
  function add(id, phase, title, story, process, output, sources, options = {}) {
    stages.push({id, phase, title, subtitle: options.subtitle || title,
      status: options.status || 'conditional', summary: story,
      learning: {story, why: options.why || story, next: options.next || 'Ikuti garis berlabel untuk mengetahui syarat dan tujuan berikutnya.', terms: options.terms || []},
      input: options.input || 'Konten dan bukti versi soal yang sama.', process,
      formula: options.formula || '', example: options.example || '', output,
      cautions: options.cautions || [], sources: sources.map(path => ({path})), latex: []});
  }
  add('model-rubric-v8', 'Label AI', 'Pilih rubrik v8 sesuai kelas dan jalur',
    'Rubrik dipilih untuk SD 1–6, SMP 7/8/9, SMA reguler 10/11/12, atau TL 11/12. Prompt v10 membaca definisi langsung dari YAML.',
    ['Nilai solusi minimum relatif terhadap kesempatan belajar kelas sasaran.',
     'Easy: penerapan familiar yang langsung, sedikit keputusan, integrasi rendah.',
     'Medium: pemilihan prosedur familiar, langkah terkait atau perpindahan representasi dengan tuntutan sedang.',
     'Hard: perencanaan dan integrasi tinggi, kendala berinteraksi atau justifikasi substantif dengan sedikit bantuan. Prosedur familiar tetap dapat Hard.',
     'Applying tidak otomatis Medium; reasoning tidak otomatis Hard. Panjang soal, banyak operasi, topik lanjut dan angka besar bukan penentu tunggal.'],
    {rubric: 'math-rubric-3x4x3-v8-<kelas/track>-grade-aware', prompt: 'v10 blind-key-verified', quotaInBlindPrompt: false},
    ['app/llm/silver.py', 'configs/rubric_math_3x4x3_v8_sd.yaml', 'configs/rubric_math_3x4x3_v8_smp7.yaml', 'configs/rubric_math_3x4x3_v8_smp8.yaml', 'configs/rubric_math_3x4x3_v8_smp9.yaml', 'configs/rubric_math_3x4x3_v8_sma10.yaml', 'configs/rubric_math_3x4x3_v8_sma11.yaml', 'configs/rubric_math_3x4x3_v8_sma12.yaml', 'configs/rubric_math_3x4x3_v8_sma11_tl.yaml', 'configs/rubric_math_3x4x3_v8_sma12_tl.yaml'], {status:'implemented'});
  for (let run = 1; run <= 3; run++) add(`model-run-${run}`, 'Label AI', `Run ${run} · Gemini blind`,
    `Penilaian independen ke-${run} dari model Gemini yang sama. Reviewer tidak menerima prediksi IndoBERT, label lama, vote run lain atau kuota Easy/Medium/Hard.`,
    ['Baca soal, opsi, kelas/track dan gambar yang terlampir; verifikasi kunci dan solusi minimum.',
     'Isi tiga head, evidence spans, rationale ringkas serta profil difficulty. Classify atau abstain sesuai kecukupan bukti.',
     'Validasi JSON dengan schema; simpan prompt/response hash, status, latency dan usage. Respons gagal tidak menjadi suara.',
     'Tiga kartu menunjukkan independensi penilaian, bukan tiga model atau tiga request yang selalu berjalan bersamaan. Runner batch memakai satu worker.'],
    {runIndex:run, status:'success / failed', heads:['mathCognitiveDomain','knowledgeDimension','intendedDifficulty'], evidence:'key, minimum solution, visual transcript, difficulty profile'},
    ['app/llm/silver.py','scripts/generate_silver_labels_kelas1.py'], {status:'implemented', subtitle:'Satu dari tiga penilaian independen · eksekusi batch serial'});
  add('model-checkpoint', 'Label AI', 'Simpan checkpoint · tunggu / lanjutkan',
    'Run belum lengkap tetap draft. Semua run sukses dipertahankan dan hanya bagian yang belum berhasil yang diproses ketika resume dilakukan.',
    ['Pada 429 pertama, hentikan seluruh panggilan Gemini dan catat quota ID bila tersedia.',
     'Key/model/konfigurasi tidak sah atau batas lokal panggilan juga menghentikan batch. Tidak ada rotasi key/model otomatis.',
     'Schema/provider/network error tetap failed; retry terbatas dicatat. Jika bukti tetap kurang, status stopped_incomplete_provider_evidence.',
     'Resume memeriksa hash sumber, prompt/rubrik, model dan track. Perubahan identitas bukti memerlukan batch baru.',
     'Array progres: item belum selesai memiliki label/skor null, confidence 0 dan status inactive. Hasil aktif lama tidak diganti oleh draft.'],
    {executionStatus:'blocked_provider_daily_quota / stopped_incomplete_provider_evidence / stopped_api_call_budget', resume:'Hanya run dan adjudikasi yang belum lengkap'},
    ['scripts/revalidate_all_grades.py','scripts/generate_silver_labels_kelas1.py','scripts/export_revalidation_progress.py']);
  add('model-adjudication', 'Label AI', 'Adjudikasi AI terpisah',
    'Ketidaksepakatan, abstain atau masalah konten/kunci memerlukan keputusan baru berdasarkan soal dan bukti tiga run. Adjudikasi bukan suara keempat.',
    ['Reviewer membaca konten dan evidence tiga run tanpa prediksi IndoBERT atau target distribusi.',
     'Temperature adjudikasi 0.0; label tidak dipilih dengan mayoritas 2/3 secara otomatis.',
     'Keputusan dapat memperbarui label, status konten/kunci, solusi dan transkripsi pada agregat.',
     'Abstain atau concern tetap masuk qualification untuk ditahan; provider/schema error tetap belum lengkap.'],
    {status:'success / failed', aggregate:'adjudicated; label atau abstain', isFourthVote:false},
    ['app/llm/silver.py','scripts/generate_silver_labels_kelas1.py']);
  add('model-consensus', 'Label AI', 'Konsensus 3–0 · lanjutkan pemeriksaan',
    'Ketiga run sukses memberi label yang sama pada setiap head, dengan status konten dan kunci yang memenuhi syarat. Jalur ini tidak membutuhkan panggilan adjudikasi.',
    ['Periksa kesepakatan tiga run pada cognitive, knowledge, dan difficulty.',
     'Simpan keputusan agregasi beserta bukti run yang sudah lengkap.',
     'Lanjutkan ke pemeriksaan profil dan qualification; kesepakatan AI tidak menggantikan pemeriksaan kualitas konten.'],
    {decision:'unanimous', successfulRuns:3, adjudicationRequired:false},
    ['app/llm/silver.py'], {status:'implemented', subtitle:'3 sukses · sepakat pada ketiga head dan kunci'});
  add('model-evidence-profile', 'Label AI', 'Baca profil tuntutan difficulty',
    'Profil menunjukkan alasan tuntutan soal relatif terhadap kelas. Ini bukan skor penjumlahan yang otomatis mengubah label rubrik.',
    ['expectedPrerequisite: prasyarat yang wajar; dependentSteps: langkah yang saling bergantung.',
     'routineStatus: familiar_routine / routine_selection / nonroutine_strategy.',
     'strategySelection dan representationTransfer: keputusan strategi dan perpindahan bentuk informasi.',
     'relevantInformationUnits dan interactingConstraints: informasi relevan dan kendala yang berinteraksi.',
     'calculationLoad, scaffoldLevel, distractorQuality dan gradeRelativeRationale melengkapi bukti.',
     'Periksa apakah solusi langsung yang lebih sederhana tersedia. Kunci/gambar bermasalah adalah masalah konten, bukan alasan menaikkan difficulty.'],
    {profileFields:11, rubricCategory:'Easy / Medium / Hard berdasarkan bukti, bukan threshold jumlah operasi'},
    ['app/llm/silver.py','configs/rubric_math_3x4x3_v8_sd.yaml']);
  add('model-content-hold', 'Validasi', 'Tahan soal · revisi / AI review',
    'Soal yang tidak memenuhi qualification tetap tersimpan sebagai inactive. Jalur revisi konten berbeda dari jalur bukti AI yang belum cukup.',
    ['Struktur gagal, content concern atau konflik kunci → revision_required.',
     'Evidence tidak cukup, label abstain, kunci/solusi tidak terverifikasi atau transkripsi visual kurang → needs_ai_review.',
     'Perbaikan isi/kunci/gambar menghasilkan hash/versi konten baru, kemudian validasi blind diulang.',
     'Jangan mengaktifkan soal hanya untuk memenuhi jumlah Easy/Medium/Hard.'],
    {finalRouting:'revision_required / needs_ai_review', databaseStatus:'inactive'},
    ['app/silver/policy.py','scripts/refresh_ai_validation_reports.py']);
  add('model-ai-archive', 'Bank soal', 'Kunci dan arsipkan hasil AI asli',
    'Bundle yang sudah lengkap dan terverifikasi menjadi sumber bukti AI. Publikasi bank relatif tidak mengubah arsip ini.',
    ['Audit sumber, byte aset, prompt/rubrik, respons dan checkpoint sebelum lock.',
     'Simpan final_snapshot_v1, ai_decisions.json dan manifest checksum. qualification menentukan active/inactive.',
     'ai_validation_results.json menyimpan label blind asli byte-for-byte setelah bank operasional dipublikasikan.',
     'Training dan persiapan IRT membaca arsip AI melalui ai_validation_path, bukan label kuota.'],
    {labelProvenance:'ai_silver', originalArray:'hasil_validasi/ai_validation_results.json', decisions:'bukti_validasi/ai_decisions.json'},
    ['scripts/revalidate_all_grades.py','scripts/publish_operational_bank.py','app/silver/exports.py'], {status:'implemented'});
  add('model-operational-balance', 'Bank soal', 'Opsional · bagi bank mendekati ⅓',
    'Kebijakan bank relatif mengurutkan soal aktif dari profil bukti, lalu membagi Easy/Medium/Hard dengan selisih jumlah maksimal satu soal per kelas.',
    ['Hanya item active yang dihitung. Item inactive dipertahankan tanpa perubahan.',
     'Ranking heuristik memakai langkah terkait, familiaritas, strategi, representasi, kendala, informasi, beban hitung dan bantuan.',
     'Kuota dibagi menggunakan divmod(n,3); sisa dialokasikan Easy lalu Medium. Skor sama dapat terpisah; source order menjadi pemecah seri yang diaudit.',
     'Heuristik belum dikalibrasi terhadap siswa. Pembagian sepertiga adalah distribusi seragam, bukan distribusi normal statistik.',
     'Label memiliki provenance relative_bank_quota; bukan AI silver untuk training dan bukan parameter IRT.'],
    {labelProvenance:'relative_bank_quota', distribution:'Mendekati ⅓ per kategori untuk soal aktif setiap kelas', audit:'operational_balance_audit.json'},
    ['scripts/balance_operational_difficulty.py','scripts/publish_operational_bank.py']);
  add('model-bank-export', 'Bank soal', 'Publikasikan validation_results.json',
    'Array bank mengikuti field dan urutan soal_pretest_db.json. Isi soal dan bukti asli tetap dapat ditelusuri.',
    ['cognitive_level memakai easy/medium/hard; cognitive_score memetakan 600/1000/1400.',
     'confidence_score adalah dukungan run AI asli terendah dari tiga head terhadap label operasional. Label kuota tanpa dukungan dapat 0.',
     'Adjudikasi bukan suara tambahan; confidence ini bukan calibratedConfidence IndoBERT atau probabilitas jawaban benar.',
     'Manifest mencatat sourceFingerprint, versionDirectory dan newRubricValidationComplete. False berarti bukti aktif masih berasal dari rubrik sebelumnya.',
     'Versi immutable dan checksum diverifikasi; perubahan baru dipublikasikan hanya sesudah kelas selesai.'],
    {file:'hasil_validasi/validation_results.json', confidence:'Dukungan AI asli, dapat 0', originalEvidence:'ai_validation_results.json', activeStatus:'Qualification tetap berlaku'},
    ['scripts/publish_operational_bank.py','scripts/balance_operational_difficulty.py']);
  add('model-training-gates', 'IndoBERT', 'Semua bundle dan split memenuhi gate?',
    'Classifier baru dapat dilatih ketika seluruh 14 kelas/track terverifikasi dengan rubrik v8, lalu snapshot memenuhi cakupan dan jumlah minimum setiap label.',
    ['Verifikasi kelas 1–12 reguler dan TL 11–12: tepat tiga run sukses per item serta adjudikasi terselesaikan.',
     'Ambil label AI asli yang qualified; jangan campur label historis atau relative_bank_quota untuk menyatakan dataset v8 lengkap.',
     'Train memerlukan minimal 30 per label; validation dan test masing-masing minimal 15 per label pada setiap head.',
     'Semua 14 pasangan grade/track harus hadir di setiap split. Group sumber/duplikat/stimulus tidak boleh bocor antar-split.'],
    {readyForTraining:'true hanya jika verification dan gate data lolos', minimum:{train:30,validation:15,test:15}},
    ['scripts/prepare_allgrade_retraining.py','app/training/v2/dataset.py']);
  add('model-training-blocked', 'IndoBERT', 'Tunda training · lengkapi data',
    'Validasi belum lengkap atau kelas label kurang menghasilkan readiness report. Tidak ada model baru yang dinyatakan selesai.',
    ['Lengkapi revalidasi, tambah contoh dengan label terverifikasi, atau perbaiki split tanpa kebocoran.',
     'Bobot loss membantu ketimpangan train yang tersedia; tidak menciptakan contoh Hard/metacognitive yang tidak ada.',
     'Simpan laporan baru tanpa menimpa snapshot/readiness lama. Ulangi persiapan secara eksplisit setelah data berubah.'],
    {trainingStatus:'blocked_revalidation_incomplete / blocked_dataset_verification / blocked_quality_gates'},
    ['scripts/prepare_allgrade_retraining.py']);
  add('model-inference-gate', 'IndoBERT', 'Artifact, scope dan provenance sesuai?',
    'Kemampuan kode hingga kelas 12 tidak berarti artifact lama sudah dilatih untuk seluruh kelas. Runtime membaca scope, arsitektur dan representation dari manifest.',
    ['Endpoint publik memerlukan artifact servable yang memenuhi approval, data, anti-collapse dan promotion gate; jika tidak, HTTP 503.',
     'Artifact SD lama tetap hanya mendukung cakupannya. Grade/track di luar manifest atau provenance kurang → abstain sebelum encoder.',
     'Diagnostik offline pada kandidat research berbeda dari izin melayani inferensi publik.',
     'Grade embedding model baru memiliki 12 slot; TL menggunakan penanda teks, bukan theta siswa.'],
    {publicArtifactFailure:'HTTP 503', inputFailure:'abstain / reasons', validInput:'Lanjut serializer sesuai manifest'},
    ['app/classification/v2/runtime.py','app/classification/v2/artifact.py','configs/model_v2_config.yaml']);
  add('model-serving-blocked','IndoBERT','HTTP 503 · artifact belum servable',
    'Endpoint publik tidak melayani prediksi jika artifact belum melewati gate approval dan kualitas. Ini berbeda dari abstain akibat input di luar scope.',
    ['Periksa manifest, dataGatesPassed, antiCollapsePassed, promotionGates.passed, researchOnly dan approvedForProvisional.',
     'Kandidat research dapat dievaluasi offline; kelulusan gate dan promotion eksplisit diperlukan sebelum serving publik.'],
    {httpStatus:503,inferenceExecuted:false},['app/classification/v2/artifact.py']);
  for (const [id,title,description,output] of [
    ['model-abstain','Abstain · input tidak memenuhi gate','Scope, versi/hash atau provenance tidak sesuai: encoder belum dijalankan.',{label:null,probabilities:[],action:'abstain'}],
    ['model-review','Review · prediksi belum lolos batas','Confidence, entropy atau truncation belum memenuhi gate. Prediksi tetap advisory; review LLM bukan panggilan otomatis dari endpoint classify.',{action:'review',reviewRequired:true}],
    ['model-predict','Predict · advisory memenuhi batas','Prediksi melewati gate probabilitas dari validation, tetapi bukan bukti kunci benar atau gold ahli.',{action:'predict',reviewRequired:true}]
  ]) add(id,'IndoBERT',title,description,[description,'Simpan reasons dan model trace; bandingkan dengan bukti AI yang sudah terkunci.'],output,['app/classification/v2/runtime.py']);
  for (const [id,title,labels,extra] of [
    ['model-head-cognitive','Head 1 · domain kognitif',['knowing','applying','reasoning'],'Linear multiclass dari [CLS].'],
    ['model-head-knowledge','Head 2 · dimensi pengetahuan',['factual','conceptual','procedural','metacognitive'],'Linear multiclass dari [CLS].'],
    ['model-head-difficulty','Head 3 · intended difficulty',['Easy','Medium','Hard'],'Varian baru: [CLS] + grade embedding 16 dimensi → score dan dua ordered cutpoints.']
  ]) add(id,'IndoBERT',title,'Ketiga head berbagi representasi encoder, tetapi mempelajari keluaran yang berbeda.',
    [extra,'Difficulty bukan pemetaan otomatis dari domain atau knowledge. Arsitektur aktual dibaca dari manifest.'],{labels},['app/classification/v2/model.py'],{status:'implemented'});
  add('assessment-irt-initialization','Bank soal','Siapkan IRT · belum mengestimasi parameter',
    'Skor awal 600/1000/1400 berasal dari label AI asli. Sidecar memeriksa versi item, kelas/track serta ketersediaan respons siswa.',
    ['ai_validation_path menjaga agar label operasional tidak menjadi prior AI palsu.',
     'Simpan irt_initialization.json dan checksum; tidak menambah field pada array bank.',
     'Blueprint pilot dapat disiapkan dari snapshot qualified, tanpa membuat siswa, respons, parameter a/b/c atau theta.'],
    {scoreMapping:{Easy:600,Medium:1000,Hard:1400},parameters:null,studentAbility:null},
    ['app/psychometrics/initialization.py','scripts/prepare_allgrade_retraining.py'],{status:'implemented'});
  add('assessment-wait-responses','Bank soal','Belum ada respons · waiting_for_data',
    'Bank siap bukan berarti IRT sudah terkalibrasi. Tanpa respons nyata yang cocok, sistem hanya mencatat readiness dan kebutuhan pengumpulan data.',
    ['Pakai form qualified dengan grade/track, population, versi dan content hash yang tepat.',
     'Kumpulkan respons melalui sesi asesmen; jangan membuat parameter atau kemampuan siswa buatan.'],
    {status:'waiting_for_data',calibrated:false,parameters:null,studentAbility:null},['app/psychometrics/initialization.py']);
  add('assessment-registration-blocked','Siswa','Tolak registrasi · snapshot tidak sah',
    'Form asesmen memerlukan snapshot AI silver yang qualified serta metadata dan versi yang sesuai.',
    ['Snapshot draft, provenance relatif, checksum salah, item ditahan atau grade/track tidak cocok tidak dapat menjadi delivery silver.',
     'Perbaiki qualification/snapshot dahulu, lalu ulangi registrasi internal secara eksplisit.'],
    {delivery:'Tidak dibuat',action:'Perbaiki snapshot dan qualification'},['app/assessment/store.py']);
  add('assessment-score-rejected','Siswa','Tolak event · sesi / opsi tidak sah',
    'Server memeriksa identitas peserta, sesi, versi item dan mapping opsi. Event yang ditolak tidak menjadi respons benar/salah dalam matriks.',
    ['Gunakan participant token dan opsi opaque yang diberikan untuk sesi tersebut.',
     'Periksa idempotency, status sesi, hak akses serta konflik pilihan/version; perbaiki request sebelum mengirim kembali.'],
    {accepted:false,responseMatrix:'Tidak menambah baris respons valid'},['app/assessment/store.py']);
  add('assessment-irt-wait','Psikometrik','Gate IRT gagal · simpan alasan',
    'Sampel, coverage, variasi outcome atau bukti asumsi belum cukup: IRT tidak di-fit. CTT yang tersedia tetap dapat disimpan dalam snapshot.',
    ['Rasch: minimal 100 siswa dan 5 item; 2PL: 300/10; 3PL: 1000/20.',
     'Per item minimal 50 respons dan 5 outcome benar/salah; coverage minimal 0.70; missing per siswa maksimal 0.30.',
     'Periksa connectedness, versi/grade/track, unidimensionalitas, independensi lokal dan representativitas; ukuran sampel saja tidak cukup.',
     'Kumpulkan atau bersihkan data dan jalankan screen baru. Snapshot lama tetap immutable.'],
    {irtFit:'Tidak dijalankan',next:'Data tambahan / cleaning / review asumsi → screen baru'},['app/psychometrics/analysis.py','app/psychometrics/contracts.py']);
  for (const [id,title,story] of [
    ['feedback-retain','Pertahankan versi','Tanpa blocker kualitas: pertahankan item dan simpan bukti empiris. Intended difficulty tidak ditimpa otomatis.'],
    ['feedback-collect','Kumpulkan bukti tambahan','Evidence belum cukup atau tidak stabil: tambah respons dan jalankan screening pada window/snapshot baru.'],
    ['feedback-hold','Tahan versi · validasi AI baru','Blocker kualitas memicu empirical_ai_hold. Perbaikan konten/keputusan memerlukan versi dan qualification baru.'],
    ['feedback-promotion-blocked','Tunda promotion · kandidat tetap terpisah','Gate evaluasi/approval gagal: kandidat tidak menggantikan model aktif; simpan laporan dan evaluasi ulang secara eksplisit.']
  ]) add(id,'Umpan balik',title,story,[story,'Pertahankan histori keputusan, versi konten dan provenance.'],{affectsSilverLabels:false,automaticWeightUpdate:false},['app/assessment/store.py','app/classification/v2/artifact.py']);
  window.FLOW_PIPELINE_STAGES = stages;
})();
