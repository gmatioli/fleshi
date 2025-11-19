from flask import  render_template, request
from flask_login import login_required
from appfleshi import app
from appfleshi.forms import LoginForm, RegisterForm

#redireciona p login
@app.route('/')
def homepage():
    login_form = LoginForm()
    return render_template('homepage.html', form=login_form)

@app.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    register_form = RegisterForm()
    return render_template('createaccount.html')

#rota dinamica nome da var aq eh o perfil
@app.route('/profile/<username>')
@login_required
def profile(username):
    return render_template('profile.html', username=username)

