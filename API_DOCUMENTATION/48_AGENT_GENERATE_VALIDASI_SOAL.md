# Instruksi AI agent: kontribusi generate dan validasi soal

Dokumen ini dapat diberikan langsung kepada AI agent yang memiliki akses terminal
dan folder proyek **extraction_model**. Agent wajib membaca lalu melaksanakan
alur di bawah sesuai permintaan kontributor. Semua path relatif terhadap root
proyek; tidak bergantung pada nama pengguna atau drive komputer pembuat proyek.

**File ini adalah instruksi kerja beserta script/perintah untuk menjalankan kode
yang sudah ada.** Kontributor tetap membutuhkan salinan repository, sumber materi,
dan kredensial sendiri. Mengunggah Markdown ini saja ke chatbot tanpa akses repo
dan terminal tidak menyediakan program atau data proyek.

## 1. Cara memakai untuk kontributor baru

**Sebelum memberikan file ini ke agent**, ikuti
[panduan persiapan kontributor](49_PERSIAPAN_KONTRIBUTOR.md): akses proyek,
Python, paket sumber, API key Gemini pribadi, akses 9Router dan pengisian `.env`.
Panduan tersebut ditujukan kepada pemilik akun; dokumen ini mengatur eksekusi
oleh agent setelah kebutuhan tersedia.

1. Buka repository ini di IDE/terminal AI agent Anda.
2. Lampirkan file ini atau sebutkan path-nya.
3. Kirim instruksi berikut. Parameter boleh diganti sesuai pembagian kerja tim.

```text
Baca API_DOCUMENTATION/48_AGENT_GENERATE_VALIDASI_SOAL.md dan jalankan alurnya.
Saya ingin berkontribusi generate + validasi soal kelas1 pada batch baru.
Pilih bab/subbab dari sumber yang tersedia. Buat pilot 30 soal teks,
validasi Gemini N=3, batas generation 12 request dan validation 120 request.
Gunakan konfigurasi pribadi di .env. Lanjutkan semua tahap dalam batas tersebut,
termasuk approval manifest ketika generation lengkap, tanpa konfirmasi berulang.
Jika ada prasyarat yang belum tersedia, kerjakan pemeriksaan yang masih bisa
dilakukan dan laporkan prasyarat yang kurang. Simpan laporan kontribusi.
```

Untuk hanya menyiapkan pekerjaan, ganti permintaan menjadi `preflight saja`.
Untuk hanya membuat kandidat, tulis `generate saja, jangan mulai validasi`.
Perintah dari kontributor menentukan izin fase; jangan menganggap permintaan
generate saja sebagai izin validasi.

## 2. Kontrak kerja agent dan parameter

Tujuan: menghasilkan kandidat baru dari materi terverifikasi, menjalankan
validasi blind, dan menyerahkan soal beserta bukti yang dapat diperiksa tim.
Gunakan program existing; jangan membuat generator/validator pengganti hanya
untuk menjalankan panduan ini.

Jika parameter tidak diberikan, gunakan:

```yaml
kelas: kelas1
bab: auto_dari_kurikulum_dan_halaman_sumber
subbab: auto_dari_kurikulum_dan_halaman_sumber
batch: baru_otomatis_minimal_batch02
jumlah_kandidat: 30
persen_visual: 0
provider_generate: 9router_dari_env
provider_validasi: gemini
validation_runs: 3
max_generation_requests: 12
max_validation_requests: 120
```

- Kelas yang didukung: `kelas1` sampai `kelas12`, `kelas11_tl`, `kelas12_tl`.
- `jumlah_kandidat` pada jalur pilot ini harus 1–30. Plan membagi target
  easy/medium/hard berbobot 30/40/30 dengan pembulatan sesuai kode proyek.
- Default teks dipilih agar kontribusi tidak bergantung pada dukungan renderer.
  Jika diminta bergambar, misalnya `persen_visual: 70`, baca batas pada bagian 6.
