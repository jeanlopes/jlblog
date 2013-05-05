# -*- coding: utf-8 -*-
'''
Created on 17/04/2013

@author: jean
'''
from wtforms import Form, TextField, DateField, \
                          TextAreaField, IntegerField
from wtforms.validators import DataRequired
from infra.widgets.listWidget import list_widget

class AccountForm(Form):
    author = TextField('Autor',validators = [DataRequired()])
    birh = DateField('Data de Nascimento' ,validators = [DataRequired()], format='%Y-%m-%d %H:%M:%S')
    about_me = TextAreaField('Sobre mim',validators = [DataRequired()])
    sex = IntegerField('Sexo',validators = [DataRequired()])
    occupation = TextField(''.join(['Ocupa',u'\u00e7',u'\u00e3','o']),validators = [DataRequired])
    interests = list_widget(model = 'InterestsListModel', id_select = "Interests", div_class = "div_interests")
    