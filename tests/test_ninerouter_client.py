import json

import httpx
import pytest

from app.llm.ninerouter import NineRouterClient, NineRouterError, NineRouterSettings


def _settings(**overrides):
    base = dict(api_key="secret-key", base_url="http://router.test/v1", model="m1")
    base.update(overrides)
    return NineRouterSettings(**base)


def test_key_not_in_repr():
    assert "secret-key" not in repr(_settings())


@pytest.mark.parametrize("field,value", [("api_key", " "), ("model", ""), ("base_url", "router/v1")])
def test_invalid_settings_rejected(field, value):
    with pytest.raises(ValueError):
        _settings(**{field: value})


def test_chat_parses_usage_and_sends_bearer():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["auth"] = request.headers["authorization"]
        seen["path"] = request.url.path
        return httpx.Response(200, json={
            "model": "m1",
            "choices": [{"message": {"content": "siap"}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 7, "completion_tokens": 2},
        })

    client = NineRouterClient(_settings(stream=False), transport=httpx.MockTransport(handler))
    result = client.chat([{"role": "user", "content": "hai"}])
    assert (result.text, result.input_tokens, result.output_tokens) == ("siap", 7, 2)
    assert seen == {"auth": "Bearer secret-key", "path": "/v1/chat/completions"}


def test_http_error_is_wrapped_without_key():
    transport = httpx.MockTransport(lambda r: httpx.Response(429, text="rate limited"))
    client = NineRouterClient(_settings(stream=False), transport=transport)
    with pytest.raises(NineRouterError) as err:
        client.chat([{"role": "user", "content": "hai"}])
    assert "429" in str(err.value) and "secret-key" not in str(err.value)


def test_stream_joins_chunks_and_reads_usage():
    sse = (b': keep-alive\n\n'
           b'data: {"model":"m1","choices":[{"delta":{"content":"si"}}]}\n\n'
           b'data: {"choices":[{"delta":{"content":"ap"},"finish_reason":"stop"}]}\n\n'
           b'data: {"choices":[],"usage":{"prompt_tokens":9,"completion_tokens":3}}\n\n'
           b'data: [DONE]\n\n')
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.content)
        return httpx.Response(200, content=sse, headers={"content-type": "text/event-stream"})

    client = NineRouterClient(_settings(stream=True), transport=httpx.MockTransport(handler))
    result = client.chat([{"role": "user", "content": "hai"}])
    assert (result.text, result.input_tokens, result.output_tokens, result.finish_reason) == ("siap", 9, 3, "stop")
    assert seen["body"]["stream"] is True


def test_stream_http_error_is_wrapped_without_key():
    transport = httpx.MockTransport(lambda r: httpx.Response(503, text="provider down"))
    client = NineRouterClient(_settings(stream=True), transport=transport)
    with pytest.raises(NineRouterError) as err:
        client.chat([{"role": "user", "content": "hai"}])
    assert "503" in str(err.value) and "secret-key" not in str(err.value)


def test_koneksi_putus_diulang_otomatis(monkeypatch):
    monkeypatch.setattr("app.llm.ninerouter.time.sleep", lambda *_: None)
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] < 3:
            raise httpx.ReadError("koneksi diputus", request=request)
        return httpx.Response(200, json={"model": "m1", "choices": [{"message": {"content": "siap"}}]})

    client = NineRouterClient(_settings(stream=False), transport=httpx.MockTransport(handler))
    assert client.chat([{"role": "user", "content": "hai"}]).text == "siap"
    assert calls["n"] == 3


def test_galat_http_tidak_diulang(monkeypatch):
    monkeypatch.setattr("app.llm.ninerouter.time.sleep", lambda *_: None)
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        return httpx.Response(429, text="kuota habis")

    client = NineRouterClient(_settings(stream=False), transport=httpx.MockTransport(handler))
    with pytest.raises(NineRouterError):
        client.chat([{"role": "user", "content": "hai"}])
    assert calls["n"] == 1


def test_menunggu_reset_lalu_berhasil(monkeypatch):
    tidur = []
    monkeypatch.setattr("app.llm.ninerouter.time.sleep", lambda d: tidur.append(d))
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            return httpx.Response(503, text='{"error":{"message":"[x] [403]: HTTP 403 (reset after 1m 30s)"}}')
        return httpx.Response(200, json={"model": "m1", "choices": [{"message": {"content": "siap"}}]})

    client = NineRouterClient(_settings(stream=False), transport=httpx.MockTransport(handler))
    assert client.chat([{"role": "user", "content": "hai"}]).text == "siap"
    assert tidur == [95]


def test_reset_terlalu_lama_tidak_ditunggu(monkeypatch):
    monkeypatch.setattr("app.llm.ninerouter.time.sleep", lambda d: (_ for _ in ()).throw(AssertionError("tidur")))
    transport = httpx.MockTransport(
        lambda r: httpx.Response(503, text='{"error":{"message":"quota (reset after 2h 41m)"}}'))
    client = NineRouterClient(_settings(stream=False), transport=transport)
    with pytest.raises(NineRouterError):
        client.chat([{"role": "user", "content": "hai"}])
