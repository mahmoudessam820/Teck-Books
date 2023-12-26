from flask import render_template
from jinja2 import TemplateNotFound 

from . import market 
from app import login_required
from models.model import Books


@market.route('/market', methods=["GET"])
@login_required
def market():
    try:
        books = Books.query.all()
        return render_template('pages/market.html', books=books), 200
    except TemplateNotFound:
        return render_template('pages/error.html', message='Template not found'), 404