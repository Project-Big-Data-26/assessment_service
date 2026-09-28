"""Render an editable flowchart for Nalar's target validation workflow."""

from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "API_DOCUMENTATION" / "20_END_TO_END_VALIDATION_FLOW.svg"
W, H = 2500, 8640
C = {
    "bg": "#F7FAFD",
    "white": "#FFFFFF",
    "navy": "#122C46",
    "ink": "#17304A",
    "muted": "#4B6278",
    "line": "#A9BED0",
    "blue": "#2879B9",
    "blue_soft": "#EAF5FC",
    "purple": "#7059AF",
    "purple_soft": "#F1EFFA",
    "green": "#158672",
    "green_soft": "#EAF8F3",
    "orange": "#B97920",
    "orange_soft": "#FFF6E9",
    "red": "#BA4858",
    "red_soft": "#FFF0F2",
}

edges = []
nodes = []


def put(value):
    nodes.append(value)


def text(x, y, value, size=21, weight=400, color="ink", anchor="start"):
    put(
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="Segoe UI, Arial, sans-serif" font-size="{size}" '
        f'font-weight="{weight}" fill="{C.get(color, color)}">{escape(value)}</text>'
    )


def rect(x, y, w, h, fill="white", stroke="line", radius=18, sw=2):
    put(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
        f'fill="{C.get(fill, fill)}" stroke="{C.get(stroke, stroke)}" stroke-width="{sw}"/>'
    )


def path(points, color="line", dashed=False, arrow=True, width=3):
    data = " ".join(
        ("M" if i == 0 else "L") + f" {x} {y}"
        for i, (x, y) in enumerate(points)
    )
    dash = ' stroke-dasharray="11 9"' if dashed else ""
    mark = f' marker-end="url(#arr-{color})"' if arrow else ""
    edges.append(
        f'<path d="{data}" fill="none" stroke="{C[color]}" stroke-width="{width}" '
        f'stroke-linecap="round" stroke-linejoin="round"{dash}{mark}/>'
    )


def icon(name, x, y, color, size=39):
    put(
        f'<use href="#ic-{name}" x="{x}" y="{y}" width="{size}" height="{size}" '
        f'color="{C[color]}"/>'
    )


def number(value, y, color):
    put(f'<circle cx="323" cy="{y}" r="30" fill="{C[color]}"/>')
    text(323, y + 8, str(value).zfill(2), 21, 800, "white", "middle")


def terminal(cx, y, w, h, label, color="blue"):
    rect(cx - w / 2, y, w, h, C[color + "_soft"], color, h / 2, 3)
    text(cx, y + h / 2 + 10, label, 28, 800, color, "middle")


def io(x, y, w, h, title, body, color="blue", step=None, symbol="upload"):
    points = f"{x+52},{y} {x+w},{y} {x+w-52},{y+h} {x},{y+h}"
    put(f'<polygon points="{points}" fill="{C[color + "_soft"]}" stroke="{C[color]}" stroke-width="3"/>')
    if step is not None:
        number(step, y + h / 2, color)
    icon(symbol, x + 93, y + 28, color, 48)
    text(x + 159, y + 59, title, 29, 800)
    for i, line in enumerate(body):
        text(x + 95, y + 101 + i * 31, line, 21, 400, "muted")


def process(x, y, w, h, title, body, color="blue", step=None, symbol="file", note=None):
    rect(x, y, w, h, "white", color, 18, 2.5)
    put(f'<rect x="{x}" y="{y}" width="11" height="{h}" rx="5" fill="{C[color]}"/>')
    if step is not None:
        number(step, y + 43, color)
    icon(symbol, x + 29, y + 27, color, 45)
    text(x + 91, y + 56, title, 29, 800)
    for i, line in enumerate(body):
        text(x + 34, y + 99 + i * 31, line, 21, 400, "muted")
    if note:
        text(x + 34, y + h - 19, note, 18, 700, color)


