from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#libs p login
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datafleshi.db"
app.config['SECRET_KEY'] = 'secret'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()

#direciona p onde está a tela de login (homepage no caso)
login_manager.login_view = 'homepage'

from appfleshi import routes