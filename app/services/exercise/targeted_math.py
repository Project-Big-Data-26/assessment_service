"""Exact certificates for the second, curriculum-specific local authoring pass."""
from dataclasses import dataclass
from itertools import product
import sympy as s
from .replenishment_math import numeric, text, m, pair, rp
from app.presentation.latex import normalize_text


@dataclass
class Authored:
    draft: object
    level: str
    steps: int
    rationale: str
    certificate: dict


def system(variables, equations, query, conditions=()):
    return {"type": "symbolic_constraints", "variables": variables,
            "equations": [str(v) for v in equations], "query": str(query),
            "positive": [str(v) for v in conditions]}


def finite(variables, ranges, constraints, query, aggregate="max"):
    return {"type": "finite_constraints", "variables": variables, "ranges": ranges,
            "equations": [str(v) for v in constraints], "query": str(query), "aggregate": aggregate}


def solve_certificate(cert):
    if cert['type']=='finite_probability':
        variables=s.symbols(' '.join(cert['variables']),real=True)
        if not isinstance(variables,tuple):variables=(variables,)
        names=dict(zip(cert['variables'],variables));names.update(Eq=s.Eq,Mod=s.Mod,And=s.And)
        event=s.sympify(cert['event'],locals=names);condition=s.sympify(cert['condition'],locals=names)
        numerator=denominator=0
        for values in product(*(range(a,b+1) for a,b in cert['ranges'])):
            sub=dict(zip(variables,values))
            if bool(condition.subs(sub)):
                denominator+=1;numerator+=bool(event.subs(sub))
        assert denominator
        return s.Rational(numerator,denominator)
    variables = s.symbols(" ".join(cert["variables"]), real=True)
    if not isinstance(variables, tuple): variables = (variables,)
    names = dict(zip(cert["variables"], variables))
    names.update(sqrt=s.sqrt, pi=s.pi, Max=s.Max, Min=s.Min, Abs=s.Abs,
                 binomial=s.binomial, log=s.log, sin=s.sin, cos=s.cos)
    equations = [s.sympify(v, locals=names) for v in cert["equations"]]
    query = s.sympify(cert["query"], locals=names)
    if cert["type"] == "finite_constraints":
        results = []
        for values in product(*(range(a,b+1) for a,b in cert["ranges"])):
            substitution = dict(zip(variables, values))
            if all(s.simplify(eq.subs(substitution)) == 0 for eq in equations):
                results.append(s.simplify(query.subs(substitution)))
        assert results, "No feasible interpretation"
        op = cert["aggregate"]
        return {"max": max, "min": min, "sum": sum, "count": len}[op](results)
    solutions = s.solve(equations, variables, dict=True)
    positive = [s.sympify(v, locals=names) for v in cert["positive"]]
    values = []
    for solution in solutions:
        evaluated=[s.simplify(v.subs(solution)) for v in positive]
        if not all(v.is_real is True and v>0 for v in evaluated): continue
        value = s.simplify(query.subs(solution))
        assert not value.free_symbols and value.is_real is True and value.is_finite is True
        values.append(value)
    assert values and all(s.simplify(v-values[0]) == 0 for v in values), "Query is not uniquely determined"
    return values[0]


def checked(q, value, solution, family, level, cert, steps=None, rationale=None, wrong=None):
    value = s.sympify(value)
    actual = solve_certificate(cert)
    assert s.simplify(actual-s.sympify(value)) == 0, (family, actual, value)
    steps = steps or {"easy":1,"medium":3,"hard":5}[level]
    rationale = rationale or {
        "easy":"Satu konsep dan satu prosedur langsung dengan data lengkap.",
        "medium":"Menghubungkan dua sampai tiga langkah rutin yang saling bergantung.",
        "hard":"Menyusun model dari beberapa kendala, menentukan parameter tersembunyi, lalu mengevaluasi solusi atau batas yang relevan."}[level]
    if wrong is None:
        wrong = [1-value, value**2, value/2] if value.is_number and 0 < value < 1 else [value-1,value+1,2*value] if value.is_Integer else [value/2, value*2, -value]
    draft = numeric(normalize_text(q), value, normalize_text(solution), family, wrong=wrong)
    draft.proof.update(local_certificate=cert, assessed_level=level, dependent_steps=steps,
                       assessment_rationale=rationale, independent_ai_validation="not_requested_local_review")
    return Authored(draft, level, steps, rationale, cert)


def constant(q, value, solution, family, level, steps=None, rationale=None, wrong=None):
    # Use only for direct easy/medium formula application; hard requires a model.
    assert level != "hard"
    z=s.Symbol('z',real=True)
    return checked(q,value,solution,family,level,system(['z'],[z-value],z),steps,rationale,wrong)
