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
