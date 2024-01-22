import pytest

from app import create_app, db
from config import config


@pytest.fixture
def app():
    """
    Fixture that sets up and tears down the Flask application for testing purposes.

    Returns:
        Flask: The Flask application object.
    """

    config_name = 'testing'
    app = create_app(config_name)
    app.config.from_object(config[config_name])

    return app



@pytest.fixture
def client(app):
    """
    Creates a test client for the Flask application.

    Args:
        app (Flask): The Flask application object.

    Yields:
        FlaskClient: The test client.
    """

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
            print(db.engine.table_names())
        yield client
        with app.app_context():
            db.drop_all()  # Drop the database tables after testing
