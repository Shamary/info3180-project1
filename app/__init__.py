from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "project###1$$$random###key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://projectv4:projectv4@localhost/projectv4" #"postgresql://lab5:lab5@localhost/lab5"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER']="./app/static/pics"


db = SQLAlchemy(app)

"""# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'"""

app.config.from_object(__name__)
from app import views