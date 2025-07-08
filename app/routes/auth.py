from flask import Blueprint, render_template, redirect, session, url_for, request, flash
from app.models import User, db

auth_bp = Blueprint('auth',__name__)


@auth_bp.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username

            flash(f'Login successful! Welcome, {username}!', 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            exist_user = User.query.filter_by(username=username).first()
            if exist_user:
                flash('Username already exists. Please choose a different one.', 'danger')
                return redirect(url_for('auth.register'))
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
             # Store in Flask session
            session['username'] = username
            flash(f'Registration successful! Welcome, {username}!', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Please provide both username and password.', 'danger')

    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('auth.login'))