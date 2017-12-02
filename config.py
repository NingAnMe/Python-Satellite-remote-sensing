# coding:utf-8

'''全局常量
'''

class Config(object):
    # 数据库信息
    HOSTNAME = 'localhost'
    DATABASE = 'blog'
    USERNAME = 'blog'
    PASSWORD = 'blog'
    DB_URI = 'mysql://{}:{}@{}/{}'.format(
            USERNAME, PASSWORD, HOSTNAME, DATABASE,)

    # SQLAlchemy配置信息
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 是否开启DEBUG模式
    DEBUG = True

    # 初始化APP
    @staticmethod
    def init_app(app):
        pass
