"""Render alur pipeline generate soal latihan via 9Router sebagai SVG (dapat diedit) dan PNG (untuk slide).

Dijalankan dari mana saja dengan Python repo ini. Tidak mengakses provider, database, atau model.
Status tiap tahap harus mengikuti kenyataan kode: ubah STATUS pada Card di bawah bila tahap berubah.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "API_DOCUMENTATION"
STEM = "38_EXERCISE_9ROUTER_PIPELINE_FLOW"
W, H = 3200, 1800

COLORS = {
    "bg": "#F3F6FB", "ink": "#142D46", "muted": "#496077", "line": "#7891A9", "white": "#FFFFFF",
    "ok": "#08786D", "ok_soft": "#E4F4EF",          # sudah jalan
    "wip": "#A35F0B", "wip_soft": "#FFF2DA",        # sedang dioptimalkan
    "plan": "#7650A5", "plan_soft": "#F0EBF8",      # rencana
    "gw": "#2266A4", "gw_soft": "#E9F2FB",          # 9Router
}
STATUS = {"ok": "SUDAH JALAN", "wip": "SEDANG DISEMPURNAKAN", "plan": "RENCANA"}


@dataclass(frozen=True)
class Card:
    num: str
    title: str
    status: str
    desc: str
    bullets: tuple[str, ...]


CARDS = (
    Card("1", "SIAPKAN BAHAN", "ok", "Mengumpulkan bahan untuk membuat soal satu subbab.", (
        "Isi buku siswa untuk subbab tersebut.",
        "Soal pretest sebagai contoh.",
        "Soal yang sudah ada, supaya tidak sama.",
        "Aturan cara menulis soal.")),
    Card("2", "AI PENULIS", "ok", "AI pertama menulis soal, 5 soal setiap kali menulis.", (
        "Sebagian soal meniru contoh buku (angka diganti), sebagian dibuat baru.",
        "Menulis pertanyaan, jawaban benar, 3 pilihan salah, dan pembahasan.",
        "Pilihan salah dibuat dari kesalahan yang sering dilakukan siswa.",
        "Urutan pilihan A-D diacak oleh program.")),
    Card("3", "PERIKSA OTOMATIS", "ok", "Program memeriksa aturan. Soal yang tidak lolos ditulis ulang.", (
        "Jumlah soal dan format sudah benar.",
        "Kalimat contoh benar-benar ada di buku.",
        "Tidak sama dengan soal yang sudah ada.",
        "Tingkat kesulitan sesuai levelnya.")),
    Card("4", "AI PENGERJA", "ok", "AI kedua mengerjakan soal tanpa melihat kunci jawaban.", (
        "Mengerjakan sendiri dan menulis cara hitungnya.",
        "Jawabannya dibandingkan dengan kunci.",
        "Jawaban beda: soal ditandai untuk diperiksa orang, tidak dibuang.",
        "Hasil perbandingan disimpan.")),
    Card("5", "TENTUKAN KESULITAN", "wip", "Tim validasi menentukan seberapa sulit tiap soal.", (
        "Tiap soal diberi tingkat kognitif dan skor.",
        "Soal yang kurang meyakinkan diperiksa oleh orang.",
        "Nanti dikoreksi lagi dari jawaban siswa.",
        "Caranya masih disempurnakan.")),
    Card("6", "SIMPAN KE DATABASE", "plan", "Soal masuk database MongoDB dengan status menunggu.", (
        "Belum tampil ke siswa.",
        "Dicatat AI mana yang membuat dan hasil pengecekannya.",
        "Tampil ke siswa setelah diperiksa orang.",
        "Aman dijalankan ulang tanpa menggandakan soal.")),
)


class Canvas:
    def __init__(self) -> None:
        self.img = Image.new("RGB", (W, H), COLORS["bg"])
        self.draw = ImageDraw.Draw(self.img)
        self.svg: list[str] = []
        self._fonts: dict[tuple[int, bool], ImageFont.FreeTypeFont] = {}

    def font(self, size: int, bold: bool = False):
        key = (size, bold)
        if key not in self._fonts:
            for cand in (Path("C:/Windows/Fonts") / ("segoeuib.ttf" if bold else "segoeui.ttf"),
                         Path("/usr/share/fonts/truetype/dejavu") / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")):
                if cand.exists():
                    self._fonts[key] = ImageFont.truetype(str(cand), size)
                    break
            else:
                self._fonts[key] = ImageFont.load_default()
        return self._fonts[key]

    @staticmethod
    def c(name: str) -> str:
        return COLORS.get(name, name)

    def text(self, x, y, value, size=28, *, bold=False, color="ink", anchor="start"):
        font = self.font(size, bold)
        width = font.getlength(value)
        px = x - width / 2 if anchor == "middle" else x
        self.draw.text((px, y), value, fill=self.c(color), font=font, anchor="ls")
        self.svg.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Segoe UI,DejaVu Sans,sans-serif" '
                        f'font-size="{size}" font-weight="{700 if bold else 400}" fill="{self.c(color)}">{escape(value)}</text>')

    def rect(self, x, y, w, h, fill, *, border=None, radius=22, width=3):
        self.draw.rounded_rectangle((x, y, x + w, y + h), radius, fill=self.c(fill),
                                    outline=self.c(border) if border else None, width=width)
        stroke = f' stroke="{self.c(border)}" stroke-width="{width}"' if border else ""
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{self.c(fill)}"{stroke}/>')

    def wrap(self, value: str, width: int, size: int, bold=False) -> list[str]:
        lines, line = [], ""
        for word in value.split():
            trial = f"{line} {word}".strip()
            if self.font(size, bold).getlength(trial) > width and line:
                lines.append(line)
                line = word
            else:
                line = trial
        return lines + ([line] if line else [])

    def paragraph(self, x, y, value, width, size, *, bold=False, color="ink", lead=1.32) -> int:
        for ln in self.wrap(value, width, size, bold):
            self.text(x, y, ln, size, bold=bold, color=color)
            y += round(size * lead)
        return y

    def polyline(self, pts, *, color="line", width=5, dashed=False, arrow=True):
        col = self.c(color)
        if dashed:
            for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
                length = math.hypot(x2 - x1, y2 - y1)
                n = max(1, int(length // 22))
                for i in range(n):
                    if i % 2 == 0:
                        a, b = i / n, min(1, (i + 1) / n)
                        self.draw.line((x1 + (x2 - x1) * a, y1 + (y2 - y1) * a, x1 + (x2 - x1) * b, y1 + (y2 - y1) * b),
                                       fill=col, width=width)
        else:
            self.draw.line(pts, fill=col, width=width, joint="curve")
        d = " ".join(f"{x},{y}" for x, y in pts)
        dash = ' stroke-dasharray="14 10"' if dashed else ""
        self.svg.append(f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="{width}"{dash} stroke-linejoin="round"/>')
        if arrow:
            (x1, y1), (x2, y2) = pts[-2], pts[-1]
            ang = math.atan2(y2 - y1, x2 - x1)
            size = 22
            tri = [(x2, y2), (x2 - size * math.cos(ang - 0.45), y2 - size * math.sin(ang - 0.45)),
                   (x2 - size * math.cos(ang + 0.45), y2 - size * math.sin(ang + 0.45))]
            self.draw.polygon(tri, fill=col)
            self.svg.append(f'<polygon points="{" ".join(f"{px:.1f},{py:.1f}" for px, py in tri)}" fill="{col}"/>')

    def pill(self, x, y, label, fg, bg, size=24, *, pad=22, bold=True) -> float:
        w = self.font(size, bold).getlength(label) + pad * 2
        self.rect(x, y, w, size + 24, bg, border=fg, radius=(size + 24) // 2, width=2)
        self.text(x + pad, y + size + 6, label, size, bold=bold, color=fg)
        return w

    def save(self):
        self.img.save(OUT / f"{STEM}.png", optimize=True)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
               f'<rect width="{W}" height="{H}" fill="{COLORS["bg"]}"/>' + "".join(self.svg) + "</svg>")
        (OUT / f"{STEM}.svg").write_text(svg, encoding="utf-8")


CARD_W, CARD_H, GAP, X0, CARD_Y = 450, 650, 60, 100, 610


def cx(i: int) -> int:
    return X0 + i * (CARD_W + GAP)


def draw_card(cv: Canvas, i: int, card: Card):
    x, y = cx(i), CARD_Y
    fg, soft = card.status, f"{card.status}_soft"
    cv.rect(x, y, CARD_W, CARD_H, "white", border=fg, width=4)
    cv.rect(x, y, CARD_W, 18, fg, radius=9)
    cv.text(x + 28, y + 85, card.num, 54, bold=True, color=fg)
    cv.text(x + 85, y + 78, card.title, 30, bold=True)
    cv.pill(x + 28, y + 108, STATUS[card.status], fg, soft, 20, pad=16)
    yy = cv.paragraph(x + 28, y + 195, card.desc, CARD_W - 56, 27, bold=True, color="muted")
    yy += 10
    for b in card.bullets:
        cv.text(x + 28, yy, "•", 26, bold=True, color=fg)
        yy = cv.paragraph(x + 56, yy, b, CARD_W - 84, 25)
        yy += 8


def main() -> None:
    cv = Canvas()
    cv.text(100, 120, "Alur Pembuatan Soal Latihan Otomatis dengan 9Router", 64, bold=True)
    cv.paragraph(100, 175, "Untuk setiap subbab dan tingkat (mudah / sedang / sulit): bahan dari buku, AI menulis soal, "
                 "diperiksa program dan AI kedua, lalu masuk database.", 2900, 30, color="muted")

    # pemicu
    cv.rect(100, 260, 450, 150, "plan_soft", border="plan", width=3)
    cv.text(125, 318, "JADWAL 00.00  atau  manual", 29, bold=True, color="plan")
    cv.paragraph(125, 360, "Jalan tengah malam saat pengguna sepi.", 400, 24, color="muted")
    cv.rect(610, 260, 450, 150, "plan_soft", border="plan", width=3)
    cv.text(635, 318, "DAFTAR TUGAS", 29, bold=True, color="plan")
    cv.paragraph(635, 360, "1 tugas = 1 subbab + 1 tingkat. Bisa dilanjutkan bila terputus.", 400, 24, color="muted")
    cv.polyline([(550, 335), (610, 335)], color="plan")
    cv.pill(1120, 305, "RENCANA", "plan", "plan_soft", 22)
    cv.text(1120, 395, "Belum dibangun: saat ini tugas dijalankan manual satu per satu.", 25, color="muted")
    cv.polyline([(830, 410), (830, 485), (cx(0) + CARD_W // 2, 485), (cx(0) + CARD_W // 2, CARD_Y)], color="plan")

    for i, card in enumerate(CARDS):
        draw_card(cv, i, card)
        if i < len(CARDS) - 1:
            cv.polyline([(cx(i) + CARD_W + 4, CARD_Y + 330), (cx(i + 1) - 4, CARD_Y + 330)], width=6)

    # putaran ulang validator -> generate
    cv.polyline([(cx(2) + CARD_W // 2, CARD_Y), (cx(2) + CARD_W // 2, 560), (cx(1) + CARD_W // 2, 560),
                 (cx(1) + CARD_W // 2, CARD_Y - 4)], color="wip", dashed=True)
    cv.text((cx(1) + cx(2) + CARD_W) // 2, 540, "soal ditolak → AI menulis ulang", 24,
            bold=True, color="wip", anchor="middle")

    # 9Router
    band_y = 1430
    cv.rect(100, band_y, 3000, 130, "gw_soft", border="gw", width=4)
    cv.text(130, band_y + 55, "9ROUTER", 38, bold=True, color="gw")
    cv.text(130, band_y + 100, "Satu pintu untuk memakai banyak AI (Gemini, GPT, dan lainnya). "
            "AI yang dipakai bisa diganti lewat pengaturan, tanpa mengubah program.", 27, color="muted")
    for i, label in ((1, "AI PENULIS · Gemini 3.8 Flash"), (3, "AI PENGERJA · GPT-6 Luna")):
        px = cx(i) + CARD_W // 2
        cv.polyline([(px, band_y), (px, CARD_Y + CARD_H + 4)], color="gw", dashed=True, arrow=False)
        w = cv.font(25, True).getlength(label) + 44
        cv.rect(px - w / 2, CARD_Y + CARD_H + 25, w, 56, "white", border="gw", radius=28, width=3)
        cv.text(px, CARD_Y + CARD_H + 62, label, 25, bold=True, color="gw", anchor="middle")

    # hasil uji + legenda
    cv.rect(100, 1610, 1850, 150, "white", border="line", width=3)
    cv.text(130, 1660, "HASIL UJI PERTAMA  ·  Kelas 9, Bab 2, Subbab A, tingkat mudah", 28, bold=True)
    cv.text(130, 1705, "15 dari 15 soal lolos pemeriksaan otomatis (± 2-4 menit)   |   AI pengerja menjawab sama dengan kunci: 15 dari 15", 27)
    cv.text(130, 1745, "AI pengerja bisa menangkap salah hitung, tetapi bukan fakta yang salah bila kedua AI sama-sama keliru: tetap perlu diperiksa orang.",
            24, color="muted")
    cv.text(2000, 1650, "KETERANGAN STATUS", 25, bold=True, color="muted")
    x = 2000
    for key in ("ok", "wip", "plan"):
        w = cv.pill(x, 1675, STATUS[key], key, f"{key}_soft", 22)
        x += w + 20
    cv.save()
    print("ditulis:", OUT / f"{STEM}.svg", "dan", OUT / f"{STEM}.png")


if __name__ == "__main__":
    main()
