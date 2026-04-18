
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

# Set your custom threshold
THRESHOLD = 0.3

# UI Route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction (for form UI)
@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("text")

    if not text:
        return render_template("index.html", prediction="Please enter text")

    # Transform input
    text_tfidf = tfidf.transform([text])

    # Get probability of class 1 (Fake Job)
    probability = model.predict_proba(text_tfidf)[0][1]

    # Apply custom threshold
    if probability >= THRESHOLD:
        result = f"⚠️ Fake Job (Confidence: {probability:.2f})"
    else:
        result = f"✅ Real Job (Confidence: {probability:.2f})"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
