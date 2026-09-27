"""Build the editable, large-format SVG for architecture documents 15 and 16."""

from pathlib import Path
from xml.sax.saxutils import escape


WIDTH = 4000
HEIGHT = 8500
OUT = Path(__file__).resolve().parents[1] / "API_DOCUMENTATION" / "18_END_TO_END_AI_PSYCHOMETRIC_VARIATION_ARCHITECTURE.svg"

COLORS = {
    "ink": "#14243A",
    "muted": "#506279",
    "line": "#6B8099",
    "blue": "#2774B8",
    "teal": "#138A80",
    "violet": "#7256B5",
    "amber": "#BA7719",
    "red": "#C94F5D",
    "green": "#23815B",
    "paper": "#F7FAFE",
}

lines = []
nodes = []


def marker(color):
    return {
        COLORS["line"]: "arrow-gray",
        COLORS["blue"]: "arrow-blue",
        COLORS["teal"]: "arrow-teal",
        COLORS["violet"]: "arrow-violet",
        COLORS["amber"]: "arrow-amber",
        COLORS["red"]: "arrow-red",
        COLORS["green"]: "arrow-green",
    }[color]


def path(points, color="line", dashed=False, width=4, arrow=True):
    color = COLORS.get(color, color)
    coords = " ".join(("M" if i == 0 else "L") + f" {x} {y}" for i, (x, y) in enumerate(points))
    extra = f' marker-end="url(#{marker(color)})"' if arrow else ""
    dash = ' stroke-dasharray="12 10"' if dashed else ""
    lines.append(f'<path d="{coords}" fill="none" stroke="{color}" stroke-width="{width}" '
                 f'stroke-linecap="round" stroke-linejoin="round"{dash}{extra}/>' )


def label(x, y, value, color="muted", size=23, anchor="middle", rotate=None):
    transform = f' transform="rotate({rotate} {x} {y})"' if rotate else ""
    nodes.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" '
                 f'font-weight="700" fill="{COLORS.get(color, color)}"{transform}>{escape(value)}</text>')


def section(y, number, title, subtitle, accent):
    c = COLORS[accent]
    nodes.append(f'<rect x="85" y="{y}" width="1765" height="100" rx="22" fill="{c}"/>')
    nodes.append(f'<text x="125" y="{y+43}" font-size="33" font-weight="800" fill="#FFFFFF">'
                 f'{escape(number)}  {escape(title)}</text>')
    nodes.append(f'<text x="125" y="{y+77}" font-size="21" fill="#EAF3FF">{escape(subtitle)}</text>')


def card(x, y, w, h, title, body=(), tech="", accent="blue", fill="#FFFFFF", title_size=31,
         body_size=23, kind="process"):
    c = COLORS[accent]
    if kind == "status":
        fill = {
            "red": "#FFF1F2", "green": "#ECF8F1", "amber": "#FFF6E8",
            "violet": "#F4F0FB", "blue": "#EEF6FD", "teal": "#EAF8F6",
        }[accent]
    nodes.append(f'<g class="card"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" '
                 f'fill="{fill}" stroke="{c}" stroke-width="3"/>')
    nodes.append(f'<rect x="{x}" y="{y}" width="12" height="{h}" rx="6" fill="{c}"/>')
    tx = x + 36
    nodes.append(f'<text x="{tx}" y="{y+44}" font-size="{title_size}" font-weight="800" '
                 f'fill="{COLORS["ink"]}">{escape(title)}</text>')
    for idx, line in enumerate(body):
        nodes.append(f'<text x="{tx}" y="{y+83+idx*32}" font-size="{body_size}" '
                     f'fill="{COLORS["muted"]}">{escape(line)}</text>')
    if tech:
        nodes.append(f'<text x="{tx}" y="{y+h-22}" font-size="20" font-weight="700" '
                     f'fill="{c}">{escape(tech)}</text>')
    nodes.append('</g>')


