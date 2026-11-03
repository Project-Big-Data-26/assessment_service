# Exercise visual: generate dahulu, validasi terpisah

Implementasi baru memakai `scripts/exercise_visual.py`. Tujuan pilot: maksimal
30 kandidat dengan target 70% visual dan difficulty 30/40/30; target tersebut
tidak mengubah label AI, alokasi operasional relatif, atau hasil IRT.

## Perintah dan prasyarat

Semua perintah dijalankan dari root proyek dengan PowerShell. `--book` mendukung
kelas 1–12 serta 11/12 TL. Pilih batch baru; jangan menimpa batch berbayar lama.

```powershell
# Offline: cek sumber dan tulis laporan ke runs/exercise_visual/.
.\.venv\Scripts\python.exe -X utf8 scripts/exercise_visual.py preflight --book kelas1 --batch 2
```

Sumber wajib: `data/bab_prasyarat/Prasyarat_Math.xlsx`, PDF Buku Siswa asli di
lokasi discovery buku, serta `data/processed/pretest_md/<kelas>/siswa/index.json`
dan halaman `pNNNN.md`. `plan` memeriksa bab/subbab terhadap kurikulum, rentang
halaman dan checksum seluruh sumber. Tidak ada fallback yang mengarang kurikulum.

Pada audit implementasi, semua sumber itu belum tersedia untuk kelas 1. Git
history lokal juga tidak memiliki file Prasyarat_Math.xlsx pada lokasi tersebut.
Karena itu **belum ada generate soal nyata atau panggilan API baru**.

Setelah sumber dipulihkan, pilih bab/subbab yang benar. Contoh berikut hanya
berlaku bila bab 1/subbab A ada dan materinya cukup untuk pilot:

```powershell
# Offline: susun dan bekukan rencana; tidak memanggil model.
.\.venv\Scripts\python.exe -X utf8 scripts/exercise_visual.py plan --book kelas1 --batch 2 --bab 1 --subbab A --total 30 --visual-percent 70

# BERBAYAR: generate kandidat saja, setelah pengguna memerintahkan JALANKAN PILOT.
.\.venv\Scripts\python.exe -X utf8 scripts/exercise_visual.py generate --book kelas1 --batch 2 --max-api-calls 12 --execute

# Offline: status, jumlah, distribusi target, manifest hash, dan izin validasi.
.\.venv\Scripts\python.exe -X utf8 scripts/exercise_visual.py status --book kelas1 --batch 2
```

Provider generation memakai konfigurasi `NINEROUTER_*` yang sudah ada. Jangan
menampilkan key. Maksimum request bersifat kumulatif per batch, termasuk retry
transport pada client. Resume memakai kandidat yang tersimpan. Naikkan limit
secara eksplisit jika memang ingin menambah anggaran. HTTP 401/403/429/503
menghentikan generation, menyimpan progres dan tidak memicu validator.

Tidak ada klaim harga atau kemampuan dari nama model saja. Jika model generator
lewat 9Router adalah Gemini, generation tetap mengonsumsi kuota Gemini.

Antrean lama memiliki `--generation-only --max-api-calls N`; batch baru dan
batch yang sudah dikelola fase otomatis memakai generation-only. Antrean
generation-only melewati `kerjakan_slot`/solver. Untuk pilot dengan pembagian
modalitas, gunakan plan di atas; antrean tanpa plan tetap memakai kuota teks
legacy. Batas slot/waktu antrean tidak boleh dipakai untuk mengubah plan diam-diam.

CLI export juga menerima:

```powershell
.\.venv\Scripts\python.exe -m app.services.exercise.export --book kelas1 --batch 2 --generation-only
```

Ekspor baru default pending. Ekspor ulang batch managed tetap pending, tidak
membuat approval atau memanggil Gemini. Batch lama tanpa dokumen fase tetap
menggunakan mekanisme resume lama. Proses lama kelas lain tidak dinonaktifkan.

## Gambar dan pemeriksaan lokal

Renderer saat ini mendukung tiga spesifikasi terstruktur: kelompok objek
lingkaran/persegi/segitiga, pola bentuk dengan satu tempat kosong, dan jam analog
dengan kelipatan lima menit. Pilih hanya bentuk yang sesuai halaman sumber.
Belum mencakup ilustrasi bebas, grafik kompleks, atau seluruh topik semua kelas.

Kode menghasilkan SVG, PNG dan provenance: sumber `generated_svg`, versi
renderer, semanticSpec, ukuran, checksum SVG/PNG. Fakta visual diperiksa secara
lokal terhadap spesifikasi; jawaban kandidat tetap belum diverifikasi. Status
kebutuhan gambar adalah `pending_independent_validation`, bukan klaim esensial
yang sudah dibuktikan. Gambar tidak mengandalkan warna sebagai satu-satunya kode.

