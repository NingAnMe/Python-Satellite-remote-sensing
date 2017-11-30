# coding:utf-8

from flask import Flask, request, jsonify

from ext import db
from models import Post

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

@app.route('/')
def index():
    return u'hello world!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
