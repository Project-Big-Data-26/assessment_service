# Validasi Matematika Tingkat Lanjut kelas 11 dan 12

Batch `validasi_blind_20261003_v1` menggunakan sumber TL yang terpisah dari
matematika umum: 55 soal kelas 11 TL dan 41 soal kelas 12 TL. Setiap soal mendapat
tiga penilaian blind Gemini; perbedaan suara, abstain, atau masalah konten/kunci
masuk adjudikasi AI terpisah. Target awal adalah 288 run, di luar adjudikasi dan
percobaan ulang. API key dibaca dari konfigurasi lingkungan tanpa dicatat pada laporan.

## Rubrik dan konteks

`--track tl` memilih rubrik khusus TL hanya untuk kelas 11 dan 12. Default
`--track regular` mempertahankan prompt dan rubrik kelas reguler yang ada.
Checkpoint menyimpan `subjectTrack`, grade, model, hash sumber, versi prompt,
versi/hash rubrik, hash prompt/respons, usage, serta riwayat percobaan gagal.
Resume menolak pertukaran track, grade, rubrik, sumber, atau model. Run sukses
yang sudah tersimpan tidak dipanggil ulang.

| Kelas | Soal | Target run awal | Konteks materi |
|---|---:|---:|---|
| 11 TL | 55 | 165 | Matriks, polinomial, trigonometri, vektor, transformasi, fungsi dan pemodelan, serta prasyarat |
| 12 TL | 41 | 123 | Lingkaran/elips, turunan, integral, variabel acak, distribusi binomial/normal, serta prasyarat |

Rubrik tersedia di
[`rubric_math_3x4x3_v7_sma11_tl.yaml`](../configs/rubric_math_3x4x3_v7_sma11_tl.yaml)
dan [`rubric_math_3x4x3_v7_sma12_tl.yaml`](../configs/rubric_math_3x4x3_v7_sma12_tl.yaml).
Prompt TL memakai versi v9. Tingkat lanjut atau simbol kalkulus/matriks tidak
otomatis berarti Hard. Kesulitan dinilai relatif siswa TL pada kelas sasaran.
Opsi yang tidak menjawab bentuk pertanyaan, konflik kunci, notasi rusak, dan
visual yang tidak cukup dicatat sebagai masalah konten, tanpa mengubah sumber.

## Eksekusi dan resume

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS='4096'
.\.venv\Scripts\python.exe scripts/generate_silver_labels_sma.py `
  --grades 11 12 --track tl --batch-name validasi_blind_20261003_v1 --execute
```

Pelaksana memakai folder `kelas11_tl` dan `kelas12_tl`, berjalan serial, serta
menghentikan batch berikutnya jika provider memblokir kuota harian atau konfigurasi.
Ringkasan eksekusi bersama:
[`validasi_blind_20261003_v1_sma_tl_execution.json`](../output/pretest/validasi_blind_20261003_v1_sma_tl_execution.json).
Jangan memanggil ulang ketika blok provider belum terselesaikan.

Setelah tiga run per soal dan semua adjudikasi selesai, packaging offline:

```powershell
.\.venv\Scripts\python.exe scripts/package_sma_tl_validation.py `
  --grades 11 12 --batch-name validasi_blind_20261003_v1 `
  --snapshot-name final_snapshot_v1
```

Packaging memverifikasi hash prompt/respons dan integritas sumber/gambar,
menyalin checkpoint ke snapshot immutable, mengauditnya sebelum diagnostik
IndoBERT, lalu membuat laporan dan kelompok Easy/Medium/Hard/undecided.
Laporan aktif sebelumnya, bila ada, diarsipkan. Snapshot yang sudah diaudit
tidak boleh diubah atau dipakai sebagai checkpoint resume.

## Membaca hasil

- [Laporan 11 TL](../output/pretest/kelas11_tl/hasil_validasi/LAPORAN_VALIDASI.md)
- [Data keputusan 11 TL](../output/pretest/kelas11_tl/hasil_validasi/validation_results.json)
- [Laporan 12 TL](../output/pretest/kelas12_tl/hasil_validasi/LAPORAN_VALIDASI.md)
- [Data keputusan 12 TL](../output/pretest/kelas12_tl/hasil_validasi/validation_results.json)

