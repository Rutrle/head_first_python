from flask import Flask, render_template
from vsearch import search4letters

app = Flask(__name__)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='welcome to search4letter on the web!')


@app.route('/')
def hello() -> str:
    return 'Hello world from FLask!'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('Hello world from FLask!'))


app.run(port=5000)
