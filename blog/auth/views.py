# coding:utf-8

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user

from . import auth
from ..models import User
from .. import db
from .forms import LoginForm, InitForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # 如果 WTF 验证通过
        # 验证账号密码
        pass
        # 返回主页
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', form=form)

@auth.route('/init', methods=['GET', 'POST'])
def init():
    form = InitForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You init the blog.')
        return redirect(url_for('auth.login'))
    return render_template('auth/init.html', form=form)
