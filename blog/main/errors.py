# coding:utf-8

from flask import render_template
from . import main

@main.apperrorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.apperrorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