def decision(x, y, w, h, title, body=(), accent="amber"):
    c = COLORS[accent]
    nodes.append(f'<polygon points="{x+w/2},{y} {x+w},{y+h/2} {x+w/2},{y+h} {x},{y+h/2}" '
                 f'fill="#FFFFFF" stroke="{c}" stroke-width="3"/>')
    nodes.append(f'<text x="{x+w/2}" y="{y+h/2-4}" text-anchor="middle" font-size="27" '
                 f'font-weight="800" fill="{COLORS["ink"]}">{escape(title)}</text>')
    for idx, line in enumerate(body):
        nodes.append(f'<text x="{x+w/2}" y="{y+h/2+29+idx*27}" text-anchor="middle" '
                     f'font-size="21" fill="{COLORS["muted"]}">{escape(line)}</text>')


# Draw connectors before nodes, keeping routes behind the content.
# Ingest and verify a parent question.
path([(675, 630), (675, 675), (2000, 675)], "blue", arrow=False)
path([(2000, 630), (2000, 715)], "blue")
path([(3325, 630), (3325, 675), (2000, 675)], "blue", arrow=False)
path([(2000, 885), (2000, 975)], "blue")
path([(2000, 1130), (2000, 1165)], "blue", arrow=False)
path([(550, 1165), (3450, 1165)], "blue", arrow=False)
for cx in (550, 1510, 2470, 3430):
    path([(cx, 1165), (cx, 1205)], "blue")
for cx in (550, 1510, 2470, 3430):
    path([(cx, 1375), (cx, 1430)], "blue", arrow=False)
path([(550, 1430), (3430, 1430)], "blue", arrow=False)
path([(2000, 1430), (2000, 1475)], "blue")
path([(1350, 1550), (1130, 1550)], "amber")
path([(2650, 1550), (2840, 1550)], "red")
path([(590, 1475), (590, 1025), (1275, 1025)], "amber", dashed=True)
path([(2000, 1625), (2000, 1735)], "blue")
path([(2000, 1890), (2000, 1975)], "blue")
path([(1350, 2055), (1130, 2055)], "amber")
path([(2650, 2055), (2840, 2055)], "red")
path([(590, 1975), (590, 1810), (1345, 1810)], "amber", dashed=True)
path([(2000, 2130), (2000, 2205)], "blue")
path([(2650, 2285), (2840, 2285)], "red")
path([(2000, 2370), (2000, 2460)], "blue")

# Independent taxonomy classifiers, agreement and finite arbitration.
path([(2000, 2535), (2000, 2570)], "violet", arrow=False)
path([(970, 2570), (3030, 2570)], "violet", arrow=False)
path([(970, 2570), (970, 2600)], "violet")
path([(3030, 2570), (3030, 2600)], "violet")
path([(970, 2845), (970, 2895)], "violet", arrow=False)
path([(3030, 2845), (3030, 2895)], "violet", arrow=False)
path([(970, 2895), (3030, 2895)], "violet", arrow=False)
path([(2000, 2895), (2000, 2950)], "violet")
path([(1250, 3040), (1170, 3040)], "red")
path([(2750, 3040), (2830, 3040)], "amber")
path([(3350, 2950), (3350, 2875), (2550, 2875), (2550, 2945)], "amber", dashed=True)
path([(2000, 3130), (2000, 3200)], "green")
path([(2000, 3360), (2000, 3400)], "green", arrow=False)
path([(950, 3400), (3050, 3400)], "green", arrow=False)
path([(950, 3400), (950, 3430)], "green")
path([(3050, 3400), (3050, 3430)], "green")

