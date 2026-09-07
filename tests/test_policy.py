from captcha_solver_tool.handler import solve_checkpoint, FixtureTransport

BASE={"task_id":"qa-1","origin":"https://example.test","challenge_type":"recaptcha_v2","authorized":True}
def test_fixture_success(): assert solve_checkpoint(BASE)["status"] == "solved"
def test_requires_authorization():
 d=dict(BASE,authorized=False); assert solve_checkpoint(d)["reason"] == "authorization_required"
def test_attempt_budget():
 d=dict(BASE,attempt=1); assert solve_checkpoint(d)["reason"] == "attempt_budget_exhausted"
def test_invalid_result_stops(): assert solve_checkpoint(BASE,FixtureTransport({"status":"failed"}))["status"] == "manual_review"
