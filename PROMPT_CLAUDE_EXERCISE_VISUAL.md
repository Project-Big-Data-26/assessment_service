# Prompt untuk Claude Code: exercise visual dan otomasi validasi

Salin bagian di bawah ke Claude Code yang membuka repository ini. Jika memakai
chat Claude biasa, berikan file kode yang diminta; chat tidak boleh mengaku sudah
membaca atau mengubah repository tanpa akses tersebut.

---

Kamu bertugas membantu mengembangkan bank soal matematika di repository lokal:

`D:\KULIAH\Big Data\extraction_model`

Shell: PowerShell, Python: `.\.venv\Scripts\python.exe`, zona waktu Asia/Jakarta.

Saya ingin exercise mayoritas bergambar, terutama kelas 1–4 yang belum memiliki
exercise. Kerjakan audit, implementasi, dan tes secara bertahap. Jangan langsung
generate massal. Jangan menghapus pekerjaan atau hasil validasi yang sudah ada.
Jangan tampilkan isi `.env`, API key, atau kredensial ke terminal, laporan, atau git.

## 0. Prioritas terbaru: generate dahulu, validasi belakangan

Instruksi bagian ini mengesampingkan alur lama yang langsung memvalidasi setelah
generate. Fokus tahap pertama adalah menyelesaikan generate kandidat dan aset.
Jangan menjalankan solver blind, validasi LLM/Gemini, pemeriksaan tanpa gambar
berbasis API, IRT, atau fine-tuning untuk batch baru ini selama fase generate.
Pemeriksaan lokal tanpa API tetap berjalan: schema, ID, file gambar, checksum,
render, fakta gambar yang dapat dihitung, opsi, duplikasi, dan konsistensi ekspor.

Alasan: kuota/API Gemini untuk validasi perlu dipakai pada tahap terpisah;
jangan membuat generate dan validasi berebut kuota atau berjalan bersamaan.
Jika generator sendiri memakai Gemini, jelaskan bahwa generate tetap memakai
kuotanya. Tidak adanya validasi paralel bukan jaminan API tidak akan mencapai
batas. Bedakan penggunaan Claude interaktif dari API provider yang benar-benar
tersedia; jangan mengasumsikan langganan Claude memberikan API key.

Implementasikan pemisahan fase yang nyata, bukan hanya janji di laporan:

- Sediakan mode eksplisit `generation-only` pada antrean/pilot dan ekspor.
  Nama flag akhir boleh mengikuti gaya repo, tetapi tuliskan perintah persisnya
  setelah diimplementasikan. Ini permintaan fitur, bukan klaim flag sudah ada.
- Antrean sekarang memanggil `kerjakan_slot` yang dapat melakukan solver dan
  repair berbasis API. Mode generate harus menghindari seluruh rangkaian itu;
  gunakan jalur generate kandidat tanpa memanggil solver, lalu cek lokal saja.
- Tulis status terpisah `generation_complete` dan `validation_pending` beserta
  manifest jumlah soal, kelas/batch, hash teks/aset, serta distribusi target.
  Status tersebut bukan bukti bahwa jawaban atau level sudah tervalidasi.
- Jangan menerbitkan `extraction_ready.json` yang memicu validasi untuk batch
  baru selama validasi masih ditunda. Gunakan marker/status generation terpisah.
- Lindungi batch baru dari auto-hook antrean, CLI export, `bootstrapJobs`, dan
  Task Scheduler pukul 01.00. Runner harus mengecek persetujuan fase yang sama,
  termasuk jika proses dimulai ulang atau marker lama masih ada. Jangan sekadar
  menonaktifkan satu pemanggilan CLI. Jangan hentikan pekerjaan lama kelas lain.
- Izin validasi harus merujuk hash manifest generation; perubahan teks/gambar
  membatalkan izin itu. Default batch baru adalah belum diizinkan divalidasi.
- Tidak ada auto-release berdasarkan jam, timeout, atau selesai generate.
  Tunggu instruksi saya `MULAI VALIDASI` untuk batch yang sudah dilaporkan.
