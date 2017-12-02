# coding:utf-8

from flask import Flask, request, jsonify


from .. import db
from ..models import Post
from . import main


@main.route('/')
def index():
    return u'hello world!'

@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', posts=[post])

@main.route('/login', methods['GET', 'POST'])
def login():
    pass

@main.route('/add', methods['GET', 'POST'])
def add_post():
    return render_template('add_post.html', form=form)
