from .handler import solve_checkpoint
TOOL_SCHEMA = {"name":"solve_captcha_checkpoint","description":"Handle one authorized CAPTCHA checkpoint.","parameters":{"type":"object","properties":{"task_id":{"type":"string"},"origin":{"type":"string"},"challenge_type":{"type":"string"},"authorized":{"type":"boolean"}},"required":["task_id","origin","challenge_type","authorized"]}}
def handle_tool_message(message: dict) -> dict:
    return solve_checkpoint(message)
