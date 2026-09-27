# Smoke Evaluation Gemini

## Tujuan dan batas klaim

Evaluasi ini memeriksa jalur integrasi nyata `gemini-3.8-flash` untuk tiga peran:

1. solver jawaban dengan tiga sampel independen;
2. taxonomy screening dengan self-consistency `N=3`;
3. adjudicator untuk konflik label IndoBERT-LLM.

Ini adalah smoke evaluation kecil, bukan pengukuran akurasi produksi, bukan validasi psikometrik, dan tidak menghasilkan gold label. API key hanya dibaca dari `.env`; key, header otorisasi, dan environment tidak dimasukkan ke artefak evaluasi.

## Fixture terkontrol

| Peran | Kasus | Ekspektasi |
|---|---|---|
| Solver | fakta nilai pi | memilih `opt-a` pada ketiga sampel |
| Solver | luas lingkaran, `r=7`, `pi=22/7` | jawaban numerik `154` pada ketiga sampel |
| Solver | luas segitiga tanpa tinggi | abstain pada ketiga sampel |
| Screening | fakta nilai pi | `C1 / factual / Easy`, voting `N=3` |
| Screening | penerapan rumus luas lingkaran | `C3 / procedural / Easy`, voting `N=3` |
| Adjudicator | konflik C2-konseptual vs C3-prosedural | memilih kandidat C3-prosedural-Easy atau abstain secara aman |

Fixture machine-readable berada di `project_assessment/backend/test/fixtures/gemini-smoke-cases.json`. Runner berada di `project_assessment/backend/scripts/evaluateGemini.js` dan dapat dijalankan dengan:

```powershell
Set-Location project_assessment/backend
npm run llm:smoke
```

## Kontrol teknis runner

- strict JSON Schema untuk setiap peran;
- screening benar-benar melakukan tiga request terpisah, bukan meminta tiga jawaban dalam satu request;
- default pacing smoke test `31.000 ms` antar-request;
- initial cooldown `65.000 ms` untuk mengosongkan rolling quota setelah health check;
- exponential backoff dengan jitter dan maksimum empat attempt;
- kuota harian/billing yang terdeteksi tidak di-retry langsung;
- latency provider dipisahkan dari waktu antrean pacing;
- penulisan hasil memakai temporary file lalu atomic rename;
- artefak hanya menyimpan konfigurasi non-rahasia, input fixture, output terstruktur, dan telemetri aman.

Nilai pacing adalah kontrol operasional untuk evaluasi lokal, bukan parameter kualitas model. Sesuaikan dengan active rate limit yang terlihat pada Google AI Studio.

## Hasil run 27 September 2026

Artefak utama:

`data/local/evaluations/GEMINI-SMOKE-2026-09-27T08-33-33-903Z.json`

Pemeriksaan marker `apiKey`, `GEMINI_API_KEY`, `Bearer`, dan `authorization` pada artefak menghasilkan `SANITIZED_OK`.

### Hasil fungsional

| Peran/kasus | Hasil | Interpretasi |
|---|---|---|
| Solver fakta pi | PASS | 3/3 sampel memilih opsi yang benar; stabil |
| Solver luas lingkaran | PASS | 3/3 sampel menghasilkan `154`; stabil |
| Solver soal tidak lengkap | TIDAK TERUKUR | run berhenti pada gangguan provider sebelum tiga sampel lengkap |
| Screening fakta pi | TIDAK TERUKUR | seluruh ensemble tidak selesai karena HTTP 429 |
| Screening penerapan rumus | TIDAK TERUKUR | seluruh ensemble tidak selesai karena HTTP 429 |
| Adjudicator | TIDAK TERUKUR | request tidak selesai karena HTTP 429 |

Ringkasan otomatis mencatat `2/6` kasus PASS. Angka ini **tidak boleh dibaca sebagai akurasi 33,3%**: empat kasus lain gagal secara operasional dan tidak menghasilkan output lengkap untuk dinilai. Untuk dua kasus solver yang selesai, konsistensi jawaban adalah `100%` pada enam sampel.

### Latency dan keandalan akses

| Metrik | Nilai |
|---|---:|
| Total request/attempt | 25 |
| Respons sukses | 7 |
| HTTP 429 | 13 |
| Gangguan unavailable/network | 5 |
| Provider latency minimum | 2.932 ms |
| Provider latency median | 4.082 ms |
| Provider latency rata-rata | 6.559 ms |
| Provider latency p95/maksimum | 14.168 ms |
| Total waktu antrean pacing | 590.960 ms |
| Total waktu enam operasi | 745.710 ms |

Waktu operasi solver yang selesai adalah 96.308 ms dan 123.719 ms karena masing-masing mencakup tiga request serta pacing. Angka tersebut bukan latency satu inferensi.

## Keputusan kelayakan

**Gemini layak dilanjutkan untuk tahap engineering dan evaluasi berikutnya, tetapi belum layak diaktifkan sebagai komponen keputusan AI `provisional`.**

Dasarnya:

- sisi positif: koneksi, strict structured output, solver pilihan ganda, solver numerik, evidence, dan konsistensi tiga sampel telah bekerja;
- sisi negatif: kuota aktif tidak mampu menyelesaikan satu suite kecil secara andal, sehingga screening `N=3`, abstention, dan adjudication belum memiliki bukti evaluasi lengkap;
- konsekuensi: kegagalan provider harus tetap membuat workflow `failed/retryable`, tidak boleh berubah menjadi consensus, provisional, atau label final.

## Syarat sebelum melanjutkan ke pilot

1. Periksa active rate limit dan usage proyek di Google AI Studio. Gunakan tier/kuota yang mampu menuntaskan suite tanpa dominasi HTTP 429.
2. Jalankan ulang smoke suite sampai semua peran menghasilkan output lengkap. Jangan mengubah fixture ekspektasi setelah melihat hasil hanya untuk memperoleh PASS.
3. Setelah jalur operasional stabil, perluas reference set dengan label yang telah ditetapkan melalui prosedur riset yang sah; ukur per-head accuracy/F1, calibration, abstention, disagreement, dan error taxonomy.
4. Tetap pisahkan solver, screening, dan adjudicator. Screening tidak boleh menerima prediksi IndoBERT; adjudicator hanya dipanggil ketika kandidat konflik.
5. Integrasi Gemini saja tidak cukup untuk `provisional`: artefak IndoBERT yang layak, evaluasi OOD/calibration, serta risk policy yang disetujui tetap wajib.

Verdict machine-readable pada artefak tetap `requires_revision_before_continuing` sampai suite penuh lolos. Secara arsitektural, keputusan yang sehat adalah melanjutkan eksperimen Gemini sambil menahan aktivasi produksi.