# Verified parent feeds the item-model generator; parent can also be piloted directly.
path([(950, 3580), (950, 3610), (2000, 3610), (2000, 3780)], "teal")
path([(3050, 3580), (3050, 3640), (3920, 3640), (3920, 6015), (2755, 6015)], "green")
path([(2000, 3960), (2000, 4000)], "teal", arrow=False)
path([(1010, 4000), (2990, 4000)], "teal", arrow=False)
path([(1010, 4000), (1010, 4110)], "teal")
path([(2990, 4000), (2990, 4110)], "teal")
path([(1010, 4340), (1010, 4410)], "teal", arrow=False)
path([(2990, 4340), (2990, 4410)], "teal", arrow=False)
path([(1010, 4410), (2990, 4410)], "teal", arrow=False)
path([(2000, 4410), (2000, 4450)], "teal")
path([(2000, 4600), (2000, 4650), (1050, 4650), (1050, 4710)], "teal")
path([(1800, 4795), (2200, 4795)], "teal")
path([(2950, 4880), (2950, 4920), (2000, 4920), (2000, 5010)], "teal")
path([(1250, 5095), (1110, 5095)], "amber")
path([(2750, 5095), (2840, 5095)], "red")
path([(590, 5010), (590, 4590), (1270, 4590)], "amber", dashed=True)
path([(2000, 5190), (2000, 5300)], "teal")
path([(2750, 5385), (2840, 5385)], "red")
path([(2000, 5475), (2000, 5570)], "green")
path([(2000, 5730), (2000, 5930)], "green")

# Shared delivery and empirical assessment.
path([(2000, 6090), (2000, 6200)], "green")
path([(2000, 6370), (2000, 6460)], "green")
path([(2000, 6630), (2000, 6730)], "green")
path([(2000, 6910), (2000, 6970)], "green", arrow=False)
path([(730, 6970), (3270, 6970)], "green", arrow=False)
for cx in (730, 2000, 3270):
    path([(cx, 6970), (cx, 7030)], "green")
path([(2000, 7200), (2000, 7290)], "violet", arrow=False)
path([(1020, 7290), (2980, 7290)], "violet", arrow=False)
path([(1020, 7290), (1020, 7410)], "violet")
path([(2980, 7290), (2980, 7410)], "teal")
path([(130, 7115), (100, 7115), (100, 6280), (1245, 6280)], "amber", dashed=True)
path([(3270, 7200), (3270, 7370), (3180, 7370), (3180, 7405)], "teal", dashed=True)
# Outside-rail feedback makes the two learning loops unambiguous.
path([(170, 7570), (45, 7570), (45, 2730), (165, 2730)], "violet", dashed=True, width=5)
path([(3830, 7570), (3950, 7570), (3950, 3860), (2755, 3860)], "teal", dashed=True, width=5)

# Header and section labels.
nodes.append('<rect x="0" y="0" width="4000" height="285" fill="#112844"/>')
nodes.append('<text x="100" y="89" font-size="59" font-weight="900" fill="#FFFFFF">'
             'ARSITEKTUR END-TO-END SOAL CERDAS &amp; VARIASI TERKENDALI</text>')
nodes.append('<text x="100" y="143" font-size="28" fill="#D6E7F8">'
             'Gabungan dokumen 15 + 16 · dari authoring hingga perbaikan model dan generator berbasis bukti respons</text>')
nodes.append('<text x="100" y="207" font-size="23" fill="#B9D2EB">'
             'Alur utama: garis penuh  |  Loop iteratif: garis putus-putus  |  Status gagal/karantina: merah  |  Keputusan otomatis: tanpa reviewer manual</text>')
section(305, "01", "INGEST, EKSTRAKSI & VERIFIKASI SOAL INDUK", "Teacher adalah author; seluruh gate setelah submit berjalan otomatis.", "blue")
section(2435, "02", "KLASIFIKASI INDEPENDEN & KONSENSUS AI", "Tiga head taksonomi dinilai terpisah; konflik diproses dengan arbitration terbatas.", "violet")
section(3635, "03", "ITEM MODEL & GENERASI VARIASI TERKENDALI", "Varian memakai invariant konstruk, constraint, seed, jawaban hitung ulang, dan screening baru.", "teal")
section(5810, "04", "PROVISIONAL BANK, DELIVERY & PSIKOMETRIK", "Induk dan varian hanya dipilotkan setelah gate; metrik selalu terkait versi dan populasi.", "green")
section(7275, "05", "DUA LOOP SELF-IMPROVEMENT", "Bukti empiris memperbaiki model prediksi dan kebijakan generator melalui versi baru.", "violet")

