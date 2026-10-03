# Psychometrics API: CTT dan IRT

CTT batch serta IRT **Rasch, 2PL dan 3PL sudah diimplementasikan** di `app/psychometrics`. Analisis offline tidak membutuhkan IndoBERT, MongoDB atau LLM. Screening pilot membaca event server dan menyimpan snapshot immutable di SQLite. Runbook: [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md).

## Endpoint aktif

| Method | Path | Fungsi |
|---|---|---|
| GET | `/v2/psychometrics-info` | Kesiapan/model/minimum data; tanpa network call |
| POST | `/api/v1/internal/psychometrics/item-analysis` | Matriks eksternal/sintetis, stateless |
| POST | `/api/v1/internal/psychometrics/screen` | Normalisasi respons pilot dan persist snapshot |
| GET | `/api/v1/internal/psychometrics/snapshots/{snapshot_id}` | Snapshot staff termasuk EAP pseudonim |
| GET | `/api/v1/psychometrics/items/{question_id}/snapshots` | Agregat terautentikasi tanpa estimasi peserta |
| GET | `/api/v1/internal/psychometrics/snapshots/{snapshot_id}/decisions` | Keputusan empiris AI |

Analisis/agregat memerlukan `X-Internal-API-Key` yang cocok dengan `PSYCHOMETRICS_API_TOKEN` (≥32 karakter), atau cookie staff. Mutation cookie memerlukan CSRF. POST keputusan memerlukan cookie + CSRF + profil/role AI; service token tidak cukup. Tidak ada hasil individual publik. Endpoint family/variant dan screening per question pada desain lama masih target.

## Matriks dan normalisasi

`MatrixAnalysisInput`: population, assessment family, grade, item references, subject IDs unik, matriks `0|1|null`, model, data origin dan assumption review. Contoh executable dibuat CLI demo. [Schema aktual](schemas/implemented-api.schema.json#/$defs/MatrixAnalysisInput).

Kolom diikat ke `questionId/questionVersionId/contentVersion/contentHash` dan intended difficulty. Satu question tidak boleh muncul dengan dua versi. Boolean, string angka, nonbinary, dimensi salah dan nonfinite ditolak. Batas: 10.000 peserta, 200 item, 500.000 sel. Upload tidak boleh mengklaim `server_scored`; gunakan screening.

Screening menerima:

```json
{
  "assessmentId": "pilot-kelas1-v1",
  "model": "rasch",
  "attemptPolicy": "first",
  "fromTime": "2026-10-01T00:00:00Z",
  "toTime": "2026-11-01T00:00:00Z",
  "assumptionReview": {
    "reviewedBy": "<pemeriksa desain psikometrik>",
    "evidence": "<bukti dimensi, independensi lokal dan sampling yang telah ditinjau>",
    "unidimensional": true,
    "localIndependence": true,
    "representativeSample": true
  }
}
```

Time window memakai **session completedAt**, awal inklusif/akhir eksklusif. First/last memilih satu session lengkap per subject. Duplicate/conflicting IDs, versi/populasi/grade salah, invalid/rapid guess, unscored/malformed event dicatat dalam exclusions. Skip tetap null; incorrect menjadi 0. Tanpa session lengkap, screening memberi 409. CTT tetap tersedia ketika gate IRT gagal.

## CTT

Metrik: proporsi benar + Wilson CI95, empirical band, missing rate, upper/lower discrimination, corrected item–total correlation, KR-20, distribusi opsi/distraktor, median/IQR waktu server bila event tersedia. Total score, correlation dan KR-20 menggunakan **complete cases**, tanpa imputasi nol. N lengkap dicantumkan; variance nol/data kurang menghasilkan null.

Discrimination memakai **rest score** (total tanpa item), cutoff kuantil 27/73%; ties tidak dibelah arbitrer. KR-20 memakai sample item/total variance yang konsisten. Distraktor memakai verified key, termasuk bila semua respons salah. Tanpa log opsi/waktu, metrik tersebut null.

Band CTT: `p>0.7` Easy, `p<0.3` Hard, selainnya Medium. Disagreement hanya di-flag ketika seluruh Wilson CI berada pada satu band berbeda dari intended difficulty. Label asli tidak diubah.

## Gate dan estimator IRT

| Model | Minimum peserta eligible | Minimum item | Parameter |
|---|---:|---:|---|
| `rasch` | 100 | 5 | a=1, b estimated, c=0 |
| `2pl` | 300 | 10 | a,b estimated, c=0 |
| `3pl` | 1.000 | 20 | a,b,c estimated |

[Policy aktif](../configs/psychometrics_policy.json): setiap item ≥50 respons, ≥5 benar dan ≥5 salah; peserta >30% missing dikeluarkan dari fit; coverage eligible ≥70%; desain item terhubung. Asumsi dimensi, independensi lokal dan sampling wajib ditinjau/didukung. Minimum ini kebijakan penelitian proyek, bukan standar universal atau bukti identifiability.

`P(θ)=c+(1−c)sigmoid[a(θ−b)]`; D=1, skala θ~N(0,1). **Regularized marginal likelihood**, Gauss-Hermite 41 titik dan L-BFGS-B. Missing tidak memberi likelihood. Prior b~N(0,3²), log(a)~N(0,0.75²), c~Beta(5,17) untuk 3PL. Bounds b∈[-5,5], a∈[0.2,4], c∈[0.001,0.35]. c diestimasi, bukan otomatis 1/jumlah opsi.

Keluaran: convergence/iteration, likelihood, AIC/BIC deskriptif, a/b/c, curvature posterior SD/interval b bila teridentifikasi, EAP/posterior SD, infit/outfit candidate, residual adjusted-Q3 dan test information curve. AIC/BIC regularized bukan approval pemilihan model; posterior-curvature interval bukan frequentist SE tanpa penalti. Prior memengaruhi estimasi, khususnya 3PL.

Band b: b<-1 Easy, b>1 Hard, selainnya Medium pada skala lokal. Tidak ada pooling lintas grade/populasi/form/version. Multi-group linking, DIF, equating, CAT dan polytomous masih target.

Referensi algoritmik: [estimasi/model IRT mirt](https://philchalmers.github.io/mirt/docs/reference/mirt.html), [L-BFGS-B SciPy](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-lbfgsb.html). Kode proyek memakai SciPy/quadrature sendiri, bukan paket mirt.

## Snapshot dan feedback

Snapshot menyimpan policy lengkap + hash, matrix hash, manifest sampel + hash, population/family/grade, time window, cleaning, CTT, gate dan IRT. Rerun input/policy identik mengambil snapshot yang sama. Data/policy berubah menghasilkan snapshot baru.

IRT statuses: waiting_for_data, waiting_for_assumption_review, estimated, estimated_with_warnings, failed. Nonconvergence, boundary, uncertainty gagal dan residual dependence tetap membutuhkan review. Hasil memakai `researchOnly=true`, `reviewMode=automated_ai`, `labelProvenance=ai_silver`; `reviewRequired` menunjukkan kebutuhan AI review.

Routing item: collect_more_events, ai_review, observation_only. Sistem otomatis menyimpan retain/collect_more_events/needs_ai_review terikat snapshot/hash/version. needs_ai_review menahan delivery dan dikecualikan oleh builder silver yang memakai assessment database. Domain, knowledge dan intended difficulty tidak diganti otomatis. Revisi → content version baru → validasi AI → freeze snapshot → training terkontrol; jawaban siswa mentah tidak menjadi teks training.