- Izin `JALANKAN PILOT` hanya mengizinkan generate pilot; tidak sekaligus
  mengizinkan validasi API atau generate massal.
- Buat tes bahwa fase generate, finalisasi, ekspor, pemanggilan ulang, dan
  nightly tidak memanggil API validasi untuk batch yang masih pending.

Setelah generation selesai, laporkan kandidat, aset, pemeriksaan lokal,
distribusi TARGET, masalah, hash manifest, dan perintah untuk fase validasi.
Jangan melaporkan jumlah "lolos validasi AI" sebelum fase itu dijalankan.

## 1. Konteks dan kondisi terakhir

- Inventaris terakhir: exercise kelas 5–12 termasuk 11 TL dan 12 TL berjumlah
  8.332 soal; semuanya tidak memiliki `image_url`. Kelas 1–4 belum memiliki
  file exercise maupun hasil generate. Hitung ulang sebelum membuat rencana.
- Pretest terpisah berjumlah 580 soal, 150 memiliki referensi `image_url`.
  Referensi tersebut belum membuktikan file gambar tersedia atau sesuai untuk
  dipakai ulang. Jangan menghitungnya sebagai 150 aset unik atau exercise baru.
- Generator saat ini mendukung mode `--gambar`, tetapi hanya mengambil gambar
  pretest pada subbab terkait. Konfigurasi sekarang membatasi maksimal 5 soal
  gambar per level/subbab dan penggunaan ulang satu gambar maksimal 2 soal
  per level. Itu belum cukup untuk menyimpulkan target dominasi gambar bisa tercapai.
- Kuota teks lama: SD 10, SMP 15, SMA 20 soal PER LEVEL PER SUBBAB. Tiga level
  menghasilkan bank 30/45/60 soal dengan pembagian awal sekitar sepertiga-sepertiga.
- Ekspor operasional memiliki pembagian relatif per bab 30/40/30. Pembagian
  bank tersebut bukan bukti bahwa soal secara intrinsik mudah/sedang/sulit.
- Validasi exercise saat ini menolak `image_url` nonkosong. Handoff otomatis
  juga hanya menerima batch teks. Jangan sekadar menghapus pemeriksaan ini.
- Daftar kelas pada validator/nightly sekarang hanya kelas 5–12 dan TL;
  dukungan validasi exercise kelas 1–4 perlu diperiksa dan ditambahkan dengan
  rubric yang sesuai, bukan diasumsikan sudah tersedia.
- File kurikulum yang diharapkan,
  `data/bab_prasyarat/Prasyarat_Math.xlsx`, tidak ditemukan pada pengecekan
  terakhir. Telusuri sumber resmi lain yang sudah ada di repo/riwayat lokal.
  Jika tetap tidak ada, laporkan input yang diperlukan; jangan mengarang subbab
  atau menetapkan jumlah total soal berdasarkan perkiraan.
- Perubahan otomasi sebelumnya mungkin masih belum di-commit. Baca `git status`
  dan diff, pertahankan perubahan tersebut. Jangan reset atau overwrite.

## 2. File yang perlu dibaca

Cari `AGENTS.md` yang berlaku, lalu periksa:

- `.claude/skills/generate-soal-exercise/SKILL.md`: aturan lama menyebut teks saja.
- `app/services/exercise/config.py`, `schema.py`, `llm_generate.py`,
  `llm_verify.py`, `llm_pipeline.py`, `validate.py`, `verify.py`, `export.py`, `handoff.py`.
- `scripts/generate_exercise_9router.py`, `verify_exercise_9router.py`,
  `run_exercise_queue.py`, `validate_exercise_batch.py`, `nightly_pipeline.py`,
  `provider_failover.py`, `empirical_finetuning.py`.
- `configs/nightly_pipeline.json` dan
  `API_DOCUMENTATION/39_NIGHTLY_VALIDATION_AND_IRT.md`.
