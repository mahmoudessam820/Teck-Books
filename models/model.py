from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView


db = SQLAlchemy()

# ? Models

#! User Model


class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=50), nullable=False, unique=True)
    email = db.Column(db.String(length=255), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=255), nullable=False)

    def __init__(self, username: str, email: str, password_hash: str) -> None:
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def __repr__(self) -> str:
        return f'<username: {self.username}, email: {self.email}, Password: {self.password_hash}>'


#! Books Model

class Books(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=255), nullable=False, unique=True)
    author = db.Column(db.String(length=40), nullable=False, unique=False)
    category = db.Column(db.String(length=40), nullable=False)
    language = db.Column(db.String(length=40), nullable=False)
    pages = db.Column(db.Integer(), nullable=False)
    published = db.Column(db.Integer(), nullable=False)
    link = db.Column(db.String(), nullable=False)

    def __init__(self, name: str, author: str, category: str, language: str, pages: int, published: int, link: str) -> None:
        self.name = name
        self.author = author
        self.category = category
        self.language = language
        self.pages = pages
        self.published = published
        self.link = link

    def __repr__(self) -> str:
        return f"<Book name: {self.name}, author: {self.author}, category: {self.category}, language: {self.language}, pages: {self.pages}, published: {self.published}, link: {self.link}>"


#! Secure Admin Model

class SecureAdminIndexView(AdminIndexView):
    """
        Override the default admin methods to prevent the user
        from accessing the admin page if not authenticated.
    """

    # If the user is authenticated
    def is_accessible(self) -> None:
        if current_user.id == 1 and current_user.username == 'tito':
            return current_user.is_authenticated


class SecureModelView(ModelView):

    def is_accessible(self) -> None:
        if current_user.id == 1 and current_user.username == 'tito':
            return current_user.is_authenticated
