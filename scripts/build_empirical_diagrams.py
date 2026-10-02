"""Render code-native 4K diagrams for the implemented empirical/ordinal flows."""
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "API_DOCUMENTATION"
W, H = 3840, 2160
COLORS = {"bg": "#f4f7fc", "ink": "#132d49", "muted": "#4a6078", "line": "#92a6bd",
          "blue": "#2468a0", "green": "#157566", "purple": "#7057a3", "orange": "#a06515"}


class Diagram:
    def __init__(self, title, subtitle):
        self.image = Image.new("RGB", (W, H), COLORS["bg"])
        self.draw = ImageDraw.Draw(self.image)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
                    f'<rect width="{W}" height="{H}" fill="{COLORS["bg"]}"/>']
        self.text(100, 65, title, 72, bold=True)
        self.text(100, 170, subtitle, 36, color="muted")

    @staticmethod
    def font(size, bold=False):
        candidates = [Path("C:/Windows/Fonts") / ("segoeuib.ttf" if bold else "segoeui.ttf"),
                      Path("/usr/share/fonts/truetype/dejavu") / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")]
        for path in candidates:
            if path.exists():
                return ImageFont.truetype(str(path), size)
        return ImageFont.load_default(size=size)

    def text(self, x, y, value, size, *, bold=False, color="ink"):
        fill = COLORS.get(color, color)
        self.draw.text((x, y), value, font=self.font(size, bold), fill=fill)
        self.svg.append(f'<text x="{x}" y="{y + size}" font-family="Segoe UI,DejaVu Sans,sans-serif" '
                        f'font-size="{size}" font-weight="{700 if bold else 400}" fill="{fill}">{escape(value)}</text>')

    def rectangle(self, x, y, width, height, fill, border=None):
        self.draw.rounded_rectangle((x, y, x + width, y + height), radius=24, fill=fill, outline=border, width=3)
        self.svg.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="24" fill="{fill}" '
                        f'stroke="{border or fill}" stroke-width="3"/>')

    def wrapped(self, text, width, size):
        lines = []; current = ""
        for word in text.split():
            trial = (current + " " + word).strip()
            if self.font(size).getlength(trial) > width and current:
                lines.append(current); current = word
            else:
                current = trial
        if current:
            lines.append(current)
        return lines

    def card(self, x, y, width, height, title, lines, color="blue"):
        accent = COLORS[color]
        self.rectangle(x, y, width, height, "#ffffff", accent)
        self.text(x + 36, y + 22, title, 43, bold=True, color=color)
        cursor = y + 98
        for value in lines:
            for line in self.wrapped(value, width - 72, 33):
                self.text(x + 36, cursor, line, 33)
                cursor += 47
        if cursor > y + height - 12:
            raise ValueError(f"card text overflows: {title}")

    def arrow(self, start, end):
        self.draw.line((start, end), fill=COLORS["line"], width=8)
        x, y = end; sx, sy = start
        if x == sx:
            points = [(x, y), (x - 16, y - 25), (x + 16, y - 25)]
        elif x > sx:
            points = [(x, y), (x - 25, y - 16), (x - 25, y + 16)]
        else:
            points = [(x, y), (x + 25, y - 16), (x + 25, y + 16)]
        self.draw.polygon(points, fill=COLORS["line"])
        self.svg.append(f'<line x1="{sx}" y1="{sy}" x2="{x}" y2="{y}" stroke="{COLORS["line"]}" stroke-width="8"/>')
        self.svg.append('<polygon points="' + " ".join(f"{a},{b}" for a, b in points) + f'" fill="{COLORS["line"]}"/>')

    def save(self, stem):
        (OUT / f"{stem}.svg").write_text("\n".join(self.svg + ["</svg>"]), encoding="utf-8")
        self.image.save(OUT / f"{stem}.png", optimize=True)
        self.image.save(OUT / f"{stem}.jpg", quality=94, subsampling=0)


