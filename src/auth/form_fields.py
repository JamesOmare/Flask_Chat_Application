from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from ..models.user import User

class RegistrationForm(FlaskForm):
    """Registration Form"""
    
    username = StringField('username_label', 
                validators=[InputRequired(message='Username required'),
                Length(min=4, max=25, message='Username must be between 4 and 25 characters')])

    password = PasswordField('password_label',
                validators=[InputRequired(message='Password required'), 
                Length(min=5, message='Password must not be less than five characters')])

    confirm_pass = PasswordField('confirm_pass_label',
                validators=[InputRequired(message='Password Required'), 
                EqualTo('password', message='Passwords must match')])

    submit_btn = SubmitField('Create')

    # # Adding custom validators
    # def validate_username(self, username):
    #     user_exists = User.query.filte_by(username = username.data).first()
    #     if user_exists:
    #         raise ValidationError('Username already exists, select another one.')

class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField('username_label', 
                validators=[InputRequired(message='Username required')])

    password = PasswordField('password_label',
                validators=[InputRequired(message='Password required')])

    submit_btn = SubmitField('Login')