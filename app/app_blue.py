from fastapi import FastAPI
import joblib

app = FastAPI(title="Spam Detection API - BLUE")

model = joblib.load("model/artifacts/spam_model.pkl")
vectorizer = joblib.load("model/artifacts/vectorizer.pkl")

@app.post("/predict")
def predict(message: str):
    vec = vectorizer.transform([message])
    pred = model.predict(vec)[0]
    return {"version": "BLUE", "prediction": "spam" if pred else "ham"}
