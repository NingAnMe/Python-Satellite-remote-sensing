# coding:utf-8

from flask import Flask, request, jsonify


from .. import db
from ..models import Post
from . import main


@main.route('/')
def index():
    return u'hello world!'
