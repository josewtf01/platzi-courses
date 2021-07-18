from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, SubmitField)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()] )
    password = PasswordField('Password', validators=[DataRequired()] )
    submit = SubmitField('Send')

class BookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    submit = SubmitField('Add Book')

class DeleteBookForm(FlaskForm):
    submit = SubmitField('Delete')

class UpdateBookForm(FlaskForm):
    submit = SubmitField('Update')
