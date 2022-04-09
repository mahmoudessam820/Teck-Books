from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, IntegerField)
from wtforms.validators import (
    Length, EqualTo, Email, DataRequired, ValidationError, URL)
from models import User


class RegisterForm(FlaskForm):
    #! Custom validator
    def validate_username(self, username_exist):
        user = User.query.filter_by(username=username_exist.data).first()
        if user:
            raise ValidationError('Username already exist!!!')

    def validate_email(self, email_exist):
        email = User.query.filter_by(email=email_exist.data).first()
        if email:
            raise ValidationError('Email already exist!!!')

    username = StringField(label='User Name', validators=[
        Length(min=3, max=50), DataRequired()])
    email = StringField(label='Email Address', validators=[
        Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[
        Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[
        EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='LogIn')


class AddBook(FlaskForm):
    name = StringField(label='Book Name', validators=[
                       Length(min=3, max=100), DataRequired()])
    author = StringField(label='Author', validators=[
                         Length(min=3, max=50), DataRequired()])
    category = StringField(label='Category', validators=[
        Length(min=3, max=50), DataRequired()])
    language = StringField(label='language', validators=[
                           Length(min=2, max=30), DataRequired()])
    pages = IntegerField(label='Pages', validators=[DataRequired()])
    published = IntegerField(label='Published', validators=[DataRequired()])
    link = StringField(label='Download link', validators=[URL()])
    submit = SubmitField(label='Add Book')
