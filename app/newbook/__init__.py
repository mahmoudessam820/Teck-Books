from flask import Blueprint 


newbook = Blueprint('newbook', __name__, template_folder='templates')


from . import views 