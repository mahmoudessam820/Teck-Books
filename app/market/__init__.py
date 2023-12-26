from flask import Blueprint 


market: Blueprint = Blueprint('market', __name__, template_folder='templates')

from . import views 