from zoneinfo import ZoneInfo

from datetime import  datetime

from appfleshi import database, login_manager
from flask_login import UserMixin

#add o userMixin para saber q eh daq q vem os logins
class User(database.Model, UserMixin):
  id = database.Column(database.Integer, primary_key=True)
  username = database.Column(database.String(20), unique=True, nullable=False)
  email = database.Column(database.String(100), unique=True, nullable=False)
  password = database.Column(database.String(60), nullable=False)
  photos = database.relationship('Photo', backref='user', lazy=True)

#função p carregar o user (pega pelo id)
#sempre q altera algo no models roda o create_database p atualizar
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Photo(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    file_name = database.Column(database.String(255), unique=True, nullable=False, default='default.png')
    upload_date = database.Column(database.DateTime, nullable=False, default=lambda: datetime.now(ZoneInfo("America/Sao_Paulo")))
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)