def detailed(x, y, w, h, title, steps, note, color, step, symbol):
    process(x, y, w, h, title, [], color, step, symbol)
    for i, item in enumerate(steps):
        yy = y + 108 + i * 54
        put(f'<circle cx="{x+55}" cy="{yy-7}" r="17" fill="{C[color + "_soft"]}" stroke="{C[color]}" stroke-width="1.5"/>')
        text(x + 55, yy, str(i + 1), 18, 800, color, "middle")
        text(x + 91, yy, item, 21, 500)
    text(x + 35, y + h - 22, note, 18, 700, color)


def decision(cx, y, w, h, title, lines, color="blue", step=None):
    points = f"{cx},{y} {cx+w/2},{y+h/2} {cx},{y+h} {cx-w/2},{y+h/2}"
    put(f'<polygon points="{points}" fill="{C[color + "_soft"]}" stroke="{C[color]}" stroke-width="3"/>')
    if step is not None:
        number(step, y + h / 2, color)
    text(cx, y + 61, title, 27, 800, color, "middle")
    for i, item in enumerate(lines):
        text(cx, y + 91 + i * 27, item, 19, 400, "ink", "middle")


def data(cx, y, w, h, title, body, color="green", step=None):
    x = cx - w / 2
    put(
        f'<path d="M{x},{y+25} C{x},{y-8} {x+w},{y-8} {x+w},{y+25} '
        f'L{x+w},{y+h-25} C{x+w},{y+h+8} {x},{y+h+8} {x},{y+h-25} Z" '
        f'fill="{C[color + "_soft"]}" stroke="{C[color]}" stroke-width="3"/>'
    )
    put(
        f'<ellipse cx="{cx}" cy="{y+25}" rx="{w/2}" ry="25" '
        f'fill="{C[color + "_soft"]}" stroke="{C[color]}" stroke-width="3"/>'
    )
    if step is not None:
        number(step, y + h / 2, color)
    icon("database", x + 43, y + 65, color, 42)
    text(x + 102, y + 81, title, 27, 800)
    for i, item in enumerate(body):
        text(x + 102, y + 113 + i * 28, item, 19, 400, "muted")


def side(x, y, w, h, title, lines, color, symbol):
    rect(x, y, w, h, C[color + "_soft"], color, 18, 2)
    icon(symbol, x + 19, y + 19, color, 36)
    text(x + 62, y + 47, title, 21, 800, color)
    for i, item in enumerate(lines):
        text(x + 20, y + 78 + i * 27, item, 18, 400, "ink")


def stack(y, h, title, items, color):
    x, w = 1850, 570
    rect(x, y, w, h, C[color + "_soft"], "line", 19, 1.5)
    put(f'<rect x="{x}" y="{y}" width="10" height="{h}" rx="5" fill="{C[color]}"/>')
    text(x + 29, y + 46, title, 23, 800, color)
    for i, item in enumerate(items):
        text(x + 29, y + 86 + i * 34, item, 19, 400, "ink")


def label(x, y, value, color="muted"):
    text(x, y, value, 19, 800, color)


icons = {
    "upload": '<path d="M12 16V3 M7 8l5-5 5 5 M4 17v4h16v-4"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z M14 2v6h6 M8 13h8 M8 17h8"/>',
    "scan": '<path d="M4 9V5a1 1 0 0 1 1-1h4 M15 4h4a1 1 0 0 1 1 1v4 M20 15v4a1 1 0 0 1-1 1h-4 M9 20H5a1 1 0 0 1-1-1v-4 M7 12h10"/>',
    "check": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 9l2 2 4-4 M8 16h8"/>',
    "chip": '<rect x="5" y="5" width="14" height="14" rx="2"/><path d="M9 9h6v6H9z M9 1v4 M15 1v4 M9 19v4 M15 19v4 M1 9h4 M1 15h4 M19 9h4 M19 15h4"/>',
    "spark": '<path d="M12 2l1.7 6.3L20 10l-6.3 1.7L12 18l-1.7-6.3L4 10l6.3-1.7z M19 17l.7 2.3L22 20l-2.3.7L19 23l-.7-2.3L16 20l2.3-.7z"/>',
    "users": '<circle cx="9" cy="8" r="3"/><path d="M3 20v-2a6 6 0 0 1 12 0v2z M17 5a3 3 0 0 1 0 6 M18 14a5 5 0 0 1 3 5v1"/>',
    "vote": '<path d="M4 10h16l-2 10H6z M8 10V4h8v6 M10 15l2 2 4-4"/>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5 M3 12c0 1.7 4 3 9 3s9-1.3 9-3"/>',
    "screen": '<rect x="2" y="3" width="20" height="15" rx="2"/><path d="M8 22h8 M12 18v4"/>',
    "chart": '<path d="M4 20V4 M4 20h16 M8 17v-5 M12 17V8 M16 17v-9 M20 17V5"/>',
    "loop": '<path d="M20 7v5h-5 M4 17v-5h5 M6 8a7 7 0 0 1 12-2l2 1 M18 16a7 7 0 0 1-12 2l-2-1"/>',
    "pause": '<circle cx="12" cy="12" r="9"/><path d="M9 8v8 M15 8v8"/>',
}

head = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
    f'viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
    '<title id="title">Alur validasi soal matematika dengan keputusan bersyarat</title>',
    '<desc id="desc">Flowchart berbahasa Indonesia dari soal guru, pilihan OCR, pemeriksaan '
    'format, IndoBERT, tiga run Claude, tiga ahli blind, voting manusia, pilot, CTT, dan IRT opsional. '
    'Cabang ya/tidak, simbol flowchart, serta teknologi pendukung ditampilkan terpisah.</desc>',
    "<defs>",
]
for name, icon_markup in icons.items():
    head.append(
        f'<symbol id="ic-{name}" viewBox="0 0 24 24" fill="none" '
        f'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
        f'stroke-linejoin="round">{icon_markup}</symbol>'
    )
for key in ("line", "blue", "purple", "green", "orange", "red"):
    head.append(
        f'<marker id="arr-{key}" markerWidth="12" markerHeight="12" '
        f'refX="9" refY="6" orient="auto" markerUnits="userSpaceOnUse">'
        f'<path d="M1 1 L10 6 L1 11 Z" fill="{C[key]}"/></marker>'
    )
head.append("</defs>")
head.append(f'<rect width="{W}" height="{H}" fill="{C["bg"]}"/>')
head.append('<rect x="0" y="0" width="2500" height="213" fill="#122C46"/>')

text(80, 75, "NALAR  /  ALUR VALIDASI SOAL MATEMATIKA", 46, 800, "white")
text(80, 128, "Dari soal guru sampai keputusan pakar dan bukti psikometrik", 29, 400, "#DDEBF8")
text(80, 173, "Diagram target • biru: input | ungu: AI | hijau: ahli | jingga: pilot & empiris", 20, 400, "#BBD2E7")

# Legend uses real notation. These shapes are samples, not flow nodes.
rect(72, 245, 2350, 161, "white", "line", 19, 1.5)
text(102, 281, "CARA MEMBACA", 22, 800)
rect(112, 306, 120, 52, "blue_soft", "blue", 26, 2)
text(172, 340, "Mulai", 18, 700, "blue", "middle")
text(246, 340, "awal/akhir", 18, 400)
put('<polygon points="460,306 600,306 580,358 440,358" fill="#EAF5FC" stroke="#2879B9" stroke-width="2"/>')
text(520, 340, "Soal", 18, 700, "blue", "middle")
text(617, 340, "masukan", 18, 400)
rect(786, 306, 125, 52, "purple_soft", "purple", 5, 2)
text(848, 340, "Model", 18, 700, "purple", "middle")
text(926, 340, "proses", 18, 400)
put('<polygon points="1160,305 1223,332 1160,359 1097,332" fill="#EAF8F3" stroke="#158672" stroke-width="2"/>')
text(1160, 338, "?", 23, 800, "green", "middle")
text(1245, 340, "keputusan: ya/tidak", 18, 400)
put('<ellipse cx="1680" cy="317" rx="74" ry="13" fill="#EAF8F3" stroke="#158672" stroke-width="2"/>')
rect(1606, 317, 148, 37, "green_soft", "green", 0, 2)
put('<ellipse cx="1680" cy="354" rx="74" ry="13" fill="#EAF8F3" stroke="#158672" stroke-width="2"/>')
text(1772, 340, "data tersimpan", 18, 400)
text(2050, 340, "→ alur  - - → ulang", 18, 700, "muted")
static_nodes_end = len(nodes)
text(86, 456, "ALUR UTAMA", 21, 800, "blue")
text(1850, 456, "TEKNOLOGI PENDUKUNG", 21, 800, "muted")
text(1850, 481, "(kotak kanan bukan langkah alur)", 17, 400, "muted")

