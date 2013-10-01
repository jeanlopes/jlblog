# -*- coding: utf-8 -*-
"""
Created on 17/04/2013

@author: jean
"""
import sys
sys.path.append('/home/jean/workspace/jlblog')

from wtforms import Form, TextField, DateField, \
                          TextAreaField, BooleanField
from wtforms.validators import DataRequired
from infra.widgets import listWidget
from wtforms.fields.simple import PasswordField


class AccountModel(Form):
    author = TextField(u'Autor: ',validators = [DataRequired()])
    birth = DateField('Data de Nascimento: ' ,validators = [DataRequired()], format='%Y-%m-%d')
    about_me = TextAreaField('Sobre mim: ',validators = [DataRequired()])
    sex = BooleanField('Sexo: ')
    occupation = TextField(u'Ocupação:',validators = [DataRequired()])
    username = TextField(u'Nome de Usuário:', validators = [DataRequired()])
    password = PasswordField('Senha:', validators = [])
    interests = list()
    

class InterestsList(object):
    
    def __init__(self, **kwargs):
        self.label = 'Interesses: '
        if kwargs.has_key('options'):
            opts = kwargs.pop('options')
        else:
            opts = None
        self.html = listWidget.list_widget(div_class = kwargs.pop('div_class'),\
                                           model = kwargs.pop('model'),\
                                            id_select = kwargs.pop('id_select'),\
                                             options = opts)        
        self.list = opts
