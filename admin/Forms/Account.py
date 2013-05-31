# -*- coding: utf-8 -*-
'''
Created on 17/04/2013

@author: jean
'''
from wtforms import Form, TextField, DateField, \
                          TextAreaField, IntegerField
from wtforms.validators import DataRequired
from infra.widgets import listWidget

class AccountForm(Form):
    author = TextField(u'Autor: ',validators = [DataRequired()])
    birth = DateField('Data de Nascimento: ' ,validators = [DataRequired()], format='%Y-%m-%d %H:%M:%S')
    about_me = TextAreaField('Sobre mim: ',validators = [DataRequired()])
    sex = IntegerField('Sexo: ',validators = [DataRequired()])
    occupation = TextField(u'Ocupação:',validators = [DataRequired])
    def interests(self):
        pass
    interests.label = 'Interesses: '
    interests.html = listWidget.list_widget(div_class = 'list_interests', model = 'interestsListModel', id_select = 'interests')
    