def empirical():
    diagram = Diagram("VALIDASI EMPIRIS: DELIVERY, CTT / IRT, DAN REVIEW AHLI",
                      "Backend tersedia • data siswa nyata tetap diperlukan • version / population / grade tidak dicampur")
    content = [
        ("01  GOLD DAN BLUEPRINT", ["Human-gold snapshot + checksum.", "Kunci/solusi dan versi terverifikasi.", "Fixed form, satu grade/populasi.", "Silver / research tidak boleh delivery."], "green"),
        ("02  DELIVERY IMMUTABLE", ["Participant Bearer terikat assessment.", "Opsi diacak, public IDs opaque.", "Refresh memakai snapshot yang sama.", "Key / solution tidak masuk DTO siswa."], "blue"),
        ("03  RESPONS SERVER", ["Benar = 1; salah = 0; skip = NA.", "Identity, version, scoring dari server.", "Event immutable; retry tanpa duplikasi.", "Server timing dan anomaly flags."], "blue"),
        ("04  CLEANING DAN MATRIKS", ["Satu completed attempt per subject.", "First / last; completion time window.", "Exclude mismatch, invalid, rapid guess.", "Missing tetap NA, tanpa imputasi nol."], "blue"),
        ("05  CTT DAN GATE IRT", ["p / Wilson CI, rest-score D dan r_it.", "KR-20 menggunakan complete cases.", "N, coverage, variasi, connected design.", "Review dimensi, local independence, sampling."], "orange"),
        ("06  RASCH / 2PL / 3PL", ["Regularized marginal likelihood; θ~N(0,1).", "Gauss-Hermite; missing tanpa likelihood.", "a / b / c, EAP, uncertainty, information.", "Convergence, bounds, infit/outfit, Q3.", "Gate gagal: CTT + waiting status."], "purple"),
        ("07  SNAPSHOT ADVISORY", ["Immutable policy / matrix / sample hashes.", "Populasi, family, grade, time window.", "CTT / IRT tetap empirical difficulty.", "Disagreement hanya review flag.", "Research-only; bukan gold otomatis."], "purple"),
        ("08  KEPUTUSAN AHLI", ["Authenticated expert + CSRF + rationale.", "Retain / revise / quarantine append-only.", "Hold delivery pada versi terkait.", "Exclude held version dari freeze berikutnya.", "Label awal dan histori tetap tersimpan."], "green"),
        ("09  VERSIONING / TRAINING", ["Revisi → versi baru → review manusia.", "Freeze gold baru, group-aware split.", "IndoBERT ordinal grade-aware + calibration.", "Technical gates + approval model.", "Respons siswa bukan training text."], "green"),
    ]
    positions = [(100, 300), (1340, 300), (2580, 300), (2580, 850), (1340, 850), (100, 850),
                 (100, 1400), (1340, 1400), (2580, 1400)]
    width, height = 1160, 450
    for (title, lines, color), (x, y) in zip(content, positions, strict=True):
        diagram.card(x, y, width, height, title, lines, color)
    for (x, y), (nx, ny) in zip(positions, positions[1:]):
        if y == ny:
            start = (x + width + 10, y + height / 2) if nx > x else (x - 10, y + height / 2)
            end = (nx - 10, ny + height / 2) if nx > x else (nx + width + 10, ny + height / 2)
        else:
            start, end = (x + width / 2, y + height + 10), (nx + width / 2, ny - 10)
        diagram.arrow(start, end)
    diagram.rectangle(100, 1940, 3640, 130, "#e6edf7")
    diagram.text(135, 1958, "FastAPI + MongoDB gold/auth + SQLite pilot + NumPy/SciPy • API 2.1.0 • Dokumen 07 / 27", 36, bold=True)
    diagram.text(135, 2011, "Minimum proyek: Rasch 100×5; 2PL 300×10; 3PL 1000×20. Tidak ada pooling, auto-label, CAT atau equating.", 31)
    diagram.save("23_EMPIRICAL_VALIDATION_FEEDBACK_FLOW")


def ai_detail():
    diagram = Diagram("INDOBERT ORDINAL GRADE-AWARE DAN BLIND LLM N=3",
                      "Protokol terbaru: label blind dikunci sebelum comparison; gold manusia tetap otoritas label")
    left = [
        ("A1  SNAPSHOT DAN SPLIT", ["Gold manusia atau silver research: provenance terpisah.", "Hash lock; group-aware 70/15/15; source / stimulus / duplicate family."]),
        ("A2  SERIALIZER DAN ENCODER", ["Stem, stimulus, metadata grade, opsi, solusi/visual terverifikasi.", "Serializer tunggal; IndoBERT shared encoder + LoRA query/value."]),
        ("A3  TIGA HEAD", ["Head 1: knowing / applying / reasoning; Head 2: empat knowledge classes.", "Head 3: cumulative ordinal + grade embedding + ordered cutpoints."]),
        ("A4  LOSS DAN CALIBRATION", ["Multiclass + ordinal loss; train-only class weights; anti-collapse.", "Validation temperature / confidence+entropy; per-grade bila support cukup."]),
        ("A5  PACKAGING DAN PROMOTION", ["Adapter / heads / tokenizer / label map / hashes / version / metrics.", "Gold + technical gates + approval; silver tetap research-only, API 503."]),
    ]
    right = [
        ("B1  INPUT BLIND", ["Gemini menerima soal, grade, rubrik, key / solution / image evidence.", "Tanpa prediksi IndoBERT, agent difficulty, vote lain atau target distribution."]),
        ("B2  TIGA INITIAL RUNS", ["Tiga panggilan terpisah; structured JSON dan bukti/rationale ringkas.", "Hidden chain-of-thought tidak disimpan; schema/error status diperiksa."]),
        ("B3  VOTING DAN ADJUDICATION", ["Hanya 3–0 diterima langsung sebagai silver advisory.", "2–1, abstain, key/visual/content conflict → adjudikasi AI terpisah."]),
        ("B4  CHECKPOINT DAN AUDIT", ["Resume memakai run sukses; failure/history tidak menjadi label.", "Audit hash mengunci checkpoint; boundary/data gate sebelum expansion."]),
        ("B5  COMPARISON OFFLINE", ["Prediksi dibuat setelah blind labels terkunci; join disagreement offline.", "Tidak ada anchored review baru; agreement bukan confidence atau human gold."]),
    ]
    for column, cards, color in [(100, left, "blue"), (2000, right, "purple")]:
        for index, (title, body) in enumerate(cards):
            diagram.card(column, 300 + index * 310, 1740, 265, title, body, color)
            if index < 4:
                diagram.arrow((column + 870, 575 + index * 310), (column + 870, 600 + index * 310))
    diagram.rectangle(100, 1910, 3640, 170, "#e5f3ee")
    diagram.text(140, 1930, "CTT / IRT → review manusia → retain / revise / quarantine → versi/gold baru → training terkontrol", 39, bold=True, color="green")
    diagram.text(140, 1995, "Parallel-v1 / conditioned-difficulty-v1 adalah legacy ablation. Jawaban siswa mentah dan label AI bukan gold training.", 34)
    diagram.save("24_INDOBERT_FINETUNING_LLM_REASONING_DETAIL")


if __name__ == "__main__":
    empirical()
    ai_detail()
    print("Rendered current empirical and ordinal/blind-LLM diagrams as SVG / PNG / JPG")
