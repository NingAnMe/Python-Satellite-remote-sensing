# coding:utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(1, 64),])
    password = PasswordField('密码', validators=[Required(), Length(1, 64)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')

class InitForm(FlaskForm):
    '''
    初始化 Blog
    '''
    username = StringField('用户名', validators=[Required(), Length(1, 64),])
    password = PasswordField('密码', validators=[Required(), Length(1, 64),])
    submit = SubmitField('初始化')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Already Inited blog.')
