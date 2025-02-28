# 📰 Fake News Detection System

A simple **Fake News Detection** web app using **Machine Learning** and **Flask**.

---

## 🔑 Key Features
- Detects if news is **FAKE** or **REAL**
- Accepts multiple news articles at once
- Beautiful Pie Chart Visualization
- Confetti Animation on Success
- Fully Responsive Design

---

## 🎯 Technology Stack
- Python
- Flask
- Scikit-Learn
- HTML, CSS, JavaScript

---

## 📂 Project Structure
Fake_News_Detection/
│
├─ static/                  # Static Files (CSS, JS, Images)
│   ├─ style.css            # Custom CSS
│   ├─ script.js            # JavaScript Animations
│   ├─ chart.js             # Pie Chart Visualization
│   ├─ screenshots/         # Screenshots Folder (Images for README.md)
│       ├─ Homepage.png     # Homepage Screenshot
│       ├─ Result.png       # Result Page Screenshot
│       
│
├─ templates/               # HTML Pages
│   ├─ index.html           # Homepage Form
│   ├─ result.html          # Prediction Results
│
├─ fake_news_model.pkl      # Machine Learning Model
├─ tfidf_vectorizer.pkl     # TF-IDF Vectorizer
├─ app.py                   # Flask Backend API
├─ requirements.txt         # Dependencies
└─ README.md                # Documentation
