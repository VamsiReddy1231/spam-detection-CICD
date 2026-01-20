import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset (Kaggle format)
data = pd.read_csv("data/spam.csv", encoding="latin-1")

# Keep required columns
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

X = data['message']
y = data['label'].map({'ham': 0, 'spam': 1})

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Evaluation
accuracy = accuracy_score(y_test, model.predict(X_test_vec))
print(f"Model Accuracy: {accuracy}")

# Save artifacts
os.makedirs("model/artifacts", exist_ok=True)
joblib.dump(model, "model/artifacts/spam_model.pkl")
joblib.dump(vectorizer, "model/artifacts/vectorizer.pkl")

with open("model/artifacts/accuracy.txt", "w") as f:
    f.write(str(accuracy))