# Section 01.
card(100, 455, 1150, 175, "SUMBER SOAL", ["PDF / gambar / JSON / CSV / TXT / TEX", "Manual, upload, object storage, external API"], "MinIO / S3-compatible · file provenance", "blue")
card(1425, 455, 1150, 175, "AUTHORING TEACHER", ["Buat / koreksi draft dan submit", "Revisi membuat content_version baru"], "Teacher ≠ reviewer / adjudicator", "blue")
card(2750, 455, 1150, 175, "REQUEST & SOURCE SNAPSHOT", ["Request ID, checksum, ownership, metadata", "Berkas mentah dan preview tetap terlacak"], "MongoDB · object store", "blue")
card(1275, 715, 1450, 170, "API GATEWAY & SECURITY GATE", ["Schema, MIME, ukuran, checksum, duplikat", "Job asinkron setelah lolos request gate"], "Node.js · Express · Multer · AJV · Redis/Celery", "blue")
card(1275, 975, 1450, 155, "DOCUMENT EXTRACTION ROUTER", ["Jalur dipilih menurut jenis file dan wilayah rumus"], "Python · FastAPI · worker queue", "blue")
card(100, 1205, 900, 170, "PDF BERTEKS", ["Ambil text layer dan posisi teks"], "PyMuPDF", "blue", title_size=29)
card(1060, 1205, 900, 170, "SCAN / GAMBAR", ["Render halaman, OCR ind+eng"], "Pillow · Tesseract", "blue", title_size=29)
card(2020, 1205, 900, 170, "REGION RUMUS", ["Layout, formula → LaTeX"], "PaddleOCR · PP-DocLayout · FormulaNet", "blue", title_size=29)
card(2980, 1205, 900, 170, "DATA TERSTRUKTUR", ["Parse JSON / CSV / TXT / TEX"], "Structured parser", "blue", title_size=29)
card(130, 1475, 1000, 150, "RECOVERY TERBATAS", ["DPI ↑, OCR alternatif, segmentasi ulang"], "Retry ≤ Rmax", "amber", kind="status", title_size=28)
card(1350, 1475, 1300, 150, "EXTRACTION QUALITY GATE", ["Confidence, kelengkapan opsi, render rumus"], "Auto-retry bila dapat dipulihkan", "blue")
card(2840, 1475, 1030, 150, "KARANTINA EKSTRAKSI", ["Retry habis / teks tidak andal"], "quarantine_extraction", "red", kind="status", title_size=28)
card(1350, 1735, 1300, 155, "CANONICAL QUESTION BUILDER", ["NFKC, opsi, LaTeX, ID, provenance"], "Pydantic · versioned content", "blue")
card(130, 1975, 1000, 155, "SAFE AUTO-REPAIR", ["Hanya format, label opsi, whitespace"], "Validasi ulang", "amber", kind="status", title_size=28)
card(1350, 1975, 1300, 155, "DETERMINISTIC VALIDATION", ["Schema, range, kunci di opsi, duplikat, LaTeX"], "AJV · Pydantic · Mongoose · content hash", "blue")
card(2840, 1975, 1030, 155, "REJECT / REVISION", ["Invalid non-repairable; author revisi versi"], "rejected_invalid", "red", kind="status", title_size=28)
card(1350, 2205, 1300, 165, "ANSWER VERIFICATION", ["SymPy / rules; solver LLM independen bila perlu", "Kunci harus stabil dan konsisten"], "SymPy · rule verifier · LLM solver fallback", "blue")
card(2840, 2205, 1030, 165, "KONFLIK JAWABAN", ["Kunci hilang / solver tidak sepakat"], "quarantine_answer_conflict", "red", kind="status", title_size=28)

