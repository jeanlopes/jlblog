# -*- coding: utf-8 -*-
from utils import enum


class AccountModel(object):
    
    def __init__(self):
        self._author = ""
        self._birth = None
        self._about_me = ""
        self._sex = enum.Sex.MALE
        self._occupation = ""
        self._interests = []
        
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        self._author = value
        
    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, value):
        self._birth = value
    
    @property
    def about_me(self):
        return self._about_me
    @about_me.setter
    def about_me(self, value):
        self._about_me = value
        
    @property
    def sex(self):
        return self._sex
    @sex.setter
    def sex(self, value):
        self._sex = value
    
    @property
    def occupation(self):
        return self._occupation
    @occupation.setter
    def occupation(self, value):
        self._occupation = value
        
    @property
    def interests(self):
        return self._interests
    @interests.setter
    def interests(self, value):
        self._interests = value