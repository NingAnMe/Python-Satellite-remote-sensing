# coding:utf-8
'''blog程序主模块
'''

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
