from flask import  render_template, request, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from appfleshi import app, database, bcrypt
from appfleshi.forms import LoginForm, RegisterForm
from appfleshi.models import User, Photo


@app.route('/', methods=['GET', 'POST'])
def homepage():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            return redirect(url_for('profile', username=user.username))
    return render_template('homepage.html', form=login_form)

@app.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        password = bcrypt.generate_password_hash(register_form.password.data)
        user = User(username=register_form.username.data, email=register_form.email.data, password=password)
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('profile', username=user.username))
    return render_template('createaccount.html', form=register_form)

@app.route('/profile/<username>')
@login_required
def profile(username):
    return render_template('profile.html', username=username)