- Kode rubric/pelabelan pada `app/llm/`, training di `app/training/v2/`,
  serta assessment/psikometrik di `app/assessment/` dan `app/psychometrics/`.
- Tes yang terkait generator gambar, validasi, handoff, nightly, dan feedback.

Instruksi saya memperluas dukungan ke exercise visual. Perbarui panduan teks-saja
yang bertentangan setelah implementasi, sambil mempertahankan pemeriksaan mutu
yang relevan. Jangan menganggap aturan lama tersebut sudah mendukung visual.

## 3. Target konten dan kesulitan

Gunakan kebijakan konfigurabel berikut sebagai USULAN AWAL saya:

- 70% soal memerlukan informasi visual, 30% soal teks.
- Target generation difficulty: 30% easy, 40% medium, 30% hard.
- Contoh bank 100 soal:

  | Bentuk | Easy | Medium | Hard | Total |
  |---|---:|---:|---:|---:|
  | Visual | 21 | 28 | 21 | 70 |
  | Teks | 9 | 12 | 9 | 30 |
  | Total | 30 | 40 | 30 | 100 |

Angka ini adalah kebijakan perencanaan, bukan standar ilmiah wajib. Terapkan
per bab jika materi mendukung. Jika ada subbab yang tidak cocok untuk visual,
laporkan kapasitas sebenarnya dan kompensasikan di tingkat bab; jangan memaksakan
gambar dekoratif atau soal duplikat. Jangan memaksakan persentase pada setiap
subbab kecil. Gunakan pembulatan deterministik dengan total yang tetap tepat.

Pisahkan dan laporkan:

1. `level_target`: sasaran saat generate.
2. Label AI hasil validasi blind beserta confidence, provenance dan rubric.
3. Label/alokasi operasional relatif untuk kebutuhan distribusi bank.
4. `empiricalDifficulty`: hasil IRT untuk versi soal dan populasi tertentu.

Jangan mengganti label hasil validasi agar terlihat memenuhi kuota. Jika distribusi
validasi meleset, perbaiki atau tambah kandidat pada level yang kurang. Soal yang
ditahan tidak dihitung sebagai bank aktif. Tampilkan distribusi sebelum dan
sesudah seleksi, termasuk jumlah ditolak dan tertunda.

Difficulty tidak ditentukan dari panjang teks, banyaknya gambar, jumlah langkah,
atau C1–C6 saja. Gunakan rubric per kelas: kebutuhan inferensi, transfer konsep,
representasi, dan kemandirian strategi. Hard kelas 1 tetap sesuai materi kelas 1.
Label kognitif, dimensi pengetahuan, dan kesulitan merupakan dimensi terpisah.

## 4. Kebijakan gambar

Yang dihitung dalam 70% haruslah visual yang diperlukan untuk menyelesaikan soal:
misalnya menghitung objek, membandingkan kelompok, pola, nilai tempat, posisi,
bangun, jam, pengukuran, piktogram, diagram, atau grafik sesuai kurikulum kelas.
Gambar hiasan saja tidak dihitung sebagai soal visual.

Prioritaskan aset matematika deterministik dari SVG atau renderer programatik
untuk jumlah objek, label, ukuran dan koordinat yang harus tepat. Aset raster
boleh untuk ilustrasi yang sesuai, tetapi tetap diverifikasi. Gunakan alat yang
benar-benar tersedia; jangan mengaku berlangganan Claude otomatis menyediakan
API generator gambar atau provider berbayar lain.

Untuk setiap aset simpan ID, path, checksum, sumber, spesifikasi semantik, dan
lisensi/izin bila mengambil dari sumber luar. Bedakan `source=pretest_reuse`,
`generated_svg`, `generated_raster`, atau jenis lain yang memang digunakan.
Jangan memalsukan asal atau referensi buku.

Periksa jumlah objek, angka, satuan, label, skala, arah, warna, resolusi, margin,
keterbacaan dan kesesuaian dengan opsi. Jangan mengubah angka pertanyaan sambil
mempertahankan gambar lama yang bertentangan. Jangan memakai warna sebagai
satu-satunya pembeda. Hindari identitas siswa atau foto pribadi.

