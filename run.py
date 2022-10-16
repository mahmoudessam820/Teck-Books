from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin

from models.model import (
    db, User, Books, SecureAdminIndexView, SecureModelView)

from views.home import home_bp
from views.market import market_bp
from views.register_page import register_bp
from views.login_page import login_bp
from views.logout import logout_bp
from views.new_book_page import new_book_bp
from views.admin import admin_bp

#! Instantiation Classes
migrate: Migrate = Migrate()
login_manager: LoginManager = LoginManager()


def create_app():

    #! App Config
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)

    #! Migrate init
    migrate.init_app(app, db)

    #! App Login Manager Config
    login_manager.init_app(app)
    login_manager.login_view = 'login_bp.login'
    login_manager.login_message_category = 'info'

    # This callback is used to reload the user object from the user ID stored in the session.
    @login_manager.user_loader
    def load_user(user_id) -> None:
        return User.query.get(int(user_id))

    #! Admin Config
    admin = Admin(app, index_view=SecureAdminIndexView(),
                  template_mode='bootstrap4')
    admin.add_view(SecureModelView(Books, db.session))
    admin.add_view(SecureModelView(User, db.session))

    # ? Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(market_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(new_book_bp)

    return app
