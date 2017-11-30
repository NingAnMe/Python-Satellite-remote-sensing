# coding:utf-8

'''全局常量
'''

HOSTNAME = 'localhost'
DATABASE = 'blog'
USERNAME = 'blog'
PASSWORD = 'blog'
DB_URI = 'mysql://{}:{}@{}/{}'.format(
        USERNAME, PASSWORD, HOSTNAME, DATABASE,)
