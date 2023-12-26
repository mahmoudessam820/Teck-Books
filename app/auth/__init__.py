from flask import Blueprint 


auth: Blueprint = Blueprint('auth', __name__, template_folder='templates') 

from . import views 