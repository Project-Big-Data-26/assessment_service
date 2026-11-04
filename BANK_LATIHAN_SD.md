# Bank latihan lokal kelas 1–4

**Penilaian ulang selesai: 2.921 soal tersimpan, 2.911 aktif, 10 ditahan.**
Kekurangan satu sesi pada 85 subbab dan 255 kombinasi subbab-level: **0**.
Database production belum disinkronkan.

Setiap subbab memiliki **minimal 10 easy, 10 medium, dan 10 hard aktif**.
Setiap kelompok level menyediakan setidaknya **7 soal bergambar dan 3 teks**.
Jumlahnya dapat lebih dari 10 setelah koreksi level; label aktual pada ekspor
validasi yang digunakan untuk menghitung stok, bukan nama file atau target awal.

| Kelas | Bab | Subbab | Easy aktif | Medium aktif | Hard aktif | Aktif | Gambar aktif | Ditahan |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 25 | 349 | 268 | 250 | 867 | 607 | 0 |
| 2 | 8 | 20 | 291 | 223 | 200 | 714 | 500 | 0 |
| 3 | 5 | 18 | 191 | 205 | 180 | 576 | 405 | 10 |
| 4 | 6 | 22 | 236 | 298 | 220 | 754 | 529 | 0 |
| Total | 27 | 85 | 1.067 | 994 | 850 | 2.911 | 2.041 | 10 |

Bank awal berisi 2.550 soal. Pada penilaian ulang, 302 label diperbaiki,
10 soal garis kelas 3 ditahan karena jawaban tidak bergantung pada gambar,
dan 371 soal ditambahkan untuk mengisi kekurangan tanpa memaksakan label.
Proporsi gambar aktif setiap kelas tetap sedikitnya 70%.

Pemeriksaan lokal mencakup perhitungan ulang, empat opsi berbeda, hubungan data
gambar dengan jawaban, hash antarberkas, dan kuota berdasarkan ekspor canonical.
Sebanyak **1.445 ekspresi matematika** diperiksa dengan KaTeX tanpa error.
Tes integrasi dan pemulihan penulisan dicatat di
`runs/sd_difficulty_review_v2/tests.xml`.

Soal tersimpan di `output/exercise/kelasN/batch01/babNN/<KODE>_<level>.json`.
PNG untuk siswa, SVG, serta spesifikasi faktanya berada di `batch01/assets`.
Hasil pemeriksaan lokal ada di `batch01/hasil_validasi/validation_results.json`
beserta metadata, laporan, manifest hash, dan bukti perhitungan.

Katalog pada `generation_plan.json` dibekukan dari daftar bab/subbab yang tersimpan,
dicocokkan dengan struktur pretest. `reference_blueprints.json` menyimpan teks,
kunci, ID dan lokasi acuan. Adaptasi konsep untuk subbab kelas 4 yang belum
memiliki acuan langsung dicatat pada metadata; kelas asal acuan tidak diubah.

## Menjalankan dan melanjutkan

Semua perintah berikut menggunakan kode dan aset lokal, tanpa API eksternal:

```powershell
.\.venv\Scripts\python.exe scripts/generate_sd_bank_local.py --pilot
.\.venv\Scripts\python.exe scripts/generate_sd_bank_local.py
.\.venv\Scripts\python.exe scripts/generate_sd_bank_local.py --audit-only
.\.venv\Scripts\python.exe scripts/review_sd_difficulty_local.py
.\.venv\Scripts\python.exe scripts/review_sd_difficulty_local.py --audit-only
```

Pilot membuat satu subbab lengkap pada setiap kelas (120 soal), yang ikut dihitung
dalam total. Perintah penuh melanjutkan checkpoint; tidak menggandakan ID atau
menambah soal pada file yang sudah lengkap. `--classes 1 2` dapat membatasi kelas.
`--refresh-owned` hanya untuk bank generasi awal; flag ini ditolak jika batch
sudah memiliki penilaian ulang agar tambahan dan riwayatnya tidak terhapus.
Runner penilaian ulang dapat dijalankan kembali tanpa menggandakan soal.

Laporan terkini ada di `runs/sd_difficulty_review_v2/REPORT.md`, dengan
rincian setiap subbab dan level pada `runs/sd_difficulty_review_v2/final_audit.json`.
`runs/sd_bank_local_v1` menyimpan catatan historis target awal 2.550 soal.

## Makna hasil validasi

`status: active` pada ekspor ini berarti soal lolos pemeriksaan lokal Codex:
model hitung, kecukupan informasi, pilihan berbeda, data gambar, serta format
KaTeX. Easy/medium/hard merupakan penilaian lokal sesuai lingkup usia,
bukan kalibrasi empiris terhadap jawaban siswa.

Confidence **0 berarti belum diukur**. Provenance menandai pemeriksaan lokal,
`api_runs: 0`, dan `training_evidence_qualified: false`; pemeriksaan ini tidak
diklaim sebagai validasi AI independen. Validasi API otomatis diblokir untuk batch
yang dikelola runner ini. Tidak ada perintah di atas yang menyinkronkan MongoDB
atau memanggil endpoint generator SD/9Router.

PNG dapat diperiksa langsung. Referensi gambar pada ekspor bersifat relatif
terhadap batch (`assets/...png`); deployment web tetap perlu membawa/menyajikan
aset tersebut. Keberadaan hasil lokal tidak membuktikan bahwa production telah
diperbarui.

Status gambar terkini terdapat di
`hasil_validasi/bukti_validasi/assets_validation_results.json`. JSON aset yang
bernama hash mempertahankan catatan awal renderer, termasuk status pending
saat render; berkas tersebut bukan hasil validasi akhir. Riwayat label serta
alasan perubahan ada pada `validation_results_meta.json` dan
`LAPORAN_PERUBAHAN_LEVEL.md` di setiap kelas.
