from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='welcome to search4letter on the web!')


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', mode='a') as write_log:
        print(req.form, req.remote_addr, req.user_agent,
              res, file=write_log, sep='|')


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    title = "Here are your results"
    word = request.form['phrase']
    letters = request.form['letters']

    results = str(search4letters(word, letters))
    log_request(request, results)
    return render_template('result.html', the_title=title, the_phrase=word, the_letters=letters, the_results=results)


@app.route('/viewlog')
def view_log() -> str:
    with open('vsearch.log', mode='r') as log_file:
        content = log_file.read()
    return escape(content)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
