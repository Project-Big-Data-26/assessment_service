/* Offline documentation player. All examples are pedagogical, no network IO. */
(function () {
  'use strict';
  const $ = id => document.getElementById(id);
  const esc = text => String(text ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const data = [...(window.FLOW_MODEL_STAGES || []), ...(window.FLOW_ASSESSMENT_STAGES || []), ...(window.FLOW_FEEDBACK_STAGES || [])];
  const M = window.FlowMath, Q = window.FlowQuadrature, E = window.FlowExplain;
  const statusText = {implemented:'KODE TERSEDIA',conditional:'BERSYARAT / GATE',planned:'RANCANGAN'};
  let current = 0, playing = false, timer = null, filter = 'Semua', expanded = false, copyStatusTimer = null;
  const phases = [...new Set(data.map(s => s.phase))];
  const serial = value => typeof value === 'string' ? value : JSON.stringify(value, null, 2);
  const badge = stage => `<span class="status-pill ${esc(stage.status)}">${statusText[stage.status] || esc(stage.status)}</span>`;
  const branchLabels = {'model-silver-qualification':'QUALIFICATION SILVER', 'model-legacy-advisory':'CABANG OPSIONAL', 'assessment-silver-gate':'SILVER QUALIFIED', 'feedback-future-irt-features':'RANCANGAN'};
  function branchNote(stage) {
    const notes = {
      'model-silver-qualification':'<b>Qualification:</b> sistem memeriksa bukti dan konten sebelum snapshot silver dipakai.',
      'model-legacy-advisory':'<b>Cabang legacy opsional:</b> review yang melihat prediksi ada untuk reproduksi historis. Pipeline blind aktif berhenti pada comparison diagnostik setelah lock; tahap anchored ini bukan tahap wajib.',
      'assessment-silver-gate':'<b>Sambungan aktif:</b> registrasi snapshot silver menghubungkan soal qualified ke delivery siswa, tanpa menunggu kesiapan classifier baru.'
    };
    return notes[stage.id] ? `<p class="bridge-note">${notes[stage.id]}</p>` : '';
  }
  function sourceLink(source) {
    // Only local repository paths are allowed in the source data files.
    const path = source.path;
    if (!/^[a-zA-Z0-9_./-]+$/.test(path) || path.includes('..')) return esc(path);
    return `<a href="../${esc(path)}" target="_blank" rel="noopener">${esc(path)}${source.symbol ? ' · '+esc(source.symbol) : ''}</a>`;
  }
  function stageBody(stage) {
    const learning=stage.learning;
    return `<div class="stage-content"><p class="summary">${esc(learning?.story || stage.summary)}</p>
      ${learning?`<section class="why-card"><h3>Mengapa tahap ini diperlukan?</h3><p>${esc(learning.why)}</p></section><h3>Istilahnya berarti apa?</h3>${E.terms(learning.terms)}`:''}
      ${stage.example?`<h3>Bayangkan contoh berikut</h3><p class="example">${esc(stage.example)}</p>`:''}
      ${stage.latex?.length?`<h3>Rumus, arti simbol, dan alasannya</h3>${stage.latex.map(E.formula).join('')}`:''}
      ${learning?`<div class="next-stage"><b>Setelah tahap ini…</b><p>${esc(learning.next)}</p></div>`:''}
      <details class="technical-detail"><summary>Buka detail teknis: input, proses, dan output</summary>
        <h3>Input / format data</h3><pre>${esc(serial(stage.input))}</pre>
        <h3>Langkah implementasi</h3><ol>${stage.process.map(p=>`<li>${esc(p)}</li>`).join('')}</ol>
        ${stage.formula?`<details class="implementation-rule"><summary>Catatan aturan dalam implementasi</summary><pre>${esc(stage.formula)}</pre></details>`:''}
        <h3>Output / format hasil</h3><pre>${esc(serial(stage.output))}</pre>
      </details>
      ${stage.cautions.length?`<div class="cautions"><h3>Hal yang perlu dibaca bersama hasilnya</h3><ul>${stage.cautions.map(c=>`<li>${esc(c)}</li>`).join('')}</ul></div>`:''}
      <h3>Rujukan fungsi di kode</h3><div class="sources">${stage.sources.map(sourceLink).join('')}</div></div>`;
  }
  function drawConnectors() {
    const board = $('flow-board'), svg = $('connectors');
    if (!board.offsetWidth) return;
    const origin = board.getBoundingClientRect(), nodes = [...document.querySelectorAll('.node')];
    svg.setAttribute('viewBox', `0 0 ${origin.width} ${origin.height}`);
    svg.innerHTML = '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#aabfc1"/></marker></defs>';
    nodes.forEach((node,i) => {
      if (i === 0) return;
      const a = nodes[i-1].getBoundingClientRect(), b = node.getBoundingClientRect();
      let d;
      if (Math.abs(a.top-b.top) < 3) {
        const x1 = a.right-origin.left, y = a.top-origin.top+a.height/2, x2=b.left-origin.left;
        d = `M ${x1} ${y} L ${x2} ${y}`;
      } else {
        const x1 = a.left-origin.left+a.width/2, y1 = a.bottom-origin.top;
        const x2 = b.left-origin.left+b.width/2, y2 = b.top-origin.top, mid = (y1+y2)/2;
        d = `M ${x1} ${y1} L ${x1} ${mid} L ${x2} ${mid} L ${x2} ${y2}`;
      }
      const boundary = data[i].phase !== data[i-1].phase || !!branchLabels[data[i].id];
      const path = document.createElementNS('http://www.w3.org/2000/svg','path');
      path.setAttribute('d',d); path.setAttribute('class',`connector${boundary?' boundary':''}${i===current?' active':''}`); path.setAttribute('marker-end','url(#arrow)'); svg.append(path);
      if (i===current && playing && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        const circle = document.createElementNS('http://www.w3.org/2000/svg','circle');
        circle.setAttribute('r','3.5');circle.setAttribute('class','flow-particle');
        const motion=document.createElementNS('http://www.w3.org/2000/svg','animateMotion');
        motion.setAttribute('dur','1.4s');motion.setAttribute('repeatCount','indefinite');motion.setAttribute('path',d);
        circle.append(motion);svg.append(circle);
      }
    });
  }
  function select(index, fromManual = true) {
    current = Math.max(0,Math.min(data.length-1,index));
    const stage = data[current];
    document.querySelectorAll('.node').forEach((node,i) => {
      node.classList.toggle('active',i===current);node.classList.toggle('visited',i<current);
      node.classList.toggle('dimmed',filter!=='Semua' && data[i].phase!==filter);
      node.setAttribute('aria-pressed',i===current?'true':'false');
    });
    $('stage-detail').innerHTML = `<div class="detail-heading"><span class="phase-label">${String(current+1).padStart(2,'0')} / ${esc(stage.phase)}</span>${badge(stage)}</div><h2>${esc(stage.title)}</h2><p class="subtitle">${esc(stage.subtitle)}</p>${branchNote(stage)}${stageBody(stage)}`;
    $('step-counter').textContent=`${current+1} / ${data.length} tahap · ${stage.phase}`;
    $('progress').style.width=`${(current+1)/data.length*100}%`;
    $('previous').disabled = current===0; $('next').disabled=current===data.length-1;
    drawConnectors();
    if (fromManual && playing) schedule();
  }
  function schedule() {
    clearTimeout(timer);
    if (!playing) return;
    timer=setTimeout(()=>{if(current===data.length-1){setPlaying(false);return;}select(current+1,false);schedule();},Number($('speed').value));
  }
  function setPlaying(value) {
    playing=value;document.body.classList.toggle('is-playing',value);
    $('play').textContent=value?'Ⅱ Jeda':'▶ Putar';$('play').setAttribute('aria-label',value?'Jeda animasi':'Putar animasi');
    drawConnectors();schedule();
  }
  function setView(name) {
    if(name!=='flow')setPlaying(false);
    document.querySelectorAll('[data-view]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.view===name?'true':'false'));
    ['flow','lab','summary','reference'].forEach(view=>$('view-'+view).hidden=view!==name);
    document.body.classList.toggle('printing-summary', name==='summary');
    if(name==='flow')requestAnimationFrame(drawConnectors);
  }
  function runCalculator(id, fn) {
    try { $(id).removeAttribute('role');fn(); }
    catch(error) {$(id).setAttribute('role','alert');$(id).textContent=error.message;}
  }
  function read(id, min=-Infinity,max=Infinity,integer=false) {
    const raw=$(id).value.trim(), value=raw===''?NaN:Number(raw);
    if (!Number.isFinite(value)||value<min||value>max||(integer&&!Number.isInteger(value))) throw new RangeError(`Input ${id}: nilai ${integer?'bulat ':''}antara ${min} dan ${max} diperlukan.`);
    return value;
  }
  const f=(v,n=5)=>(Math.abs(Number(v))<.5*10**(-n)?0:Number(v)).toFixed(n);
  function labResult(id, cards, rows, notes=[]) {
    $(id).innerHTML=cards.map(E.formula).join('')+E.metrics(rows)+notes.map(note=>`<p class="calculation-note">${esc(note)}</p>`).join('');
  }
  function classification() {runCalculator('classification-result',()=>{
    const logits=['logit-easy','logit-medium','logit-hard'].map(id=>read(id,-20,20)), t=read('temperature',.05,10);
    const p=M.softmax(logits,t), decision=M.route(p,read('confidence-floor',0,1),read('entropy-ceiling',0,1),$('routing').value);
    const labels=['Easy','Medium','Hard'],winner=labels[p.indexOf(Math.max(...p))];
    $('probability-bars').innerHTML=p.map((v,i)=>`<div class="probability-row"><span>${labels[i]}</span><div class="probability-track"><div style="width:${v*100}%"></div></div><span>${f(v*100,2)}%</span></div>`).join('');
    labResult('classification-result',[
      {title:'1. Ubah skor mentah menjadi probabilitas',tex:String.raw`\begin{aligned}p_k&=\frac{\exp(z_k/T)}{\sum_{\ell=1}^{K}\exp(z_\ell/T)}\\ \mathbf{z}/T&=[${logits.map(v=>f(v/t,3)).join(', ')}]\\ \mathbf{p}&=[${p.map(v=>f(v)).join(', ')}]\end{aligned}`,symbols:[{symbol:String.raw`z_k`,meaning:'Skor mentah untuk label k; bukan probabilitas.'},{symbol:String.raw`T`,meaning:'Temperature, pengatur ketajaman probabilitas. Dipilih menggunakan validation.'},{symbol:String.raw`K`,meaning:'Jumlah kategori; di contoh ini ada tiga: Easy, Medium, Hard.'}],why:'Softmax membuat setiap nilai berada antara 0 dan 1 dan totalnya menjadi 1. Skor antarlabel kemudian dapat dibandingkan. Temperature mengubah ketajaman keyakinan tanpa memilih label berdasarkan skor yang tidak sebanding.'},
      {title:'2. Baca keyakinan dan penyebaran pilihan',tex:String.raw`\begin{aligned}C&=\max_k p_k=${f(decision.confidence)}\\ H_{\mathrm{norm}}&=-\frac{\sum_{k=1}^{K}p_k\ln p_k}{\ln K}\\ &=${f(decision.entropy)}\end{aligned}`,symbols:[{symbol:String.raw`C`,meaning:'Confidence: probabilitas label yang paling tinggi.'},{symbol:String.raw`H_{\mathrm{norm}}`,meaning:'Entropy ternormalisasi: mendekati 0 jika pilihan terkonsentrasi, mendekati 1 jika merata.'},{symbol:String.raw`\ln K`,meaning:'Entropy maksimum untuk K kategori; pembagi ini menyamakan skala menjadi 0–1.'}],why:'Confidence memeriksa pilihan teratas. Entropy juga memperhatikan seluruh distribusi, sehingga dapat membantu menandai model yang membagi probabilitasnya ke banyak pilihan.'}
    ],[{label:'Label dengan probabilitas tertinggi',value:winner,key:'label'},{label:'Confidence',value:f(decision.confidence),key:'confidence'},{label:'Entropy',value:f(decision.entropy),key:'entropy'},{label:'Tindakan dari batas contoh',value:decision.action==='predict'?'predict: probability gate memenuhi batas contoh':'review: hasil perlu ditinjau',key:'action'},{label:'Alasan dari runtime',value:decision.reasons.join(', ')||'Tidak ada pelanggaran batas contoh.',key:'reasons'}],['Confidence dan entropy adalah hasil setelah inferensi. Entropy rendah maupun confidence tinggi belum membuktikan bahwa label benar.','reviewRequired = true: kontrak klasifikasi tetap berupa usulan untuk ditinjau.']);
  });}
  function ordinal() {runCalculator('ordinal-result',()=>{
    const s=read('ordinal-score',-10,10),t1=read('ordinal-first',-10,10), gap=read('ordinal-gap',-10,10);
    const r=M.ordinal(s,t1,gap), calibrated=M.softmax(r.probabilities.map(Math.log),read('temperature',.05,10));
    labResult('ordinal-result',[
      {title:'1. Jaga kedua batas tetap berurutan',tex:String.raw`\begin{aligned}t_2&=t_1+\ln(1+e^g)+10^{-4}\\ &= ${f(r.second)}\end{aligned}`,symbols:[{symbol:String.raw`g`,meaning:'Parameter yang dipelajari untuk mengatur jarak kedua batas.'},{symbol:String.raw`\ln(1+e^g)`,meaning:'Softplus: menghasilkan nilai positif agar batas kedua tidak mendahului batas pertama.'}],why:'Easy, Medium, dan Hard mempunyai urutan. Jarak yang positif membuat batas antar kategori ikut mempertahankan urutan itu.'},
      {title:'2. Bentuk probabilitas tiap kategori',tex:String.raw`\begin{aligned}q_1&=\sigma(s-t_1)=${f(r.q1)}\\ q_2&=\sigma(s-t_2)=${f(r.q2)}\\ p_{\mathrm{Easy}}&=1-q_1\\ p_{\mathrm{Medium}}&=q_1-q_2\\ p_{\mathrm{Hard}}&=q_2\end{aligned}`,symbols:[{symbol:String.raw`s`,meaning:'Skor soal dari representasi teks dan embedding kelas.'},{symbol:String.raw`\sigma(u)`,meaning:'Sigmoid: mengubah skor u menjadi nilai 0–1.'},{symbol:String.raw`q_1,q_2`,meaning:'Peluang berada di atas batas Easy dan di atas batas Medium.'}],why:'Selisih dua peluang kumulatif memberi probabilitas Medium, yaitu wilayah di antara kedua batas.'}
    ],[{label:'Probabilitas sebelum temperature',value:r.probabilities.map(v=>f(v)).join(' / '),key:'raw'},{label:'Probabilitas setelah temperature',value:calibrated.map(v=>f(v)).join(' / '),key:'calibrated'},{label:'Entropy setelah kalibrasi',value:f(M.entropy(calibrated)),key:'entropy'}]);
  });}
  function snapshot() {runCalculator('snapshot-result',()=>{
    const n=read('sample-count',0,10000,true),eligible=read('eligible-count',0,10000,true),j=read('item-count',1,200,true),cov=read('coverage',0,1),rate=read('correct-rate',0,1);
    if(eligible>n)throw new RangeError('N_fit tidak dapat melebihi N_selected.');
    const model=$('irt-model').value, minN={rasch:100,'2pl':300,'3pl':1000}[model],minJ={rasch:5,'2pl':10,'3pl':20}[model];
    const valid=Math.floor(eligible*cov),r=Math.round(valid*rate);
    const failures=[];
    if(eligible<minN)failures.push(`N_fit < ${minN}`);if(j<minJ)failures.push(`J < ${minJ}`);
    if(cov<.7)failures.push('fit coverage < 70%');
    if(valid<50)failures.push('respons/item < 50');if(r<5||valid-r<5)failures.push('benar atau salah/item < 5');
    if(!$('assumptions').checked)failures.push('asumsi belum direview');
    const ci=valid>0?M.wilson(r,valid):null;
    labResult('snapshot-result',[
      {title:'1. Hitung siswa yang datanya cukup lengkap',tex:String.raw`\begin{aligned}r_i&=\frac{\text{item terjawab valid oleh siswa }i}{J}\\ N_{\mathrm{fit}}&=\sum_{i=1}^{N_{\mathrm{selected}}}\mathbf{1}(r_i\geq 0.70)\end{aligned}`,symbols:[{symbol:String.raw`J`,meaning:'Jumlah item pada form asesmen.'},{symbol:String.raw`r_i`,meaning:'Proporsi jawaban valid milik siswa i.'},{symbol:String.raw`\mathbf{1}(\cdot)`,meaning:'Bernilai 1 jika syarat terpenuhi, 0 jika tidak; penjumlahannya menghitung siswa eligible.'}],why:'Setiap peserta dipilih satu kali, lalu kelengkapan jawabannya diperiksa. Jumlah peserta unik saja belum menjamin ada cukup bukti untuk mengestimasi kemampuan dan karakteristik soal.'},
      {title:'2. Pendekatan jumlah respons per item pada contoh',tex:String.raw`n_j\approx\left\lfloor N_{\mathrm{fit}}\times\mathrm{coverage}\right\rfloor=${valid}`,symbols:[{symbol:String.raw`n_j`,meaning:'Jumlah jawaban valid pada item j. Di data nyata nilainya bisa berbeda antaritem.'},{symbol:String.raw`\lfloor\cdot\rfloor`,meaning:'Pembulatan ke bawah untuk pendekatan homogen di panel ini.'}],why:'Panel hanya memakai ringkasan agregat. Rumus pendekatan ini membantu melihat efek pertambahan peserta, tetapi tidak menggantikan pemeriksaan matriks jawaban sebenarnya.'}
    ],[{label:'Model dan minimum sampel',value:`${model}: N_fit ≥ ${minN}, J ≥ ${minJ}`},{label:'Peserta unik terpilih (N_selected)',value:n,key:'selected'},{label:'Siswa lolos cleaning (N_fit)',value:eligible,key:'eligible'},{label:'Baris yang dikeluarkan',value:n-eligible},{label:'Jawaban valid per item, pendekatan',value:valid},{label:'Benar / salah per item, contoh',value:`${r} / ${valid-r}`},{label:'Coverage pada matriks fit',value:`${f(cov*100,1)}%`},{label:'Proporsi benar dan Wilson CI95 contoh',value:ci?`${f(ci.p)}; [${f(ci.low)}, ${f(ci.high)}]`:'Belum ada respons valid.'},{label:'Syarat agregat contoh',value:failures.length?'Belum memenuhi':'Terindikasi memenuhi; readiness backend belum dinilai',key:'status'},{label:'Syarat yang belum terpenuhi',value:failures.join('; ')||'Tetap perlu pemeriksaan matriks lengkap.'}],['N_fit tidak dapat disimpulkan dari coverage rata-rata; nilainya dimasukkan sesudah cleaning. Matriks nyata tetap harus diperiksa per siswa, per item, keterhubungan item, dan asumsi model.']);
  });}
  function chart(theta,a,b,c) {
    const svg=$('icc-chart'),width=560,height=255,left=52,right=22,top=22,bottom=43;
    const x=v=>left+(v+3)/6*(width-left-right),y=v=>height-bottom-v*(height-top-bottom);
    const points=Array.from({length:121},(_,i)=>{const th=-3+i*.05;return`${i?'L':'M'}${f(x(th),2)},${f(y(M.irt(th,a,b,c).p),2)}`;}).join(' ');
    const p=M.irt(theta,a,b,c).p;
    svg.innerHTML=`<rect x="${left}" y="${top}" width="${width-left-right}" height="${height-top-bottom}" fill="white" stroke="#dce4e6"/>${[0,.25,.5,.75,1].map(v=>`<line x1="${left}" x2="${width-right}" y1="${y(v)}" y2="${y(v)}" stroke="#edf0f1"/><text x="${left-9}" y="${y(v)+4}" font-size="11" text-anchor="end" fill="#59697b">${f(v,2)}</text>`).join('')}${[-3,-2,-1,0,1,2,3].map(v=>`<text x="${x(v)}" y="${height-bottom+18}" font-size="11" text-anchor="middle" fill="#59697b">${v}</text>`).join('')}<text x="${width/2}" y="${height-6}" font-size="12" text-anchor="middle" fill="#172638">Kemampuan θ (skala lokal N(0,1))</text><text transform="translate(13 ${height/2}) rotate(-90)" font-size="12" text-anchor="middle" fill="#172638">P(jawaban benar)</text><path d="${points}" fill="none" stroke="#087b64" stroke-width="3"/><line x1="${x(theta)}" x2="${x(theta)}" y1="${top}" y2="${height-bottom}" stroke="#6b90b7" stroke-dasharray="4 4"/><circle cx="${x(theta)}" cy="${y(p)}" r="5" fill="#2463b2"/><text x="${x(theta)+ (theta>1?-10:10)}" y="${Math.max(top+12,y(p)-10)}" font-size="12" text-anchor="${theta>1?'end':'start'}" fill="#2463b2">${f(p,3)}</text>`;
  }
  function irt() {runCalculator('irt-result',()=>{
    const th=read('theta',-3,3),a=read('irt-a',.2,4),b=read('irt-b',-5,5),c=read('irt-c',0,.35),r=M.irt(th,a,b,c);
    $('theta-value').textContent=f(th,2);chart(th,a,b,c);
    labResult('irt-result',[
      {title:'1. Hitung peluang siswa menjawab benar',tex:String.raw`\begin{aligned}P(\theta)&=c+\frac{1-c}{1+\exp[-a(\theta-b)]}\\ &=${f(c,2)}+${f(1-c,2)}\,\sigma(${f(a*(th-b),3)})\\ &=${f(r.p)}\end{aligned}`,symbols:[{symbol:String.raw`\theta`,meaning:'Kemampuan siswa pada skala kalibrasi lokal.'},{symbol:String.raw`b`,meaning:'Kesulitan item; makin besar, makin tinggi kemampuan yang diperlukan.'},{symbol:String.raw`a`,meaning:'Daya pembeda atau kemiringan hubungan kemampuan dengan peluang benar.'},{symbol:String.raw`c`,meaning:'Batas bawah peluang benar. Pada Rasch dan 2PL nilainya 0.'}],why:'Selisih kemampuan dan kesulitan menjelaskan mengapa satu soal memberi peluang benar berbeda untuk siswa yang berbeda. Bentuk sigmoid menjaga peluang tetap antara batas bawah c dan 1.'},
      {title:'2. Ukur informasi yang diberikan item',tex:String.raw`\begin{aligned}L&=\sigma[a(\theta-b)]\\ P'(\theta)&=(1-c)aL(1-L)\\ I_j(\theta)&=\frac{[P'_j(\theta)]^2}{P_j(\theta)[1-P_j(\theta)]}\\ &=${f(r.information)}\end{aligned}`,symbols:[{symbol:String.raw`P'(\theta)`,meaning:'Perubahan peluang benar ketika kemampuan berubah sedikit.'},{symbol:String.raw`I_j(\theta)`,meaning:'Informasi pengukuran yang diberikan item j pada kemampuan tersebut.'}],why:'Item lebih informatif ketika perbedaan kemampuan menghasilkan perubahan peluang benar yang jelas. Informasi bergantung pada titik kemampuan, sehingga satu soal tidak sama informatifnya untuk semua siswa.'}
    ],[{label:'Peluang benar',value:`${f(r.p*100,2)}%`,key:'probability'},{label:'Informasi item pada θ pilihan',value:f(r.information),key:'information'},{label:'Kategori kesulitan empiris dari b',value:M.empiricalDifficulty(b)},{label:'Peluang ketika θ = b',value:f((1+c)/2)}],['Parameter di sini adalah contoh yang Anda tentukan. Di backend, a/b/c diestimasi bersama dari matriks jawaban setelah syarat data dan asumsi terpenuhi.']);
  });}
  const exampleItems=[-1,-.5,0,.5,1].map(b=>({a:1,b,c:0}));
  function eap() {runCalculator('eap-result',()=>{
    const answers=exampleItems.map((_,i)=>$('response-'+i).value==='null'?null:Number($('response-'+i).value));
    const r=M.eap(exampleItems,answers,Q);
    const information=exampleItems.reduce((sum,item,i)=>sum+(answers[i]!==null?M.irt(r.mean,item.a,item.b,item.c).information:0),0);
    labResult('eap-result',[
      {title:'1. Perbarui keyakinan menggunakan jawaban',tex:String.raw`\begin{aligned}L_i(\theta_q)&=\prod_{j\in O_i}P_j(\theta_q)^{x_{ij}}[1-P_j(\theta_q)]^{1-x_{ij}}\\ w_{iq}&=\frac{v_qL_i(\theta_q)}{\sum_{\ell=1}^{41}v_\ell L_i(\theta_\ell)}\end{aligned}`,symbols:[{symbol:String.raw`O_i`,meaning:'Item yang memiliki jawaban valid dari siswa i; missing tidak ikut dikalikan.'},{symbol:String.raw`x_{ij}`,meaning:'Skor 1 untuk benar atau 0 untuk salah.'},{symbol:String.raw`v_q`,meaning:'Bobot awal pada titik kemampuan q dari prior N(0,1) dan quadrature.'},{symbol:String.raw`w_{iq}`,meaning:'Bobot posterior setelah pola jawaban diperhitungkan; seluruh bobot berjumlah 1.'}],why:'Setiap jawaban menaikkan bobot kemampuan yang lebih cocok dengan pola tersebut. Nilai awal dan likelihood jawaban digabung, kemudian dinormalisasi agar bisa digunakan sebagai distribusi.'},
      {title:'2. Ambil rata-rata kemampuan dan ketidakpastiannya',tex:String.raw`\begin{aligned}\widehat\theta_{\mathrm{EAP},i}&=\sum_{q=1}^{41}w_{iq}\theta_q=${f(r.mean)}\\ \mathrm{SD}_{\mathrm{post},i}&=\sqrt{\sum_{q=1}^{41}w_{iq}\theta_q^2-\widehat\theta_{\mathrm{EAP},i}^{\,2}}\\ &=${f(r.sd)}\end{aligned}`,symbols:[{symbol:String.raw`\widehat\theta_{\mathrm{EAP},i}`,meaning:'Rata-rata kemampuan menurut distribusi posterior siswa i.'},{symbol:String.raw`\mathrm{SD}_{\mathrm{post},i}`,meaning:'Simpangan baku posterior; menunjukkan seberapa lebar kemungkinan kemampuan yang masih masuk akal.'}],why:'Satu angka kemampuan tidak menunjukkan seberapa banyak bukti pendukungnya. Rata-rata memberi estimasi, sementara simpangan baku menjelaskan ketidakpastian hasil.'},
      {title:'3. Bedakan informasi tes dari SD posterior',tex:String.raw`\begin{aligned}I_{\mathrm{test}}(\theta)&=\sum_{j\in O_i}I_j(\theta)\\ \mathrm{SE}_{\mathrm{info}}(\theta)&\approx\frac{1}{\sqrt{I_{\mathrm{test}}(\theta)}}\end{aligned}`,symbols:[{symbol:String.raw`I_{\mathrm{test}}`,meaning:'Jumlah informasi item yang dijawab pada contoh ini.'},{symbol:String.raw`\mathrm{SE}_{\mathrm{info}}`,meaning:'Pendekatan kesalahan pengukuran berbasis informasi, bukan SD posterior.'}],why:'Informasi menjelaskan kepekaan item pada kemampuan tertentu. SD posterior menjelaskan penyebaran distribusi kemampuan setelah prior dan seluruh jawaban digabung; keduanya tidak harus sama.'}
    ],[{label:'Pola jawaban contoh',value:JSON.stringify(answers)},{label:'Item terjawab',value:r.answered,key:'answered'},{label:'Estimasi kemampuan EAP',value:f(r.mean),key:'eap'},{label:'Simpangan baku posterior',value:f(r.sd),key:'posterior-sd'},{label:'Informasi pada EAP',value:f(information)},{label:'SE berbasis informasi',value:information>0?f(1/Math.sqrt(information)):'Tidak terdefinisi: tidak ada item terjawab.'}], [r.answered===0?'Tanpa jawaban valid, posterior kembali ke prior N(0,1). Backend mengeluarkan baris tanpa jawaban dari fitting.':'Parameter soal tetap pada panel ini. Backend menghitung EAP setelah mengestimasi item dari snapshot, bukan otomatis setiap kali respons masuk.']);
    $('eap-table').innerHTML=`<table><thead><tr><th>θq</th><th>Bobot prior vq</th><th>log(vq Lq)</th><th>Posterior wq</th></tr></thead><tbody>${Q.theta.map((t,i)=>`<tr><td>${f(t,4)}</td><td>${Q.weights[i].toExponential(3)}</td><td>${f(r.logJoint[i],4)}</td><td>${r.posterior[i].toExponential(3)}</td></tr>`).join('')}</tbody></table>`;
  });}
  function comparison() {runCalculator('comparison-result',()=>{
    const correct=read('correct-count',0,10000,true),total=read('valid-count',1,10000,true),b=read('comparison-b',-5,5),old=$('old-label').value;
    const ci=M.wilson(correct,total),stable=M.stableBand(ci),empirical=ci.p>.7?'Easy':ci.p<.3?'Hard':'Medium';
    const flags=[];if(total<50)flags.push('insufficient_item_sample');if(ci.width>.3)flags.push('wide_difficulty_interval');if(correct===0||correct===total)flags.push('no_response_variation');if(stable&&stable!==old)flags.push('intended_empirical_disagreement');
    const quality=$('policy-example').value; if(quality==='ai_review') flags.push('negative_discrimination'); const weak=total<50||ci.width>.3||correct===0||correct===total; const decision=weak?'collect_more_events':quality==='ai_review'?'needs_ai_review':'retain'; const consequence=decision==='collect_more_events'?'Data contoh belum kuat: kumpulkan respons tambahan.':decision==='needs_ai_review'?'Policy menahan versi untuk validasi ulang AI berdasarkan flag kualitas contoh.':'Policy mempertahankan label awal; kategori empiris tersimpan terpisah.';
    labResult('comparison-result',[
      {title:'1. Hitung proporsi benar beserta intervalnya',tex:String.raw`\begin{aligned}\widehat p&=\frac{r}{n}=\frac{${correct}}{${total}}=${f(ci.p)}\\ d&=1+\frac{z^2}{n}\\ m&=\frac{\widehat p+z^2/(2n)}{d}\\ h&=\frac{z}{d}\sqrt{\frac{\widehat p(1-\widehat p)}{n}+\frac{z^2}{4n^2}}\\ \mathrm{CI}_{95\%}&=[m-h,m+h]\\ &=[${f(ci.low)},${f(ci.high)}]\end{aligned}`,symbols:[{symbol:String.raw`r,n`,meaning:'Jumlah jawaban benar dan jumlah jawaban valid untuk item yang sama.'},{symbol:String.raw`z=1.96`,meaning:'Nilai z yang digunakan kode untuk interval sekitar 95%.'},{symbol:String.raw`m,h`,meaning:'Titik tengah dan setengah lebar interval Wilson.'}],why:'Proporsi benar saja mudah berubah ketika sampel sedikit. Interval Wilson menunjukkan rentang ketidakpastian dan tetap bermakna pada proporsi yang dekat 0 atau 1. Sistem membandingkan kategori hanya jika seluruh interval berada pada satu band yang stabil.'}
    ],[{label:'Intended difficulty lama',value:old},{label:'Kategori dari proporsi benar',value:empirical},{label:'Kategori stabil dari seluruh interval',value:stable||'Belum stabil: interval melewati batas kategori.'},{label:'Lebar interval Wilson',value:f(ci.width)},{label:'Flags yang dapat dihitung dari r/n/label',value:flags.join(', ')||'Tidak ada pada subset input contoh.',key:'flags'},{label:'Kategori IRT dari b contoh',value:`${M.empiricalDifficulty(b)} (b=${b})`},{label:'Keputusan sistem',value:decision,key:'decision'}],[consequence,'affectsSilverLabels=false: keputusan empiris tidak menulis label silver pengganti. Label baru berasal dari validasi AI pada versi terkait.','Daya pembeda negatif dan distraktor tidak berfungsi memerlukan data respons lengkap. Perbedaan intended dan empirical sendiri dicatat sebagai flag observasi.','Setelah versi baru lolos qualification AI, dataset baru dapat dibekukan, dipakai untuk training offline, dikalibrasi, lalu dievaluasi sebelum modelnya diaktifkan.']);
  });}
  function bindInputs(ids,callback) {ids.forEach(id=>$(id).addEventListener('input',callback));}
  async function copyText(text, label) {
    let copied=false;
    try { if(navigator.clipboard?.writeText) {await navigator.clipboard.writeText(text);copied=true;} } catch (_error) { /* file:// fallback below */ }
    if(!copied) {
      $('manual-copy').hidden=false;$('manual-copy-text').value=text;$('manual-copy-text').focus();$('manual-copy-text').select();
      try {copied=document.execCommand('copy');} catch(_error) {copied=false;}
      if(copied)$('manual-copy').hidden=true;
    }
    $('copy-status').textContent=copied?`${label} sudah disalin.`:'Teks sudah dipilih. Tekan Ctrl+C atau gunakan menu salin.';
    clearTimeout(copyStatusTimer);
    if(copied)copyStatusTimer=setTimeout(()=>{$('copy-status').textContent='';},5000);
  }
  function slideText(slide,notes=false) {
    return `${slide.title}\n\n${slide.message}\n\n${slide.bullets.map(b=>'• '+b).join('\n')}\n\nMengapa: ${slide.why}${notes?'\n\nCatatan pembicara: '+slide.speakerNotes:''}`;
  }
  function termText(term) {
    return `${term.term}: ${term.meaning}\nFungsi / alasan: ${term.why}`;
  }
  function presentationText(presentation) {
    const slides=presentation.slides.map(slide=>{
      const terms=(slide.terms||[]).map(termText).join('\n\n');
      const formulas=(slide.latex||[]).map(card=>`${card.title}\n\n$$\n${card.tex}\n$$\n\n${card.symbols.map(s=>`${s.symbol}: ${s.meaning}`).join('\n')}\n\nMengapa dihitung begitu: ${card.why}`).join('\n\n');
      return `${slideText(slide,true)}${terms?'\n\nARTI ISTILAH\n'+terms:''}${formulas?'\n\nRUMUS LATEX\n'+formulas:''}`;
    }).join('\n\n---\n\n');
    const decisions=presentation.decisions.map(d=>`${d.method}\nArti dan fungsi: ${d.meaning}\nMengapa: ${d.why}\nBatas penggunaan: ${d.limit}`).join('\n\n');
    return `KESIMPULAN\n${presentation.conclusion}\n\n${presentation.intro}\n\n${slides}\n\nALASAN PEMILIHAN METODE\n${decisions}\n\nGLOSARIUM\n${presentation.glossary.map(termText).join('\n\n')}`;
  }
  function setupSummary() {
    const presentation=window.FLOW_PRESENTATION;
    if(!presentation){$('summary-intro').textContent='Bahan ringkasan belum termuat. Pastikan presentation-summary.js tersedia.';return;}
    $('summary-intro').textContent=presentation.intro;
    $('summary-conclusion').innerHTML=`<p class="eyebrow">KESIMPULAN UTAMA</p><h3>AI memberi label silver, jawaban siswa memberi bukti, sistem mengatur tindak lanjut.</h3><p>${esc(presentation.conclusion)}</p>`;
    $('ppt-slides').innerHTML=presentation.slides.map((slide,i)=>`<article class="ppt-card" id="ppt-${esc(slide.id)}"><div class="ppt-card-heading"><span class="phase-label">SLIDE ${String(i+1).padStart(2,'0')}</span><button type="button" data-copy-slide="${i}">Salin poin slide</button></div><h3>${esc(slide.title)}</h3><p class="ppt-message">${esc(slide.message)}</p><ul class="ppt-points">${slide.bullets.map(b=>`<li>${esc(b)}</li>`).join('')}</ul><div class="ppt-why"><b>Mengapa?</b><p>${esc(slide.why)}</p></div><details class="speaker-notes"><summary>Catatan pembicara, arti istilah, dan rumus</summary><p>${esc(slide.speakerNotes)}</p>${slide.terms?.length?E.terms(slide.terms):''}${(slide.latex||[]).map(E.formula).join('')}</details></article>`).join('');
    $('method-decisions').innerHTML=`<table><thead><tr><th>Metode / istilah</th><th>Artinya dan fungsinya</th><th>Mengapa dipilih?</th><th>Batas penggunaannya</th></tr></thead><tbody>${presentation.decisions.map(d=>`<tr><td><b>${esc(d.method)}</b></td><td>${esc(d.meaning)}</td><td>${esc(d.why)}</td><td>${esc(d.limit)}</td></tr>`).join('')}</tbody></table>`;
    $('summary-glossary').innerHTML=E.terms(presentation.glossary);
    $('copy-conclusion').addEventListener('click',()=>copyText(presentation.conclusion,'Kesimpulan'));
    $('copy-summary').addEventListener('click',()=>copyText(presentationText(presentation),'Seluruh bahan PPT'));
    $('print-summary').addEventListener('click',()=>{setView('summary');window.print();});
    document.addEventListener('click',event=>{
      const formulaButton=event.target.closest('[data-copy-tex]');
      if(formulaButton){copyText(formulaButton.dataset.copyTex,'Kode LaTeX');return;}
      const slideButton=event.target.closest('[data-copy-slide]');
      if(slideButton)copyText(slideText(presentation.slides[Number(slideButton.dataset.copySlide)]),'Poin slide');
    });
    $('close-copy').addEventListener('click',()=>{$('manual-copy').hidden=true;});
  }
  function init() {
    if (!data.length || !window.FLOW_MODEL_STAGES || !window.FLOW_ASSESSMENT_STAGES || !window.FLOW_FEEDBACK_STAGES || !M || !Q || !E || !window.katex) {
      $('stage-detail').innerHTML='<p role="alert">Ada berkas dokumentasi yang tidak termuat. Pastikan folder interactive tetap berada di sebelah HTML dan seluruh berkas JS tersedia.</p>';return;
    }
    $('nodes').innerHTML=data.map((stage,i)=>`<button type="button" class="node" data-status="${esc(stage.status)}" data-index="${i}" aria-pressed="false" aria-label="Tahap ${i+1}: ${esc(stage.title)}, ${statusText[stage.status]}"><span class="node-number">${String(i+1).padStart(2,'0')} <span aria-hidden="true">→</span></span><span class="node-title">${esc(stage.title)}</span><span class="node-phase">${esc(branchLabels[stage.id] || stage.phase)}</span></button>`).join('');
    $('phase-filter').innerHTML=['Semua',...phases].map(phase=>`<button type="button" data-phase="${esc(phase)}" aria-pressed="${phase===filter}">${esc(phase)}</button>`).join('');
    document.querySelectorAll('.node').forEach(button=>button.addEventListener('click',()=>select(Number(button.dataset.index))));
    document.querySelectorAll('[data-phase]').forEach(button=>button.addEventListener('click',()=>{
      filter=button.dataset.phase;document.querySelectorAll('[data-phase]').forEach(b=>b.setAttribute('aria-pressed',b===button?'true':'false'));
      if(filter==='Semua')select(current);else select(data.findIndex(s=>s.phase===filter));
    }));
    $('play').addEventListener('click',()=>{if(!playing&&current===data.length-1)select(0);setPlaying(!playing);});
    $('previous').addEventListener('click',()=>select(current-1));$('next').addEventListener('click',()=>select(current+1));
    $('restart').addEventListener('click',()=>{setPlaying(false);filter='Semua';document.querySelectorAll('[data-phase]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.phase===filter?'true':'false'));select(0);});
    $('speed').addEventListener('change',schedule);
    document.querySelectorAll('[data-view]').forEach(b=>b.addEventListener('click',()=>setView(b.dataset.view)));
    document.addEventListener('keydown',event=>{
      if($('view-flow').hidden || /INPUT|SELECT|TEXTAREA/.test(event.target.tagName))return;
      if(event.key==='ArrowRight'){event.preventDefault();select(current+1);}if(event.key==='ArrowLeft'){event.preventDefault();select(current-1);}
    });
    // Background tabs do not silently advance the educational timeline.
    document.addEventListener('visibilitychange',()=>{if(document.hidden)setPlaying(false);});
    $('all-stages').innerHTML=data.map((s,i)=>`<details id="ref-${esc(s.id)}"><summary><span class="phase-label">${String(i+1).padStart(2,'0')} / ${esc(s.phase)}</span><strong>${esc(s.title)}</strong>${badge(s)}</summary><p class="subtitle">${esc(s.subtitle)}</p>${branchNote(s)}${stageBody(s)}</details>`).join('');
    $('expand-reference').addEventListener('click',()=>{expanded=!expanded;document.querySelectorAll('#all-stages > details').forEach(d=>d.open=expanded);$('expand-reference').textContent=expanded?'Tutup seluruh tahap':'Buka seluruh tahap';});
    $('print-reference').addEventListener('click',()=>{document.querySelectorAll('#all-stages details').forEach(d=>d.open=true);window.print();});
    $('response-pattern').innerHTML=exampleItems.map((item,i)=>`<label>Item ${i+1}<small>a=1, b=${item.b}, c=0</small><select id="response-${i}" aria-label="Jawaban item ${i+1}"><option value="1"${i<3?' selected':''}>Benar (1)</option><option value="0"${i>=3?' selected':''}>Salah (0)</option><option value="null">Missing (null)</option></select></label>`).join('');
    bindInputs(['logit-easy','logit-medium','logit-hard','temperature','confidence-floor','entropy-ceiling','routing'],()=>{classification();ordinal();});
    bindInputs(['ordinal-score','ordinal-first','ordinal-gap'],ordinal);
    bindInputs(['sample-count','eligible-count','item-count','coverage','correct-rate','irt-model','assumptions'],snapshot);
    bindInputs(['theta','irt-a','irt-b','irt-c'],irt);
    bindInputs(exampleItems.map((_,i)=>'response-'+i),eap);
    bindInputs(['correct-count','valid-count','old-label','comparison-b','policy-example'],comparison);
    $('arrival').addEventListener('click',()=>{runCalculator('snapshot-result',()=>{const n=read('sample-count',0,10000,true),eligible=read('eligible-count',0,10000,true),add=Math.min(10,10000-n);$('sample-count').value=n+add;$('eligible-count').value=Math.min(n+add,eligible+add);snapshot();});});
    let snapshotId=0;
    $('freeze-snapshot').addEventListener('click',()=>{snapshot();if($('snapshot-result').getAttribute('role')==='alert')return;const entry=document.createElement('details');entry.open=true;const summary=document.createElement('summary');summary.textContent=`Snapshot contoh S${++snapshotId} · N_selected=${$('sample-count').value}, N_fit=${$('eligible-count').value}, J=${$('item-count').value}, model=${$('irt-model').value}`;const snapshotCopy=document.createElement('div');snapshotCopy.className='frozen-metrics';snapshotCopy.innerHTML=$('snapshot-result').querySelector('.result-metrics').outerHTML;const note=document.createElement('p');note.textContent='Hasil contoh ini tetap sama ketika peserta baru masuk. Perhitungan baru memiliki snapshot berikutnya.';entry.append(summary,snapshotCopy,note);if(snapshotId===1)$('frozen-result').textContent='';$('frozen-result').prepend(entry);});
    classification();ordinal();snapshot();irt();eap();comparison();setupSummary();select(0);
    new ResizeObserver(drawConnectors).observe($('flow-board'));
  }
  init();
})();
