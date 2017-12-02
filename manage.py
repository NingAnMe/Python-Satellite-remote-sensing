#! /usr/bin/env python
# coding:utf-8

from flask_script import Manager, Shell

from blog import create_app, db
from blog.models import User

app = create_app()
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User,)


manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
