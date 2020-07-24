from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
from functools import wraps

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='template'
)


def login_required(needs):
    @wraps(needs)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return needs(*args, **kwargs)
        else:
            flash('Gotta login first pal')
            return redirect(url_for('login'))
    return wrap


@users_blueprint.route('/login', methods=['GET', 'POST'])
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


@users_blueprint.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('udah keluar yak')
    return redirect(url_for('home'))


@users_blueprint.route('/')
def home():
    return render_template('index.html')


@users_blueprint.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')
