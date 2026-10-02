# Spesifikasi IndoBERT 3×4×3

## Batas sistem

Model v2 adalah classifier advisory untuk soal matematika SD kelas 1–6. Tiga targetnya:

1. `mathCognitiveDomain`: `knowing | applying | reasoning`;
2. `knowledgeDimension`: `factual | conceptual | procedural | metacognitive`;
3. `intendedDifficulty`: `Easy | Medium | Hard`.

KKO adalah fitur eksperimen, bukan target dan bukan penentu gold. `/v1/classify` C1–C6 tetap legacy. `/v2/classify` tidak pernah fallback ke rules jika artefak tidak ada atau rusak.

## Arsitektur v2

```text
serializer math-question-text-v1
            │
IndoBERT base p1 @ revision 789e955…
            │
 LoRA attention query/value (r=8 atau 16)
            │
 pooled token [CLS]
   ┌────────┼───────────┐
   │        │           │
 3 kelas   4 kelas     3 kelas
 domain   knowledge   difficulty
```

Base encoder dibekukan. Hanya adapter LoRA dan tiga classification head yang mendapat gradient. Training memakai float32 CPU, dynamic padding, physical batch 2, gradient accumulation 8, weighted cross-entropy dari distribusi train, maksimum 12 epoch, dan early stopping dari rata-rata macro-F1 validation.

## Gold dan split

Gold hanya berasal dari tiga ahli matematika blind. Keputusan 3–0 dan 2–1 dapat menjadi gold; 1–1–1, abstain, konflik kunci, atau bukti tidak cukup masuk pembahasan/adjudikasi ahli senior keempat. Prediksi model, KKO, tingkat kesulitan agen, dan jawaban agen tidak menjadi gold.

Snapshot SD memakai split deterministik 70/15/15 berbasis kelompok. Source exercise, stimulus bersama, exact duplicate, dan near-duplicate family tidak boleh bocor antar-split. SMP/SMA disimpan sebagai expansion/shift set.

## Artefak

```text
models/indobert-3x4x3-v1/
├── adapter/                 # LoRA safetensors
├── heads.safetensors        # tiga classification head
├── base_model/              # snapshot revision untuk offline load
├── tokenizer/
└── manifest.json            # checksum, label, calibration, threshold, provenance
```

Loader memverifikasi seluruh checksum sebelum model dianggap ready. Temperature scaling dan selective threshold berasal hanya dari validation. `approvedForProvisional` tetap `false` sampai gate teknis dan persetujuan penelitian selesai.

Konfigurasi kanonik berada di [model_v2_config.yaml](configs/model_v2_config.yaml), [rubric_math_3x4x3_v1.yaml](configs/rubric_math_3x4x3_v1.yaml), dan [model_v2_risk_policy.json](configs/model_v2_risk_policy.json). Runbook lengkap ada di [dokumen implementasi](API_DOCUMENTATION/22_INDOBERT_V2_IMPLEMENTATION_RUNBOOK.md).
