# Rubrik v8, validasi semua kelas, training dan persiapan IRT

Rubrik v8 memperjelas batas Easy–Medium–Hard relatif terhadap kelas sasaran.
Prosedur familiar dapat Hard jika siswa harus merencanakan dan mengintegrasikan
hubungan atau kendala dengan sedikit bantuan. Banyak operasi, angka besar atau
stem panjang saja tidak cukup. Label mengikuti bukti, tanpa persentase target
dan tanpa menjanjikan distribusi normal.

## Versi dan cakupan

- `configs/rubric_math_3x4x3_v8_sd.yaml`: SD kelas 1–6.
- `configs/rubric_math_3x4x3_v8_smp7.yaml` sampai `v8_smp9.yaml`: SMP.
- `configs/rubric_math_3x4x3_v8_sma10.yaml` sampai `v8_sma12.yaml`: SMA reguler.
- `configs/rubric_math_3x4x3_v8_sma11_tl.yaml` dan `v8_sma12_tl.yaml`: SMA TL.
- `app/llm/silver.py`: dispatch versi, prompt v10, definisi dibaca dari YAML.

YAML dan checkpoint lama tidak ditimpa. Resume menolak source, model, versi
prompt, hash rubrik atau track yang berbeda. Pilot tetap memakai sumber lengkap
yang tidak berubah, sehingga panggilan suksesnya dapat digunakan pada batch penuh.

## Eksekusi

Jalankan dari root proyek menggunakan Python pada `.venv`. Kunci Gemini tetap
di `.env` atau environment; jangan memasukkannya ke log atau perintah.

```powershell
# Persiapan offline: 14 kelas/track, checkpoint dan laporan rencana.
.\.venv\Scripts\python.exe scripts/revalidate_all_grades.py --batch-name rubric_v8_20261005_v1

# Respons lebih panjang untuk mengurangi risiko keluaran terpotong.
$env:GEMINI_MAX_OUTPUT_TOKENS = '4096'
.\.venv\Scripts\python.exe scripts/revalidate_all_grades.py --batch-name rubric_v8_20261005_v1 --execute --train
```

Perintah kedua dapat dilanjutkan dengan batch name yang sama setelah kuota
tersedia. Run dan adjudikasi sukses tidak dibayar ulang. Pilih batch baru untuk
perubahan rubrik, sumber, atau model. Jangan menjalankan dua proses pada batch
yang sama sekaligus.

Urutannya: dua sampel per kelas/track, verifikasi hash bukti, perbandingan pilot,
batch penuh kelas 1–12 reguler dan kelas 11–12 TL, packaging offline, kemudian
persiapan dataset dan training jika gate data terpenuhi.

Reviewer menerima soal, opsi, gambar dan rubrik; label sebelumnya dipakai untuk
pemilihan sampel saja. Tiga run blind dinilai terlebih dahulu. Ketidaksepakatan,
abstention dan masalah isi/kunci diperiksa dengan adjudikasi terpisah.

## Batas API dan status berhenti

Default `--max-api-calls 2500` membatasi panggilan aplikasi seluruh batch,
termasuk retry dan adjudikasi, bukan token dan bukan saldo akun. Untuk 580 soal,
run awal memerlukan 1.740 panggilan; adjudikasi dapat menambah hingga 580 sebelum
retry. Hasil pilot merupakan bagian dari angka ini, bukan tambahan run awal.

Eksekusi serial berhenti pada 429 pertama. Rate limit jangka pendek dan kuota
harian dapat berbeda; jenis batas dicatat jika provider memberikan quota ID.
Tidak ada percobaan berulang setelah 429 dan tidak ada perpindahan model/key.
SDK dapat melakukan retry pada kegagalan 5xx; angka aplikasi tidak sama dengan
jumlah semua request HTTP. Sebagian respons gagal sebelum penggunaan token
dapat dicatat; laporan penggunaan sukses tidak menyatakan total tagihan akun.

| Status | Makna |
|---|---|
| `blocked_provider_daily_quota` | Provider menyatakan kuota harian habis |
| `blocked_provider_quota_or_rate_limit` | 429, jenis batas belum dipastikan |
| `blocked_provider_configuration` | Kesalahan key/model/konfigurasi; seluruh batch berhenti |
| `stopped_api_call_budget` | Batas lokal panggilan aplikasi tercapai |
| `stopped_incomplete_provider_evidence` | Run belum lengkap atau adjudikasi belum selesai |
| `training_blocked_quality_gates` | Validasi selesai, tetapi data training belum memenuhi gate |

## Lokasi dan integritas hasil

- `runs/<batch>/execution.json` dan `REPORT.md`: status seluruh kelas.
- `runs/<batch>/pilot_comparison.json`: label sebelum/sesudah untuk sampel.
- `output/pretest/<kelas>/<batch>/silver_labels.json`: checkpoint kerja.
- `output/pretest/<kelas>/<batch>/final_snapshot_v1/`: bukti terkunci,
  audit, bundle baru, dan `previous_active_report`.
- `output/pretest/<kelas>/hasil_validasi/validation_results.json`: array soal
  dengan schema sumber yang sama, diperbarui hanya setelah kelas tersebut selesai.

Kelas yang belum selesai tetap memakai hasil aktif sebelumnya; laporan batch
menyatakan kelas mana yang sudah diperbarui. Label baru tidak dicampur dengan
label historis untuk menyatakan dataset training v8 selesai.

