# coding:utf-8

from datetime import datetime
from . import db

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
    title = db.Column(db.Unicode(256), nullable=False,)
    body = db.Column(db.UnicodeText,)
    time_stamp = db.Column(db.DateTime, index=True, default=datetime.utcnow,
                            nullable=False,
                            )
    time_last_modify = db.Column(db.DateTime, default=datetime.utcnow,
                                    nullable=False,
                                  )
    tab = db.Column(db.Unicode(64),)
