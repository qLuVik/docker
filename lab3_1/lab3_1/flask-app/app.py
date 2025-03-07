from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')

app = Flask(__name__)
es = Elasticsearch("http://elasticsearch-1:9200")

# Загрузка данных для обучения модели
data = pd.read_csv('reviews.csv')  # Файл с отзывами для обучения
data['clean_text'] = data['text'].apply(lambda x: ' '.join([word for word in re.sub(r'[^\w\s]', '', x).lower().split() if word not in stopwords.words('english')]))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['clean_text'])
y = data['sentiment']

model = MultinomialNB()
model.fit(X, y)

@app.route('/add_review', methods=['POST'])
def add_review():
    data = request.json
    text = data['text']
    clean_text = ' '.join([word for word in re.sub(r'[^\w\s]', '', text).lower().split() if word not in stopwords.words('english')])
    sentiment = model.predict(vectorizer.transform([clean_text]))[0]

    doc = {
        'text': text,
        'sentiment': sentiment
    }
    es.index(index='reviews', document=doc)
    return jsonify({"status": "success", "message": "Review added", "sentiment": sentiment})

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    res = es.search(index='reviews', body={"query": {"match": {"text": query}}})
    return jsonify(res['hits']['hits'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
