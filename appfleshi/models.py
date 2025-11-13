from zoneinfo import ZoneInfo
from datetime import datetime
from appfleshi import database

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    email = database.Column(database.String(100), unique=True, nullable=False)
    password = database.Column(database.String(60), nullable=False)
    photos = database.relationship("Photo", backref="user", lazy=True)
    pass

class Photo(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey("user.id"), nullable=False)
    file_name = database.Column(database.String(255), unique=True, nullable=False, default='default.png')
    upload_date = database.Column(database.DateTime, nullable=False, default=lambda: datetime.now(ZoneInfo("America/Sao_Paulo")))