- Gunakan `--book kelasN` saat generate dan `--classes kelasN` saat validasi.
  Batch generate berbentuk integer (`2`); batch validasi berbentuk `batch02`.
- Batas request bukan batas rupiah atau token. Jangan menaikkan anggaran,
  mengganti provider/model, atau menurunkan N=3 menjadi N=1 tanpa instruksi.
  Jika anggaran habis, simpan progres dan laporkan sisanya.
- Baca `AGENTS.md` yang berlaku jika tersedia. Periksa perubahan Git sebelum
  mengedit; pertahankan pekerjaan lain yang sudah ada.
- Kerjakan kelas dan batch yang dialokasikan. Jangan menjalankan validator
  tanpa `--classes`/`--batch`, karena default dapat mencakup pekerjaan tim lain.
- **Jangan menimpa `batch01` atau bukti lama.** Batch dengan
  `reference_replenishment_state.json` dan `reviewMode: local_without_external_api`
  memang menolak validasi API. Gunakan batch baru untuk kontribusi API ini.
- Jangan mengubah `validation_results.json` secara manual, memaksa status active,
  mengisi confidence fiktif, atau menggandakan ID untuk mengejar jumlah.
- Jangan mencetak/menyalin isi `.env`, API key, header Authorization, atau respons
  HTTP yang mengandung kredensial ke chat, log, laporan, maupun commit.

Alur utama:

```text
Setup -> preflight sumber -> plan -> generate kandidat -> cek manifest
      -> approval manifest -> stage -> blind validation -> audit -> laporan
```

## 3. Setup pada komputer teman

Semua contoh terminal menggunakan **PowerShell dari root repository**.
Gunakan Python 3.12 sesuai Dockerfile proyek. Jika `.venv` sudah ada, gunakan
environment itu; tidak perlu membuat ulang atau mengaktifkan Activate.ps1.

```powershell
# Hanya jika .venv belum ada; periksa versi Python lebih dahulu.
python --version
python -m venv .venv
if ($LASTEXITCODE -ne 0) { throw 'Pembuatan virtualenv gagal.' }

.\.venv\Scripts\python.exe -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) { throw 'Instalasi requirements gagal; periksa error.' }

# Pembaca Prasyarat_Math.xlsx mengimpor openpyxl; belum tercantum di requirements.txt.
.\.venv\Scripts\python.exe -m pip install openpyxl
if ($LASTEXITCODE -ne 0) { throw 'Instalasi pembaca Excel gagal.' }

if (-not (Test-Path -LiteralPath '.env')) {
    Copy-Item -LiteralPath '.env.example' -Destination '.env'
}
```

Jika dependency tidak tersedia untuk platform/Python tersebut, laporkan paket
dan errornya. Jangan mengganti pin versi proyek secara diam-diam.

Kontributor mengisi `.env` secara lokal. Agent boleh memeriksa konfigurasi melalui
loader proyek, tetapi hanya melaporkan nama variabel yang belum valid, bukan
nilainya. Minimum jalur default:

| Variabel | Kegunaan |
|---|---|
| `NINEROUTER_BASE_URL` | URL server 9Router kontributor, berakhiran `/v1` |
| `NINEROUTER_API_KEY` | Kredensial pribadi generator |
| `NINEROUTER_MODEL` | Model yang benar-benar tersedia di server tersebut |
| `GEMINI_API_KEY` atau `GEMINI_API_KEY_1` | Kredensial validator Gemini |
| `GEMINI_MODEL` | Model validator yang tersedia pada akun kontributor |

Nama model dan alamat LAN pada `.env.example` adalah contoh konfigurasi proyek,
bukan jaminan dapat digunakan oleh teman. `NINEROUTER_MODEL_SOLVER` tidak dipakai
pada fase generation-only ini. `--execute` pada runner validasi memberikan izin
live untuk invocation tersebut; jangan mengaktifkan seluruh layanan/scheduler
hanya untuk menjalankan kontribusi ini.

