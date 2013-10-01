# -*- coding: utf-8 -*-

from flask import request, session, jsonify, abort
from flask import Blueprint, render_template
from Models import Login 
from domain.entities import Account
#import pdb

admin = Blueprint('admin', __name__, template_folder='../static', static_folder='static')


@admin.before_request
def before_request():
    if not request.form and not session.get('user'):
        return abort(401)    
    return


@admin.route('/login', methods=['POST'])
def login():
    form = Login.LoginModel(request.form)
    errors = form.errors
    account = None
    if form.validate():
        account = Account.Account.get_by_username(form.user.data)
        if len(account) > 0 and form.password.data == account.password:
            session['user'] = account.id.decode()
            return jsonify(success='true')
        else:
            errors['validação'] = u'Usuário ou Senha inválidos.'
    else:        
        if 'account' in vars() and len(account) == 0 and errors == {}:
            errors['validação'] = u'Usuário não encontrado'
        errors = form.errors          
        
    return jsonify(success='false', errors=errors)


@admin.route('/admin', defaults={'page': 'admin'})
def index(page):
    return render_template('admin/%s.html' % page, form=None)


@admin.route('/admin/create', methods=['POST'])
def create(post):
    pass


@admin.route('/admin/publish', methods=['POST'])
def publish(postId):
    pass


@admin.route('/admin/unpublish', methods=['POST'])
def unpublish(postId):
    pass


@admin.route('/admin/discart', methods=['POST'])
def discart(postId):
    pass


@admin.route('/admin/save', methods=['PUT'])
def save():
    print(request.form)


@admin.route('/admin/openPost', methods=['GET'])
def openPost(postId):
    pass


@admin.route('admin/listPosts', methods=['GET'])
def listPosts():
    pass


