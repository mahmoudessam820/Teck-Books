import uuid
from flask import Response, redirect, url_for
from flask_login import UserMixin, current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView


from app import db, login_manager, admin, bcrypt 

# Models

# Users Model


class Users(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.String(), primary_key=True)
    username = db.Column(db.String(length=50), nullable=False, unique=False)
    email = db.Column(db.String(length=150), nullable=False, unique=True)
    password = db.Column(db.String(length=255), nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    is_staff = db.Column(db.Boolean, default=False, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, **data: dict) -> None:
        self.id = data.get('id')
        self.username = data.get('username')
        self.email = data.get('email')
        self.password = data.get('password')
        self.is_active = data.get('is_active', True)
        self.is_staff = data.get('is_staff', False)
        self.is_admin = data.get('is_admin', False)

    def __repr__(self) -> str:
        return f'<username: {self.username}, email: {self.email}>'

    @classmethod
    def create_admin(cls, **kwargs: dict) -> None:
        password = bcrypt.generate_password_hash(kwargs.get('password1')).decode('utf8')
        admin = cls(
            id = str(uuid.uuid4()),
            username = kwargs.get('username'),
            email = kwargs.get('email'),
            password = password,
            is_admin = True,
            is_staff = True,
            is_active = True
        )
        db.session.add(admin)
        db.session.commit()

    @classmethod 
    def create_user(cls, **kwargs: dict) -> None:
        password = bcrypt.generate_password_hash(kwargs.get('password1')).decode('utf8')
        user = cls(
            id = str(uuid.uuid4()),
            username = kwargs.get('username'),
            email = kwargs.get('email'),
            password = password,
            is_active = True,
            is_staff = False,
            is_admin = False
        )
        db.session.add(user)
        db.session.commit()



# Books Model

class Books(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.String(), primary_key=True)
    title = db.Column(db.String(length=255), nullable=False, unique=True)
    author = db.Column(db.String(length=40), nullable=False, unique=False)
    category = db.Column(db.String(length=40), nullable=False)
    language = db.Column(db.String(length=40), nullable=False)
    pages = db.Column(db.Integer(), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    link = db.Column(db.String(), nullable=False)

    def __init__(self, **data: dict) -> None:
        self.id = data.get('id')
        self.title = data.get('title')
        self.author = data.get('author')
        self.category = data.get('category')
        self.language = data.get('language')
        self.pages = data.get('pages')
        self.year = data.get('year') 
        self.link = data.get('link')

    def __repr__(self) -> str:
        return f"<Book Details: {self.title}, author: {self.author}, category: {self.category}, language: {self.language}, pages: {self.pages}, year: {self.year}, link: {self.link}>"



# Login Manager
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(str(user_id))


class Premissions:
    pass



# Secure admin view

class SecureAdminIndexView(AdminIndexView):
    """
        Override the default admin methods to prevent the user
        from accessing the admin page if not authenticated.
    """

    def is_accessible(self) -> None:
        if current_user.is_authenticated and current_user.is_admin:
            return current_user.is_authenticated


class SecureModelView(ModelView):

    def is_accessible(self) -> None:
        if current_user.is_admin:
            return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs) -> Response:
        # redirect to home page if user doesn't have access
        return redirect(url_for('main.home'))

# Register admin models view
# class UserView(ModelView):
#     pass

# admin.add_view(UserView(Users, db.session))

# class BookView(ModelView):
#     pass

# admin.add_view(BookView(Books, db.session))