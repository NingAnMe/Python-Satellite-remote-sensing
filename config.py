# coding:utf-8

'''全局常量
'''

class Config(object):
    HOSTNAME = 'localhost'
    DATABASE = 'blog'
    USERNAME = 'blog'
    PASSWORD = 'blog'
    DB_URI = 'mysql://{}:{}@{}/{}'.format(
            USERNAME, PASSWORD, HOSTNAME, DATABASE,)

    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass
