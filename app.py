from flask import Flask, request, render_template,redirect,url_for
import pickle
from textblob import TextBlob

app = Flask(__name__)

# Load the sentiment analysis model
with open('bert_embeddings.pickle', 'rb') as f:
    model = pickle.load(f)

# Home page with a form to submit a review
@app.route('/')
def home():
    return render_template('index.html')

# Analyze sentiment of the submitted review
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        # Use TextBlob for sentiment analysis
        analysis = TextBlob(review)
        # Determine sentiment
        if analysis.sentiment.polarity > 0:
            sentiment = 'Positive'
        elif analysis.sentiment.polarity == 0:
            sentiment = 'Neutral'
        else:
            sentiment = 'Negative'
        return render_template('review.html', review=review, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
