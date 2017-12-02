# coding:utf-8

from flask import render_template

from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')
