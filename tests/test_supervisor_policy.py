from supervisor_policy import MAX_RETRIES, SYNTHETIC_FALLBACK, next_action


def test_passed_verification_completes():
    assert next_action(retry_count=0, verification_passed=True) == "complete"


def test_failed_verification_retries_within_bound():
    assert next_action(retry_count=MAX_RETRIES - 1, verification_passed=False) == "retry"


def test_v1_uses_synthetic_fallback_after_retry_bound():
    assert SYNTHETIC_FALLBACK is True
    assert next_action(retry_count=MAX_RETRIES, verification_passed=False) == "synthetic_fallback"
