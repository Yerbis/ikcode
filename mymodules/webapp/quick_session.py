from flask import Flask, session
from checker import check_logged_in 

app = Flask(__name__)


@app.route('/')
def start():
    return 'IKcode simple webapp functions website'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return 'You are now logged out'

@app.route('/status')
def check_status():
    if 'logged_in' in session:
        return 'You are currently logged in'
    return 'You are NOT logged in'


app.secret_key = 'PanzerKampfWagenIIIAusf.N'

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']

def check_logged_in():
    if 'logged_in' in session:
        return True
    return False


@app.route('/page1')
@check_logged_in
def page1():
    if 'logged_in' in session:
        return 'This is page 1.'
    return 'You are NOT logged in. Page inaccessable.'

if __name__  == '__main__':
    app.run(debug=True)

@app.route("/page2")
@check_logged_in
def page2():
    return 'This is page 2'

@app.route('/page3')
@check_logged_in
def page3():
    return 'This is page 3'

if __name__ == '__main__':
    app.run(debug=True)

