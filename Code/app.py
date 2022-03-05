"""Main script, uses other modules to generate sentences."""
import pdb
from flask import Flask, render_template, request, redirect
from dictogram import Dictogram
from twitter import TwitterBot
from markov import markov_chain
from markov import tweet_generator
from tasks import open_and_low
from tokens import tokenize
from cleanup import read_file

app = Flask(__name__)
instance = TwitterBot()

file = open_and_low('code/burgundy.txt')
tokenized = tokenize(file)
markov = markov_chain(tokenized)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    arr = []
    f = open('sjack.txt')
    for line in f:
        for word in line.split(' '):
            arr.append(word)
    return Dictogram(arr)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    data = before_first_request()
    sentence = 'hello'
    a = instance.tweet(sentence)
    
    return f'<p>{data.sample()}</p>'


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)