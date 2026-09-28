"""
review_app.py -- halaman web sederhana (FastAPI) untuk REVIEW MANUAL hasil
Tahap 1 + Tahap 2 (file JSON di folder output/ atau output_mcq/), supaya
tidak perlu baca JSON mentah satu-satu.

PENTING: tool ini HANYA BACA file JSON lokal di komputer kamu -- TIDAK
menyentuh MongoDB, TIDAK mengubah data, dan TIDAK terhubung ke aplikasi
FastAPI utama punya tim (main.py). Ini murni alat bantu QA manual buat
kamu sendiri, jalan terpisah.

Cara pakai (dari root project ai_services_lms, venv aktif):
    pip install fastapi uvicorn jinja2   # kalau belum ada
    uvicorn scripts.review_app:app --reload --port 8010

Lalu buka http://127.0.0.1:8010 di browser.

Fitur:
- Pilih file JSON (otomatis di-scan dari folder "output/" dan "output_mcq/")
- Filter berdasarkan status (draft, mcq_generated, pending_mcq_conversion, dst)
- Filter khusus "butuh review prioritas" -- item yang correct_answer atau
  distractor-nya berasal dari LLM (flag *_by_llm), karena itu yang paling
  perlu dicek manual dulu (lihat diskusi kita soal item yang lolos verifikasi
  verbatim tapi ternyata salah secara makna).
- Highlight visual untuk flag *_by_llm supaya gampang dipindai matanya.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

app = FastAPI(title="Review Tool -- Pretest MCQ (lokal, read-only)")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SEARCH_DIRS = [PROJECT_ROOT / "output", PROJECT_ROOT / "output_mcq"]
# Urutan prioritas file default: stage2 (hasil akhir) > stage1b (sudah
# digabung Buku Siswa) > stage1 (mentah).

STATUS_COLORS = {
    "mcq_generated": "#1a7f37",
    "pending_mcq_conversion": "#9a6700",
    "needs_review_extraction": "#b35900",
    "needs_image": "#6639ba",
    "skipped_open_ended": "#57606a",
    "skipped_pembuktian": "#57606a",
    "draft": "#57606a",
    "needs_review_missing_soal": "#cf222e",
    "needs_review_soal_match": "#bc4c00",
    "needs_review_answer": "#a40e26",
    "needs_review_soal_source": "#8250df",
    "needs_review_soal_format": "#8250df",
    "needs_review_no_answer_key": "#57606a",
}

LLM_FLAG_PREFIXES = ("answer_extracted_by_llm", "distractors_generated_by_llm")
# Flag hasil soal_merger.py / pengecekan jawaban yang perlu mata manusia.
REVIEW_FLAGS = ("soal_match_ambiguous", "soal_text_weak", "soal_count_mismatch",
                "soal_fewer_than_answers", "ordinal_count_mismatch", "soal_boundary_suspect",
                "answer_is_label_list", "answer_restates_soal", "answer_is_teacher_note",
                "answer_empty", "soal_only_in_guru_text")


def _find_json_files() -> list[Path]:
    """
    Cari semua file JSON di folder output/ dan output_mcq/, diurutkan supaya
    file hasil AKHIR (mengandung "stage2" di namanya -- output dari
    answer_option_generator.py) muncul PALING ATAS/terpilih duluan, bukan
    file "stage1" (hasil mentah extractor_text.py, belum ada correct_answer/
    options sama sekali). Ditemukan langsung dari testing manual: tanpa ini,
    file stage1 kepilih default karena urutan alfabet ("stage1" < "stage2"),
    bikin bingung seolah-olah hasil MCQ-nya kosong padahal cuma salah lihat
    file. Di dalam grup yang sama, file terbaru (mtime) ditaruh duluan.
    """
    files: list[Path] = []
    for d in SEARCH_DIRS:
        if d.is_dir():
            files.extend(d.glob("*.json"))
    def rank(f: Path) -> int:
        n = f.name.lower()
        return 0 if "stage2" in n else 1 if "stage1b" in n else 2
    files.sort(key=lambda f: (rank(f), -f.stat().st_mtime))
    return files


def _guru_cell(it: dict) -> str:
    """Kolom kunci jawaban dari Buku Guru + asal kuncinya (file, halaman,
    section, nomor). Soal selalu dari Buku Siswa (kolom Teks Soal)."""
    import html

    guru = it.get("jawaban_text_guru")
    if not guru:
        return '<span class="meta">kunci tidak ditemukan di Buku Guru</span>'
    src = it.get("kunci_source") or {}
    meta = (f'<div class="meta">kunci dari: {html.escape(str(src.get("file") or ""))} &middot; '
            f'hal {src.get("page")} &middot; {html.escape(str(src.get("activity") or src.get("section") or ""))} '
            f'no {src.get("item_no")} &middot; {it.get("soal_match_method")} &middot; conf {it.get("soal_match_confidence")}</div>')
    return html.escape(guru[:500]) + meta


def _load_items(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        payload = json.load(f)
    return payload.get("items", [])


def _page_shell(body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>Review Tool -- Pretest MCQ</title>
<style>
  body {{ font-family: -apple-system, Segoe UI, Arial, sans-serif; margin: 0; padding: 24px;
          background: #f6f8fa; color: #1f2328; }}
  h1 {{ font-size: 20px; margin-bottom: 4px; }}
  .subtitle {{ color: #57606a; font-size: 13px; margin-bottom: 20px; }}
  .toolbar {{ margin-bottom: 16px; display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
  select, a.btn {{ padding: 6px 10px; border-radius: 6px; border: 1px solid #d0d7de; background: white;
                    font-size: 13px; text-decoration: none; color: #1f2328; }}
  a.btn.active {{ background: #0969da; color: white; border-color: #0969da; }}
  table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden;
           box-shadow: 0 1px 2px rgba(0,0,0,0.05); }}
  th, td {{ text-align: left; padding: 10px 12px; border-bottom: 1px solid #eaeef2; font-size: 13px;
            vertical-align: top; }}
  th {{ background: #f6f8fa; font-weight: 600; position: sticky; top: 0; }}
  tr.llm-flagged {{ background: #fff8f0; }}
  .status-pill {{ display: inline-block; padding: 2px 8px; border-radius: 999px; color: white;
                   font-size: 11px; font-weight: 600; white-space: nowrap; }}
  .flags {{ font-size: 11px; color: #57606a; }}
  .flag-llm {{ color: #b35900; font-weight: 600; }}
  .qtext {{ white-space: pre-wrap; max-width: 380px; font-size: 12.5px; }}
  .options {{ font-size: 12px; }}
  .options .correct {{ color: #1a7f37; font-weight: 600; }}
  .meta {{ font-size: 11px; color: #8c959f; }}
  .empty {{ padding: 40px; text-align: center; color: #57606a; }}
</style>
</head>
<body>
{body}
</body>
</html>"""


