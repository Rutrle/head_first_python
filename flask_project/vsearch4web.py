from flask import Flask, render_template, request, escape, session
from DBcm import UseDatabase
from vsearch import search4letters
import mysql.connector
from checker import check_logged_in

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuess'

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


@app.route('/login')
def login():
    session['logged_in'] = True
    return "You are now logged in"


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return "You have succesfully logged out"


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='welcome to search4letter on the web!')


def log_request(req: 'flask_request', res: str) -> None:

    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    title = "Here are your results"
    word = request.form['phrase']
    letters = request.form['letters']

    results = str(search4letters(word, letters))
    log_request(request, results)
    return render_template('result.html', the_title=title, the_phrase=word, the_letters=letters, the_results=results)


@app.route('/viewlog')
@check_logged_in
def view_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        content = cursor.fetchall()

    titles = ('Phrase', 'Letters' 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='View Log', the_row_titles=titles, the_data=content)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
