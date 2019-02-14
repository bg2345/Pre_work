from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name: ',
    validators=[DataRequired()])
    phone = StringField('Phone #: ')
    email = StringField('Email: ',
    validators=[DataRequired()])
    message = StringField('Comment: ')
    submit = SubmitField('Submit')
