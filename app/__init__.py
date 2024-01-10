from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_admin import Admin
from flask_bcrypt import Bcrypt 
from flask_login import (
    LoginManager, 
    login_user, 
    logout_user, 
    login_required, 
    current_user
)

from config import config 


# Initialize flask app extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
admin = Admin()

# Initialize flask login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_user = login_user
logout_user = logout_user
login_required = login_required
current_user = current_user


def create_app(config_name: str) -> Flask:

    """
    Create a Flask application with the given configuration name.

    Args:
        config_name (str): The name of the configuration to load.

    Returns:
        Flask: The Flask application.

    """

    # Create Flask application
    app = Flask(__name__)
    
    # Load configuration from config module 
    app.config.from_object(config[config_name]) 
    
    # Initialize dependencies
    config[config_name].init_app(app)

    # Register extensions
    db.init_app(app)
    bcrypt.init_app(app)

    login_manager.init_app(app) 


    # Create and initialize admin
    from models.model import Users, SecureModelView, SecureAdminIndexView

    admin = Admin(template_mode='bootstrap4', index_view=SecureAdminIndexView())
    admin.add_view(SecureModelView(Users, db.session))
    admin.init_app(app)


    # Register blueprints

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, name='auth')

    from .main import main as main_bp
    app.register_blueprint(main_bp, name='main')

    from .market import market as market_bp
    app.register_blueprint(market_bp, name='market')

    from .newbook import newbook as newbook_bp
    app.register_blueprint(newbook_bp, name='newbook')


    return app 