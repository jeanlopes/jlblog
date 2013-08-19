import httplib2
import json

h = httplib2.Http()
resp, content = h.request('http://localhost:5984/jlblog','POST',json.dumps({'oi':1}),headers={'Content-Type':'application/json'})

resp, content = h.request('http://localhost:5984/jlblog/users','GET')
c = json.loads(content)

c.has_key('admin')
c.get('admin')

from couchdbkit import Server

s = Server()
db = s.get_db('jlblog')
db.save_doc(dict(oi=1))
