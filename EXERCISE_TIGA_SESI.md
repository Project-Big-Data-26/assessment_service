# Latihan tiga sesi: SD, SMP, SMA, dan TL

**Selesai:** 19.871 soal tambahan, 34.656 soal aktif, dan kekurangan 0 pada
271 subbab / 813 kombinasi subbab-level. Seluruh kelas memenuhi tiga sesi.
Audit akhir memeriksa 32.983 ekspresi KaTeX soal tambahan tanpa error dan
10.140 berkas PNG; 776 tes otomatis lolos. Lihat [laporan lengkap](runs/exercise_sessions_3/REPORT.md).

Putaran ini menambah variasi pada bank latihan lokal sampai setiap subbab dan
level easy, medium, serta hard mempunyai stok untuk tiga sesi tanpa mengulang
ID soal. Status selesai ditentukan oleh audit akhir, bukan jumlah kandidat yang
sudah digenerate.

| Jenjang | Soal per sesi dan level | Target aktif per subbab-level |
|---|---:|---:|
| SD kelas 1–6 | 10 | 30 |
| SMP kelas 7–9 | 15 | 45 |
| SMA kelas 10–12, termasuk 11 TL dan 12 TL | 20 | 60 |

Kelas 1–4 menyediakan minimal **21 soal bergambar dan 9 teks** pada setiap
subbab-level. Kelas 5–12/TL menyediakan minimal **30% soal bergambar dari stok
aktif akhir masing-masing kelas**. Gambar harus memuat informasi yang diperlukan
untuk menjawab; aset dirender secara lokal menjadi PNG, dengan SVG dan
spesifikasi fakta sebagai bukti.

## Menjalankan dan melanjutkan

Jalankan dari folder proyek. Semua perintah menggunakan kode lokal tanpa API
eksternal.

```powershell
.\.venv\Scripts\python.exe scripts/extend_exercise_sessions_local.py --plan-only
.\.venv\Scripts\python.exe scripts/extend_exercise_sessions_local.py --pilot
.\.venv\Scripts\python.exe scripts/extend_exercise_sessions_local.py --resume
.\.venv\Scripts\python.exe scripts/extend_exercise_sessions_local.py --audit-only
```

`--pilot` menyiapkan satu subbab per kelas dan belum memublikasikannya ke ekspor
validasi. Perintah penuh melanjutkan checkpoint, memeriksa kandidat, lalu
memublikasikan satu kelas ketika lengkap. Gunakan `--classes kelas5 kelas6` untuk
membatasi kelas yang dikerjakan. Target putaran ini tetap `--sessions 3`.

Jangan menghapus checkpoint atau mereset putaran lama untuk melanjutkan proses.
Runner memakai lock, snapshot awal, penulisan atomik, dan pemulihan publikasi
yang terputus. Bila kapasitas variasi habis, runner berhenti dengan laporan
kombinasi yang membutuhkan keluarga soal tambahan; label tidak dipaksa agar
memenuhi kuota.

## Lokasi soal dan hasil pemeriksaan

Hierarki final tetap sama:

```text
output/exercise/kelasN/batch01/
  babNN/<KODE>_<level>.json
  assets/<hash>.png, <hash>.svg, <hash>.json
  soal_exercise_db.json
  soal_exercise_meta.json
  hasil_validasi/validation_results.json
  hasil_validasi/validation_results_meta.json
  hasil_validasi/bukti_validasi/
```

Nama kelas jalur lanjut adalah `kelas11_tl` dan `kelas12_tl`. Hitung stok dari
`status: active` dan label aktual pada `validation_results.json`; nama file dan
`level_target` menunjukkan sasaran awal. Master sumber mempertahankan kandidat
inactive tanpa label sampai hasil pemeriksaannya diterbitkan. Soal lama,
penilaiannya, dan pretest dipertahankan.

Catatan putaran ada di `runs/exercise_sessions_3/`: `plan.json` membekukan target
dan acuan, `staging/kelasN/checkpoint.json` menyimpan pekerjaan yang dapat
dilanjutkan, dan `progress.json` mencatat kandidat, tambahan yang sudah
dipublikasikan, persentase, sisa, serta komposisi gambar/teks.

Setelah audit seluruh kelas lolos, baca [laporan akhir](runs/exercise_sessions_3/REPORT.md),
`final_audit.json`, dan `session_assignments.json`. Berkas pembagian sesi
membuktikan tiga kelompok ID yang tidak berulang pada setiap subbab-level.

## Arti validasi lokal

Hasil terkini adalah `validation_results.json` dan `validation_results_meta.json`.
Bukti tambahan putaran tiga sesi ada pada
`bukti_validasi/codex_session_review.json`; status gambar putaran ini ada pada
`bukti_validasi/session_assets_validation.json`. Bukti putaran sebelumnya tetap
disimpan sebagai riwayat. Status pending di JSON aset adalah catatan awal renderer,
bukan status akhir soal pada ekspor validasi.

Pemeriksaan meliputi perhitungan ulang, keunikan empat pilihan jawaban, isi dan
level, hubungan fakta gambar dengan jawaban, render KaTeX, kuota, serta
konsistensi raw–master–metadata–ekspor. Bukti dan riwayat disimpan bersama hasil
validasi tiap kelas.

**Confidence 0 berarti belum diukur.** Label adalah penilaian lokal Codex,
bukan validasi AI independen atau kalibrasi empiris dari jawaban siswa.
Provenance mencatat `api_runs: 0` dan `training_evidence_qualified: false`;
validasi API otomatis untuk batch lokal tetap diblokir.

Runner tidak menyinkronkan database production. Web production baru memperoleh
stok dan gambar ini setelah proses sinkronisasi/deployment terpisah.
