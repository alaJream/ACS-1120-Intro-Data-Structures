"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from dictogram import Dictogram

app = Flask(__name__)


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
    return f'<p>{data.sample()}</p>'


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)