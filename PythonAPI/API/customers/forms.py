from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2)])
    password = StringField('Password', validators=[DataRequired(), Length(min=2)])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=2)])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=2)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
