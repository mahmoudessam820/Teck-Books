from flask import render_template, abort 
from jinja2 import TemplateNotFound

from . import main 


@main.route('/', methods=["GET"])
@main.route('/home')
def home():
    try:
        return render_template('pages/home.html')
    except TemplateNotFound:
        abort(404)
