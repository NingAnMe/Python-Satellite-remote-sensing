# coding:utf-8

from flask import render_template, session, redirect, url_for, current_app

from .. import db
from ..models import User, Post
from . import main


@main.route('/')
def index():
    return render_template('main/index.html')
