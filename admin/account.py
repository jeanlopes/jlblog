# -*- coding: utf-8 -*-

#import sys
#sys.path.append('/home/jean/workspace/jlblog')

from flask import request  # , session, jsonify, abort
from flask import Blueprint, render_template
from Models.Account import AccountModel, InterestsList
from domain.entities.Account import Account
import admin
from flask.helpers import flash
from flask import session
from domain.application.accountService import AccountService
#import pdb

account = Blueprint('account', __name__, template_folder='../static', static_folder='static')


@account.before_request
def before_request():
    return admin.before_request()


@account.route('/account', defaults={'page': 'account'})
def index(page):
    account_model = AccountModel()
    service = AccountService(account=account_model)
    entity = service.get_by_id(session['user'], Account)  # Entity.get_by_id(session['user'], AccountEntity)

    account_model.about_me.data = entity.about_me
    account_model.author.data = entity.author
    account_model.birth.data = entity.birth
    account_model.about_me.data = entity.about_me
    account_model.sex.data = True if entity.sex == 'Feminino' else False
    account_model.occupation.data = entity.occupation
    account_model.interests = entity.interests.doc
    account_model.username.data = entity.username
    account_model.password.data = entity.password

    session['pass'] = account_model.password.data

    select_list = InterestsList(div_class='list_interests',
                                model='interestsListModel',
                                id_select='interests',
                                options=account_model.interests)

    return render_template('admin/%s.html' % page, accountForm=account, selectList=select_list)


@account.route('/updateAccount', defaults={'page': 'account'}, methods=['POST'])
def save(page):
    #pdb.set_trace()
    account_model = AccountModel(request.form)
    account_model.interests = request.form.getlist('interests')

    select_list = InterestsList(div_class='list_interests',
                                model='interestsListModel',
                                id_select='interests',
                                options=account_model.interests)

    if account_model.validate() and len(account_model.interests) != 0:
        entity = Account.Account(author=account_model.author.data,
                                 birth=account_model.birth.data,
                                 about_me=account_model.about_me.data,
                                 sex=account_model.sex.data,
                                 occupation=account_model.occupation.data,
                                 interests=account_model.interests,
                                 username=account_model.username.data,
                                 password=account_model.password.data if len(account_model.password.data) > 0 else
                                 session['pass'])

        entity.update(session['user'])
        flash('Seus dados foram atualizados com muito sucesso!')
    else:
        flash(u'O formulário não está válido, verifique erros ou incoerências')
        #flash(account.)

    return render_template('admin/%s.html' % page, accountForm=account, selectList=select_list)
