from flask import (render_template, Blueprint, abort)
from flask_login import login_required
from jinja2 import TemplateNotFound
from models.model import Books


market_bp: Blueprint = Blueprint(
    'market_bp', __name__, template_folder='templates')


@market_bp.route('/market', methods=['GET'])
@login_required
def market() -> None:
    try:
        books = Books.query.all()
        return render_template('pages/market.html', books=books)
    except TemplateNotFound:
        abort(404)
