# -*- coding: utf-8 -*-

#from flask.ext.wtf import Form, TextField, PasswordField, DataRequired
from wtforms import Form, TextField, PasswordField
from wtforms.validators import DataRequired

class LoginModel(Form):
    user = TextField('Usu&aacute;rio', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    