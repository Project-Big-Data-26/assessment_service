/* Silver operational flow; numerical examples remain educational. */
window.FLOW_ASSESSMENT_STAGES = [
  {
    "id": "assessment-silver-gate",
    "phase": "Siswa",
    "title": "Gerbang assessment: silver yang qualified",
    "subtitle": "Snapshot AI langsung terhubung ke delivery",
    "status": "implemented",
    "summary": "Snapshot silver didaftarkan ke SQLite. Assessment memakai grade dan track yang cocok tanpa menunggu persetujuan pelabel manusia.",
    "learning": {
      "story": "Snapshot silver didaftarkan ke SQLite. Assessment memakai grade dan track yang cocok tanpa menunggu persetujuan pelabel manusia.",
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
      "why": "Snapshot silver didaftarkan ke SQLite. Assessment memakai grade dan track yang cocok tanpa menunggu persetujuan pelabel manusia.",
      "next": "Snapshot kelas 11 TL dapat dipakai assessment kelas 11 TL meskipun scope IndoBERT lama hanya SD."
    },
    "latex": [
      {
        "title": "Sidik jari paket tes",
        "tex": "H_{\\mathrm{assessment}}=\\operatorname{SHA256}\\!\\left(\\operatorname{canonicalJSON}(B)\\right)",
        "symbols": [
          {
            "symbol": "B",
            "meaning": "Blueprint lengkap: konfigurasi, versi soal, kunci privat, dan kebijakan scoring/delivery."
          },
          {
            "symbol": "H_{\\mathrm{assessment}}",
            "meaning": "Hash yang mengikat identitas assessment ke isi blueprint."
          }
        ],
        "why": "Data yang sama menghasilkan hash yang sama. assessmentId yang sama dengan hash berbeda ditolak, sehingga paket historis tidak tertimpa."
      }
    ],
    "input": {
      "snapshotId": "silver-v2",
      "labelProvenance": "ai_silver",
      "grade": 11,
      "subjectTrack": "tl"
    },
    "process": [
      "POST internal/silver/snapshots memeriksa checksum rows dan expansionRows serta provenance.",
      "POST internal/assessments membaca snapshot terdaftar.",
      "Pilih versi pada grade/track yang sesuai; tolak held versions dan kunci/solusi tidak qualified."
    ],
    "formula": "deliveryEligible = ai_silver ∧ qualified ∧ checksum valid ∧ grade/track cocok ∧ tidak held",
    "example": "Snapshot kelas 11 TL dapat dipakai assessment kelas 11 TL meskipun scope IndoBERT lama hanya SD.",
    "output": {
      "status": "ready",
      "labelProvenance": "ai_silver"
    },
    "cautions": [
      "Delivery teks memerlukan transkripsi gambar essential.",
      "Service key berada di backend integrasi."
    ],
    "sources": [
      {
        "path": "app/assessment/routes.py",
        "symbol": "register_silver_snapshot / create_assessment"
      },
      {
        "path": "app/assessment/store.py",
        "symbol": "validate_snapshot / register_snapshot / create_assessment"
      }
    ]
  },
  {
    "id": "assessment-participant-session",
    "phase": "Siswa",
    "title": "Peserta pseudonim dan sesi",
    "subtitle": "Kenali peserta yang sama tanpa menaruh identitas langsung di jawaban",
    "status": "implemented",
    "summary": "Setelah paket tes siap, operator memberi peserta token privat. Server menghubungkan token itu ke satu identitas pseudonim dalam populasi yang sama dan membuka sesi dengan batas waktu; retry permintaan yang sama mengembalikan sesi lama.",
    "learning": {
      "story": "Setelah daftar soal dikunci, sistem perlu mengetahui siapa pemilik setiap sesi. Kode peserta diubah menjadi subjectHash dengan secret yang stabil, lalu token privat dipakai untuk mengakses sesi. Jika siswa yang sama mengulang tes dengan kode yang konsisten, screening nanti tetap mengenalinya sebagai satu peserta.",
      "terms": [
        {
          "term": "Pseudonim / subjectHash",
          "meaning": "Identitas pengganti yang menghubungkan jawaban siswa tanpa mencantumkan kode asli pada response event.",
          "why": "Diperlukan untuk menghitung peserta unik dan memilih satu attempt per peserta."
        },
        {
          "term": "HMAC",
          "meaning": "Hash dengan kunci rahasia; hasilnya bergantung pada secret, populationId, dan kode peserta.",
          "why": "Kode yang sama dalam populasi yang sama memberi identitas stabil; secret melindungi pemetaan langsung."
        },
        {
          "term": "Bearer token",
          "meaning": "Token privat yang menunjukkan hak peserta untuk mengakses assessment dan sesinya.",
          "why": "Server mengecek kepemilikan sesi sebelum mengirim soal atau menerima jawaban."
        },
        {
          "term": "Idempotency",
          "meaning": "Permintaan yang diulang dengan identitas dan isi yang sama tidak membuat hasil baru.",
          "why": "Retry jaringan tidak menggandakan sesi atau jawaban."
        }
      ],
      "why": "Identitas stabil diperlukan karena jumlah sesi belum tentu sama dengan jumlah siswa: seorang siswa dapat mencoba beberapa kali. Token dan ownership mengikat tindakan ke peserta, sedangkan idempotency membedakan retry dari attempt baru yang sengaja dibuat.",
      "next": "Dengan sesi aktif dan pemiliknya jelas, server dapat mengirim satu soal beserta pilihan yang aman untuk ditampilkan."
    },
    "latex": [
      {
        "title": "Identitas peserta dan waktu sesi",
        "tex": "\\begin{aligned}h_s&=\\operatorname{HMAC\\!\\text{-}\\!SHA256}(K,P\\Vert\\text{NUL}\\Vert C)\\\\t_{\\mathrm{expiry}}&=t_{\\mathrm{start}}+\\Delta t\\end{aligned}",
        "symbols": [
          {
            "symbol": "h_s",
            "meaning": "Subject hash peserta."
          },
          {
            "symbol": "K",
            "meaning": "Secret stabil milik store."
          },
          {
            "symbol": "P",
            "meaning": "Population ID."
          },
          {
            "symbol": "C",
            "meaning": "Kode peserta yang dikelola operator."
          },
          {
            "symbol": "\\text{NUL}",
            "meaning": "Pemisah U+0000 agar gabungan input tidak ambigu."
          },
          {
            "symbol": "\\Delta t",
            "meaning": "Durasi sesi; default 120 menit."
          }
        ],
        "why": "Populasi dan kode yang konsisten memberi identitas yang konsisten. Kode berbeda untuk orang yang sama tidak otomatis digabung."
      }
    ],
    "input": {
      "participantEndpoint": "POST /api/v1/internal/assessments/{assessment_id}/participants",
      "participantCode": "kode-peserta-ilustrasi",
      "startEndpoint": "POST /api/v1/assessments/{assessment_id}/sessions",
      "headers": {
        "Authorization": "Bearer <token peserta privat>",
        "Idempotency-Key": "start-ilustrasi-001"
      }
    },
    "process": [
      "subjectHash adalah HMAC-SHA256 dengan secret stabil; raw participantCode tidak disimpan dalam response event.",
      "Token peserta dibuat acak. Tabel participants menyimpan SHA256(token), assessment_id dan subject_hash.",
      "Start memvalidasi token untuk assessment yang diminta; session ownership selalu diikat ke subject_hash dan assessment_id.",
      "Kombinasi assessmentId, subjectHash, Idempotency-Key yang sama mengembalikan sesi lama. Key start baru dapat membuat attempt baru.",
      "expiresAt = startedAt + sessionTtlMinutes; default 120 menit, kontrak mengizinkan 5–1440 menit.",
      "SQLite BEGIN IMMEDIATE menyerialkan operasi store, termasuk retry dan GET next yang bersamaan."
    ],
    "formula": "subjectHash = HMAC-SHA256(secret, populationId + U+0000 + participantCode)\ntokenHash = SHA256(bearerToken)\nunique session key = (assessmentId, subjectHash, Idempotency-Key)",
    "example": "Membuat dua token untuk participantCode yang sama dalam populationId yang sama tetap menghasilkan subjectHash yang sama. Dua completed attempts kemudian dipilih salah satunya saat screening; siswa tidak dihitung dua kali.",
    "output": {
      "sessionId": "<UUID sesi>",
      "assessmentId": "ilustrasi-kelas1-v1",
      "status": "active",
      "expiresAt": "<timestamp timezone-aware>",
      "nextItemUrl": "/api/v1/sessions/<UUID sesi>/items/next"
    },
    "cautions": [
      "Unique subject bergantung pada participantCode yang konsisten. Dua kode untuk orang yang sama tidak otomatis digabung oleh sistem.",
      "Penggantian secret pada store lama ditolak; migrasi diperlukan agar identitas pseudonim tidak pecah.",
      "Tidak ada jumlah seluruh siswa masa depan atau daftar hadir nasional yang dipakai estimator."
    ],
    "sources": [
      {
        "path": "app/assessment/store.py",
        "symbol": "AssessmentStore.participant / start / _owned_session / connection"
      },
      {
        "path": "app/assessment/routes.py",
        "symbol": "participant_token / start"
      },
      {
        "path": "tests/test_assessment_empirical_flow.py",
        "symbol": "test_store_survives_restart_and_rejects_secret_rotation"
      }
    ]
  },
  {
    "id": "assessment-delivery-mapping",
    "phase": "Siswa",
    "title": "Delivery soal dan mapping opsi",
    "subtitle": "Kirim satu soal; simpan hubungan ID pilihan publik dengan kunci privat",
    "status": "implemented",
    "summary": "Setelah sesi terbuka, server mengambil soal berikutnya dari blueprint. Pilihan diacak sekali dan diberi ID publik; hubungan dengan label internal disimpan, sehingga refresh mengembalikan soal yang sama dan kunci tetap berada di server.",
    "learning": {
      "story": "Setelah peserta memperoleh sesi aktif, server mengirim satu soal untuk dikerjakan. Siswa hanya melihat teks dan ID pilihan publik, sementara server menyimpan pilihan publik itu sebenarnya merujuk opsi A, B, dan seterusnya. Bila halaman dimuat ulang sebelum menjawab, server mengirim ulang delivery yang sama agar pilihan tidak berubah.",
      "terms": [
        {
          "term": "Delivery instance",
          "meaning": "Satu kejadian pengiriman soal kepada satu sesi, dengan ID dan mapping tersendiri.",
          "why": "Jawaban dapat diikat tepat ke versi serta pilihan yang benar-benar dilihat siswa."
        },
        {
          "term": "Mapping opsi",
          "meaning": "Hubungan ID pilihan publik yang acak dengan label opsi internal.",
          "why": "Server tetap dapat menilai pilihan meskipun urutan opsi sudah diacak."
        },
        {
          "term": "Pending delivery",
          "meaning": "Soal yang sudah dikirim tetapi belum mempunyai respons final.",
          "why": "Refresh memakai catatan ini, bukan membuat pengiriman baru."
        },
        {
          "term": "Fixed-form",
          "meaning": "Soal berikutnya mengikuti posisi blueprint, bukan estimasi kemampuan siswa.",
          "why": "Menjelaskan perilaku sekarang dan membedakannya dari rancangan CAT."
        }
      ],
      "why": "Mapping memisahkan informasi yang dibutuhkan siswa dari kunci dan identitas versi yang diperlukan server. Delivery yang disimpan serta transaksi SQLite menjaga agar refresh dan request bersamaan tidak mengubah pilihan atau menggandakan posisi soal.",
      "next": "Sesudah siswa memilih ID publik atau menekan skip, server memakai mapping ini untuk menilai dan menyimpan respons."
    },
    "latex": [
      {
        "title": "Pilihan publik kembali ke opsi internal",
        "tex": "\\begin{aligned}o_{\\mathrm{internal}}&=m(o_{\\mathrm{public}})\\\\k&=\\#\\{\\text{delivery yang sudah dibuat pada sesi}\\}\\end{aligned}",
        "symbols": [
          {
            "symbol": "m",
            "meaning": "Mapping privat milik delivery tertentu."
          },
          {
            "symbol": "o_{\\mathrm{public}}",
            "meaning": "ID pilihan yang dikirim siswa."
          },
          {
            "symbol": "o_{\\mathrm{internal}}",
            "meaning": "Label opsi internal yang dipakai scoring."
          },
          {
            "symbol": "k",
            "meaning": "Indeks berikutnya pada blueprint, mulai dari nol."
          }
        ],
        "why": "Kunci tetap di server. ID yang tidak termasuk mapping delivery ditolak."
      }
    ],
    "input": {
      "endpoint": "GET /api/v1/sessions/{session_id}/items/next",
      "authorization": "Bearer <token pemilik sesi>"
    },
    "process": [
      "Sesi harus aktif dan belum expired. Jika ada delivery yang belum dijawab, server me-replay public item yang sama.",
      "Jika tidak ada pending delivery, sequence berasal dari jumlah deliveries pada sesi; item berikutnya diambil dari posisi blueprint tersebut.",
      "Server mengacak opsi dengan SystemRandom lalu membuat mapping publicOptionId → label internal.",
      "Public response berisi stem/stimulus, teks opsi dan ID publik, sequence serta timing. answerKey, verifiedMinimalSolution, intendedDifficulty, contentHash dan questionVersionId tetap privat.",
      "Unique(session_id, sequence) bersama transaksi memastikan request bersamaan tidak menghasilkan beberapa delivery untuk posisi yang sama.",
      "Versi held tidak dikirim. Setelah semua posisi habis, GET next memberi finished=true; completion tetap langkah tersendiri."
    ],
    "formula": "mapping: id-publik-1 → B; id-publik-2 → A\nnext index = COUNT(deliveries WHERE session_id=...)\nselection = blueprint.items[next index] (fixed-form, bukan CAT)",
    "example": "Kunci internal A boleh berada pada opsi publik kedua. Mengirim selectedOptionIds=['A'] ditolak karena siswa harus mengirim ID publik milik delivery, bukan label internal.",
    "output": {
      "deliveryInstanceId": "<UUID delivery>",
      "item": {
        "publicItemId": "<ID acak>",
        "questionType": "multiple_choice",
        "questionText": "<stem + transcript bila ada>",
        "stimulus": null,
        "options": [
          {
            "id": "id-publik-1",
            "text": "<teks opsi B>"
          },
          {
            "id": "id-publik-2",
            "text": "<teks opsi A>"
          }
        ],
        "media": []
      },
      "sequence": {
        "current": 1,
        "total": 5
      }
    },
    "cautions": [
      "GET next tidak memilih item berdasarkan theta, grade embedding atau riwayat mastery. Online personalization/CAT masih target.",
      "Pilot tidak mengirim media gambar langsung; item visual memerlukan transcript yang diverifikasi."
    ],
    "sources": [
      {
        "path": "app/assessment/store.py",
        "symbol": "AssessmentStore.next_item"
      },
      {
        "path": "app/assessment/contracts.py",
        "symbol": "PublicItem / DeliveredItem"
      },
      {
        "path": "tests/test_assessment_empirical_flow.py",
        "symbol": "test_concurrent_next_item_returns_one_immutable_delivery"
      }
    ]
  },
  {
    "id": "assessment-server-score",
    "phase": "Siswa",
    "title": "Jawaban dinilai server dan disimpan",
    "subtitle": "Jawaban langsung dinilai dan dicatat; IRT belum dihitung pada submit ini",
    "status": "implemented",
    "summary": "Setelah pilihan dikirim, server mengubah ID publik ke opsi internal dan mencocokkannya dengan kunci. Benar menjadi 1, salah 0, dan skip tetap null; event disimpan saat itu juga, tetapi fitting IRT menunggu proses screening batch.",
    "learning": {
      "story": "Setelah soal diterima siswa, pilihan yang dikirim belum dianggap sebagai score dari client. Server memeriksa kepemilikan delivery, membuka mapping, lalu menentukan benar atau salah dari kunci privat. Respons final disimpan sekali; retry yang sama mendapat receipt lama, sedangkan IRT belum dijalankan pada langkah ini.",
      "terms": [
        {
          "term": "Server scoring",
          "meaning": "Server menghitung correctness; client hanya mengirim pilihan atau skip.",
          "why": "Nilai tidak dapat ditetapkan dengan mengirim isCorrect=true dari browser."
        },
        {
          "term": "Response event",
          "meaning": "Catatan final jawaban beserta sesi, versi soal, populasi, waktu, dan flags.",
          "why": "Ini bahan baku yang nanti dibersihkan sebelum disusun menjadi matriks respons."
        },
        {
          "term": "Null / missing",
          "meaning": "Tidak ada skor benar-salah yang dapat dipakai, misalnya explicit skip.",
          "why": "Tidak disamakan dengan 0 karena belum ada observasi jawaban salah."
        },
        {
          "term": "Rapid-guess candidate",
          "meaning": "Flag jawaban non-skip yang diterima lebih cepat dari cutoff waktu server bila cutoff diaktifkan.",
          "why": "Menyaring evidence yang mungkin berasal dari menebak cepat; bukan diagnosis pasti."
        }
      ],
      "why": "Scoring di server menjaga asal nilai, sedangkan satu respons final per delivery mencegah retry menambah evidence ganda. Waktu server dipakai untuk filter rapid guess agar aturan tidak bergantung hanya pada klaim client; default cutoff=null berarti filter itu tidak aktif.",
      "next": "Event masuk saat submit, tetapi seluruh posisi perlu dijawab atau di-skip sebelum sesi menjadi unit sampel screening."
    },
    "latex": [
      {
        "title": "Skor respons dan waktu server",
        "tex": "\\begin{aligned}X_{ij}&=\\begin{cases}1&\\text{jawaban valid dan benar}\\\\0&\\text{jawaban valid dan salah}\\\\\\varnothing&\\text{skip / missing}\\end{cases}\\\\\\tau&=t_{\\mathrm{server}}-t_{\\mathrm{delivery}}\\\\\\Delta t_{\\mathrm{ms}}&=\\max\\!\\left(0,\\left\\lfloor1000\\tau\\right\\rfloor\\right)\\end{aligned}",
        "symbols": [
          {
            "symbol": "X_{ij}",
            "meaning": "Skor peserta i pada item j."
          },
          {
            "symbol": "\\varnothing",
            "meaning": "Null; bukan skor 0."
          },
          {
            "symbol": "t_{\\mathrm{server}}",
            "meaning": "Waktu penerimaan respons menurut server."
          },
          {
            "symbol": "t_{\\mathrm{delivery}}",
            "meaning": "Waktu pengiriman delivery yang disimpan."
          },
          {
            "symbol": "\\Delta t_{\\mathrm{ms}}",
            "meaning": "Response time server dalam milidetik."
          },
          {
            "symbol": "\\tau",
            "meaning": "Selisih waktu penerimaan dan pengiriman dalam detik."
          }
        ],
        "why": "Skor dan waktu berasal dari state server. Event terflag tetap disimpan untuk audit, namun dapat menjadi missing pada analisis."
      }
    ],
    "input": {
      "endpoint": "POST /api/v1/responses",
      "headers": {
        "Idempotency-Key": "response-ilustrasi-001"
      },
      "body": {
        "responseId": "response-ilustrasi-001",
        "deliveryInstanceId": "<UUID delivery>",
        "selectedOptionIds": [
          "id-publik-2"
        ],
        "skipped": false,
        "responseTimeMs": 12000,
        "answerChanges": 1
      }
    },
    "process": [
      "StrictRecord menolak field tambahan seperti isCorrect atau score. Pilih tepat satu public option atau skipped=true dengan selectedOptionIds=[].",
      "Idempotency-Key wajib sama dengan responseId. Ownership sesi serta keanggotaan ID opsi di mapping delivery divalidasi server.",
      "Map opsi ke label internal lalu bandingkan dengan answerKey. isCorrect=true/false, score=1/0; skip menghasilkan isCorrect=null, score=null.",
      "Server menghitung elapsed_ms dari deliveredAt hingga waktu penerimaan; responseTimeMs milik client disimpan terpisah sebagai clientResponseTimeMs.",
      "Jika rapidGuessMs dikonfigurasi dan elapsed_ms < cutoff untuk jawaban non-skip, tandai rapid_guess_candidate. Item yang held setelah delivery diberi item_held_after_delivery. Event tetap disimpan, validForAnalysis=false bila memiliki flag tersebut.",
      "Retry dengan responseId dan hash payload identik mengembalikan receipt lama, termasuk setelah sesi selesai. Payload berubah dengan ID sama atau respons kedua pada delivery sama ditolak.",
      "Receipt hanya accepted=true dan URL berikutnya. Tidak ada correctness, score atau theta yang dikirim kepada siswa pada pilot."
    ],
    "formula": "internalChoice = mapping[selectedOptionId]\nisCorrect = skipped ? null : (internalChoice == answerKey)\nscore = isCorrect == null ? null : int(isCorrect)\nelapsed_ms = max(0, floor((server_now - deliveredAt) × 1000))\nrapid_guess = cutoff != null AND elapsed_ms < cutoff AND NOT skipped",
    "example": "Mapping id-publik-2→A dengan key A menghasilkan score=1. Mengulang payload identik tetap satu event. Jika client mengklaim 12 detik tetapi elapsed server 300 ms dan cutoff=1000 ms, event mendapat rapid_guess_candidate dan tidak dipakai analisis. Default cutoff=null tidak menerapkan filter rapid guess.",
    "output": {
      "receipt": {
        "responseId": "response-ilustrasi-001",
        "accepted": true,
        "nextItemUrl": "/api/v1/sessions/<UUID sesi>/items/next"
      },
      "privateEventFields": [
        "subjectHash",
        "sessionId",
        "deliveryInstanceId",
        "questionVersionId",
        "contentVersion",
        "contentHash",
        "populationId",
        "assessmentFamily",
        "grade",
        "selectedInternalOptionIds",
        "isCorrect",
        "score",
        "responseTimeMs",
        "clientResponseTimeMs",
        "flags",
        "validForAnalysis",
        "submittedAt"
      ]
    },
    "cautions": [
      "Scoring dan penyimpanan event berlangsung saat submit; fitting seluruh bank IRT tidak otomatis dipicu POST response.",
      "Server timing mengurangi manipulasi client tetapi masih mencakup jaringan/idle; rapid guess adalah kandidat screening, bukan diagnosis pasti.",
      "Skip dan event invalid menjadi missing untuk analisis, bukan jawaban salah."
    ],
    "sources": [
      {
        "path": "app/assessment/contracts.py",
        "symbol": "ResponseCreate"
      },
      {
        "path": "app/assessment/routes.py",
        "symbol": "response"
      },
      {
        "path": "app/assessment/store.py",
        "symbol": "AssessmentStore.respond / _receipt"
      },
      {
        "path": "tests/test_assessment_empirical_flow.py",
        "symbol": "test_delivery_scoring_retry_privacy_and_skipped_missing"
      }
    ]
  },
  {
    "id": "assessment-complete-session",
    "phase": "Siswa",
    "title": "Selesaikan sesi sebelum agregasi",
    "subtitle": "Tutup sesi hanya setelah semua posisi dijawab atau di-skip",
    "status": "implemented",
    "summary": "Setelah setiap respons dicatat, server memastikan jumlah respons final sama dengan jumlah item. Sesi yang lengkap diberi status completed; hanya sesi selesai yang dipilih untuk screening, kemudian kualitas responsnya masih diperiksa lagi.",
    "learning": {
      "story": "Setelah jawaban per item tersimpan, sistem perlu membedakan siswa yang sudah selesai dari siswa yang baru mengerjakan sebagian. Completion pertama hanya diterima jika semua posisi sudah mempunyai jawaban atau explicit skip dan sesi belum expired. Completed menjadi tanda bahwa satu administration sudah selesai, bukan tanda bahwa seluruh evidence pasti layak IRT.",
      "terms": [
        {
          "term": "Completed session",
          "meaning": "Satu sesi yang ditutup setelah seluruh posisi mempunyai respons final.",
          "why": "Screening memakai sesi ini agar tidak mencampur administration yang belum selesai."
        },
        {
          "term": "Explicit skip",
          "meaning": "Siswa menyatakan melewati soal, sehingga respons final ada tetapi skornya null.",
          "why": "Completion dapat berjalan tanpa memalsukan skip menjadi jawaban salah."
        },
        {
          "term": "Unit sampling",
          "meaning": "Satuan data yang dipilih bersama untuk analisis; di sini whole completed session.",
          "why": "Satu attempt dipilih utuh agar jawaban terbaik dari beberapa attempt tidak dicampur."
        }
      ],
      "why": "Completion membuat pemilihan administration jelas dan dapat diulang. Meski sesi selesai, skip serta jawaban terflag tetap mengikuti aturan cleaning; jumlah completed sessions belum menentukan N eligible untuk IRT.",
      "next": "Screening selanjutnya memilih sesi selesai dalam window yang diminta dan menghitung peserta uniknya."
    },
    "latex": [
      {
        "title": "Syarat menutup sesi",
        "tex": "n_{\\mathrm{final\\ responses}}=J",
        "symbols": [
          {
            "symbol": "n_{\\mathrm{final\\ responses}}",
            "meaning": "Jumlah respons final sesi, termasuk explicit skip."
          },
          {
            "symbol": "J",
            "meaning": "Jumlah item blueprint."
          }
        ],
        "why": "Ini syarat completion, bukan syarat bahwa seluruh sel analisis memiliki skor 0 atau 1."
      }
    ],
    "input": {
      "endpoint": "POST /api/v1/sessions/{session_id}/complete",
      "headers": {
        "Authorization": "Bearer <token pemilik>",
        "Idempotency-Key": "complete-ilustrasi-001"
      }
    },
    "process": [
      "Server mengecek ownership. Untuk completion pertama, sesi harus masih active dan belum expired.",
      "Jumlah respons final pada sesi harus sama dengan jumlah item blueprint; respons skipped tetap dihitung sebagai respons final.",
      "Jika jumlah belum lengkap, kembalikan 409. Jika lengkap, set status=completed dan completed_at=server timestamp.",
      "Pemanggilan complete ulang pada sesi yang sudah completed mengembalikan status completed; complete tidak membuat event jawaban baru.",
      "Menyelesaikan sesi tidak otomatis menjalankan IRT. Operator berikutnya menjalankan screen secara eksplisit."
    ],
    "formula": "can_complete = COUNT(final responses in session) == itemCount\nsampling eligibility tahap awal = status == completed",
    "example": "Blueprint 5 item: 4 jawaban dan 1 explicit skip dapat selesai; matriks analisis memiliki satu null. Empat jawaban tanpa skip pada item kelima belum dapat selesai.",
    "output": {
      "sessionId": "<UUID sesi>",
      "status": "completed"
    },
    "cautions": [
      "Header Idempotency-Key wajib pada endpoint complete; store melakukan replay berdasarkan status completed, bukan menyimpan record key completion tersendiri.",
      "Completed bukan berarti seluruh sel valid untuk IRT; filter event dan missing peserta masih diperiksa setelahnya."
    ],
    "sources": [
      {
        "path": "app/assessment/store.py",
        "symbol": "AssessmentStore.complete"
      },
      {
        "path": "app/assessment/routes.py",
        "symbol": "complete"
      },
      {
        "path": "tests/test_assessment_empirical_flow.py",
        "symbol": "test_delivery_scoring_retry_privacy_and_skipped_missing"
      }
    ]
  },
  {
    "id": "assessment-sample-window",
    "phase": "Psikometrik",
    "title": "Hitung N sekarang dari window dan peserta unik",
    "subtitle": "Ambil peserta unik yang selesai sekarang, lalu pilih satu attempt utuh",
    "status": "implemented",
    "summary": "Setelah sesi selesai tersedia, operator menjalankan screening untuk satu assessment dan rentang waktu. Server memilih satu attempt per peserta; jumlah siswa untuk analisis adalah sampel yang terpilih saat itu, sehingga tidak perlu menebak berapa siswa akan datang nanti.",
    "learning": {
      "story": "Setelah sesi ditutup, kita dapat mengambil sampel yang tersedia tanpa menunggu semua siswa masa depan. Screening membatasi completion time, lalu memilih satu whole attempt pertama atau terakhir per subjectHash. Jawaban yang datang setelah pembacaan ini diperhitungkan pada screening berikutnya; fitting IRT aktif adalah batch, bukan per-submit.",
      "terms": [
        {
          "term": "Time window",
          "meaning": "Rentang completion time untuk memilih sesi; batas awal termasuk, batas akhir tidak.",
          "why": "Analisis terikat pada sampel periode yang jelas dan dapat diaudit."
        },
        {
          "term": "N selected",
          "meaning": "Jumlah subjectHash unik setelah filter window dan pemilihan attempt.",
          "why": "Berbeda dari token, respons, atau completed sessions yang dapat mencakup pengulangan."
        },
        {
          "term": "N eligible",
          "meaning": "Jumlah baris peserta yang memenuhi minimum observasi setelah cleaning.",
          "why": "Inilah N yang diperiksa pada gate IRT, sehingga dapat lebih kecil dari N selected."
        },
        {
          "term": "First / last attempt",
          "meaning": "Satu whole session pertama/terakhir dalam urutan started_at lalu id pada window.",
          "why": "Menghindari penghitungan siswa dua kali dan pencampuran jawaban antarattempt."
        }
      ],
      "why": "Kalibrasi membutuhkan sampel yang tersedia dan terdefinisi, bukan jumlah siswa masa depan. Window dan attempt policy mengendalikan perubahan sampel secara eksplisit; snapshot berikutnya dapat memakai evidence baru tanpa menulis ulang snapshot lama.",
      "next": "Dari sesi terpilih, normalisasi membersihkan response events dan membentuk baris peserta serta kolom versi soal."
    },
    "latex": [
      {
        "title": "Window dan jumlah observasi",
        "tex": "\\begin{aligned}t_{\\mathrm{from}}&\\le t_{\\mathrm{completed}}<t_{\\mathrm{to}}\\\\N_{\\mathrm{selected}}&=\\left|\\{\\text{subject unik terpilih}\\}\\right|\\\\n_j&=\\sum_{i=1}^{N_{\\mathrm{selected}}}O_{ij}\\end{aligned}",
        "symbols": [
          {
            "symbol": "t_{\\mathrm{completed}}",
            "meaning": "Waktu completion sesi; bukan waktu satu respons."
          },
          {
            "symbol": "N_{\\mathrm{selected}}",
            "meaning": "Jumlah peserta unik terpilih."
          },
          {
            "symbol": "O_{ij}",
            "meaning": "1 bila sel i,j mempunyai skor valid 0/1 setelah cleaning, selainnya 0."
          },
          {
            "symbol": "n_j",
            "meaning": "Jumlah observasi valid item j; dapat berbeda antaritem."
          }
        ],
        "why": "Completed sessions, peserta unik, dan respons valid per item memiliki denominator berbeda. N eligible diketahui setelah pola missing tiap peserta diperiksa."
      }
    ],
    "input": {
      "endpoint": "POST /api/v1/internal/psychometrics/screen",
      "assessmentId": "ilustrasi-kelas1-v1",
      "model": "rasch",
      "attemptPolicy": "first",
      "fromTime": "2026-10-01T00:00:00+07:00",
      "toTime": "2026-10-03T00:00:00+07:00",
      "assumptionReview": "<review AI bila sudah tersedia>"
    },
    "process": [
      "Ambil status=completed hanya untuk assessmentId yang diminta, urutkan started_at lalu id.",
      "Window menggunakan session.completed_at: fromTime inklusif, toTime eksklusif. Timestamp harus timezone-aware; kedua nilai boleh null.",
      "attemptPolicy=first mengambil whole session pertama per subjectHash; last mengambil yang terakhir dalam urutan started_at,id di window. Jangan gabungkan jawaban terbaik dari beberapa attempt.",
      "Ambil response events dari sesi terpilih, lalu lepaskan transaksi sebelum pekerjaan numerik. Respons yang masuk kemudian baru diperhitungkan pada screen berikutnya.",
      "Jika tidak ada completed session terpilih, screen memberi 409 dengan instruksi mengumpulkan respons. Tidak ada fallback data simulasi.",
      "N_selected=jumlah subjectHash unik terpilih; N_eligible baru dihitung setelah missing-person filter. Denominator per item n_j menghitung sel 0/1 valid item itu, sehingga dapat berbeda dari N.",
      "Sistem tidak mempunyai scheduler realtime fitting dalam jalur ini. Screening periodik berbasis waktu/jumlah peserta adalah rancangan operasi yang bisa memakai endpoint tersedia, dan harus diimplementasikan terpisah."
    ],
    "formula": "window = [fromTime, toTime) pada completed_at\nN_selected = |unique subjectHash dari whole completed attempts terpilih|\nN_eligible = Σ_i 1(observed_i / J ≥ 0.70)\nn_j = Σ_i 1(X_ij ∈ {0,1})",
    "example": "Ilustrasi: 142 completed sessions total assessment, beberapa attempt berulang dan sebagian di luar window; sesudah window+dedup terdapat 130 unique subjects, setelah filter missing terdapat 119 eligible. N untuk gate Rasch=119. Banyaknya event atau token peserta tidak menggantikan hitungan ini. Peserta berikutnya menambah evidence pada snapshot baru.",
    "output": {
      "cleaning": {
        "completedSessions": "jumlah seluruh completed sessions assessment sebelum filter window",
        "selectedSessions": "jumlah subject unik setelah window dan first/last",
        "selectionUnit": "whole_completed_session",
        "timeWindowBasis": "session_completed_at"
      },
      "normalization": {
        "persons": "N_selected"
      },
      "readiness": {
        "eligiblePersons": "N_eligible"
      }
    },
    "cautions": [
      "completedSessions pada output aktual menghitung seluruh completed sessions assessment, termasuk yang di luar window; selectedSessions sudah sesudah filter dan dedup.",
      "Tidak perlu menunggu seluruh roster masa depan selesai. Kelulusan gate saat ini tetap memerlukan sampel representatif dan bukan sekadar N besar.",
      "Window terbuka dapat berubah saat screen diulang. Gunakan cutoff toTime untuk window yang ditutup, lalu simpan snapshot baru bila data/policy berubah."
    ],
    "sources": [
      {
        "path": "app/assessment/store.py",
        "symbol": "AssessmentStore.screen"
      },
      {
        "path": "app/psychometrics/contracts.py",
        "symbol": "ScreeningInput.time_window"
      },
      {
        "path": "tests/test_assessment_empirical_flow.py",
        "symbol": "test_attempt_policy_selects_whole_session_and_AI_hold_does_not_relabel"
      }
    ]
  },
  {
    "id": "assessment-clean-matrix",
    "phase": "Psikometrik",
    "title": "Bersihkan event dan susun matriks 0/1/null",
    "subtitle": "Bersihkan bukti, lalu pisahkan benar, salah, dan belum teramati",
    "status": "implemented",
    "summary": "Setelah sesi dipilih, event diperiksa agar identitas versi, populasi, dan scoring konsisten. Hasilnya matriks dengan satu baris per peserta dan satu kolom per versi soal: 1 benar, 0 salah, null bila tidak ada observasi valid.",
    "learning": {
      "story": "Setelah kita tahu sesi mana yang diikutkan, responsnya belum langsung dihitung semua. Normalisasi mengeluarkan konflik ID, mismatch versi/populasi, rapid guess, dan scoring yang tidak konsisten, sambil menyimpan jumlah alasan exclusion. Matriks akhir mempertahankan null agar tidak adanya evidence tidak disalahartikan sebagai jawaban salah.",
      "terms": [
        {
          "term": "Response matrix",
          "meaning": "Tabel peserta × item; setiap sel hanya 0, 1, atau null.",
          "why": "Memberi bentuk data bersama untuk perhitungan CTT dan likelihood IRT."
        },
        {
          "term": "Observed mask",
          "meaning": "Tabel penanda 1 untuk skor 0/1 yang sah, dan 0 untuk missing.",
          "why": "Menghitung denominator serta menghilangkan kontribusi missing dari likelihood."
        },
        {
          "term": "Coverage",
          "meaning": "Proporsi sel dengan observasi valid dari seluruh sel matriks.",
          "why": "Menunjukkan banyaknya evidence; coverage agregat belum memberi N eligible dengan sendirinya."
        },
        {
          "term": "Complete case",
          "meaning": "Peserta dengan observasi valid pada semua item dalam form.",
          "why": "Dipakai untuk korelasi skor total, discrimination dan KR-20 tanpa mengisi missing sebagai nol."
        }
      ],
      "why": "Mengisi null dengan 0 akan mengubah pola kemampuan seolah siswa menjawab salah. Kode mempertahankan missing: CTT per item memakai observasi item itu, metrik berbasis total memakai complete cases, sedangkan IRT memakai baris eligible dan hanya sel observed.",
      "next": "Dengan matriks yang jelas, sistem dapat menghitung statistik tes klasik dan melihat seberapa pasti proporsi benar setiap soal."
    },
    "latex": [
      {
        "title": "Coverage dan missing per item",
        "tex": "\\begin{aligned}O_{ij}&=\\mathbf{1}\\{X_{ij}\\in\\{0,1\\}\\}\\\\C&=\\frac{\\sum_i\\sum_jO_{ij}}{N_{\\mathrm{selected}}J}\\\\M_j&=1-\\frac{n_j}{N_{\\mathrm{selected}}}\\end{aligned}",
        "symbols": [
          {
            "symbol": "O_{ij}",
            "meaning": "Observed mask setelah cleaning."
          },
          {
            "symbol": "C",
            "meaning": "Coverage matriks sebelum filter peserta IRT."
          },
          {
            "symbol": "N_{\\mathrm{selected}}",
            "meaning": "Jumlah baris peserta terpilih."
          },
          {
            "symbol": "J",
            "meaning": "Jumlah kolom item."
          },
          {
            "symbol": "M_j",
            "meaning": "Missing rate item j."
          },
          {
            "symbol": "n_j",
            "meaning": "Jumlah skor valid 0/1 pada item j."
          }
        ],
        "why": "Setiap item mempunyai denominator observed sendiri. Null tidak dihitung sebagai benar ataupun salah."
      }
    ],
    "input": {
      "events": "response events dari whole sessions terpilih",
      "items": "questionId, questionVersionId, contentVersion, contentHash dan reference blueprint",
      "subjectIds": "subjectHash unik, diurutkan"
    },
    "process": [
      "Duplicate responseId dengan isi sama dihitung sebagai duplicate_event dan dipakai sekali. responseId dengan isi berbeda dianggap conflict; semua kandidat ID itu dikeluarkan.",
      "Version reference harus cocok pada questionId, questionVersionId, contentVersion dan contentHash.",
      "populationId, assessmentFamily, grade dan subjectHash harus cocok dengan konteks screening.",
      "Event harus validForAnalysis=true, tanpa rapid_guess_candidate, memiliki scoringStatus scored/skipped, isCorrect berupa boolean/null yang konsisten, dan submittedAt timezone-aware.",
      "Repeated cell dalam administration terpilih diselesaikan menurut submittedAt dengan first/last yang eksplisit; exclusion counts disimpan.",
      "Sel benar=1, salah=0, skipped/event dikeluarkan/tidak ada event=null. MatrixAnalysisInput melarang nilai lain, string angka, bool, duplicate subjects, versi duplicate dan dua versi questionId yang sama.",
      "Kontrak membatasi ≤10000 subjects, ≤200 items dan ≤500000 sel. Endpoint matriks eksternal menolak klaim dataOrigin=server_scored; provenance server hanya dari aggregator screen."
    ],
    "formula": "X_ij = 1 jika valid dan benar; 0 jika valid dan salah; null jika missing\ncoverage = jumlah sel observed / (N_selected × J)\nmissingRate_j = 1 − n_j / N_selected\ncomplete cases = baris dengan seluruh J sel observed",
    "example": "Matriks ilustratif [[1,0,null],[0,1,1],[null,1,0]] mempunyai N=3, J=3, 7 observed cells, 2 missing cells, coverage=7/9=0.7778. Item pertama n_1=2, correct=1, p=0.5. Hanya baris kedua merupakan complete case.",
    "output": {
      "matrix": [
        [
          1,
          0,
          null
        ],
        [
          0,
          1,
          1
        ],
        [
          null,
          1,
          0
        ]
      ],
      "dataOrigin": "server_scored",
      "cleaning": {
        "inputEvents": "jumlah event input",
        "selectedEvents": "jumlah event setelah cleaning, termasuk explicit skip",
        "exclusions": "counts menurut alasan"
      },
      "normalization": {
        "observedCells": 7,
        "missingCells": 2,
        "missingScore": null
      }
    },
    "cautions": [
      "CTT per item menggunakan semua baris validnya; correlation/discrimination/KR-20 menggunakan complete cases. IRT menggunakan baris yang lolos missing-person gate, bukan harus complete case.",
      "Contoh 3×3 hanya ilustrasi format dan tidak memenuhi gate IRT produksi proyek."
    ],
    "sources": [
      {
        "path": "app/psychometrics/analysis.py",
        "symbol": "normalize_events / analyze_matrix"
      },
      {
        "path": "app/psychometrics/contracts.py",
        "symbol": "MatrixAnalysisInput.rectangular_binary_matrix"
      },
      {
        "path": "app/assessment/routes.py",
        "symbol": "item_analysis"
      }
    ]
  },
  {
    "id": "assessment-ctt-metrics",
    "phase": "Psikometrik",
    "title": "CTT: p, interval, diskriminasi dan kualitas tes",
    "subtitle": "Lihat proporsi benar dan ketidakpastiannya sebelum menarik kesimpulan",
    "status": "implemented",
    "summary": "Setelah matriks bersih, CTT menghitung proporsi siswa yang menjawab benar dan intervalnya. Sistem juga menilai hubungan item dengan skor lain, konsistensi tes, pilihan distraktor, dan waktu; hasil ini tetap tersedia ketika data belum siap untuk IRT.",
    "learning": {
      "story": "Setelah respons menjadi matriks, langkah paling langsung adalah menghitung p: jumlah benar dibagi jumlah respons valid pada item. Wilson interval menunjukkan bahwa p=0.80 dari sampel kecil belum mempunyai kepastian yang sama dengan p=0.80 dari sampel besar. Perbedaan label awal baru diberi flag ketika seluruh interval berada pada band empiris yang berbeda; label awal belum ditimpa.",
      "terms": [
        {
          "term": "CTT / teori tes klasik",
          "meaning": "Statistik item dan tes yang dihitung langsung dari respons sampel, termasuk proporsi benar.",
          "why": "Memberi pengamatan awal walau gate IRT belum terpenuhi."
        },
        {
          "term": "Difficulty index p",
          "meaning": "Proporsi respons valid yang benar pada item dalam sampel ini.",
          "why": "P besar berarti lebih banyak benar; berbeda dari b IRT yang besar berarti lebih sulit."
        },
        {
          "term": "Wilson CI95",
          "meaning": "Interval ketidakpastian proporsi benar dengan z=1.96.",
          "why": "Seluruh interval dipakai untuk memastikan band CTT stabil sebelum flag disagreement."
        },
        {
          "term": "KR-20",
          "meaning": "Ukuran konsistensi internal tes berskor 0/1 dari variansi, yaitu sebaran skor item dan total pada complete cases.",
          "why": "Memberi pemeriksaan kualitas tes; bukan label difficulty atau kemampuan seorang siswa."
        }
      ],
      "why": "Proporsi saja mudah berubah karena sampel, jadi kode memakai interval dan minimum evidence untuk routing. Korelasi memakai total tanpa item yang diuji agar hubungan tidak naik hanya karena item itu ikut dalam total; variansi KR-20 memakai denominator sampel yang konsisten.",
      "next": "CTT memberi observasi awal. Sebelum estimasi IRT, sistem mengecek peserta eligible, data tiap item, desain, dan review asumsi."
    },
    "latex": [
      {
        "title": "Proporsi benar dan band CTT",
        "tex": "\\begin{aligned}p_j&=\\frac{k_j}{n_j}\\\\\\operatorname{band}(p_j)&=\\begin{cases}\\text{Easy}&p_j>0.7\\\\\\text{Hard}&p_j<0.3\\\\\\text{Medium}&0.3\\le p_j\\le0.7\\end{cases}\\end{aligned}",
        "symbols": [
          {
            "symbol": "k_j",
            "meaning": "Jumlah respons benar item j."
          },
          {
            "symbol": "n_j",
            "meaning": "Jumlah skor valid 0/1 item j."
          },
          {
            "symbol": "p_j",
            "meaning": "Proporsi benar pada populasi/window ini."
          }
        ],
        "why": "Menggunakan respons teramati per item dan tidak memasukkan missing ke denominator."
      },
      {
        "title": "Interval Wilson 95%",
        "tex": "\\begin{aligned}d&=1+\\frac{z^2}{n}\\\\\\mu_W&=\\frac{p+z^2/(2n)}{d}\\\\m_W&=\\frac{z}{d}\\sqrt{\\frac{p(1-p)}{n}+\\frac{z^2}{4n^2}}\\\\\\mathrm{CI}_{95}&=[\\max(0,\\mu_W-m_W),\\min(1,\\mu_W+m_W)]\\end{aligned}",
        "symbols": [
          {
            "symbol": "z",
            "meaning": "1.96 untuk interval 95% yang dipakai kode."
          },
          {
            "symbol": "n",
            "meaning": "Jumlah respons valid item."
          },
          {
            "symbol": "\\mu_W",
            "meaning": "Titik tengah interval Wilson."
          },
          {
            "symbol": "m_W",
            "meaning": "Setengah lebar interval."
          }
        ],
        "why": "Membedakan perbedaan p yang belum pasti dari band stabil; width>0.3 diberi flag terpisah."
      },
      {
        "title": "Hubungan item dengan skor lain",
        "tex": "\\begin{aligned}r_{\\mathrm{pb},j}&=\\operatorname{Corr}(X_j,T-X_j)\\\\D_j&=\\overline{X_j\\mid T-X_j\\ge q_{0.73}}\\\\&\\quad-\\overline{X_j\\mid T-X_j\\le q_{0.27}}\\end{aligned}",
        "symbols": [
          {
            "symbol": "T",
            "meaning": "Total skor complete-case peserta."
          },
          {
            "symbol": "r_{\\mathrm{pb},j}",
            "meaning": "Corrected point-biserial: correlation skor item dengan rest score."
          },
          {
            "symbol": "D_j",
            "meaning": "Selisih proporsi benar kelompok rest-score tinggi dan rendah."
          },
          {
            "symbol": "q_{0.27},\\ q_{0.73}",
            "meaning": "Quantile rest score; ties dapat mengubah ukuran kelompok."
          }
        ],
        "why": "Mengurangi score item dari total menghindari hubungan dengan dirinya sendiri. Kode memerlukan ≥8 complete cases dan kondisi variansi/quantile yang mendukung."
      },
      {
        "title": "KR-20 dengan variansi sampel konsisten",
        "tex": "\\begin{aligned}\\mathrm{KR20}&=\\frac{J}{J-1}\\left(1-\\frac{\\sum_{j=1}^{J}s_j^2}{s_T^2}\\right)\\\\s^2&=\\frac{\\sum_{i=1}^{n_c}(x_i-\\bar{x})^2}{n_c-1}\\end{aligned}",
        "symbols": [
          {
            "symbol": "J",
            "meaning": "Jumlah item; minimal dua."
          },
          {
            "symbol": "s_j^2",
            "meaning": "Variansi sampel item j pada complete cases."
          },
          {
            "symbol": "s_T^2",
            "meaning": "Variansi total skor complete cases; harus positif."
          },
          {
            "symbol": "n_c",
            "meaning": "Jumlah complete cases; kode memerlukan minimal delapan."
          }
        ],
        "why": "Item dan total memakai peserta yang sama dan ddof=1. Nilai negatif menjadi warning, bukan dipaksa positif."
      }
    ],
    "input": {
      "matrix": "matriks 0/1/null",
      "events": "opsional untuk timing/distractor",
      "intendedDifficulty": "Easy / Medium / Hard dari reference versi soal"
    },
    "process": [
      "n_j=jumlah jawaban 0/1 valid, k_j=jumlah benar, p_j=k_j/n_j. Band CTT: Easy bila p>0.7, Hard bila p<0.3, Medium pada 0.3≤p≤0.7; tanpa observasi nilainya null.",
      "Wilson 95% memakai z=1.96. intended_empirical_disagreement hanya diberikan jika seluruh CI berada dalam satu band dan band itu berbeda dari intendedDifficulty.",
      "Corrected point-biserial = Pearson correlation(X_j, total score − X_j) pada complete cases; perlu ≥8 dan variansi tidak nol.",
      "Discrimination = mean(X_j pada rest score ≥ quantile_0.73) − mean(X_j pada rest score ≤ quantile_0.27), complete cases ≥8 dan quantile bawah < atas. Ties dapat membuat kelompok bukan tepat 27%.",
      "KR-20 proyek = J/(J−1) × (1 − Σ sample item variance / sample total-score variance), complete cases ≥8, J≥2, variansi total positif. Semua variansi memakai ddof=1.",
      "Dari events: hitung optionSelectionCounts, distractor yang dipilih <5% seluruh jawaban valid, distractorEfficiency, median responseTimeMs dan IQR=P75−P25. Matriks eksternal tanpa events menghasilkan timing/distractor null.",
      "Review flags: sample per item <50, lebar CI>0.3, semua benar/salah, diskriminasi negatif, disagreement stabil, distractor tidak berfungsi. Routing collect_more_events jika sample/CI/variation lemah; jika flags lainnya ai_review; tanpa flags observation_only."
    ],
    "formula": "p=k/n; d=1+z²/n\nWilson center=(p+z²/(2n))/d\nWilson margin=z√[(p(1−p)+z²/(4n))/n]/d\nCI=[max(0,center−margin),min(1,center+margin)]\nr_pb=Corr(X_j, T−X_j)\nD=mean(X_j|rest≥q.73)−mean(X_j|rest≤q.27)\nKR20=J/(J−1)·[1−Σ Var_sample(X_j)/Var_sample(T)]\ndistractorEfficiency=1−nonFunctioningCount/distractorCount",
    "example": "Ilustrasi 80 benar dari 100: p=0.80, Wilson CI95=[0.711169,0.866634], band=Easy. Karena lower CI>0.7, intendedDifficulty=Medium mendapat intended_empirical_disagreement. Label awal tetap Medium sampai workflow review/versioning selesai. Distractor A,B,C selain key: satu dipilih 2/100 (<0.05) → satu non-functioning; efficiency=2/3.",
    "output": {
      "validResponseCount": 100,
      "correctCount": 80,
      "difficultyIndex": 0.8,
      "difficultyCi95": [
        0.7111690380734977,
        0.8666340774409013
      ],
      "empiricalDifficulty": "Easy",
      "totalScoreJoin": "complete_cases_only",
      "additionalFields": [
        "discrimination",
        "correctedPointBiserial",
        "missingRate",
        "optionSelectionCounts",
        "distractorEfficiency",
        "nonFunctioningDistractors",
        "medianResponseTimeMs",
        "responseTimeIqrMs",
        "kr20"
      ]
    },
    "cautions": [
      "P besar berarti lebih banyak benar pada sampel ini. IRT b besar berarti lebih sulit pada skala lokal; p dan b tidak boleh disamakan.",
      "KR-20 kode ini memakai variansi sampel yang konsisten, bukan mengganti satu bagian dengan p(1−p) tanpa koreksi denominator.",
      "Flag disagreement aktif berasal dari CI CTT yang stabil. Kode tidak otomatis memberi flag intended vs IRT b atau menulis ulang label."
    ],
    "sources": [
      {
        "path": "app/psychometrics/analysis.py",
        "symbol": "analyze_matrix / _correlation"
      },
      {
        "path": "app/evaluation/psychometrics.py",
        "symbol": "wilson_interval"
      },
      {
        "path": "configs/psychometrics_policy.json",
        "symbol": "easyP / hardP / maxCiWidth / distractorMinRate"
      }
    ]
  },
  {
    "id": "assessment-irt-readiness",
    "phase": "Psikometrik",
    "title": "Gerbang kesiapan Rasch, 2PL dan 3PL",
    "subtitle": "Pastikan bukti dan asumsi cukup sebelum membuat estimasi IRT",
    "status": "conditional",
    "summary": "Setelah CTT dihitung, sistem memeriksa apakah IRT layak dijalankan pada sampel ini. Peserta dengan terlalu banyak missing dikeluarkan dari fit; jumlah peserta, jumlah item, observasi dan variasi per item, keterhubungan desain, serta asumsi semuanya harus lolos.",
    "learning": {
      "story": "Setelah melihat statistik awal, kita belum boleh menganggap IRT pasti dapat diestimasi. Kode memilih peserta dengan minimal 70% observasi, lalu mengecek kecukupan data seluruh item dan review asumsi. Jika ada syarat gagal, output menyatakan menunggu beserta alasannya; CTT tetap ada dan parameter IRT tidak dibuat-buat.",
      "terms": [
        {
          "term": "Readiness gate",
          "meaning": "Syarat yang harus semuanya lolos sebelum optimizer IRT dipanggil.",
          "why": "Menghindari fit yang dipaksakan pada data atau desain yang belum mendukung."
        },
        {
          "term": "Eligible participant",
          "meaning": "Peserta dengan observed/J minimal 70% setelah cleaning.",
          "why": "Jumlah eligible dibandingkan dengan minimum peserta tiap model."
        },
        {
          "term": "Connected design",
          "meaning": "Seluruh item terhubung melalui peserta yang menjawab pasangan item.",
          "why": "Bagian bank yang terpisah tidak ditopang pola respons bersama dalam kalibrasi ini."
        },
        {
          "term": "Assumption review",
          "meaning": "Review berbukti: tes mengukur satu kemampuan dominan; pada kemampuan yang sama, jawaban item tidak saling bergantung; sampel mewakili populasi sasaran.",
          "why": "Boolean true harus berasal dari review yang sah; bukan bukti otomatis karena form sudah diisi."
        }
      ],
      "why": "Rasch, 2PL, dan 3PL memiliki kompleksitas parameter berbeda, sehingga policy proyek memberi minimum berbeda. Gate juga memerlukan respons benar dan salah per item agar optimizer tidak hanya melihat satu outcome; ambang ini aturan proyek dan tidak menjamin validitas universal.",
      "next": "Hanya bila semua gate lolos, fit_irt menjalankan integrasi kemampuan dan optimisasi parameter item pada fit matrix."
    },
    "latex": [
      {
        "title": "Peserta eligible dan coverage fit",
        "tex": "\\begin{aligned}E_i&=\\mathbf{1}\\!\\left\\{\\frac{\\sum_jO_{ij}}{J}\\ge0.70\\right\\}\\\\N_{\\mathrm{eligible}}&=\\sum_iE_i\\\\C_{\\mathrm{fit}}&=\\frac{\\sum_i\\sum_jE_iO_{ij}}{N_{\\mathrm{eligible}}J}\\ge0.70\\end{aligned}",
        "symbols": [
          {
            "symbol": "E_i",
            "meaning": "1 jika peserta i memenuhi batas missing default, selainnya 0."
          },
          {
            "symbol": "O_{ij}",
            "meaning": "Penanda skor valid 0/1."
          },
          {
            "symbol": "N_{\\mathrm{eligible}}",
            "meaning": "Jumlah peserta yang dipakai fit."
          },
          {
            "symbol": "C_{\\mathrm{fit}}",
            "meaning": "Coverage sesudah filter peserta; dicek bila ada peserta eligible."
          }
        ],
        "why": "Coverage agregat tidak menentukan eligible rows. Dengan lima item, minimal empat jawaban valid diperlukan agar ≥70%."
      },
      {
        "title": "Minimum menurut model dan per item",
        "tex": "\\begin{gathered}\\begin{array}{c|rr}\\text{Model}&N_{\\min}&J_{\\min}\\\\\\hline\\text{Rasch}&100&5\\\\\\text{2PL}&300&10\\\\\\text{3PL}&1000&20\\end{array}\\\\n_{j,\\mathrm{fit}}\\ge50,\\quad k_{j,\\mathrm{fit}}\\ge5\\\\n_{j,\\mathrm{fit}}-k_{j,\\mathrm{fit}}\\ge5\\end{gathered}",
        "symbols": [
          {
            "symbol": "N_{\\min},\\ J_{\\min}",
            "meaning": "Minimum peserta eligible dan item dari policy aktif."
          },
          {
            "symbol": "n_{j,\\mathrm{fit}}",
            "meaning": "Observed responses item j setelah filter peserta."
          },
          {
            "symbol": "k_{j,\\mathrm{fit}}",
            "meaning": "Jumlah benar pada item j setelah filter peserta."
          }
        ],
        "why": "Minimum N saja tidak cukup. Setiap item juga harus memiliki sample dan outcome variation yang memadai."
      },
      {
        "title": "Keterhubungan antaritem",
        "tex": "G_{jk}=\\mathbf{1}\\!\\left\\{\\sum_{i:E_i=1}O_{ij}O_{ik}>0\\right\\}",
        "symbols": [
          {
            "symbol": "G_{jk}",
            "meaning": "Ada sisi graph jika minimal satu peserta eligible mengamati kedua item."
          },
          {
            "symbol": "O_{ij}O_{ik}",
            "meaning": "1 bila peserta i punya skor valid pada item j dan k."
          }
        ],
        "why": "Kode menelusuri graph dan meminta semua item terjangkau. Ketiga asumsi tetap memerlukan review terpisah."
      }
    ],
    "input": {
      "policyVersion": "empirical-dichotomous-v1",
      "minPersons": {
        "rasch": 100,
        "2pl": 300,
        "3pl": 1000
      },
      "minItems": {
        "rasch": 5,
        "2pl": 10,
        "3pl": 20
      },
      "minResponsesPerItem": 50,
      "minOutcomeCount": 5,
      "minCoverage": 0.7,
      "maxPersonMissingRate": 0.3,
      "assumptionReview": {
        "reviewedBy": "<AI peninjau>",
        "evidence": "<bukti empiris yang benar-benar ditinjau>",
        "unidimensional": true,
        "localIndependence": true,
        "representativeSample": true
      }
    },
    "process": [
      "Person keep = mean(observed cells dalam baris) ≥ 1−maxPersonMissingRate. Default berarti minimal 70% item memiliki respons 0/1 valid.",
      "N_eligible harus memenuhi minPersons model; jumlah kolom J harus memenuhi minItems model.",
      "Coverage setelah filter peserta harus ≥0.7. Setiap item pada fit matrix memerlukan ≥50 observed responses, ≥5 benar dan ≥5 salah.",
      "Graph item co-observation harus connected: pasangan item terhubung bila ada peserta eligible yang menjawab keduanya; seluruh item harus terjangkau.",
      "assumptionReview wajib tersedia dan ketiga booleans harus true. Ini review AI atas unidimensionality, local independence dan representative sample, bukan pemeriksaan otomatis yang terbukti hanya dari boolean.",
      "Jika asumsi belum ditinjau/tidak didukung, status waiting_for_assumption_review; jika gate data gagal tetapi asumsi lolos, waiting_for_data. Semua failures tetap dilaporkan.",
      "Bila semua gate lolos baru panggil fit_irt. Tidak ada pengisian estimate a,b,c atau theta buatan saat gate gagal."
    ],
    "formula": "N_eligible=Σ_i 1(observed_i/J ≥ 0.70)\ncoverage_fit=observed fit cells/(N_eligible·J) ≥0.70\n∀j: n_j_fit≥50 AND correct_j_fit≥5 AND incorrect_j_fit≥5\nreadiness.passed=(failures.length == 0)",
    "example": "2PL dengan 280 eligible dan 12 item tetap gagal insufficient_persons walau ada 400 token peserta. Rasch 110 eligible/5 item juga gagal bila salah satu item hanya punya 4 respons salah. Untuk 5 item, ≥70% mengharuskan minimal 4 jawaban valid; untuk 10 item minimal 7, untuk 12 item minimal 9.",
    "output": {
      "readiness": {
        "passed": false,
        "eligiblePersons": 280,
        "coverage": 0.9,
        "failures": [
          "insufficient_persons"
        ]
      },
      "irt": {
        "status": "waiting_for_data",
        "model": "2pl",
        "items": [],
        "persons": [],
        "warnings": []
      }
    },
    "cautions": [
      "Threshold 100/300/1000 adalah kebijakan proyek yang aktif, bukan jaminan validitas universal.",
      "Ambang tepat memakai ≥. Contoh readiness ini mengasumsikan gate lainnya, termasuk review asumsi, telah lolos.",
      "Connected design dan sample representative tidak otomatis menjamin linking antar-populasi atau fairness."
    ],
    "sources": [
      {
        "path": "configs/psychometrics_policy.json",
        "symbol": "seluruh policy readiness"
      },
      {
        "path": "app/psychometrics/analysis.py",
        "symbol": "analyze_matrix / _connected"
      },
      {
        "path": "app/psychometrics/contracts.py",
        "symbol": "AssumptionReview / AnalysisPolicy"
      },
      {
        "path": "tests/test_empirical_analysis.py",
        "symbol": "test_disconnected_forms_and_excess_missing_cannot_be_calibrated"
      }
    ]
  },
  {
    "id": "assessment-irt-marginal-fit",
    "phase": "Psikometrik",
    "title": "IRT: probabilitas, integrasi kemampuan dan optimisasi",
    "subtitle": "Cari parameter item dari pola bersama, dengan kemampuan yang belum diketahui",
    "status": "conditional",
    "summary": "Setelah gate lolos, IRT mencari parameter yang paling menjelaskan pola benar-salah seluruh peserta. Karena kemampuan siswa belum diketahui, sistem mengintegrasikan kemungkinan kemampuan dengan prior lokal, lalu meminimalkan objective regularized memakai L-BFGS-B.",
    "learning": {
      "story": "Setelah sampel siap, kita ingin menjelaskan mengapa satu item lebih sering benar untuk peserta tertentu daripada item lain. IRT memakai kurva probabilitas berdasarkan kemampuan theta dan parameter item a, b, c; theta belum dianggap sebagai data yang diketahui. Kode mengintegrasikan theta pada 41 titik Gauss–Hermite, menambahkan prior, lalu mengoptimasi parameter item bersama dengan L-BFGS-B, bukan outer loop EM.",
      "terms": [
        {
          "term": "Theta / kemampuan laten",
          "meaning": "Kemampuan yang tidak diamati langsung, diestimasi melalui pola respons.",
          "why": "Kalibrasi menetapkan skala lokal theta~N(0,1); belum comparable lintas populasi tanpa linking."
        },
        {
          "term": "Sigmoid",
          "meaning": "Fungsi berbentuk S yang mengubah skor a(theta−b) menjadi probabilitas antara 0 dan 1.",
          "why": "Memberi kurva respons monotone untuk diskriminasi a yang positif."
        },
        {
          "term": "Marginal likelihood",
          "meaning": "Peluang pola respons yang diamati menurut model, setelah berbagai kemungkinan kemampuan dirata-ratakan dengan bobot prior.",
          "why": "Parameter item dicari tanpa menganggap kemampuan siswa sebagai input yang sudah pasti."
        },
        {
          "term": "Prior / regularization",
          "meaning": "Preferensi parameter pada objective, seperti b pada skala N(0,3²).",
          "why": "Membantu estimasi numerik tetap finite pada pola ekstrem; bukan pengganti evidence atau jaminan benar."
        }
      ],
      "why": "Menghitung b hanya dari logit(p) mengabaikan pola bersama antarpeserta dan antaritem. Marginal likelihood memanfaatkan pola itu sambil memperhitungkan berbagai kemungkinan theta. Gauss–Hermite mengganti integral dengan sejumlah titik dan bobot yang ditentukan secara matematis; L-BFGS-B mencari parameter yang menurunkan objective sambil menghormati batas parameter, memakai gradient analitis. Prior dan bounds membantu kestabilan numerik; ini bukan jaminan model benar.",
      "next": "Parameter item kemudian dipakai untuk posterior kemampuan peserta, uncertainty, diagnostics kecocokan, dan informasi tes."
    },
    "latex": [
      {
        "title": "Kurva probabilitas IRT",
        "tex": "\\begin{aligned}P_j(\\theta)&=c_j+(1-c_j)\\sigma\\!\\left(a_j(\\theta-b_j)\\right)\\\\\\sigma(z)&=\\frac{1}{1+e^{-z}}\\\\P_j(b_j)&=\\frac{1+c_j}{2}\\end{aligned}",
        "symbols": [
          {
            "symbol": "a_j",
            "meaning": "Kemiringan/diskriminasi item; Rasch menetapkan a=1."
          },
          {
            "symbol": "b_j",
            "meaning": "Lokasi difficulty pada skala theta lokal."
          },
          {
            "symbol": "c_j",
            "meaning": "Lower asymptote; Rasch/2PL c=0, 3PL mengestimasi c."
          },
          {
            "symbol": "\\theta",
            "meaning": "Kemampuan laten; D=1 dalam logistic ini."
          }
        ],
        "why": "b lebih besar menggeser kurva ke kemampuan lebih tinggi. Pada 3PL P(theta=b) bukan selalu 0.5, dan c bukan otomatis 1/jumlah opsi."
      },
      {
        "title": "Integrasi marginal dengan Gauss–Hermite",
        "tex": "\\begin{aligned}t_q&=\\sqrt{2}\\,h_q,\\quad v_q=\\frac{w_q}{\\sqrt{\\pi}}\\\\L_i&\\approx\\sum_{q=1}^{41}v_q\\prod_{j:O_{ij}=1}P_j(t_q)^{X_{ij}}\\bigl(1-P_j(t_q)\\bigr)^{1-X_{ij}}\\end{aligned}",
        "symbols": [
          {
            "symbol": "h_q,\\ w_q",
            "meaning": "Nodes dan weights dari numpy.hermgauss(41)."
          },
          {
            "symbol": "t_q,\\ v_q",
            "meaning": "Grid theta dan bobot prior untuk N(0,1)."
          },
          {
            "symbol": "L_i",
            "meaning": "Marginal likelihood pola respons peserta i."
          },
          {
            "symbol": "O_{ij}",
            "meaning": "Observed mask; hanya skor valid ikut produk."
          }
        ],
        "why": "Missing memberi kontribusi likelihood nol dalam log-space. Kode memakai logsumexp agar probabilitas kecil tidak menyebabkan underflow."
      },
      {
        "title": "Objective dan prior optimizer",
        "tex": "\\begin{aligned}\\mathcal{J}&=-\\sum_i\\log L_i+\\sum_j\\frac{b_j^2}{18}\\\\&\\quad+\\delta_A\\sum_j\\frac{(\\log a_j)^2}{2(0.75)^2}\\\\&\\quad-\\delta_C\\sum_j\\bigl[4\\log c_j+16\\log(1-c_j)\\bigr]\\end{aligned}",
        "symbols": [
          {
            "symbol": "𝒥",
            "meaning": "Negative marginal log-likelihood ditambah penalty prior; diminimalkan."
          },
          {
            "symbol": "\\delta_A",
            "meaning": "1 untuk 2PL/3PL, 0 untuk Rasch."
          },
          {
            "symbol": "\\delta_C",
            "meaning": "1 untuk 3PL, selainnya 0."
          },
          {
            "symbol": "\\sum_j b_j^2/18",
            "meaning": "Penalty b~N(0,3²)."
          },
          {
            "symbol": "\\sum_j\\frac{(\\log a_j)^2}{2(0.75)^2}",
            "meaning": "Prior log a~N(0,0.75²)."
          },
          {
            "symbol": "-\\sum_j[4\\log c_j+16\\log(1-c_j)]",
            "meaning": "Prior Beta(5,17), dengan batas c dari kode."
          }
        ],
        "why": "Ini objective regularized sebenarnya. Bounds: b∈[−5,5], a∈[0.2,4], c∈[0.001,0.35] saat 3PL. Bagian δ_C=0 dihilangkan pada Rasch/2PL; tidak menghitung log(0)."
      },
      {
        "title": "Inisialisasi bukan hasil akhir b",
        "tex": "\\begin{aligned}p_{0j}&=\\frac{k_j+0.5}{n_j+1}\\\\b_{0j}&=\\operatorname{clip}\\!\\left(\\log\\frac{1-p_{0j}}{p_{0j}},-3,3\\right)\\end{aligned}",
        "symbols": [
          {
            "symbol": "k_j,\\ n_j",
            "meaning": "Benar dan observed count pada fit matrix."
          },
          {
            "symbol": "p_{0j}",
            "meaning": "Proporsi dengan smoothing untuk initializer."
          },
          {
            "symbol": "b_{0j}",
            "meaning": "Parameter awal sebelum optimisasi seluruh pola respons."
          }
        ],
        "why": "Smoothing menjaga nilai awal finite. Final b berasal dari objective marginal yang dioptimasi, bukan rumus p tunggal ini."
      }
    ],
    "input": {
      "fitMatrix": "N_eligible × J, 0/1/NaN",
      "model": "rasch / 2pl / 3pl",
      "quadraturePoints": 41,
      "maxIterations": 300,
      "tolerance": 0.000001
    },
    "process": [
      "Rasch mengestimasi b dengan a=1,c=0; 2PL mengestimasi b dan log(a) dengan c=0; 3PL juga mengestimasi c. D=1, latent theta~N(0,1), kalibrasi lokal.",
      "Inisialisasi p0_j=(correct_j+0.5)/(observed_j+1), b0_j=clip(log((1−p0_j)/p0_j),−3,3). log(a) mulai 0 sehingga a=1; c 3PL mulai 0.15.",
      "hermgauss(41) menghasilkan nodes h_q dan weights w_q. Theta grid t_q=√2·h_q; prior quadrature weights v_q=w_q/√π.",
      "Hitung P_qj=c_j+(1−c_j)·sigmoid[a_j(t_q−b_j)], clip ke [1e−12,1−1e−12]. Set skor missing menjadi 0 hanya pada array aljabar dengan observed mask; missing tetap kontribusi likelihood nol.",
      "Untuk setiap peserta, joint log weight = Σ observed[X log(P)+(1−X)log(1−P)] + log(v_q). logsumexp menstabilkan integrasi marginal.",
      "Minimalkan negative marginal log-likelihood + prior penalty menggunakan scipy.optimize.minimize L-BFGS-B, jac=True, maxiter=300, ftol=1e−6, gtol=1e−5.",
      "Prior penalty: Σ b²/18 (b~N(0,3²)); tambah Σ log(a)²/(2·0.75²) untuk 2PL/3PL; tambah −Σ[4log(c)+16log(1−c)] untuk 3PL, Beta(5,17). Batas b∈[−5,5], a∈[0.2,4], c∈[0.001,0.35] untuk 3PL.",
      "Gradient analitis memakai posterior grid, expected_correct=posteriorᵀ·scores dan expected_count=posteriorᵀ·observed. Kode melakukan optimisasi langsung; tidak menjalankan outer loop EM E-step/M-step terpisah."
    ],
    "formula": "P_ij=c_j+(1−c_j)·σ[a_j(θ_i−b_j)]\nσ(z)=1/(1+exp(−z))\nL_i=Σ_q v_q ∏_{j observed} P_qj^Xij(1−P_qj)^(1−Xij)\nobjective=−Σ_i log(L_i)+Σ_j b_j²/18\n  + Σ_j log(a_j)²/(2·0.75²) [2PL/3PL]\n  − Σ_j[4log(c_j)+16log(1−c_j)] [3PL]\nposterior_iq=exp(joint_iq−logsumexp_q joint_iq)",
    "example": "Ilustrasi probabilitas: theta=0,b=−1.2 Rasch → P=0.768525. Dengan a=1.4,b=0.5, 2PL → P=0.331812; tambah c=0.2 untuk 3PL → P=0.465450. Pada 80/100 benar, initializer b0=−1.367832; ini bukan final b. Fit juga memakai pola respons lintas item/seluruh peserta dan prior. Demo sintetis resmi seed=42, Rasch 180×12 menghasilkan item pertama b=−1.965912, bukan b dari sekadar logit(p).",
    "output": {
      "method": "regularized_marginal_likelihood_gauss_hermite",
      "scale": "theta ~ N(0,1); logistic D=1; no cross-population linking",
      "items": "a,b,c untuk tiap kolom fit matrix",
      "converged": "optimizer success",
      "iterations": "L-BFGS-B iteration count",
      "logLikelihood": "Σ log(L_i), sebelum penalty",
      "status": "estimated / estimated_with_warnings / failed"
    },
    "cautions": [
      "b untuk 3PL adalah titik tengah antara c dan 1: P(theta=b)=(1+c)/2, bukan selalu 0.5.",
      "c adalah lower asymptote yang diestimasi dengan prior/bounds; tidak otomatis 1/jumlah opsi.",
      "Angka demo di sini eksplisit sintetis dan tidak menyatakan ada calibration release untuk siswa nyata.",
      "Parameter b pada dua calibration/population berbeda belum comparable tanpa linking/equating."
    ],
    "sources": [
      {
        "path": "app/psychometrics/irt.py",
        "symbol": "response_probability / fit_irt / posterior / objective"
      },
      {
        "path": "scripts/psychometrics.py",
        "symbol": "simulated_matrix"
      },
      {
        "path": "configs/psychometrics_policy.json",
        "symbol": "quadraturePoints / maxIterations / tolerance"
      }
    ]
  },
  {
    "id": "assessment-eap-diagnostics-information",
    "phase": "Psikometrik",
    "title": "EAP siswa, uncertainty, fit dan informasi tes",
    "subtitle": "Beri estimasi kemampuan beserta ketidakpastian, lalu cek apakah model cocok",
    "status": "conditional",
    "summary": "Setelah parameter item ditemukan, posterior respons setiap peserta menghasilkan theta EAP dan SD. Sistem juga menghitung uncertainty b, infit/outfit, informasi tes, AIC/BIC, dan Q3; semua ini diagnostics lokal, bukan jaminan validitas atau confidence IndoBERT.",
    "learning": {
      "story": "Setelah parameter item tersedia, pola jawaban seorang peserta memberi bobot berbeda pada kemungkinan theta. EAP mengambil rata-rata posterior itu, dan posterior SD menunjukkan seberapa tersebar kemungkinan kemampuannya. Sistem lalu memeriksa kecocokan respons dengan model serta uncertainty parameter item, agar satu angka theta atau b tidak ditafsirkan tanpa konteks.",
      "terms": [
        {
          "term": "EAP / posterior",
          "meaning": "Posterior adalah distribusi kemungkinan kemampuan sesudah melihat jawaban; EAP mengambil rata-rata distribusi itu.",
          "why": "Memberi estimasi finite pada skala lokal, termasuk pola semua-benar atau semua-salah dengan prior."
        },
        {
          "term": "Posterior SD",
          "meaning": "Ukuran penyebaran kemampuan yang masih mungkin menurut posterior.",
          "why": "Theta dibaca bersama uncertainty; berbeda dari confidence/entropy classifier."
        },
        {
          "term": "Hessian / curvature",
          "meaning": "Matriks turunan kedua objective, mengukur kelengkungan di sekitar optimum.",
          "why": "Inverse curvature memberi SD b jika optimum dan identifikasinya mendukung; bukan frequentist SE tanpa prior."
        },
        {
          "term": "Fit diagnostics",
          "meaning": "Pemeriksaan seperti infit/outfit dan Q3 untuk respons yang menyimpang atau bergantung.",
          "why": "Menjadi evidence review, bukan aturan otomatis bahwa item atau tes sudah valid."
        }
      ],
      "why": "Rata-rata posterior menggabungkan pola jawaban dengan prior dan SD menjelaskan keterbatasan evidence. Optimizer yang converged belum menjamin model sesuai asumsi atau penggunaannya, sehingga diagnostics diperiksa. Test information menunjukkan wilayah theta tempat item lebih informatif; AIC/BIC di sini hanya deskriptif.",
      "next": "Hasil dan diagnostics disimpan bersama sampel serta policy dalam snapshot immutable untuk ditinjau AI."
    },
    "latex": [
      {
        "title": "Posterior, EAP, dan SD kemampuan",
        "tex": "\\begin{aligned}\\rho_{iq}&=\\frac{v_q\\prod_{j:O_{ij}=1}P_j(t_q)^{X_{ij}}(1-P_j(t_q))^{1-X_{ij}}}{L_i}\\\\\\widehat{\\theta}_{i,\\mathrm{EAP}}&=\\sum_q\\rho_{iq}t_q\\\\s_{\\theta_i}&=\\sqrt{\\max\\!\\left(0,\\sum_q\\rho_{iq}t_q^2-\\widehat{\\theta}_{i,\\mathrm{EAP}}^2\\right)}\\end{aligned}",
        "symbols": [
          {
            "symbol": "\\rho_{iq}",
            "meaning": "Bobot posterior peserta i pada titik theta t_q."
          },
          {
            "symbol": "v_q",
            "meaning": "Bobot prior quadrature."
          },
          {
            "symbol": "L_i",
            "meaning": "Likelihood marginal dari jumlah quadrature pada tahap sebelumnya."
          },
          {
            "symbol": "\\widehat{\\theta}_{i,\\mathrm{EAP}}",
            "meaning": "Rata-rata theta posterior."
          },
          {
            "symbol": "s_{\\theta_i}",
            "meaning": "Posterior SD kemampuan."
          }
        ],
        "why": "Bobot dihitung dari log-joint yang dinormalisasi dengan logsumexp. Missing dikeluarkan; tanpa evidence kembali ke prior, tetapi baris itu tidak lolos fit gate."
      },
      {
        "title": "Uncertainty b dari curvature",
        "tex": "\\begin{aligned}s_{b_j}&=\\sqrt{(H^{-1})_{jj}}\\\\\\mathrm{CI}_{b_j}&\\approx[b_j-1.96s_{b_j},\\ b_j+1.96s_{b_j}]\\end{aligned}",
        "symbols": [
          {
            "symbol": "H",
            "meaning": "Hessian simetris objective regularized pada optimum."
          },
          {
            "symbol": "(H^{-1})_{jj}",
            "meaning": "Posisi parameter b_j pada Hessian penuh; covariance antaritem disertakan."
          },
          {
            "symbol": "s_{b_j}",
            "meaning": "bPosteriorSd dari curvature, bukan unpenalized frequentist SE."
          }
        ],
        "why": "Kode memakai central difference gradient step 10⁻⁴; perlu optimizer sukses, tanpa boundary, dan eigenvalue minimum H>10⁻⁷. Jika tidak mendukung, uncertainty dapat null."
      },
      {
        "title": "Infit dan outfit item",
        "tex": "\\begin{aligned}e_{ij}&=X_{ij}-P_j(\\widehat\\theta_i)\\\\V_{ij}&=P_j(\\widehat\\theta_i)(1-P_j(\\widehat\\theta_i))\\\\\\operatorname{infit}_j&=\\frac{\\sum_iO_{ij}e_{ij}^2}{\\sum_iO_{ij}V_{ij}}\\\\\\operatorname{outfit}_j&=\\frac{\\sum_iO_{ij}e_{ij}^2/V_{ij}}{\\sum_iO_{ij}}\\end{aligned}",
        "symbols": [
          {
            "symbol": "e_{ij}",
            "meaning": "Selisih skor observed dengan probabilitas pada theta EAP."
          },
          {
            "symbol": "V_{ij}",
            "meaning": "Variansi Bernoulli; kode membatasi minimum 10⁻⁹ untuk stabilitas."
          },
          {
            "symbol": "O_{ij}",
            "meaning": "1 untuk skor observed dan 0 untuk missing."
          },
          {
            "symbol": "\\operatorname{infit}_j,\\ \\operatorname{outfit}_j",
            "meaning": "Ukuran residual kuadrat dengan pembobotan variance yang berbeda."
          }
        ],
        "why": "Kode memberi irt_misfit_candidate jika infit atau outfit>1.5; ini memicu review, bukan otomatis membuang atau relabel item."
      },
      {
        "title": "Informasi item dan tes",
        "tex": "\\begin{aligned}L_j(\\theta)&=\\sigma\\!\\left(a_j(\\theta-b_j)\\right)\\\\P_j^{\\prime}(\\theta)&=(1-c_j)a_jL_j(\\theta)(1-L_j(\\theta))\\\\I_j(\\theta)&=\\frac{[P_j^{\\prime}(\\theta)]^2}{P_j(\\theta)(1-P_j(\\theta))}\\\\I_{\\mathrm{test}}(\\theta)&=\\sum_jI_j(\\theta)\\end{aligned}",
        "symbols": [
          {
            "symbol": "L_j(\\theta)",
            "meaning": "Sigmoid bagian logistic; berbeda dari P_j saat c_j>0."
          },
          {
            "symbol": "P_j^{\\prime}",
            "meaning": "Laju perubahan probabilitas benar terhadap theta."
          },
          {
            "symbol": "I_j",
            "meaning": "Informasi item pada kemampuan tertentu."
          },
          {
            "symbol": "I_{\\mathrm{test}}",
            "meaning": "Jumlah informasi seluruh item pada theta yang sama."
          }
        ],
        "why": "Backend memakai 25 titik −3 sampai 3, langkah 0.25; berbeda dari 41 titik quadrature fitting. Informasi besar berarti kurva lebih sensitif terhadap theta di wilayah itu."
      },
      {
        "title": "AIC/BIC deskriptif dan Q3",
        "tex": "\\begin{aligned}\\mathrm{AIC}&=2K-2\\ell\\\\\\mathrm{BIC}&=K\\log N_{\\mathrm{eligible}}-2\\ell\\\\Q3_{jk}&=\\operatorname{Corr}(e_j,e_k)\\\\Q3_{jk}^{\\mathrm{adj}}&=Q3_{jk}-\\overline{Q3}\\end{aligned}",
        "symbols": [
          {
            "symbol": "K",
            "meaning": "Jumlah parameter item: J Rasch, 2J 2PL, 3J 3PL."
          },
          {
            "symbol": "\\ell",
            "meaning": "Log-likelihood marginal tanpa penalty pada estimates regularized."
          },
          {
            "symbol": "Q3_{jk}",
            "meaning": "Correlation residual pasangan item dengan ≥30 paired observations."
          },
          {
            "symbol": "Q3_{jk}^{\\mathrm{adj}}",
            "meaning": "Q3 dikurangi rata-rata semua Q3 yang dapat dihitung."
          }
        ],
        "why": "AIC/BIC bukan approval model-selection. adjusted Q3>0.2 menjadi suspect pair/local-dependence warning, bukan bukti independence terpenuhi."
      }
    ],
    "input": {
      "itemParameters": "a,b,c hasil fit",
      "posteriorGrid": "posterior_iq pada 41 titik theta",
      "fitMatrix": "observed mask dan skor tiap peserta"
    },
    "process": [
      "thetaEap_i=Σ posterior_iq·t_q. posteriorSd_i=√max(0,Σ posterior_iq·t_q²−thetaEap_i²). answeredItems_i=jumlah observed cells baris itu.",
      "Jika optimizer sukses dan tidak ada parameter berjarak <0.001 dari batas, Hessian diperoleh dari central difference analytical gradient dengan step=1e−4, disimetriskan, lalu diperiksa eigenvalue minimum>1e−7.",
      "bPosteriorSd=√diag(Hessian⁻¹) untuk parameter b; bInterval95=b±1.96·SD. Ini curvature posterior regularized dengan covariance antar-item, bukan frequentist SE tanpa prior. Bila tak teridentifikasi, uncertainty null/warning.",
      "Pada person EAP, e_ij=X_ij−P_ij dan V_ij=P_ij(1−P_ij), clip V≥1e−9. Item infit=Σ observed e²/Σ observed V; outfit=mean observed(e²/V). Nilai >1.5 menghasilkan irt_misfit_candidate; tidak otomatis membuang item.",
      "Band IRT: Easy bila b<−1, Hard bila b>1, selain itu Medium. Output juga menyimpan optimizer_not_converged, parameter_at_boundary atau uncertainty_not_identified bila terjadi.",
      "Test information dihitung pada 25 titik theta dari −3 sampai 3 dengan langkah 0.25: I_j(theta)=(dP_j/dtheta)²/[P_j(1−P_j)], testInformation=Σ_j I_j. Ini grid berbeda dari 41 titik quadrature fitting.",
      "AIC=2K−2logLikelihood; BIC=K log(N_eligible)−2logLikelihood. K=J Rasch,2J 2PL,3J 3PL. Values deskriptif pada regularized estimates, bukan approval model selection.",
      "Residual Q3 adalah correlation pasangan residual dengan ≥30 paired observations. adjustedQ3=Q3−mean(Q3 pairs); >0.2 menjadi suspectPairs/local_dependence_candidate dan status estimated_with_warnings.",
      "Subject IDs/EAP hanya ada pada full staff snapshot. Ini belum online theta scorer/CAT dan tidak menjadi mastery otomatis per topik."
    ],
    "formula": "EAP_i=Σ_q posterior_iq·t_q\nSD_i=√[Σ_q posterior_iq·t_q²−EAP_i²]\nSE_b_curvature=√diag(H⁻¹)_b; CI_b=b±1.96·SE_b_curvature\ninfit_j=Σ_i O_ij(X_ij−P_ij)² / Σ_i O_ijP_ij(1−P_ij)\noutfit_j=Σ_i O_ij[(X_ij−P_ij)²/(P_ij(1−P_ij))] / Σ_i O_ij\ndP/dθ=(1−c)·a·σ[a(θ−b)]·(1−σ[a(θ−b)])\nI_j(θ)=(dP/dθ)²/[P(1−P)]; I_test=Σ_j I_j\nAIC=2K−2ℓ; BIC=Klog(N_eligible)−2ℓ\nadjustedQ3(left,right)=Corr(residual_left,residual_right)−mean_Q3",
    "example": "Ilustrasi conditional scoring dengan parameter tetap, bukan bank yang dirilis: Rasch b=[−1,0,1], respons=[1,1,0], prior N(0,1), quadrature 41 → thetaEap=0.315435, posteriorSd=0.795630. Demo sintetis 180×12 seed42: item pertama b=−1.965912, bPosteriorSd=0.232781, interval=[−2.422163,−1.509661], infit=1.042699, outfit=1.138196; person pertama EAP=0.901460, SD=0.596344, answeredItems=11.",
    "output": {
      "itemFields": [
        "a",
        "b",
        "c",
        "bPosteriorSd",
        "bInterval95",
        "infit",
        "outfit",
        "empiricalDifficulty"
      ],
      "personFields": [
        "subjectId",
        "thetaEap",
        "posteriorSd",
        "answeredItems"
      ],
      "diagnostics": [
        "converged",
        "iterations",
        "logLikelihood",
        "aic",
        "bic",
        "warnings",
        "testInformation",
        "localDependenceScreen"
      ]
    },
    "cautions": [
      "Posterior SD theta bukan confidence classifier IndoBERT atau entropy label; ketiganya mengukur uncertainty yang berbeda.",
      "EAP lokal bukan percentile nasional, mastery seluruh topik atau hasil online yang sudah disediakan endpoint siswa.",
      "Q3 adalah screen local dependence, bukan bukti asumsi independence terpenuhi. Data boundary/non-convergence perlu review.",
      "Current code menyimpan parameter boundary/Q3 sebagai global IRT warnings; per-item reviewFlags tidak memuat seluruh global warning."
    ],
    "sources": [
      {
        "path": "app/psychometrics/irt.py",
        "symbol": "fit_irt: eap / hessian / infit / outfit / information / AIC / BIC"
      },
      {
        "path": "app/psychometrics/analysis.py",
        "symbol": "analyze_matrix: localDependenceScreen"
      },
      {
        "path": "app/psychometrics/contracts.py",
        "symbol": "IrtItemParameters / PersonEstimate / IrtResult"
      }
    ]
  },
  {
    "id": "assessment-snapshot-review",
    "phase": "Psikometrik",
    "title": "Snapshot immutable dan feedback otomatis",
    "subtitle": "Analisis menghasilkan keputusan sistem",
    "status": "implemented",
    "summary": "Screen membekukan hasil CTT/IRT dan secara otomatis menyimpan feedback satu per versi item.",
    "learning": {
      "story": "Screen membekukan hasil CTT/IRT dan secara otomatis menyimpan feedback satu per versi item.",
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
      "why": "Screen membekukan hasil CTT/IRT dan secara otomatis menyimpan feedback satu per versi item.",
      "next": "Sampel lemah meminta data tambahan. Kandidat masalah kualitas ditahan untuk AI revalidation."
    },
    "latex": [
      {
        "title": "Identitas snapshot dan pengaruh keputusan",
        "tex": "\\begin{aligned}H_S&=\\operatorname{SHA256}(\\operatorname{canonicalJSON}(R))\\\\\\mathrm{id}_S&=\\text{psy-}\\Vert\\operatorname{prefix}_{24}(H_S)\\\\\\operatorname{held}(v)&=\\mathbf{1}\\{a_{\\mathrm{latest},v}\\in\\{\\text{revise},\\text{quarantine}\\}\\}\\end{aligned}",
        "symbols": [
          {
            "symbol": "R",
            "meaning": "Result lengkap sebelum snapshotId dan createdAt ditambahkan."
          },
          {
            "symbol": "H_S",
            "meaning": "Snapshot hash 64 hex."
          },
          {
            "symbol": "\\operatorname{prefix}_{24}",
            "meaning": "24 hex pertama untuk snapshotId."
          },
          {
            "symbol": "a_{\\mathrm{latest},v}",
            "meaning": "Tindakan empiris terakhir bagi versi v."
          }
        ],
        "why": "Hash sama me-replay snapshot lama. Output tetap researchOnly=true, reviewRequired=true, automaticLabelReplacement=false; keputusan menyimpan affectsSilverLabels=false."
      }
    ],
    "input": {
      "assessmentId": "pilot-1",
      "model": "rasch"
    },
    "process": [
      "Pilih session selesai per peserta dan window.",
      "Simpan snapshot hasil yang immutable.",
      "Simpan keputusan retain, collect_more_events atau needs_ai_review; GET decisions membaca audit."
    ],
    "formula": "feedback = policy(reviewFlags, sampleQuality)",
    "example": "Sampel lemah meminta data tambahan. Kandidat masalah kualitas ditahan untuk AI revalidation.",
    "output": {
      "actorType": "system",
      "affectsSilverLabels": false
    },
    "cautions": [
      "Screen dipanggil integrasi; tidak dijalankan setiap respons.",
      "Difficulty empiris tidak menimpa intendedDifficulty."
    ],
    "sources": [
      {
        "path": "app/assessment/store.py",
        "symbol": "screen / _automated_decisions / _held"
      },
      {
        "path": "app/psychometrics/analysis.py",
        "symbol": "recommendedRouting"
      }
    ]
  }
];