Tidak diperlukan MongoDB, S3, server FastAPI, atau data respons siswa untuk
generate + validasi file lokal ini. Artifact IndoBERT lokal diperlukan untuk
diagnostik model saat packaging; minta salinan artifact yang sesuai dari tim jika
runner membutuhkannya. Jangan membuat prediksi pengganti bila artifact hilang.

## 4. Sumber materi: jangan dilewati

Tim perlu memberikan file berikut melalui sarana berbagi proyek yang digunakan:

| Sumber | Lokasi/aturan |
|---|---|
| Kurikulum | `data/bab_prasyarat/Prasyarat_Math.xlsx`, sheet `Sheet2` dan `Per BAB` |
| Buku Siswa PDF | Di bawah `data/sd/`, `data/smp/`, atau `data/sma/` |
| Hasil ekstraksi buku | `data/processed/pretest_md/<kelas>/siswa/index.json` dan `pNNNN.md` |
| Artifact diagnostik bila diperlukan | `models/indobert-3x4x3-v1/`, utuh sesuai manifest/checksum |

Discovery PDF mengenali `panduan_siswa_kelas1.pdf` dan nama kelas lain dengan
pola yang sama. TL menggunakan suffix `_peminatan` atau `_tingkat_lanjut`,
misalnya `panduan_siswa_kelas11_tingkat_lanjut.pdf`. Key programnya `kelas11_tl`.

`data/sd`, `data/smp`, `data/sma`, `data/bab_prasyarat`, `data/processed`,
`models`, dan `runs` diabaikan Git. **Clone repository saja belum menyediakan
semua prasyarat.** Jangan membuat Excel/index/halaman kosong untuk meloloskan cek.
Jika belum ada ekstraksi buku, laporkan kebutuhan ekstraksi kepada tim; jalur ini
tidak otomatis mengubah atau mengekstrak ulang pretest.

Jalankan pemeriksaan offline; contoh memakai kelas1:

```powershell
$Book = 'kelas1'
$Py = Join-Path (Get-Location) '.venv/Scripts/python.exe'
if (-not (Test-Path -LiteralPath $Py)) { throw 'Virtualenv belum tersedia.' }

& $Py -X utf8 scripts/exercise_visual.py preflight --book $Book
if ($LASTEXITCODE -ne 0) { throw 'Sumber belum lengkap; baca missingInputs.' }
```

Laporan: `runs/exercise_visual/preflight_<kelas>.json`. Lanjut hanya jika
`status: ready`. Exit 2 / `waiting_for_sources` berarti laporkan daftar
`missingInputs` dengan jujur, tanpa panggilan API.

**Catatan pemeriksaan panduan, 8 November 2026:** preflight kelas1 pada workspace
penyusun menunjukkan Excel kurikulum, PDF, index dan halaman Markdown belum
tersedia. Ini catatan lokal saat penulisan; agent harus memeriksa ulang komputer
kontributor dan kelas yang dipilih.

Untuk mengetahui bab/subbab, gunakan loader kurikulum existing. Contoh ini
read-only; ganti `kelas1` bila kelas pekerjaan berbeda:

```powershell
@'
from app.services.pretest.agentic.kurikulum import load
for bab in sorted(load().values(), key=lambda b: (b.book, b.bab_no)):
    if bab.book == 'kelas1':
        print(bab.bab_no, bab.nama, bab.subbab)
'@ | & $Py -X utf8 -
if ($LASTEXITCODE -ne 0) { throw 'Pembacaan kurikulum gagal.' }
```

Agent membaca halaman sumber, memilih bab/subbab yang terdaftar dan materinya
cukup untuk jumlah soal, lalu mencatat pilihan itu dalam laporan. `bab 1 / A`
di contoh berikut hanya contoh; ganti dengan hasil pemeriksaan sumber. Jika
jumlah/visual yang diminta tidak layak, jelaskan kekurangannya sebelum mengubah
parameter atau mengeluarkan biaya.

