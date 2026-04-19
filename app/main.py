#Cette app permet de ping l'hote utilisateur
from Fastapi import FastAPI, Query
import subprocess

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello my APP secure"}

@app.get("/ping")
def ping(host: str = Query(..., description="The host to ping")):
    try:
        result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
        return {"output": result.stdout}
    except Exception as e:
        return {"error": str(e)}