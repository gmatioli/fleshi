from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route("/profile/<username>")
def profile(username):
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)