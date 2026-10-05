/* Explicit edges, not the order of cards. Labels describe actual conditions. */
(function () {
  'use strict';
  const nodes = [], edges = [];
  const n = (id,row,lane=1,kind='process') => nodes.push({id,row,lane,kind});
  const e = (from,to,label,kind='pass') => edges.push({from,to,label,kind});
  n('model-source-json',1); n('model-import-version',2,1,'gate');
  n('model-rubric-v8',3); n('model-content-hold',3,2,'hold');
  n('model-blind-label',4);
  n('model-run-1',5,0,'run'); n('model-run-2',5,1,'run'); n('model-run-3',5,2,'run');
  n('model-votes-lock',6,1,'gate'); n('model-checkpoint',7,0,'hold'); n('model-consensus',7); n('model-adjudication',7,2);
  n('model-evidence-profile',8); n('model-silver-qualification',9,1,'gate');
  n('model-ai-archive',10);
  n('model-operational-balance',11,0); n('model-snapshot-split',11); n('assessment-irt-initialization',11,2);
  n('model-bank-export',12,0); n('model-training-gates',12,1,'gate'); n('assessment-wait-responses',12,2,'hold');
  n('model-training-blocked',13,0,'hold'); n('model-training-lora',13);
  n('model-serving-blocked',14,0,'hold'); n('model-inference-gate',14,1,'gate'); n('model-abstain',14,2,'hold');
  n('model-serializer',15); n('model-token-encoder',16);
  n('model-head-cognitive',17,0,'head'); n('model-head-knowledge',17,1,'head'); n('model-head-difficulty',17,2,'head');
  n('model-three-heads',18); n('model-prob-confidence',19); n('model-entropy-routing',20,1,'gate');
  n('model-predict',21); n('model-review',21,2,'hold');
  n('model-locked-comparison',22); n('model-legacy-advisory',22,2,'optional');
  n('assessment-silver-gate',23,1,'gate'); n('assessment-registration-blocked',23,2,'hold');
  n('assessment-participant-session',24); n('assessment-delivery-mapping',25);
  n('assessment-server-score',26,1,'gate'); n('assessment-score-rejected',26,2,'hold');
  n('assessment-complete-session',27); n('assessment-sample-window',28); n('assessment-clean-matrix',29);
  n('assessment-ctt-metrics',30,0); n('assessment-irt-readiness',30,1,'gate'); n('assessment-irt-wait',31,2,'hold');
  n('assessment-irt-marginal-fit',31); n('assessment-eap-diagnostics-information',32); n('assessment-snapshot-review',33);
  n('feedback-discrepancy',34); n('feedback-system-decision',35,1,'gate');
  n('feedback-retain',36,0); n('feedback-collect',36); n('feedback-hold',36,2,'hold');
  n('feedback-new-version',37,2); n('feedback-freeze',37);
  n('feedback-challenger',38); n('feedback-compare-promote',39,1,'gate');
  n('feedback-promotion-blocked',40,0,'hold'); n('feedback-future-irt-features',40,2,'optional');
  e('model-source-json','model-import-version','JSON + provenance');
  e('model-import-version','model-rubric-v8','Struktur & aset sesuai');
  e('model-import-version','model-content-hold','Tidak sesuai → revisi','fail');
  e('model-rubric-v8','model-blind-label','Kelas / track dipilih');
  for(let r=1;r<=3;r++) {e('model-blind-label',`model-run-${r}`,`Input blind · run ${r}`,'fork'); e(`model-run-${r}`,'model-votes-lock',`Bukti run ${r}`,'fork');}
  e('model-votes-lock','model-checkpoint','Run gagal / belum lengkap','wait');
  e('model-checkpoint','model-blind-label','Resume: hanya yang belum sukses','manual');
  e('model-votes-lock','model-consensus','3 sukses · 3–0 setiap head');
  e('model-consensus','model-evidence-profile','Konsensus tercatat; periksa bukti');
  e('model-votes-lock','model-adjudication','2–1 / abstain / concern','review');
  e('model-adjudication','model-evidence-profile','Keputusan adjudikasi sukses');
  e('model-adjudication','model-checkpoint','Provider / schema gagal','wait');
  e('model-evidence-profile','model-silver-qualification','Periksa bukti & keputusan');
  e('model-silver-qualification','model-ai-archive','silver_ready');
  e('model-silver-qualification','model-content-hold','revision_required / needs_ai_review','fail');
  e('model-content-hold','feedback-new-version','Perbaiki konten / keputusan','manual');
  e('model-ai-archive','model-operational-balance','Opsional: --balance-bank','optional');
  e('model-operational-balance','model-bank-export','relative_bank_quota');
  e('model-ai-archive','model-snapshot-split','Label AI asli · ai_silver');
  e('model-snapshot-split','model-training-gates','Split group-aware 70/15/15');
  e('model-training-gates','model-training-lora','14 bundle & gate data lolos');
  e('model-training-gates','model-training-blocked','Kurang label / scope / bukti','fail');
  e('model-training-blocked','model-snapshot-split','Lengkapi data lalu persiapan baru','manual');
  e('model-training-lora','model-inference-gate','Kandidat ≠ otomatis aktif');
  e('model-inference-gate','model-serializer','Manifest & input memenuhi gate');
  e('model-inference-gate','model-abstain','Scope / provenance gagal','fail');
  e('model-inference-gate','model-serving-blocked','Artifact tidak servable → HTTP 503','fail');
  e('model-serializer','model-token-encoder','Teks sesuai representation');
  for(const h of ['cognitive','knowledge','difficulty']) {e('model-token-encoder',`model-head-${h}`,'Shared [CLS]','fork');e(`model-head-${h}`,'model-three-heads','Keluaran head','fork');}
  e('model-three-heads','model-prob-confidence','Logits / ordinal log(p)');
  e('model-prob-confidence','model-entropy-routing','Temperature dari validation');
  e('model-entropy-routing','model-predict','Batas probabilitas lolos');
  e('model-entropy-routing','model-review','Batas gagal / truncation','review');
  e('model-predict','model-locked-comparison','Diagnostik setelah blind lock');
  e('model-review','model-locked-comparison','Catat action & reasons','review');
  e('model-locked-comparison','model-legacy-advisory','Opt-in: anchored legacy','optional');
  e('model-ai-archive','assessment-irt-initialization','AI priors + versi item');
  e('assessment-irt-initialization','assessment-wait-responses','Respons cocok belum tersedia','wait');
  e('model-ai-archive','assessment-silver-gate','Snapshot qualified; tidak menunggu classifier','manual');
  e('assessment-silver-gate','assessment-participant-session','Snapshot sah + registrasi internal');
  e('assessment-silver-gate','assessment-registration-blocked','Provenance / checksum / scope gagal','fail');
  e('assessment-registration-blocked','model-silver-qualification','Perbaiki dan verifikasi ulang','manual');
  e('assessment-participant-session','assessment-delivery-mapping','Participant token + sesi');
  e('assessment-delivery-mapping','assessment-server-score','Jawaban dengan opsi opaque');
  e('assessment-server-score','assessment-complete-session','Event sah → persist');
  e('assessment-server-score','assessment-score-rejected','Sesi / opsi / akses tidak sah','fail');
  e('assessment-score-rejected','assessment-delivery-mapping','Perbaiki request; jangan fabrikasi skor','manual');
  e('assessment-complete-session','assessment-sample-window','Sesi selesai + screen eksplisit','manual');
  e('assessment-sample-window','assessment-clean-matrix','Satu attempt per peserta / window');
  e('assessment-clean-matrix','assessment-ctt-metrics','Matriks valid untuk CTT','fork');
  e('assessment-clean-matrix','assessment-irt-readiness','Matriks + review asumsi','fork');
  e('assessment-irt-readiness','assessment-irt-marginal-fit','Sampel & asumsi memenuhi');
  e('assessment-irt-readiness','assessment-irt-wait','Gate / bukti asumsi belum cukup','wait');
  e('assessment-irt-wait','assessment-sample-window','Data tambahan → screen baru','manual');
  e('assessment-irt-marginal-fit','assessment-eap-diagnostics-information','Parameter fit + diagnostics');
  e('assessment-eap-diagnostics-information','assessment-snapshot-review','EAP & ketidakpastian','fork');
  e('assessment-ctt-metrics','assessment-snapshot-review','CTT disimpan meski IRT belum fit','fork');
  e('assessment-irt-wait','assessment-snapshot-review','Simpan alasan gate','wait');
  e('assessment-snapshot-review','feedback-discrepancy','Bukti empiris terpisah');
  e('feedback-discrepancy','feedback-system-decision','Policy tindak lanjut');
  e('feedback-system-decision','feedback-retain','Tanpa blocker kualitas');
  e('feedback-system-decision','feedback-collect','Evidence belum cukup','wait');
  e('feedback-system-decision','feedback-hold','Blocker kualitas','fail');
  e('feedback-collect','assessment-sample-window','Window berikutnya','manual');
  e('feedback-hold','feedback-new-version','Revisi + histori keputusan');
  e('feedback-new-version','model-rubric-v8','Hash / versi baru → blind N=3 ulang','manual');
  e('model-ai-archive','feedback-freeze','Jika batch baru telah qualified','optional');
  e('feedback-freeze','feedback-challenger','Job training baru + gate data','manual');
  e('feedback-challenger','feedback-compare-promote','Validation, calibration, test & approval');
  e('feedback-compare-promote','feedback-promotion-blocked','Gate / approval gagal','fail');
  e('feedback-compare-promote','model-inference-gate','Lolos gate & promotion eksplisit','manual');
  e('feedback-compare-promote','feedback-future-irt-features','Fitur empiris / online: rancangan','optional');
  const start=['model-source-json','model-import-version','model-rubric-v8','model-blind-label','model-run-1','model-run-2','model-run-3','model-votes-lock'];
  const qualified=['model-consensus','model-evidence-profile','model-silver-qualification','model-ai-archive'];
  const students=['assessment-silver-gate','assessment-participant-session','assessment-delivery-mapping','assessment-server-score','assessment-complete-session','assessment-sample-window','assessment-clean-matrix','assessment-ctt-metrics','assessment-irt-readiness'];
  const routes=[
    {id:'bank',name:'Label AI → bank operasional',stages:[...start,...qualified,'model-operational-balance','model-bank-export']},
    {id:'adjudication',name:'Label berbeda → adjudikasi',stages:[...start,'model-adjudication',...qualified.slice(1)]},
    {id:'incomplete',name:'Run belum lengkap → checkpoint',stages:[...start,'model-checkpoint']},
    {id:'content',name:'Konten gagal → revisi',stages:['model-source-json','model-import-version','model-content-hold','feedback-new-version','model-rubric-v8']},
    {id:'training',name:'AI asli → training IndoBERT',stages:[...start,...qualified,'model-snapshot-split','model-training-gates','model-training-lora','model-inference-gate','model-serializer','model-token-encoder','model-head-cognitive','model-head-knowledge','model-head-difficulty','model-three-heads','model-prob-confidence','model-entropy-routing','model-predict','model-locked-comparison']},
    {id:'training-blocked',name:'Data kurang → tunda training',stages:[...start,...qualified,'model-snapshot-split','model-training-gates','model-training-blocked']},
    {id:'irt',name:'Siswa → CTT dan IRT siap',stages:[...start,...qualified,...students,'assessment-irt-marginal-fit','assessment-eap-diagnostics-information','assessment-snapshot-review','feedback-discrepancy','feedback-system-decision','feedback-retain']},
    {id:'irt-wait',name:'Siswa → gate IRT belum cukup',stages:[...start,...qualified,...students,'assessment-irt-wait','assessment-snapshot-review','feedback-discrepancy','feedback-system-decision','feedback-collect']}
  ];
  window.FLOW_GRAPH={nodes,edges,routes};
})();