# Section 02.
card(170, 2600, 1600, 245, "INDOBERT MULTI-HEAD", ["Bloom 6 · knowledge 4 · intended difficulty 3", "Probabilitas, entropy/head, top-two margin, OOD", "Cold start: weak labels LLM+rules → train v0"], "IndoBERT · PyTorch · Hugging Face", "violet")
card(2230, 2600, 1600, 245, "LLM TAXONOMY ENSEMBLE", ["Rubric berversi + retrieval contoh", "N sampling, voting/head, evidence, abstention", "Tidak melihat prediksi IndoBERT saat screening"], "LLM adapter · JSON Schema · FAISS", "violet")
card(170, 2950, 1000, 180, "KARANTINA AI", ["OOD, warning kritis, konflik menetap"], "quarantine_ai_conflict", "red", kind="status", title_size=29)
card(1250, 2950, 1500, 180, "AGREEMENT & COMPOSITE RISK", ["Seluruh head harus sepakat; answer passed", "Entropy, margin, SC, evidence, OOD, extraction risk"], "Threshold dikalibrasi; bukan angka universal", "violet")
card(2830, 2950, 1000, 180, "ARBITRATION TERBATAS", ["Prompt/model lain; retry ≤ Amax", "Hasil kembali ke risk gate"], "Automated · auditable", "amber", kind="status", title_size=29)
card(1250, 3200, 1500, 160, "AI CONSENSUS + PROVENANCE", ["Keputusan otomatis, model/rubric/prompt/version tersimpan"], "MongoDB · JSONL/Parquet snapshot", "green", kind="status")
card(300, 3430, 1300, 150, "VERIFIED PARENT ITEM", ["Struktur, jawaban, taksonomi, tujuan stabil"], "Sumber item model", "green", kind="status")
card(2400, 3430, 1300, 150, "INDUK → PROVISIONAL", ["Dapat dipilotkan sebagai item asli"], "Masuk bank bersama varian", "green", kind="status")

# Section 03.
card(1250, 3780, 1500, 180, "BANGUN & UJI ITEM MODEL", ["Invariant, slot, constraint, solusi, distraktor", "Range = family rule ∩ grade ∩ difficulty profile"], "Dry-run · Hypothesis/Pytest · range provenance", "teal")
card(210, 4110, 1600, 230, "MODE A · PARAMETER VARIANT", ["Constructive generation, angka/satuan valid", "Seeded RNG; target difficulty features", "Retry terbatas bila di luar band"], "Python · NumPy · SymPy · Z3/OR-Tools opsional", "teal")
card(2190, 4110, 1600, 230, "MODE B · ISOMORPHIC CANDIDATE", ["Ubah konteks/redaksi/representasi yang diizinkan", "Strict JSON + daftar perubahan", "Kandidat belum dianggap ekuivalen"], "LLM adapter · transformation policy · Pydantic", "teal")
card(1275, 4450, 1450, 150, "INSTANSIASI KANDIDAT VARIAN", ["Snapshot parameter, seed, lineage, versi model"], "item_family_id · item_model_version", "teal")
card(300, 4710, 1500, 170, "HITUNG ULANG & VERIFIKASI KUNCI", ["Solution rule → answer → independent check", "Kunci induk tidak disalin"], "SymPy · deterministic rule verifier", "teal")
card(2200, 4710, 1500, 170, "DISTRAKTOR MISKONSEPSI", ["Rule menghitung opsi salah; LLM hanya usul pola", "Tepat satu benar, opsi unik, satuan konsisten"], "Misconception rules · LLM-assisted", "teal")
card(100, 5010, 1010, 180, "NEW FAMILY CANDIDATE", ["Soal valid tetapi konstruk bergeser", "Dipisahkan dari keluarga lama"], "new_item_family_candidate", "amber", kind="status", title_size=28)
card(1250, 5010, 1500, 180, "AUTOMATED VARIANT QUALITY GATE", ["Schema/opsi/render/duplikat · matematika", "Objective, formula, solution graph, step delta"], "Repair/regenerate ≤ Rmax bila layak", "teal")
card(2840, 5010, 1030, 180, "KARANTINA / REJECT", ["Jawaban konflik, constraint gagal", "atau retry habis"], "quarantined / rejected", "red", kind="status", title_size=28)
card(1250, 5300, 1500, 175, "SCREENING ULANG TIAP VARIAN", ["IndoBERT + LLM independen; label induk hanya referensi", "Taksonomi, invariant, OOD, risiko + arbitration"], "Reuses AI agreement engine di atas", "violet")
card(2840, 5300, 1030, 175, "KONFLIK / OOD", ["Tidak sepakat setelah arbitration"], "quarantine_ai_conflict", "red", kind="status", title_size=28)
card(1250, 5570, 1500, 160, "AI CONSENSUS VARIANT", ["Item keluarga berversi, status provisional"], "MongoDB · immutable lineage", "green", kind="status")

