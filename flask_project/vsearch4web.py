from flask import Flask, render_template, request, escape
from vsearch import search4letters
import mysql.connector

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='welcome to search4letter on the web!')


def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res, ))

    conn.commit()
    cursor.close()
    conn.close()


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    title = "Here are your results"
    word = request.form['phrase']
    letters = request.form['letters']

    results = str(search4letters(word, letters))
    log_request(request, results)
    return render_template('result.html', the_title=title, the_phrase=word, the_letters=letters, the_results=results)


@app.route('/viewlog')
def view_log() -> 'html':
    content = []
    with open('vsearch.log', mode='r') as log_file:
        for line in log_file:
            content.append([])
            for item in line.split('|'):
                content[-1].append(escape(item))

    titles = ('Form_data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='View Log', the_row_titles=titles, the_data=content)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
