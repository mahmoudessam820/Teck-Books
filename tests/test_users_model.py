from models.model import Users


def test_create_admin_user(app):
    """
    Test the creation of an admin user in the application.

    Parameters:
    - app (Flask): The Flask application instance.

    This method creates an admin user with specified credentials,
    adds it to the Users table in the database, and then queries the
    database to ensure that the admin user was created successfully.

    It asserts that the properties of the retrieved admin user match the expected values,
    including username, email, is_admin, is_active, and is_staff.

    Raises:
    - AssertionError: If any of the assertions fail.
    """

    with app.app_context():

        Users.create_admin(
            username='admin',
            email='admin@example.com', 
            password1='adminpassword'
        )

        query_set = Users.query.all()

        assert query_set[0].username == 'admin'
        assert query_set[0].email == 'admin@example.com'
        assert query_set[0].is_admin is True
        assert query_set[0].is_active is True
        assert query_set[0].is_staff is True



def test_signin_regular_user(app):
    """
    Test the sign-in process for a regular user in the application.

    Parameters:
    - app (Flask): The Flask application instance.

    This method creates a regular user with specified credentials,
    adds it to the Users table in the database, and then queries the
    database to ensure that the regular user was created successfully.

    It asserts that the properties of the retrieved regular user match the expected values,
    including username, email, is_active, is_staff, and is_admin.

    Raises:
    - AssertionError: If any of the assertions fail.
    """

    with app.app_context():

        Users.create_user(
            username='user',
            email='user@example.com',
            password1='userpassword'
        )

        query_set = Users.query.all()

        assert query_set[1].username == 'user'
        assert query_set[1].email == 'user@example.com'
        assert query_set[1].is_active == True
        assert query_set[1].is_staff == False 
        assert query_set[1].is_admin == False 


