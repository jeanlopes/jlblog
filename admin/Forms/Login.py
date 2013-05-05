# -*- coding: utf-8 -*-

#from flask.ext.wtf import Form, TextField, PasswordField, DataRequired
from wtforms import Form, TextField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    user = TextField('Usu&aacute;rio', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    #userLabel = ''.join(['Usu',u'\u00e1','rio'])
    #passwordLabel = 'Senha'