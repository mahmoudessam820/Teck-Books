import uuid

from models.model import Books
from app import db

def test_add_new_book(app):
    """
    Test the functionality of adding a new book to the database.

    Parameters:
    - app (Flask): The Flask application instance.

    This method creates a new book with test data, adds it to the database,
    and then queries the database to ensure that the book was added correctly.

    It asserts that the properties of the retrieved book match the expected values.

    Raises:
    - AssertionError: If any of the assertions fail.
    """

    with app.app_context():

        new_book =Books(
            id=str(uuid.uuid4()),
            title='test',
            author='test',
            category='test',
            language='test',
            pages=100,
            year=2000,
            link='test.com'
        )

        db.session.add(new_book)
        db.session.commit()

        query_set = Books.query.all()

        assert query_set[0].title == 'test' 
        assert query_set[0].author == 'test' 
        assert query_set[0].category == 'test' 
        assert query_set[0].language == 'test' 
        assert query_set[0].pages == 100
        assert query_set[0].year == 2000
        assert query_set[0].link == 'test.com'
