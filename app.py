from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem-vindo ao Fléshi!'

if __name__ == '__main__':
    app.run(debug=True)