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
        pass
        # db.session.remove()
        # db.drop_all()
        # self.app_context.pop()


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
        WHEN   the '/' page is requested (GET)
        THEN   check that the response is valid (200) status code is returned
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            'Free Tech Books Market' in response.get_data(as_text=True))

    def test_home_page_post(self) -> None:
        """
        GIVEN  a home page with invalid request method
        WHEN   the '/' page is  posted to (POST)
        THEN   check that a (405) status code is returned
        """

        response = self.client.post('/')
        self.assertEqual(response.status_code, 405)

    def test_market_page_get(self) -> None:
        """
        GIVEN  a market page without register
        WHEN   the '/market' page is requested (GET)
        THEN   check that a (302) status code is returned
        """
        response = self.client.get('/market')
        self.assertEqual(response.status_code, 302)

    def test_market_page_post(self) -> None:
        """
        GIVEN  a market page without register and invaild request method
        WHEN   the '/market' page is requested (POST)
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

        response = self.client.post('/newbook', follow_redirects=True)

        b = Books(
            name='Learning Web Design',
            author='Niederst Robbins',
            category='Web Development',
            language='html',
            pages=422,
            published=2018,
            link='https://www.pdfdrive.com/learning-web-design-a-beginners-guide-to-html-css-javascript-and-web-graphics-d188549005.html'
        )

        db.session.add(b)
        db.session.commit()

        book_exist = Books.query.filter_by(
            name='Learning Web Design').first()

        self.assertIsNotNone(book_exist)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
