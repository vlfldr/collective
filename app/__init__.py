# The application will exist in a package. 
# In Python, a sub-directory that includes a __init__.py file 
# is considered a package, and can be imported. 
# When you import a package, the __init__.py executes and defines 
# what symbols the package exposes to the outside world.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_cors import CORS
import os

app = Flask(__name__)
devDatabasePath = "sqlite:///" + \
    os.path.join(os.path.expanduser('~'), 'repos', 'collective', 'collective.db')
app.config['SQLALCHEMY_DATABASE_URI']=devDatabasePath
app.app_context().push()
sqlDB = SQLAlchemy(app)
sqlDB.create_all()

#CORS(app)

if __name__ == '__main__':
    app.run('0.0.0.0', 9222, debug=True)

from app import routes, models