# Section 04.
card(1250, 5930, 1500, 160, "PROVISIONAL ITEM BANK", ["Induk + varian diterima; status dan versi immutable"], "MongoDB · item_models · families · variants", "green", kind="status")
card(1250, 6200, 1500, 170, "SECURE ASSESSMENT DELIVERY", ["Snapshot per attempt; opsi publik, kunci tetap server", "Server-side scoring; refresh tidak mengganti varian"], "Express API · React · KaTeX · JSXGraph/SVG", "green")
card(1250, 6460, 1500, 170, "RESPONSE EVENTS & VALIDATION", ["ID/version/population, correctness, waktu, perubahan", "Dedup, rapid guess, anomali, grouping"], "MongoDB / event store · pseudonymous ID", "green")
card(1250, 6730, 1500, 180, "CTT · VARIANT & FAMILY ANALYSIS", ["p + Wilson CI, discrimination, point-biserial", "Distraktor, waktu; variance & stability antarsibling"], "Pandas · NumPy · SciPy · scikit-learn", "green")
card(130, 7030, 1200, 170, "BUKTI BELUM CUKUP", ["collect_more_events", "Tetap pilot terbatas"], "CI lebar / N rendah", "amber", kind="status", title_size=29)
card(1400, 7030, 1200, 170, "STABIL", ["empirically_screened", "Target training eligible bila quality gate lolos"], "Bukti per versi & populasi", "green", kind="status", title_size=29)
card(2670, 7030, 1200, 170, "FLAG BERAT", ["auto_unpublish / regenerate / retire", "Jangan latih dari snapshot bermasalah"], "Anomali / kualitas buruk", "red", kind="status", title_size=29)

# Section 05 and stack strip.
card(170, 7410, 1700, 300, "LOOP A · MODEL PSIKOMETRIK", ["Target: p, hardness, discrimination, quality, time", "Weight dari N, CI, stability; split per item family", "Fine-tune multi-task IndoBERT; evaluasi vs champion", "Shadow → canary → monitor → promote / rollback"], "JSONL/Parquet · PyTorch · MLflow / manifests", "violet")
card(2130, 7410, 1700, 300, "LOOP B · KEBIJAKAN GENERATOR", ["Kalibrasi range, difficulty driver, distraktor, konteks", "Candidate policy v2 + provenance snapshot", "Dry-run, replay seed lama, compare invalid/error", "Promote policy baru atau reject; versi lama utuh"], "Python rules · Hypothesis · MongoDB · MLflow", "teal")

nodes.append('<rect x="85" y="7780" width="3830" height="625" rx="24" fill="#EAF0F7" stroke="#CBD8E6" stroke-width="2"/>')
nodes.append(f'<text x="125" y="7835" font-size="34" font-weight="900" fill="{COLORS["ink"]}">PETA TECH STACK &amp; DATA PRODUCTS</text>')
tech_columns = [
    (125, "INGEST / EXTRACTION", ["Node.js · Express · Multer · AJV", "Redis + Celery/RQ · FastAPI", "PyMuPDF · Tesseract · Pillow", "PaddleOCR · PP-DocLayout · FormulaNet"]),
    (1075, "REASONING / GENERATION", ["IndoBERT · PyTorch · HF", "LLM adapter · JSON Schema · FAISS", "Python · NumPy · SymPy · rules", "Z3/OR-Tools opsional · Hypothesis"]),
    (2025, "STORAGE / DELIVERY", ["MongoDB · MinIO/S3-compatible", "JSONL · Parquet · MLflow/manifests", "React · KaTeX · JSXGraph/SVG", "Versioned snapshot · server scoring"]),
    (2975, "EVIDENCE / OPERATIONS", ["Pandas · SciPy · scikit-learn", "Prometheus · Grafana · OpenTelemetry", "Docker · Docker Compose · CI/CD", "Shadow · canary · auto rollback", "IRT opsional setelah linking & item fit"]),
]
for x, title, items in tech_columns:
    nodes.append(f'<text x="{x}" y="7905" font-size="26" font-weight="800" fill="{COLORS["blue"]}">{escape(title)}</text>')
    for i, item in enumerate(items):
        nodes.append(f'<text x="{x}" y="{7954+i*45}" font-size="22" fill="{COLORS["ink"]}">•  {escape(item)}</text>')
