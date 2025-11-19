from flask import  render_template, request
from flask_login import login_required

from appfleshi import app

#redireciona p login
@app.route('/')
def homepage():
    return render_template('homepage.html')



#rota dinamica nome da var aq eh o perfil
@app.route('/profile/<username>')
@login_required
def profile(username):
    return render_template('profile.html', username=username)