## 5. Pilih batch baru dan bekukan plan

Pada kontribusi baru, pilih nomor terkecil mulai 2 yang belum dipakai baik di
output maupun checkpoint validasi. Pada resume, gunakan nomor pekerjaan semula;
jangan menjalankan pemilih batch baru lagi.

```powershell
$BatchNumber = 2
while ($true) {
    $BatchName = 'batch{0:D2}' -f $BatchNumber
    $Occupied = Test-Path -LiteralPath (Join-Path "output/exercise/$Book" $BatchName)
    foreach ($Scope in @('', 'groq', 'deepseek', 'failover')) {
        $CheckpointBase = Join-Path 'runs/exercise_validation' $Scope
        $Candidate = Join-Path $CheckpointBase "$BatchName/${Book}_exercise_$BatchName"
        if (Test-Path -LiteralPath $Candidate) { $Occupied = $true }
    }
    if (-not $Occupied) { break }
    $BatchNumber++
}
$Base = Join-Path "output/exercise/$Book" $BatchName

# Ganti dua nilai ini dengan bab/subbab yang sudah diperiksa pada tahap 4.
$Chapter = 1
$Subchapter = 'A'
$Total = 30
$VisualPercent = 0
$GenerationLimit = 12
$ValidationLimit = 120
$Runs = 3

& $Py -X utf8 scripts/exercise_visual.py plan --book $Book --batch $BatchNumber --bab $Chapter --subbab $Subchapter --total $Total --visual-percent $VisualPercent
if ($LASTEXITCODE -ne 0) { throw 'Plan gagal; jangan mulai generate.' }
```

Periksa `generation_plan.json`: class, batch, slot bab/subbab, total, proporsi
visual, dan hash sumber. Simpan identitas kelas/batch dan parameter dalam laporan
kontribusi sebelum API pertama. Plan tidak memanggil API. Jangan memodifikasi
plan yang sudah digunakan; perubahan cakupan/sumber memerlukan batch baru.

## 6. Generate kandidat dengan batas request

Jalankan bagian ini jika kontributor meminta generate. Ini dapat memakai kuota
atau menimbulkan biaya, termasuk ketika model di belakang 9Router adalah Gemini.

```powershell
& $Py -X utf8 scripts/exercise_visual.py generate --book $Book --batch $BatchNumber --max-api-calls $GenerationLimit --execute
$GenerationExit = $LASTEXITCODE

& $Py -X utf8 scripts/exercise_visual.py status --book $Book --batch $BatchNumber
if ($LASTEXITCODE -ne 0) { throw 'Status generation tidak dapat dibaca.' }
if ($GenerationExit -ne 0) { throw 'Generate gagal; periksa progres yang tersimpan.' }

$State = Get-Content -LiteralPath (Join-Path $Base 'generation_state.json') -Raw | ConvertFrom-Json
$Manifest = Get-Content -LiteralPath (Join-Path $Base 'generation_manifest.json') -Raw | ConvertFrom-Json
if ($State.phase -ne 'generation_complete' -or $Manifest.complete -ne $true) {
    throw 'Kandidat belum lengkap. Simpan progres; jangan approve atau validasi.'
}
```

Penting: exit code generate saja tidak membuktikan kuota kandidat lengkap.
Periksa `stopReason`, `file_dilewati`, state dan manifest. Generation mencakup
cek lokal schema, opsi unik, acuan, duplikasi, kuota dan aset; belum membuktikan
solusi, label atau status active. Kandidat tetap `validation_pending`.

Jika meminta visual, renderer existing terbatas pada kelompok objek
lingkaran/persegi/segitiga, pola bentuk dengan satu tempat kosong, dan jam analog
kelipatan lima menit. Agent memastikan tipe visual sesuai halaman sumber;
jangan memaksakannya untuk grafik/topik yang tidak didukung. Gambar harus
membawa informasi yang diperlukan untuk menjawab, dan ikut direview secara
visual saat tersedia alat penampil gambar. Simpan PNG/SVG/spesifikasi/provenance.

