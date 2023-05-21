from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


# devDatabasePath = 'sqlite:////app/collective.db'      # docker
devDatabasePath = "sqlite:///" + \
    os.path.join(os.path.expanduser('~'), 'repos', 'collective', 'collective.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=devDatabasePath
db = SQLAlchemy(app)
app.app_context().push()

from app import routes, models

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run('0.0.0.0', 9222, debug=True)