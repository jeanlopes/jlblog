'''
Created on 30/06/2013

@author: jean
'''

from couchdbkit import Document
from couchdbkit.schema.properties import StringProperty, DateTimeProperty,\
    ListProperty
#import sys
#sys.path.append('/home/jean/workspace/jlblog/domain')
#from application import Context

import datetime
from Entity import Entity


class AccountEntity(Document):
    author = StringProperty()
    birth = DateTimeProperty()
    about_me = StringProperty()
    sex = StringProperty()
    occupation = StringProperty()
    interests = ListProperty()
    username = StringProperty()
    password = StringProperty()
    
class Account(Entity):
        
    def __init__(self, author, birth, about_me, sex, occupation, interests, username, password):                           
        self.entity = AccountEntity(author = author,\
                                    birth = datetime.datetime(birth.year, birth.month, birth.day),  \
                                    about_me = about_me, \
                                    sex = 'Feminino' if sex == True else 'Masculino', \
                                    occupation = occupation, \
                                    interests = interests, \
                                    username = username, \
                                    password = password)        
        super(Account, self).__init__(self.c, self.entity)        
    
    @classmethod
    def get_by_username(cls, username):
        if type(username) != unicode:
            raise NameError('O valor passado deve ser um unicode - Valor passado: ' + str(type(username)))
        
        result = cls.context.db.list('main/entities', 'accounts', key = username)
        doc = AccountEntity.wrap(result)
        doc.id = result.get('_id')

        return doc