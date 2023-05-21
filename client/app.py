from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('home.html', client={'clientName': ''})

if __name__ == '__main__':
    app.run('0.0.0.0', 9222, debug=True)