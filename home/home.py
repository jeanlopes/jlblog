'''
Created on 18/09/2012

@author: jean
'''
from flask import Blueprint, render_template
from admin.Models import Login
from flask.globals import request
from flask_debugtoolbar_lineprofilerpanel.profile import line_profile

from flask_debugtoolbar.panels.logger import logging


home = Blueprint('home', __name__, template_folder='../static',static_folder='static')


@line_profile
@home.route('/', defaults={'page': 'home'})
@home.route('/home',defaults={'page': 'home'})
#@home.route('/<page>')
def index(page):
    
    logging.fatal('babababa')
    logging.critical('critico')
    logging.error('erro')
    logging.warn('perigo')
    form = Login.LoginModel(request.form)    
    #try:    
    return render_template('home/%s.html' % page, form = form)
    #except TemplateNotFound:
    #    abort(404)