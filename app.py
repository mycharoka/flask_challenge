from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps


app = Flask(__name__)

# 127.0.0.1:50155

# config file
import os
app.config.from_object(os.environ['APP_SETTINGS'])

# login required decorator
from project.models import User, db


def login_required(needs):
    @wraps(needs)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return needs(*args, **kwargs)
        else:
            flash('Gotta login first pal')
            return redirect(url_for('login'))
    return wrap


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials!'
        else:
            session['logged_in'] = True
            flash('MASUK COI!!!!!')
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('udah keluar yak')
    return redirect(url_for('home'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')
