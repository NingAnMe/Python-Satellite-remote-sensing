#! /usr/bin/env python
# coding:utf-8

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from blog import create_app, db
from blog.models import User

# 创建 app
app = create_app('test') # 'production' or 'test'

# 创建脚本管理器
manager = Manager(app)

# 添加 shell 参数，用于调试程序
def make_shell_context():
    return dict(app=app, db=db, User=User,)
manager.add_command('shell', Shell(make_context=make_shell_context))

# 添加 migrate 参数,用于迁移数据库
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# 添加 test 参数，用于启动单元测试
@manager.command
def test():
    '''启动单元测试'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