# Connectors are kept behind the nodes.
path([(905, 502), (905, 548)], "blue")
path([(905, 700), (905, 758)], "blue")
path([(905, 930), (905, 1178)], "blue")
path([(630, 845), (220, 845), (220, 958)], "blue")
path([(220, 1122), (220, 1148), (905, 1148), (905, 1178)], "blue")
path([(905, 1352), (905, 1408)], "blue")
path([(905, 1592), (905, 1638)], "blue")
path([(905, 1812), (905, 1868)], "purple")
path([(1180, 1725), (1468, 1725)], "red")
path([(1640, 1638), (1640, 1314), (1434, 1314), (1434, 1265)], "red", dashed=True)
path([(905, 2222), (905, 2278)], "purple")
path([(905, 2642), (905, 2698)], "purple")
path([(905, 2872), (905, 2928)], "green")
path([(1180, 2785), (1468, 2785)], "red")
path([(905, 3112), (905, 3168)], "green")
path([(905, 3342), (905, 3398)], "green")
path([(905, 3592), (905, 3848)], "green")
path([(1185, 3495), (1468, 3495)], "red")
path([(1635, 3572), (1635, 3638)], "red")
path([(1470, 3720), (1370, 3720), (1370, 3940), (1295, 3940)], "green")
path([(1635, 3802), (1635, 3848)], "red")
path([(905, 4032), (905, 4088)], "green")
path([(1180, 4175), (1468, 4175)], "red")
path([(905, 4262), (905, 4318)], "orange")
path([(905, 4492), (905, 4548)], "orange")
path([(905, 4712), (905, 4768)], "orange")
path([(905, 5120), (905, 5188)], "orange")
path([(630, 5275), (372, 5275)], "orange")
path([(220, 5200), (220, 4630), (375, 4630)], "orange", dashed=True)
path([(905, 5362), (905, 5418)], "orange")
path([(1180, 5510), (1468, 5510)], "orange")
path([(905, 5602), (905, 5668)], "purple")
path([(1635, 5590), (1635, 6150), (1185, 6150)], "orange")
path([(905, 5990), (905, 6048)], "purple")
path([(1180, 6145), (1468, 6145)], "red")
path([(905, 6242), (905, 6318)], "green")
path([(905, 6502), (905, 6558)], "green")
path([(905, 6782), (905, 6828)], "green")

# Main flow.
terminal(905, 422, 350, 82, "Mulai", "blue")
io(380, 550, 1050, 150, "Soal masuk dari guru", [
    "Guru mengetik soal, mengimpor data, atau mengunggah PDF/gambar.",
    "Tidak ada tahap koreksi guru yang wajib untuk setiap soal.",
], "blue", 1, "upload")
decision(905, 760, 550, 170, "Perlu baca dokumen?", [
    "PDF/gambar → YA",
    "Input langsung → TIDAK",
], "blue", 2)
side(72, 960, 300, 162, "Baca berkas", [
    "OCR/ambil teks,",
    "opsi dan rumus.",
    "Simpan tanda ragu.",
], "blue", "scan")
process(380, 1180, 1050, 172, "Simpan versi soal", [
    "Satukan teks, opsi, gambar, kunci, solusi, kelas dan topik.",
    "Setiap perubahan isi penting membuat versi soal baru.",
], "blue", 3, "file")
process(380, 1410, 1050, 182, "Periksa format dan kunci jawaban", [
    "Cek kelengkapan, pilihan jawaban, rumus, dan soal ambigu.",
    "Cocokkan kunci dengan solusi/rule matematika bila memungkinkan.",
], "blue", 4, "check")
decision(905, 1640, 550, 172, "Soal siap?", [
    "Format + kunci valid?",
    "YA → model; TIDAK → perbaiki/tahan",
], "blue")
side(1470, 1640, 332, 155, "Perbaiki / tahan", [
    "Guru revisi isi soal,",
    "atau karantina.",
    "Versi baru diperiksa lagi.",
], "red", "pause")

