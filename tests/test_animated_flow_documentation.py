"""Check pedagogical math against backend recipes and keep source links usable.

These checks do not invoke LLMs, write responses, load models, or fit an artifact.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import shutil
import subprocess

import numpy as np
from numpy.polynomial.hermite import hermgauss
import pytest

from app.classification.v2.calibration import normalized_entropy, softmax
from app.evaluation.psychometrics import wilson_interval
from app.psychometrics.irt import response_probability

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "API_DOCUMENTATION" / "interactive"


@pytest.fixture(scope="module")
def js_results():
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node is needed to verify browser calculator parity")
    program = r"""
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const root = process.argv[1];
const M = require(path.join(root, 'math.js'));
const Q = require(path.join(root, 'quadrature.js'));
const ctx = {window: {}};
vm.createContext(ctx);
['model-stages','pipeline-stages','assessment-stages','feedback-stages','presentation-summary','graph'].forEach(name =>
  vm.runInContext(fs.readFileSync(path.join(root, name+'.js'), 'utf8'), ctx));
const cases = [
  {z:[2,1,0],t:1}, {z:[1000,999,998],t:1},
  {z:[-3,0,4],t:0.05}, {z:[2,1,0],t:2.5},
  {z:[0,0,0,0],t:1}
];
const items = [-1,0,1].map(b=>({a:1,b,c:0}));
let rejected = false;
try { M.softmax([1,2,3],0); } catch { rejected=true; }
const output = {
  cases: cases.map(c => ({...c,p:M.softmax(c.z,c.t),h:M.entropy(M.softmax(c.z,c.t))})),
  wilson: [[80,100],[0,100],[100,100],[5,10]].map(([r,n])=>({r,n,...M.wilson(r,n)})),
  irt: [[0,1,0.5,0],[0.5,1.5,0.5,0.2],[-3,4,5,0.15],[3,0.2,-5,0]].map(v=>({v,...M.irt(...v)})),
  eap: M.eap(items,[1,1,0],Q), prior: M.eap(items,[null,null,null],Q),
  quadrature: Q,
  ordinal: M.ordinal(0,-0.5,Math.log(Math.expm1(2))),
  zeroThreshold: M.route([.8,.15,.05],0,.7,'confidence-entropy-v1'),
  entropyReview: M.route([.8,.15,.05],.7,.3,'confidence-entropy-v1'),
  confidenceOnly: M.route([.8,.15,.05],.7,.3,'confidence-only-v1'),
  stableBands: [M.stableBand({low:.7,high:.9}),M.stableBand({low:.1,high:.3}),M.stableBand({low:.3,high:.7})],
  boundaryLabels: [-1.001,-1,1,1.001].map(M.empiricalDifficulty),
  invalidTemperatureRejected: rejected,
  stages: ['FLOW_MODEL_STAGES','FLOW_PIPELINE_STAGES','FLOW_ASSESSMENT_STAGES','FLOW_FEEDBACK_STAGES'].flatMap(name=>ctx.window[name]),
  graph: ctx.window.FLOW_GRAPH,
  presentation: ctx.window.FLOW_PRESENTATION
};
process.stdout.write(JSON.stringify(output));
"""
    completed = subprocess.run(
        [node, "-e", program, str(ASSETS)], check=True,
        capture_output=True, text=True, encoding="utf-8",
    )
    return json.loads(completed.stdout)


def test_softmax_and_entropy_match_backend_with_extreme_logits(js_results):
    for case in js_results["cases"]:
        probabilities = softmax(np.asarray(case["z"]), case["t"])
        np.testing.assert_allclose(case["p"], probabilities, atol=1e-14)
        assert case["h"] == pytest.approx(normalized_entropy(probabilities), abs=1e-14)
    assert js_results["invalidTemperatureRejected"]


def test_wilson_and_difficulty_boundaries_match_actual_policy(js_results):
    for case in js_results["wilson"]:
        np.testing.assert_allclose(
            [case["low"], case["high"]],
            wilson_interval(case["r"], case["n"]), atol=1e-14,
        )
    assert js_results["stableBands"] == [None, None, "Medium"]
    assert js_results["boundaryLabels"] == ["Easy", "Medium", "Medium", "Hard"]


def test_logistic_information_derivative_and_eap_match_backend(js_results):
    for case in js_results["irt"]:
        theta, a, b, c = case["v"]
        assert case["p"] == pytest.approx(float(response_probability(theta, a, b, c)), abs=1e-14)
        step = 1e-5
        derivative = float((response_probability(theta + step, a, b, c)
                            - response_probability(theta - step, a, b, c)) / (2 * step))
        assert case["derivative"] == pytest.approx(derivative, abs=1e-10)
        assert case["information"] == pytest.approx(
            case["derivative"] ** 2 / max(case["p"] * (1-case["p"]), 1e-12)
        )
    nodes, weights = hermgauss(41)
    np.testing.assert_allclose(js_results["quadrature"]["theta"], nodes * np.sqrt(2), atol=1e-14)
    np.testing.assert_allclose(js_results["quadrature"]["weights"], weights / np.sqrt(np.pi), atol=1e-14)
    assert js_results["eap"]["mean"] == pytest.approx(0.3154347716117324, abs=1e-12)
    assert js_results["eap"]["sd"] == pytest.approx(0.7956298112392798, abs=1e-12)
    assert js_results["prior"]["mean"] == pytest.approx(0, abs=1e-12)
    assert js_results["prior"]["sd"] == pytest.approx(1, abs=1e-12)
    assert js_results["prior"]["answered"] == 0


def test_ordinal_ordering_and_routing_preserve_advisory_boundaries(js_results):
    result = js_results["ordinal"]
    assert result["second"] == pytest.approx(1.5001)
    assert result["q1"] > result["q2"]
    assert sum(result["probabilities"]) == pytest.approx(1)
    assert all(value > 0 for value in result["probabilities"])
    assert js_results["zeroThreshold"]["reasons"] == ["selective_threshold_gate_not_met"]
    assert js_results["entropyReview"]["action"] == "review"
    assert js_results["confidenceOnly"]["action"] == "predict"
    assert js_results["confidenceOnly"]["reviewRequired"] is True


def test_every_stage_has_resolvable_code_sources_and_data(js_results):
    stages = js_results["stages"]
    assert len(stages) >= 60
    assert len({stage["id"] for stage in stages}) == len(stages)
    required = {"id", "phase", "title", "subtitle", "status", "summary", "input",
                "process", "formula", "example", "output", "cautions", "sources", "learning", "latex"}
    for stage in stages:
        assert required.issubset(stage)
        assert stage["status"] in {"implemented", "conditional", "planned"}
        assert stage["sources"]
        assert {"story", "terms", "why", "next"}.issubset(stage["learning"])
        assert stage["learning"]["why"] and stage["learning"]["next"]
        assert all({"term", "meaning", "why"}.issubset(term) for term in stage["learning"]["terms"])
        for source in stage["sources"]:
            assert (ROOT / source["path"]).is_file(), source


def test_all_latex_and_symbol_definitions_render_with_local_katex(js_results):
    cards = [card for stage in js_results["stages"] for card in stage["latex"]]
    cards += [card for slide in js_results["presentation"]["slides"] for card in slide["latex"]]
    expressions = []
    for card in cards:
        assert {"title", "tex", "symbols", "why"}.issubset(card)
        assert card["tex"] and card["why"]
        expressions.append(card["tex"])
        expressions += [symbol["symbol"] for symbol in card["symbols"]]
    for expression in expressions:
        # JavaScript accepts "\m" as "m"; KaTeX then silently renders letters.
        assert not re.search(r"(?<!\\)\b(?:mathrm|mathbf|mathbb|mathcal|operatorname)\s*\{", expression), expression
    program = r"""
