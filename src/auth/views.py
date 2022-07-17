from flask import Blueprint, jsonify, redirect, render_template, request, flash, url_for, current_app
from .form_fields import RegistrationForm, LoginForm
from ..models.user import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from ..utils import db

auth = Blueprint('auth', __name__)



@auth.route('/', methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()

    

    if request.method == 'POST':
        #validate on submit returns true if all checks clear out and false otherwise
        if reg_form.validate_on_submit():
            username = reg_form.username.data
            password = reg_form.password.data

            #check if username exists
            username_exists = User.query.filter_by(username = username).first()
            if username_exists:
                flash('Username already exists, choose another one.', 'primary')
            
            else:
                new_user = User(
                    username = username,
                    password = generate_password_hash(password, method='sha256')
                )

                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('User created, you can log in with the registered credentials', 'success')

                return redirect(url_for('auth.login'))

    

    return render_template('register.html', form = reg_form, user = current_user)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()

    if request.method == 'POST':
        if login_form.validate_on_submit():
            username = login_form.username.data
            password = login_form.password.data

            user = User.query.filter_by(username = username).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('Logged in!', 'success')
                    login_user(user, remember=True)  
                    return redirect(url_for('chat.home'))
                
                else:
                    flash('Username or Password is incorrect!', 'error')
                
            else:
                flash('Username or Password is incorrect!', 'error')
    
    return render_template('login.html', form = login_form, user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'primary')
    return redirect(url_for('auth.login'))