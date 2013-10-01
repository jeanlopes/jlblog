# -*- coding: utf-8 -*-

from flask import request, session, jsonify, abort
from flask import Blueprint, render_template
from Models.Login import LoginModel
from domain.application.accountService import AccountService
from domain.application.postService import PostService
from domain.entities.Post import Post
#import pdb

admin = Blueprint('admin', __name__, template_folder='../static', static_folder='static')
service = PostService()


@admin.before_request
def before_request():
    if not request.form and not session.get('user'):
        return abort(401)    
    return


@admin.route('/login', methods=['POST'])
def login():
    form = LoginModel(request.form)
    errors = form.errors
    account = None
    account_service = AccountService()
    if form.validate():
        account = account_service.get_by_username(form.user.data)  # Account.Account.get_by_username(form.user.data)
        if len(account) > 0 and form.password.data == account.password:
            session['user'] = account.id.decode()
            return jsonify(success='true')
        else:
            errors['validation'] = u'Usuário ou Senha inválidos.'
    else:        
        if 'account' in vars() and len(account) == 0 and errors == {}:
            errors['validation'] = u'Usuário não encontrado'
        errors = form.errors          
        
    return jsonify(success='false', errors=errors)


@admin.route('/admin', defaults={'page': 'admin'})
def index(page):
    return render_template('admin/%s.html' % page, form=None)


@admin.route('/admin/create', methods=['POST'])
def create(post):
    post_service = PostService(post=post)
    _id = post_service.create()
    return jsonify(id=_id)


@admin.route('/admin/publish', methods=['POST'])
def publish(post_id):
    post = service.get_by_id(post_id, Post)
    return jsonify(post=post)


@admin.route('/admin/unpublish', methods=['POST'])
def unpublish(post_id):
    service.set_published(False, post_id)


@admin.route('/admin/discart', methods=['POST'])
def discart(post_id):
    service.delete(_id=post_id)


@admin.route('/admin/save', methods=['PUT'])
def save(post):
    post_service = PostService(post)
    post_service.save()


@admin.route('/admin/openPost', methods=['GET'])
def open_post(post_id):
    return service.get_by_id(post_id, Post)


@admin.route('admin/listPosts', methods=['GET'])
def list_posts():
    return service.list()


