import json
from pathlib import Path
import subprocess

import pytest

from app.presentation.latex import normalize_text, normalize_document, math_spans


@pytest.mark.parametrize("original,expected", [
    ("$" + "\x0crac{5}{100}" + "$", r"$\frac{5}{100}$"),
    ("$x " + "\times" + " 7$", r"$x \times 7$"),
    ("$" + r"\frac{23}{3} " + "\x07pprox 7{,}67$", r"$\frac{23}{3} \approx 7{,}67$"),
    (r"$\\left(2^{-1}+4^{-1}\\right)^{-1}$", r"$\left(2^{-1}+4^{-1}\right)^{-1}$"),
    (r"$\left(\ dfrac{3}{2}ight)^{-2}$", r"$\left(\dfrac{3}{2}\right)^{-2}$"),
    (r"\frac{5}{3}", r"$\frac{5}{3}$"),
    (r"2\sqrt{7}", r"$2\sqrt{7}$"),
    (r"-\frac{1}{4}\cos^4 x + C$", r"$-\frac{1}{4}\cos^4 x + C$"),
    (r"Radian: \frac{3 \pi}{2} dan \frac{\pi}{5}.", r"Radian: $\frac{3 \pi}{2}$ dan $\frac{\pi}{5}$."),
])
def test_repairs_transport_and_missing_math_delimiters(original, expected):
    assert normalize_text(original) == expected
    assert normalize_text(expected) == expected


@pytest.mark.parametrize("text", [
    r"$2^{-1}+4^{-1}=8^{-1}$",  # Wrong mathematical distractor, but valid presentation.
    r"$\left(\frac{3}{2}\right)^{-2}=\frac{4}{9}$",
    r"$$\begin{bmatrix}1 & 2 \\ \frac{1}{2} & 3\end{bmatrix}$$",
    r"$$\begin{cases}x^2 & x>0 \\\frac{x}{2} & x\le 0\end{cases}$$",
    "Harga Rp25.000,00 dan diskon 5%.",
    r"`\frac{1}{2}` is a code example.",
    r"Path C:\folder\data.json",
])
def test_correct_formulas_prose_and_real_matrix_row_separators_stay_unchanged(text):
    assert normalize_text(text) == text


def test_delivery_repair_does_not_mutate_ids_labels_keys_or_source():
    source = {"_id": "same", "jawaban": "B", "contentHash": "a" * 64,
              "cognitive_level": "hard", "options": [{"option_id": "A", "text": "$\x0crac{1}{2}$"}],
              "source_path": r"C:\frac\original.json"}
    before = json.dumps(source)
    fixed = normalize_document(source)
    assert fixed["options"][0]["text"] == r"$\frac{1}{2}$"
    assert {k: v for k, v in fixed.items() if k != "options"} == {k: v for k, v in source.items() if k != "options"}
    assert json.dumps(source) == before


def test_screenshot_style_expressions_render_in_local_katex(tmp_path):
    candidates = [r"$\left(2^{-1}+4^{-1}ight)^{-1}=2+4$",
        r"$2^{3^{2}}=\left(2^{3}ight)^{2}$",
        r"$2^{-1}+4^{-1}=8^{-1}$", r"$\left(\ dfrac{3}{2}ight)^{-2}=\dfrac{4}{9}$"]
    rows = [{"id": i, "tex": tex, "display": display} for i, candidate in enumerate(candidates)
            for tex, display in math_spans(normalize_text(candidate))]
    path = tmp_path / "math.json"
    path.write_text(json.dumps(rows), encoding="utf-8")
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(["node", str(root / "scripts/latex_render_check.cjs"), str(path)],
        check=True, capture_output=True, text=True, encoding="utf-8")
    assert json.loads(result.stdout)["errors"] == []
