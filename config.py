# coding:utf-8

'''全局常量
'''

class Config(object):
    # SQLAlchemy 配置信息
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-WTF 需要的密钥
    SECRET_KEY = 'please dont to guess this'

    # 初始化 APP
    @staticmethod
    def init_app(app):
        pass

class BlogConfig(Config):
        # 数据库信息
        HOSTNAME = 'localhost'
        DATABASE = 'blog'
        USERNAME = 'blog'
        PASSWORD = 'blog'
        DB_URI = 'mysql://{}:{}@{}/{}'.format(
                USERNAME, PASSWORD, HOSTNAME, DATABASE,)
        SQLALCHEMY_DATABASE_URI = DB_URI

        # 是否开启DEBUG模式
        DEBUG = False

class TestConfig(Config):
        # 数据库信息
        HOSTNAME = 'localhost'
        DATABASE = 'test'
        USERNAME = 'test'
        PASSWORD = 'test'
        DB_URI = 'mysql://{}:{}@{}/{}'.format(
                USERNAME, PASSWORD, HOSTNAME, DATABASE,)
        SQLALCHEMY_DATABASE_URI = DB_URI

        # 是否开启DEBUG模式
        DEBUG = True

config = {
        'production': BlogConfig,
        'test': TestConfig,
    }
