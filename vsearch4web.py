from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='welcome to search4letter on the web!')


@app.route('/')
def hello() -> str:
    return 'Hello world from FLask!'


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    word = request.form['phrase']
    letters = request.form['letters']
    return str(search4letters(word, letters))


app.run(port=5000, debug=True)
