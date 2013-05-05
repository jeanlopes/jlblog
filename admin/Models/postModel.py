# -*- coding: utf-8 -*-
from datetime import date
from utils import enum

class PostModel(object):
    
    def __init__(self):
        self._title = None
        self._subtitle = None
        self._keywords = []
        self._exhibition_data = date.today()
        self._draft = True
        self._date = date.today()
        self._content = ""
        self._author = None
        self._allow_comments = enum.AllowComments.YES
        self._attachments = {}
    
    @property
    def title(self):
        """ Título da página """
        return self._title    
    @title.setter
    def title(self, value):
        self._title = value
    
    
    @property
    def subtitle(self):
        return self._subtitle
    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value
    
    
    @property
    def keywords(self):
        return self._keywords    
    @keywords.setter
    def keywords(self, value):
        self._keywords = value
        
        
    @property
    def exhibition_data(self):
        return self._exhibition_data    
    @exhibition_data.setter
    def exhibition_data(self, value):
        self._exhibition_data = value
        
    
    @property
    def draft(self):
        return self._draft
    @draft.setter
    def draft(self, value):
        self._draft = value

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        self._date = value
    
    @property
    def content(self):
        return self._content
    @content.setter
    def content(self, value):
        self._content = value
    
    