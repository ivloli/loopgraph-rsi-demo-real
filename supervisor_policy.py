"""Versioned supervisor policy used by the real RSI demonstration."""

MAX_RETRIES = 3
SYNTHETIC_FALLBACK = True


def next_action(*, retry_count: int, verification_passed: bool) -> str:
    """Return a bounded action for one verification result."""
    if verification_passed:
        return "complete"
    if retry_count < MAX_RETRIES:
        return "retry"
    if SYNTHETIC_FALLBACK:
        return "synthetic_fallback"
    return "human_gate"
