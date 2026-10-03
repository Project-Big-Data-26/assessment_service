# Runbook pilot silver dan CTT/IRT

Pilot menerima snapshot AI silver yang qualified. Sistem tidak memerlukan approval guru, role pelabel atau label gold. Endpoint matrix analysis dan demo numerik dapat berjalan tanpa dataset delivery.

```powershell
.\.venv\Scripts\python.exe scripts/psychometrics.py demo --model rasch --output tmp/rasch-demo.json
.\.venv\Scripts\python.exe scripts/psychometrics.py create-assessment --silver-snapshot output/pretest/silver_operational/dataset_snapshot_v2.json --assessment-config tmp/assessment.json --output tmp/assessment-created.json
.\.venv\Scripts\python.exe scripts/psychometrics.py screen --request tmp/screen.json --output tmp/empirical-snapshot.json
```

Demo berlabel synthetic dan tidak membuktikan karakteristik siswa nyata. Pada pilot, participant token dikeluarkan server; opsi opaque; scoring dilakukan server; skip/missing tetap null. Screen memilih session selesai per peserta unik pada satu assessment, grade/track, populasi, family dan window.

| Syarat konfigurasi | Rasch | 2PL | 3PL |
|---|---:|---:|---:|
| Minimum peserta layak | 100 | 300 | 1000 |
| Minimum item | 5 | 10 | 20 |

Minimum respons per item 50, minimum benar dan salah masing-masing 5, coverage 0,7, serta bukti unidimensionalitas, independensi lokal dan sampel representatif tetap diperiksa. Angka ini adalah policy proyek. `assumptionReview` berisi bukti teknis dan dapat dikirim service analisis; tidak mensyaratkan akun guru. Ketiadaan bukti menghasilkan status menunggu, tanpa menganggap asumsi otomatis benar.

CTT menghitung p, Wilson CI, diskriminasi, point-biserial, distraktor dan KR-20. Rasch/2PL/3PL memakai estimasi regularized MML dan menghasilkan parameter item serta EAP siswa, uncertainty dan diagnostik. Kurang data tetap menghasilkan CTT bila dapat dihitung, tetapi menunda IRT.

Band IRT proyek: `b < -1` Easy, `-1 <= b <= 1` Medium, `b > 1` Hard. Intended, CTT dan IRT difficulty terpisah. Konvergensi, misfit, ketidakpastian dan warning harus dibaca bersama kategori.

Screen menyimpan snapshot immutable dan feedback sistem otomatis. GET decisions untuk audit; mutation keputusan manual telah dihapus. Scheduler analisis ulang disediakan integrasi, bukan berjalan otomatis setiap siswa menjawab. CAT, DIF, linking/equating dan profil adaptif masih rancangan.
