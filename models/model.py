
from flask_login import UserMixin, current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView


from app import db, login_manager, admin

# ? Models

#! User Model


class Users(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.String(), primary_key=True)
    username = db.Column(db.String(length=50), nullable=False, unique=False)
    email = db.Column(db.String(length=150), nullable=False, unique=True)
    password = db.Column(db.String(length=255), nullable=False)

    def __init__(self, **data: dict) -> None:
        self.id = data.get('id')
        self.username = data.get('username')
        self.email = data.get('email')
        self.password = data.get('password')

    def __repr__(self) -> str:
        return f'<username: {self.username}, email: {self.email}, password: {self.password}>'


#! Books Model

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


# Admin Views
class UserView(ModelView):
    pass

admin.add_view(UserView(Users, db.session))

class BookView(ModelView):
    pass

admin.add_view(BookView(Books, db.session))





