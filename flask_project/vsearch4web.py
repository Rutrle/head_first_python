from flask import Flask, render_template, request, escape, session, copy_current_request_context
from DBcm import UseDatabase, ConnectionError, CredentialsError,  SQLError
from vsearch import search4letters
from checker import check_logged_in
from time import sleep
from threading import Thread

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


@app.route('/search4', methods=['POST'])
def do_search() -> str:

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        sleep(15)  # simulationg slow communication
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

    title = "Here are your results"
    word = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(word, letters))

    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('***** Logging failed with this error: ', str(err))
    return render_template('result.html', the_title=title, the_phrase=word, the_letters=letters, the_results=results)


@app.route('/viewlog')
@check_logged_in
def view_log() -> 'html':
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            content = cursor.fetchall()

    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('something went wrong: ', str(err))

    titles = ('Phrase', 'Letters' 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='View Log', the_row_titles=titles, the_data=content)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