Generation memeriksa schema, kuota plan, opsi unik, acuan, duplikasi serta file
dan checksum aset. Pemeriksaan ini tidak menjalankan solver atau API validasi.
Gambar turunan dipaketkan sebagai path relatif `assets/...` pada master.

## Dokumen fase dan hasil

```text
output/exercise/<kelas>/batchNN/
  generation_state.json             # generating / generation_complete / generation_incomplete
  generation_plan.json              # alokasi dan hash sumber pilot
  generation_budget.json            # request generation kumulatif
  generation_manifest.json          # hash master/meta/raw/aset, jumlah, target
  babNN/<K>_<level>[_gambar].json    # kandidat dan spesifikasi visual
  assets/                           # SVG, PNG, provenance
  soal_exercise_db.json              # envelope items, kolom validasi tetap null
  soal_exercise_meta.json            # per _id, target dan provenance
  per_subbab/                       # lembar koreksi, ditandai belum validasi AI
```

`generation_complete` berarti rencana kandidat terpenuhi dan cek lokal lolos.
`validation_pending` tetap berlaku. Jika ada kandidat kurang/berkas dilewati,
manifest tidak dapat diizinkan untuk validasi. Tidak ada validation_results palsu.
Generation dan validation memiliki checkpoint terpisah.

Batch lock OS yang sama dipakai generation, export, approval dan CLI validation.
Lock dilepas OS saat proses mati. File sementara checkpoint memakai nama unik;
bila Windows terus mengunci tujuan, file lengkap tersisa untuk recovery. Ini
mencegah benturan nama silver_labels.json.tmp pada dua penulis.

## Mulai validasi hanya setelah instruksi terpisah

Setelah pengguna mengatakan **MULAI VALIDASI**, gunakan hash yang dilaporkan:

```powershell
# Ganti HASH_MANIFEST dengan SHA256 dari status. Ini mengizinkan jadwal malam
# untuk memproses batch; tidak membuat panggilan API dengan sendirinya.
.\.venv\Scripts\python.exe -X utf8 scripts/exercise_visual.py approve-validation --book kelas1 --batch 2 --manifest-sha256 HASH_MANIFEST

# BERBAYAR: validasi langsung, atau tunggu runner nightly 01.00 WIB.
.\.venv\Scripts\python.exe -X utf8 scripts/validate_exercise_batch.py run --classes kelas1 --batch batch02 --provider gemini --checkpoint-namespace failover --runs 1 --max-api-calls 60 --execute
```

Approval terikat class/batch dan manifest SHA256. Perubahan teks, raw kandidat,
spesifikasi atau byte aset membatalkan approval. Sesudah approval, generation
dibekukan; revisi isi menggunakan batch baru. Nightly, bootstrapJobs, stale
extraction marker, CLI validator, solver terpisah dan labeler bertahap semuanya
memeriksa fase; waktu berlalu tidak pernah melepaskan batch pending.

Adapter visual yang didukung pada jalur silver ini adalah Gemini. Groq/DeepSeek
tidak dipakai sebagai fallback visual. PNG/JPEG/WebP dikirim sebagai gambar
sebenarnya, bukan sekadar nama file/transkrip. Input staging memasukkan hash
byte aset, sehingga checkpoint berbayar tidak dipakai ulang untuk gambar berbeda.

Untuk batch managed baru, prompt blind tidak menyertakan kunci generator atau
alasan opsi. Validator menyelesaikan dari teks/opsi/gambar dan menulis fakta
visual. Audit gambar memeriksa keterbacaan, konsistensi dan kebutuhan informasi;
gambar dekoratif/ambigu ditandai concern/insufficient_evidence. Satu jawaban
benar tanpa gambar tidak otomatis membuktikan gambar tidak diperlukan.

Setelah validasi, exporter existing tetap menghasilkan:

```text
hasil_validasi/
  validation_results.json
  validation_results_meta.json
  export_status.json
  manifest.json
  LAPORAN_VALIDASI.md
  ...bukti validasi dan turunan sesuai kontrak existing
```

Field resmi, ID dan hubungan master/meta dipertahankan. Partial/draft berbeda
dari lengkap. N=1 tidak otomatis memenuhi syarat tiga run blind pada dataset
training AI silver lama. IRT memerlukan respons server-scored yang nyata, dan
fine-tuning empiris tetap menunggu gate data serta menghasilkan challenger
research-only. Tidak ada sinkronisasi otomatis ke backend eksternal di fitur ini.