const fs = require('node:fs');
const path = require('node:path');
const katex = require(path.join(process.argv[1],'vendor/katex/katex.min.js'));
const expressions = JSON.parse(fs.readFileSync(0,'utf8'));
expressions.forEach(tex => {
  const html = katex.renderToString(tex,{throwOnError:true,strict:'error',trust:false,output:'htmlAndMathml'});
  if (!html.includes('<math')) throw new Error('Accessible MathML is missing');
});
process.stdout.write(String(expressions.length));
"""
    checked = subprocess.run(
        [shutil.which("node"), "-e", program, str(ASSETS)],
        input=json.dumps(expressions), capture_output=True, text=True,
        encoding="utf-8", check=True,
    )
    assert int(checked.stdout) == len(expressions)
    assert len(cards) >= 50


def test_presentation_copy_explains_choices_and_preserves_scope(js_results):
    presentation = js_results["presentation"]
    assert presentation["intro"] and presentation["conclusion"]
    assert len(presentation["slides"]) == 12
    assert len({slide["id"] for slide in presentation["slides"]}) == 12
    for slide in presentation["slides"]:
        assert slide["why"] and slide["speakerNotes"] and slide["terms"]
        assert 3 <= len(slide["bullets"]) <= 4
    assert len(presentation["glossary"]) >= 20
    copy = json.dumps(presentation, ensure_ascii=False)
    for required in ("silver", "snapshot", "confidence", "entropy", "CTT", "IRT", "versi"):
        assert required.lower() in copy.lower()


def test_conditional_graph_covers_stages_and_real_forks(js_results):
    graph = js_results["graph"]
    stage_ids = {stage["id"] for stage in js_results["stages"]}
    assert {node["id"] for node in graph["nodes"]} == stage_ids
    assert len({(node["row"], node["lane"]) for node in graph["nodes"]}) == len(graph["nodes"])
    for edge in graph["edges"]:
        assert edge["from"] in stage_ids and edge["to"] in stage_ids
        assert edge["label"] and edge["kind"] in {"pass", "fork", "fail", "wait", "review", "manual", "optional"}
    edges = {(edge["from"], edge["to"]) for edge in graph["edges"]}
    for run in range(1, 4):
        assert ("model-blind-label", f"model-run-{run}") in edges
        assert (f"model-run-{run}", "model-votes-lock") in edges
    for head in ("cognitive", "knowledge", "difficulty"):
        assert ("model-token-encoder", f"model-head-{head}") in edges
        assert (f"model-head-{head}", "model-three-heads") in edges
    for route in graph["routes"]:
        assert set(route["stages"]) <= stage_ids


def test_error_paths_keep_ai_evidence_bank_labels_and_irt_separate(js_results):
    edges = {(edge["from"], edge["to"]): edge for edge in js_results["graph"]["edges"]}
    required = {
        ("model-import-version", "model-content-hold"): "fail",
        ("model-votes-lock", "model-checkpoint"): "wait",
        ("model-votes-lock", "model-adjudication"): "review",
        ("model-checkpoint", "model-blind-label"): "manual",
        ("model-training-gates", "model-training-blocked"): "fail",
        ("model-inference-gate", "model-serving-blocked"): "fail",
        ("model-inference-gate", "model-abstain"): "fail",
        ("model-entropy-routing", "model-review"): "review",
        ("assessment-silver-gate", "assessment-registration-blocked"): "fail",
        ("assessment-server-score", "assessment-score-rejected"): "fail",
        ("assessment-irt-readiness", "assessment-irt-wait"): "wait",
        ("feedback-system-decision", "feedback-hold"): "fail",
        ("feedback-new-version", "model-rubric-v8"): "manual",
    }
    for pair, kind in required.items():
        assert edges[pair]["kind"] == kind
    assert "3–0" in edges["model-votes-lock", "model-consensus"]["label"]
    assert ("model-consensus", "model-evidence-profile") in edges
    assert ("model-operational-balance", "model-snapshot-split") not in edges
    assert ("model-bank-export", "assessment-irt-initialization") not in edges
    assert ("model-ai-archive", "assessment-silver-gate") in edges
    stages = {stage["id"]: stage for stage in js_results["stages"]}
    assert stages["model-bank-export"]["output"]["originalEvidence"] == "ai_validation_results.json"
    assert stages["assessment-irt-initialization"]["output"]["parameters"] is None
    assert stages["model-serving-blocked"]["output"]["httpStatus"] == 503
    assert stages["model-abstain"]["output"]["action"] == "abstain"


def test_rubric_and_feature_descriptions_match_latest_config(js_results):
    import yaml
    from app.llm.silver import silver_rubric
    stages = {stage["id"]: stage for stage in js_results["stages"]}
    rubric_paths = {source["path"] for source in stages["model-rubric-v8"]["sources"]}
    for grade, track in [(grade, "regular") for grade in range(1, 13)] + [(11, "tl"), (12, "tl")]:
        rubric = silver_rubric(grade, track=track)
        assert "v8" in rubric.version and "v10" in rubric.prompt_version
        assert rubric.path.relative_to(ROOT).as_posix() in rubric_paths
    config = yaml.safe_load((ROOT / "configs/model_v2_config.yaml").read_text(encoding="utf-8"))
    assert config["model"]["grade_embedding_count"] == 12
    assert config["model"]["default_input_representation"] == "solution"
    assert config["model"]["subject_track_feature"] == "tl_text_marker"
    assert stages["model-evidence-profile"]["output"]["profileFields"] == 11
