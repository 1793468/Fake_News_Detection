from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load Model & Vectorizer
model = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news'].strip()  # Get the full textarea content
        if not news_text:
            return render_template('index.html', error="Please enter news content!")

        # Split the input by newlines to process multiple articles
        news_list = news_text.split('\n')
        results = []
        
        # Process each news article
        for news in news_list:
            news = news.strip()  # Remove leading/trailing whitespace
            if news:  # Only process non-empty lines
                news_transformed = vectorizer.transform([news])
                prediction = model.predict(news_transformed)[0]
                if prediction == 0:
                    label = 'FAKE'
                elif prediction == 1:
                    label = 'REAL'
                else:
                    label = 'UNKNOWN'
                results.append({'news': news, 'prediction': label})

        if not results:
            return render_template('index.html', error="No valid news content provided!")

        return render_template('result.html', results=results)

@app.route('/stats')
def stats():
    labels = ['Fake News', 'Real News']
    values = [random.randint(100, 500), random.randint(100, 500)]  # Simulated data
    plt.figure(figsize=(6, 4))
    sns.barplot(x=labels, y=values, palette='coolwarm')
    plt.title("Fake vs Real News")
    plt.ylabel("Count")
    plt.savefig('static/chart.png')  # Save image
    return jsonify({'status': 'Chart Generated'})

if __name__ == '__main__':
    app.run(debug=True)