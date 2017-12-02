# coding:utf-8

import unittest

from flask import current_app
from blog import create_app, db

class DatabaseTestCase(unittest.TestCase):
    '''数据库相关测试
    '''
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_existes(self):
        self.assertFalse(current_app is None)
