"""Verify only arithmetic expressions whose meaning can be extracted unambiguously."""
from __future__ import annotations

import re
from typing import Any

import sympy


EXPRESSION = re.compile(r"(?i)\bhitung(?:lah)?(?:\s+hasil\s+dari)?\s+([0-9()+*/.\-\s]{3,80})")
NUMBER = re.compile(r"^-?\d+(?:\.\d+)?$")


def verify_arithmetic(question_text: str, options: list[dict[str, str]], answer_spec: dict[str, Any]) -> dict[str, Any]:
    match = EXPRESSION.search(question_text)
    if not match:
        return {"status": "unsupported", "method": "sympy_arithmetic_v1"}
    expression = match.group(1).strip()
    if not expression or not re.fullmatch(r"[0-9()+*/.\-\s]+", expression) or "**" in expression:
        return {"status": "unsupported", "method": "sympy_arithmetic_v1"}
    if any(len(number) > 8 for number in re.findall(r"\d+", expression)):
        return {"status": "unsupported", "method": "sympy_arithmetic_v1"}
    try:
        computed = sympy.sympify(expression, evaluate=True)
        if not computed.is_real or not computed.is_finite:
            return {"status": "unsupported", "method": "sympy_arithmetic_v1"}
        computed_float = float(computed)
    except (SyntaxError, TypeError, ValueError, ZeroDivisionError, sympy.SympifyError):
        return {"status": "unsupported", "method": "sympy_arithmetic_v1"}

    kind = answer_spec.get("kind")
    if kind == "numeric":
        tolerance = float(answer_spec.get("tolerance") or 0)
        verified = abs(computed_float - float(answer_spec["value"])) <= tolerance + 1e-10
    elif kind == "option_ids":
        matching = []
        for option in options:
            text = option["text"].strip().strip("$")
            if NUMBER.fullmatch(text) and abs(float(text) - computed_float) <= 1e-10:
                matching.append(option["id"])
        verified = len(matching) == 1 and matching == answer_spec.get("optionIds")
    else:
        return {"status": "unsupported", "method": "sympy_arithmetic_v1"}
    return {"status": "passed" if verified else "conflict", "method": "sympy_arithmetic_v1", "computedAnswer": computed_float}