nodes.append(f'<text x="125" y="8240" font-size="23" fill="{COLORS["muted"]}">'
             'Status: arsitektur target. Komponen yang belum tersedia di repository tetap ditampilkan sebagai rancangan, bukan klaim implementasi.</text>')
nodes.append(f'<text x="125" y="8310" font-size="22" fill="{COLORS["muted"]}">'
             'Sumber: API_DOCUMENTATION/15_AUTONOMOUS_AI_PSYCHOMETRIC_LEARNING_ARCHITECTURE.md + 16_CONTROLLED_QUESTION_VARIATION_GENERATION.md</text>')

# Explanatory labels placed after cards for clean reading.
label(2000, 681, "submit → validasi request", "blue")
label(2000, 945, "job asinkron", "blue")
label(2000, 1403, "kandidat ekstraksi", "blue")
label(2000, 1698, "lolos quality gate", "blue")
label(2000, 1942, "canonical version", "blue")
label(2000, 2175, "struktur valid", "blue")
label(2000, 2416, "jawaban terverifikasi", "blue")
label(2000, 2923, "prediksi independen", "violet")
label(2000, 3171, "full agreement + risk rendah", "green")
label(1450, 3595, "parent untuk variasi", "teal")
label(3795, 3770, "jalur item induk", "green", 22, rotate=90)
label(2000, 4085, "pilih mode", "teal")
label(2000, 4395, "kandidat", "teal")
label(2000, 4665, "hitung ulang", "teal")
label(2000, 4955, "opsi tervalidasi", "teal")
label(2000, 5255, "lolos seluruh gate", "teal")
label(2000, 5525, "taksonomi sepakat + risk rendah", "green")
label(2000, 5885, "varian diterima", "green")
label(2000, 6162, "pilot terbatas", "green")
label(2000, 6422, "attempt terversi", "green")
label(2000, 6690, "respons valid", "green")
label(2000, 6978, "quality gate empiris", "green")
label(135, 6720, "lanjutkan pilot", "amber", 22, rotate=-90)
label(90, 5900, "feedback model", "violet", 22, rotate=-90)
label(3910, 6120, "feedback generator", "teal", 22, rotate=-90)

defs = [
    '<defs>',
    '<style>text{font-family:Segoe UI,Arial,sans-serif} .card{filter:url(#shadow)}</style>',
    '<filter id="shadow" x="-10%" y="-15%" width="120%" height="135%"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#183552" flood-opacity="0.09"/></filter>',
]
for name, color in [("gray", "line"), ("blue", "blue"), ("teal", "teal"), ("violet", "violet"),
                    ("amber", "amber"), ("red", "red"), ("green", "green")]:
    defs.append(f'<marker id="arrow-{name}" viewBox="0 0 12 12" refX="10" refY="6" '
                f'markerWidth="11" markerHeight="11" orient="auto-start-reverse">'
                f'<path d="M1 1 L11 6 L1 11 Z" fill="{COLORS[color]}"/></marker>')
defs.append('</defs>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
       f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img" '
       'aria-labelledby="diagram-title diagram-desc">\n'
       '<title id="diagram-title">Arsitektur end-to-end AI psikometrik dan generasi variasi soal</title>\n'
       '<desc id="diagram-desc">Diagram lima bagian yang menggabungkan ingest dan ekstraksi, klasifikasi AI, '
       'generasi varian terkendali, delivery dan psikometrik, serta loop perbaikan model dan generator.</desc>\n'
       + "\n".join(defs) + "\n"
       + f'<rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="{COLORS["paper"]}"/>\n'
       + "\n".join(lines) + "\n" + "\n".join(nodes) + "\n</svg>\n")
OUT.write_text(svg, encoding="utf-8")
print(OUT)
