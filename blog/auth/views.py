# coding:utf-8

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user

from . import auth
from ..models import User
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)
