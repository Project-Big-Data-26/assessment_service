"""Transparent baseline used for demos and as a benchmark, never as a silver label."""
from __future__ import annotations
import re
from app.classification.base import ClassificationPrediction

BLOOM_SIGNALS = {
    "C6": ("rancang", "buat", "susun", "kembangkan", "hasilkan", "ciptakan"),
    "C5": ("evaluasi", "nilai", "kritik", "buktikan", "pertahankan", "rekomendasikan"),
    "C4": ("analisis", "bandingkan", "bedakan", "hubungkan", "temukan kesalahan", "kelompokkan"),
    "C3": ("hitung", "tentukan", "gunakan", "terapkan", "selesaikan", "demonstrasikan"),
    "C2": ("jelaskan", "ringkas", "tafsirkan", "klasifikasikan", "beri contoh"),
    "C1": ("sebutkan", "identifikasi", "definisikan", "tuliskan", "ingat"),
}
KNOWLEDGE_SIGNALS = {
    "metacognitive": ("strategi", "refleksi", "cara berpikir", "periksa kembali", "belajarmu"),
    "procedural": ("langkah", "prosedur", "algoritma", "gunakan rumus", "selesaikan"),
    "conceptual": ("mengapa", "hubungan", "sifat", "konsep", "bandingkan"),
    "factual": ("nama", "simbol", "nilai", "definisi", "sebutkan"),
}

class RuleBasedBaselineClassifier:
    """Auditable lexical/structural baseline for smoke tests and model comparison."""
    version = "pedagogical-baseline-v1"

    def predict(self, question_text: str) -> ClassificationPrediction:
        if not question_text.strip(): raise ValueError("question_text must not be empty")
        lowered = question_text.casefold()
        bloom, bloom_hits = self._first_match(lowered, BLOOM_SIGNALS, "C2")
        knowledge, knowledge_hits = self._first_match(lowered, KNOWLEDGE_SIGNALS, "conceptual")
        reasoning_markers = len(re.findall(r"[,;:]| dan | kemudian |jelaskan|buktikan|bandingkan", lowered))
        formula_count = len(re.findall(r"\$[^$]+\$|\\[a-zA-Z]+|[=<>]", question_text))
        word_count = len(question_text.split())
        score = word_count / 35 + reasoning_markers * 0.32 + formula_count * 0.18 + (int(bloom[1]) - 1) * 0.17
        difficulty = "Hard" if score >= 2.0 else "Medium" if score >= 0.9 else "Easy"
        return ClassificationPrediction(
            bloom_level=bloom, bloom_confidence=min(0.88, 0.56 + 0.08 * len(bloom_hits)),
            knowledge_dimension=knowledge, knowledge_confidence=min(0.84, 0.54 + 0.08 * len(knowledge_hits)),
            difficulty_level=difficulty, difficulty_confidence=min(0.8, 0.58 + abs(score - 1.35) * 0.08),
            model_version=self.version, status="baseline_advisory", prediction_source="rules_baseline",
            rationale=(f"Bloom signals: {', '.join(bloom_hits) or 'default contextual prior'}", f"Knowledge signals: {', '.join(knowledge_hits) or 'default contextual prior'}", f"Structural score={score:.2f}; words={word_count}; formulas={formula_count}; markers={reasoning_markers}"),
        )

    @staticmethod
    def _first_match(text: str, groups: dict[str, tuple[str, ...]], default: str) -> tuple[str, list[str]]:
        for label, signals in groups.items():
            hits = [signal for signal in signals if signal in text]
            if hits: return label, hits
        return default, []
