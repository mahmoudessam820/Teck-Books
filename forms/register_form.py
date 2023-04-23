from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField)
from wtforms.validators import (
    Length, EqualTo, Email, DataRequired, ValidationError)
from models.model import User


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

    username = StringField(label='User Name*', validators=[
        Length(min=3, max=50), DataRequired()])

    email = StringField(label='Email Address*', validators=[
        Email(), DataRequired()])

    password1 = PasswordField(label='Password*', validators=[
        Length(min=6), DataRequired()])

    password2 = PasswordField(label='Confirm Password*', validators=[
        EqualTo('password1'), DataRequired()])

    submit = SubmitField(label='Create Account')
