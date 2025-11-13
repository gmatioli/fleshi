from appfleshi import app, database
from appfleshi.models import User, Photo

with app.app_context():
     database.create_all()