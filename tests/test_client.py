from tests.conftest import app


def test_app_exists():
    """
    GIVEN a flask instance that can be used to test the existence instance of a flask
    WHEN  a flask instance is created and initialized 
    THEN  check that the instance exists
    """

    assert app is not None


def test_home_page_get(client):
    """
    GIVEN a home page with valid request method
    WHEN the '/' page is requested [GET]
    THEN check that the response is valid (200) status code is returned
    """

    response = client.get('/')
    assert response.status_code == 200
    assert 'Free Tech Books Market' in response.get_data(as_text=True)


def test_home_page_post(client):
    """
    GIVEN a home page with invalid request method
    WHEN the '/' page is posted to [POST]
    THEN check that a (405) status code is returned
    """

    response = client.post('/')
    assert response.status_code == 405


def test_market_page_get(client):
    """
    GIVEN a market page without register
    WHEN the '/market' page is requested [GET]
    THEN check that a (302) status code is returned
    """
    response = client.get('/market')
    assert response.status_code == 302


def test_market_page_post(client):
    """
    GIVEN  a market page without register and invaild request method
    WHEN   the '/market' page is requested [POST]
    THEN   check that a (405) status code is returned
    """

    response = client.post('/market')
    assert response.status_code == 405