Resume generation menggunakan perintah generate yang sama. Limit generation
bersifat **kumulatif per batch**, termasuk retry transport, dengan rentang 1–100.
Mengulang limit 12 setelah 12 request terpakai tidak memberikan 12 request baru.
Periksa `generation_budget.json`; penambahan anggaran membutuhkan instruksi
kontributor. Jangan menghapus budget/checkpoint untuk mengulang jatah.

## 7. Approval manifest lalu validasi blind

Lanjut jika permintaan mencakup **generate + validasi** atau kontributor sudah
meminta mulai validasi. Jika izin itu sudah ada dan kandidat lengkap, agent
melakukan approval teknis berbasis hash berikut tanpa bertanya ulang.
Untuk `generate saja`, akhiri dengan laporan kandidat pending dan lewati tahap ini.

```powershell
$ManifestPath = Join-Path $Base 'generation_manifest.json'
$ManifestHash = (Get-FileHash -LiteralPath $ManifestPath -Algorithm SHA256).Hash.ToLowerInvariant()

& $Py -X utf8 scripts/exercise_visual.py approve-validation --book $Book --batch $BatchNumber --manifest-sha256 $ManifestHash
if ($LASTEXITCODE -ne 0) { throw 'Approval manifest gagal; jangan lanjut validasi.' }

& $Py -X utf8 scripts/validate_exercise_batch.py stage --classes $Book --batch $BatchName --provider gemini --runs $Runs
if ($LASTEXITCODE -ne 0) { throw 'Staging gagal; periksa sumber/checkpoint.' }

& $Py -X utf8 scripts/validate_exercise_batch.py run --classes $Book --batch $BatchName --provider gemini --runs $Runs --max-api-calls $ValidationLimit --max-output-tokens 4096 --stop-on-503 --execute
$ValidationExit = $LASTEXITCODE

& $Py -X utf8 scripts/validate_exercise_batch.py status --classes $Book --batch $BatchName --provider gemini
if ($LASTEXITCODE -ne 0) { throw 'Status validasi gagal dibaca.' }
if ($ValidationExit -ne 0) {
    Write-Output "Validasi berhenti dengan exit $ValidationExit; periksa checkpoint dan export_status.json."
}
```

Approval mengikat hash master, metadata, raw, aset dan plan. Setelah approval,
generation dibekukan. `approve-validation` juga menulis marker handoff untuk
nightly; cek proses yang berjalan agar satu batch hanya dikerjakan satu runner.
Gunakan namespace default pada contoh ini; jangan mencampur checkpoint
`failover`/provider lain saat resume.

`run` menjalankan pilot lalu full, memakai ulang run sukses, melakukan adjudikasi
N=3 bila dibutuhkan, dan memaketkan hasil/progres. Dengan 30 kandidat N=3,
minimal 90 evaluasi awal diperlukan; retry/adjudikasi dapat menghabiskan sisa
anggaran. Batas validation berlaku **per invocation**, bukan kumulatif. Catat
`apiAttempts` sebelum/sesudah di laporan dan jangan otomatis mengulang panggilan
live sampai melewati total batas pekerjaan yang disepakati.

Validator menilai isi, kunci, solusi minimum dan tiga head:
`mathCognitiveDomain`, `knowledgeDimension`, `intendedDifficulty`.
Jangan menyisipkan target generator sebagai label final atau memberikan kunci
generator sebagai bukti yang sudah benar. Jalur managed menyiapkan input blind.

Gemini digunakan pada panduan ini agar aset visual dapat dikirim sebagai gambar
nyata. Jangan fallback visual ke Groq/DeepSeek. N=1 hanya digunakan atas
permintaan kontributor; konsistensi antar-run tidak terukur dan tidak otomatis
memenuhi gate training N=3. Scope artifact IndoBERT yang didokumentasikan adalah
kelas 1–6 reguler; di luar scope hasil diagnostik abstain, bukan prediksi buatan.

