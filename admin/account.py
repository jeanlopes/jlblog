# -*- coding: utf-8 -*-

from flask import request #, session, jsonify, abort
from flask import Blueprint, render_template
#from provider import provider
from Forms import Account
import admin


account = Blueprint('account', __name__, template_folder='../static',static_folder='static')

@account.before_request
def before_request():
    return admin.before_request()


@account.route('/account',defaults={'page': 'account'})
def index(page):
    account = Account.AccountForm(request.form)
    return render_template('admin/%s.html' % page, accountForm = account)

