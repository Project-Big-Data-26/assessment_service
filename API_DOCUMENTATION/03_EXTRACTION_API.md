# Extraction API

Implementasi aktual: `/v1/extract` sinkron dan agentic CLI menghasilkan staging, lalu import dan qualification AI silver. Pilot server-scored dan CTT/IRT kini tersedia setelah silver dibekukan; [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md). Async extraction jobs/authoring gateway pada contoh di bawah tetap target.

## 1. Posisi modul

Extraction API mengubah PDF, gambar, atau data terstruktur menjadi **authoring candidate**. Hasil ekstraksi belum membuktikan kunci benar dan belum memberi label tiga head. OCR menjaga teks, rumus, tabel/grafik dan provenance karena bukti tersebut akan diperlukan IndoBERT dan penilaian AI.

Teacher dapat memperbaiki candidate di authoring UI sebelum menyimpannya sebagai draft. Tindakan tersebut adalah revisi input/authoring, bukan review atau adjudikasi.

## 2. Endpoint target

```http
POST /api/v1/extractions
Content-Type: multipart/form-data
Idempotency-Key: <uuid>

GET /api/v1/extractions/{jobId}
POST /api/v1/questions/from-extraction
```

Prototype FastAPI Python menyediakan ekstraksi sinkron; `POST /api/v1/ai/extract` adalah kontrak gateway lama yang sudah dihapus bersama `project_assessment`. Target resource-oriented API memakai job karena OCR dan formula recognition dapat berlangsung lama.

## 3. Input dan keamanan

Multipart field wajib: `file`.

Format target:

- PDF;
- PNG/JPEG/TIFF;
- JSON/CSV;
- TXT/TEX.

Gateway target memeriksa:

- size limit;
- ekstensi dan MIME signature;
- checksum/idempotency;
- malware scan;
- tenancy/owner;
- object-storage retention policy.

## 4. Respons create job

```json
{
  "jobId": "EXT-001",
  "status": "queued",
  "statusUrl": "/api/v1/extractions/EXT-001"
}
```

## 5. Extraction result

```json
{
  "jobId": "EXT-001",
  "status": "completed_with_warnings",
  "source": {
    "filename": "soal-aljabar.pdf",
    "mediaType": "application/pdf",
    "checksumSha256": "...",
    "pageCount": 1
  },
  "engine": {
    "pipelineVersion": "extractor-0.2.0",
    "textEngine": "pymupdf+tesseract",
    "formulaEngine": "pp-formulanet"
  },
  "candidates": [
    {
      "candidateId": "CAND-001",
      "questionText": "Jika $x^2+5x+6=0$, tentukan akar-akarnya.",
      "options": [],
      "latexCandidates": ["x^2+5x+6=0"],
      "pageNumbers": [1],
      "confidence": 0.87,
      "warnings": [
        {"code": "options_not_detected", "severity": "medium"}
      ],
      "visualPreviews": [
        {
          "previewId": "PREV-001",
          "mediaType": "image/webp",
          "url": "/api/v1/extractions/EXT-001/previews/PREV-001",
          "cropMethod": "question_bounds"
        }
      ]
    }
  ]
}
```

Gunakan signed/resource URL untuk preview production. Data URL besar tidak dijadikan kontrak utama karena membebani JSON dan caching.

## 6. Status

```text
queued -> running -> completed
                  -> completed_with_warnings
                  -> failed
                  -> quarantined
```

`completed` hanya berarti pipeline ekstraksi selesai. Ia tidak berarti konten atau formula benar.

## 7. Membuat draft dari candidate

```http
POST /api/v1/questions/from-extraction
```

```json
{
  "extractionJobId": "EXT-001",
  "candidateId": "CAND-001",
  "authoringContent": {
    "subject": "Matematika",
    "grade": 10,
    "topic": "Aljabar",
    "subtopic": "Persamaan Kuadrat",
    "learningObjective": "Menerapkan pemfaktoran",
    "questionType": "multiple_choice",
    "questionText": "Jika $x^2+5x+6=0$, tentukan akar-akarnya.",
    "options": [],
    "answerSpec": {"kind": "option_ids", "optionIds": []},
    "source": {"origin": "extraction", "extractionJobId": "EXT-001"}
  }
}
```

Teacher boleh memperbaiki candidate sebelum create. Server tetap menyimpan lineage ke job/candidate dan membentuk `author_draft`; workflow otomatis belum berjalan sampai teacher memanggil submit.

## 8. Recovery otomatis

```text
text layer -> PyMuPDF
scanned page -> render higher DPI -> Tesseract ind+eng
formula region -> layout detection -> formula OCR
structured source -> schema-aware parser

low quality
  -> alternate DPI/engine/segmentation
  -> bounded retry
  -> quarantined jika tetap gagal
```

Sistem tidak boleh mengarang teks atau formula untuk memaksa candidate lolos.

## 9. Frontend contract

Frontend hanya perlu memahami:

```ts
type ExtractionPort = {
  create(file: File): Promise<{ jobId: string; statusUrl: string }>;
  get(jobId: string): Promise<ExtractionJob>;
  createDraft(input: CreateQuestionFromExtraction): Promise<QuestionResource>;
};
```

UI tidak mengetahui PyMuPDF, Tesseract, Paddle, lokasi object storage, atau detail queue.

## 10. Status implementasi

Ada dua implementasi ekstraksi Python yang perlu dibedakan. `POST /v1/extract` pada `app/main.py` adalah parser/OCR sinkron umum. Pipeline `app/services/pretest/agentic/` adalah batch lokal khusus pasangan Buku Siswa/Buku Guru: `pymupdf4llm` membuat Markdown per halaman dan indeks, Claude Code menyusun `babNN.json`, lalu validator memeriksa teks verbatim, angka, bukti kunci, opsi senilai, subbab dan gambar. Pipeline lama regex + Ollama masih tersimpan tetapi bukan jalur kanonis baru.

Output agentic adalah **staging evidence**, bukan silver. `app/ingestion/pretest_import.py` dan `scripts/load_candidates_to_atlas.py` kini membentuk identity/content version immutable, hash, provenance, opsi stabil, serta routing qualification langsung dari `babNN.json`. `draft` agentic tetap tidak berarti validasi AI. Private asset signer tersedia sebagai helper sumber, sedangkan job gateway publik, MIME signature, antivirus, dan retry orchestration masih target. Kontrak dan pemetaan lengkap ada pada [dokumen 21](21_PRETEST_AGENTIC_PIPELINE_INTEGRATION.md).