## 8. Audit hasil dan arti kolom

```text
output/exercise/<kelas>/batchNN/
  generation_plan.json
  generation_state.json
  generation_budget.json
  generation_manifest.json
  validation_authorization.json
  babNN/<KODE>_<level>[_gambar].json
  assets/                              # jika ada gambar
  soal_exercise_db.json                 # envelope dengan items
  soal_exercise_meta.json               # dictionary per _id
  hasil_validasi/
    validation_results.json            # array hasil final/draft
    validation_results_meta.json       # metadata + validasi per _id
    export_status.json                 # kelengkapan dan progres
    manifest.json
    RINGKASAN_VALIDASI.md
    LAPORAN_VALIDASI.md
    bukti_validasi/

runs/exercise_validation/batchNN/<kelas>_exercise_batchNN/
  soal_exercise_db.json                 # array staging
  silver_labels.json                   # checkpoint API; jangan dihapus
  snapshots/                           # bukti/report per checkpoint
```

| Nilai/kolom | Arti |
|---|---|
| Nama raw `*_hard.json`, metadata `level_target: hard` | Sasaran generator |
| `cognitive_level: hard` pada hasil validasi | Difficulty final hasil penilaian, bukan label C1–C6 |
| `cognitive_score` 600/1000/1400 | Skor awal easy/medium/hard; bukan hasil IRT |
| `status: active` | Lolos qualification konten / silver_ready |
| `status: inactive` | Bisa draft, perlu revisi, atau belum qualified; baca metadata |
| `fullComplete: true` pada export_status | Semua penilaian sesuai mode dan adjudikasi yang diperlukan lengkap |
| `confidence_score: 0` | Tidak cukup untuk menyimpulkan gagal; periksa metode dan ketersediaan confidence |

N=3 menggunakan dukungan run awal terhadap label akhir sesuai kebijakan ekspor;
N=1 menggunakan diagnostik probabilitas model bila tersedia. Review lokal
memiliki provenance sendiri dan confidence dapat belum diukur. Tidak satu pun
boleh disebut akurasi empiris tanpa bukti respons siswa.

Agent wajib memverifikasi integritas bundle existing, relasi ID dan preservasi
field sumber. Jalankan dari root dengan `$Book` dan `$BatchName` pekerjaan ini:

```powershell
@'
import json
import sys
from collections import Counter
from pathlib import Path
from scripts.refresh_ai_validation_reports import verify_bundle

book, batch = sys.argv[1:3]
base = Path('output/exercise') / book / batch
stage = Path('runs/exercise_validation') / batch / f'{book}_exercise_{batch}'
bundle = base / 'hasil_validasi'
def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

verify_bundle(stage / 'soal_exercise_db.json', bundle)
source = read(base / 'soal_exercise_db.json')['items']
metadata = read(base / 'soal_exercise_meta.json')
result = read(bundle / 'validation_results.json')
result_meta = read(bundle / 'validation_results_meta.json')
ids = [str(q['_id']) for q in source]
assert ids and len(ids) == len(set(ids)), 'ID sumber tidak unik/kosong'
assert [str(q['_id']) for q in result] == ids, 'Urutan/ID ekspor berbeda'
assert set(metadata) == set(ids) == set(result_meta), 'Relasi metadata berbeda'
validation_fields = {'cognitive_level', 'cognitive_score', 'confidence_score', 'status'}
for original, exported in zip(source, result):
    assert set(original) == set(exported), original['_id']
    assert all(original[k] == exported[k] for k in original if k not in validation_fields), original['_id']
    assert exported['status'] in ('active', 'inactive'), original['_id']
progress = read(bundle / 'export_status.json')
summary = {
    'class': book, 'batch': batch, 'questionCount': len(result),
    'fullComplete': progress['fullComplete'],
    'status': dict(Counter(q['status'] for q in result)),
    'activeDifficulty': dict(Counter(q['cognitive_level'] for q in result if q['status'] == 'active')),
    'progress': progress['summary'], 'integrityVerified': True,
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
raise SystemExit(0 if progress['fullComplete'] else 2)
'@ | & $Py -X utf8 - $Book $BatchName
$AuditExit = $LASTEXITCODE
if ($AuditExit -ne 0) { Write-Output "Audit exit $AuditExit; jangan klaim seluruh batch selesai." }
```

