import os 
from flask_migrate import Migrate 
from app import create_app, db 
from models.model import Users, Books 


app = create_app(os.getenv('APP_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():

    """
    Creates a shell context for the flask application.

    Returns:
        dict: The shell context.
    """

    return dict(db=db, Users=Users, Books=Books)