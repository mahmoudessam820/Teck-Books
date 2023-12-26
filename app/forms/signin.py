from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField)
from wtforms.validators import (Length, EqualTo, Email, DataRequired, ValidationError)


class SigninForm(FlaskForm):
    
    username = StringField(label="User Name*", validators=[Length(min=3, max=50), DataRequired()])
    email = StringField(label="Email*", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password*", validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label="Confirm Password*", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')