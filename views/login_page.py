from flask import (Blueprint, render_template, abort,
                   request, redirect, flash, url_for)
from jinja2 import TemplateNotFound
from flask_login import login_user
from flask_bcrypt import Bcrypt

from forms.login_form import LoginForm
from models.model import User

bcrypt: Bcrypt = Bcrypt()

login_bp: Blueprint = Blueprint(
    'login_bp', __name__, template_folder='templates')


@login_bp.route('/login', methods=['GET', 'POST'])
def login() -> None:
    try:
        form: LoginForm = LoginForm()

        if form.validate_on_submit() and request.method == 'POST':

            get_user = User.query.filter_by(
                username=form.username.data).first()

            if get_user is not None and bcrypt.check_password_hash(get_user.password_hash, form.password.data):

                login_user(get_user)
                flash(
                    f"You were successfully logged in! {get_user.username}", 'success')
                return redirect(url_for('market_bp.market'))

            else:
                flash(f'Invalid  username or password', 'danger')

        return render_template('auth/login.html', form=form)

    except TemplateNotFound:
        abort(404)
