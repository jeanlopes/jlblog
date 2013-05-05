# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 19:48:31 2012

@author: jean
"""

import httplib2
import json
#import pdb

class crud:

    http = httplib2.Http()
    db_url = 'http://localhost:5984/jlblog'        
    
    def get(self,
            url = '',
            key = '',
            keys = '',
            limit = '',
            skip = '',
            descending = '',
            startkey = '',
            endkey = ''):
 #       pdb.set_trace()
        resp, content = self.http.request(self.db_url+url,'GET')
        if resp.status == 404:
            return None
        if resp.status == 200:
            return json.loads(content)
    
    def put(self, _id, _rev, data):
        pass
    
    def post(self, data = {}):
        resp, content = self.http.request('http://localhost:5984/jlblog',
                                          'POST',
                                          json.dumps(data),
                                          headers={'Content-Type':'application/json'}
                                          )
        if resp.status == 201:
            return True
        else:
            return resp
        
    def delete(self, _id):
        pass

class provider(crud):
    
    def auth_user(self, user, pwd):
       resp = crud.get(self, url = '/users')
       if resp.has_key(user):
           if str(resp.get(user)) == pwd:
               return True
               
       return False
    
    def get_posts(categories = [],
                  keywords = [],
                  draft = None,
                  author = '',
                  start_date = '',
                  end_date = '',                  
                  limit = 0,
                  skip = 0):
                      #draft = None -> publicados e rascunhos
                      #draft = True -> rascunhos
                      #draft = False -> publicados
                      pass


    def get_post(_id=''):
        pass
    
    def add_post(post = {}):
        pass
    
    def edit_post(_id = '', post = {}):
        pass
    
    def remove_post(_id):
        pass
    
    def remove_posts(_ids):
        pass    
    
    