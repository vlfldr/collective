from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('home.html')

@app.get('/register')
def registerView():
    return render_template('register.html', client={'clientName': ''})

@app.post('/register')
def registerPost():
    print(request.form['backupTime'])
    return 'OK'

@app.get('/login')
def loginView():
    return render_template('login.html')

@app.post('/login')
def loginPost():
    print(request.form['clientName'])
    return 'OK'


if __name__ == '__main__':
    app.run('localhost', 9222, debug=True)