from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='welcome to search4letter on the web!')


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    title = "Here are your results"
    word = request.form['phrase']
    letters = request.form['letters']

    results = str(search4letters(word, letters))
    log_request(request, results)
    return render_template('result.html', the_title=title, the_phrase=word, the_letters=letters, the_results=results)


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.txt', mode='w') as write_log:
        print(req, res, file=write_log)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
