# Animasi aliran data: JSON, LLM, IndoBERT, siswa, CTT/IRT dan umpan balik

[Buka animasi interaktif](33_ANIMATED_DATA_FLOW.html). Perjalanan dimulai ketika soal disimpan dalam JSON, yaitu format data yang mudah dibaca program. Setelah teks, opsi dan kuncinya diperiksa, LLM memberi usulan label berdasarkan isi soal. Usulan AI dan penilaian manusia mempunyai asal serta kewenangan yang berbeda; IndoBERT dapat dilatih pada dataset yang memenuhi syarat untuk jalurnya.

Selanjutnya, soal yang disahkan melalui penilaian manusia dapat dikerjakan siswa dalam pilot saat ini. Jawaban mereka menjadi bukti untuk memeriksa kualitas soal melalui CTT dan mengestimasi karakteristik soal melalui IRT. Setelah hasilnya ditinjau ahli, perubahan yang disetujui dapat masuk ke versi soal, dataset, dan model berikutnya. Dengan begitu, setiap perbaikan mempunyai alasan dan riwayat yang dapat diperiksa.

Pada setiap tahap animasi, baca **cerita alurnya → mengapa tahap diperlukan → arti istilah dan fungsinya → contoh → rumus beserta arti simbol → langkah berikutnya**. Input JSON, langkah kode dan output tetap tersedia di panel **Buka detail teknis**. Contoh angka ditujukan untuk belajar; halaman tidak menjalankan penilaian LLM atau kalibrasi siswa nyata.

Tab **Ringkasan untuk PPT** berisi 12 bagian yang siap disalin, alasan pemilihan metode, catatan pembicara dan glosarium. Materi yang sama tersedia di [34 — ringkasan untuk PPT](34_PPT_SUMMARY.md).

Dokumentasi ini mengikuti kode repository saat dibuat. Status **IMPLEMENTED** berarti fungsi tersedia; **BERSYARAT** berarti membutuhkan dataset, artifact, autentikasi atau gate yang sesuai; **RANCANGAN** berarti belum menjadi fungsi sistem. Panah animasi menjelaskan hubungan data, bukan bukti bahwa seluruh layanan sudah berjalan. Sumber kode di setiap tahap membantu memeriksa aturan yang ditampilkan.

## Menjalankan animasi

Cara langsung: buka `API_DOCUMENTATION/33_ANIMATED_DATA_FLOW.html` dengan double-click. File JavaScript/CSS lokal dimuat tanpa CDN, login atau token API. Pastikan folder `interactive/` tetap berdampingan dengan HTML.

Untuk membuka lewat server lokal, jalankan dari root repository:

```powershell
.\.venv\Scripts\python.exe -m http.server 8765 --bind 127.0.0.1
```

