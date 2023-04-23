#----------------------------------------------------------------#
# Imports
#----------------------------------------------------------------#
import unittest
from urllib import response
from flask import current_app
from flask_login import current_user
from run import create_app, db

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

    def test_home_page_get(self) -> None:
        """
        GIVEN  a home page with valid request method
        WHEN   the '/' page is requested [GET]
        THEN   check that the response is valid (200) status code is returned
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'Free Tech Books Market' in response.get_data(as_text=True))

    def test_home_page_post(self) -> None:
        """
        GIVEN  a home page with invalid request method
        WHEN   the '/' page is  posted to [POST]
        THEN   check that a (405) status code is returned
        """

        response = self.client.post('/')
        self.assertEqual(response.status_code, 405)

    def test_market_page_get(self) -> None:
        """
        GIVEN  a market page without register
        WHEN   the '/market' page is requested [GET]
        THEN   check that a (302) status code is returned
        """
        response = self.client.get('/market')
        self.assertEqual(response.status_code, 302)

    def test_market_page_post(self) -> None:
        """
        GIVEN  a market page without register and invaild request method
        WHEN   the '/market' page is requested [POST]
        THEN   check that a (405) status code is returned
        """
        response = self.client.post('/market')
        self.assertEqual(response.status_code, 405)

    def test_add_new_book(self) -> None:
        """
        GIVEN  a new book page
        WHEN   the '/newbook' page is requested (POST)
        THEN   check that a (200) status code is returned
        """

        response = self.client.post('/newbook', data=dict(

            name='Learning Web Design',
            author='Niederst Robbins',
            category='Web Development',
            language='html',
            pages=422,
            published=2018,
            link='https://www.pdfdrive.com/learning-web-design-a-beginners-guide-to-html-css-javascript-and-web-graphics-d188549005.html'

        ), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book Market', response.data)

    def test_registeration_page(self) -> None:
        """
        GIVEN  a register page 
        WHEN   the '/register' page is requested [POST]
        THEN   check that a vailed user is registered and (200) status code is returned
        """
        response = self.client.post('/register',
                                    data=dict(
                                        username='amr',
                                        email='amr@example.com',
                                        password1='cat',
                                        password2='cat',
                                    ),
                                    follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book Market', response.data)

    def test_login_page(self) -> None:
        """
        GIVEN  a login page 
        WHEN   the '/login' page is requested [POST]
        THEN   check that a vailed user ingin and (200) status code is returned
        """
        response = self.client.post('/login',
                                    data=dict(
                                        username='amr',
                                        password='cat',
                                    ),
                                    follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book Market', response.data)

    def test_logout_page(self) -> None:
        """
        GIVEN  a logout page 
        WHEN   the '/logout' page is requested
        THEN   check that a vailed user and (200) status code is returned
        """

        response = self.client.get('/logout', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('You were successfully logout!' in response.get_data(
            as_text=True))


if __name__ == "__main__":
    unittest.main()
