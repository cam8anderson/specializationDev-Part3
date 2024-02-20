from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField('username', [validators.input_required()])
    password = PasswordField('password', [validators.input_required()])