Pisahkan fakta visual/transkrip dari jawaban dan pembahasan. Transkrip boleh
membantu pipeline teks setelah diverifikasi, tetapi tidak boleh membocorkan
jawaban atau menggantikan inspeksi gambar yang sebenarnya.

## 5. Alur teknis yang harus diwujudkan

Fase A — generate saja, yang menjadi fokus pertama:

Inventaris kurikulum dan aset
→ alokasi slot teks/visual serta target kesulitan
→ generate kandidat + aset
→ pemeriksaan lokal format, aset, render, dan konsistensi
→ ekspor kandidat + manifest ber-hash
→ `generation_complete` / `validation_pending`
→ berhenti dan laporkan hasil generate.

Fase B — hanya setelah instruksi `MULAI VALIDASI` untuk batch terkait:

Verifikasi ulang hash manifest kandidat
→ solver blind menerima soal, opsi, dan gambar sebenarnya
→ pencocokan jawaban dan pemeriksaan ambiguitas
→ pemeriksaan kebutuhan gambar
→ perbaikan terbatas atau penahanan
→ ekspor versi baru + penanda siap ber-hash
→ validasi visual-aware
→ publikasi hasil lengkap/draft yang dapat dibedakan
→ respons siswa yang diskor server
→ CTT/IRT
→ dataset empiris versi baru
→ fine-tuning challenger jika semua gate terpenuhi.

Pisahkan checkpoint generation dari checkpoint validation, sehingga kegagalan
API di fase B tidak mengharuskan generate ulang soal yang sudah tersimpan.

Solver blind tidak menerima kunci generator, pembahasan, target level, atau
deskripsi yang mengandung jawaban. Utamakan solver independen dari generator
dan catat provider/model, versi prompt, hash konten/gambar, serta hasilnya.
Jika model tidak memiliki kemampuan vision yang benar-benar tersedia,
batch visual harus berstatus menunggu, bukan dianggap tervalidasi.

Pemeriksaan tanpa gambar adalah bukti pendukung, bukan aturan bahwa solver wajib
selalu salah: jawaban benar bisa terjadi karena menebak. Gabungkan audit informasi
yang hanya ada pada gambar, beberapa bukti pemeriksaan jika perlu, dan flag review.
Jangan meloloskan atau menggugurkan soal hanya karena satu percobaan tanpa gambar.

Perluas validator, exporter, metadata, handoff dan marker sehingga memahami aset
gambar dan hash-nya. Perubahan gambar harus membatalkan status validasi lama,
meskipun teksnya tetap. Jangan menghapus guard text-only tanpa pengganti.

Pertahankan resume, batas biaya/call, retry terbatas, stop kuota, dan failover
hanya ke model yang mampu memvalidasi modalitas soal tersebut. Cegah dua proses
menulis checkpoint yang sama. Riwayat pernah mengalami benturan file
`silver_labels.json.tmp`; periksa lock dan file sementara unik, bukan hanya retry.

Jangan menambah atau mengedit isi batch yang sudah berbayar/tervalidasi secara
diam-diam. Gunakan batch baru untuk revisi teks/aset, atau mekanisme extend
terverifikasi jika hanya menambah dan semua input lama persis sama.

### Hasil validasi harus tetap kompatibel dengan exercise sebelumnya

Setelah fase B benar-benar berjalan, gunakan struktur dan kontrak hasil lama:

```text
output/exercise/<kelas>/batchNN/
  soal_exercise_db.json             # envelope master `items`
  soal_exercise_meta.json           # metadata per `_id`
  <aset gambar dan manifest generation>
  hasil_validasi/
    validation_results.json
    validation_results_meta.json
    export_status.json
    manifest.json
    LAPORAN_VALIDASI.md
    <artefak bukti lain sesuai kontrak exporter yang sudah ada>
```

