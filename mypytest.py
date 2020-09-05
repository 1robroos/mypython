#/usr/bin/python3
from flask import Flask
from kl import Kl, FileHandler, SpanishTransformer
from textblob import TextBlob

# create Flask app
app=Flask(__name__)

# a simple home page
@app.route('/')
def hello():
    return 'I am loving it'

# create sentiment API:
@app.route('/<message>')
def index(message):
    sentiment="positive"
    if (TextBlob(message).sentiment.polarity < 0.0):
        sentiment='negative'
    return app.make_response(sentiment)

    
