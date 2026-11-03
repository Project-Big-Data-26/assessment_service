"""Conservative LaTeX transport repairs; never evaluate or rewrite mathematics."""
import re
from functools import lru_cache

POLICY_VERSION = "latex-presentation-v1"
# Restrict transport repair to recognizable TeX commands. A real \\ row
# separator, ordinary backslashes, code, and prose are preserved.
COMMANDS = ("left", "right", "frac", "dfrac", "tfrac", "sqrt", "times", "cdot", "div", "pm", "mp",
    "le", "leq", "ge", "geq", "ne", "neq", "equiv", "approx", "sim", "simeq", "in", "notin",
    "subset", "subseteq", "supset", "supseteq", "cup", "cap", "emptyset", "varnothing", "infty",
    "pi", "theta", "alpha", "beta", "gamma", "delta", "Delta", "lambda", "mu", "sigma", "omega",
    "sin", "cos", "tan", "cot", "sec", "csc", "arcsin", "arccos", "arctan", "log", "ln", "exp",
    "lim", "to", "rightarrow", "sum", "prod", "int", "iint", "oint", "partial", "nabla",
    "begin", "end", "text", "textrm", "textbf", "mathrm", "mathbf", "mathbb", "mathcal",
    "operatorname", "displaystyle", "overline", "underline", "bar", "vec", "hat", "dot",
    "underbrace", "overbrace", "binom", "dbinom", "tbinom", "choose", "circ", "degree",
    "ldots", "cdots", "vdots", "ddots", "dots", "quad", "qquad", "mid", "vert", "lvert", "rvert",
    "langle", "rangle", "lceil", "rceil", "lfloor", "rfloor", "perp", "parallel", "angle")
KNOWN = "(?:" + "|".join(sorted(COMMANDS, key=len, reverse=True)) + ")(?![A-Za-z])"
DOUBLE_COMMAND = re.compile(r"(?<!\\)(\\{2,})(?=(" + KNOWN + r"))")
SPACE_COMMAND = re.compile(r"(?<!\\)\\[ \t]+(" + KNOWN + r")")
MATH = re.compile(r"(?<!\\)\$\$(.+?)(?<!\\)\$\$|(?<!\\)\$(?!\$)((?:\\.|[^$])+?)(?<!\\)\$|\\\[(.+?)\\\]|\\\((.+?)\\\)", re.S)


@lru_cache(maxsize=100000)
def repair_math(tex):
    original = tex
    # Three slashes before a command inside an environment can mean a genuine
    # row separator plus a command. Do not flatten that sequence.
    in_environment = bool(re.search(r"\\+begin\{", tex))
    def collapse(match):
        count = len(match.group(1))
        return "\\" * 3 if in_environment and count == 3 else "\\"
    tex = DOUBLE_COMMAND.sub(collapse, tex)
    tex = SPACE_COMMAND.sub(lambda m: "\\" + m.group(1), tex)
    for broken, restored in (("\right", r"\right"), ("\x0crac", r"\frac"),
                              ("\x08egin", r"\begin"), ("\times", r"\times"),
                              ("\x0bert", r"\vert"), ("\nabla", r"\nabla"), ("\x07pprox", r"\approx")):
        tex = tex.replace(broken, restored)
    # A stripped carriage return can leave 'ight)' after a real \left(.
    if r"\left" in tex and len(re.findall(r"\\left\b", tex)) > len(re.findall(r"\\right\b", tex)):
        tex = re.sub(r"(?<![A-Za-z\\])ight(?=[)\]}.|])", lambda m: r"\right", tex)
    return tex


@lru_cache(maxsize=100000)
def normalize_text(text):
    if not isinstance(text, str):
        return text
    # Preserve already valid delimiters and normalize each math span once.
    result, position = [], 0
    for match in MATH.finditer(text):
        result.append(_outside(text[position:match.start()]))
        result.append(_replace_span(match))
        position = match.end()
    result.append(_outside(text[position:]))
    return "".join(result)


def _outside(text):
    if "`" in text:
        return text  # Never rewrite code examples.
    candidate = text.strip().strip("$").strip()
    if re.search(r"\\+(?:frac|dfrac|tfrac|sqrt|left|right|pi|cos|sin|tan)\b", candidate):
        without_commands = re.sub(r"\\+[A-Za-z]+", "", candidate)
        words = re.findall(r"[A-Za-z]{2,}", without_commands)
        if not words or all(word in {"sin", "cos", "tan", "log", "ln"} for word in words):
            # A standalone formula option (possibly with an orphan dollar).
            return text[:len(text)-len(text.lstrip())] + "$" + repair_math(candidate) + "$" + text[len(text.rstrip()):]
    # For prose wrap complete command groups, not surrounding Indonesian text.
    # Fractions/radicals have explicit groups, so their boundaries are unambiguous.
    pattern = re.compile(r"(?<!\\)\\(?:frac|dfrac|tfrac|sqrt|pi)\b")
    result, cursor = [], 0
    for match in pattern.finditer(text):
        if match.start() < cursor:
            continue
        command = match.group()[1:]
        end = match.end()
        needed = 2 if command in {"frac", "dfrac", "tfrac"} else 1 if command == "sqrt" else 0
        valid = True
        for _ in range(needed):
            while end < len(text) and text[end].isspace():
                end += 1
            if end >= len(text) or text[end] != "{":
                valid = False
                break
            depth = 0
            while end < len(text):
                char = text[end]
                if char == "{" and (end == 0 or text[end-1] != "\\"):
                    depth += 1
                elif char == "}" and text[end-1] != "\\":
                    depth -= 1
                end += 1
                if depth == 0:
                    break
            if depth:
                valid = False
                break
        if not valid:
            continue
        start = match.start()
        prefix = re.search(r"(?<![\w])[-+]?\d+(?:[.,]\d+)?[ \t]*$", text[cursor:start])
        if prefix:
            start = cursor + prefix.start()
        result.append(text[cursor:start])
        result.append("$" + repair_math(text[start:end]) + "$")
        cursor = end
    result.append(text[cursor:])
    return "".join(result)


def _replace_span(match):
    for index, delimiters in ((1, ("$$", "$$")), (2, ("$", "$")), (3, (r"\[", r"\]")), (4, (r"\(", r"\)"))):
        if match.group(index) is not None:
            return delimiters[0] + repair_math(match.group(index)) + delimiters[1]
    return match.group(0)


def math_spans(text):
    return [(next(value for value in match.groups() if value is not None),
             match.group(1) is not None or match.group(3) is not None) for match in MATH.finditer(text)]


DISPLAY_KEYS = {"soal_text", "pertanyaan", "pertanyaan_text", "question_text", "questionText", "stem", "stimulus",
    "text", "teks", "alasan", "jawaban_benar", "alasan_benar", "pembahasan", "correct_answer",
    "verifiedMinimalSolution", "visualTranscript", "deskripsi_gambar", "reasoningSummary", "rationale", "explanation"}


def normalize_document(document):
    """Copy display fields only; preserve IDs, keys, labels, paths and evidence hashes."""
    if isinstance(document, list):
        return [normalize_document(value) for value in document]
    if isinstance(document, dict):
        return {key: normalize_text(value) if key in DISPLAY_KEYS and isinstance(value, str)
                else normalize_document(value) if isinstance(value, (dict, list)) else value
                for key, value in document.items()}
    return document
