# coding:utf-8

from flask import Flask, request, jsonify

from . import main
from .. import db
from .. models import Post

@main.route('/')
def index():
    return u'hello world!'
