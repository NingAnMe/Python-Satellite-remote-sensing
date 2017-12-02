# coding:utf-8
'''blog程序的登录模块
'''

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
