from flask import (render_template, request, redirect, url_for, flash) 

from . import auth 
from ..forms.signin import SigninForm
from ..forms.login import LoginForm
from app import db, bcrypt, login_user, logout_user
from models.model import Users



@auth.route('/signin', methods=["POST", "GET"])
def signin():
    form = SigninForm()

    if request.method == 'POST' and form.validate_on_submit():

        password_hash = bcrypt.generate_password_hash(form.password1.data)

        new_user = Users(
            username=form.username.data,
            email=form.email.data,
            password=password_hash
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)

            flash(f"You have successfully created a new account. Welcome {new_user.username}", 'success')

            form.username.data = ''
            form.email.data = ''
            form.password1.data = ''

            return redirect(url_for('market.market'))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred. Account could not be created. Error: {str(e)}", category='danger')
    else:
        for error_message in form.errors.values():
            flash(f"An error occurred: {error_message}. Account could not be created", category='danger')

    return render_template('auth/signin.html', form=form)



@auth.route('/login', methods=["POST", "GET"])
def login():

    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():

        user = Users.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):

            login_user(user)
            flash(f"You are now logged in as {user.username}", 'success')

            form.email.data = ''
            form.password.data = ''

            return redirect(url_for('market.market'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('auth/login.html', form=form)



@auth.route('/logout', methods=["POST", "GET"])
def logout():
    logout_user()
    flash('You were successfully logout!', 'info')
    return redirect(url_for('main.home'))