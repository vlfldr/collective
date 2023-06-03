from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import string
import random

from flask_jwt_extended import JWTManager

load_dotenv()
app = Flask(__name__)

# database
devDatabasePath = "sqlite:///" + \
    os.path.join(os.path.expanduser('~'), 'repos', 'collective', 'collective.db')
app.config['SQLALCHEMY_DATABASE_URI']=devDatabasePath

db = SQLAlchemy(app)
app.app_context().push()

# authorization
if os.getenv('JWT_SECRET_KEY') == None:
    print('Fatal error: JWT_SECRET_KEY environment variable not set. Please review the Dockerfile or create a .env file next to server.py.')
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

from app import routes, models

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run('0.0.0.0', 9222, debug=True)