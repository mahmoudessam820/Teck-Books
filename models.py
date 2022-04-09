from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

#! Establish connections with database
db = SQLAlchemy()


# ? Models


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=50), nullable=False, unique=True)
    email = db.Column(db.String(length=255), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=255), nullable=False)

    def __repr__(self):
        return f'<username: {self.username}, email: {self.email}, Password: {self.password_hash}>'


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=255), nullable=False, unique=True)
    author = db.Column(db.String(length=40), nullable=False, unique=True)
    category = db.Column(db.String(length=40), nullable=False)
    language = db.Column(db.String(length=40), nullable=False)
    pages = db.Column(db.Integer(), nullable=False)
    published = db.Column(db.Integer(), nullable=False)
    link = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Book name: {self.name}, author: {self.author}, category: {self.category}, language: {self.language}, pages: {self.pages}, puplished: {self.puplished}, link: {self.link}>"