Audit ini untuk jalur **Gemini/default namespace** di panduan ini. Bila validator
belum menghasilkan bundle, catat kondisi itu dan gunakan checkpoint/status untuk
melanjutkan; jangan membuat file hasil kosong supaya audit lolos.

Baca laporan per soal dan review kandidat yang ambigu, kunci berbeda, materi
melampaui kelas, atau level berbeda dari target. Label final boleh berbeda dari
target. Batch lengkap tidak berarti semua kandidat active. Jangan memaksa
distribusi hasil menjadi 30/40/30. Untuk gambar, periksa juga keterbacaan dan
kesesuaian gambar dengan soal, bukan checksum saja.

## 9. Resume dan penanganan masalah

Sebelum resume, pulihkan `$Py`, `$Book`, `$BatchNumber`, `$BatchName`, `$Base`
dari laporan pekerjaan. Baca state terlebih dahulu. Jangan mengulang `plan` atau
`generate` terhadap batch yang sudah `validation_authorized`.

```powershell
# Offline: cek status tanpa API. Status dapat menyiapkan ulang staging yang sama.
& $Py -X utf8 scripts/validate_exercise_batch.py status --classes $Book --batch $BatchName --provider gemini

# Offline: buat ulang laporan final/draft dari checkpoint existing.
& $Py -X utf8 scripts/validate_exercise_batch.py progress --classes $Book --batch $BatchName --provider gemini
```

Resume live menggunakan perintah `run` pada tahap 7 dengan kelas, batch,
provider dan mode run yang sama, serta **sisa anggaran yang masih diizinkan**
sebagai `--max-api-calls`. Jangan langsung menyalin batas 120 lagi jika sebagian
anggaran pekerjaan sudah terpakai. Respons sukses dipakai ulang.

| Kondisi | Tindakan agent |
|---|---|
| Sumber belum ada / `waiting_for_sources` | Laporkan missingInputs dan lokasi tujuan; hentikan API |
| API key/model/URL tidak valid, 401/403 | Laporkan variabel/provider yang perlu diperbaiki tanpa membocorkan nilainya |
| 429 / kuota atau anggaran habis | Pertahankan progres, hitung sisa; tunggu kuota/anggaran tersedia |
| 503 / jaringan bermasalah | Pertahankan checkpoint; resume sesuai batas, tanpa loop retry tak terbatas |
| `generation_incomplete` | Periksa raw/error/stopReason; jangan approve |
| `validation_pending` | Pastikan generation lengkap dan izin validasi ada; approve hash yang benar |
| Source/asset/hash berubah setelah approval/checkpoint | Pertahankan bukti; kerjakan revisi pada batch baru |
| `local_review_mode` / local publication protected | Gunakan batch baru; jangan hapus penahanan atau manifest lama |
| Lock batch / access denied Windows | Pastikan tidak ada penulis lain; laporkan file yang terkunci, jangan paksa hapus |
| Artifact model tidak tersedia | Laporkan kebutuhan artifact; jangan mengunduh/melatih model pengganti diam-diam |
| Final tapi inactive | Baca alasan qualification; revisi terpisah, jangan edit hasil jadi active |

## 10. Serah terima kontribusi

