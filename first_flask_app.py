from flask import Flask
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from FLask!'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('Hello world from FLask!'))


app.run(port=5000)
