#! /usr/bin/env python
# coding:utf-8

from blog import create_app
from flask_script import Manager

app = create_app()
app.app_context().push()

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