@app.get("/", response_class=HTMLResponse)
def index(
    file: Optional[str] = Query(default=None),
    status: Optional[str] = Query(default=None),
    only_llm: bool = Query(default=False),
):
    files = _find_json_files()
    if not files:
        return _page_shell(
            "<h1>Review Tool</h1><div class='empty'>Tidak ada file JSON ditemukan di folder "
            "<code>output/</code> atau <code>output_mcq/</code>. Jalankan dulu extractor_text.py / "
            "answer_option_generator.py, atau test_batch_mcq_generation.py.</div>"
        )

    selected_path = None
    if file:
        for f in files:
            if f.name == file:
                selected_path = f
                break
    if selected_path is None:
        selected_path = files[0]

    items = _load_items(selected_path)

    all_statuses = sorted({it.get("status", "?") for it in items})
    status_counts = {s: sum(1 for it in items if it.get("status") == s) for s in all_statuses}
    llm_count = sum(
        1 for it in items if any(
            f in it.get("extraction_flags", []) for f in LLM_FLAG_PREFIXES
        )
    )

    filtered = items
    if status:
        filtered = [it for it in filtered if it.get("status") == status]
    if only_llm:
        filtered = [
            it for it in filtered
            if any(f in it.get("extraction_flags", []) for f in LLM_FLAG_PREFIXES)
        ]

    file_options = "".join(
        f'<option value="{f.name}" {"selected" if f == selected_path else ""}>{f.name}</option>'
        for f in files
    )

    status_links = " ".join(
        f'<a class="btn {"active" if status == s else ""}" '
        f'href="/?file={selected_path.name}&status={s}{"&only_llm=1" if only_llm else ""}">'
        f'{s} ({status_counts[s]})</a>'
        for s in all_statuses
    )
    clear_link = f'<a class="btn {"active" if not status else ""}" href="/?file={selected_path.name}{"&only_llm=1" if only_llm else ""}">semua ({len(items)})</a>'
    llm_link = (
        f'<a class="btn {"active" if only_llm else ""}" '
        f'href="/?file={selected_path.name}{"&status=" + status if status else ""}&only_llm={"0" if only_llm else "1"}">'
        f"⚠ hanya via LLM ({llm_count})</a>"
    )

    rows = []
    for it in filtered:
        s = it.get("status", "?")
        color = STATUS_COLORS.get(s, "#57606a")
        flags = it.get("extraction_flags", []) or []
        flags_html = " ".join(
            f'<span class="{"flag-llm" if (fl in LLM_FLAG_PREFIXES or fl in REVIEW_FLAGS) else ""}">{fl}</span>'
            for fl in flags
        )
        is_llm = any(fl in LLM_FLAG_PREFIXES for fl in flags)

        options_html = ""
        opts = it.get("options") or []
        correct = it.get("correct_answer")
        if opts:
            options_html = "<br>".join(
                f'<span class="{"correct" if o["text"] == correct else ""}">'
                f'{o["option_id"]}. {o["text"]}</span>'
                for o in opts
            )
        elif correct:
            options_html = f"<em>correct_answer (belum ada opsi):</em> {correct}"

        rows.append(f"""
        <tr class="{'llm-flagged' if is_llm else ''}">
          <td class="meta">{it.get('source_file') or ''}<br>hal {it.get('source_page')} &middot; {it.get('source_section') or ''} no {it.get('source_item_no')}<br>{it.get('source_bab') or it.get('source_subbab') or ''}</td>
          <td class="qtext">{(it.get('pertanyaan_text') or '')[:500]}</td>
          <td class="qtext">{_guru_cell(it)}</td>
          <td><span class="status-pill" style="background:{color}">{s}</span></td>
          <td class="options">{options_html}</td>
          <td class="flags">{flags_html}</td>
        </tr>""")

    body = f"""
    <h1>Review Tool -- Pretest MCQ</h1>
    <div class="subtitle">Read-only, baca file JSON lokal saja. Tidak menyentuh MongoDB.</div>
    <div class="toolbar">
      <form method="get" style="display:flex; gap:8px; align-items:center;">
        <select name="file" onchange="this.form.submit()">{file_options}</select>
      </form>
      {clear_link} {status_links} {llm_link}
    </div>
    <div class="meta" style="margin-bottom:10px;">
      Menampilkan {len(filtered)} dari {len(items)} item -- file: <code>{selected_path.name}</code>
    </div>
    <table>
      <tr><th>Sumber</th><th>Teks Soal</th><th>Kunci Jawaban (Buku Guru)</th><th>Status</th><th>Opsi / Jawaban</th><th>Flags</th></tr>
      {''.join(rows) if rows else '<tr><td colspan="6" class="empty">Tidak ada item untuk filter ini.</td></tr>'}
    </table>
    """
    return _page_shell(body)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8010)
