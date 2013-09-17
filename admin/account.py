# -*- coding: utf-8 -*-

#import sys
#sys.path.append('/home/jean/workspace/jlblog')

from flask import request #, session, jsonify, abort
from flask import Blueprint, render_template
from Models import Account as Model
from domain.entities import Account
import admin
from flask.helpers import flash
from flask import session
from domain.entities.Account import AccountEntity
from domain.entities.Entity import Entity
#import pdb

account = Blueprint('account', __name__, template_folder='../static',static_folder='static')

@account.before_request
def before_request():
    return admin.before_request()


@account.route('/account', defaults={'page': 'account'})
def index(page):
    account = Model.AccountModel()
    entity = Entity.get_by_id(session['user'], AccountEntity)
    
    account.about_me.data = entity.about_me
    account.author.data = entity.author
    account.birth.data = entity.birth
    account.about_me.data = entity.about_me
    account.sex.data = True if entity.sex == 'Feminino' else False
    account.occupation.data = entity.occupation
    account.interests = entity.interests.doc
    account.username.data = entity.username
    account.password.data = entity.password    
    
    session['pass'] = account.password.data
    
    selectList = Model.InterestsList(div_class = 'list_interests',\
                                     model = 'interestsListModel',\
                                     id_select = 'interests',
                                     options = account.interests)
    
    return render_template('admin/%s.html' % page, accountForm = account, selectList = selectList )

@account.route('/updateAccount', defaults={'page': 'account'}, methods=['POST'])
def save(page):
    #pdb.set_trace()
    account = Model.AccountModel(request.form)
    account.interests = request.form.getlist('interests')
    
    selectList = Model.InterestsList(div_class = 'list_interests',\
                                     model = 'interestsListModel',\
                                     id_select = 'interests',
                                     options = account.interests)
    
    if account.validate() and len(account.interests) != 0:
        entity = Account.Account(author = account.author.data, \
                         birth = account.birth.data, \
                         about_me = account.about_me.data, \
                         sex = account.sex.data, \
                         occupation = account.occupation.data, \
                         interests = account.interests, \
                         username = account.username.data, \
                         password = account.password.data if len(account.password.data) > 0 else session['pass'])
        
        entity.update(session['user'])
        flash('Seus dados foram atualizados com muito sucesso!')
    else:
        flash(u'O formulário não está válido, verifique erros ou incoerências')
        #flash(account.)
        
    return render_template('admin/%s.html' % page, accountForm = account, selectList = selectList)
