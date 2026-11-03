# Generate penambalan batch01 — kelas 5-12

Atas instruksi pengguna, generate dituntaskan dahulu melalui Codex dengan
variasi matematika terparameterisasi dan acuan soal active yang sudah berlabel
di kelas/bab/subbab yang sama. Acuan dipilih acak secara deterministik agar
resume dapat ditelusuri. Tidak ada API generate, API validasi, atau perubahan
database production pada tahap ini.

## Hasil

**2.028 kandidat baru** sudah ditambahkan ke `batch01`:

| Kelas | Kandidat baru |
|---|---:|
| 5 | 192 |
| 6 | 55 |
| 7 | 205 |
| 8 | 121 |
| 9 | 96 |
| 10 | 215 |
| 11 Umum | 105 |
| 11 TL | 343 |
| 12 Umum | 170 |
| 12 TL | 526 |
| Total | 2.028 |

Distribusi target: easy 684, medium 357, hard 987. Jumlah tambahan tiap slot
sama dengan selisih kuota pada audit per level. Kelas 1-4 di luar cakupan
permintaan sekitar 2.000 soal ini.

Ini adalah kelengkapan **generate kandidat**, bukan bukti semua kekurangan soal
aktif sudah tertutup. Label final masih null dan status inactive. Gemini bisa
menolak soal atau memberi level berbeda dari target; sesudah validasi jumlah
kekurangan perlu dihitung ulang. `cognitive_c`, jumlah langkah dan alasan level
yang ditulis generator juga usulan, bukan label hasil validasi independen.

## Lokasi hasil

- JSON kerja: `output/exercise/<kelas>/batch01/babNN/<KODE>_<level>.json`.
- Master dan metadata lama tetap ada, dengan kandidat baru ditambahkan di akhir.
- Preview per kelas beserta acuan asli:
  `output/exercise/<kelas>/batch01/_replenishment/PREVIEW.md`.
- Snapshot blueprint: `_replenishment/blueprints.json` pada setiap kelas.
- Pemeriksaan lokal per slot: `_replenishment/NN_KODE_level_checks.json`.
- Progres lengkap: `runs/exercise_replenishment/codex_batch01/PROGRESS.md`.
- Bukti audit: `audit.json`, `katex_audit.json`, `tests.xml` pada folder progres.
- Backup berkas sebelum penambahan: `codex_batch01/backups/<kelas>/...`.

Soal lama, urutan master lama, metadata lama, dan hasil validasi lama tidak
diganti. Acuan baru menggunakan `exercise_validated` atau `pretest_validated`,
dengan ID sumber, teks dan kunci asli, snapshot, serta SHA-256.

## Pemeriksaan

Audit memeriksa jumlah kandidat per slot, kesesuaian raw/master/meta, ID unik,
empat opsi berbeda, stem yang tidak berulang dalam kelas, snapshot sumber active
di lokasi yang sama, dan hash berkas. Pemeriksaan matematika lokal menggunakan
aritmetika eksak, enumerasi, atau operasi simbolik sesuai keluarga soal.
Ini tidak menggantikan pemeriksaan semantik, pedagogi, dan level oleh Gemini.

Formula baru diuji dengan KaTeX lokal. Kandidat tetap perlu validasi independen
atas kunci, kejelasan, kesesuaian materi, dan kesulitan.

## Penahanan validasi otomatis

`reference_replenishment_state.json` dan `reference_replenishment_manifest.json`
memisahkan penambahan pada batch lama dari checkpoint berbayar yang sudah ada.
Nightly/handoff ditahan sampai persetujuan manifest setelah instruksi pengguna
`MULAI VALIDASI`. Exporter lama menolak membangun ulang batch yang ditambal,
agar soal lama tidak terhapus atau ID berubah.

Saat fase validasi dimulai, persetujuan harus mencocokkan hash manifest. Sesudah
itu gunakan jalur `extend` pada validator untuk mengadopsi ID baru dan
mengarsipkan evidence lama tanpa mengulang hasil sukses. Jangan langsung
menjalankan `full` terhadap checkpoint yang source hash-nya belum diperluas.

Planner mengenali kandidat penambahan ini sebagai pending, sehingga tidak
meminta generate ulang. Kandidat belum mengurangi hitungan stok active.