Lalu buka [http://127.0.0.1:8765/API_DOCUMENTATION/33_ANIMATED_DATA_FLOW.html](http://127.0.0.1:8765/API_DOCUMENTATION/33_ANIMATED_DATA_FLOW.html). Hentikan server dengan Ctrl+C. Tombol putar/jeda, langkah dan pemilihan tahap mengendalikan animasi; kalkulator mengubah angka contoh agar hubungannya dapat dipelajari. Rumus tampil sebagai persamaan LaTeX, dilengkapi arti simbol dan tombol salin kode. Renderer serta font disertakan di `interactive/vendor/katex/`, sehingga rumus juga berjalan offline. Folder itu harus tetap tersedia bersama berkas dokumentasi.

## Memahami alasan alurnya terlebih dahulu

| Setelah tahap… | Yang dilakukan berikutnya | Mengapa diperlukan? |
|---|---|---|
| Soal masuk sebagai JSON | Periksa isi, kunci, visual dan identitas versi | Perhitungan yang benar tetap bisa menilai konten yang salah. Kualitas sumber perlu diperiksa sejak awal. |
| Konten cukup lengkap | LLM menilai dengan rubrik, tanpa melihat prediksi IndoBERT | Label awal perlu menilai tuntutan isi secara mandiri sebelum dibandingkan dengan model. |
| Label/data memenuhi syarat jalurnya | IndoBERT mempelajari hubungan konteks teks dan tiga jenis label | Model membutuhkan contoh yang jelas; satu kata kerja saja tidak menjelaskan seluruh tuntutan soal. |
| Probabilitas model tersedia | Baca confidence dan entropy, lalu tentukan kebutuhan review | Label teratas saja tidak menunjukkan kekuatan dan penyebaran pilihan model. |
| Ahli mengesahkan versi soal | Siswa mengerjakan, server memberi skor dan menyimpan jawaban | Analisis empiris membutuhkan jawaban yang terikat pada konten dan kunci yang tepat. |
| Jawaban valid terkumpul | Bekukan snapshot dan periksa syarat CTT/IRT | Jumlah siswa terus bertambah, tetapi satu hasil hitung perlu batas data yang jelas dan cukup bukti. |
| Hasil empiris tersedia | Ahli memutuskan pertahankan, revisi, atau karantina | Kesulitan populasi dan tuntutan isi adalah dua ukuran berbeda; perbedaan perlu dijelaskan sebelum label diubah. |
| Versi dan label baru disetujui | Bekukan dataset baru, latih dan evaluasi model | Perbaikan harus dapat diulang dan ditelusuri, serta tidak mengubah model yang aktif secara diam-diam. |

## Peta implementasi

| Bagian | Kemampuan sekarang | Batas yang harus terlihat pada flow |
|---|---|---|
| Ekstraksi | JSON strict per bab, validasi mekanis, ekspor dan import tersedia sebagai workflow lokal | `soal_pretest_db.json` merupakan candidate export; `sesi_pretest.json` bukan session siswa nyata |
| Silver LLM | Gemini blind N=3, key/solution/visual evidence, adjudikasi AI, audit/checkpoint dan bundle laporan | Label silver/advisory; tiga run model yang sama bukan tiga ahli manusia |
| IndoBERT | Runtime tiga head dan training tersedia; default training baru grade-aware ordinal + LoRA | Artifact lama dapat memakai `parallel-v1`; arsitektur/input/calibration yang benar berasal dari manifest |
| Scope | Kontrak JSON mengizinkan grade 1–12; runtime classifier sekarang mendukung grade 1–6 | Grade 7–12 menghasilkan `out_of_scope`/`abstain`, meskipun validasi Gemini lengkap |
| Gold ahli | Blind review tiga ahli, consensus, diskusi, senior adjudication dan freeze tersedia | Memerlukan reviewer/data manusia; gold pada bundle AI tidak dibuat oleh voting AI |
| Assessment siswa | Fixed-form pilot, participant token, immutable delivery, server scoring, complete tersedia | `AssessmentStore.create_assessment` mensyaratkan snapshot `human_gold`, `researchOnly=false`; delivery langsung dari silver belum tersedia |
| CTT/IRT | Cleaning, sample gate, CTT, regularized Rasch/2PL/3PL dan immutable snapshot tersedia | Penelitian/advisory; IRT batch memerlukan data dan assumption review, bukan per jawaban otomatis |
| Feedback | Expert retain/revise/quarantine, hold delivery dan exclusion pada freeze tersedia | Keputusan mempunyai `affectsGoldLabels=false`; tidak auto-relabel atau auto-retrain |
| Integrasi berikutnya | Dapat dibahas sebagai rancangan eksplisit | Fitur IRT ke classifier, silver delivery adapter, learner profile, CAT, release calibration, linking/equating dan DIF belum diimplementasikan |

Rujukan utama: [21 — ekstraksi](21_PRETEST_AGENTIC_PIPELINE_INTEGRATION.md), [24 — IndoBERT/LLM](24_INDOBERT_FINETUNING_LLM_REASONING_DETAIL.md), [25 — training baru](25_GRADE_AWARE_ORDINAL_PIPELINE.md), [27 — pilot/IRT](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md), dan [28 — topology serta batas silver](28_END_TO_END_PERSONALIZED_ASSESSMENT_FLOW.md). Dokumen 21 juga menyimpan desain/histori Claude pascaprediksi; protokol silver aktif pada 24/25 dan kode blind adalah acuan untuk eksperimen baru.

## 1. Dari JSON ekstraksi menjadi versi soal

`babNN.json` menyimpan asal buku, bab, halaman, section, pertanyaan, stimulus, gambar, kunci, solusi agen, distraktor dan catatan ekstraksi. Validator memeriksa schema, verbatim/angka terhadap sumber, key evidence, opsi duplikat/senilai serta media. `tingkat_kesulitan` 1–5 dan confidence exporter `0.95/0.60/0.30` merupakan heuristik staging; keduanya bukan label difficulty model atau probabilitas terkalibrasi.

Adapter [`import_bab_file`](../app/ingestion/pretest_import.py) menyusun opsi stabil dan `QuestionVersionDocument`. Identitas, `contentVersion`, `contentHash`, source record/asset checksum dan extraction evidence dipertahankan. `next_content_version` menghasilkan versi sama jika hash konten sama, atau versi berikutnya bila hash berubah. Helper ini belum menjadi endpoint revisi konten otomatis. Perubahan source JSON, prompt atau byte gambar mengharuskan penilaian ulang; run lama hanya dapat dipertahankan jika input yang dinilai masih cocok.

`draft`, `needs_review_kunci`, `needs_review_soal` dan `needs_image` adalah status ekstraksi. `draft` belum menjadi gold atau siap pilot. Item yang perlu gambar/key/revisi harus menampilkan cabang pemeriksaan sebelum masuk snapshot. Perbedaan schema export DB lama juga membutuhkan adapter; file export tidak diberikan langsung ke endpoint siswa.

## 2. Label awal LLM dan arti penjelasan yang tersimpan

Gemini menerima soal, opsi, grade, rubrik domain kognitif/dimensi pengetahuan/difficulty, key evidence dan gambar yang tersedia. Prompt blind tidak menerima prediksi IndoBERT, estimasi difficulty agen, vote run lain atau distribusi target. Output terstruktur mencakup content/key status, verified key, solusi minimum, label/action/evidence/rationale per head serta difficulty evidence profile.

Sistem menyimpan **solusi minimum terverifikasi, evidence spans, rationale singkat dan profil bukti**. Itulah penjelasan yang dapat diaudit dan ditampilkan. Hidden chain-of-thought internal model tidak diminta atau disimpan. Tidak ada formula aritmetis yang menjumlahkan evidence profile untuk mengubahnya menjadi Easy/Medium/Hard.

Aturan silver:

1. Jalankan tiga initial runs dan validasi output terhadap schema strict.
2. Terima langsung hanya 3–0 tanpa blocker content/key/visual.
3. 2–1, abstain, konflik atau concern masuk adjudikasi AI terpisah; bukti yang belum cukup tetap undecided/blocked sesuai routing.
4. Error `429`, `503`, invalid schema atau provider failure dicatat sebagai kegagalan, bukan label default. Checkpoint kerja dapat di-resume; audit snapshot/hash lama tetap dipertahankan.
5. Lock hasil blind melalui audit sebelum prediksi dan perbandingan model dibuat.

Agreement `3/3` adalah tingkat kesepakatan run, bukan calibrated confidence IndoBERT dan bukan jaminan kebenaran. Di hasil AI, `humanValidation.goldLabels=null` berarti data manusia belum ada. Lihat [`app/llm/silver.py`](../app/llm/silver.py), [`generate_silver_labels_kelas1.py`](../scripts/generate_silver_labels_kelas1.py), [`audit_grade_aware_pilot.py`](../scripts/audit_grade_aware_pilot.py) dan [laporan aktif](../output/pretest/README.md).

## 3. Fitur, token, tiga head, confidence dan entropy IndoBERT

Field teks dirender oleh [`serialize_question`](../app/classification/v2/serializer.py) sesuai `inputRepresentation` di manifest: `stem_options`, `metadata`, `solution` atau `kko`. Normalisasi/urutan field tetap; `grade` juga disediakan sebagai input numerik pada arsitektur grade-aware. Tokenizer tersimpan bersama artifact, memakai `maxLength` manifest dan truncation. Report mencatat serialized input, jumlah token sebelum truncation, panjang maksimum dan apakah input terpotong.

IndoBERT membaca token dan menghasilkan representasi `[CLS]`. Head kognitif mempunyai 3 kelas, knowledge 4 kelas dan intended difficulty 3 kelas. Pada `grade-aware-ordinal-v2`, difficulty memakai concat representasi encoder + grade embedding (default 16 dimensi), skor `s` dan cutpoints terurut. Arsitektur artifact lama harus dibaca dari manifest, bukan diasumsikan dari default training baru.

$$
\begin{aligned}
q_0 &= \sigma(s-\tau_0), & q_1 &= \sigma(s-\tau_1),\\
P(\mathrm{Easy}) &= 1-q_0,\\
P(\mathrm{Medium}) &= q_0-q_1,\\
P(\mathrm{Hard}) &= q_1,\\
\tau_1 &= \tau_0+\ln(1+e^{g})+10^{-4}>\tau_0.
\end{aligned}
$$

Di sini $s$ adalah skor difficulty dari model, $\tau_0,\tau_1$ adalah dua batas kategori yang dipelajari, dan $g$ mengatur jarak keduanya. $\sigma$ adalah sigmoid, fungsi yang mengubah skor menjadi peluang 0–1. **Mengapa dua batas?** Easy, Medium dan Hard memiliki urutan; selisih dua peluang kumulatif membentuk kategori Medium yang berada di tengah.

Contoh ilustratif `s=0`, `τ0=−0.5`, `τ1=1.5` memberi probabilitas ≈ `[0.378, 0.440, 0.182]`. Difficulty ordinal menghasilkan log probabilitas untuk tahap kalibrasi; head multiclass menghasilkan logits. Runtime menerapkan temperature `T` yang dipilih menggunakan validation:

$$
\begin{aligned}
p_k &= \frac{\exp(z_k/T)}{\sum_{j=1}^{K}\exp(z_j/T)},\\
p_k^{\mathrm{cal,ordinal}} &\propto (p_k^{\mathrm{raw}})^{1/T},\\
C &= \max_k p_k,\\
H_{\mathrm{norm}} &= -\frac{\sum_{k=1}^{K}p_k\ln p_k}{\ln K}.
\end{aligned}
$$

$z_k$ adalah skor mentah atau logit untuk kategori $k$, $T$ adalah temperature yang dipilih dari validation, dan $K$ adalah jumlah kategori. $C$ merangkum peluang tertinggi; $H_{\mathrm{norm}}$ merangkum sebaran seluruh peluang. **Mengapa dinormalisasi dengan $\ln K$?** Itu adalah entropy maksimum untuk $K$ kategori, sehingga hasilnya berada pada skala 0–1 untuk head dengan jumlah kelas berbeda. Temperature menyesuaikan ketajaman probabilitas sebelum ringkasannya dihitung.

Contoh `p=[0.80,0.15,0.05]`: label argmax adalah kelas pertama, confidence `0.80`, entropy ≈`0.558`. Entropy mendekati 0 jika distribusi terkonsentrasi dan 1 jika seragam. Confidence/entropy adalah ringkasan **output probabilitas**, bukan fitur awal JSON atau hasil IRT.

Untuk policy `confidence-entropy-v1`, `predict` membutuhkan confidence ≥ threshold, entropy ≤ threshold dan tidak ada reason lain. Confidence di bawah batas, entropy di atas batas atau input mencapai truncation limit menghasilkan `review`. Provenance gagal atau grade di luar scope menghasilkan `abstain` dengan label null. Artifact `confidence-only-v1` hanya memakai confidence untuk gate; entropy tetap dilaporkan. Threshold/T global atau per-grade berasal dari manifest/calibration yang benar; contoh angka kalkulator tidak menetapkan policy repository. Untuk item yang sudah ada di manifest `contentRegistry`, version/hash yang berbeda menghasilkan `ContentConflictError` (API 409), bukan prediksi pada konten pengganti. Probabilitas nonfinite atau tidak berjumlah 1 menghasilkan error dan menandai runtime failure.

Sumber: [`model.py`](../app/classification/v2/model.py), [`calibration.py`](../app/classification/v2/calibration.py), [`runtime.py`](../app/classification/v2/runtime.py) dan [`contracts.py`](../app/classification/v2/contracts.py). API menerima schema strict; field tambahan seperti `b`, `theta` atau `irtFeature` ditolak.

## 4. Validasi blind dan gold manusia menuju pilot

Pipeline silver aktif melakukan perbandingan **setelah label blind dikunci**, tanpa reviewer LLM yang membaca prediksi pascaproses. [`compare_blind_labels_to_predictions.py`](../scripts/compare_blind_labels_to_predictions.py) memeriksa hash/audit/input match serta timestamp, lalu join per `questionId`, menghasilkan agreement/confusion/evidence. Kesesuaian versi wajib dijaga lewat provenance sebelum join; label null/out-of-scope tidak boleh diperlakukan sebagai prediksi kelas valid. Bundle AI tetap advisory dan tidak menjadi assessment gold.

Ada jalur manusia terpisah. [`build_consensus`](../app/annotation/consensus.py) memerlukan tiga reviewer berbeda pada versi yang sama. Bila tiga vote lengkap, 3–0 diterima unanimous dan 2–1 diterima majority. Split 1–1–1, abstain atau gate content/key/solution gagal membutuhkan diskusi; unresolved dilanjutkan ke senior adjudication. Semua reviewer harus menyatakan content valid, key verified dengan key yang sama dan solusi tersedia agar content eligible langsung. Keputusan settled tidak boleh diganti oleh diskusi/adjudication.

Setelah freeze human gold, [`AssessmentStore.create_assessment`](../app/assessment/store.py) memverifikasi snapshot hash, grade, versi, human decision, jenis PG satu jawaban, key/solution dan hold. Silver/research snapshot ditolak. Delivery pilot bersifat text-only; visual esensial membutuhkan transkripsi terverifikasi. Adapter silver pada dokumen 28 adalah rancangan, sehingga animasi tidak mengklaim output silver sekarang otomatis dikirim ke siswa.

## 5. Respons siswa: segera dicatat, calibration IRT dilakukan batch

Alur API tersedia adalah create assessment → create participant → start session → next item → submit response → complete. Token peserta menyatakan ownership. Server membuat delivery immutable: urutan opsi acak dan public option IDs tetap sama ketika refresh/retry. Payload siswa tidak berisi key, solusi atau reasoning LLM. Submit memuat public option ID/skip; server menilai menggunakan mapping privat dan key versi tersebut.

$$
x_{ij}=\begin{cases}
1 & \text{jawaban siswa }i\text{ pada item }j\text{ benar},\\
0 & \text{jawaban salah},\\
\mathrm{NA} & \text{skip atau missing}.
\end{cases}
$$

**Mengapa skip tidak menjadi 0?** Skor 0 menyatakan ada jawaban yang salah; NA menyatakan belum ada bukti respons yang bisa dinilai. Menyamakan keduanya akan menambah kesalahan yang sebenarnya tidak diamati. Pada kode, `isCorrect=true/false/null` dipetakan menjadi 1/0/NA.

Timestamp/delivery timing berasal dari server. Idempotency melindungi start/response/complete terhadap duplikasi; `Idempotency-Key` pada response harus cocok dengan `responseId`. Completion membutuhkan seluruh item sudah answered atau explicitly skipped. Pengisian `jawaban_agen`, tiga vote AI dan file `sesi_pretest.json` tidak menghasilkan respons atau siswa nyata.

**Realtime sekarang**: respons dinilai/disimpan pada submit. **Batch sekarang**: operator memanggil screening untuk mengambil window completed sessions dan menghitung snapshot empiris. Tidak ada scheduler otomatis atau item calibration per jawaban. Refit dapat dipanggil lagi ketika evidence bertambah; data/window/policy identik me-replay snapshot lama, data/policy berubah menghasilkan snapshot baru. Online theta scoring untuk seorang siswa dengan bank parameter tetap adalah fitur CAT yang terpisah dan belum ada.

## 6. Menghitung jumlah siswa ketika siswa terus masuk

Jumlah siswa terdaftar, sedang online, response events atau session yang dibuat bukan `N` untuk fit IRT. [`AssessmentStore.screen`](../app/assessment/store.py) memilih session **completed** dalam completion time window `[fromTime,toTime)`, lalu memilih satu **whole session** first/last per `subjectHash`. First/last mengikuti urutan `started_at,id` setelah filter completion window. Satu siswa dengan tiga attempt tidak menjadi tiga siswa. Session incomplete/window mismatch dan attempt lain tidak terpilih; cleaning mencatat `completedSessions`/`selectedSessions`, sedangkan alasan exclusions terperinci tersedia untuk response events.

[`normalize_events`](../app/psychometrics/analysis.py) memeriksa response IDs, versi/hash, population/family/grade/subject, valid-for-analysis, rapid guesses, scoring status dan timezone. Data conflict/invalid tidak dipaksa menjadi 0. Matriks menggunakan satu baris per selected subject dan satu kolom per versi item; missing/skip tetap NA.

$$
\begin{aligned}
r_i &= \frac{m_i}{J},\\
N_{\mathrm{fit}} &= \sum_{i=1}^{N_{\mathrm{selected}}}\mathbf{1}(r_i\geq 0.70),\\
n_j &= \sum_i \mathbf{1}(x_{ij}\text{ teramati dan valid}).
\end{aligned}
$$

$N_{\mathrm{selected}}$ adalah jumlah peserta unik dengan sesi selesai yang terpilih, $m_i$ jumlah item terjawab valid oleh siswa $i$, dan $J$ jumlah item. Fungsi indikator $\mathbf{1}$ bernilai 1 ketika syarat terpenuhi dan 0 bila tidak. $N_{\mathrm{fit}}$ menghitung siswa yang cukup lengkap untuk fitting; $n_j$ menghitung respons valid pada satu item. **Mengapa dibedakan?** Seratus siswa terpilih belum berarti setiap soal mempunyai seratus jawaban, atau semua baris layak dipakai untuk IRT.

Contoh ilustratif: 150 siswa terdaftar, 120 mempunyai completed session terpilih dan 12 di antaranya missing >30% → `N_fit=108`. Gate Rasch jumlah orang dapat lolos, tetapi gate per item, coverage, outcome variation, desain dan asumsi tetap diperiksa. `n_item` dapat berbeda untuk setiap item; tidak ada syarat mengetahui total siswa yang akan datang pada masa depan.

Untuk cohort yang terus bertambah, ambil cutoff window yang jelas dan simpan snapshot A. Jawaban/session selesai setelah cutoff menjadi evidence untuk snapshot B. Catat population, family, grade, form/version, first/last policy dan completion window pada keduanya. Ini prosedur screening yang dapat dijalankan operator sekarang; scheduling/cadence/release otomatis adalah rancangan operasional.

## 7. CTT dahulu, readiness gate sebelum IRT

CTT per item menghitung `p=benar/n_valid` dan Wilson interval. Corrected point-biserial serta upper/lower discrimination memakai **complete cases** untuk score total, mengurangi score item sendiri dari rest score. Tidak ada zero-imputation untuk join skor total atau KR-20. Discrimination kode memakai kelompok rest-score di bawah quantile 0.27 dan di atas 0.73; ties dapat mengubah ukuran kelompok. Event valid memberi frekuensi pilihan distraktor, median/IQR waktu dan distractor efficiency.

$$
\begin{aligned}
\widehat p &= \frac{r}{n}, & d &= 1+\frac{z^2}{n},\\
m &= \frac{\widehat p+z^2/(2n)}{d},\\
h &= \frac{z}{d}\sqrt{\frac{\widehat p(1-\widehat p)}{n}+\frac{z^2}{4n^2}},\\
\mathrm{CI}_{95\%} &= [m-h,m+h], & z&=1.96.
\end{aligned}
$$

$r$ adalah jumlah benar, $n$ jumlah jawaban valid, $m$ titik tengah dan $h$ setengah lebar interval Wilson. **Mengapa memakai interval?** Proporsi dari sampel kecil mudah berubah. Interval memberi gambaran ketidakpastian, termasuk ketika proporsi dekat 0 atau 1.

$$
\begin{aligned}
r_{j,\mathrm{rest}} &= \operatorname{corr}(x_j,T-x_j),\\
D_j &= \overline{x}_{j,\mathrm{upper}}-\overline{x}_{j,\mathrm{lower}},\\
\mathrm{KR20} &= \frac{J}{J-1}\left(1-\frac{\sum_{j=1}^{J}s_j^2}{s_T^2}\right),\\
s_j^2 &= \frac{n_{\mathrm{complete}}}{n_{\mathrm{complete}}-1}\,p_j(1-p_j).
\end{aligned}
$$

$T$ adalah skor total, $x_j$ skor item, $D_j$ selisih proporsi benar kelompok rest-score tinggi dan rendah, $s_j^2$ varians sampel item, serta $s_T^2$ varians sampel total. Di rumus ini $T$ berarti skor total, berbeda dari temperature pada klasifikasi. **Mengapa skor item dikurangi dari total?** Agar korelasi tidak terbantu hanya karena item itu merupakan bagian dari totalnya sendiri. KR-20 merangkum konsistensi tes; kode memakai complete cases dan sample variance `ddof=1` pada item maupun total. Ia bukan ukuran kesulitan satu soal.

Perhitungan menampilkan null bila korelasi/variance/sample tidak mendukung, beserta flags yang relevan. Detail kebijakan dan formula implementasi ada di [`analysis.py`](../app/psychometrics/analysis.py) serta [`app/evaluation/psychometrics.py`](../app/evaluation/psychometrics.py).

| Gate policy default | Rasch | 2PL | 3PL |
|---|---:|---:|---:|
| Minimum eligible persons | 100 | 300 | 1.000 |
| Minimum items | 5 | 10 | 20 |
| Minimum valid responses per item | 50 | 50 | 50 |
| Minimum correct dan incorrect per item | masing-masing 5 | masing-masing 5 | masing-masing 5 |
| Fit coverage | ≥70% | ≥70% | ≥70% |
| Missing per person | ≤30% | ≤30% | ≤30% |

Semua model juga membutuhkan connected response design dan assumption review yang mendukung unidimensionality, local independence serta representative sample. Ambang di [`configs/psychometrics_policy.json`](../configs/psychometrics_policy.json) adalah policy proyek, bukan bukti validitas otomatis. Gagal data → `waiting_for_data`; review asumsi belum ada/tidak mendukung → `waiting_for_assumption_review`. CTT tetap disimpan. Tidak ada respons complete untuk screening → error 409, bukan data sintetis pengganti.

## 8. Apa yang dihitung IRT, dengan cara teknis yang benar

Model kode menggunakan skala `θ ~ N(0,1)`, logistic `D=1` dan missing cells tidak memberi likelihood:

$$
P_j(\theta)=c_j+\frac{1-c_j}{1+\exp[-a_j(\theta-b_j)]}.
$$

Rasch menetapkan $a=1,c=0$ dan mengestimasi $b$; 2PL mengestimasi $a,b$ dengan $c=0$; 3PL mengestimasi ketiganya. **Mengapa ada tiga pilihan?** Model yang lebih kompleks mencoba mengestimasi lebih banyak karakteristik item, sehingga policy proyek menuntut sampel yang lebih besar. Kompleksitas tambahan belum otomatis menghasilkan pengukuran yang lebih baik.

`a` adalah discrimination/slope, `b` posisi difficulty pada skala lokal dan `c` lower asymptote. Untuk 2PL/Rasch, `θ=b` memberi P=0.5. Untuk 3PL, `θ=b` memberi P=(1+c)/2, misalnya c=0.2 →0.6. `c` diestimasi menggunakan prior dan batas; tidak ditetapkan sama dengan 1/jumlah opsi. Contoh 2PL `a=1.2, b=0.5, θ=1.5` memberi P≈0.769.

`fit_irt` mengintegrasikan kemampuan lewat 41 Gauss-Hermite quadrature points default, menghitung marginal likelihood dengan `logsumexp`, menambahkan prior/regularization dan mengoptimasi L-BFGS-B. Inisialisasi menggunakan smoothed p, bukan jawaban akhir:

$$
\begin{aligned}
p_{0j} &= \frac{\mathrm{correct}_j+0.5}{\mathrm{observed}_j+1},\\
b_{\mathrm{init},j} &= \operatorname{clip}\left(\ln\frac{1-p_{0j}}{p_{0j}},-3,3\right),\\
L_i &= \int \phi(\theta)\prod_{j\in O_i}P_j(\theta)^{x_{ij}}[1-P_j(\theta)]^{1-x_{ij}}\,d\theta,\\
\mathcal J &= -\sum_i\ln L_i+\text{penalti prior}.
\end{aligned}
$$

$O_i$ memuat item terjawab valid oleh siswa $i$; $\phi$ adalah kepadatan prior normal. **Mengapa kemampuan diintegrasikan?** Kemampuan siswa belum diketahui ketika parameter item diestimasi. Marginal likelihood memperhitungkan berbagai kemungkinan kemampuan menurut skala yang ditetapkan. Smoothing pada nilai awal mencegah logaritma ekstrem pada semua benar/salah; itu hanya inisialisasi, bukan hasil akhir. Prior lemah membantu estimasi tetap terbatas pada pola yang ekstrem.

$$
\begin{aligned}
\widehat\theta_{\mathrm{EAP},i} &= \sum_q w_{iq}\theta_q,\\
\mathrm{SD}_{\mathrm{post},i} &= \sqrt{\sum_q w_{iq}\theta_q^2-\widehat\theta_{\mathrm{EAP},i}^{\,2}},\\
I_j(\theta) &= \frac{[P'_j(\theta)]^2}{P_j(\theta)[1-P_j(\theta)]},\\
I_{\mathrm{test}}(\theta) &= \sum_j I_j(\theta).
\end{aligned}
$$

$w_{iq}$ adalah bobot posterior yang sudah diperbarui dengan jawaban dan dinormalisasi. **Mengapa memakai EAP?** Rata-rata posterior memberi estimasi kemampuan yang terbatas untuk pola semua benar/salah, disertai simpangan baku sebagai ketidakpastian. **Mengapa menghitung informasi?** Informasi menunjukkan seberapa peka item/tes terhadap perubahan kemampuan di titik tertentu; ia berbeda dari confidence model klasifikasi.

Bounds/prior aktual: b∈[−5,5] dengan N(0,3²); a∈[0.2,4] melalui log-a dengan N(0,0.75²); c∈[0.001,0.35] dengan Beta(5,17). Code memeriksa finite estimates, convergence, parameter boundary, posterior-curvature uncertainty, infit/outfit dan residual dependence. `bPosteriorSd`/interval berasal dari curvature objective yang berpenalti, bukan unpenalized frequentist standard error.

Output memuat a/b/c per item, b interval bila tersedia, infit/outfit, empirical band, theta EAP/posterior SD per person, test information, log-likelihood, descriptive AIC/BIC, convergence/iterations/warnings dan scale. AIC/BIC pada regularized estimates bukan approval pemilihan model. `estimated_with_warnings` juga belum menjadi release calibration. Semua calibration ini lokal: beda population/grade/form/version belum comparable tanpa linking/equating.

Rujukan sumber: [`irt.py`](../app/psychometrics/irt.py), [`analysis.py`](../app/psychometrics/analysis.py), [07 — kontrak psikometrik](07_PSYCHOMETRICS_API.md) dan [27 — CLI/API](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md). Data demo diberi `dataOrigin=synthetic`; hasil demo tidak menunjukkan calibration siswa nyata.

## 9. Hasil IRT kembali ke IndoBERT melalui jalur apa?

**Jalur yang tersedia**: empirical snapshot → flag/review ahli → retain/revise/quarantine → hold bila perlu → revised/qualified version + anotasi manusia → freeze snapshot baru → training/calibration artifact baru → perbandingan/evaluasi → gate/approval. `EmpiricalDecisionInput` hanya menyatakan tindakan dan rationale; [`AssessmentStore.decide`](../app/assessment/store.py) menyimpan `affectsGoldLabels=false`. Respons siswa mentah, θ dan a/b/c tidak masuk serializer/training row aktif.

Label intended lama dan empirical band dihitung berdampingan. Flag disagreement CTT baru muncul bila **Wilson CI berada seluruhnya dalam band yang stabil** dan band tersebut berbeda dari intended. Contoh 85/100 benar memberi CI≈[0.767,0.907]; intended Hard dibanding stable CTT Easy menjadi alasan review. IRT b=−1.2 memberi empirical Easy secara advisory, tidak mengganti intended. Domain kognitif dan knowledge juga tetap membutuhkan bukti konten.

`revise`/`quarantine` menahan versi terkait untuk delivery baru dan mengecualikannya dari freeze berikutnya. Perubahan konten/key/solusi/visual memiliki versi dan hash baru. Gold baru berasal dari ahli; silver baru berasal dari protokol blind AI dengan provenance research. Keduanya tidak disamakan. Label lama tetap di snapshot lamanya.

Perbandingan sejarah yang harus dicatat operator:

| Objek | Label/hasil ilustratif | Asal |
|---|---|---|
| Question v2, snapshot gold-v1 | intended Hard | Review ahli v2 |
| Calibration v2, population A/window A | p=0.85, b=−1.2, empirical Easy | Respons siswa valid pada v2 |
| Decision pada empirical snapshot A | revise; affectsGoldLabels=false | Ahli meninjau bukti |
| Question v3, snapshot gold-v2 | intended Medium | Revisi + review ahli v3 |
| Model challenger pada v3 | predicted Medium, p=0.78 | Prediksi model; bukan sumber gold |

Tidak ada weighted formula 40% model + 60% LLM, confidence×IRT atau b→gold aktif. Perbandingan v2/v3 di atas adalah lineage revisi pada dua input; evaluasi champion/challenger yang adil membutuhkan benchmark item/version yang tetap. Sistem comparison terpadu old-gold/new-gold/model dan auto-relabel belum tersedia sebagai layanan; comparison script aktif hanya locked silver versus prediksi offline.

Jika ingin fitur IRT masuk neural classifier kelak, diperlukan schema, empirical feature/missingness/provenance, fusion head, target yang sesuai, pemisahan waktu/populasi/family untuk mencegah leakage dan ablation. Itu **RANCANGAN** di animasi. Online theta scoring juga memerlukan bank calibration yang dilepas, ownership learner, posterior update, exposure/content constraints serta stopping policy. Tidak ada auto-release IRT sekarang.

## 10. Training, evaluasi dan aktivasi artifact berikutnya

Training baru memakai shared IndoBERT + LoRA query/value, CE untuk domain/knowledge dan weighted BCE untuk dua ordinal targets difficulty. Easy=[0,0], Medium=[1,0], Hard=[1,1]. Class weights berasal dari train; validation menentukan calibration/threshold. Checkpoint dipilih berdasarkan anti-collapse, macro-F1 head terlemah lalu rata-rata. Source family, stimulus dan duplicate families tidak melintasi train/validation/test. Test tetap frozen menurut gate.

Promotion aktual pada [`promotion_gate_failures`](../app/training/v2/train_lora.py) memeriksa H1/H2 macro-F1≥0.70, H3≥0.65, tiap class F1≥0.50, tiap head ECE≤0.10, selective accuracy≥0.80 pada coverage≥0.70, anti-collapse/baseline serta stabilitas tiga seed. Manifest menyimpan data/split/model/calibration/rubric/architecture/checksum versions. Artifact baru menolak overwrite.

$$
\mathrm{servable}=A\land\neg R\land D\land C\land P.
$$

$A$ adalah approval eksplisit, $R$ status research-only, $D$ lolos data gates, $C$ lolos anti-collapse, dan $P$ lolos promotion gates. **Mengapa semua diperlukan?** Metrik bagus pada satu pengujian belum menjamin dataset memadai, model tidak collapse, atau penggunaan sudah disetujui. Persamaan logika ini merangkum gate aktual, bukan rumus pembobotan label.

Silver tetap `researchOnly=true` walaupun metrics bagus. [/v2/classify](04_CLASSIFICATION_API.md) dapat mengembalikan 503 jika artifact belum servable. Gate teknis dan approval model berbeda dari readiness IRT atau keputusan gold; tidak ada auto-train, auto-publish atau silent promotion setelah respons siswa bertambah.

## Cabang yang harus dapat dilihat dan dipahami

| Kondisi | Perilaku yang benar |
|---|---|
| Schema/angka/verbatim/opsi invalid | Blokir/review staging; jangan membuat label default |
| Kunci berbeda/ambiguous | Verifikasi key/solusi; jangan lanjut sebagai item siap scoring |
| Gambar esensial hilang | Review/abstain; transkripsi terverifikasi diperlukan untuk model teks |
| Input/prompt/image byte berubah | Invalidate penilaian yang tidak cocok; checkpoint versi baru + undecided sampai selesai |
| Provider gagal/kuota habis | Run failure/history + resume; tidak dihitung sebagai vote label |
| Silver 2–1/abstain/content concern | Adjudikasi AI; tetap advisory |
| Gold manusia 2–1 lengkap, content eligible | Majority dapat settled; policy berbeda dari silver |
| Grade 7–12 | LLM dapat menilai; runtime IndoBERT sekarang out_of_scope/abstain |
| Low confidence/high entropy/truncation | review sesuai manifest; label prediksi bukan keputusan final |
| Registered model content version/hash berbeda | 409 content conflict; tidak mengubah input terdaftar secara diam-diam |
| Artifact/checksum/model tidak siap atau probabilitas invalid | Readiness/error; jangan memalsukan label/probabilitas |
| Silver/research snapshot ke assessment | Ditolak; silver delivery adapter masih rancangan |
| Skip/missing | NA; tidak dijadikan salah atau likelihood respons |
| Response retry/concurrency | Ownership + idempotency + delivery immutable; jumlah siswa tidak mengganda |
| Repeat/incomplete/rapid guess/version mismatch | Attempt selection/cleaning/exclusion; tidak masuk sampel valid tanpa pemeriksaan |
| N/item/outcome/coverage/asumsi tidak cukup | CTT tersedia; IRT waiting dengan reasons |
| IRT boundary/nonconvergence/uncertainty | Warning dan review; bukan calibration release |
| Empirical vs intended berbeda | Flag + review; label/version lama tetap tersimpan |
| Hold setelah item dikirim | Event tetap tersimpan dengan flag invalid; delivery baru ditahan |
| Synthetic demo/test | Diberi label synthetic; bukan data siswa atau bukti validitas lapangan |
| Source family/form/grade/population berbeda | Jangan membandingkan calibration tanpa linking |
| Fitur IRT/realtime CAT ditampilkan | Label RANCANGAN; schema/runtime saat ini tidak mengimplementasikannya |

## Rujukan kontrak, artefak dan kode

- [00 — indeks dokumentasi](00_README.md), [12 — endpoint aktual](12_ENDPOINT_MASTER_REFERENCE.md), [schemas implementasi](schemas/implemented-api.schema.json).
- [06 — respons siswa](06_STUDENT_RESPONSE_API.md), [07 — psikometrik](07_PSYCHOMETRICS_API.md), [08 — delivery](08_ASSESSMENT_DELIVERY_API.md), [23 — feedback empiris](23_EMPIRICAL_VALIDATION_FEEDBACK_FLOW.md).
- [21 — ekstraksi](21_PRETEST_AGENTIC_PIPELINE_INTEGRATION.md), [24 — detail model/LLM](24_INDOBERT_FINETUNING_LLM_REASONING_DETAIL.md), [25 — grade-aware training](25_GRADE_AWARE_ORDINAL_PIPELINE.md), [27 — operasional pilot](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md), [28 — topology dan integrasi target](28_END_TO_END_PERSONALIZED_ASSESSMENT_FLOW.md).
- [Laporan validasi AI aktif](../output/pretest/README.md), [kelas 1](../output/pretest/kelas1/hasil_validasi/README.md), [kelas 8](../output/pretest/kelas8/hasil_validasi/README.md). Report AI adalah state batch terkait dan dapat diperbarui; buka manifest/audit untuk version/hash yang benar.
- [`freeze_dataset_v2.py`](../scripts/freeze_dataset_v2.py), [`train_lora.py`](../app/training/v2/train_lora.py), [`artifact.py`](../app/classification/v2/artifact.py), [`assessment/store.py`](../app/assessment/store.py), [`psychometrics/analysis.py`](../app/psychometrics/analysis.py), [`psychometrics/irt.py`](../app/psychometrics/irt.py).

Animasi merangkum pipeline dan memperlihatkan perhitungan dengan angka contoh. Kontrak/kode/manifest per versi tetap menjadi rujukan untuk menjalankan sistem nyata.
