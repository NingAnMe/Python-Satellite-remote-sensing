# coding:utf-8

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user

from . import auth
from ..models import User
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # 如果 WTF 验证通过
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', form=form)
