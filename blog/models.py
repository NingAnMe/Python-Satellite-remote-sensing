# coding:utf-8

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from . import db
from . import login_manager


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    title = db.Column(db.String(256), nullable=False,)
    tab = db.Column(db.String(64),)
    body = db.Column(db.Text,)
    time_stamp = db.Column(db.DateTime, index=True, default=datetime.utcnow,
                           nullable=False,
                           )
    time_last_modify = db.Column(db.DateTime, default=datetime.utcnow,
                                nullable=False,
                                )


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    username = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        '''用户认证方法
        '''
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    '''加载用户的回调函数
    '''
    return User.query.get(int(user_id))
