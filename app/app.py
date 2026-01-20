from fastapi import FastAPI
import joblib

app = FastAPI(title="Spam Detection API")

# Load trained artifacts
model = joblib.load("model/artifacts/spam_model.pkl")
vectorizer = joblib.load("model/artifacts/vectorizer.pkl")

@app.post("/predict")
def predict(message: str):
    vector = vectorizer.transform([message])
    prediction = model.predict(vector)[0]

    return {
        "message": message,
        "prediction": "spam" if prediction == 1 else "ham"
    }
