import hashlib
import json

import httpx
import pytest

from app.llm.deepseek import DeepSeekSettings, DeepSeekSilverAdapter
from app.llm.silver import build_silver_prompt
from tests.test_blind_pilot_audit import question
from tests.test_silver_grade import silver_output


def settings(**kwargs):
    return DeepSeekSettings(api_key="private-test-key", live_enabled=True, **kwargs)


def test_valid_json_uses_shared_rubric_and_never_retains_reasoning():
    requests = []
    output = silver_output("Easy")
    def response(request):
        requests.append(json.loads(request.content))
        assert request.headers["Authorization"] == "Bearer private-test-key"
        return httpx.Response(200, json={"id": "ds-1", "choices": [{"finish_reason": "stop", "message": {
            "content": output.model_dump_json(), "reasoning_content": "private-internal-reasoning"}}],
            "usage": {"prompt_tokens": 100, "completion_tokens": 40, "total_tokens": 140,
                      "completion_tokens_details": {"reasoning_tokens": 15}}})
    with httpx.Client(transport=httpx.MockTransport(response)) as client:
        result = DeepSeekSilverAdapter(settings(), client=client).label_once(question("q1"), [], run_index=1, grade=8)
    assert result.status == "success" and result.output == output
    assert result.promptHash == hashlib.sha256(build_silver_prompt(question("q1"), grade=8).encode()).hexdigest()
    assert result.responseHash == hashlib.sha256(output.model_dump_json().encode()).hexdigest()
    assert (result.usage.outputTokens, result.usage.thinkingTokens, result.usage.totalTokens) == (25, 15, 140)
    assert requests[0]["response_format"] == {"type": "json_object"}
    assert requests[0]["thinking"] == {"type": "enabled"}
    assert "SilverDifficultyHead" in requests[0]["messages"][0]["content"]
    assert "private-internal-reasoning" not in result.model_dump_json()
    assert "private-test-key" not in repr(settings())


@pytest.mark.parametrize("code,reason", [(401, "api_key_invalid"), (402, "insufficient_balance"),
    (403, "permission_denied"), (429, None), (503, None), (504, None)])
def test_http_errors_are_sanitized_and_not_retried_in_transport(code, reason):
    calls = []
    def response(request):
        calls.append(True)
        return httpx.Response(code, json={"error": {"message": "private-test-key confidential prompt"}})
    with httpx.Client(transport=httpx.MockTransport(response)) as client:
        result = DeepSeekSilverAdapter(settings(), client=client).label_once(question("q1"), [], run_index=1)
    assert len(calls) == 1 and result.status == "failed"
    assert result.errorCode.endswith(":" + str(code)) and result.providerFailureReason == reason
    assert "private-test-key" not in result.model_dump_json() and "confidential" not in result.model_dump_json()


@pytest.mark.parametrize("content,finish", [("", "stop"), ('{"api_key":"private-test-key"}', "stop"),
    (silver_output("Easy").model_dump_json(), "length")])
def test_empty_invalid_or_truncated_output_cannot_become_a_decision(content, finish):
    def response(request):
        return httpx.Response(200, json={"choices": [{"finish_reason": finish, "message": {"content": content}}],
                                       "usage": {"prompt_tokens": 5, "completion_tokens": 10, "total_tokens": 15}})
    with httpx.Client(transport=httpx.MockTransport(response)) as client:
        result = DeepSeekSilverAdapter(settings(), client=client).label_once(question("q1"), [], run_index=1)
    assert result.status == "failed" and result.output is None and result.usage.totalTokens == 15
    assert "private-test-key" not in result.model_dump_json()


@pytest.mark.parametrize("address", ["http://api.deepseek.com", "https://api.deepseek.com.evil.test",
    "https://api.deepseek.com/?key=secret", "https://user@api.deepseek.com", "https://api.deepseek.com:444"])
def test_credentials_only_go_to_the_official_https_endpoint(address):
    with pytest.raises(ValueError, match="official DeepSeek"):
        settings(api_base_url=address)


def test_missing_key_or_disabled_live_mode_makes_no_request():
    with pytest.raises(ValueError, match="DEEPSEEK_API_KEY"):
        DeepSeekSilverAdapter(DeepSeekSettings())
    with pytest.raises(ValueError, match="DEEPSEEK_LIVE_ENABLED"):
        DeepSeekSilverAdapter(DeepSeekSettings(api_key="private-test-key"))
