'''
Created on 05/06/2013

@author: jean
'''

from couchdbkit.client import Server
from asq.initiators import query 


class Context(object):
        #producao server = Server('https://jeanlopes:fp87694fbr@jeanlopes.cloudant.com')
        def __init__(self):
            self.server = Server('http://192.168.56.101:5984')
            self.db = self.server.get_db('jlblog')
