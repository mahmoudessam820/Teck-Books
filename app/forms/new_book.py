from flask_wtf import FlaskForm 
from wtforms import (StringField, SubmitField, IntegerField)
from wtforms.validators import (DataRequired, URL)


class NewBookForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    author = StringField(label="Author", validators=[DataRequired()])
    category = StringField(label="Category", validators=[DataRequired()])
    language = StringField(label="Language", validators=[DataRequired()])
    pages = IntegerField(label="Pages", validators=[DataRequired()])
    year = IntegerField(label="Year", validators=[DataRequired()])
    link = StringField(label="Link", validators=[URL(), DataRequired()])
    submit = SubmitField(label='Add Book')