import time
from .policy import SolveRequest, authorize

class FixtureTransport:
    def __init__(self, result=None): self.result = result or {"status": "ready", "token": "fixture-token"}
    def solve(self, payload, timeout): return dict(self.result)

def solve_checkpoint(payload: dict, transport=None) -> dict:
    req = SolveRequest(**payload)
    allowed, reason = authorize(req)
    if not allowed: return {"status": "manual_review", "reason": reason, "task_id": req.task_id}
    started = time.monotonic()
    result = (transport or FixtureTransport()).solve(payload, req.timeout_seconds)
    if time.monotonic() - started > req.timeout_seconds: return {"status": "manual_review", "reason": "timeout", "task_id": req.task_id}
    if result.get("status") != "ready" or not result.get("token"):
        return {"status": "manual_review", "reason": "invalid_solver_result", "task_id": req.task_id}
    return {"status": "solved", "task_id": req.task_id, "token": result["token"], "attempts_used": 1}
