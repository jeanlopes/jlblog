# -* coding: utf-8 *-

'''
Created on 30/06/2013

@author: jean
'''

from couchdbkit.schema.properties import StringProperty, DateTimeProperty, \
    ListProperty
#import sys
#sys.path.append('/home/jean/workspace/jlblog/domain')
#from application import Context

import datetime
from Entity import Entity


class Account(Entity):

    def __init__(self, author, birth, about_me, sex, occupation, interests, username, password):

        self.author = StringProperty(author)
        self.birth = DateTimeProperty(datetime.datetime(birth.year, birth.month, birth.day))
        self.about_me = StringProperty(about_me)
        self.sex = StringProperty('Feminino' if sex else 'Masculino')
        self.occupation = StringProperty(occupation)
        self.interests = ListProperty(interests)
        self.username = StringProperty(username)
        self.password = StringProperty(password)