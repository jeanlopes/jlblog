'''
Created on 18/09/2012

@author: jean
'''
from flask import Flask
from home.home import home
from admin.admin import admin
from admin.account import account
from couchdbkit import Server

app = Flask(__name__)
app.secret_key = 'parangaricotirimirruaro'
app.register_blueprint(home)
app.register_blueprint(admin)
app.register_blueprint(account)

@app.route('/teste')
def teste():
    s = Server('https://jeanlopes:fp87694fbr@jeanlopes.cloudant.com')
    content = s.all_dbs()
    return content[0]

if __name__ == '__main__':
    app.run(debug=True)
