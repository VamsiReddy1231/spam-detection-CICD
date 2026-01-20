from fastapi import FastAPI
import requests

app = FastAPI(title="Spam Detection API - PROXY")

@app.post("/predict")
def route_request(message: str):
    with open("live_version.txt") as f:
        version = f.read().strip()

    if version == "blue":
        url = "http://127.0.0.1:8000/predict"
    else:
        url = "http://127.0.0.1:8001/predict"

    response = requests.post(url, params={"message": message})
    return response.json()
