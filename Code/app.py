"""Main script, uses other modules to generate sentences."""
from distutils import text_file
import pdb
from flask import Flask, render_template, request, redirect
from sentence import get_sentance, create_markov, create_histogram
from dictogram import Dictogram
from twitter import TwitterBot
from markov import markov_chain
from tokens import tokenize

app = Flask(__name__)
instance = TwitterBot()
text_file = 'data/corpus.txt'
words = tokenize(text_file)
histogram = create_histogram(words)
markov = markov_chain(histogram, words)



@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    def index():
        return render_template('index.html', title='Burgundy Tweet', generated_text=get_sentance(histogram, markov, 5))
    
        # return f'<p>{data.sample()}</p>'

@app.route('/tweet', methods=['POST'])
def create_tweet():
  status = request.form['sentence']
  print(status)
  TwitterBot.tweet(status)
  return redirect('/')

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)