Audit schema/exporter lama untuk memastikan field dan tipe yang tepat. Jangan
mengganti kontrak hasil menjadi format visual yang tidak bisa dibaca backend.
Master generation tetap mempertahankan kolom validasi belum-terisi sesuai
kontrak sebelumnya; `level_target` disimpan di metadata. Setelah validasi,
hasil per `_id` harus memuat kolom resmi seperti `cognitive_level`,
`cognitive_score`, `confidence_score`, dan `status`, ditambah bukti gambar
di metadata/provenance tanpa merusak kontrak yang sudah ada.

Jangan membuat `validation_results` palsu dengan mengisi target generator sebagai
hasil validasi. Sebelum fase B, cukup manifest pending; setelah fase B, status
parsial/draft/lengkap harus eksplisit dan tidak boleh menerbitkan bank lengkap
ketika masih ada soal yang belum diperiksa. Pertahankan resume, ID, arsip
versi lama, dan pemetaan master ke hasil validasi.

## 6. IRT dan fine-tuning yang sudah disambungkan

Nightly dijadwalkan 01.00 WIB lewat Windows Task Scheduler. Antrean generate
sendiri belum dijadwalkan otomatis. Setelah generate lengkap, kode handoff yang
baru menghubungkan ekspor ke validasi; pastikan perluasannya tetap aman untuk visual.
Untuk batch visual baru yang diminta di sini, ubah jalur itu agar menghormati
`validation_pending` dan izin fase di bagian 0. Deskripsi kemampuan otomasi lama
bukan izin menjalankannya bersamaan dengan generate.

IRT memerlukan jawaban siswa sungguhan dan gate readiness. Jangan membuat respons
sintetis agar IRT atau training terlihat siap. Pemeriksaan terakhir menemukan
0 assessment pada database lokal; verifikasi ulang. Backend eksternal tidak
otomatis tersinkron hanya karena file lokal berubah.

`empirical_finetuning.py` membuat target difficulty empiris per populasi/assessment,
mempertahankan split awal dan label kognitif, mengecualikan versi ditahan, dan
memanggil training LoRA IndoBERT setelah gate dataset terpenuhi. Hasil identik
dipakai ulang. Snapshot empiris dan artifact challenger berstatus research-only;
tidak otomatis mengganti model produksi atau menimpa master AI silver.

Periksa khusus jalur visual: verifikasi fakta/transkrip, jangan masukkan kunci
jawaban ke input prediksi, dan jangan menyamakan transkrip fakta dengan penalaran
solver. Jelaskan keterbatasan model IndoBERT berbasis teks terhadap gambar.

## 7. Pelaksanaan dan batas tahap pertama

Tahap awal yang saya minta sekarang: audit, perbaikan kode, konfigurasi, tes,
dan rancangan pilot kelas 1 dengan total maksimum 30 soal baru (usulan target
9 easy, 12 medium, 9 hard; 21 visual dan 9 teks secara total). Pilih materi
berdasarkan sumber kurikulum yang berhasil diverifikasi. Jika cakupan terlalu
sempit, kecilkan pilot dan laporkan distribusi yang realistis.

Jangan menjalankan generation berbayar atau massal hanya karena kamu melihat
API key. Siapkan dahulu rencana pilot konkret: materi, model/provider yang
tersedia, aset, batas request/retry, perkiraan biaya jika tarif diketahui, file
keluaran baru, dan perintah eksekusi. Jangan mengarang harga atau kemampuan model.
Saya akan mengirim `JALANKAN PILOT` untuk mengeksekusi rencana tersebut.
Jangan mengasumsikan izin pilot sebagai izin generate semua kelas.

Contoh perintah lama untuk DIPELAJARI, bukan langsung dieksekusi:

```powershell
# Gunakan bab/subbab yang benar dari hasil audit; jangan menebak placeholder.
.\.venv\Scripts\python.exe scripts/generate_exercise_9router.py --help
.\.venv\Scripts\python.exe scripts/verify_exercise_9router.py --help
.\.venv\Scripts\python.exe scripts/run_exercise_queue.py --help
.\.venv\Scripts\python.exe scripts/nightly_pipeline.py --help
```

