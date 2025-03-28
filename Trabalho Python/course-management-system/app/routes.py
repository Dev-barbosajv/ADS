from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, RegistrationForm, CheckInForm
from .models import User, CheckIn
from . import db
from datetime import datetime

app = Blueprint('app', __name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('app.dashboard'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if not current_user.is_admin:
        flash('You do not have permission to access this page.')
        return redirect(url_for('app.login'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully.')
        return redirect(url_for('app.login'))
    return render_template('register.html', form=form)

@app.route('/checkin', methods=['GET', 'POST'])
@login_required
def checkin():
    form = CheckInForm()
    if form.validate_on_submit():
        checkin_entry = CheckIn(user_id=current_user.id, timestamp=datetime.now())
        db.session.add(checkin_entry)
        db.session.commit()
        flash('Check-in recorded successfully.')
        return redirect(url_for('app.dashboard'))
    return render_template('checkin.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app.login'))