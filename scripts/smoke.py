from captcha_solver_tool.handler import solve_checkpoint
r=solve_checkpoint({"task_id":"smoke","origin":"http://localhost","challenge_type":"image_to_text","authorized":True})
assert r["status"]=="solved"
print("smoke: PASS")
