# coding:utf-8

import unittest

from blog.models import User


class UserModelTestCase(unittest.TestCase):
    '''密码散列化测试
    '''
    def test_password_setter(self):
        u = User(password='blog')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='blog')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='blog')
        self.assertTrue(u.verify_password('blog'))
        self.assertFalse(u.verify_password('web'))

    def test_password_salts_are_random(self):
        u = User(password='blog')
        u2 = User(password='blog')
        self.assertTrue(u.password_hash != u2.password_hash)
