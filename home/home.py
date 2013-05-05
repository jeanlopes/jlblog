'''
Created on 18/09/2012

@author: jean
'''
from flask import Blueprint, render_template
from admin.Forms import Login
from flask.globals import request

home = Blueprint('home', __name__, template_folder='../static',static_folder='static')

@home.route('/', defaults={'page': 'home'})
@home.route('/home',defaults={'page': 'home'})
#@home.route('/<page>')
def index(page):
    form = Login.LoginForm(request.form)
    #try:
    teste = ''.join(['Ocupa',u'\u00e7',u'\u00e3','o'])                    
    return render_template('home/%s.html' % page, form = form, teste = teste)
    #except TemplateNotFound:
    #    abort(404)
    