from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SubmitField)
from wtforms.validators import (DataRequired, URL, Length)


class NewBook(FlaskForm):

    name = StringField(label='Book Name*', validators=[
        Length(min=1, max=100), DataRequired()])

    author = StringField(label='Author*', validators=[
                         Length(min=3, max=60), DataRequired()])

    category = StringField(label='Category*', validators=[
                           Length(min=3, max=60), DataRequired()])

    language = StringField(label='Language*', validators=[
                           Length(min=1, max=40), DataRequired()])

    pages = IntegerField(label='Pages*', validators=[
                         Length(min=1, max=100), DataRequired()])

    published = IntegerField(label='Published*', validators=[
                             Length(min=4, max=4), DataRequired()])

    link = StringField(label='Download link*', validators=[URL()])

    submit = SubmitField(label='Add Book')