Periksa `finalRouting` bersama `llmAdvisory.advisoryLabels`:
`pending_expert_review` berarti tidak ada blocker konten yang terdeteksi,
`revision_required` berarti ada masalah struktur/konten/kunci, dan
`llm_retry_or_manual_review` berarti bukti atau keputusan belum cukup.
Kategori difficulty pada soal yang perlu revisi tidak menyatakan soal layak digunakan.

Seluruh label tetap silver/advisory, bukan gold ahli. Penilaian N=3 dan adjudikasi
memakai model Gemini yang sama, bukan penilai manusia independen. IndoBERT lama
hanya mencakup kelas 1–6: untuk TL semua head abstain/out_of_scope tanpa inferensi
encoder. Gate audit tidak otomatis lolos karena API selesai; ketidaklengkapan
bukti, konflik kunci, proporsi abstain, atau boundary distribusi dapat menahan
ekspansi/training. Sumber soal/gambar tidak direvisi, tidak ada training/publishing,
dan CTT/IRT belum dihitung karena belum ada respons siswa.

## Hasil eksekusi 3 Oktober 2026

Seluruh **96 soal** selesai mendapat **288/288 run awal sukses** dan **34
adjudikasi sukses**. Tidak ada run API gagal yang tersisa atau adjudikasi tertunda.
Tiga kegagalan koneksi sandbox sebelum akses jaringan tersedia disimpan sebagai
`retryHistory` pada soal pertama 11 TL; run suksesnya tidak ditimpa.

| Kelas | Soal | Run awal sukses | Adjudikasi | Tanpa blocker konten, menunggu ahli | Perlu revisi |
|---|---:|---:|---:|---:|---:|
| 11 TL | 55 | 165/165 | 19 | 54 | 1 |
| 12 TL | 41 | 123/123 | 15 | 40 | 1 |
| Total | 96 | 288/288 | 34 | 94 | 2 |

Distribusi difficulty berikut dibedakan antara seluruh usulan dan soal tanpa
blocker konten. Tidak ada label yang diubah untuk mengisi kategori Hard.

| Kelas | Cakupan | Easy | Medium | Hard | Undecided |
|---|---|---:|---:|---:|---:|
| 11 TL | Seluruh usulan | 44 | 11 | 0 | 0 |
| 11 TL | Tanpa blocker konten | 43 | 11 | 0 | 0 |
| 12 TL | Seluruh usulan | 30 | 11 | 0 | 0 |
| 12 TL | Tanpa blocker konten | 30 | 10 | 0 | 0 |

Temuan revisi:

- **11 TL, soal 30** (`5364425a70eacc615935825f`, Aturan Sinus): sudut C = 145°,
  b = 10 dan c = 6 tidak membentuk segitiga. Sudut C yang tumpul mengharuskan
  sisi c terpanjang, tetapi b > c. Kunci D dari operasi arcsin tidak memenuhi
  jumlah sudut segitiga. Ketiga run dan adjudikasi mencatat konflik kunci.
- **12 TL, soal 1** (`5faf4ffecb76e0e311ebef4d`, Lingkaran): pertanyaan meminta
  persamaan lingkaran, sementara opsi A hanya memberi pusat (3,4) dan jari-jari
  24. Persamaan yang diperoleh adalah (x−3)²+(y−4)²=576. Adjudikasi mencatat
  ketidaksesuaian bentuk jawaban sebagai konflik kunci; soal perlu ditinjau.

Kedua batch memiliki `readyForExpansion=false`: gate `requiredEvidenceComplete`
gagal karena konflik kunci, dan `boundaryAnalysisClear` belum lolos karena
kategori Hard tidak ada serta belum ada boundary analysis yang diterima.
Ini tidak membatalkan selesainya penilaian AI; hasil belum menyetujui training
atau menetapkan gold ahli. Absennya Hard tidak boleh diperbaiki dengan memaksa label.

Token pada respons sukses yang tercatat berjumlah **839.346** (11 TL: 472.494;
12 TL: 366.852), bukan estimasi tagihan. Sumber soal/gambar serta `.env` tetap
utuh. Pengujian kode terkait selesai: **56 tes lulus**.

Snapshot final dan bukti audit:

- [Snapshot/audit 11 TL](../output/pretest/kelas11_tl/validasi_blind_20261003_v1/final_snapshot_v1/execution_verification.json)
- [Snapshot/audit 12 TL](../output/pretest/kelas12_tl/validasi_blind_20261003_v1/final_snapshot_v1/execution_verification.json)
