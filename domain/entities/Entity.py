# -*- coding:utf-8 -*-

'''
Created on 22/07/2013

@author: jean
'''
from couchdbkit import Document
from couchdbkit.ext.django.schema import BooleanProperty


class Entity(Document):
    deleted = BooleanProperty()