Simpan laporan di `runs/contributions/<kelas>_<batch>/LAPORAN_KONTRIBUSI.md`.
Buat laporan sejak parameter dibekukan dan perbarui ketika berhenti atau selesai.
Minimal isinya:

```text
Kontributor / tanggal:
Commit dasar repository:
Kelas / track / bab / subbab / batch:
Parameter jumlah, visual, runs, batas request:
Lokasi dan hash sumber; hash generation manifest:
Provider/model yang benar-benar dipakai (tanpa kredensial):
Generation: phase, kandidat/target, apiAttempts, stopReason:
Validation: fullComplete, final/draft, active/inactive, request terpakai:
Distribusi label final active; perbedaan dari target:
Hasil audit integritas, relasi ID, dan review gambar bila ada:
File hasil/bukti yang harus diserahkan:
Masalah yang belum selesai dan perintah resume dengan sisa anggaran:
```

Serahkan seluruh folder batch terkait beserta aset, checkpoint/bukti dan laporan
yang diperlukan untuk resume. `runs/` diabaikan Git sehingga laporan/checkpoint
perlu ikut paket serah terima melalui media tim. Untuk kontribusi melalui Git,
review diff lalu stage **hanya path kontribusi yang dimaksud**; jangan `git add .`
atau `git add -A` pada workspace yang berisi perubahan orang lain. File sumber
PDF/Excel, artifact besar dan kredensial dibagikan terpisah sesuai mekanisme tim.
Jangan push, merge, sinkronkan database production atau deploy hanya karena
generate dan validasi lokal sudah selesai.

Jawaban akhir agent kepada kontributor menyebut lokasi soal dan laporan, jumlah
kandidat, jumlah active/inactive/draft, kelengkapan validasi, request terpakai,
hasil audit dan hambatan nyata. Jika hanya preflight yang bisa berjalan, tulis
bahwa belum ada soal baru atau panggilan API; jangan mengklaim generate selesai.

## 11. Kontribusi pada bank lokal yang sudah ada

Repository juga memiliki jalur **generate + review lokal tanpa API eksternal**.
Itu berbeda provenance dari validasi blind Gemini di atas. Jika kontributor
secara khusus ditugaskan memperluas keluarga soal lokal, baca
`EXERCISE_TIGA_SESI.md`, `BANK_LATIHAN_SD.md`, modul
`app/services/exercise/session_expansion.py`, dan skrip
`scripts/extend_exercise_sessions_local.py` terlebih dahulu.

Runner tiga sesi adalah putaran existing dengan target tetap tiga sesi, bukan
generator umum untuk permintaan arbitrer. Menjalankannya kembali dapat hanya
melanjutkan atau mengaudit target yang sudah terpenuhi. Jangan mereset plan atau
menghapus checkpoint agar menghasilkan soal baru. Perubahan keluarga matematika
memerlukan review kode, uji perhitungan yang sesuai dan audit publikasi jalur
lokal. Catat `api_runs: 0` dan status training sesuai bukti; jangan menyebut
review lokal sebagai validasi API independen.

## Referensi kode dan penjelasan lanjutan

- [Generation/approval visual dan pemisahan fase](43_EXERCISE_VISUAL_GENERATION.md)
- [Kontrak validasi exercise dan ekspor](38_EXERCISE_BATCH_VALIDATION.md)
- [Nightly dan handoff](39_NIGHTLY_VALIDATION_AND_IRT.md)
- [Catatan bank tiga sesi lokal](../EXERCISE_TIGA_SESI.md)
- [CLI plan, generate, status, approval](../scripts/exercise_visual.py)
- [CLI validasi dan resume](../scripts/validate_exercise_batch.py)
- [Implementasi phase guard dan manifest](../app/services/exercise/workflow.py)
- [Verifikasi bundle](../scripts/refresh_ai_validation_reports.py)

Jika dokumentasi lama berbeda, periksa implementasi dan `--help` pada checkout
yang sedang dipakai. Laporkan ketidaksesuaian; jangan melepas guard integritas.
