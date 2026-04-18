# 📄 Fake Job Posting Detection System

A Machine Learning-based web application that detects whether a job posting is **real or fake** using Natural Language Processing (NLP) techniques.

---

## 🚀 Live Demo

🔗 Deployed on Render  
[https://fake-job-detection-wtcq.onrender.com]

---

## 📌 Project Overview

Fake job postings are increasingly common and can lead to scams or data theft. This system analyzes job descriptions and predicts whether they are legitimate or fraudulent.

---

## 🧠 Features

- Detects fake vs real job postings
- Displays prediction with confidence score
- Simple and clean web interface
- Fast inference using pre-trained model
- Deployed on Render

---

## 🏗️ Tech Stack

- Backend: Flask
- Machine Learning: Scikit-learn
- Frontend: HTML, CSS
- Deployment: Render
- Model Serialization: Pickle

---

## 📂 Project Structure

├── app.py  
├── model.pkl  
├── tfidf.pkl  
├── templates/  
│   └── index.html  
├── requirements.txt  
└── README.md  

---

## ⚙️ How It Works

1. User enters a job description  
2. Text is transformed using TF-IDF vectorizer  
3. Model predicts Fake or Real  
4. Confidence score is displayed ( It indicate percentage of fraud , if the job is real then also it will give fraudulent percentage )

---

## 🖥️ Installation & Setup

### Clone Repository

[https://github.com/KrishGolchha0105/fake-job-detection.git](https://github.com/KrishGolchha0105/fake-job-detection.git)

cd fake-job-detection

### Install Dependencies

pip install -r requirements.txt

### Run App

python app.py

App runs at: [http://localhost:10000](http://localhost:10000)

---

## ☁️ Deployment (Render)

- Build Command: pip install -r requirements.txt  
- Start Command: gunicorn app:app  
