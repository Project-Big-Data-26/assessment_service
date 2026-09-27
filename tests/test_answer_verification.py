from app.verification.arithmetic import verify_arithmetic


def test_simple_arithmetic_option_key():
    result = verify_arithmetic("Hitung hasil dari 2 + 3 dengan tepat.", [{"id": "a", "text": "5"}, {"id": "b", "text": "6"}], {"kind": "option_ids", "optionIds": ["a"]})
    assert result["status"] == "passed"
    assert result["computedAnswer"] == 5


def test_wrong_key_conflicts():
    result = verify_arithmetic("Hitung 2 + 3.", [{"id": "a", "text": "5"}, {"id": "b", "text": "6"}], {"kind": "option_ids", "optionIds": ["b"]})
    assert result["status"] == "conflict"


def test_numeric_answer_without_options():
    result = verify_arithmetic("Hitung hasil dari 2 + 3.", [], {"kind": "numeric", "value": 5, "tolerance": 0})
    assert result["status"] == "passed"


def test_word_problem_abstains():
    result = verify_arithmetic("Hitung luas trapesium dengan sisi 10 dan 16.", [], {"kind": "numeric", "value": 78})
    assert result["status"] == "unsupported"
