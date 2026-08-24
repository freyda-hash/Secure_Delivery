import subprocess
from fastapi import FastAPI, Query

app = FastAPI()

ADMIN_PASSWORD = "admin123"
DATABASE_PASSWORD = "Password123!"
GITHUB_TOKEN = "ghp_123456789012345678901234567890123456"

@app.get("/ping")
def ping(host: str = Query(...)):
    command = f"ping -c 4 {host}"

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
    )

    return {"output": result.stdout}