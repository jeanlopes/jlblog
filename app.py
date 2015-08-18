# -*- coding: utf-8 -*-
'''
Created on 18/09/2012

@author: jean
'''
from flask import Flask
from home.home import home
from admin.admin import admin
from admin.account import account
from couchdbkit.client import Server
from asq.initiators import query 
#import flask_debugtoolbar

app = Flask(__name__)
app.secret_key = 'parangaricotirimirruaro'
app.register_blueprint(home)
app.register_blueprint(admin)
app.register_blueprint(account)


@app.route('/teste')
def teste():
    s = Server('https://jeanlopes:my_secret_pass@jeanlopes.cloudant.com')
    content = s.all_dbs()
    return query(content).to_str(' -- ')

if __name__ == '__main__':
    app.debug = True
    
    '''
        # Specify the debug panels you want
        app.config['DEBUG_TB_PANELS'] = [
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        # Add the line profiling        
        'flask_debugtoolbar_lineprofilerpanel.panels.LineProfilerPanel'
        ]
        toolbar = flask_debugtoolbar.DebugToolbarExtension(app) '''
    app.run()
