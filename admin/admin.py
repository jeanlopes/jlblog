# -*- coding: utf-8 -*-

from flask import request, session, jsonify, abort
from flask import Blueprint, render_template
from JLBlogProvider import JLBlogProvider
from Models import postModel
from Forms import Login
import pdb

admin = Blueprint('admin', __name__, template_folder='../static',static_folder='static')

provider = JLBlogProvider.provider()

@admin.before_request
def before_request():
    if not request.form and not session.get('user'):
        #print 'list is empty'
        return abort(401)
    #else:
        #print 'session.get(user)' #   print session.get('user')
    return


@admin.route('/login',defaults={'page': 'login'}, methods=['POST'])
def login(page):
    #pdb.set_trace()
    form = Login.LoginForm(request.form)
    auth = provider.auth_user(form['user'].data, form['password'].data)
    if form.validate() and auth:
        session['user'] = True
        print 'validou'
        return jsonify(success='true')
    else:
        print 'nao validou'
        errors = form.errors
        if not auth and errors == {}:
            errors['correctData'] = 'Usuario ou Senha invalidos'
                   
        return jsonify(success='false', errors = errors)



@admin.route('/admin',defaults={'page': 'admin'})
def index(page):
    return render_template('admin/%s.html' % page, form = None)


@admin.route('/admin/save', methods=['POST'])
def save():
    print(request.form);