Perintah `run_exercise_queue` tidak boleh diasumsikan sudah mendukung rencana
70/30 visual: baca kode, tambah dukungan dan tes terlebih dahulu. CLI export
yang baru bisa memicu validasi berbayar ketika batch siap; jangan memakainya
sebagai inspeksi read-only. Mode generation-only wajib memutus pemicu tersebut
dan tetap menghormati guard pada runner. Buat opsi dry-run yang jelas.

Tes minimal: pembulatan kuota; visual esensial/dekoratif; aset hilang/berubah;
jumlah objek dan opsi salah; solver tanpa vision; konten gambar ambigu;
resume tanpa panggilan ulang; batch parsial tidak terbit sebagai lengkap;
lock proses; model non-vision tidak menjadi fallback visual; pemisahan target,
label AI, kuota relatif dan label IRT; tidak ada training tanpa data siswa.
Gunakan mock untuk tes API; tes otomatis tidak boleh memakai key nyata.

## 8. Hasil yang harus kamu sampaikan

1. Apa yang sudah didukung, apa yang belum, dan konflik aturan yang ditemukan.
2. Inventaris soal/aset nyata, file sumber yang hilang, dan rencana kapasitas.
3. Perubahan kode dan konfigurasi beserta hasil tes.
4. Tabel rencana pilot menurut materi, level, modalitas dan sumber aset.
5. Perintah siap jalan beserta batas request/retry; tandai panggilan berbayar.
6. Jalur file laporan dan cara memeriksa status validasi/gambar/IRT/training.
7. Tegaskan apakah baru menyiapkan sistem, sudah generate, sudah memvalidasi,
   atau sudah training. Jangan menyamakan kode yang tersedia dengan proses
   yang benar-benar dijalankan.
8. Buktikan batch baru masih `validation_pending`, belum ada panggilan API
   solver/validator, dan jadwal malam tidak akan memvalidasinya sebelum diizinkan.

Mulai dengan membaca repository dan audit. Jika memiliki akses coding, lanjutkan
pekerjaan offline yang aman sampai kode dan rencana pilot dapat diperiksa.
Jika hanya chat tanpa akses file, jelaskan file yang perlu saya berikan dan
jangan mengarang hasil audit.

---

## Pesan lanjutan setelah meninjau rencana Claude

Hanya kirim ini setelah memahami rencana pilot, biaya/batas API, dan lokasi output:

> JALANKAN PILOT sesuai rencana yang baru kamu tampilkan, maksimum 30 soal baru,
> dalam batch/lokasi baru yang tidak menimpa data lama. Terapkan batas request
> dan retry yang sudah disebutkan. Hentikan jika sumber kurikulum/aset belum
> valid atau kuota generator habis. Jalankan mode GENERATE SAJA dan pemeriksaan
> lokal, tanpa solver blind atau validasi Gemini. Simpan manifest dan status
> `validation_pending`; jangan terbitkan marker yang memicu auto-validasi.
> Laporkan jumlah kandidat, distribusi target aktual, aset, hash manifest,
> biaya/call generator yang tercatat, dan masalah tersisa. Jangan memperluas
> ke generate massal atau mengaktifkan fase validasi.

## Pesan terpisah setelah generate selesai dan saya siap memakai API validasi

> MULAI VALIDASI untuk kelas/batch dan hash manifest generation yang baru kamu
> laporkan. Verifikasi hash teks/aset masih sama dan generate untuk batch itu
> sudah berhenti. Tampilkan lalu gunakan batas request/retry sesuai rencana
> validasi yang telah disepakati. Lanjutkan dari checkpoint tanpa generate ulang.
> Gunakan solver/validator yang mendukung gambar sebenarnya, simpan
> `hasil_validasi/validation_results.json`, metadata, manifest dan laporan dengan
> kontrak exercise lama. Jika kuota habis, simpan progres dan berhenti; jangan
> pindah ke generate atau mengubah kunci/label agar terlihat lolos.
