from flask import (
    Response, 
    render_template, 
    request, 
    redirect, 
    url_for, 
    flash
)
from wtforms import ValidationError 
from sqlite3 import IntegrityError


from . import auth 
from ..forms.signin import SigninForm
from ..forms.login import LoginForm
from app import db, bcrypt, login_user, logout_user, current_user, login_required
from models.model import Users



@auth.route('/signin', methods=["POST", "GET"])
def signin() -> (Response | str):
    if request.method == 'POST':
        form = SigninForm()
        if form.validate_on_submit():
            existing_admin = Users.query.filter_by(is_admin=True).first()

            if not existing_admin:
                try:
                    Users.create_admin(
                        username=form.username.data,
                        email=form.email.data,
                        password1=form.password1.data
                    )
                    admin_user = Users.query.filter_by(is_admin=True).first()
                    login_user(admin_user)
                    flash("Admin user created successfully.", 'success')
                    return redirect(url_for('market.market'))
                except IntegrityError:
                    db.session.rollback()
                    flash("An error occurred. Admin account could not be created.", category='danger')
                except ValidationError as e:
                    error_messages_str = " ".join(str(error) for error in e.messages)
                    flash(f"An error occurred: {error_messages_str}", category='danger')
                    return redirect(url_for('auth.signin'))
            else:
                try:
                    Users.create_user(
                        username=form.username.data,
                        email=form.email.data,
                        password1=form.password1.data
                    )

                    new_user = Users.query.filter_by(email=form.email.data).first()
                    login_user(new_user)

                    flash(f"You have successfully created a new account. Welcome {new_user.username}", 'success')
                    return redirect(url_for('market.market'))
                except IntegrityError:
                    db.session.rollback()
                    flash("An error occurred. Account could not be created.", category='danger')
                except ValidationError as e:
                    error_messages_str = " ".join(str(error) for error in e.messages)
                    flash(f"An error occurred: {error_messages_str}", category='danger')
                    return redirect(url_for('auth.signin'))
        else:
            for error_message in form.errors.values():
                error_message_str = " ".join(str(message) for message in error_message)
                flash(f"An error occurred: {error_message_str}", category='danger')
    else:
        form = SigninForm()

    form.username.data = ''
    form.email.data = ''
    form.password1.data = ''
    return render_template('auth/signin.html', form=form)



@auth.route('/login', methods=["POST", "GET"])
def login() -> (Response | str):
    form = LoginForm()

    if request.method == 'POST':

        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()

            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Login successful', 'success')

                return redirect(url_for('market.market'))
            else:
                flash('Invalid email or password', 'danger')
        else:
            flash('Form validation failed', 'danger')

    form.email.data = ''
    form.password.data = ''
    return render_template('auth/login.html', form=form)



@auth.route('/logout', methods=["POST", "GET"])
def logout() -> Response:
    logout_user()
    flash('You were successfully logout!', 'info')
    return redirect(url_for('main.home'))

