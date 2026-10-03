"""Generate an evidence-based, per-question Markdown report without API calls.

Run from the repository root:
    python scripts/report_pretest_kelas1.py

This report distinguishes structural checks from semantic validation and never
invents IndoBERT probabilities or Gemini responses when those runs are absent.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.classification.v2.kko import detect_kko  # noqa: E402
from app.ingestion.pretest_import import ImportedOption, equivalent_option_flags  # noqa: E402
from app.services.pretest.agentic.schema import Soal, derive_status  # noqa: E402

SOURCE = ROOT / "output/pretest/kelas1/soal_pretest_db.json"
DESTINATION = ROOT / "output/pretest/kelas1/HASIL_KATEGORISASI_PER_SOAL.md"
ARTIFACT = ROOT / "models/indobert-3x4x3-v1/manifest.json"


def inline(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().replace("|", "\\|").replace("`", "\\`")


def blockquote(value: object) -> str:
    lines = str(value or "").strip().splitlines()
    return "\n".join("> " + line if line.strip() else ">" for line in lines)


def normalized(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().casefold()


def source_matches(item: dict, source_rows: list[tuple[str, dict]]) -> list[tuple[str, dict]]:
    options = item.get("options") or []
    key_text = next(
        (option.get("text") for option in options if option.get("option_id") == item.get("jawaban")),
        "",
    )
    image_names = {
        Path(str(ref)).name.split("pdf-")[-1] for ref in (item.get("image_url") or [])
    }
    matches: list[tuple[str, dict]] = []
    for source_file, source in source_rows:
        source_text = f"{source.get('stimulus') or ''} {source.get('pertanyaan') or ''}"
        if normalized(source_text) != normalized(item.get("soal_text")):
            continue
        if normalized(source.get("jawaban_benar")) != normalized(key_text):
            continue
        source_images = {Path(str(ref)).name.split("pdf-")[-1] for ref in source.get("image_refs") or []}
        if image_names and not image_names.intersection(source_images):
            continue
        matches.append((source_file, source))
    return matches


def inspect_item(item: dict, ordinal: int, source_rows: list[tuple[str, dict]]) -> dict:
    options = item.get("options") or []
    option_labels = [str(option.get("option_id") or "").strip() for option in options]
    key = str(item.get("jawaban") or "").strip()
    source_text = str(item.get("soal_text") or "").strip()
    refs = item.get("image_url") or []
    if isinstance(refs, str):
        refs = [refs]

    issues: list[str] = []
    if not source_text:
        issues.append("stem_kosong")
    if len(options) != 4:
        issues.append("jumlah_opsi_bukan_4")
    if any(not label for label in option_labels) or len(option_labels) != len(set(option_labels)):
        issues.append("label_opsi_kosong_atau_ganda")
    if any(not str(option.get("text") or "").strip() for option in options):
        issues.append("teks_opsi_kosong")
    if option_labels.count(key) != 1:
        issues.append("kunci_tidak_menunjuk_tepat_satu_opsi")
    if str(item.get("soal_type") or "").strip() != "Pilihan Ganda":
        issues.append("tipe_soal_tidak_dikenali")
    issues.extend(
        equivalent_option_flags(
            [ImportedOption(label=label or "?", text=str(option.get("text") or ""))
             for label, option in zip(option_labels, options)]
        )
    )

    missing_refs: list[str] = []
    valid_refs: list[str] = []
    for ref in refs:
        ref_path = (SOURCE.parent / str(ref)).resolve()
        if ref_path.is_relative_to(SOURCE.parent.resolve()) and ref_path.is_file():
            valid_refs.append(str(ref))
        else:
            missing_refs.append(str(ref))
    if missing_refs:
        issues.append("aset_gambar_tidak_ditemukan")

    key_option = next((option for option in options if str(option.get("option_id")) == key), None)
    key_reason = str((key_option or {}).get("alasan") or "").strip()
    if key_option and key_reason.casefold().startswith("salah"):
        issues.append("alasan_opsi_kunci_bertentangan")
    if any(
        str(option.get("alasan") or "").strip().casefold().startswith("benar")
        for option in options if str(option.get("option_id")) != key
    ):
        issues.append("alasan_distraktor_bertentangan")

    matches = source_matches(item, source_rows)
    source_info = None
    if len(matches) == 1:
        source_file, source = matches[0]
        extraction_status, extraction_flags = derive_status(Soal.model_validate(source))
        source_info = {
            "file": source_file,
            "id": source["id"],
            "page": source["source_page"],
            "teacher_page": (source.get("kunci_guru") or {}).get("halaman"),
            "key_status": source["status_kunci"],
            "agent_answer_match": normalized(source["jawaban_agen"]) == normalized(source["jawaban_benar"]),
            "extraction_status": extraction_status,
            "extraction_flags": extraction_flags,
            "agent_difficulty": source.get("tingkat_kesulitan"),
            "agent_difficulty_reason": source.get("alasan_kesulitan"),
        }

    return {
        "number": ordinal,
        "id": str(item.get("_id") or ""),
        "subtopic": str(item.get("subbab_id") or ""),
        "stem": source_text,
        "options": options,
        "key": key,
        "key_text": str((key_option or {}).get("text") or ""),
        "key_reason": key_reason,
        "refs": refs,
        "valid_refs": valid_refs,
        "missing_refs": missing_refs,
        "kko": detect_kko(source_text),
        "issues": issues,
        "structure_ok": not issues,
        "source_info": source_info,
        "source_match_count": len(matches),
    }


def render(records: list[dict], source_digest: str) -> str:
    now = datetime.now(ZoneInfo("Asia/Jakarta")).strftime("%Y-%m-%d %H:%M WIB")
    issue_counts = Counter(issue for record in records for issue in record["issues"])
    structure_ok = sum(record["structure_ok"] for record in records)
    image_items = sum(bool(record["refs"]) for record in records)
    image_refs = sum(len(record["refs"]) for record in records)
    available_refs = sum(len(record["valid_refs"]) for record in records)
    unique_provenance = sum(record["source_info"] is not None for record in records)
    extraction_counts = Counter(
        record["source_info"]["extraction_status"]
        for record in records if record["source_info"] is not None
    )
    body = [
        "# Hasil kategorisasi dan validasi per soal — pretest kelas 1",
        "",
        f"Dibuat: **{now}**. Sumber: [`soal_pretest_db.json`](soal_pretest_db.json) "
        f"(SHA-256 `{source_digest}`). Jumlah: **{len(records)} soal**.",
        "",
        "## Status hasil saat laporan dibuat",
        "",
        "| Tahap | Hasil yang tersedia | Keterangan |",
        "|---|---|---|",
        f"| Pemeriksaan struktur JSON | **{structure_ok}/{len(records)} lulus** | "
        "Stem, 4 opsi, keunikan opsi, kunci, konsistensi alasan dan keberadaan aset |",
        f"| Aset visual | **{image_items} soal** memuat {image_refs} referensi; "
        f"**{available_refs}/{image_refs} file ditemukan** | Keberadaan file belum membuktikan isi gambar atau kecocokannya |",
        f"| Provenance `babNN.json` | **{unique_provenance}/{len(records)} cocok tunggal** | "
        "Match berdasarkan stem, teks jawaban, dan referensi gambar; sisanya ambigu |",
        "| Status ekstraksi sumber | "
        + ", ".join(f"`{name}`: {count}" for name, count in sorted(extraction_counts.items()))
        + " | Status pipeline ekstraksi; belum keputusan AI |",
        "| Validasi konten/kunci/solusi oleh AI | **Belum** | Kunci yang menunjuk opsi belum membuktikan opsi itu benar secara matematika |",
        "| Klasifikasi IndoBERT 3×4×3 | **Belum** | Artefak model terlatih tidak tersedia; `/v2/classify` belum menghasilkan prediksi |",
        "| Confidence IndoBERT | **Belum** | Memerlukan logits model serta suhu kalibrasi yang ditetapkan dari validation silver |",
        "| Gemini silver label / review | **Belum** | Belum ada hasil generasi per soal pada laporan ini |",
        "| CTT / IRT | **Tidak diterapkan** | Belum ada jawaban siswa |",
        "",
        "Tanda **—** pada tabel di bawah berarti hasil belum dihasilkan; itu bukan skor nol atau "
        "prediksi `knowing`. Pemeriksaan struktur tidak memberi silver label. `cognitive_level`, "
        "`cognitive_score`, dan `confidence_score` pada sumber saat ini kosong.",
        "",
        "## Ringkasan masalah format",
        "",
    ]
    if issue_counts:
        body.extend(["| Flag | Jumlah soal |", "|---|---:|"])
        body.extend(f"| `{name}` | {count} |" for name, count in sorted(issue_counts.items()))
    else:
        body.append("Tidak ditemukan masalah format oleh pemeriksaan otomatis. Isi matematika tetap harus direview.")
    body.extend([
        "",
        "## Ringkasan 50 soal",
        "",
        "| No. | ID sumber | Subtopik | Stem singkat | KKO terdeteksi | Kesulitan agen 1–5 | Bukti buku guru | Validasi format | "
        "IndoBERT 3×4×3 | Confidence | Gemini |",
        "|---:|---|---|---|---|---:|---|---|---|---|---|",
    ])
    for record in records:
        preview = inline(record["stem"])
        if len(preview) > 88:
            preview = preview[:85] + "…"
        format_status = "Lulus struktur" if record["structure_ok"] else "Perlu cek: " + ", ".join(record["issues"])
        source = record["source_info"]
        teacher_evidence = (
            f"{source['key_status']}, guru hlm. {source['teacher_page']}"
            if source and source["teacher_page"] else
            (source["key_status"] if source else "match sumber ambigu")
        )
        body.append(
            f"| {record['number']} | `{record['id']}` | {inline(record['subtopic'])} | "
            f"{preview} | {', '.join(record['kko']) or '—'} | "
            f"{source['agent_difficulty'] if source else '—'} | {teacher_evidence} | {inline(format_status)} | "
            "— | — | — |"
        )
    body.extend([
        "",
        "## Detail tiap soal",
        "",
        "Pada setiap kartu, status `perlu review isi` berarti seseorang masih harus memeriksa "
        "ketepatan kunci, kecukupan stimulus, makna gambar, dan solusi minimum. Semua model tetap "
        "berstatus advisory sampai ada anotasi manusia.",
        "",
    ])
    for record in records:
        source = record["source_info"]
        body.extend([
            f"### {record['number']:02d}. `{record['id']}`",
            "",
            f"Subtopik: {inline(record['subtopic']) or '—'} · tipe: pilihan ganda · kelas: 1.",
            "",
            blockquote(record["stem"]),
            "",
            "| Opsi | Isi | Catatan sumber |",
            "|---|---|---|",
        ])
        for option in record["options"]:
            body.append(
                f"| {inline(option.get('option_id'))} | {inline(option.get('text'))} | "
                f"{inline(option.get('alasan'))} |"
            )
        body.extend([
            "",
            f"- Kunci pada file: **{inline(record['key'])} — {inline(record['key_text'])}**. "
            "Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.",
            (f"- Provenance: `{source['file']}` / `{source['id']}`; siswa hlm. "
             f"{source['page']}, guru hlm. {source['teacher_page'] or '—'}; "
             f"status kunci sumber `{source['key_status']}`, status ekstraksi "
             f"`{source['extraction_status']}`, jawaban agen "
             f"{'cocok' if source['agent_answer_match'] else 'berbeda'}. "
             "Ini bukti ekstraksi, belum verifikasi AI."
             if source else
             f"- Provenance: {record['source_match_count']} kandidat dari `babNN.json`; "
             "asal tunggal belum dapat dipastikan dari file ringkasan ini."),
            (f"- Perkiraan kesulitan agen ekstraksi: **{source['agent_difficulty']}/5**; "
             f"alasan sumber: {inline(source['agent_difficulty_reason']) or '—'}. "
             "Skor ini berbeda dari head `intendedDifficulty` IndoBERT."
             if source else "- Perkiraan kesulitan agen ekstraksi: — (provenance ambigu)."),
            (f"- Flag ekstraksi: {', '.join('`' + flag + '`' for flag in source['extraction_flags']) or 'tidak ada'}."
             if source else "- Flag ekstraksi: — (provenance ambigu)."),
            f"- Validasi struktur: **{'lulus' if record['structure_ok'] else 'perlu koreksi'}**"
            f"; flag: {', '.join('`' + issue + '`' for issue in record['issues']) or 'tidak ada'}.",
            f"- Gambar: {len(record['valid_refs'])}/{len(record['refs'])} file tersedia"
            + ("; " + ", ".join(f"`{inline(ref)}`" for ref in record["refs"]) if record["refs"] else "; tidak ada referensi")
            + ". Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.",
            f"- KKO terdeteksi: **{', '.join(record['kko']) or 'tidak terdeteksi'}**. "
            "KKO hanya fitur teks; tidak menentukan head kognitif.",
            "- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.",
            "- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, "
            "`intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` "
            "(artefak terlatih belum ada).",
            "- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` "
            "untuk laporan ini (belum dipanggil).",
            "",
        ])
    body.extend([
        "## Cara IndoBERT akan bekerja setelah artefak tersedia",
        "",
        "1. Import sumber sebagai versi konten tetap. `kelas_id` yang kosong diisi sebagai kelas 1 "
        "berdasarkan lokasi dataset, dengan provenance inferensi tersebut. Stem, opsi, kunci, "
        "dan gambar diberi `contentHash`. Revisi soal membuat versi baru.",
        "2. Periksa format, isi, kunci, dan gambar. `jawaban` hanyalah kunci opsi, bukan "
        "`verifiedMinimalSolution`. Banyak soal visual tidak dapat dinilai aman dari teks saja.",
        "3. Serialisasi input menjadi `Kelas`, `Topik/Subtopik`, `Tipe`, `Stimulus`, "
        "`Soal`, `Pilihan`, `Solusi minimum terverifikasi` jika tersedia, `KKO`, dan "
        "transkripsi visual terverifikasi. Jangan mengarang field yang belum ada.",
        "4. Tokenizer IndoBERT memecah teks ke token, memakai truncation maksimum yang tercatat "
        "pada manifest, lalu shared encoder menghasilkan representasi. Tiga head menghasilkan "
        "masing-masing 3, 4, dan 3 logits.",
        "5. Probabilitas per head dihitung `softmax(logits / temperature_head)`. Label tertinggi "
        "dan probabilitasnya menjadi `calibratedConfidence`. Normalized entropy, truncation, "
        "scope, dan provenance menentukan `predict`, `review`, atau `abstain`.",
        "6. Temperature dan threshold harus dipilih pada validation set silver AI. Tanpa silver, "
        "angka probabilitas model bootstrap tidak boleh disebut terkalibrasi atau akurasi ilmiah.",
        "",
        "Parameter yang dipakai model: tugas matematika yang benar-benar diminta, struktur "
        "operasi, konsep, langkah solusi, hubungan representasi, kelas dan subtopik, opsi, "
        "beban visual, serta KKO sebagai sinyal lemah. Label head 1: `knowing/applying/reasoning`; "
        "head 2: `factual/conceptual/procedural/metacognitive`; head 3: `Easy/Medium/Hard` "
        "sebagai kesulitan yang dimaksud oleh isi soal.",
        "",
        "## Cara Gemini akan bekerja",
        "",
        "1. Untuk bootstrap tanpa silver, Gemini dapat mengusulkan tiga label sebagai **silver** "
        "melalui prompt dan structured JSON. Output menyertakan bukti singkat, alasan dan "
        "`abstain` bila soal tidak cukup jelas.",
        "2. Jika N=3 diaktifkan, tiga run model dan konfigurasi yang sama dikumpulkan. "
        "3 sama → konsisten; 2 sama → mayoritas dengan dissent; 1–1–1 atau abstain "
        "tanpa mayoritas → antrean review. N=3 mengukur kestabilan Gemini, bukan voting AI.",
        "3. Setelah IndoBERT benar-benar ada, reviewer Gemini dapat melihat item, prediksi, "
        "probabilitas per head dan rubrik; keluarannya `confirm/revise/abstain` per head. "
        "Runtime reviewer yang ada tidak dapat menghasilkan hasil ini ketika prediksi "
        "IndoBERT belum tersedia.",
        "4. Simpan ID model, versi prompt/rubrik, hash input, response ID, latency, "
        "token usage, tiga hasil mentah yang sudah divalidasi, dan keputusan agregat. "
        "Jangan menyimpan atau menampilkan API key maupun chain-of-thought.",
        "",
        "Gemini yang membentuk silver dan kemudian mereview IndoBERT memberi dua hasil "
        "yang tidak independen. Agreement keduanya dapat dipakai untuk diagnosis pipeline, "
        "bukan sebagai bukti silver atau kualitas model.",
        "",
        "## Batas dan langkah berikutnya",
        "",
        "- Semua 50 item memerlukan verifikasi konten dan kunci. Prioritaskan item visual "
        "serta stem yang masih merujuk gambar. File gambar tersedia, tetapi isi gambarnya "
        "belum diperiksa dalam audit ini.",
        "- Untuk menjalankan klasifikasi IndoBERT, perlu silver dataset yang diberi "
        "provenance jelas, training, kalibrasi yang layak, dan artefak manifest terverifikasi. "
        "Laporan ini belum memuat angka model karena artefak tidak tersedia.",
        "- Panggilan Gemini memerlukan konfigurasi live dan akan memakai kuota. "
        "Laporan ini dihasilkan offline dan tidak mengirim soal atau key ke penyedia.",
        "- Proses berhenti pada paket review manusia. CTT, discrimination index, dan IRT "
        "tidak dapat dihitung tanpa data jawaban siswa dan tidak dikerjakan di sini.",
        "",
    ])
    return "\n".join(body)


def main() -> None:
    source_bytes = SOURCE.read_bytes()
    items = json.loads(source_bytes)
    if not isinstance(items, list):
        raise ValueError("expected a list of questions")
    source_rows = [
        (path.name, source)
        for path in sorted(SOURCE.parent.glob("bab[0-9][0-9].json"))
        for source in json.loads(path.read_text(encoding="utf-8"))["soal"]
    ]
    records = [inspect_item(item, index, source_rows) for index, item in enumerate(items, start=1)]
    digest = hashlib.sha256(source_bytes).hexdigest()
    DESTINATION.write_text(render(records, digest), encoding="utf-8")
    print(f"report={DESTINATION.relative_to(ROOT)}")
    print(f"questions={len(records)}")
    print(f"structure_pass={sum(record['structure_ok'] for record in records)}")
    print(f"image_refs={sum(len(record['refs']) for record in records)}")
    print(f"missing_image_refs={sum(len(record['missing_refs']) for record in records)}")
    print(f"unique_provenance={sum(record['source_info'] is not None for record in records)}")
    print(f"indobert_artifact_present={ARTIFACT.is_file()}")
    print("gemini_generation_calls=0")


if __name__ == "__main__":
    main()
