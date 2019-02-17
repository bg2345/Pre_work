from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask import flash
from app.models import User

class ContactForm(FlaskForm):
    name = StringField('Name: ',
    validators=[DataRequired()])
    phone = StringField('Phone #: ')
    email = StringField('Email: ',
    validators=[DataRequired()])
    message = StringField('Comment: ')
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    username = StringField('Username:', validators=[DataRequired()])
    email = StringField('E-Mail:', validators=[DataRequired(), Email()])
    url = StringField('Website URL:')
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    password2 = PasswordField('Re-type Password:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Sorry but those credentials are already in use.')
            raise ValidationError('Username is already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Sorry but those credentials are already in use.')
            raise ValidationError('E-Mail already used.')
