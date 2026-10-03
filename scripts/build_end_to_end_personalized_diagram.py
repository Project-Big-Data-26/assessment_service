"""Render the documented end-to-end flow as editable SVG and a matching JPG.

Run from any directory with the repository's Python environment. No provider,
database, student data, browser, or model artifact is accessed.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "API_DOCUMENTATION"
STEM = "28_END_TO_END_PERSONALIZED_ASSESSMENT_FLOW"
WIDTH = 4800
ROW_Y = 510
CARD_X = (170, 1310, 2450, 3590)
CARD_WIDTH, CARD_HEIGHT = 1040, 600
PANEL_HEIGHT = CARD_HEIGHT + 180
ROW_STEP = PANEL_HEIGHT + 30

COLORS = {
    "background": "#F3F6FB", "ink": "#142D46", "muted": "#496077",
    "line": "#7891A9", "white": "#FFFFFF",
    "I": "#08786D", "I_soft": "#E4F4EF",
    "L": "#2266A4", "L_soft": "#E9F2FB",
    "R": "#7650A5", "R_soft": "#F0EBF8",
    "T": "#A35F0B", "T_soft": "#FFF2DA",
}
STATUS = {"I": "KODE TERSEDIA", "L": "WORKFLOW LOKAL", "R": "RISET / ADVISORY", "T": "TARGET PENGEMBANGAN"}


@dataclass(frozen=True)
class Card:
    id: str
    title: str
    status: str
    description: str
    body: tuple[str, ...]


@dataclass(frozen=True)
class Phase:
    title: str
    subtitle: str
    footer: str
    cards: tuple[Card, ...]
    sequential: bool = True


PHASES = (
    Phase("A  |  SOURCE, EXTRACTION AND QUALIFICATION", "Mengubah soal dari buku menjadi data terstruktur, memeriksa kelengkapannya, lalu menyimpan versi yang dapat ditelusuri.",
          "A4 → B1. Candidate belum menjadi label silver sebelum melewati blind review dan audit.", (
        Card("A1", "SOURCE MANIFEST", "L", "Mencatat asal soal dan sidik berkas (hash), agar setiap hasil ekstraksi dapat ditelusuri ke sumbernya.", ("PDF siswa dan guru; tabel bab prasyarat.", "Kelas, bab, halaman, sumber eksternal dan hash.", "Konversi ke Markdown, indeks dan gambar.", "Referensi sumber dipertahankan untuk setiap item.")),
        Card("A2", "AGENTIC EXTRACTION", "L", "Agen AI memisahkan soal dari buku menjadi data terstruktur, termasuk pilihan jawaban dan bukti kunci.", ("Workflow Claude Code dijalankan per bab.", "Stem, stimulus, opsi dan bukti kunci diekstrak.", "Gambar ditranskripsi dan solusi minimal dibuat.", "Difficulty agen 1–5 hanya heuristik staging.")),
        Card("A3", "VALIDATION AND REPORT", "L", "Memeriksa format dan isi ekstraksi, lalu membuat laporan error, warning, status, dan provenance sebelum ekspor.", ("Schema, verbatim, angka, kunci dan media diperiksa.", "ERROR memblokir; warning disimpan untuk audit.", "Report mencatat alasan, status dan provenance item.", "Candidate bank diekspor setelah gate terpenuhi.")),
        Card("A4", "CANONICAL VERSION", "I", "Memberi identitas dan versi tetap pada soal yang lolos pemeriksaan, agar revisi tidak menimpa riwayat lama.", ("Import idempotent dan qualification konten.", "Simpan questionId, versionId dan contentHash.", "Kelas, opsi, transkrip visual dan lineage dicatat.", "Kunci atau visual yang tidak lengkap ditahan.")),
    )),
    Phase("B  |  BLIND LLM SILVER LABELING", "Membentuk label silver dari tiga penilaian awal Gemini yang terpisah, menyelesaikan konflik lewat AI, lalu mengunci hasil audit.",
          "B4 menghasilkan silver terkunci. Agreement N=3 adalah self-consistency, bukan confidence terkalibrasi.", (
        Card("B1", "INITIAL BLIND PROMPT", "L", "Prompt awal memuat soal, kelas, rubrik, kunci, solusi, opsi, dan gambar tanpa prediksi model atau vote lain.", ("Pilot dipilih deterministik dan distratifikasi.", "Schema output memaksa label, evidence dan rationale.", "Label agen, prediksi model dan distribusi disembunyikan.", "Bukti kurang menghasilkan abstain, bukan label default.")),
        Card("B2", "THREE INITIAL RUNS", "R", "Gemini menilai soal dalam tiga panggilan terpisah; hasil awal tiap panggilan tidak melihat keputusan panggilan lain.", ("Tiga panggilan menghasilkan JSON per head.", "Status konten dan kunci disertai bukti ringkas.", "Schema, error provider dan retry diperiksa.", "Checkpoint dapat dilanjutkan; run gagal bukan label.")),
        Card("B3", "VOTING AND AI ADJUDICATION", "R", "Menerima kesepakatan penuh yang bebas masalah, lalu meminta AI meninjau hasil yang berbeda atau bermasalah.", ("Keputusan 3–0 tanpa blocker diterima sebagai silver.", "Hasil 2–1, abstain atau konflik masuk adjudikasi.", "Riwayat initial runs tetap dipertahankan.", "Hidden chain-of-thought tidak disimpan.")),
        Card("B4", "AUDIT AND SILVER FREEZE", "R", "Memeriksa kelengkapan label dan mengunci dataset dengan hash sebelum hasilnya dibandingkan dengan IndoBERT.", ("Kelengkapan dan boundary distribution diaudit.", "SHA-256 mengunci checkpoint dan provenance.", "Item tidak eligible dipisahkan dari training set.", "Prediksi model baru dibandingkan setelah lock.")),
    )),
    Phase("C  |  INDOBERT TRAINING AND RESEARCH INFERENCE", "Melatih IndoBERT dari silver terkunci untuk memprediksi karakteristik soal; model dan penggunaannya tetap berstatus riset.",
          "C4 → D1 untuk pilot silver terisolasi. /v2/classify publik tetap 503 selama guard research-only aktif.", (
        Card("C1", "SILVER SNAPSHOT AND SPLIT", "I", "Membagi dataset silver tetap menjadi data latih, validasi, dan uji, tanpa membocorkan soal sekeluarga antarbagian.", ("Gabungkan snapshot silver kelas yang lolos audit.", "Split group-aware 70 / 15 / 15 secara deterministik.", "Source, stimulus dan duplicate family tidak bocor.", "Class support dan frozen test gate diperiksa.")),
        Card("C2", "JSON-TO-TEXT AND THREE HEADS", "I", "JSON valid diubah menjadi teks kanonis sesuai manifest, ditokenisasi, lalu dibaca IndoBERT oleh tiga kepala prediksi.", ("Fitur teks: metadata, stimulus, soal, opsi dan visual.", "Solution dan KKO masuk hanya jika representation memilihnya.", "IndoBERT + LoRA menghasilkan representasi [CLS].", "Difficulty ordinal memakai grade embedding terpisah.")),
        Card("C3", "TRAINING AND CALIBRATION", "I", "Melatih model dan menyesuaikan probabilitasnya dengan data validasi, agar prediksi dan tingkat keyakinan dapat dievaluasi.", ("Loss multiclass dan cumulative ordinal digunakan.", "Anti-collapse dan weakest-head macro-F1 diperiksa.", "Temperature, confidence dan entropy dari validation.", "Kalibrasi per kelas hanya jika support cukup.")),
        Card("C4", "RESEARCH ARTIFACT", "R", "Mengemas model, konfigurasi, dan hasil evaluasi sebagai artefak berversi yang hanya dapat dipakai melalui mode riset.", ("Adapter, heads, tokenizer dan manifest dikemas.", "Checksum, metrik dan calibration disimpan.", "Artifact yang belum lolos gate tetap researchOnly.", "Inference riset membutuhkan opt-in eksplisit.")),
    )),
    Phase("D  |  SILVER PILOT DELIVERY", "Menjalankan pilot silver qualified: peserta menerima soal melalui sesi, sedangkan server menjaga versi, jawaban, dan penilaian.",
          "D1 registry silver tersedia; D2-D4 menyediakan jalur siswa dan scoring server.", (
        Card("D1", "SILVER SNAPSHOT REGISTRY", "I", "Mendaftarkan snapshot silver qualified ke SQLite dan menghubungkannya ke assessment siswa.", ("Verifikasi hash rows dan expansionRows.", "Wajib bukti AI, kunci, solusi dan versi.", "Cocokkan grade dan subjectTrack.", "Service key tidak membutuhkan akun pelabel.")),
        Card("D2", "PARTICIPANT AND SESSION", "I", "Membuat akses peserta dan sesi miliknya. Komponen ini dapat dipakai pada pilot silver melalui registry D1.", ("Operator membuat Bearer token per assessment.", "SubjectHash dibentuk dari populasi dan kode peserta.", "Start idempotent; ownership dan expiry diperiksa.", "Akun siswa longitudinal masih target.")),
        Card("D3", "IMMUTABLE DELIVERY", "I", "Mengirim soal tanpa kunci dan membekukan susunan opsi untuk satu percobaan, sehingga muat ulang tetap konsisten.", ("Item fixed-form dikirim sesuai blueprint silver.", "Opsi diacak dan public ID dibuat opaque.", "Refresh mempertahankan delivery dan mapping.", "Kunci, solusi dan reasoning tidak dikirim.")),
        Card("D4", "SERVER-SCORED RESPONSE", "I", "Server mencocokkan jawaban dengan versi soal yang diterima siswa dan menyimpan skor tanpa menggandakan kiriman ulang.", ("Identity dan correctness dihitung oleh server.", "Benar 1, salah 0 dan skip null / NA.", "Retry payload sama tidak membuat event baru.", "Session selesai setelah semua item dijawab / skip.")),
    )),
    Phase("E  |  CTT, IRT AND EMPIRICAL EVIDENCE", "Mengolah jawaban siswa menjadi statistik tes klasik (CTT) dan, jika syarat data terpenuhi, estimasi teori respons butir (IRT).",
          "E2 gate gagal → E4 dengan CTT dan status IRT waiting. E4 → F1 untuk feedback silver terkendali.", (
        Card("E1", "SESSION CLEANING AND MATRIX", "I", "Menyaring sesi selesai dan menyusun matriks siswa–versi soal; jawaban kosong tetap dibedakan dari jawaban salah.", ("Pilih satu completed attempt per subject.", "Window memakai completion time; attempt tidak dicampur.", "Event invalid, mismatch dan rapid guess dikeluarkan.", "Matriks siswa × versi memakai 0, 1 atau NA.")),
        Card("E2", "CTT AND READINESS GATES", "I", "Menghitung statistik tes klasik dan memeriksa kecukupan data; analisis IRT menunggu jika syarat belum terpenuhi.", ("Hitung p, Wilson CI, discrimination dan KR-20.", "Periksa sample, outcomes, coverage dan desain terhubung.", "Missing tetap NA dan tidak diubah menjadi nol.", "Assumption review diperlukan sebelum fit IRT.")),
        Card("E3", "IRT FIT AND DIAGNOSTICS", "R", "Mengestimasi karakteristik soal dan kemampuan siswa pada skala lokal, lalu memeriksa kecocokan model terhadap data.", ("Rasch 100×5; 2PL 300×10; 3PL 1000×20.", "Regularized MML dan quadrature pada theta N(0,1).", "Estimasi a, b, c, EAP, posterior SD dan information.", "Periksa convergence, bounds, infit, outfit dan Q3.")),
        Card("E4", "IMMUTABLE EMPIRICAL SNAPSHOT", "R", "Menyimpan hasil analisis bersama jejak data dan kebijakan, agar hasil yang sama dapat direproduksi dan diaudit.", ("Policy, matrix, sample hash dan exclusion disimpan.", "Input identik direplay; perubahan membuat snapshot baru.", "Feedback otomatis menyimpan actorType system.", "EAP dibatasi untuk akses internal.")),
    )),
    Phase("F  |  CONTROLLED SILVER FEEDBACK", "Memakai hasil analisis untuk menandai masalah, menahan versi berisiko, dan membentuk silver baru tanpa mengubah riwayat lama.",
          "F2/F3 → B1 untuk blind silver batch baru; F4 → C1 untuk challenger model berikutnya.", (
        Card("F1", "EMPIRICAL ROUTING", "R", "Menandai soal yang perlu ditinjau berdasarkan respons siswa; statistik menjadi bukti pemeriksaan, bukan label pengganti.", ("Bandingkan intended dan empirical difficulty.", "Tandai sample lemah, misfit dan diskriminasi negatif.", "Periksa kunci, distraktor, populasi dan konten.", "Flag adalah evidence, bukan label pengganti.")),
        Card("F2", "AUTOMATIC HOLD POLICY", "I", "Sistem menahan versi yang memiliki kandidat masalah kualitas berdasarkan feedback empiris.", ("Screen menyimpan keputusan otomatis.", "Sample lemah meminta respons tambahan.", "Hold menolak create, next item dan response.", "Freeze dengan assessment DB mengecualikan hold.")),
        Card("F3", "NEW SILVER BATCH", "L", "Mengirim soal yang direvisi ke penilaian blind dan audit baru, sehingga pembaruan silver memiliki riwayat tersendiri.", ("Konten yang dikoreksi mendapat versi baru.", "Jalankan kembali blind N=3 dan adjudikasi AI.", "Audit dan hash baru wajib sebelum digunakan.", "Checkpoint dan snapshot lama tetap immutable.")),
        Card("F4", "CHALLENGER MODEL CYCLE", "L", "Melatih calon model pengganti dari silver baru dan membandingkan hasil evaluasinya dengan model sebelumnya.", ("Bangun snapshot silver versi berikutnya.", "Train, calibrate dan evaluate challenger.", "Bandingkan dengan baseline dan artifact sebelumnya.", "Tidak ada auto-retrain atau auto-publish.")),
    )),
    Phase("G  |  PER-STUDENT PERSONALIZATION", "Target: memakai riwayat tiap siswa untuk mengenali kebutuhan belajar, memilih soal berikutnya, dan memperbarui profil bertahap.",
          "G4 → G2/G3 membentuk loop latihan. Selector adaptif terpisah dari fixed-form pilot.", (
        Card("G1", "LEARNER IDENTITY AND PROFILE", "T", "Rancangan profil berversi yang menghubungkan akun siswa dengan riwayat jawaban dan bukti belajar miliknya.", ("Akun longitudinal, sekolah, tenant dan izin akses.", "Link berizin ke subjectHash dan riwayat session.", "Respons D4 dan estimasi E4 memakai release policy.", "Versi profil, evidence dan uncertainty disimpan.")),
        Card("G2", "TOPIC-LEVEL DIAGNOSIS", "T", "Rancangan diagnosis untuk mengenali kekuatan dan kesulitan tiap topik, disertai jumlah bukti dan ketidakpastian.", ("Gunakan pretest, kelas, topik dan prasyarat.", "Mastery sementara disertai jumlah bukti dan uncertainty.", "Theta global belum membuktikan mastery tiap topik.", "Data sedikit menghasilkan status provisional.")),
        Card("G3", "CONSTRAINED ITEM SELECTOR", "T", "Rancangan pemilih soal yang menyaring kelayakan terlebih dahulu, lalu menyesuaikan tantangan dengan kebutuhan siswa.", ("Pool hanya memuat silver eligible dan non-held.", "Filter objective, kelas, prasyarat dan exposure.", "Tingkat tantangan mengikuti profil individual.", "Policy version dan alasan pemilihan dicatat.")),
        Card("G4", "ADAPTIVE PRACTICE LOOP", "T", "Rancangan siklus latihan: jawaban dinilai server, bukti belajar terkumpul, lalu profil dan pilihan soal diperbarui.", ("Scoring tetap dilakukan oleh server.", "Profil diperbarui setelah beberapa evidence.", "Feedback latihan dipisahkan dari measurement.", "Perubahan profil tidak mengubah label silver item.")),
    )),
    Phase("H  |  PRODUCT AND OPERATIONS", "Target pengembangan paralel: pendampingan belajar, laporan individual, tes adaptif, serta layanan yang siap dioperasikan.",
          "G4 → H1; G1/G2 → H2; released calibration + online selector → H3; shared backend → H4.", (
        Card("H1", "PRACTICE AND TUTORING", "T", "Rancangan pendampingan belajar dengan penjelasan dan petunjuk sesuai kesulitan siswa, memakai konten tervalidasi.", ("Penjelasan mengikuti evidence miskonsepsi.", "Konten dan solusi yang digunakan harus tervalidasi.", "Hint dan assisted attempt dicatat terpisah.", "Setiap varian menjalani validasi dan versioning.")),
        Card("H2", "INDIVIDUAL REPORTING", "T", "Rancangan laporan perkembangan per siswa yang menjelaskan capaian, kebutuhan belajar, dan batas kepastian hasil.", ("Progress dan gap per topik disertai uncertainty.", "Akses siswa dan guru dibatasi ownership.", "Raw percentage paket berbeda tidak langsung setara.", "EAP lokal bukan percentile lintas populasi.")),
        Card("H3", "CAT AND ADAPTIVE TESTING", "T", "Rancangan tes yang memilih soal dari bank terkalibrasi sesuai estimasi kemampuan terkini dan aturan penghentian.", ("Bank terkalibrasi membutuhkan release eksplisit.", "Online theta, information dan stopping policy dibangun.", "Blueprint, exposure dan dependencies dikendalikan.", "CAT, equating, linking dan DIF belum tersedia.")),
        Card("H4", "PRODUCTION OPERATIONS", "T", "Rancangan layanan operasional dengan akses pengguna, penyimpanan bersama, pemantauan, dan pemulihan data.", ("Bangun UI siswa, durable auth dan token lifecycle.", "Gunakan shared transactional backend dan queue.", "Tambahkan audit, monitoring, backup dan retention.", "Validasi operasional memakai data nyata.")),
    ), sequential=False),
)

HEIGHT = ROW_Y + len(PHASES) * ROW_STEP + 950


class Renderer:
    def __init__(self):
        self.image = Image.new("RGB", (WIDTH, HEIGHT), COLORS["background"])
        self.draw = ImageDraw.Draw(self.image)
        self.backgrounds: list[str] = []
        self.edges: list[str] = []
        self.foreground: list[str] = []
        self.bounds: dict[str, tuple[int, int, int, int]] = {}
        self.graph_edges: list[dict] = []
        self.measurements: list[dict] = []

    @staticmethod
    def font(size: int, bold: bool = False):
        candidates = (
            Path("C:/Windows/Fonts") / ("segoeuib.ttf" if bold else "segoeui.ttf"),
            Path("/usr/share/fonts/truetype/dejavu") / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"),
        )
        for candidate in candidates:
            if candidate.exists():
                return ImageFont.truetype(str(candidate), size)
        raise RuntimeError("Install Segoe UI or DejaVu Sans to reproduce the diagram")

    def text(self, x, y, value, size=30, *, bold=False, color="ink", layer=None):
        fill = COLORS.get(color, color)
        font = self.font(size, bold)
        width = font.getlength(value)
        if x < 0 or x + width > WIDTH - 12 or y - size < 0 or y > HEIGHT - 12:
            raise ValueError(f"text outside canvas: {value}")
        self.draw.text((x, y), value, fill=fill, font=font, anchor="ls")
        (self.foreground if layer is None else layer).append(
            f'<text x="{x}" y="{y}" font-family="Segoe UI,DejaVu Sans,sans-serif" '
            f'font-size="{size}" font-weight="{700 if bold else 400}" fill="{fill}">{escape(value)}</text>'
        )

    def rect(self, x, y, width, height, fill, *, border=None, radius=22, dashed=False, layer=None):
        self.draw.rounded_rectangle((x, y, x + width, y + height), radius=radius, fill=fill,
                                    outline=None if dashed else border, width=3)
        if dashed and border:
            for sx in range(int(x + radius), int(x + width - radius), 28):
                self.draw.line((sx, y, min(sx + 15, x + width - radius), y), fill=border, width=3)
                self.draw.line((sx, y + height, min(sx + 15, x + width - radius), y + height), fill=border, width=3)
            for sy in range(int(y + radius), int(y + height - radius), 28):
                self.draw.line((x, sy, x, min(sy + 15, y + height - radius)), fill=border, width=3)
                self.draw.line((x + width, sy, x + width, min(sy + 15, y + height - radius)), fill=border, width=3)
        (self.foreground if layer is None else layer).append(
            f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" '
            f'fill="{fill}" stroke="{border or fill}" stroke-width="3"'
            + (' stroke-dasharray="15 13"' if dashed else '') + '/>'
        )

    def wrap(self, value, width, size, bold=False):
        result, current = [], ""
        for word in value.split():
            if self.font(size, bold).getlength(word) > width:
                raise ValueError(f"unbreakable text: {word}")
            trial = f"{current} {word}".strip()
            if self.font(size, bold).getlength(trial) > width:
                result.append(current)
                current = word
            else:
                current = trial
        if current:
            result.append(current)
        return result

    def card(self, card: Card, x: int, y: int):
        if card.id in self.bounds:
            raise ValueError(f"duplicate node: {card.id}")
        self.bounds[card.id] = (x, y, CARD_WIDTH, CARD_HEIGHT)
        accent = COLORS[card.status]
        self.foreground.append(f'<g id="node-{card.id}" data-status="{card.status}">')
        self.rect(x, y, CARD_WIDTH, CARD_HEIGHT, COLORS["white"], border=accent, dashed=card.status == "T")
        self.rect(x + 24, y + 20, 74, 48, accent, radius=12)
        self.text(x + 36, y + 54, card.id, 25, bold=True, color="white")
        badge = STATUS[card.status]
        badge_width = self.font(22, True).getlength(badge) + 30
        self.rect(x + CARD_WIDTH - badge_width - 25, y + 20, badge_width, 48,
                  COLORS[f"{card.status}_soft"], radius=12)
        self.text(x + CARD_WIDTH - badge_width - 10, y + 52, badge, 22, bold=True, color=card.status)
        title_lines = self.wrap(card.title, CARD_WIDTH - 60, 35, True)
        for index, line in enumerate(title_lines):
            self.text(x + 30, y + 117 + index * 45, line, 35, bold=True)
        cursor = y + 164 + (len(title_lines) - 1) * 45
        description_lines = self.wrap(card.description, CARD_WIDTH - 60, 28)
        if not description_lines or len(description_lines) > 3:
            raise ValueError(f"description must occupy 1–3 lines: {card.id}")
        self.foreground.append('<g class="node-description" lang="id">')
        for line in description_lines:
            self.text(x + 30, cursor, line, 28, color="muted")
            cursor += 38
        self.foreground.append("</g>")
        cursor += 14
        self.foreground.append('<g class="node-points">')
        line_count = 0
        for value in card.body:
            lines = self.wrap(value, CARD_WIDTH - 92, 29)
            self.draw.ellipse((x + 32, cursor - 15, x + 41, cursor - 6), fill=accent)
            self.foreground.append(f'<circle cx="{x+36.5}" cy="{cursor-10.5}" r="4.5" fill="{accent}"/>')
            for line in lines:
                self.text(x + 58, cursor, line, 29)
                cursor += 40
                line_count += 1
            cursor += 12
        if cursor > y + CARD_HEIGHT - 12:
            raise ValueError(f"card overflow: {card.id} ({cursor-y}px)")
        self.measurements.append({"id": card.id, "descriptionLines": len(description_lines),
                                  "bodyLines": line_count, "bottomSpace": round(y + CARD_HEIGHT - cursor)})
        self.foreground.append("</g></g>")

    def route(self, source, target, points, *, color="line", dashed=False, role="flow"):
        if source not in self.bounds or target not in self.bounds:
            raise ValueError(f"undefined connector: {source} -> {target}")
        fill = COLORS[color]
        # All routes are orthogonal and stay in the dedicated gutters.
        for start, end in zip(points, points[1:]):
            if start[0] != end[0] and start[1] != end[1]:
                raise ValueError("non-orthogonal route")
            for node_id, (x, y, width, height) in self.bounds.items():
                if start[0] == end[0]:
                    blocked = x + 2 < start[0] < x + width - 2 and max(min(start[1], end[1]), y + 2) < min(max(start[1], end[1]), y + height - 2)
                else:
                    blocked = y + 2 < start[1] < y + height - 2 and max(min(start[0], end[0]), x + 2) < min(max(start[0], end[0]), x + width - 2)
                if blocked:
                    raise ValueError(f"connector {source}->{target} crosses card {node_id}")
            if dashed:
                length = abs(end[0] - start[0]) + abs(end[1] - start[1])
                for offset in range(0, int(length), 32):
                    stop = min(offset + 18, length)
                    dx = 0 if start[0] == end[0] else (1 if end[0] > start[0] else -1)
                    dy = 0 if start[1] == end[1] else (1 if end[1] > start[1] else -1)
                    self.draw.line((start[0] + dx * offset, start[1] + dy * offset,
                                    start[0] + dx * stop, start[1] + dy * stop), fill=fill, width=5)
            else:
                self.draw.line((start, end), fill=fill, width=5)
        sx, sy = points[-2]
        ex, ey = points[-1]
        angle = math.atan2(ey - sy, ex - sx)
        base = (ex - 22 * math.cos(angle), ey - 22 * math.sin(angle))
        polygon = ((ex, ey), (base[0] - 10 * math.sin(angle), base[1] + 10 * math.cos(angle)),
                   (base[0] + 10 * math.sin(angle), base[1] - 10 * math.cos(angle)))
        self.draw.polygon(polygon, fill=fill)
        data = " ".join(f'{"M" if index == 0 else "L"} {x} {y}' for index, (x, y) in enumerate(points))
        self.edges.append(f'<path data-source="{source}" data-target="{target}" data-role="{role}" d="{data}" '
                          f'fill="none" stroke="{fill}" stroke-width="5" stroke-linejoin="round"'
                          + (' stroke-dasharray="18 14"' if dashed else '') + f' marker-end="url(#arrow-{color})"/>')
        self.graph_edges.append({"source": source, "target": target, "role": role, "dashed": dashed})

    def right(self, node):
        x, y, w, h = self.bounds[node]
        return x + w, y + h // 2

    def left(self, node):
        x, y, _, h = self.bounds[node]
        return x, y + h // 2

    def top(self, node):
        x, y, w, _ = self.bounds[node]
        return x + w // 2, y

    def bottom(self, node):
        x, y, w, h = self.bounds[node]
        return x + w // 2, y + h

    def next_row(self, source, target, *, color="line", dashed=False):
        start, end = self.bottom(source), self.left(target)
        gutter = start[1] + 67
        # Enter at the left edge, keeping the phase heading/subtitle unobscured.
        self.route(source, target, (start, (start[0], gutter), (135, gutter), (135, end[1]), end),
                   color=color, dashed=dashed)

    def left_branch(self, source, target, *, color="I", dashed=False, rail=90, role="branch"):
        start, end = self.bottom(source), self.left(target)
        gutter = start[1] + 77
        self.route(source, target, (start, (start[0], gutter), (rail, gutter), (rail, end[1]), end),
                   color=color, dashed=dashed, role=role)

    def right_branch(self, source, target, *, color="R", dashed=False, role="branch"):
        start, end = self.right(source), self.top(target)
        gutter = end[1] - 22
        self.route(source, target, (start, (4750, start[1]), (4750, gutter), (end[0], gutter), end),
                   color=color, dashed=dashed, role=role)

    def save(self):
        markers = "".join(
            f'<marker id="arrow-{key}" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="6" markerHeight="6" '
            f'orient="auto-start-reverse"><path d="M 0 1 L 11 6 L 0 11 Z" fill="{COLORS[key]}"/></marker>'
            for key in ("line", "I", "R", "T")
        )
        graph = {"schemaVersion": "end-to-end-diagram-v1", "date": "2026-10-02", "apiVersion": "2.2.0",
                 "nodes": [{"id": card.id, "status": card.status, "title": card.title,
                            "description": card.description, "descriptionLanguage": "id"}
                           for phase in PHASES for card in phase.cards],
                 "edges": self.graph_edges}
        svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
               '<title id="title">Nalar: alur teknis end-to-end dan personalisasi per siswa</title>',
               '<desc id="desc">32 tahap dengan judul Inggris, deskripsi Indonesia sebelum poin teknis: ekstraksi, label silver blind, training IndoBERT, pilot silver terisolasi, psikometrik, feedback silver, dan target personalisasi siswa.</desc>',
               '<metadata>' + escape(json.dumps(graph, ensure_ascii=False)) + '</metadata>',
               '<defs>' + markers + '</defs>',
               f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS["background"]}"/>',
               *self.backgrounds, *self.edges, *self.foreground, '</svg>']
        OUT.mkdir(parents=True, exist_ok=True)
        svg_path = OUT / f"{STEM}.svg"
        jpg_path = OUT / f"{STEM}.jpg"
        svg_path.write_text("\n".join(svg), encoding="utf-8")
        self.image.save(jpg_path, quality=95, subsampling=0, optimize=True)
        return {"svg": str(svg_path), "jpg": str(jpg_path), "pixels": [WIDTH, HEIGHT],
                "nodes": len(self.bounds), "edges": len(self.graph_edges),
                "minimumCardBottomSpace": min(item["bottomSpace"] for item in self.measurements)}


def build():
    renderer = Renderer()
    renderer.text(150, 145, "NALAR  |  SILVER END-TO-END FLOW", 82, bold=True)
    renderer.text(150, 214, "Dari sumber soal ke silver, model, respons siswa, bukti empiris dan personalisasi", 42, color="muted")
    renderer.text(150, 278, "Baseline kode: API 2.2.0  •  2 Oktober 2026  •  Jalur aktual dan ekstensi target diberi status berbeda", 35, color="muted")
    x = 150
    for status in STATUS:
        value = f"{status}  {STATUS[status]}"
        width = renderer.font(26, True).getlength(value) + 54
        renderer.rect(x, 326, width, 60, COLORS[f"{status}_soft"], border=COLORS[status], radius=14,
                      dashed=status == "T")
        renderer.text(x + 23, 366, value, 26, bold=True, color=status)
        x += width + 40
    renderer.text(150, 446, "Panah solid = alur tersedia / lokal; orange putus-putus = target; judul Inggris dan seluruh poin berbahasa Indonesia.", 31, color="muted")

    for row, phase in enumerate(PHASES):
        y = ROW_Y + row * ROW_STEP
        renderer.rect(118, y, 4564, PANEL_HEIGHT, COLORS["white"], border="#DDE5EE", radius=28, layer=renderer.backgrounds)
        renderer.text(154, y + 55, phase.title, 43, bold=True)
        renderer.text(154, y + 97, phase.subtitle, 28, color="muted")
        for x, card in zip(CARD_X, phase.cards, strict=True):
            renderer.card(card, x, y + 132)
        renderer.text(154, y + PANEL_HEIGHT - 7, phase.footer, 25, bold=True,
                      color="T" if row >= 6 else "muted")

    for phase in PHASES:
        if phase.sequential:
            for source, target in zip(phase.cards, phase.cards[1:]):
                target_flow = source.status == "T" or target.status == "T"
                renderer.route(source.id, target.id, (renderer.right(source.id), renderer.left(target.id)),
                               color="T" if target_flow else "line", dashed=target_flow)
    renderer.next_row("A4", "B1", color="R")
    for source, target, color, role in (
        ("D4", "D3", "line", "next_item_until_completed"),
        ("E2", "E4", "R", "waiting_without_irt_fit"),
    ):
        start, end = renderer.bottom(source), renderer.bottom(target)
        gutter = start[1] + 12
        renderer.route(source, target, (start, (start[0], gutter), (end[0], gutter), end),
                       color=color, role=role)
    renderer.next_row("B4", "C1", color="R")
    renderer.next_row("C4", "D1", color="T", dashed=True)
    renderer.next_row("D4", "E1")
    renderer.next_row("E4", "F1", color="R")
    renderer.left_branch("F3", "B1", rail=48, role="new_blind_silver_cycle")
    renderer.left_branch("F4", "C1", rail=65, role="next_silver_model_cycle")
    renderer.right_branch("D4", "G1", color="T", dashed=True, role="future_individual_response_link")
    renderer.left_branch("E4", "G1", color="T", dashed=True, role="future_released_calibration_link")
    start, end = renderer.bottom("G4"), renderer.bottom("G2")
    gutter = start[1] + 12
    renderer.route("G4", "G2", (start, (start[0], gutter), (end[0], gutter), end),
                   color="T", dashed=True, role="future_practice_profile_update")

    footer_y = ROW_Y + len(PHASES) * ROW_STEP + 70
    renderer.rect(150, footer_y, 4500, 690, "#E6EDF6", border="#CCD8E6", radius=28)
    renderer.text(190, footer_y + 66, "BOUNDARY, STORAGE DAN SYARAT VALIDITAS", 43, bold=True)
    notes = (
        "Silver: blind LLM N=3 + adjudikasi AI + audit hash. Delivery qualified memakai provenance ai_silver; model tunduk gate teknis.",
        "Registry silver dan qualification tersedia; grade/track, source evidence dan checksum tetap wajib.",
        "SQLite lokal menyimpan assessment, peserta, session, delivery, response dan snapshot; MongoDB tetap menyimpan candidate/version bila dipakai.",
        "p CTT = performa populasi; b IRT = parameter item lokal; theta = estimasi individual lokal; intendedDifficulty = label awal relatif kelas.",
        "Grade conditioning berbeda dari personalisasi: profil siswa dan selector adaptif tidak mengganti label silver item secara otomatis.",
        "Calibration release, online scoring, CAT, mastery per topik, linking, DIF, varian, UI dan multi-tenant memerlukan validasi tersendiri.",
        "R1: F3 → B1 untuk blind silver baru. R2: F4 → C1 untuk challenger model. R3: G4 → G2/G3 untuk loop latihan target.",
        "Referensi utama: dokumen 21 / 24 / 25 / 27. Detail lengkap dan boundary implementasi ada pada Markdown dokumen 28.",
    )
    cursor = footer_y + 130
    for note in notes:
        for line in renderer.wrap(note, 4400, 29):
            renderer.text(190, cursor, line, 29)
            cursor += 41
        cursor += 16
    if cursor > footer_y + 690 - 15:
        raise ValueError(f"footer overflow: {cursor-footer_y}")
    renderer.text(150, HEIGHT - 80, f"SVG vektor editable + JPG {WIDTH} × {HEIGHT}  •  Dibangun lokal tanpa data pribadi siswa", 30, color="muted")
    return renderer.save()


if __name__ == "__main__":
    print(json.dumps(build(), ensure_ascii=False, indent=2))
