from flask import Flask, render_template, redirect, request
import requests     # to talk to server

app = Flask(__name__)
API_URL = 'http://localhost:9333'

@app.get('/')
def home():
    return render_template('home.html', hideHeader=True)

@app.get('/register')
def registerView():
    return render_template('register.html')

@app.post('/register')
def registerPost():
    data = dict(request.form)

    # split textarea lines into array; discard empty lines
    data['backupDirs'] = [d for d in data['backupDirs'].split('\r\n') if d != '']
    data['excludeDirs'] = [d for d in data['excludeDirs'].split('\r\n') if d != '']

    res = requests.post(API_URL + '/register', json=data)
    return res.text

@app.get('/login')
def loginView():
    return render_template('login.html')

@app.post('/login')
def loginPost():
    print(request.form['clientName'])
    return 'OK'


if __name__ == '__main__':
    app.run('localhost', 9222, debug=True)