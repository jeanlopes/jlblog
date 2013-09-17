# -* coding: utf-8 *-

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
        
        '''
            se cls possui um "context" a classe Entity foi instanciada, pois a função super foi chamada,
            senão, ela está sendo usada como classe estática e será usado o contexto genérico "c"
        '''
        if hasattr(cls, 'context'):            
            result = cls.context.db.list('main/entities', 'accounts', key = username)
        else:
            result = cls.c.db.list('main/entities', 'accounts', key = username)
        if len(result) == 0:
            return result
        
        doc = AccountEntity.wrap(result)
        doc.id = result.get('_id')

        return doc
    
    
    
    