detailed(380, 1870, 1050, 352, "IndoBERT memprediksi tiga hal", [
    "Siapkan teks, opsi, solusi, kelas, topik, format; KKO = fitur kata.",
    "Tokenisasi → encoder IndoBERT membaca konteks bahasa soal.",
    "Tiga head → domain matematika (3), pengetahuan (4), kesulitan (3).",
    "Simpan P(label), H = -Σ p log₂ p per head, OOD, modelVersion.",
], "Tidak ada konversi langsung KKO → label dan tidak ada C1–C6.", "purple", 5, "chip")
detailed(380, 2280, 1050, 362, "Claude: CoT + majority voting (N = 3)", [
    "Tiga run terpisah: soal, rubrik, solusi, prediksi IndoBERT.",
    "CoT/telaah bertahap: cek kunci, jalur solusi, bukti 3 head.",
    "JSON tiap run: label, confirm/revise/abstain, flag, bukti.",
    "Majority vote per head: 3/3, 2/3; 1–1–1 → flag ke ahli.",
], "3 run Claude bukan 3 pakar, confidence, atau gold label.", "purple", 6, "spark")
decision(905, 2700, 550, 172, "Tiga run sah?", [
    "Schema, versi, bukti valid?",
    "Konflik label tetap lanjut ke ahli.",
], "purple")
side(1470, 2710, 332, 155, "Ulang / tahan", [
    "Timeout, JSON rusak",
    "atau tanpa bukti.",
    "Tidak boleh bypass LLM.",
], "red", "pause")

process(380, 2930, 1050, 182, "Tiga ahli menilai blind", [
    "Tidak melihat AI/suara ahli lain; catat keputusan awal tetap.",
    "Cek cakupan, kejelasan, kunci, skor; lalu label 3 head + bukti.",
], "green", 7, "users")
process(380, 3170, 1050, 172, "Tiga ahli melihat usulan AI", [
    "Sesudah pass blind terkunci, buka IndoBERT + 3 run Claude.",
    "Terima/ubah/tolak per head; alasan dan perubahan disimpan.",
], "green", 8, "vote")
decision(905, 3400, 560, 192, "Ada mayoritas?", [
    "Tiga ahli manusia, per head.",
    "3–0 / 2–1 → YA jika isi layak",
    "1–1–1 / abstain → adjudikasi",
], "green", 9)
side(1470, 3420, 332, 152, "Diskusi pakar", [
    "Baca rubrik dan",
    "bukti soal; bila perlu",
    "adjudicator senior.",
], "red", "users")
decision(1635, 3640, 330, 162, "Selesai?", [
    "YA → valid",
    "TIDAK → tahan",
], "green")
side(1470, 3850, 332, 150, "Tahan butir", [
    "Belum jadi gold/pilot.",
    "Jika konflik masif, audit",
    "rubrik per head.",
], "red", "pause")
data(905, 3850, 780, 182, "Bank soal tervalidasi ahli", [
    "Simpan keputusan per head, dissent, alasan dan versi soal.",
    "Kesepakatan dua AI saja tidak cukup.",
], "green", 10)
decision(905, 4090, 550, 172, "Boleh uji coba?", [
    "Keputusan ahli +",
    "kebijakan pilot lolos?",
], "green")
side(1470, 4100, 332, 155, "Tahan dari pilot", [
    "Kunci/izin/risiko",
    "belum memenuhi",
    "kebijakan.",
], "red", "pause")

