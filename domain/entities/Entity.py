# -*- coding:utf-8 -*-
from domain.application import Context
'''
Created on 22/07/2013

@author: jean
'''
from couchdbkit.schema.base import Document

class Entity(object):
    '''
    Classe que implementa métodos básicos a todas as entidades
    '''
    c = Context()            
    
    def __init__(self, context, entity):
        self.context = context
        self.entity = entity
        self.entity.set_db(self.c.db)
    
    
    def update(self, _id):

        doc = self.entity.get(_id, db = self.c.db)
        for g in self.entity.items():
            doc[g[0]] = g[1]
        doc.save()
    
    
    def save(self):
        self.entity.save()
    
    @classmethod
    def get_by_id(cls, _id, MyEntity):
                
        assert MyEntity.__class__ == Document.__class__
                
        if type(_id) != unicode:
            raise NameError('O valor passado deve ser um unicode - Valor passado: ' + str(type(_id)))
        
        return MyEntity.get(_id, db = cls.c.db)    