from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

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

    # Transform
    text_tfidf = tfidf.transform([text])

    # Predict
    prediction = model.predict(text_tfidf)[0]
    probability = model.predict_proba(text_tfidf)[0][1]

    if prediction == 1:
        result = f"⚠️ Fake Job (Confidence: {probability:.2f})"
    else:
        result = f"✅ Real Job (Confidence: {probability:.2f})"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)