# coding:utf-8

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length


class LoginForm(Form):
    username = StringField('用户名'， validators=[Required(), Length(1, 32),])
    password = PasswordField('密码', validators=[Required(), Length(1, 64)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')
