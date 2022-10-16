from flask import (Blueprint, render_template, abort,
                   request, redirect, flash, url_for)
from jinja2 import TemplateNotFound
from flask_login import login_user
from flask_bcrypt import Bcrypt

from forms.register_form import RegisterForm
from models.model import User, db

bcrypt: Bcrypt = Bcrypt()

register_bp: Blueprint = Blueprint(
    'register_bp', __name__, template_folder='templates')


@register_bp.route('/register', methods=['GET', 'POST'])
def register() -> None:
    try:
        form: RegisterForm = RegisterForm()

        if request.method == 'POST' and form.validate_on_submit():

            new_user: User = User(
                username=form.username.data,
                email=form.email.data,
                password_hash=bcrypt.generate_password_hash(
                    form.password1.data).decode('utf-8')
            )

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)

            flash(
                f"You were create new account successfully welcome {new_user.username}", 'success')

            form.username.data = ''
            form.email.data = ''
            form.password1 = ''

            return redirect(url_for('market_bp.market'))

        if form.errors != {}:
            for error_message in form.errors.values():
                flash(
                    f"An error occurred {error_message}  could not be created", category='danger')
        return render_template('auth/register.html', form=form)

    except TemplateNotFound:
        abort(404)
