from dataclasses import dataclass

@dataclass(frozen=True)
class SolveRequest:
    task_id: str
    origin: str
    challenge_type: str
    authorized: bool
    attempt: int = 0
    timeout_seconds: int = 45

SUPPORTED = {"recaptcha_v2", "recaptcha_v3", "cloudflare_turnstile", "image_to_text"}

def authorize(req: SolveRequest) -> tuple[bool, str]:
    if not req.authorized: return False, "authorization_required"
    if not req.origin.startswith(("https://", "http://localhost")): return False, "invalid_origin"
    if req.challenge_type not in SUPPORTED: return False, "unsupported_challenge"
    if req.attempt >= 1: return False, "attempt_budget_exhausted"
    if not 1 <= req.timeout_seconds <= 120: return False, "invalid_timeout"
    return True, "approved"
