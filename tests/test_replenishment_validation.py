from scripts.validate_replenishment import retry_delay


def test_short_rate_limit_is_waited_but_daily_quota_is_not_retried():
    cp = {"executionStatus": "blocked_provider_quota_or_rate_limit", "stopReason": {
        "quotaLimits": [{"quotaMetric": "tokens_per_minute", "retryAfterSeconds": "7"}]}}
    assert retry_delay(cp, 0) == 8
    assert retry_delay(cp, 2) is None
    cp["stopReason"]["quotaLimits"][0]["quotaMetric"] = "requests_per_day"
    assert retry_delay(cp, 0) is None


def test_transient_service_retries_are_bounded_and_auth_is_not_retried():
    assert retry_delay({"executionStatus": "blocked_provider_http_503"}, 0) == 15
    assert retry_delay({"executionStatus": "blocked_provider_http_503"}, 1) == 30
    assert retry_delay({"executionStatus": "blocked_provider_http_503"}, 2) is None
    assert retry_delay({"executionStatus": "blocked_provider_configuration"}, 0) is None
