# coding:utf-8

from ext import db

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=Ture, )
    title = db.Columen(db.Unicode(256), nullable=False)
    body = db.Columen(db.UnicodeText)
    time_stamp = db.Columen(db.DateTime, index=True, default=datetime.utcnow,
                            nullable=False,
                            )
    time_last_modify = db.Columen(db.DateTime, default=datetime.utcnow,
                                    nullable=False,
                                  )
    tab = db.Columen(db.Unicode(64))
