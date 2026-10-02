# Arsitektur AI dan Feedback Psikometrik Terkontrol

Implementasi saat ini menghubungkan validasi soal manusia, pilot server-scored, CTT/IRT dan keputusan empiris. Pembaruan label/model tetap memerlukan versioning dan ahli; sistem tidak melakukan self-training otomatis dari respons siswa.

```mermaid
flowchart TD
  E[Ekstraksi / babNN.json] --> Q[Import dan qualification]
  Q --> H[Tiga ahli blind]
  H --> C[Consensus / diskusi / senior adjudicator]
  C --> G[Human-gold snapshot immutable]
  G --> T[Group-aware train / validation / test]
  T --> I[IndoBERT ordinal grade-aware + kalibrasi]
  I --> P[Promotion gates + approval; silver tetap research]
  G --> A[Assessment fixed-form satu grade/populasi]
  A --> D[Delivery opaque + scoring server]
  D --> R[Completed sessions + event immutable]
  R --> M[Cleaning; 0 / 1 / NA; whole attempt]
  M --> B[CTT + gate IRT]
  B -->|Data/asumsi memadai| F[Rasch / 2PL / 3PL]
  B -->|Kurang data/asumsi| W[CTT observation; collect/review]
  F --> X[Snapshot dan flags advisory]
  W --> X
  X --> V[Ahli retain / revise / quarantine]
  V -->|Hold| S[Hentikan delivery versi lama; exclude freeze]
  V -->|Revisi versi baru| Q
  L[Gemini blind silver N=3] --> O[Audit hash dan comparison offline]
  O --> N[Research artifact; bukan gold]
```

Kode aktif: `app/annotation`, `app/training/v2`, `app/classification/v2`, `app/assessment`, `app/psychometrics`. MongoDB menyimpan keputusan/gold; SQLite menyimpan pilot/empirical. [07](07_PSYCHOMETRICS_API.md) menjelaskan statistik, [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md) menjelaskan eksekusi.

LLM blind dilakukan sebelum prediksi model untuk silver penelitian. Tiga run AI bukan tiga annotator manusia. Review anchored legacy tidak menjadi validasi baru. Hidden chain-of-thought tidak disimpan; alasan terstruktur dapat diaudit.

Judgment difficulty agen 1–5, label intended Easy/Medium/Hard, p CTT dan b IRT mempunyai makna berbeda. Tidak ada mapping otomatis antarfield. Version/population/grade/time-window/policy tetap melekat pada bukti empiris.

Calibrated confidence classifier, agreement LLM dan posterior uncertainty IRT juga berbeda. Model promotion tidak mengikuti convergence IRT atau voting AI. Semua keputusan empirical advisory tetap researchOnly=true.

Generator varian, multigroup linking, DIF/equating, CAT, continuous scheduled retraining, Redis jobs, Claude API dan public authoring lengkap masih desain lanjutan. Tidak ada klaim bahwa setiap blok arsitektur target sudah berjalan di deployment.
