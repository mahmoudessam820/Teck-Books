#----------------------------------------------------------------#
# Imports
#----------------------------------------------------------------#
import unittest
from flask import current_app
from run import create_app, db
from models.model import User, Books


#----------------------------------------------------------------#
# Unittest Setup
#----------------------------------------------------------------#


class ModelsTestCase(unittest.TestCase):
    """This class represents the models test case"""

    def setUp(self) -> None:
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

#----------------------------------------------------------------#
# Test Cases
#----------------------------------------------------------------#

    def test_app_exists(self) -> None:
        """
        GIVEN a flask instance that can be used to test the existence instance of a flask
        WHEN  a flask instance is created and initialized
        THEN  check that the instance exists
        """
        self.assertFalse(current_app is None)

    def test_app_is_testing(self) -> None:
        """
        GIVEN a flask app instance
        WHEN  a flask app instance configured
        THEN  check the flask app is testing mode
        """
        self.assertTrue(current_app.config['TESTING'])

    def test_user_model(self) -> None:
        """
        GIVEN a user model
        WHEN  a app instance is created
        THEN  create a new user
        """

        u = User(
            username='tito',
            email='tito@example.com',
            password_hash='1234560'
        )

        db.session.add(u)
        db.session.commit()

        self.assertEqual(u.username, 'tito')
        self.assertEqual(u.email, 'tito@example.com')
        self.assertEqual(u.password_hash, '1234560')

    def test_books_model(self) -> None:
        """
        GIVEN a books model
        WHEN  a app instance is created
        THEN  create a new book
        """

        b = Books(
            name='Flask Web Development',
            author='Miguel Grinberg',
            category='Web Development',
            language='python',
            pages=315,
            published=2016,
            link='Type-Driven%20Development%20with%20Idris.pdf'
        )

        db.session.add(b)
        db.session.commit()

        self.assertEqual(b.name, 'Flask Web Development')
        self.assertEqual(b.author, 'Miguel Grinberg')
        self.assertEqual(b.category, 'Web Development')
        self.assertEqual(b.language, 'python')
        self.assertEqual(b.pages, 315)
        self.assertEqual(b.published, 2016)
        self.assertEqual(
            b.link, 'Type-Driven%20Development%20with%20Idris.pdf')


if __name__ == "__main__":
    unittest.main()
