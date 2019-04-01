"""
forms.py
~~~~~~~~
Creating html forms using flask_wtf
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    """
    Creates a Flask Registration Form.
    """
    # create a username with a min length of 2
    #  and a max of 20
    username = StringField(
        'Username', validators=[DataRequired(),
        Length(min=2, max=20)]
    )

    # user email
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )

    # password required
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )

    # confirm password
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')]
    )

    # submit field
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    """
    Creates a Flask Login Form.
    """
    # user email
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )

    # password required
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    # remember field
    remeber = BooleanField('Remember Me')

    # submit field
    submit = SubmitField('Login')
