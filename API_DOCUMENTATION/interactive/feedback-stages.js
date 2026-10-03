/* Silver operational flow; numerical examples remain educational. */
window.FLOW_FEEDBACK_STAGES = [
  {
    "id": "feedback-discrepancy",
    "phase": "Umpan balik",
    "title": "Bandingkan intended dengan bukti empiris",
    "subtitle": "Setelah siswa menjawab, lihat apakah pengalaman mereka sesuai perkiraan awal",
    "status": "implemented",
    "summary": "Awalnya soal mungkin diperkirakan sulit. Setelah banyak siswa mengerjakannya, ternyata sebagian besar menjawab benar. Sistem menyimpan kedua bukti tersebut agar AI dapat mencari penyebab perbedaannya sebelum memutuskan perubahan.",
    "learning": {
      "story": "Bayangkan soal berlabel Hard dijawab benar oleh 85 dari 100 siswa. Kita sekarang mempunyai perkiraan dari isi soal dan bukti dari pengalaman siswa. Perbedaan ini mengajak AI memeriksa soal, kunci, distraktor dan kelompok siswanya.",
      "terms": [
        {
          "term": "Intended difficulty",
          "meaning": "Perkiraan kesulitan dari tuntutan isi soal, relatif terhadap kelas sasaran.",
          "why": "Menjelaskan tantangan yang direncanakan sebelum respons siswa tersedia."
        },
        {
          "term": "Empirical difficulty",
          "meaning": "Kesulitan yang terlihat dari respons kelompok siswa pada versi soal tertentu.",
          "why": "Membantu melihat apakah soal bekerja sesuai tujuan dalam pelaksanaan nyata."
        },
        {
          "term": "Wilson interval",
          "meaning": "Rentang ketidakpastian untuk proporsi jawaban benar.",
          "why": "Mencegah kesimpulan terlalu cepat ketika sampel sedikit atau proporsi dekat batas kategori."
        }
      ],
      "why": "Label awal dan respons nyata menjawab pertanyaan berbeda. Menyimpannya berdampingan membantu menemukan masalah tanpa kehilangan alasan keputusan sebelumnya.",
      "next": "Jika bukti cukup kuat menunjukkan perbedaan, AI meninjau penyebabnya dan memilih tindakan."
    },
    "latex": [
      {
        "title": "Proporsi benar dan ketidakpastiannya",
        "tex": "\\hat p=\\frac{x}{n},\\qquad [L,U]=\\frac{\\hat p+\\frac{z^2}{2n}\\ \\pm\\ z\\sqrt{\\frac{\\hat p(1-\\hat p)}{n}+\\frac{z^2}{4n^2}}}{1+\\frac{z^2}{n}}",
        "symbols": [
          {
            "symbol": "x",
            "meaning": "Jumlah respons benar pada item."
          },
          {
            "symbol": "n",
            "meaning": "Jumlah respons valid observed pada item; skip tidak masuk penyebut."
          },
          {
            "symbol": "\\hat p",
            "meaning": "Perkiraan proporsi benar."
          },
          {
            "symbol": "z",
            "meaning": "1.96 untuk Wilson CI95."
          },
          {
            "symbol": "L,U",
            "meaning": "Batas bawah dan atas interval."
          }
        ],
        "why": "p memberi ringkasan; interval menunjukkan seberapa kuat bukti itu sebelum dibuat flag review."
      },
      {
        "title": "Flag perbedaan CTT yang stabil",
        "tex": "\\begin{aligned}F&=\\mathbf{1}\\!\\left\\{d_i\\ne\\varnothing\\ \\land\\ d_s\\ne\\varnothing\\ \\land\\ d_i\\ne d_s\\right\\}\\\\d_s&=\\begin{cases}\\mathrm{Easy}&L>0.70\\\\ \\mathrm{Hard}&U<0.30\\\\ \\mathrm{Medium}&L\\ge0.30,\\ U\\le0.70\\\\ \\varnothing&\\text{lainnya}\\end{cases}\\end{aligned}",
        "symbols": [
          {
            "symbol": "F",
            "meaning": "Flag untuk review; hanya bernilai 1 ketika kedua kategori tersedia dan berbeda."
          },
          {
            "symbol": "d_i",
            "meaning": "Intended difficulty dari penilaian isi; ∅ bila label tidak tersedia."
          },
          {
            "symbol": "d_s",
            "meaning": "Kategori CTT yang stabil dari interval respons; ∅ bila interval melintasi batas kategori atau belum tersedia."
          },
          {
            "symbol": "L,U",
            "meaning": "Batas Wilson CI95 dari rumus sebelumnya."
          }
        ],
        "why": "Seluruh interval harus berada pada satu kategori agar perbedaan tidak sekadar akibat ketidakpastian sampel. Ketika intended atau stable band belum tersedia, flag bernilai 0."
      }
    ],
    "input": {
      "questionVersionId": "contoh:v2",
      "intendedDifficulty": "Hard",
      "ctt": {
        "correctCount": 85,
        "validResponseCount": 100
      },
      "irtStatus": "estimated (status global snapshot.irt.status)",
      "irt": {
        "b": -1.2
      }
    },
    "process": [
      "CTT menghitung p dan Wilson CI95 dari respons valid per item, termasuk siswa yang tidak memiliki jawaban lengkap untuk seluruh tes.",
      "Band CTT: Easy bila p > easyP; Hard bila p < hardP; sisanya Medium. Flag intended_empirical_disagreement membutuhkan CI seluruhnya berada dalam satu band yang berbeda dari intended.",
      "IRT menyimpan band empiris dari b secara terpisah: Easy bila b < easyB, Hard bila b > hardB, selain itu Medium. Convergence, boundary dan uncertainty tetap diperiksa.",
      "Bandingkan hanya pada questionVersionId, grade, populationId, assessmentFamily, window dan calibration yang sesuai; perbedaan skala membutuhkan linking."
    ],
    "formula": "p = correctCount / validResponseCount\nCTT stable Easy: WilsonLower > 0.70\nCTT stable Hard: WilsonUpper < 0.30\nCTT stable Medium: WilsonLower ≥ 0.30 dan WilsonUpper ≤ 0.70\nflag = intended tersedia ∧ stableBand tersedia ∧ intended ≠ stableBand\nIRT empirical: b < −1 → Easy; b > 1 → Hard; lainnya Medium",
    "example": "Contoh ilustratif: 85/100 benar memberi p=0.85 dan Wilson CI≈[0.767,0.907]. Karena batas bawah >0.70, band CTT stabil Easy. Intended Hard → flag review. b=−1.2 juga menghasilkan band IRT Easy. Tidak ada penggantian label otomatis.",
    "output": {
      "intendedDifficulty": "Hard",
      "cttEmpiricalDifficulty": "Easy",
      "irtEmpiricalDifficulty": "Easy",
      "reviewFlags": [
        "intended_empirical_disagreement"
      ],
      "labelChanged": false
    },
    "cautions": [
      "CTT flag di kode berasal dari Wilson CI, bukan rumus langsung b mengganti intendedDifficulty.",
      "Bila CI melewati batas band, perbedaan p saja belum menghasilkan flag ini.",
      "p/b tidak menetapkan ulang mathCognitiveDomain atau knowledgeDimension; perbedaan dapat berasal dari kunci, distraktor, populasi atau kualitas konten."
    ],
    "sources": [
      {
        "path": "app/psychometrics/analysis.py",
        "symbol": "analyze_matrix"
      },
      {
        "path": "app/psychometrics/irt.py",
        "symbol": "fit_irt"
      },
      {
        "path": "configs/psychometrics_policy.json",
        "symbol": "easyP/hardP/easyB/hardB"
      }
    ]
  },
  {
    "id": "feedback-system-decision",
    "phase": "Umpan balik",
    "title": "Sistem menentukan tindak lanjut empiris",
    "subtitle": "Tanpa keputusan pelabel manusia",
    "status": "implemented",
    "summary": "Routing otomatis membedakan observasi, data lemah dan masalah kualitas item. Hanya masalah kualitas memicu hold AI review.",
    "learning": {
      "story": "Routing otomatis membedakan observasi, data lemah dan masalah kualitas item. Hanya masalah kualitas memicu hold AI review.",
      "terms": [
        {
          "term": "Silver AI",
          "meaning": "Label awal dari validasi AI dengan bukti terkunci.",
          "why": "Mencatat sumber label tanpa gate pelabel manusia."
        },
        {
          "term": "Qualification",
          "meaning": "Pemeriksaan konten, kunci, solusi, visual dan provenance.",
          "why": "Mencegah soal bermasalah masuk delivery."
        }
      ],
      "why": "Routing otomatis membedakan observasi, data lemah dan masalah kualitas item. Hanya masalah kualitas memicu hold AI review.",
      "next": "Versi held tidak dapat diberikan ke siswa; perbaikan memerlukan versi dan bukti AI yang baru."
    },
    "latex": [
      {
        "title": "Aturan menahan versi soal",
        "tex": "\\operatorname{held}(v)=\\mathbf{1}\\!\\left\\{\\operatorname{lastAction}(v)\\in\\{\\mathrm{revise},\\mathrm{quarantine}\\}\\right\\}",
        "symbols": [
          {
            "symbol": "v",
            "meaning": "Versi soal yang sedang diperiksa."
          },
          {
            "symbol": "\\operatorname{lastAction}(v)",
            "meaning": "Tindakan pada keputusan empiris terakhir untuk versi tersebut."
          },
          {
            "symbol": "\\mathbf{1}\\{\\cdot\\}",
            "meaning": "Bernilai 1 bila kondisi benar dan 0 bila salah."
          }
        ],
        "why": "Aturan ini membuat permintaan revisi benar-benar menghentikan delivery baru tanpa menghapus data lama."
      }
    ],
    "input": {
      "reviewFlags": [
        "negative_discrimination"
      ],
      "recommendedRouting": "ai_review"
    },
    "process": [
      "collect_more_events meminta data tambahan.",
      "ai_review menyimpan needs_ai_review dan menahan versi.",
      "observation_only mempertahankan label silver; perbedaan difficulty saja tidak memicu relabel."
    ],
    "formula": "affectsSilverLabels = false",
    "example": "Versi held tidak dapat diberikan ke siswa; perbaikan memerlukan versi dan bukti AI yang baru.",
    "output": {
      "action": "needs_ai_review",
      "actorType": "system",
      "affectsSilverLabels": false,
      "nextStep": "new_content_version_and_blind_ai_validation"
    },
    "cautions": [
      "Tidak ada POST keputusan manual.",
      "Job regenerasi konten otomatis belum diimplementasikan."
    ],
    "sources": [
      {
        "path": "app/assessment/store.py",
        "symbol": "_automated_decisions / is_held"
      },
      {
        "path": "app/assessment/routes.py",
        "symbol": "decisions"
      }
    ]
  },
  {
    "id": "feedback-new-version",
    "phase": "Umpan balik",
    "title": "Versi konten baru dan validasi ulang AI",
    "subtitle": "Perubahan tetap dapat ditelusuri",
    "status": "conditional",
    "summary": "Perbaikan konten menghasilkan hash/versi baru. Gemini menilai ulang secara blind; label baru tetap silver AI.",
    "learning": {
      "story": "Perbaikan konten menghasilkan hash/versi baru. Gemini menilai ulang secara blind; label baru tetap silver AI.",
      "terms": [
        {
          "term": "Silver AI",
          "meaning": "Label awal dari validasi AI dengan bukti terkunci.",
          "why": "Mencatat sumber label tanpa gate pelabel manusia."
        },
        {
          "term": "Qualification",
          "meaning": "Pemeriksaan konten, kunci, solusi, visual dan provenance.",
          "why": "Mencegah soal bermasalah masuk delivery."
        }
      ],
      "why": "Perbaikan konten menghasilkan hash/versi baru. Gemini menilai ulang secara blind; label baru tetap silver AI.",
      "next": "Mengubah opsi atau gambar membutuhkan penilaian ulang; bukti lama tidak dipakai untuk input yang berbeda."
    },
    "latex": [
      {
        "title": "Kapan nomor versi berubah?",
        "tex": "v_{\\mathrm{new}}=\\begin{cases}v_{\\mathrm{old}}&H_{\\mathrm{new}}=H_{\\mathrm{old}}\\\\v_{\\mathrm{old}}+1&H_{\\mathrm{new}}\\ne H_{\\mathrm{old}}\\end{cases}",
        "symbols": [
          {
            "symbol": "v",
            "meaning": "Nomor contentVersion."
          },
          {
            "symbol": "H",
            "meaning": "Hash canonical content yang dibandingkan."
          }
        ],
        "why": "Konten identik tidak perlu menjadi revisi palsu; konten berbeda perlu riwayat baru."
      },
      {
        "title": "Consensus label AI per head",
        "tex": "d_h=\\begin{cases}\\operatorname{mode}(y_{1h},y_{2h},y_{3h})&\\text{3 vote lengkap dan mayoritas}\\ \\ge2\\\\\\varnothing&\\text{perlu diskusi}\\end{cases}",
        "symbols": [
          {
            "symbol": "h",
            "meaning": "Salah satu dari tiga head label."
          },
          {
            "symbol": "y_{rh}",
            "meaning": "Label reviewer AI r untuk head h."
          },
          {
            "symbol": "\\operatorname{mode}",
            "meaning": "Label dengan jumlah suara terbanyak."
          }
        ],
        "why": "Aturan ini menjelaskan 3–0/2–1 AI; kelayakan silver tetap membutuhkan gate konten/key/solution. Silver AI memakai aturan penerimaan berbeda."
      }
    ],
    "input": {
      "oldVersion": "q:silver:oldhash",
      "amendedContent": {
        "stem": "Konten diperbaiki"
      }
    },
    "process": [
      "Perbaiki sumber dan simpan lineage.",
      "Jalankan blind N=3/adjudikasi pada input baru.",
      "Bangun snapshot baru dengan key, solution dan visual evidence yang cocok."
    ],
    "formula": "versi baru = identitas soal + digest konten baru",
    "example": "Mengubah opsi atau gambar membutuhkan penilaian ulang; bukti lama tidak dipakai untuk input yang berbeda.",
    "output": {
      "labelProvenance": "ai_silver",
      "status": "silver_ready",
      "versionChanged": true
    },
    "cautions": [
      "Tidak ada auto-retrain.",
      "Regenerasi konten otomatis masih rancangan."
    ],
    "sources": [
      {
        "path": "app/ingestion/pretest_import.py",
        "symbol": "next_content_version"
      },
      {
        "path": "scripts/generate_silver_labels_kelas1.py",
        "symbol": "load_checkpoint / store_run_result"
      },
      {
        "path": "scripts/build_operational_silver.py",
        "symbol": "rows_from_bundle"
      }
    ]
  },
  {
    "id": "feedback-freeze",
    "phase": "Umpan balik",
    "title": "Bekukan snapshot silver berikutnya",
    "subtitle": "Provenance dan kelompok data tetap diperiksa",
    "status": "implemented",
    "summary": "Builder membekukan silver qualified, mengecualikan versi held bila database assessment disertakan, dan membangun split training aman.",
    "learning": {
      "story": "Builder membekukan silver qualified, mengecualikan versi held bila database assessment disertakan, dan membangun split training aman.",
      "terms": [
        {
          "term": "Silver AI",
          "meaning": "Label awal dari validasi AI dengan bukti terkunci.",
          "why": "Mencatat sumber label tanpa gate pelabel manusia."
        },
        {
          "term": "Qualification",
          "meaning": "Pemeriksaan konten, kunci, solusi, visual dan provenance.",
          "why": "Mencegah soal bermasalah masuk delivery."
        }
      ],
      "why": "Builder membekukan silver qualified, mengecualikan versi held bila database assessment disertakan, dan membangun split training aman.",
      "next": "Snapshot baru tersedia untuk registrasi delivery; training/test tetap locked bila dukungan kelas tidak cukup."
    },
    "latex": [
      {
        "title": "Sidik snapshot yang tetap",
        "tex": "H_{\\mathrm{snapshot}}=\\operatorname{SHA256}\\!\\left(\\operatorname{canonicalJSON}\\!\\left(\\operatorname{sortedRows}\\right)\\right) ",
        "symbols": [
          {
            "symbol": "H_{\\mathrm{snapshot}}",
            "meaning": "Sidik dataset untuk memeriksa identitas isinya."
          },
          {
            "symbol": "\\operatorname{sortedRows}",
            "meaning": "Training rows berurutan menurut questionVersionId."
          },
          {
            "symbol": "\\operatorname{canonicalJSON}",
            "meaning": "Serialisasi JSON deterministik yang dipakai sebelum hashing."
          }
        ],
        "why": "Jika isi berubah, hash berubah, sehingga proses tidak dapat diam-diam memakai dataset yang berbeda."
      }
    ],
    "input": {
      "snapshotId": "silver-next",
      "assessmentDb": "data/local/assessments.sqlite3"
    },
    "process": [
      "Verifikasi bundle/evidence dan qualification tiap item.",
      "Namespace kelas/track dan hash konten menjaga versi immutable.",
      "Terapkan hold, split group-aware dan gate dukungan label."
    ],
    "formula": "train / validation / test = 70 / 15 / 15 secara group-aware",
    "example": "Snapshot baru tersedia untuk registrasi delivery; training/test tetap locked bila dukungan kelas tidak cukup.",
    "output": {
      "labelProvenance": "ai_silver",
      "exclusionSummary": {
        "empirical_ai_hold": 1
      }
    },
    "cautions": [
      "Rujukan evaluasi tetap silver.",
      "Kelas 7–12/TL tetap expansionRows untuk model SD."
    ],
    "sources": [
      {
        "path": "scripts/build_operational_silver.py",
        "symbol": "main / rows_from_bundle"
      },
      {
        "path": "app/training/v2/dataset.py",
        "symbol": "TrainingRow / build_snapshot"
      }
    ]
  },
  {
    "id": "feedback-challenger",
    "phase": "Umpan balik",
    "title": "Latih, kalibrasi, dan kemas challenger",
    "subtitle": "Model belajar dari dataset baru, lalu probabilitasnya diperiksa",
    "status": "conditional",
    "summary": "Setelah label baru disahkan dan dataset dikunci, operator melatih calon model pengganti. Model belajar hubungan antara makna soal dan label rujukannya, kemudian diuji serta dikalibrasi. Inilah jalur hasil siswa dapat memperbaiki model melalui review dan data baru.",
    "learning": {
      "story": "Hasil siswa membantu AI memperbaiki soal atau label. Label yang disahkan menjadi contoh belajar baru. IndoBERT kemudian menyesuaikan bobotnya dari banyak contoh, sehingga satu hasil IRT tidak langsung mengubah prediksi model aktif.",
      "terms": [
        {
          "term": "Challenger",
          "meaning": "Calon model baru yang akan dibandingkan dengan model sebelumnya.",
          "why": "Memberi ruang menguji manfaat perubahan sebelum mengaktifkannya."
        },
        {
          "term": "Loss / optimizer",
          "meaning": "Ukuran kesalahan terhadap label rujukan dan mekanisme untuk menyesuaikan bobot.",
          "why": "Menjelaskan bagaimana contoh berlabel benar-benar mengubah model saat training."
        },
        {
          "term": "LoRA",
          "meaning": "Matriks tambahan berukuran kecil yang dilatih pada bagian query/value encoder.",
          "why": "Mengurangi jumlah parameter trainable saat menyesuaikan IndoBERT."
        },
        {
          "term": "Calibration",
          "meaning": "Penyesuaian probabilitas berdasarkan validation, lalu pemilihan batas review.",
          "why": "Membantu confidence lebih sesuai dengan ketepatan yang diamati pada evaluasi."
        }
      ],
      "why": "Pembaruan terkontrol menjaga model belajar dari bukti yang sudah diperiksa dan memungkinkan dampaknya diuji sebelum digunakan.",
      "next": "Bandingkan hasil challenger dan periksa syarat aktivasi artifact."
    },
    "latex": [
      {
        "title": "Apa yang diminimalkan saat belajar?",
        "tex": "\\mathcal{L}=\\mathrm{CE}_{\\mathrm{cognitive}}+\\mathrm{CE}_{\\mathrm{knowledge}}+\\mathrm{BCEWithLogits}_{\\mathrm{ordinal}},\\qquad \\boldsymbol t=[\\mathbf{1}(y>0),\\mathbf{1}(y>1)]",
        "symbols": [
          {
            "symbol": "\\mathcal{L}",
            "meaning": "Jumlah loss tiga head pada training."
          },
          {
            "symbol": "\\mathrm{CE}",
            "meaning": "Cross entropy multiclass dengan class weights dari train."
          },
          {
            "symbol": "\\mathrm{BCEWithLogits}",
            "meaning": "Binary cross entropy untuk dua batas ordinal dengan pos_weight dari train."
          },
          {
            "symbol": "y",
            "meaning": "Indeks intended label: Easy=0, Medium=1, Hard=2."
          },
          {
            "symbol": "\\boldsymbol t",
            "meaning": "Target ordinal: Easy=[0,0], Medium=[1,0], Hard=[1,1]."
          }
        ],
        "why": "Masing-masing head belajar targetnya; urutan difficulty dinyatakan melalui dua pertanyaan apakah label melewati suatu batas."
      }
    ],
    "input": {
      "snapshotId": "contoh-silver-v2",
      "architecture": "grade-aware-ordinal-v2",
      "inputRepresentation": "Dikunci manifest; metadata/solution/kko sesuai eksperimen",
      "operatorCommand": "python -m app.training.v2.train_lora"
    },
    "process": [
      "Serializer menghasilkan teks dan tokenizer memakai konfigurasi yang sama dengan inference. Head cognitive/knowledge multiclass; difficulty cumulative ordinal menerima embedding grade.",
      "Class weights berasal dari train saja; ordinal target Easy=[0,0], Medium=[1,0], Hard=[1,1]. Update LoRA/head dilakukan dengan optimizer.",
      "Pilih checkpoint yang lolos anti-collapse lalu weakest-head macro-F1 dan mean macro-F1. Validation menentukan temperature dan selective confidence/entropy threshold.",
      "Per-grade calibration hanya berlaku bila support mencukupi. Frozen test tetap mengikuti unlock gate, tanpa digunakan untuk memilih calibration.",
      "Kemas adapter, heads, tokenizer, base-model files, calibration, metrics, architecture dan snapshot/split/checksum dalam direktori versi baru."
    ],
    "formula": "L = CE_cognitive + CE_knowledge + BCEWithLogits_ordinal\nyOrdinal = [1(y > Easy), 1(y > Medium)]\nθ_model_new diperoleh optimizer pada train; bukan θ_ability siswa",
    "example": "Contoh: label intended pada v3 menjadi target ordinal [1,0] untuk Medium. Bukan memasukkan b=−1.2 ke fitur. bobot model baru baru tersedia setelah training, calibration dan packaging selesai.",
    "output": {
      "modelVersion": "contoh-indobert-v2",
      "datasetSnapshot": "contoh-silver-v2",
      "architectureVersion": "grade-aware-ordinal-v2",
      "calibrationVersion": "versi baru",
      "approvedForProvisional": false,
      "autoRetrained": false
    },
    "cautions": [
      "Silver model mengikuti gate teknis; dataset yang belum lolos gate tetap researchOnly.",
      "Arsitektur artifact yang ada dapat parallel-v1; jangan menganggap semua diagnostik lama sudah memakai ordinal grade-aware.",
      "Parameter kemampuan θ IRT dan parameter bobot neural network adalah dua objek berbeda."
    ],
    "sources": [
      {
        "path": "app/training/v2/train_lora.py",
        "symbol": "ordinal_difficulty_loss / run_trial / calibration_from_validation / package_artifact"
      },
      {
        "path": "app/classification/v2/model.py",
        "symbol": "GradeAwareOrdinalDifficultyHead / ThreeHeadIndoBERT"
      }
    ]
  },
  {
    "id": "feedback-compare-promote",
    "phase": "Umpan balik",
    "title": "Bandingkan label lama, label baru, dan prediksi",
    "subtitle": "Tunjukkan apa yang berubah dan apakah model baru memenuhi syarat",
    "status": "conditional",
    "summary": "Label lama, label AI yang baru dan prediksi model ditampilkan bersama asal serta versinya. Evaluasi memakai contoh yang tetap agar hasil model lama dan baru dapat dibandingkan dengan adil. Model pengganti baru dapat dilayani API setelah seluruh syarat dan persetujuan terpenuhi.",
    "learning": {
      "story": "v2 dahulu berlabel Hard; setelah revisi, AI memberi v3 label Medium. Challenger juga memprediksi Medium. Kesamaan ini perlu dicatat, tetapi peningkatan model diuji lagi pada benchmark yang tetap agar perubahan isi soal tidak disangka sebagai peningkatan model.",
      "terms": [
        {
          "term": "Agreement / confusion",
          "meaning": "Jumlah label yang sama dan pola pasangan label rujukan dengan prediksi.",
          "why": "Menunjukkan di kelas mana model cocok atau sering tertukar."
        },
        {
          "term": "Benchmark tetap",
          "meaning": "Item dan versi pengujian yang sama untuk membandingkan model.",
          "why": "Memisahkan efek model baru dari efek soal atau populasi yang berubah."
        },
        {
          "term": "Promotion / servable",
          "meaning": "Pemeriksaan syarat dan persetujuan agar artifact boleh dilayani API.",
          "why": "Mencegah calon model menjadi aktif hanya karena satu angka atau contoh terlihat bagus."
        }
      ],
      "why": "Perbandingan yang adil dan riwayat yang lengkap memungkinkan reviewer menilai manfaat perubahan beserta batasnya.",
      "next": "Jika semua gate terpenuhi, artifact dapat dipertimbangkan untuk aktivasi; integrasi IRT langsung tetap rancangan terpisah."
    },
    "latex": [
      {
        "title": "Kesamaan label pada comparison offline",
        "tex": "A_h=\\frac{\\sum_{i=1}^{N}\\mathbf{1}\\!\\left(\\widehat y_{ih}=y_{ih}^{\\mathrm{locked}}\\right)}{N}",
        "symbols": [
          {
            "symbol": "A_h",
            "meaning": "Agreement rate untuk head h."
          },
          {
            "symbol": "N",
            "meaning": "Jumlah item yang dibandingkan; berbeda dari jumlah siswa IRT."
          },
          {
            "symbol": "\\widehat y",
            "meaning": "Label prediksi model."
          },
          {
            "symbol": "y^{\\mathrm{locked}}",
            "meaning": "Label blind silver yang sudah dikunci dalam script comparison aktif."
          }
        ],
        "why": "Menunjukkan konsistensi prediksi terhadap rujukan terkunci; agreement terhadap silver mengukur kecocokan rujukan AI, bukan validitas empiris siswa."
      },
      {
        "title": "Syarat artifact dapat dilayani",
        "tex": "S=A\\land\\neg R\\land D\\land C\\land P",
        "symbols": [
          {
            "symbol": "S",
            "meaning": "servable."
          },
          {
            "symbol": "A",
            "meaning": "approvedForProvisional."
          },
          {
            "symbol": "R",
            "meaning": "researchOnly."
          },
          {
            "symbol": "D",
            "meaning": "dataGatesPassed."
          },
          {
            "symbol": "C",
            "meaning": "antiCollapsePassed."
          },
          {
            "symbol": "P",
            "meaning": "promotionGates.passed."
          }
        ],
        "why": "Kualitas data, perilaku model, metrik evaluasi dan approval harus bersama-sama terpenuhi."
      }
    ],
    "input": {
      "oldLabels": "snapshot lama",
      "newLabels": "snapshot baru dengan provenance",
      "incumbentPredictions": "model versi lama",
      "challengerPredictions": "model versi baru"
    },
    "process": [
      "Untuk perbandingan model yang adil, pakai item/version dan benchmark tetap, serializer/label map serta scope yang cocok. Label konten v2 dan v3 adalah sejarah revisi, bukan perubahan prediksi pada input identik.",
      "Comparison silver yang tersedia mengharuskan audit lock, SHA256 checkpoint/input match dan timestamp prediksi setelah lock; join per questionId menghasilkan agreement, confusion dan evidence per head.",
      "Agreement = label sama; disagreement tetap reviewRequired. Script comparison tidak memanggil LLM dan tidak menghasilkan silver pengganti.",
      "Promotion memeriksa macro-F1 H1/H2 ≥0.70, H3 ≥0.65; setiap class F1 ≥0.50; ECE ≤0.10; selective accuracy ≥0.80 pada coverage ≥0.70; anti-collapse/baseline dan stabilitas tiga seed.",
      "Manifest servable membutuhkan explicit approval, bukan researchOnly, data gates, anti-collapse dan promotion gates. /v2/classify mengembalikan 503 bila artifact belum servable."
    ],
    "formula": "changedLabel(h) = oldVersionLabel(h) ≠ newVersionLabel(h), dengan provenance/versi eksplisit\nagreementRate(h) = jumlah label model = label terkunci / jumlah item dibandingkan\nservable = approvedForProvisional ∧ ¬researchOnly ∧ dataGatesPassed ∧ antiCollapsePassed ∧ promotionGates.passed",
    "example": "Contoh ilustratif: intended v2=Hard, silver v3=Medium, challenger memprediksi Medium dengan p=0.78. Silver baru berasal dari review AI v3; p=0.78 hanya confidence model. Artifact tetap nonservable sampai semua gate dan approval terpenuhi.",
    "output": {
      "oldVersion": "contoh:v2",
      "oldIntendedLabel": "Hard",
      "newVersion": "contoh:v3",
      "newAILabel": "Medium",
      "challengerPrediction": "Medium",
      "historicalLabelsPreserved": true,
      "automaticRelabel": false
    },
    "cautions": [
      "Tabel perbandingan sejarah label/champion vs challenger terpadu masih workflow operator; script aktif khusus locked blind silver versus prediksi, bukan sistem auto-relabel.",
      "Kelas 7–12 pada runtime sekarang out_of_scope/abstain; jangan menganggap label null sebagai prediksi salah biasa.",
      "Tidak ada formula aktif 40% IndoBERT + 60% LLM atau confidence × IRT yang menetapkan label baru."
    ],
    "sources": [
      {
        "path": "scripts/compare_blind_labels_to_predictions.py",
        "symbol": "compare"
      },
      {
        "path": "app/training/v2/train_lora.py",
        "symbol": "promotion_gate_failures"
      },
      {
        "path": "app/classification/v2/artifact.py",
        "symbol": "ModelManifest.servable"
      },
      {
        "path": "app/api/v2.py",
        "symbol": "runtime_or_503"
      }
    ]
  },
  {
    "id": "feedback-future-irt-features",
    "phase": "Umpan balik",
    "title": "Rancangan fitur empiris atau pembaruan online",
    "subtitle": "Penggunaan fitur IRT atau tes adaptif perlu pengembangan berikutnya",
    "status": "planned",
    "summary": "Saat ini bukti IRT membantu proses review. Jika kelak ingin memasukkan parameter IRT ke model atau memilih soal berikutnya berdasarkan kemampuan siswa, dibutuhkan schema, model dan evaluasi tambahan. Bagian ini menjelaskan rancangan tersebut dengan status yang jelas.",
    "learning": {
      "story": "Setelah bank soal memiliki calibration yang dipercaya, kita dapat merancang pembaruan kemampuan siswa setelah setiap jawaban. Kita juga dapat meneliti apakah fitur empiris membantu classifier. Kedua ide ini membutuhkan layanan dan pengujian baru sebelum menjadi perilaku sistem.",
      "terms": [
        {
          "term": "Fusion fitur",
          "meaning": "Menggabungkan representasi teks dengan angka empiris yang punya provenance dan missing mask.",
          "why": "Memungkinkan eksperimen manfaat IRT tanpa menyembunyikan asal atau kekosongan data."
        },
        {
          "term": "Online theta scoring",
          "meaning": "Memperbarui perkiraan kemampuan siswa dengan parameter item yang sudah dikalibrasi.",
          "why": "Dapat mendukung pemilihan soal secara bertahap dalam layanan adaptif."
        },
        {
          "term": "CAT / calibration release",
          "meaning": "Tes adaptif dan izin menggunakan calibration bank item untuk tujuan tertentu.",
          "why": "Tes adaptif perlu bank, aturan pemilihan/penghentian dan validasi penggunaan yang sesuai."
        }
      ],
      "why": "Pengetahuan tentang fitur berikutnya membantu merencanakan sistem sambil menjaga penjelasan kemampuan sekarang tetap akurat.",
      "next": "Tentukan kebutuhan eksperimen, kontrak data dan validasi penggunaan sebelum membangun integrasi."
    },
    "latex": [
      {
        "title": "Rancangan pembaruan kemampuan per jawaban",
        "tex": "p_{\\mathrm{new}}(\\theta)\\propto p_{\\mathrm{old}}(\\theta)\\,P_j(\\theta)^x\\,[1-P_j(\\theta)]^{1-x}",
        "symbols": [
          {
            "symbol": "\\theta",
            "meaning": "Kemampuan laten siswa."
          },
          {
            "symbol": "x",
            "meaning": "Jawaban scored: benar=1 atau salah=0; skip tidak memberi pembaruan likelihood."
          },
          {
            "symbol": "P_j",
            "meaning": "Peluang benar item j dari bank calibration yang telah dilepas."
          },
          {
            "symbol": "p_{\\mathrm{old}},p_{\\mathrm{new}}",
            "meaning": "Distribusi kemampuan sebelum dan sesudah evidence baru."
          }
        ],
        "why": "Setiap jawaban menggeser perkiraan secara bertahap. Rumus ini rancangan; runtime online scoring/CAT belum diimplementasikan."
      }
    ],
    "input": {
      "proposalOnly": true,
      "possibleEmpiricalFeatures": [
        "a",
        "b",
        "c",
        "bPosteriorSd",
        "validResponseCount",
        "calibrationSnapshotId",
        "populationId",
        "timeWindow"
      ]
    },
    "process": [
      "Rancang schema dan fusion head tersendiri, missingness indicator serta provenance calibration; jangan mengisi b buatan ketika calibration belum tersedia.",
      "Pisahkan train/test menurut waktu dan family/populasi agar respons atau calibration dari test tidak bocor ke fitur train.",
      "Bandingkan ablation tanpa fitur IRT dengan fusion empiris pada benchmark tetap; intended difficulty dan empirical difficulty dapat memerlukan target/head berbeda.",
      "Online theta scoring membutuhkan bank calibration released, posterior update, content/exposure constraints dan stopping policy. Batch item calibration tidak otomatis menjadi CAT.",
      "Versikan release, monitoring/drift dan rollback. Tentukan kapan calibration lokal dapat digunakan lintas form/populasi melalui linking dan validasi penggunaan."
    ],
    "formula": "Contoh rancangan saja: hFusion = concat(hCLS, gradeEmbedding, empiricalFeatures, missingMask)\nContoh rancangan saja: posterior_new(θ) ∝ posterior_old(θ) · P(item|θ)^x · [1−P(item|θ)]^(1−x)\nKode aktif: input IRT ke classifier = tidak tersedia; auto-relabel = tidak tersedia",
    "example": "Sekarang request /v2/classify dengan field tambahan b atau theta ditolak kontrak extra=\"forbid\". Pada rancangan berikutnya, schema/model baru harus diuji terlebih dahulu; animasi bagian ini hanya menjelaskan kemungkinan integrasi.",
    "output": {
      "status": "planned_only",
      "currentIrtFeatureInput": false,
      "onlineItemCalibration": false,
      "catEngine": false,
      "automaticRelease": false
    },
    "cautions": [
      "Proposal ini tidak menyatakan fungsi tersebut sudah berjalan di repository.",
      "IRT yang ada tetap batch, local calibration dan research/advisory; tidak ada auto-release calibration.",
      "Profil longitudinal siswa, selector adaptif, CAT, linking/equating, DIF dan UI siswa masih target yang dijelaskan di dokumen 28."
    ],
    "sources": [
      {
        "path": "app/classification/v2/contracts.py",
        "symbol": "V2ClassificationRequest"
      },
      {
        "path": "app/classification/v2/serializer.py",
        "symbol": "serialize_question"
      },
      {
        "path": "API_DOCUMENTATION/28_END_TO_END_PERSONALIZED_ASSESSMENT_FLOW.md",
        "symbol": "G1–G4 / H3"
      }
    ]
  }
];
