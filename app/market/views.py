from flask import render_template, abort
from jinja2 import TemplateNotFound 

from . import market 
from app import db, login_required, current_user
from models.model import Books


@market.route('/market', methods=["GET"])
def market():
    try:
        books = Books.query.all()
        return render_template('pages/market.html', books=books), 200
    except TemplateNotFound:
        abort(404)