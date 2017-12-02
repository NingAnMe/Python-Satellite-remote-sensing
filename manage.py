#! /usr/bin/env python
# coding:utf-8

from flask_script import Manager, Shell

from blog import create_app, db
from blog.models import User

# 创建 app
app = create_app('test')

# 创建脚本管理器
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User,)

# 添加 shell 参数，用于调试程序
manager.add_command('shell', Shell(make_context=make_shell_context))

# 添加 test 参数，用于启动单元测试
@manager.command
def test():
    '''启动单元测试'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