process(380, 4320, 1050, 172, "Tampilkan soal ke siswa", [
    "LMS memberi versi soal yang terkunci; kunci tidak dikirim.",
    "Pilihan ganda, benar/salah, matching, checkbox, click-box, dll.",
], "orange", 11, "screen")
io(380, 4550, 1050, 162, "Jawaban siswa masuk", [
    "Simpan pilihan, waktu dan sesi; skor dihitung di server.",
    "Data selalu terkait versi soal dan populasi uji.",
], "orange", 12, "file")
detailed(380, 4770, 1050, 350, "CTT — analisis kualitas soal", [
    "p = Σ benar/N; Wilson CI menunjukkan ketidakpastian.",
    "D = p_atas − p_bawah: discrimination index.",
    "r_it = Corr(item, total tanpa item): daya beda terkoreksi.",
    "Cek distraktor, skor parsial, α form, waktu, missing.",
], "Hitung per versi, populasi, form, dan respons final yang eligible.", "orange", 13, "chart")
decision(905, 5190, 550, 172, "Data CTT cukup?", [
    "N, sampel, CI dan form",
    "cukup untuk tafsir?",
], "orange")
side(72, 5200, 300, 150, "Kumpulkan lagi", [
    "Belum klaim kualitas.",
    "Lanjutkan pilot aman",
    "dengan versi yang sama.",
], "orange", "loop")
decision(905, 5420, 550, 182, "IRT layak?", [
    "Sampel + asumsi +",
    "form terhubung?",
], "orange")
side(1470, 5430, 332, 160, "CTT saja", [
    "Simpan alasan IRT",
    "belum layak; lanjut",
    "ke telaah mutu.",
], "orange", "chart")
detailed(380, 5670, 1050, 320, "IRT — kalibrasi opsional", [
    "Cek unidimensi, independensi lokal dan model fit.",
    "1PL: b; 2PL: a + b; 3PL: a + b + c (guessing).",
    "Skor parsial: PCM/GPCM dengan ambang kategori.",
    "Estimasi θ, informasi item/tes dan kesalahan baku.",
], "Jika fit/asumsi gagal: laporkan CTT saja, jangan paksa IRT.", "purple", 14, "chart")
decision(905, 6050, 550, 192, "Soal bermasalah?", [
    "Kunci, diskriminasi,",
    "distraktor atau fit?",
], "orange")
side(1470, 6070, 332, 160, "Tinjau isi soal", [
    "Tahan jika berisiko;",
    "jika isi berubah,",
    "buat versi baru.",
], "red", "check")
data(905, 6320, 780, 182, "Simpan snapshot empiris", [
    "CTT/IRT, N, CI/SE, populasi, form dan versi.",
    "Kesulitan empiris ≠ perkiraan awal; H1/H2 tetap.",
], "green", 15)
process(380, 6560, 1050, 222, "Gunakan bukti untuk perbaikan", [
    "Isi sama: statistik baru, tanpa voting ahli ulang rutin.",
    "Isi berubah: versi baru → validasi dan pilot ulang.",
    "Data ahli + pilot dapat melatih model penantang.",
], "green", 16, "loop", "Model penantang dipakai sesudah diuji pada data terpisah.")
terminal(905, 6830, 400, 82, "Selesai / pantau", "green")

# Explicit labels on conditional edges.
label(453, 828, "YA · dokumen", "blue")
label(945, 1060, "TIDAK · langsung", "blue")
label(1260, 1697, "TIDAK", "red")
label(944, 1841, "YA", "green")
label(1255, 2756, "TIDAK", "red")
label(944, 2900, "YA", "green")
label(1240, 3472, "TIDAK", "red")
label(945, 3740, "YA", "green")
label(1370, 3698, "YA", "green")
label(1660, 3830, "TIDAK", "red")
label(1240, 4150, "TIDAK", "red")
label(945, 4292, "YA", "green")
label(420, 5250, "TIDAK", "orange")
label(944, 5390, "YA", "green")
label(1240, 5482, "TIDAK", "orange")
label(944, 5642, "YA", "purple")
label(1505, 5960, "CTT SAJA", "orange")
label(1240, 6120, "YA", "red")
label(944, 6280, "TIDAK", "green")

