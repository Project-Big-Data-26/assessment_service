# Alur Ekstraksi Soal

## Tujuan

Modul ini mengubah PDF, gambar, atau file terstruktur menjadi kandidat soal yang dapat direview. Hasil ekstraksi tidak langsung dianggap sebagai soal final dan tidak menebak kunci jawaban.

## Alur eksekusi

```text
File sumber
    |
    +-- validasi ekstensi dan batas ukuran API
    |
    +-- PDF --------------------------------------------------+
    |      |                                                  |
    |      +-- PyMuPDF membuka dokumen                        |
    |      +-- text layer tersedia -> ekstraksi terurut       |
    |      +-- text layer kosong/terlalu pendek -> render      |
    |          300 DPI -> OCR Tesseract ind+eng               |
    |                                                         |
    +-- gambar -> OCR Tesseract ind+eng                       |
    +-- JSON/CSV/TXT/TEX -> parser terstruktur/langsung       |
                                                              |
                                                              v
                teks + provenance per halaman + confidence
                                      |
                                      v
                   segmentasi nomor soal dan opsi A-H
                                      |
                                      v
               crop visual per soal (WebP lossless)
                                      |
                                      v
       JSON kandidat + gambar platform + warning + review_required
```

## Batas tanggung jawab

- PyMuPDF adalah jalur utama untuk PDF yang memiliki text layer.
- OCR hanya menjadi fallback untuk halaman yang tidak mempunyai cukup teks.
- Parser mempertahankan nomor, teks pertanyaan, opsi, dan nomor halaman asal.
- PyMuPDF menentukan batas vertikal setiap soal dan merender crop lossless yang menyertakan teks, rumus, tabel, serta gambar di dalam batas tersebut.
- Parser tidak menentukan jawaban benar, label Bloom, atau difficulty.
- Kandidat tanpa nomor, hasil OCR, dan dokumen gagal dibaca diberi penanda review.
- File upload API diproses di direktori sementara dan dihapus setelah request selesai.

## Entry point

### CLI satu file

```powershell
python -m app.extraction data\raw\pdf\soal.pdf
```

Output default:

```text
data/processed/soal.extracted.json
```

### CLI satu direktori

```powershell
python -m app.extraction data\raw\pdf --output data\processed\pdf-batch.json
```

### API internal

```http
POST /v1/extract
GET  /v1/extraction-info
```

## Bentuk kandidat soal

```json
{
  "candidate_id": "Q-001",
  "question_number": "1",
  "question_text": "Berapakah hasil 2 + 3?",
  "options": [
    {"label": "A", "text": "4"},
    {"label": "B", "text": "5"}
  ],
  "page_numbers": [1],
  "extraction_method": "text_layer",
  "needs_review": false,
  "review_reasons": [],
  "visual_previews": [
    {
      "page_number": 1,
      "mime_type": "image/webp",
      "data_url": "data:image/webp;base64,...",
      "width": 1143,
      "height": 238,
      "crop_method": "question_bounds"
    }
  ]
}
```

## Konfigurasi

Parameter runtime berada di `configs/extraction_config.yaml`:

- `ocr_enabled`: mengaktifkan fallback OCR;
- `ocr_language`: bahasa Tesseract, default `ind+eng`;
- `ocr_dpi`: resolusi render untuk OCR;
- `min_text_characters`: ambang pemilihan text layer atau OCR;
- `max_pdf_pages`: guardrail jumlah halaman per dokumen.
- `question_preview_enabled`: membuat gambar platform per kandidat soal;
- `question_preview_dpi`: resolusi crop visual, default 144 DPI;
- `max_question_previews`: batas gambar agar ukuran respons tetap terkendali.

## Status dan review

- `completed`: ada teks yang berhasil diambil. Ini bukan jaminan teks sudah benar.
- `needs_manual_review`: tidak ada teks atau dokumen tidak dapat diproses.
- `review_required=true`: minimal satu kandidat ambigu atau memakai OCR.
- `confidence=null`: normal untuk text layer dan file terstruktur; confidence hanya berasal dari OCR.
