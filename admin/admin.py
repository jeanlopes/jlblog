# -*- coding: utf-8 -*-

from flask import request, session, jsonify, abort
from flask import Blueprint, render_template
from Models import Login 
from domain.entities import Account
#import pdb

admin = Blueprint('admin', __name__, template_folder='../static',static_folder='static')


@admin.before_request
def before_request():
    if not request.form and not session['user']:        
        return abort(401)    
    return


@admin.route('/login',defaults={'page': 'login'}, methods=['POST'])
def login(page):
    #pdb.set_trace()
    form = Login.LoginModel(request.form)
    errors = form.errors
    if form.validate():
        account = Account.Account.get_by_username(form.user.data)
        if  len(account) > 0 and form.password.data == account.password:            
            session['user'] = account.id
            return jsonify(success='true')
        else:
            errors['correctData'] = u'Usuário ou Senha inválidos.'
    else:        
        if len(account) == 0 and errors == {}:
            errors['correctData'] = u'Usuário não encontrado'                    
        
        return jsonify(success='false', errors = errors)


@admin.route('/admin',defaults={'page': 'admin'})
def index(page):
    return render_template('admin/%s.html' % page, form = None)


@admin.route('/admin/save', methods=['POST'])
def save():
    print(request.form);