# Tech stack lane stays visually separate from the process.
stack(540, 310, "01–03  SOAL MASUK", [
    "UI guru + API gateway (target)",
    "OCR/PyMuPDF/Tesseract (sebagian ada)",
    "JSON Schema / Pydantic",
    "MongoDB: soal + versi (target)",
    "File sumber + jejak ekstraksi (target)",
], "blue")
stack(1385, 225, "04  PENGECEKAN", [
    "Rules + pemeriksa matematika",
    "SymPy jika cocok (target)",
    "workflow_runs / bukti kunci (target)",
], "blue")
stack(1860, 370, "05–06  MODEL AI", [
    "PyTorch / Transformers / IndoBERT",
    "3 head target, versi lama masih C1–C6",
    "Fitur KKO, probabilitas, entropy, OOD",
    "Claude CoT: telaah 3 run (target)",
    "Schema JSON + prompt/modelVersion",
    "Majority vote per head ≠ confidence/gold",
    "Secret manager; jangan kirim API key",
], "purple")
stack(2915, 300, "07–10  AHLI MATEMATIKA", [
    "UI pakar + autentikasi/RBAC (target)",
    "Blind: isi/kunci + 3 label + alasan",
    "Review AI setelah suara awal dikunci",
    "Vote manusia ≠ 3 run Claude",
    "MongoDB: suara, dissent, audit (target)",
], "green")
stack(4305, 225, "11–12  LMS & RESPONS", [
    "Gateway/LMS dan snapshot versi (target)",
    "delivery_instances + response_events",
    "Skoring di server, bukan browser",
], "orange")
stack(4770, 360, "13  CTT: ANALISIS ITEM", [
    "Python, Pandas/NumPy/SciPy",
    "CTT dasar sudah prototype",
    "p = B/N; Wilson CI; q = 1−p",
    "D = p_atas−p_bawah; r_it corrected",
    "Opsi/distraktor; skor parsial",
    "Alpha = konsistensi form, bukan item",
    "Waktu, missing, N, populasi, versi",
], "orange")
stack(5670, 315, "14  IRT: OPSIONAL", [
    "1PL/Rasch: b; 2PL: a,b; 3PL: a,b,c",
    "PCM/GPCM untuk skor parsial",
    "θ siswa, informasi item/tes, SE",
    "Uji dimensi, local independence, fit",
    "Kalibrasi butuh data/asumsi layak",
], "purple")
stack(6560, 225, "15–16  SNAPSHOT & UMPAN BALIK", [
    "psychometric_snapshots (target)",
    "JSONL/Parquet + manifest (target)",
    "Split dataset per keluarga soal",
    "Model registry/challenger (target)",
], "green")

# Optional branch is below the completed main flow.
rect(75, 6970, 2345, 223, "green_soft", "green", 22, 2)
icon("loop", 108, 7010, "green", 48)
text(176, 7046, "CABANG OPSIONAL: BUAT VARIASI SOAL", 28, 800, "green")
text(112, 7092, "Mulai dari soal induk yang sudah disetujui ahli → tetapkan aturan perubahan → hasilkan varian → hitung ulang kunci.", 21)
text(112, 7131, "Varian yang berubah isinya kembali ke langkah 03–10: periksa format, IndoBERT, Claude, dan 3 ahli sebelum pilot.", 21, 700, "green")
text(112, 7170, "Label induk tidak diwariskan otomatis; semua varian satu keluarga berada pada split data yang sama.", 20, 400, "muted")

rect(75, 7225, 2345, 183, "white", "line", 18, 1.4)
text(108, 7268, "CATATAN PENTING", 23, 800, "red")
text(108, 7303, "CoT Claude N=3: telaah bertahap dalam tiga run; simpan bukti ringkas, bukan jejak penalaran internal sebagai gold.", 19)
text(108, 7337, "Majority voting Claude dan suara 3 ahli adalah dua keputusan berbeda; 3/3 Claude bukan probabilitas benar.", 19)
text(108, 7371, "Diagram target: IRT, Claude N=3, dan UI ahli belum berarti fitur produksi sudah aktif.", 19, 700, "red")