`cognitive_level` adalah `easy`, `medium`, atau `hard`; `cognitive_score` tetap
600, 1000, atau 1400 sebagai skor awal. `confidence_score` adalah dukungan tiga
run awal terendah pada tiga head terhadap label final, bukan probabilitas
kebenaran. Adjudikasi tidak menjadi suara keempat. `status` active/inactive
tetap mengikuti qualification isi, kunci, solusi dan gambar.

## Fine-tuning

`scripts/prepare_allgrade_retraining.py` memverifikasi semua 14 bundle terhadap
rubrik terbaru sebelum membuat snapshot. Dukungan model baru meliputi grade
embedding hingga kelas 12, penanda TL pada input, dan metrik serta kalibrasi
terpisah per kelas/track. Artefak SD lama tetap memiliki scope semula.

Pembobotan loss untuk ketimpangan label sudah tersedia. Jumlah minimum tiap
label pada train/validation/test dan pengelompokan sumber tetap berlaku.
Kegagalan gate dilaporkan dalam `training_attempt_<n>/readiness.json`; tidak
diatasi dengan memindahkan label agar mencapai kuota. Artefak baru disimpan
terpisah dan tidak otomatis disetujui untuk produksi. Diagnostik model baru
memakai keputusan blind yang sama dan memeriksa array soal tidak berubah.

## IRT

`bukti_validasi/irt_initialization.json` mencatat skor awal, item qualified,
versi/hash konten, kelas/track, dan ketersediaan respons siswa. Sidecar dan hash
manifest tidak menambahkan field ke `validation_results.json`.

`scripts/psychometrics.py prepare-pilot` menyiapkan blueprint assessment dari
snapshot qualified tanpa membuat peserta atau respons. Kalibrasi Rasch/IRT
memerlukan respons siswa nyata dan pemeriksaan matrix/assumptions melalui
alur `screen` yang sudah ada. Intended difficulty dan skor awal tidak menjadi
parameter empiris a/b/c atau kemampuan theta. Data kelas/track berbeda tidak
digabung otomatis. Tanpa respons yang cocok, status adalah `waiting_for_data`.

## Bank dengan distribusi mendekati sepertiga

Untuk menjalankan validasi dan menghasilkan label bank operasional yang
diminta pengguna, gunakan batch yang sama agar run sukses tidak diulang:

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS = '4096'
.\.venv\Scripts\python.exe scripts/revalidate_all_grades.py --batch-name rubric_v8_20261005_v1 --execute --train --balance-bank --export-progress
```

`--balance-bank` mengurutkan soal aktif menggunakan profil kesulitan yang
tersimpan, kemudian membagi kelompok Easy, Medium, Hard dengan selisih jumlah
maksimal satu soal. Soal inactive tetap inactive dan tidak dihitung dalam kuota.
Ini adalah kategori relatif pada bank masing-masing kelas. Profil yang skornya
sama dapat terpisah oleh batas kuota; urutan sumber menjadi pemecah seri dan
kejadian tersebut dicatat dalam audit. Formula heuristik belum dikalibrasi
terhadap hasil siswa. Distribusi seragam ini bukan distribusi normal statistik.

Setelah validasi sebuah kelas selesai dan bundle AI diperiksa, pipeline
menyimpan versi bank di:

- `output/pretest/<kelas>/operational_balance_v2/current.json`: pointer ke versi terbaru.
- `operational_balance_v2/source_<fingerprint>/validation_results.json`: array bank seimbang.
- Folder versi yang sama memuat `ai_validation_results.json`, `ai_decisions.json`,
  `balance_audit.json`, `source_manifest.json`, dan manifest hash ekspor.
- `runs/<batch>/operational_balance_summary.json`: status semua 14 kelas/track.

Ekspor dengan sumber dan keputusan yang sama diverifikasi dan digunakan kembali.
Keputusan baru membuat versi baru; ekspor v1 dan versi terdahulu tetap tersedia.
`confidence_score` mempertahankan makna dukungan run AI asli terhadap label
operasional. Label kuota yang tidak didukung AI dapat memiliki confidence 0;
jumlah dan dukungan tiap head tercatat dalam `balance_audit.json`.

`hasil_validasi/validation_results.json` sekarang menyimpan label bank relatif
yang telah dipublikasikan, dengan schema `soal_pretest_db.json` yang sama.
`hasil_validasi/ai_validation_results.json` mempertahankan klasifikasi blind
Gemini byte-for-byte. Training dan IRT membaca arsip AI melalui
`app.silver.exports.ai_validation_path`; audit Gemini tidak diubah. Ekspor relatif memiliki
provenance `relative_bank_quota`; ekspor ini tidak didaftarkan sebagai `ai_silver`
dan bukan kalibrasi IRT. Skor 600/1000/1400 pada ekspor merupakan pemetaan
kategori operasional, bukan estimasi parameter item.

Publikasi offline seluruh 14 kelas tersedia melalui:

```powershell
.\.venv\Scripts\python.exe scripts/publish_operational_bank.py
```

Publikasi memakai bukti aktif yang tersedia. Manifest mencatat
`databaseExport.operationalBalance.newRubricValidationComplete`: false berarti
bank relatif masih bersumber dari rubrik sebelumnya karena v8 belum selesai.
`--balance-bank` pada runner mempublikasikan ulang bank tiap kelas setelah
revalidasi kelas tersebut selesai, sehingga resume mempertahankan format ini.

`--export-progress` memperbarui array final/draft di folder batch ketika seluruh
pekerjaan selesai atau proses berhenti. Item belum selesai memiliki label/skor
null, confidence 0 dan status inactive. Pada 429 pertama, seluruh panggilan
Gemini berhenti; penyimpanan ekspor progres berikutnya berjalan offline.
