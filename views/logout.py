from flask import (Blueprint, url_for, redirect, flash)
from flask_login import logout_user


logout_bp: Blueprint = Blueprint(
    'logout_bp', __name__, template_folder='templates')


@logout_bp.route('/logout')
def logout() -> None:
    logout_user()
    flash('You were successfully logout!', 'info')
    return redirect(url_for('home_bp.home'))