# Formula key is outside the decision path but large enough to read in SVG/PNG.
rect(75, 7445, 2345, 630, "white", "line", 20, 1.5)
text(108, 7492, "RUMUS: APA YANG DIHITUNG, BUKAN AMBANG SEMBARANG", 27, 800, "navy")
rect(108, 7520, 1090, 515, "orange_soft", "orange", 15, 1.4)
icon("chart", 132, 7545, "orange", 40)
text(187, 7575, "CTT — item + form tes", 25, 800, "orange")
text(132, 7622, "p = Σ X/N; q = 1−p. p tinggi = lebih mudah di populasi itu.", 19)
text(132, 7667, "D = p_atas−p_bawah; grup diurut dari total tanpa item.", 19)
text(132, 7712, "r_it = Corr(X_item, T−X_item): corrected point-biserial.", 19)
text(132, 7757, "Distraktor: n_opsi/N dan pola pilihan atas vs bawah.", 19)
text(132, 7802, "Skor parsial: mean skor / skor maksimum; jangan paksa 0/1.", 19)
text(132, 7847, "α form = k/(k−1) × (1−ΣVar(X_i)/Var(T)).", 19)
text(132, 7892, "Wilson CI untuk p; waktu median/IQR; missing terpisah.", 19)
text(132, 7950, "D negatif → audit kunci, distraktor, populasi dan skoring.", 18, 800, "orange")
text(132, 7990, "Simpan N, versi, form, kelas/populasi dan jendela data.", 18, 700, "orange")
rect(1230, 7520, 1157, 515, "purple_soft", "purple", 15, 1.4)
icon("chart", 1255, 7545, "purple", 40)
text(1310, 7575, "IRT — kalibrasi opsional", 25, 800, "purple")
text(1255, 7622, "L(z) = 1/(1+e^(−z)); θ = kemampuan laten siswa.", 19)
text(1255, 7667, "1PL: P=L(θ−b); b = kesulitan.", 19)
text(1255, 7712, "2PL: P=L[a(θ−b)]; a = daya beda.", 19)
text(1255, 7757, "3PL: P=c+(1−c)L[a(θ−b)]; c = asimtot bawah.", 19)
text(1255, 7802, "PCM/GPCM: peluang kategori skor 0…m (parsial).", 19)
text(1255, 7847, "I_i(θ)=[P'_i(θ)]²/[P_i(θ)(1−P_i(θ))].", 19)
text(1255, 7892, "I_tes(θ)=Σ I_i(θ); SE(θ) ≈ 1/√I_tes(θ).", 19)
text(1255, 7950, "Uji dimensi, independensi lokal, fit, sampel & linking.", 18, 800, "purple")
text(1255, 7990, "Jika syarat gagal: tetap CTT dengan CI; tanpa parameter IRT.", 18, 700, "purple")

# The model-bootstrap strip is outside the shifted operational flow.
flow_nodes_end = len(nodes)
rect(75, 430, 2345, 242, "purple_soft", "purple", 20, 1.8)
text(108, 472, "SEBELUM ALUR INI: SIAPKAN MODEL DAN RUBRIK", 27, 800, "purple")
for x, w, title, detail in [
    (108, 675, "1  Tetapkan rubrik 3 × 4 × 3", "Gunakan contoh soal dan bukti solusi."),
    (851, 675, "2  Tiga ahli menilai blind", "Bahas konflik; bekukan gold awal."),
    (1594, 770, "3  Latih dan uji IndoBERT", "Split per keluarga; ukur F1/kalibrasi."),
]:
    rect(x, 502, w, 121, "white", "line", 14, 1.2)
    text(x + 22, 544, title, 23, 800)
    text(x + 22, 582, detail, 19, 400, "muted")
put('<path d="M790 563 L840 563" fill="none" stroke="#7059AF" stroke-width="3" marker-end="url(#arr-purple)"/>')
put('<path d="M1533 563 L1583 563" fill="none" stroke="#7059AF" stroke-width="3" marker-end="url(#arr-purple)"/>')
text(108, 652, "Gold awal berasal dari ahli; output model/Claude tidak menjadi label pelatihan secara otomatis.", 19, 700, "purple")
bootstrap_nodes = nodes[flow_nodes_end:]
flow_nodes = nodes[static_nodes_end:flow_nodes_end]
final = (
    head + nodes[:static_nodes_end] + bootstrap_nodes
    + ['<g transform="translate(0 300)">'] + edges + flow_nodes
    + ["</g>", "</svg>"]
)
OUT.write_text("\n".join(final) + "\n", encoding="utf-8")
print(OUT)
