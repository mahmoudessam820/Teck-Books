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


class ClientTestCase(unittest.TestCase):
    """This class represents the client test case"""

    def setUp(self) -> None:
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


#----------------------------------------------------------------#
# Test Cases
#----------------------------------------------------------------#


    def test_app_exists(self):
        """
        GIVEN a flask instance that can be used to test the existence instance of a flask
        WHEN  a flask instance is created and initialized 
        THEN  check that the instance exists
        """
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        """
        GIVEN a flask app instance 
        WHEN  a flask app instance configured
        THEN  check the flask app is testing mode 
        """
        self.assertTrue(current_app.config['TESTING'])

    def test_home_page_get(self):
        """
        GIVEN  a home page with valid request method
        WHEN   the '/' page is requested (GET)
        THEN   check that the response is valid (200) status code is returned
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'Free Tech Books Market' in response.get_data(as_text=True))

    def test_home_page_post(self):
        """
        GIVEN  a home page with invalid request method
        WHEN   the '/' page is  posted to (POST)
        THEN   check that a (405) status code is returned
        """

        response = self.client.post('/')
        self.assertEqual(response.status_code, 405)

    def test_market_page_get(self):
        """
        GIVEN  a market page without register
        WHEN   the '/market' page is requested (GET)
        THEN   check that a (302) status code is returned
        """
        response = self.client.get('/market')
        self.assertEqual(response.status_code, 302)

    def test_market_page_post(self):
        """
        GIVEN  a market page without register and invaild request method
        WHEN   the '/market' page is requested (POST)
        THEN   check that a (405) status code is returned
        """
        response = self.client.post('/market')
        self.assertEqual(response.status_code, 405)

    def test_add_new_book(self):
        """
        GIVEN  a new book page 
        WHEN   the '/newbook' page is requested (POST)
        THEN   check that a (200) status code is returned
        """

        response = self.client.post('/newbook', follow_redirects=True)

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
        book_exist = Books.query.filter_by(
            name='Flask Web Development').first()

        self.assertIsNotNone(book_exist)
        self.assertEqual(response.status_code, 200)

    def test_register_login_logout_page(self):
        """
        GIVEN  a register page and login and logout pages 
        WHEN   the '/register', '/login', '/login' pages is requested (POST)
        THEN   check that a vailed user and (200) status code is returned
        """

        # register a new account
        response = self.client.post('/register', follow_redirects=True)

        u = User(
            username='tito',
            email='tito@example.com',
            password_hash='cat'
        )
        db.session.add(u)
        db.session.commit()

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'Please Create An Account' in response.get_data(
                as_text=True))

        # log in with the new account
        response = self.client.post('/login', follow_redirects=True)

        user = User.query.filter_by(username='tito').first()

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(user)
        self.assertTrue('Welcome Back' in response.get_data(as_text=True))

        # log out
        response = self.client.get('/logout', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('You were successfully logout!' in response.get_data(
            as_text=True))


if __name__ == "__main__":
    unittest.main()