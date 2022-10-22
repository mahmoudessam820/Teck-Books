from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


home_bp: Blueprint = Blueprint(
    'home_bp', __name__, template_folder='templates')


@home_bp.route('/', methods=['GET'])
@home_bp.route('/home')
def home() -> None:
    try:
        return render_template('pages/home.html'), 200
    except TemplateNotFound:
        abort(404)
